import openai
import os

# Securely load the API key from the environment
# set opne ai key as enviorment variable so I dont have to hard code it 
openai.api_key = os.getenv("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")

def chat_with_hendrix(prompt):
    try:
        #accesing librabry 
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("Ask Hendrix: ")
        if user_input.lower() in ['exit', 'stop', 'quit']:
            break
        response = chat_with_hendrix(user_input)
        print("Hendrix:", response)

