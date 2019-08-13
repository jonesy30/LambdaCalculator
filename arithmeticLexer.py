# Generated from arithmetic.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("g\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\6\2%\n\2\r\2\16")
        buf.write("\2&\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3D\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\21\6\21b\n\21\r\21\16\21c\3")
        buf.write("\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\5\3\2\62")
        buf.write(";\4\2C\\c|\5\2\13\f\17\17\"\"\2m\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\3$\3\2\2\2\5C\3\2\2\2\7E\3\2\2\2\tG")
        buf.write("\3\2\2\2\13I\3\2\2\2\rK\3\2\2\2\17M\3\2\2\2\21O\3\2\2")
        buf.write("\2\23Q\3\2\2\2\25S\3\2\2\2\27U\3\2\2\2\31W\3\2\2\2\33")
        buf.write("Y\3\2\2\2\35[\3\2\2\2\37]\3\2\2\2!a\3\2\2\2#%\t\2\2\2")
        buf.write("$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\4\3\2\2\2")
        buf.write("()\7V\2\2)*\7T\2\2*+\7W\2\2+D\7G\2\2,-\7v\2\2-.\7t\2\2")
        buf.write("./\7w\2\2/D\7g\2\2\60\61\7V\2\2\61\62\7t\2\2\62\63\7w")
        buf.write("\2\2\63D\7g\2\2\64\65\7H\2\2\65\66\7C\2\2\66\67\7N\2\2")
        buf.write("\678\7U\2\28D\7G\2\29:\7h\2\2:;\7c\2\2;<\7n\2\2<=\7u\2")
        buf.write("\2=D\7g\2\2>?\7H\2\2?@\7c\2\2@A\7n\2\2AB\7u\2\2BD\7g\2")
        buf.write("\2C(\3\2\2\2C,\3\2\2\2C\60\3\2\2\2C\64\3\2\2\2C9\3\2\2")
        buf.write("\2C>\3\2\2\2D\6\3\2\2\2EF\t\3\2\2F\b\3\2\2\2GH\7-\2\2")
        buf.write("H\n\3\2\2\2IJ\7/\2\2J\f\3\2\2\2KL\7,\2\2L\16\3\2\2\2M")
        buf.write("N\7\61\2\2N\20\3\2\2\2OP\7`\2\2P\22\3\2\2\2QR\7*\2\2R")
        buf.write("\24\3\2\2\2ST\7+\2\2T\26\3\2\2\2UV\7(\2\2V\30\3\2\2\2")
        buf.write("WX\7~\2\2X\32\3\2\2\2YZ\7@\2\2Z\34\3\2\2\2[\\\7>\2\2\\")
        buf.write("\36\3\2\2\2]^\7?\2\2^_\7?\2\2_ \3\2\2\2`b\t\4\2\2a`\3")
        buf.write("\2\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2de\3\2\2\2ef\b\21")
        buf.write("\2\2f\"\3\2\2\2\6\2&Cc\3\b\2\2")
        return buf.getvalue()


class arithmeticLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    BOOL = 2
    VARIABLE = 3
    ADD = 4
    SUBTRACT = 5
    MULTIPLY = 6
    DIVIDE = 7
    POWER = 8
    LBRACKET = 9
    RBRACKET = 10
    AND = 11
    OR = 12
    GT = 13
    LT = 14
    EQ = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'", "'&'", "'|'", 
            "'>'", "'<'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "BOOL", "VARIABLE", "ADD", "SUBTRACT", "MULTIPLY", 
            "DIVIDE", "POWER", "LBRACKET", "RBRACKET", "AND", "OR", "GT", 
            "LT", "EQ", "WS" ]

    ruleNames = [ "NUMBER", "BOOL", "VARIABLE", "ADD", "SUBTRACT", "MULTIPLY", 
                  "DIVIDE", "POWER", "LBRACKET", "RBRACKET", "AND", "OR", 
                  "GT", "LT", "EQ", "WS" ]

    grammarFileName = "arithmetic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


