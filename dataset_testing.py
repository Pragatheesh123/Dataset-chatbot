import pandas as pd
import ollama

# Load dataset
df = pd.read_csv(r"C:\Users\pragatheesh.senthil\Desktop\Datasets\New folder\dataset.txt.csv")

print("Dataset loaded successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("You can now ask questions about the dataset.")
print("Type 'exit' to stop.\n")


# Give the model information about the dataset
dataset_info = f"""
Dataset columns:
{list(df.columns)}

Data types:
{df.dtypes.to_string()}

First 5 rows:
{df.head().to_string(index=False)}
"""


while True:

    question = input("You: ")

    if question.lower().strip() == "exit":
        print("Goodbye!")
        break

    # Ask Qwen to generate the required Pandas analysis
    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "system",
                "content": f"""
You are an expert Python data analyst.

You are working with a pandas DataFrame called df.

Here is information about the dataset:

{dataset_info}

Your job is to analyze the user's question and determine
what Pandas operation is required to answer it.

Rules:

1. Use ONLY the information available in df.
2. Generate ONE Python/Pandas expression that calculates the answer.
3. The expression must use the DataFrame named df.
4. Do not invent values.
5. Do not use external information.
6. Do not use print().
7. Do not create variables.
8. Return ONLY the Python expression.
9. If grouping, filtering, sorting, counting, averaging,
   summing, finding maximum/minimum, ranking, or date analysis
   is required, use appropriate Pandas operations.
10. The expression must return the answer to the user's question.

User's question:
{question}
"""
            }
        ]
    )

    pandas_code = response.message.content.strip()

    # Remove markdown code fences if Qwen adds them
    pandas_code = pandas_code.replace("```python", "")
    pandas_code = pandas_code.replace("```", "")
    pandas_code = pandas_code.strip()

    print("\nAnalysis:", pandas_code)

    try:

        # Execute the generated Pandas expression
        result = eval(
            pandas_code,
            {
                "df": df,
                "pd": pd
            }
        )

        # Ask Qwen to explain the result
        final_response = ollama.chat(
            model="qwen3:4b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are a data analysis assistant.

Answer the user's question using the calculated result provided.

Rules:
- Do not invent information.
- Use only the calculated result.
- Give a clear and concise answer.
- If the result is a number, format it appropriately.
"""
                },
                {
                    "role": "user",
                    "content": f"""
Question:
{question}

Calculated result:
{result}

Give the final answer.
"""
                }
            ]
        )

        print("\nAI:", final_response.message.content)
        print()

    except Exception as e:

        print("\nI couldn't calculate that question.")
        print("Generated analysis:", pandas_code)
        print("Error:", e)
        print()