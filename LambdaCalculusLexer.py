# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\f\6\fN")
        buf.write("\n\f\r\f\16\fO\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\6\24a\n\24\r\24\16\24")
        buf.write("b\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25\3\2\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2g\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7-\3\2\2\2\t/\3")
        buf.write("\2\2\2\13\64\3\2\2\2\r9\3\2\2\2\17>\3\2\2\2\21B\3\2\2")
        buf.write("\2\23F\3\2\2\2\25J\3\2\2\2\27M\3\2\2\2\31Q\3\2\2\2\33")
        buf.write("S\3\2\2\2\35U\3\2\2\2\37W\3\2\2\2!Y\3\2\2\2#[\3\2\2\2")
        buf.write("%]\3\2\2\2\'`\3\2\2\2)*\7\60\2\2*\4\3\2\2\2+,\7\'\2\2")
        buf.write(",\6\3\2\2\2-.\7<\2\2.\b\3\2\2\2/\60\7D\2\2\60\61\7q\2")
        buf.write("\2\61\62\7q\2\2\62\63\7n\2\2\63\n\3\2\2\2\64\65\7d\2\2")
        buf.write("\65\66\7q\2\2\66\67\7q\2\2\678\7n\2\28\f\3\2\2\29:\7D")
        buf.write("\2\2:;\7Q\2\2;<\7Q\2\2<=\7N\2\2=\16\3\2\2\2>?\7K\2\2?")
        buf.write("@\7p\2\2@A\7v\2\2A\20\3\2\2\2BC\7k\2\2CD\7p\2\2DE\7v\2")
        buf.write("\2E\22\3\2\2\2FG\7K\2\2GH\7P\2\2HI\7V\2\2I\24\3\2\2\2")
        buf.write("JK\t\2\2\2K\26\3\2\2\2LN\t\3\2\2ML\3\2\2\2NO\3\2\2\2O")
        buf.write("M\3\2\2\2OP\3\2\2\2P\30\3\2\2\2QR\7-\2\2R\32\3\2\2\2S")
        buf.write("T\7/\2\2T\34\3\2\2\2UV\7,\2\2V\36\3\2\2\2WX\7\61\2\2X")
        buf.write(" \3\2\2\2YZ\7`\2\2Z\"\3\2\2\2[\\\7*\2\2\\$\3\2\2\2]^\7")
        buf.write("+\2\2^&\3\2\2\2_a\t\4\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2")
        buf.write("\2bc\3\2\2\2cd\3\2\2\2de\b\24\2\2e(\3\2\2\2\5\2Ob\3\b")
        buf.write("\2\2")
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
    VARIABLE = 10
    NUMBER = 11
    ADD = 12
    SUBTRACT = 13
    MULTIPLY = 14
    DIVIDE = 15
    POWER = 16
    LBRACKET = 17
    RBRACKET = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'%'", "':'", "'Bool'", "'bool'", "'BOOL'", "'Int'", 
            "'int'", "'INT'", "'+'", "'-'", "'*'", "'/'", "'^'", "'('", 
            "')'" ]

    symbolicNames = [ "<INVALID>",
            "VARIABLE", "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
            "POWER", "LBRACKET", "RBRACKET", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "VARIABLE", "NUMBER", "ADD", "SUBTRACT", 
                  "MULTIPLY", "DIVIDE", "POWER", "LBRACKET", "RBRACKET", 
                  "WS" ]

    grammarFileName = "LambdaCalculus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


