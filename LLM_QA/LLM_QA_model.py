import json
import string

#Loading Q&A data
with open("LLM_QA/Sample_QA.json", "r") as file:
    qa_data = json.load(file)

#Need to define a function that correctly retrieves answer for a specified function
def get_answer(question):
    #Need to normalize user input so that it ignores capitalization and punctuation
    normalized_input = question.lower().translate(str.maketrans("","", string.punctuation))
    for q, a in qa_data.items():
        #Have to normalize our Q
        normalized_q = q.lower().translate(str.maketrans("","", string.punctuation)) #.lower to convert both to lower case and increase chances of matching
        if normalized_input == normalized_q:
            return a
    return "I don't know, please ask a staff member."
    
#In the future, the robot will have a US sensor that triggers the response when user walks in range
print("Hi, I'm a Katbot who can help answer any questions you have about the space. Do you have any questions?")

while True:
    question = input("You: ")
    if question.lower() == "no":
        print("Ok, please let me know if you do!")
        break
#Following runs when 'False' aka user has a Q
    answer = get_answer(question)
    print("Katbot:", answer)
