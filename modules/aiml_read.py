
import aiml

class AimlRead():

    def __init__(self):
        # The Kernel object is the public interface to
        # the AIML interpreter.
        k = aiml.Kernel()

        # Use the 'learn' method to load the contents
        # of an AIML file into the Kernel.
        k.learn("../vars/std-startup.xml")

        # Use the 'respond' method to compute the response
        # to a user's input string.  respond() returns
        # the interpreter's response, which in this case
        # we ignore.
        k.respond("load aiml b")
        self.k = k
        return True

    def response_aiml(self, text_message):
        return self.k.respond(text_messase))


