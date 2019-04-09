#Autor: Andrei A. Ribeiro
import aiml
import os

def read_aiml():
    os.chdir(os.getcwd()+'/vars')
    ai = aiml.Kernel()
    ai.learn('std-startup.xml')
    ai.respond('load aiml b')
