# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\5\2")
        buf.write("\34\n\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\6\5\61\n\5\r\5\16\5\62")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\6\6<\n\6\r\6\16\6=\3\6\3")
        buf.write("\6\5\6B\n\6\3\6\3\6\3\6\3\6\7\6H\n\6\f\6\16\6K\13\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7W\n\7\3\b\3")
        buf.write("\b\5\b[\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\3")
        buf.write("\n\r\2\4\6\b\n\f\16\20\22\24\26\2\3\3\2\7\13\2g\2\33\3")
        buf.write("\2\2\2\4\35\3\2\2\2\6,\3\2\2\2\b.\3\2\2\2\nA\3\2\2\2\f")
        buf.write("V\3\2\2\2\16Z\3\2\2\2\20\\\3\2\2\2\22^\3\2\2\2\24`\3\2")
        buf.write("\2\2\26b\3\2\2\2\30\34\5\20\t\2\31\34\5\6\4\2\32\34\5")
        buf.write("\n\6\2\33\30\3\2\2\2\33\31\3\2\2\2\33\32\3\2\2\2\34\3")
        buf.write("\3\2\2\2\35\36\5\6\4\2\36\37\5\24\13\2\37\5\3\2\2\2 !")
        buf.write("\7\f\2\2!\"\5\6\4\2\"#\7\r\2\2#-\3\2\2\2$%\5\b\5\2%&\7")
        buf.write("\3\2\2&\'\5\f\7\2\'-\3\2\2\2()\5\b\5\2)*\7\3\2\2*+\5\2")
        buf.write("\2\2+-\3\2\2\2, \3\2\2\2,$\3\2\2\2,(\3\2\2\2-\7\3\2\2")
        buf.write("\2.\60\7\4\2\2/\61\5\22\n\2\60/\3\2\2\2\61\62\3\2\2\2")
        buf.write("\62\60\3\2\2\2\62\63\3\2\2\2\63\t\3\2\2\2\64\65\b\6\1")
        buf.write("\2\65B\5\4\3\2\66\67\5\6\4\2\678\5\n\6\68B\3\2\2\29;\7")
        buf.write("\f\2\2:<\5\2\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2")
        buf.write("\2>?\3\2\2\2?@\7\r\2\2@B\3\2\2\2A\64\3\2\2\2A\66\3\2\2")
        buf.write("\2A9\3\2\2\2BI\3\2\2\2CD\f\5\2\2DH\5\2\2\2EF\f\4\2\2F")
        buf.write("H\5\16\b\2GC\3\2\2\2GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3")
        buf.write("\2\2\2J\13\3\2\2\2KI\3\2\2\2LM\5\16\b\2MN\5\26\f\2NO\5")
        buf.write("\16\b\2OW\3\2\2\2PQ\5\16\b\2QR\5\26\f\2RS\5\2\2\2SW\3")
        buf.write("\2\2\2TW\5\16\b\2UW\5\2\2\2VL\3\2\2\2VP\3\2\2\2VT\3\2")
        buf.write("\2\2VU\3\2\2\2W\r\3\2\2\2X[\5\24\13\2Y[\5\20\t\2ZX\3\2")
        buf.write("\2\2ZY\3\2\2\2[\17\3\2\2\2\\]\7\5\2\2]\21\3\2\2\2^_\7")
        buf.write("\5\2\2_\23\3\2\2\2`a\7\6\2\2a\25\3\2\2\2bc\t\2\2\2c\27")
        buf.write("\3\2\2\2\13\33,\62=AGIVZ")
        return buf.getvalue()


