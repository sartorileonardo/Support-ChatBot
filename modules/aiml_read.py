
#Autor: Leonardo Sartori
#Contact: leonardogt4@hotmail.com

import aiml

class readAiml():

    def __init__(self):	
        # The Kernel object is the public interface to
        # the AIML interpreter.
        self.k = aiml.Kernel()

        # Use the 'learn' method to load the contents
        # of an AIML file into the Kernel.
        self.k.learn("vars/std-startup.xml")

        # Use the 'respond' method to compute the response
        # to a user's input string.  respond() returns
        # the interpreter's response, which in this case
        # we ignore.
        self.k.respond("load aiml b")

    def response(self, message):
        # Reading user input from the command
        # line and printing responses.

        # TODO: test with support.aiml, alter aiml repository and connect with flask web server 
        return self.k.respond(message)