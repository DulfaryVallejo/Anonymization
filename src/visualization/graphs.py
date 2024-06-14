import seaborn as sns
import os
from collections import Counter

import matplotlib.pyplot as plt

import sys


current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "src")
sys.path.append(src_dir)
from preprocessing.preprocess import XMLProcessor

dir_path = r'.\data\raw'
xml_files = [archivo for archivo in os.listdir(dir_path) if archivo.endswith('.xml')]

processor = XMLProcessor(dir_path)

all_text = ""
all_tags = []
for xml_file in xml_files:
    route_xml = os.path.join(dir_path, xml_file)
    text, list_tags = processor.get_data_from_xml(route_xml)
    all_text += text
    all_tags.extend(list_tags)

import seaborn as sns
from collections import Counter

entity_tags = [tupla[1] for tupla in all_tags]
tag_freq = Counter(entity_tags)

tags = list(tag_freq.keys())
frequencies = list(tag_freq.values())

plt.figure(figsize=(10, 6))
sns.barplot(x=tags, y=frequencies)
plt.xlabel('Tags')
plt.ylabel('Frequency')
plt.title('Fig. 3. Tag Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

for i, freq in enumerate(frequencies):
    plt.text(i, freq, str(freq), ha='center', va='bottom')

# Guardar la imagen en la misma carpeta
output_path = os.path.join(os.path.dirname(__file__), 'tag_frequency_plot.png')
plt.savefig(output_path)

plt.show()