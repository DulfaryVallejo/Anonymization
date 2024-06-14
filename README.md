# Anonymization of Electronic Health Records

A part of the thesis project focuses on the anonymization of electronic health records. This is due to the significant research opportunities presented by this data, especially with the current interest in leveraging narrative free text from EHR to develop predictive algorithms for patient stratification and personalized healthcare. However, sharing and accessing this clinical text for research purposes face severe constraints due to the inclusion of Personally Identifiable Information (PII), which may identify specific individuals. Regulations such as the United States Health Insurance Portability and Accountability Act (HIPAA) mandate the removal of re-identifying information from medical records to uphold patient confidentiality.

However, one of the challenges is the lack of labeled data in Spanish, which led to the use of the meddocan database. The primary use case of the MEDDOCAN corpus is to evaluate the performance of deep learning algorithms in automatically detecting and anonymizing PII within clinical documents. By leveraging the annotated dataset, researchers can train and test models for de-identification, assess their accuracy, and refine algorithms to enhance data privacy in healthcare settings.

## MEDDOCAN Corpus

The MEDDOCAN corpus is an annotated dataset designed to evaluate and improve algorithms for identifying and de-identifying PHI in clinical documents. It consists of 1,000 re-sampled clinical cases, totaling 33,000 sentences and approximately 495,000 words. Each clinical case includes sensitive information such as patient names, identification numbers, addresses, medical conditions, treatments, and other personal details. The corpus was annotated in standoff format and is available in UTF-8 plain text, with each clinical case in an individual text file (.txt) and the PHI annotations in BRAT format (.ann). Additionally, it is available in XML format (.xml), which includes both the clinical text and the annotations.

The XML files underwent preprocessing in Python, during which annotations were extracted. Table \ref{table:1} displays the PHI Tags, which refer to the general data types in which entities can be grouped, along with Entities and the frequency of annotations. Subsequently, each medical record was tokenized at the word level, and BIO tagging was performed for entity recognition.

## Why Use Transfer Learning?

By leveraging pretrained models, the computational and data effort required to train models for specific tasks is drastically reduced. Additionally, the prior knowledge captured in general models improves performance and generalization capabilities, accelerating the development of effective solutions. This technique is especially valuable in scenarios where resources are limited or obtaining labeled data is costly, enabling the creation of more robust and efficient models.

### Model: Pretrained "PlanTL-GOB-ES/roberta-large-bne-capitel-ner"

=======
# Anonymization of Electronic Health Records

A part of the thesis project focuses on the anonymization of electronic health records. This is due to the significant research opportunities presented by this data, especially with the current interest in leveraging narrative free text from EHR to develop predictive algorithms for patient stratification and personalized healthcare. However, sharing and accessing this clinical text for research purposes face severe constraints due to the inclusion of Personally Identifiable Information (PII), which may identify specific individuals. Regulations such as the United States Health Insurance Portability and Accountability Act (HIPAA) mandate the removal of re-identifying information from medical records to uphold patient confidentiality.

However, one of the challenges is the lack of labeled data in Spanish, which led to the use of the meddocan database. The primary use case of the MEDDOCAN corpus is to evaluate the performance of deep learning algorithms in automatically detecting and anonymizing PII within clinical documents. By leveraging the annotated dataset, researchers can train and test models for de-identification, assess their accuracy, and refine algorithms to enhance data privacy in healthcare settings.

## MEDDOCAN Corpus

The MEDDOCAN corpus is an annotated dataset designed to evaluate and improve algorithms for identifying and de-identifying PHI in clinical documents. It consists of 1,000 re-sampled clinical cases, totaling 33,000 sentences and approximately 495,000 words. Each clinical case includes sensitive information such as patient names, identification numbers, addresses, medical conditions, treatments, and other personal details. The corpus was annotated in standoff format and is available in UTF-8 plain text, with each clinical case in an individual text file (.txt) and the PHI annotations in BRAT format (.ann). Additionally, it is available in XML format (.xml), which includes both the clinical text and the annotations.

The XML files underwent preprocessing in Python, during which annotations were extracted. Table \ref{table:1} displays the PHI Tags, which refer to the general data types in which entities can be grouped, along with Entities and the frequency of annotations. Subsequently, each medical record was tokenized at the word level, and BIO tagging was performed for entity recognition.

## Why Use Transfer Learning?

By leveraging pretrained models, the computational and data effort required to train models for specific tasks is drastically reduced. Additionally, the prior knowledge captured in general models improves performance and generalization capabilities, accelerating the development of effective solutions. This technique is especially valuable in scenarios where resources are limited or obtaining labeled data is costly, enabling the creation of more robust and efficient models.

### Model: Pretrained "PlanTL-GOB-ES/roberta-large-bne-capitel-ner"

This model was selected for its direct relevance to the task of Named Entity Recognition (NER). Specifically designed and trained for this task, it possesses a deep understanding of the structure and semantics of entities in the text, which can translate into superior performance in NER tasks. Additionally, being pretrained, it benefits from broad prior knowledge gained during training on a variety of texts, generally improving its ability to tackle specific tasks such as NER. In summary, the choice of this model is based on its suitability and previous experience in NER tasks, which can result in better performance and effectiveness for this particular application.
