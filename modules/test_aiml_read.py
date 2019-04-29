#Autor: Leonardo Sartori
#Contact: leonardogt4@hotmail.com

from aiml_read import readAiml
aiml = readAiml()

try:
    print(type(aiml.response("COMPUTER")))
except:
    print('etst')
