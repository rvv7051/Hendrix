# command i for copilot to generate the code 
import openai

openai.api_key = "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"

#hendrix chat 
def chat_with_hendrix(prompt):
    response = openai.Completion.create(
      engine="davinci-codex",
      prompt=prompt,
      max_tokens=150
    )
    return response.choices[0].text.strip()

