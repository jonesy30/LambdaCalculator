# Generated from arithmetic.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\3\3\3\3\3\7\3\32")
        buf.write("\n\3\f\3\16\3\35\13\3\3\4\3\4\3\4\5\4\"\n\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\4\3\2\6\7\3\2\b")
        buf.write("\t\2\'\2\16\3\2\2\2\4\26\3\2\2\2\6!\3\2\2\2\b#\3\2\2\2")
        buf.write("\n%\3\2\2\2\f\'\3\2\2\2\16\23\5\4\3\2\17\20\t\2\2\2\20")
        buf.write("\22\5\4\3\2\21\17\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2")
        buf.write("\23\24\3\2\2\2\24\3\3\2\2\2\25\23\3\2\2\2\26\33\5\n\6")
        buf.write("\2\27\30\t\3\2\2\30\32\5\n\6\2\31\27\3\2\2\2\32\35\3\2")
        buf.write("\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\5\3\2\2\2\35\33\3")
        buf.write("\2\2\2\36\"\5\n\6\2\37\"\5\b\5\2 \"\5\f\7\2!\36\3\2\2")
        buf.write("\2!\37\3\2\2\2! \3\2\2\2\"\7\3\2\2\2#$\7\5\2\2$\t\3\2")
        buf.write("\2\2%&\7\3\2\2&\13\3\2\2\2\'(\7\4\2\2(\r\3\2\2\2\5\23")
        buf.write("\33!")
        return buf.getvalue()


class arithmeticParser ( Parser ):

    grammarFileName = "arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'", "'&'", 
                     "'|'", "'>'", "'<'", "'=='" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "BOOL", "VARIABLE", "ADD", 
                      "SUBTRACT", "MULTIPLY", "DIVIDE", "POWER", "LBRACKET", 
                      "RBRACKET", "AND", "OR", "GT", "LT", "EQ", "WS" ]

    RULE_function = 0
    RULE_multiplyingExpression = 1
    RULE_atom = 2
    RULE_variable = 3
    RULE_number = 4
    RULE_boolean_value = 5

    ruleNames =  [ "function", "multiplyingExpression", "atom", "variable", 
                   "number", "boolean_value" ]

    EOF = Token.EOF
    NUMBER=1
    BOOL=2
    VARIABLE=3
    ADD=4
    SUBTRACT=5
    MULTIPLY=6
    DIVIDE=7
    POWER=8
    LBRACKET=9
    RBRACKET=10
    AND=11
    OR=12
    GT=13
    LT=14
    EQ=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplyingExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.MultiplyingExpressionContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.MultiplyingExpressionContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(arithmeticParser.ADD)
            else:
                return self.getToken(arithmeticParser.ADD, i)

        def SUBTRACT(self, i:int=None):
            if i is None:
                return self.getTokens(arithmeticParser.SUBTRACT)
            else:
                return self.getToken(arithmeticParser.SUBTRACT, i)

        def getRuleIndex(self):
            return arithmeticParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = arithmeticParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.multiplyingExpression()
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==arithmeticParser.ADD or _la==arithmeticParser.SUBTRACT:
                self.state = 13
                _la = self._input.LA(1)
                if not(_la==arithmeticParser.ADD or _la==arithmeticParser.SUBTRACT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 14
                self.multiplyingExpression()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyingExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.NumberContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.NumberContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(arithmeticParser.MULTIPLY)
            else:
                return self.getToken(arithmeticParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(arithmeticParser.DIVIDE)
            else:
                return self.getToken(arithmeticParser.DIVIDE, i)

        def getRuleIndex(self):
            return arithmeticParser.RULE_multiplyingExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyingExpression" ):
                listener.enterMultiplyingExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyingExpression" ):
                listener.exitMultiplyingExpression(self)




    def multiplyingExpression(self):

        localctx = arithmeticParser.MultiplyingExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_multiplyingExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.number()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==arithmeticParser.MULTIPLY or _la==arithmeticParser.DIVIDE:
                self.state = 21
                _la = self._input.LA(1)
                if not(_la==arithmeticParser.MULTIPLY or _la==arithmeticParser.DIVIDE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 22
                self.number()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(arithmeticParser.NumberContext,0)


        def variable(self):
            return self.getTypedRuleContext(arithmeticParser.VariableContext,0)


        def boolean_value(self):
            return self.getTypedRuleContext(arithmeticParser.Boolean_valueContext,0)


        def getRuleIndex(self):
            return arithmeticParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = arithmeticParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [arithmeticParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.number()
                pass
            elif token in [arithmeticParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.variable()
                pass
            elif token in [arithmeticParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.boolean_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(arithmeticParser.VARIABLE, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = arithmeticParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(arithmeticParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(arithmeticParser.NUMBER, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = arithmeticParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(arithmeticParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(arithmeticParser.BOOL, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_boolean_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_value" ):
                listener.enterBoolean_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_value" ):
                listener.exitBoolean_value(self)




    def boolean_value(self):

        localctx = arithmeticParser.Boolean_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_boolean_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(arithmeticParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





