import openai
import json


with open('creds.json', 'r') as f:
    cred = json.load(f)


openai.api_key = cred["api_key"]

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # print(response)
    return response.choices[0].text.strip()

# Example usage

name = input("Please enter your name: ")
print("Hello, " + name + "!")

command = input("What would you like to ask ChatGPT3.5 ")

if len(command) != 0:
    generated_text = generate_text(command)
    print(generated_text)