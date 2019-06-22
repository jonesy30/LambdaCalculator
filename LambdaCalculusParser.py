# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\5\2\26\n\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4,\n\4\3\4\3\4\3\4\3\4\7\4\62\n\4\f\4\16")
        buf.write("\4\65\13\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5=\n\5\3\6\3\6\5")
        buf.write("\6A\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\2\3\6\n\2\4\6\b\n")
        buf.write("\f\16\20\2\3\3\2\7\13\2I\2\25\3\2\2\2\4 \3\2\2\2\6+\3")
        buf.write("\2\2\2\b<\3\2\2\2\n@\3\2\2\2\fB\3\2\2\2\16D\3\2\2\2\20")
        buf.write("F\3\2\2\2\22\26\5\f\7\2\23\26\5\4\3\2\24\26\5\6\4\2\25")
        buf.write("\22\3\2\2\2\25\23\3\2\2\2\25\24\3\2\2\2\26\3\3\2\2\2\27")
        buf.write("\30\7\f\2\2\30\31\5\4\3\2\31\32\7\r\2\2\32!\3\2\2\2\33")
        buf.write("\34\7\3\2\2\34\35\5\f\7\2\35\36\7\4\2\2\36\37\5\b\5\2")
        buf.write("\37!\3\2\2\2 \27\3\2\2\2 \33\3\2\2\2!\5\3\2\2\2\"#\b\4")
        buf.write("\1\2#$\7\f\2\2$%\5\2\2\2%&\5\2\2\2&\'\7\r\2\2\',\3\2\2")
        buf.write("\2()\5\4\3\2)*\5\n\6\2*,\3\2\2\2+\"\3\2\2\2+(\3\2\2\2")
        buf.write(",\63\3\2\2\2-.\f\5\2\2.\62\5\2\2\2/\60\f\4\2\2\60\62\5")
        buf.write("\n\6\2\61-\3\2\2\2\61/\3\2\2\2\62\65\3\2\2\2\63\61\3\2")
        buf.write("\2\2\63\64\3\2\2\2\64\7\3\2\2\2\65\63\3\2\2\2\66\67\5")
        buf.write("\n\6\2\678\5\20\t\289\5\n\6\29=\3\2\2\2:=\5\n\6\2;=\5")
        buf.write("\2\2\2<\66\3\2\2\2<:\3\2\2\2<;\3\2\2\2=\t\3\2\2\2>A\5")
        buf.write("\16\b\2?A\5\f\7\2@>\3\2\2\2@?\3\2\2\2A\13\3\2\2\2BC\7")
        buf.write("\5\2\2C\r\3\2\2\2DE\7\6\2\2E\17\3\2\2\2FG\t\2\2\2G\21")
        buf.write("\3\2\2\2\t\25 +\61\63<@")
        return buf.getvalue()


class LambdaCalculusParser ( Parser ):

    grammarFileName = "LambdaCalculus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'%'", "'.'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "VARIABLE", 
                      "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
                      "POWER", "LBRACKET", "RBRACKET", "WS" ]

    RULE_term = 0
    RULE_abstraction = 1
    RULE_application = 2
    RULE_function = 3
    RULE_expression = 4
    RULE_variable = 5
    RULE_number = 6
    RULE_operation = 7

    ruleNames =  [ "term", "abstraction", "application", "function", "expression", 
                   "variable", "number", "operation" ]

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
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.abstraction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.application(0)
                pass


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

        def variable(self):
            return self.getTypedRuleContext(LambdaCalculusParser.VariableContext,0)


        def function(self):
            return self.getTypedRuleContext(LambdaCalculusParser.FunctionContext,0)


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
        self.enterRule(localctx, 2, self.RULE_abstraction)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LambdaCalculusParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(LambdaCalculusParser.LBRACKET)
                self.state = 22
                self.abstraction()
                self.state = 23
                self.match(LambdaCalculusParser.RBRACKET)
                pass
            elif token in [LambdaCalculusParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(LambdaCalculusParser.T__0)
                self.state = 26
                self.variable()
                self.state = 27
                self.match(LambdaCalculusParser.T__1)
                self.state = 28
                self.function()
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

    class ApplicationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(LambdaCalculusParser.LBRACKET, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaCalculusParser.TermContext)
            else:
                return self.getTypedRuleContext(LambdaCalculusParser.TermContext,i)


        def RBRACKET(self):
            return self.getToken(LambdaCalculusParser.RBRACKET, 0)

        def abstraction(self):
            return self.getTypedRuleContext(LambdaCalculusParser.AbstractionContext,0)


        def expression(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ExpressionContext,0)


        def application(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ApplicationContext,0)


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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_application, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 33
                self.match(LambdaCalculusParser.LBRACKET)
                self.state = 34
                self.term()
                self.state = 35
                self.term()
                self.state = 36
                self.match(LambdaCalculusParser.RBRACKET)
                pass

            elif la_ == 2:
                self.state = 38
                self.abstraction()
                self.state = 39
                self.expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LambdaCalculusParser.ApplicationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                        self.state = 43
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 44
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = LambdaCalculusParser.ApplicationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                        self.state = 45
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 46
                        self.expression()
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_function)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.expression()
                self.state = 53
                self.operation()
                self.state = 54
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
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
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LambdaCalculusParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.number()
                pass
            elif token in [LambdaCalculusParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
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
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
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
        self.enterRule(localctx, 12, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
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
        self.enterRule(localctx, 14, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
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
        self._predicates[2] = self.application_sempred
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
         




