from flask import Flask, request
app = Flask(__name__)

import spacy
from collections import Counter
from string import punctuation

nlp = spacy.load("en_core_web_lg")

def get_hotwords(text):
    result = []
    
    #keyword identification
    pos_tag = ['PROPN', 'ADJ', 'NOUN']
    doc = nlp(text.lower())
    formatted = ""

    #Looping through sentence to find keywords
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            result.append(token.text)

    #Formatting the output to come up with hashtags
    for i in range(len(result)):
        formatted += ('#' + result[i] + ' ')

    #Printing out results as output
    return (formatted)

@app.route('/testroute') 
def test():
    sentence = request.get_json()
    print(sentence)


@app.route('/gethashtags') 
def getTags():
    sentenceList = []
    repeat = 'y'

    #Looping to ask multiple sentences
    while(repeat == 'y'):
        sentenceList.append(input("Sentence to create hashtags. "))
        repeat = input("repeat? ")

    #Getting outputs
    for sent in sentenceList:
        output = get_hotwords(sent)
        print(output)
