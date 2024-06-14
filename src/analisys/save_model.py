from transformers import AutoModelForTokenClassification, AutoTokenizer
import os

model_checkpoint = r".\results\checkpoint-7188"
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

output_dir = r".\test\saved_model"

# Create folder if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the model and tokenizer
model.save_model(output_dir)
tokenizer.save_pretrained(output_dir)