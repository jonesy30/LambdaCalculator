# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\6\b\64\n")
        buf.write("\b\r\b\16\b\65\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\3\20\6\20G\n\20\r\20\16\20H\3\20")
        buf.write("\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21\3\2\5\4\2C\\c|\3\2")
        buf.write("\62;\5\2\13\f\17\17\"\"\2M\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13,\3\2")
        buf.write("\2\2\r\60\3\2\2\2\17\63\3\2\2\2\21\67\3\2\2\2\239\3\2")
        buf.write("\2\2\25;\3\2\2\2\27=\3\2\2\2\31?\3\2\2\2\33A\3\2\2\2\35")
        buf.write("C\3\2\2\2\37F\3\2\2\2!\"\7\60\2\2\"\4\3\2\2\2#$\7\'\2")
        buf.write("\2$\6\3\2\2\2%&\7<\2\2&\b\3\2\2\2\'(\7D\2\2()\7q\2\2)")
        buf.write("*\7q\2\2*+\7n\2\2+\n\3\2\2\2,-\7K\2\2-.\7p\2\2./\7v\2")
        buf.write("\2/\f\3\2\2\2\60\61\t\2\2\2\61\16\3\2\2\2\62\64\t\3\2")
        buf.write("\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2")
        buf.write("\2\2\66\20\3\2\2\2\678\7-\2\28\22\3\2\2\29:\7/\2\2:\24")
        buf.write("\3\2\2\2;<\7,\2\2<\26\3\2\2\2=>\7\61\2\2>\30\3\2\2\2?")
        buf.write("@\7`\2\2@\32\3\2\2\2AB\7*\2\2B\34\3\2\2\2CD\7+\2\2D\36")
        buf.write("\3\2\2\2EG\t\4\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2")
        buf.write("\2\2IJ\3\2\2\2JK\b\20\2\2K \3\2\2\2\5\2\65H\3\b\2\2")
        return buf.getvalue()


class LambdaCalculusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    VARIABLE = 6
    NUMBER = 7
    ADD = 8
    SUBTRACT = 9
    MULTIPLY = 10
    DIVIDE = 11
    POWER = 12
    LBRACKET = 13
    RBRACKET = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'%'", "':'", "'Bool'", "'Int'", "'+'", "'-'", "'*'", 
            "'/'", "'^'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "VARIABLE", "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
            "POWER", "LBRACKET", "RBRACKET", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "VARIABLE", "NUMBER", 
                  "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "POWER", "LBRACKET", 
                  "RBRACKET", "WS" ]

    grammarFileName = "LambdaCalculus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


