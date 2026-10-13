# Dataset Chatbot

A simple Python chatbot that answers questions about a sales dataset. It uses pandas to work with the data and Ollama's `qwen3:4b` model to understand questions and explain results.

## What it does

- Loads `dataset.txt.csv` into a pandas DataFrame.
- Lets you ask questions about the data in the terminal.
- Calculates an answer using pandas and displays a short explanation.

## Requirements

- Python
- Ollama, with the `qwen3:4b` model downloaded
- The Python packages `pandas` and `ollama`

Install the packages with:

```bash
pip install pandas ollama
```

To download the model, run:

```bash
ollama pull qwen3:4b
```

## Run the chatbot

Make sure Ollama is running. In `dataset_testing.py`, update the CSV file path if the project folder is somewhere other than the path set in the script. Then run:

```bash
python dataset_testing.py
```

Type a question when prompted. Type `exit` to close the chatbot.

## Examples

See [examples.md](./examples.md) for sample questions, pandas analyses, and answers.

## Note

The chatbot uses AI-generated pandas code to calculate answers. Run it only with data and questions you trust.
