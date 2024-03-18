import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

with open('pack_1_parsed.txt', 'r') as f:
    content = f.readlines()

tuple_list = []  # Create an empty list to store the tuples

for line in content:
    parts = line.strip().split("|")  # Split each line by the "|" character
    if len(parts) == 2:
        tuple_list.append((parts[0].strip(' '), parts[1].strip(' ')))  # Create a tuple and add it to the list

# 'tuple_list' now contains the desired tuples.
questions = [tup[0] for tup in tuple_list][:10]
question_string = " ".join(questions)


def answer_questions(questions):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Here are trivia questions. Please answer each one."},
            {"role": "user", "content": f"Here are the questions: {questions}"},
            {"role": "user", "content": "Please just respond with the answer, no need to include the question."}
        ]
    )
    answers = response['choices'][0]['message']['content']
    return answers


print(answer_questions(question_string))
