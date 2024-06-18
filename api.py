import google.generativeai as genai

api_key = input("API Key: ")

genai.configure(api_key=api_key)

PROMPT = "You are an AI search query generator. The user will put in a question, and you will generate a list of search queries that will return the answer to the question."

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

chat_session = model.start_chat(history=[])


def send_question(question):
  if question != "":
    response = chat_session.send_message(PROMPT + question)
    print(response.text)
