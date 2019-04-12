
import aiml

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("vars/std-startup.xml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
k.respond("load aiml b")

# Loop forever, reading user input from the command
# line and printing responses.

# TODO: test with support.aiml, alter aiml repository and connect with flask web server 
while True: print(k.respond(input("> ").upper()))
