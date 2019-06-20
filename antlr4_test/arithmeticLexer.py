# Generated from arithmetic.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("S\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\7\2\"\n\2\f\2\16\2%\13\2\3\3\5")
        buf.write("\3(\n\3\3\4\3\4\5\4,\n\4\3\5\6\5/\n\5\r\5\16\5\60\3\5")
        buf.write("\3\5\6\5\65\n\5\r\5\16\5\66\5\59\n\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\6\17N\n\17\r\17\16\17O\3\17\3\17\2\2\20\3\3")
        buf.write("\5\2\7\2\t\2\13\2\r\2\17\4\21\5\23\6\25\7\27\b\31\t\33")
        buf.write("\n\35\13\3\2\6\5\2C\\aac|\4\2GGgg\4\2--//\5\2\13\f\17")
        buf.write("\17\"\"\2S\2\3\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5\'\3\2\2\2\7+\3\2\2")
        buf.write("\2\t.\3\2\2\2\13:\3\2\2\2\r<\3\2\2\2\17>\3\2\2\2\21@\3")
        buf.write("\2\2\2\23B\3\2\2\2\25D\3\2\2\2\27F\3\2\2\2\31H\3\2\2\2")
        buf.write("\33J\3\2\2\2\35M\3\2\2\2\37#\5\5\3\2 \"\5\7\4\2! \3\2")
        buf.write("\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\4\3\2\2\2%#\3\2\2")
        buf.write("\2&(\t\2\2\2\'&\3\2\2\2(\6\3\2\2\2),\5\5\3\2*,\4\62;\2")
        buf.write("+)\3\2\2\2+*\3\2\2\2,\b\3\2\2\2-/\4\62;\2.-\3\2\2\2/\60")
        buf.write("\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\618\3\2\2\2\62\64\7")
        buf.write("\60\2\2\63\65\4\62;\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28\62\3\2\2\289\3\2\2")
        buf.write("\29\n\3\2\2\2:;\t\3\2\2;\f\3\2\2\2<=\t\4\2\2=\16\3\2\2")
        buf.write("\2>?\7*\2\2?\20\3\2\2\2@A\7+\2\2A\22\3\2\2\2BC\7-\2\2")
        buf.write("C\24\3\2\2\2DE\7/\2\2E\26\3\2\2\2FG\7,\2\2G\30\3\2\2\2")
        buf.write("HI\7\61\2\2I\32\3\2\2\2JK\7\60\2\2K\34\3\2\2\2LN\t\5\2")
        buf.write("\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2PQ\3\2\2\2Q")
        buf.write("R\b\17\2\2R\36\3\2\2\2\n\2#\'+\60\668O\3\b\2\2")
        return buf.getvalue()


class arithmeticLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VARIABLE = 1
    LPAREN = 2
    RPAREN = 3
    PLUS = 4
    MINUS = 5
    TIMES = 6
    DIV = 7
    POINT = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "VARIABLE", "LPAREN", "RPAREN", "PLUS", "MINUS", "TIMES", "DIV", 
            "POINT", "WS" ]

    ruleNames = [ "VARIABLE", "VALID_ID_START", "VALID_ID_CHAR", "NUMBER", 
                  "E", "SIGN", "LPAREN", "RPAREN", "PLUS", "MINUS", "TIMES", 
                  "DIV", "POINT", "WS" ]

    grammarFileName = "arithmetic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


