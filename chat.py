from nltk_utils import tokenize, stem, bag_of_words
import pickle
import random
import json


with open("intents.json","r") as f:
    intents = json.load(f)

modelone = pickle.load(open("models/Model V1.pkl","rb"))
all_words = pickle.load(open("wordlist/words.pkl","rb"))


#def bot_response(input):

 #   features = bag_of_words(tokenize(input),all_words)

  #  tag = modelone.predict([features])

   # for intent in intents['intents']:
    #    if tag == intent['tag']:
     #       output = random.choice(intent['responses'])
        
    #return output
def bot_response(input):
    features = bag_of_words(tokenize(input), all_words)
    tag = modelone.predict([features])#[0]  # Use [0] to get the first element of the array

    for intent in intents['intents']:
        if tag == intent['tag']:
            output = random.choice(intent['responses'])
            return output  # Return the response if it matches the main tag
        #elif 'subtags' in intent:
         #       for subtag in intent['subtags']:
          #          if tag == subtag['tag']:
           #             output = random.choice(subtag['responses'])
            #            return output  # Return the response if it matches a subtag

    return "I'm sorry, I'm not sure how to respond to that."  # Default response if no match is found

