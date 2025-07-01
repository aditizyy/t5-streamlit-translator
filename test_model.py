from transformers import pipeline
#T5 model
generator = pipeline("text2text-generation", model="t5-small")

# Format input: T5 expects a "task prefix" like "translate English to French: ..."
input_text = "translate English to French: The house is wonderful."

output = generator(input_text, max_length=50, num_return_sequences=1)

print("Generated Output:")
print(output[0]['generated_text'])
