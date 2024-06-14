# MEDDOCAN Corpus

## Overview

The MEDDOCAN corpus is a synthetic clinical dataset with unstructured data, featuring a gold standard annotation for anonymizing medical documents in Spanish. It comprises precisely 1000 clinical cases segmented as follows:

- Train set: 500 cases
- Development set: 250 cases
- Test set: 250 cases

The MEDDOCAN corpus is available in plain text format encoded in UTF-8, with each clinical case saved as a standalone text file (.txt). Additionally, PII annotations are provided in BRAT format (.ann) and XML format (.xml), which include both the clinical text and annotations. In this case only XML files are used.

## Raw Data

The `raw data` folder contains the XML files of the MEDDOCAN corpus. This corpus includes a total of 33 thousand sentences, averaging around 33 sentences per case. The dataset contains around 495 thousand words, with each clinical case containing an average of 494 words. The content of each case includes sensitive information such as patient names, identification numbers, addresses, medical conditions, treatments, and other personal details.


## Processed Data

The `processed` folder contains the Electronic Health Records (EHR) processed in a .pkl file. This file contains each clinical history divided by sentences and their respective bio tags or labels.

## Usage

The primary use case of the MEDDOCAN corpus is to evaluate the performance of deep learning algorithms in automatically detecting and anonymizing Personally Identifiable Information (PII) within clinical documents. Researchers can leverage the annotated dataset to train and test models for de-identification, assess their accuracy, and refine algorithms to enhance data privacy in healthcare settings.



Database reference: Marimon, M., Gonzalez-Agirre, A., Intxaurrondo, A., Rodriguez, H., Lopez Martin, J., Villegas, M., & Krallinger, M. (2019). Automatic De-identification of Medical Texts in Spanish: the MEDDOCAN Track, Corpus, Guidelines, Methods and Evaluation of Results. En IberLEF@SEPLN.
