import openai
import PyPDF2
import re
import tiktoken

# Set up OpenAI API credentials
openai.api_key = "yout-key"

model = 'gpt-3.5-turbo'

ppt = .002/1000

# Load PDF file
pdf_file = open('Algo_21_22_TD8_fonctions.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from PDF
text = ""
for page in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[page].extract_text()

def remove_numbers_after_newlines(text):
    return re.sub(r'(\n)\d+', r'\1', text)

# Search for text that matches the pattern
matchesraw = re.findall('(?s)\"{3}(.*?)\"{3}',text)

matches = [remove_numbers_after_newlines(m) for m in matchesraw]

# Loop through each matched text and create a separate function for each one
function_code = ""
prompt = [{"role": "system", "content": "You are to create python functions from the provided docstrings (in french). Do not write any explanations, introductions, comments, nor special formatting. Give the functions as if they were to appear in a python file, ready to be used. Each message corresponds to a docstring, so write each function in a different message"}]

for i, match in enumerate(matches):
    # Use OpenAI API to obtain completion response

    prompt.append({"role": "user", "content": match})

    
# Write all functions to Python file
with open("functions.py", "w", encoding='utf-8') as file:
    file.write(function_code)

print("Python file written successfully!")
print(f'Used {prompt_tokens} prompt tokens and {completion_tokens} completiong tokens.')
print(f'Approximate cost: ${ppt*(prompt_tokens+completion_tokens)}')
