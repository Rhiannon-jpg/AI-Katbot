import json
import string
from sentence_transformers import SentenceTransformer, util

#Loading Q&A data
with open("LLM_QA/Sample_QA.json", "r") as file:
    qa_data = json.load(file)

#Get model
model = SentenceTransformer("all-MiniLM-L6-v2")

#Create normalization function
def normalize(text):
     return text.lower().translate(str.maketrans("","", string.punctuation)).strip()

#Make embeddings of JSON Qs
questions = list(qa_data.keys())
normalized_qs = [normalize(q) for q in questions]
q_embeddings = model.encode(normalized_qs, convert_to_tensor=True)

#Need to define a function that correctly retrieves answer for a specified function
def get_answer(user_input):
    norm_input = normalize(user_input)
    input_embedding = model.encode(norm_input, convert_to_tensor=True)

    #Generate similarities between pre-trained and user input
    similarities = util.pytorch_cos_sim(input_embedding, q_embeddings)

    #Find the best similarity in embeddings
    best_match = similarities.argmax()
    best_answer = questions[best_match]

    return qa_data[best_answer]

#Main Loop
print("Hi, I'm a Katbot who can help answer any questions you have about the space. Do you have any questions?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "no":
        print("Ok, please let me know if you do!")
        break
#Following runs when 'False' aka user has a Q
    answer = get_answer(user_input)
    print("Katbot:", answer)
