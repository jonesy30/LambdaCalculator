# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\r\6\rS\n\r\r\r\16\rT\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\6\25f\n\25\r\25\16\25g\3\25\3\25\2\2\26\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26\3\2\5\4\2C\\c|\3\2\62")
        buf.write(";\5\2\13\f\17\17\"\"\2l\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\3+\3\2\2\2\5-\3\2\2\2\7/\3\2\2\2\t\61\3\2\2\2\13\64\3")
        buf.write("\2\2\2\r9\3\2\2\2\17>\3\2\2\2\21C\3\2\2\2\23G\3\2\2\2")
        buf.write("\25K\3\2\2\2\27O\3\2\2\2\31R\3\2\2\2\33V\3\2\2\2\35X\3")
        buf.write("\2\2\2\37Z\3\2\2\2!\\\3\2\2\2#^\3\2\2\2%`\3\2\2\2\'b\3")
        buf.write("\2\2\2)e\3\2\2\2+,\7\60\2\2,\4\3\2\2\2-.\7\'\2\2.\6\3")
        buf.write("\2\2\2/\60\7<\2\2\60\b\3\2\2\2\61\62\7/\2\2\62\63\7@\2")
        buf.write("\2\63\n\3\2\2\2\64\65\7D\2\2\65\66\7q\2\2\66\67\7q\2\2")
        buf.write("\678\7n\2\28\f\3\2\2\29:\7d\2\2:;\7q\2\2;<\7q\2\2<=\7")
        buf.write("n\2\2=\16\3\2\2\2>?\7D\2\2?@\7Q\2\2@A\7Q\2\2AB\7N\2\2")
        buf.write("B\20\3\2\2\2CD\7K\2\2DE\7p\2\2EF\7v\2\2F\22\3\2\2\2GH")
        buf.write("\7k\2\2HI\7p\2\2IJ\7v\2\2J\24\3\2\2\2KL\7K\2\2LM\7P\2")
        buf.write("\2MN\7V\2\2N\26\3\2\2\2OP\t\2\2\2P\30\3\2\2\2QS\t\3\2")
        buf.write("\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\32\3\2\2\2")
        buf.write("VW\7-\2\2W\34\3\2\2\2XY\7/\2\2Y\36\3\2\2\2Z[\7,\2\2[ ")
        buf.write("\3\2\2\2\\]\7\61\2\2]\"\3\2\2\2^_\7`\2\2_$\3\2\2\2`a\7")
        buf.write("*\2\2a&\3\2\2\2bc\7+\2\2c(\3\2\2\2df\t\4\2\2ed\3\2\2\2")
        buf.write("fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\b\25\2\2j*")
        buf.write("\3\2\2\2\5\2Tg\3\b\2\2")
        return buf.getvalue()


class LambdaCalculusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    VARIABLE = 11
    NUMBER = 12
    ADD = 13
    SUBTRACT = 14
    MULTIPLY = 15
    DIVIDE = 16
    POWER = 17
    LBRACKET = 18
    RBRACKET = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'%'", "':'", "'->'", "'Bool'", "'bool'", "'BOOL'", "'Int'", 
            "'int'", "'INT'", "'+'", "'-'", "'*'", "'/'", "'^'", "'('", 
            "')'" ]

    symbolicNames = [ "<INVALID>",
            "VARIABLE", "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
            "POWER", "LBRACKET", "RBRACKET", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "VARIABLE", "NUMBER", "ADD", "SUBTRACT", 
                  "MULTIPLY", "DIVIDE", "POWER", "LBRACKET", "RBRACKET", 
                  "WS" ]

    grammarFileName = "LambdaCalculus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


