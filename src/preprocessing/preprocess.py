from lxml import etree
import os
import nltk
from nltk.tokenize import sent_tokenize, RegexpTokenizer
nltk.download('punkt')
import pickle as pk

class XMLProcessor:

    """
    A class to process XML files for NLP tasks.

    Attributes
    ----------
    dir_path : str
        The path to the directory containing XML files.
    datahc : dict
        A dictionary to store processed data.
    tree : lxml.etree._ElementTree
        The parsed XML tree.

    Methods
    -------
    get_data_from_xml(doc_name)
        Parses the XML document and extracts text and annotations.
    tokenize(corpus)
        Tokenizes the input text into sentences and words.
    calculate_word_index(input_text, sentences)
        Calculates the start and end indices of each word in the text.
    bio_label(word_idx, listt)
        Labels the words with BIO tags based on the annotations.
    """
    def __init__(self, dir_path):
        """
        Initializes the XMLProcessor with the specified directory path.

        Parameters
        ----------
        dir_path : str
            The path to the directory containing XML files.
        """
        self.dir_path = dir_path
        self.datahc = {}
        self.tree = None  # Variable para almacenar el árbol XML

    def get_data_from_xml(self, doc_name):

        """
        Parses the XML document and extracts text and annotations.

        Parameters
        ----------
        doc_name : str
            The name of the XML document to be processed.

        Returns
        -------
        tuple
            A tuple containing the patient text and a list of annotations.
        """

        if self.tree is None:
            self.tree = etree.parse(doc_name)
        root = self.tree.getroot()

        patient_text = root.find('TEXT').text
        listt = []
        tags = root.find('TAGS')
        for tag in tags:
            begin_span = tag.get('start')
            end_span = tag.get('end')
            concept = tag.tag#('tYPE')  # tag.tag general concept. ie LOCATION
            text = tag.get('text').split()
            listt.append((text, concept, [begin_span, end_span]))

        return patient_text, listt

    def tokenize(self, corpus):

        """
        Tokenizes the input text into sentences and words.

        Parameters
        ----------
        corpus : str
            The input text to be tokenized.

        Returns
        -------
        list
            A list of lists, where each sublist contains the tokens of a sentence.
        """
        list_lines_tokens = []
        sentences = sent_tokenize(corpus)
        tokenizer = RegexpTokenizer(
            "[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}|[\d\w]+[ªº°]|[A-Za-z0-9]*[\d[\.\,]*\d]*\%?[A-Za-zá-ú]*|[^\w\s]|[\w]+")
        for sentence in sentences:
            list_lines_tokens.append(tokenizer.tokenize(sentence))

        return list_lines_tokens

    def calculate_word_index(self, input_text, sentences):

        """
        Calculates the start and end indices of each word in the text.

        Parameters
        ----------
        input_text : str
            The original input text.
        sentences : list
            A list of tokenized sentences.

        Returns
        -------
        list
            A list of lists, where each sublist contains tuples of words and their start and end indices.
        """
        sentence_index = []
        initial_index = 0

        for sentence in sentences:
            word_index = []
            for word in sentence:
                start_index = input_text.find(word, initial_index)
                end_index = start_index + len(word)
                word_index.append((word, start_index, end_index))
                initial_index = end_index
            sentence_index.append(word_index)
        return sentence_index

    def bio_label(self, word_idx, listt):

        """
        Labels the words with BIO tags based on the annotations.

        Parameters
        ----------
        word_idx : list
            A list of lists, where each sublist contains tuples of words and their start and end indices.
        listt : list
            A list of annotations.

        Returns
        -------
        list
            A list of lists, where each sublist contains BIO labels for the corresponding sentence.
        """
        output = []

        for list_tupla in word_idx:
            pseudo_output = ['O'] * len(list_tupla)
            for i, tuple_def in enumerate(list_tupla):
                for words_annot, concept, [begin_token, end_token] in listt:
                    if tuple_def[0] in words_annot and (
                            int(begin_token) <= tuple_def[1] < tuple_def[2] <= int(end_token)):
                        pseudo_output[i] = 'B-' + concept if tuple_def[0] == words_annot[0] else 'I-' + concept
                        break

            output.append(pseudo_output)

        return output

class FileProcessor(XMLProcessor):

    """
    A class to process XML files containing patient data and convert them to tokenized and labeled format for NLP tasks.

    Inherits from:
        XMLProcessor: A base class that provides methods to process XML data.

    Attributes:
        dir_path (str): The directory path containing the XML files.
        datahc (dict): A dictionary to store the processed data for each XML file.

    Methods:
        process_files():
            Processes each XML file in the directory, extracting patient text and annotations,
            tokenizing the text, and generating BIO labels. The results are stored in the `datahc` attribute.
    """

    def __init__(self, dir_path):
        super().__init__(dir_path)

    def process_files(self):

        """
        Processes each XML file in the directory. Extracts patient text and annotations from the XML,
        tokenizes the text, calculates word indices, and generates BIO labels. The processed data is stored
        in the `datahc` dictionary with the file names as keys.

        The dictionary structure is:
        datahc[xml_file][i] = {'sentences': input_data[i], 'labels': output_data[i]}
        where xml_file is the name of the processed XML file, and i is the index of the sentence.
        """
        xml_files = [archivo for archivo in os.listdir(self.dir_path) if archivo.endswith('.xml')]

        for xml_file in xml_files:
            route_xml = os.path.join(self.dir_path, xml_file)

            patient_text, listt = self.get_data_from_xml(route_xml)
            input_data = self.tokenize(patient_text)
            word_index_raw = self.calculate_word_index(patient_text, input_data)
            output_data = self.bio_label(word_index_raw, listt)

            self.datahc[xml_file] = {}
            for i in range(len(input_data)):
                self.datahc[xml_file][i] = {'sentences': input_data[i], 'labels': output_data[i]}

            self.tree = None


dir_path = r'.\data\raw'
processor = FileProcessor(dir_path)
processor.process_files()

file_path = r".\data\processed\data_ner_an.pkl"
file_dir = os.path.dirname(file_path)
if not os.path.exists(file_dir):
    os.makedirs(file_dir)

# Save processed data to a pickle file
with open(file_path, 'wb') as file:
    pk.dump(processor.datahc, file)