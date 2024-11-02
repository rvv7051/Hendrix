import openai
import os

# Securely load the API key from the environment
# set opne ai key as enviorment variable so I dont have to hard code it 
# i made my api key an enviormental variable so i dont have to hard code it
openai.api_key = os.getenv("OPENAI_API_KEY")
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