class LambdaCalculusParser ( Parser ):

    grammarFileName = "LambdaCalculus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'%'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "VARIABLE", 
                      "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
                      "POWER", "LBRACKET", "RBRACKET", "WS" ]

    RULE_term = 0
    RULE_value_term = 1
    RULE_abstraction = 2
    RULE_abstraction_term = 3
    RULE_application = 4
    RULE_function = 5
    RULE_expression = 6
    RULE_variable = 7
    RULE_lambda_variable = 8
    RULE_number = 9
    RULE_operation = 10

    ruleNames =  [ "term", "value_term", "abstraction", "abstraction_term", 
                   "application", "function", "expression", "variable", 
                   "lambda_variable", "number", "operation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    VARIABLE=3
    NUMBER=4
    ADD=5
    SUBTRACT=6
    MULTIPLY=7
    DIVIDE=8
    POWER=9
    LBRACKET=10
    RBRACKET=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(LambdaCalculusParser.VariableContext,0)


        def abstraction(self):
            return self.getTypedRuleContext(LambdaCalculusParser.AbstractionContext,0)


        def application(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ApplicationContext,0)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = LambdaCalculusParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_term)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.abstraction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.application(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def abstraction(self):
            return self.getTypedRuleContext(LambdaCalculusParser.AbstractionContext,0)


        def number(self):
            return self.getTypedRuleContext(LambdaCalculusParser.NumberContext,0)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_value_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_term" ):
                listener.enterValue_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_term" ):
                listener.exitValue_term(self)




    def value_term(self):

        localctx = LambdaCalculusParser.Value_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.abstraction()
            self.state = 28
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AbstractionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(LambdaCalculusParser.LBRACKET, 0)

        def abstraction(self):
            return self.getTypedRuleContext(LambdaCalculusParser.AbstractionContext,0)


        def RBRACKET(self):
            return self.getToken(LambdaCalculusParser.RBRACKET, 0)

        def abstraction_term(self):
            return self.getTypedRuleContext(LambdaCalculusParser.Abstraction_termContext,0)


        def function(self):
            return self.getTypedRuleContext(LambdaCalculusParser.FunctionContext,0)


        def term(self):
            return self.getTypedRuleContext(LambdaCalculusParser.TermContext,0)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_abstraction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction" ):
                listener.enterAbstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction" ):
                listener.exitAbstraction(self)




    def abstraction(self):

        localctx = LambdaCalculusParser.AbstractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_abstraction)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(LambdaCalculusParser.LBRACKET)
                self.state = 31
                self.abstraction()
                self.state = 32
                self.match(LambdaCalculusParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.abstraction_term()
                self.state = 35
                self.match(LambdaCalculusParser.T__0)
                self.state = 36
                self.function()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.abstraction_term()
                self.state = 39
                self.match(LambdaCalculusParser.T__0)
                self.state = 40
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abstraction_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambda_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaCalculusParser.Lambda_variableContext)
            else:
                return self.getTypedRuleContext(LambdaCalculusParser.Lambda_variableContext,i)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_abstraction_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction_term" ):
                listener.enterAbstraction_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction_term" ):
                listener.exitAbstraction_term(self)




    def abstraction_term(self):

        localctx = LambdaCalculusParser.Abstraction_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_abstraction_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(LambdaCalculusParser.T__1)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.lambda_variable()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LambdaCalculusParser.VARIABLE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ApplicationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_term(self):
            return self.getTypedRuleContext(LambdaCalculusParser.Value_termContext,0)


        def abstraction(self):
            return self.getTypedRuleContext(LambdaCalculusParser.AbstractionContext,0)


        def application(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ApplicationContext,0)


        def LBRACKET(self):
            return self.getToken(LambdaCalculusParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(LambdaCalculusParser.RBRACKET, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaCalculusParser.TermContext)
            else:
                return self.getTypedRuleContext(LambdaCalculusParser.TermContext,i)


        def expression(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_application

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplication" ):
                listener.enterApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplication" ):
                listener.exitApplication(self)



    def application(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LambdaCalculusParser.ApplicationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_application, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 51
                self.value_term()
                pass

            elif la_ == 2:
                self.state = 52
                self.abstraction()
                self.state = 53
                self.application(4)
                pass

            elif la_ == 3:
                self.state = 55
                self.match(LambdaCalculusParser.LBRACKET)
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 56
                    self.term()
                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LambdaCalculusParser.T__1) | (1 << LambdaCalculusParser.VARIABLE) | (1 << LambdaCalculusParser.LBRACKET))) != 0)):
                        break

                self.state = 61
                self.match(LambdaCalculusParser.RBRACKET)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = LambdaCalculusParser.ApplicationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                        self.state = 65
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 66
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = LambdaCalculusParser.ApplicationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                        self.state = 67
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 68
                        self.expression()
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaCalculusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,i)


        def operation(self):
            return self.getTypedRuleContext(LambdaCalculusParser.OperationContext,0)


        def term(self):
            return self.getTypedRuleContext(LambdaCalculusParser.TermContext,0)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = LambdaCalculusParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.expression()
                self.state = 75
                self.operation()
                self.state = 76
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.expression()
                self.state = 79
                self.operation()
                self.state = 80
                self.term()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(LambdaCalculusParser.NumberContext,0)


        def variable(self):
            return self.getTypedRuleContext(LambdaCalculusParser.VariableContext,0)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = LambdaCalculusParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LambdaCalculusParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.number()
                pass
            elif token in [LambdaCalculusParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.variable()
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
            return self.getToken(LambdaCalculusParser.VARIABLE, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = LambdaCalculusParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(LambdaCalculusParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Lambda_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(LambdaCalculusParser.VARIABLE, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_lambda_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda_variable" ):
                listener.enterLambda_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda_variable" ):
                listener.exitLambda_variable(self)




    def lambda_variable(self):

        localctx = LambdaCalculusParser.Lambda_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lambda_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(LambdaCalculusParser.VARIABLE)
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
            return self.getToken(LambdaCalculusParser.NUMBER, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = LambdaCalculusParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(LambdaCalculusParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(LambdaCalculusParser.ADD, 0)

        def SUBTRACT(self):
            return self.getToken(LambdaCalculusParser.SUBTRACT, 0)

        def MULTIPLY(self):
            return self.getToken(LambdaCalculusParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(LambdaCalculusParser.DIVIDE, 0)

        def POWER(self):
            return self.getToken(LambdaCalculusParser.POWER, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = LambdaCalculusParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LambdaCalculusParser.ADD) | (1 << LambdaCalculusParser.SUBTRACT) | (1 << LambdaCalculusParser.MULTIPLY) | (1 << LambdaCalculusParser.DIVIDE) | (1 << LambdaCalculusParser.POWER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.application_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def application_sempred(self, localctx:ApplicationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




