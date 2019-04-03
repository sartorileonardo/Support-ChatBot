# coding: utf-8

import nltk
import warnings
from nltk.corpus import stopwords
warnings.filterwarnings("ignore")
import numpy as np
import random
import string

language='portuguese'

f=open('vars/chatbot.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
nltk.download('punkt')
nltk.download('rslp')
nltk.download('stopwords')

sent_tokens = nltk.sent_tokenize(raw, language=language)
word_tokens = nltk.word_tokenize(raw, language=language)
#sent_tokens[:2]
#word_tokens[:5]


def LemTokens(tokens):
    #lemmer = nltk.stem.WordNetLemmatizer()
    lemmer = nltk.stem.RSLPStemmer()
#    return [lemmer.lemmatize(token) for token in tokens]
    return [lemmer.stem(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))




def greeting(sentence):
    GREETING_INPUTS = ("ola", "oi", "saudações", "sup", "tudo bem","hey")
    GREETING_RESPONSES = [ "oi {{user}}, em que posso ajudar?"]

    for word in sentence.lower().split():
        if word.decode('utf-8').lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=stopwords.words(language))
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"lamento! Eu não te entendo... :("
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

def parole(text):
    ret=""
    user_response = text
    user_response=user_response.lower()

    if(user_response!='tchau'):
        if(user_response=='obrigado'):
            ret = "ROBO: Voce é bem vindo.."
        else:
            if(greeting(user_response)!=None):

                ret = "ROBO: "+greeting(user_response)
            else:

                ret = "ROBO: "+response(user_response)
                sent_tokens.remove(user_response)

    else:
        pret = "ROBO:Falou!.."
    return ret