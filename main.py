
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("text", data_files="njala.txt")

dataset.push_to_hub("njala")
