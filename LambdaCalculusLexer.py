# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write(">\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\6\4!\n\4\r\4\16\4\"\3\5\6\5&\n\5\r\5")
        buf.write("\16\5\'\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\6\r9\n\r\r\r\16\r:\3\r\3\r\2\2\16\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\3\2\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2@\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35")
        buf.write("\3\2\2\2\7 \3\2\2\2\t%\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2")
        buf.write("\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25\63\3\2\2\2\27")
        buf.write("\65\3\2\2\2\318\3\2\2\2\33\34\7\60\2\2\34\4\3\2\2\2\35")
        buf.write("\36\7\'\2\2\36\6\3\2\2\2\37!\t\2\2\2 \37\3\2\2\2!\"\3")
        buf.write("\2\2\2\" \3\2\2\2\"#\3\2\2\2#\b\3\2\2\2$&\t\3\2\2%$\3")
        buf.write("\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\n\3\2\2\2)*\7")
        buf.write("-\2\2*\f\3\2\2\2+,\7/\2\2,\16\3\2\2\2-.\7,\2\2.\20\3\2")
        buf.write("\2\2/\60\7\61\2\2\60\22\3\2\2\2\61\62\7`\2\2\62\24\3\2")
        buf.write("\2\2\63\64\7*\2\2\64\26\3\2\2\2\65\66\7+\2\2\66\30\3\2")
        buf.write("\2\2\679\t\4\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2")
        buf.write("\2\2;<\3\2\2\2<=\b\r\2\2=\32\3\2\2\2\6\2\"\':\3\b\2\2")
        return buf.getvalue()


class LambdaCalculusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    VARIABLE = 3
    NUMBER = 4
    ADD = 5
    SUBTRACT = 6
    MULTIPLY = 7
    DIVIDE = 8
    POWER = 9
    LBRACKET = 10
    RBRACKET = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'%'", "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "VARIABLE", "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
            "POWER", "LBRACKET", "RBRACKET", "WS" ]

    ruleNames = [ "T__0", "T__1", "VARIABLE", "NUMBER", "ADD", "SUBTRACT", 
                  "MULTIPLY", "DIVIDE", "POWER", "LBRACKET", "RBRACKET", 
                  "WS" ]

    grammarFileName = "LambdaCalculus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


