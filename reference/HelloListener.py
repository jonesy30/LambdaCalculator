# Generated from Hello.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#hi.
    def enterHi(self, ctx:HelloParser.HiContext):
        pass

    # Exit a parse tree produced by HelloParser#hi.
    def exitHi(self, ctx:HelloParser.HiContext):
        pass


