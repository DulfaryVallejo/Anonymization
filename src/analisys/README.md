# Training Model for Named Entity Recognition (NER)

This project demonstrates how to train a Named Entity Recognition (NER) model using the `transformers` library from Hugging Face and a preprocessed dataset in pickle format.

## Repository Contents

- `train_ner_model.py`: Contains the Python code to train the NER model.
- `data/processed/data_ner_an.pkl`: Preprocessed dataset in pickle format.
- `results/`: Folder where training results and evaluation metrics will be saved.
- `README.md`: This file containing the project documentation.

## Steps to Train the Model

1. **Data Preparation**
   - Load the dataset from the `data_ner_an.pkl` file.
   - Tokenize the sentences and align the entity labels with the tokens.

   Although the data was previously tokenized, it was tokenized at the word level, so it is necessary to organize the input according to the model's requirements to perform the tokenization correctly.
   After data preparation, the distribution is as follows:
   DatasetDict({
    train: Dataset({
        features: ['id', 'tokens', 'ner_tags_bio', 'ner_tags'],
        num_rows: 19167
    })
    validation: Dataset({
        features: ['id', 'tokens', 'ner_tags_bio', 'ner_tags'],
        num_rows: 6389
    })
    test: Dataset({
        features: ['id', 'tokens', 'ner_tags_bio', 'ner_tags'],
        num_rows: 6389
    })
   })

2. **Model and Tokenizer Setup**
   - Use the pretrained checkpoint `PlanTL-GOB-ES/roberta-large-bne-capitel-ner` from Hugging Face.
   - Configure the label encoding and map the labels to numeric identifiers.

3. **Dataset Splitting**
   - Split the dataset into training, validation, and test sets.

4. **Tokenization and Label Alignment**
   - Tokenize the sentences and align the entity labels with the tokens.

5. **Model Training**
   - Set up training arguments and initialize the `Trainer` to train the model.

6. **Evaluation and Metrics**
   - Evaluate the model on the validation set and calculate evaluation metrics.

7. **Metrics Storage**
   - Save the evaluation metrics to a CSV file.

## Running the Code

1. Open the `train_ner_model.py` file in a compatible Python environment.
2. Execute the script to start training the model.
3. The results will be saved in the `results` folder.
