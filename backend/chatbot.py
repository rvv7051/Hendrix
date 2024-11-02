from flask import Flask, jsonify, request
import openai
import os


app = Flask(__name__)
# Securely load the API key from the environment
# set opne ai key as enviorment variable so I dont have to hard code it 
# i made my api key an enviormental variable so i dont have to hard code it
openai.api_key = os.getenv("OPENAI_API_KEY")
@app.route('/api/chat_with_hendrix', methods=['GET'])
def chat_with_hendrix():
    try:
        prompt = request.args.get('prompt')
        #accesing librabry 
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return jsonify({"message":response.choices[0].message['content'].strip()})
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    #while True:
        #user_input = input("Ask Hendrix: ")
       # if user_input.lower() in ['exit', 'stop', 'quit']:
         #   break
        #response = chat_with_hendrix(user_input)
        #print("Hendrix:", response)
    app.run(debug=True)

