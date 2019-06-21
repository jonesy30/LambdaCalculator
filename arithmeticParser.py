# Generated from arithmetic.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\32\n\4\f")
        buf.write("\4\16\4\35\13\4\3\5\3\5\3\5\2\3\6\6\2\4\6\b\2\4\3\2\b")
        buf.write("\t\3\2\6\7\2\36\2\n\3\2\2\2\4\f\3\2\2\2\6\16\3\2\2\2\b")
        buf.write("\36\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f\r\5\6\4\2\r\5")
        buf.write("\3\2\2\2\16\17\b\4\1\2\17\20\7\4\2\2\20\21\5\6\4\2\21")
        buf.write("\22\7\5\2\2\22\33\3\2\2\2\23\24\f\5\2\2\24\25\t\2\2\2")
        buf.write("\25\32\5\6\4\6\26\27\f\4\2\2\27\30\t\3\2\2\30\32\5\6\4")
        buf.write("\5\31\23\3\2\2\2\31\26\3\2\2\2\32\35\3\2\2\2\33\31\3\2")
        buf.write("\2\2\33\34\3\2\2\2\34\7\3\2\2\2\35\33\3\2\2\2\36\37\7")
        buf.write("\3\2\2\37\t\3\2\2\2\4\31\33")
        return buf.getvalue()


class arithmeticParser ( Parser ):

    grammarFileName = "arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'+'", "'-'", 
                     "'*'", "'/'", "'.'" ]

    symbolicNames = [ "<INVALID>", "VARIABLE", "LPAREN", "RPAREN", "PLUS", 
                      "MINUS", "TIMES", "DIV", "POINT", "WS" ]

    RULE_foo = 0
    RULE_equation = 1
    RULE_expression = 2
    RULE_variable = 3

    ruleNames =  [ "foo", "equation", "expression", "variable" ]

    EOF = Token.EOF
    VARIABLE=1
    LPAREN=2
    RPAREN=3
    PLUS=4
    MINUS=5
    TIMES=6
    DIV=7
    POINT=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FooContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equation(self):
            return self.getTypedRuleContext(arithmeticParser.EquationContext,0)


        def getRuleIndex(self):
            return arithmeticParser.RULE_foo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFoo" ):
                listener.enterFoo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFoo" ):
                listener.exitFoo(self)




    def foo(self):

        localctx = arithmeticParser.FooContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_foo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.equation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EquationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(arithmeticParser.ExpressionContext,0)


        def getRuleIndex(self):
            return arithmeticParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)




    def equation(self):

        localctx = arithmeticParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expression(0)
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

        def LPAREN(self):
            return self.getToken(arithmeticParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(arithmeticParser.RPAREN, 0)

        def TIMES(self):
            return self.getToken(arithmeticParser.TIMES, 0)

        def DIV(self):
            return self.getToken(arithmeticParser.DIV, 0)

        def PLUS(self):
            return self.getToken(arithmeticParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(arithmeticParser.MINUS, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = arithmeticParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(arithmeticParser.LPAREN)
            self.state = 14
            self.expression(0)
            self.state = 15
            self.match(arithmeticParser.RPAREN)
            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 23
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = arithmeticParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 17
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 18
                        _la = self._input.LA(1)
                        if not(_la==arithmeticParser.TIMES or _la==arithmeticParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 19
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = arithmeticParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 20
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 21
                        _la = self._input.LA(1)
                        if not(_la==arithmeticParser.PLUS or _la==arithmeticParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        self.expression(3)
                        pass

             
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 28
            self.match(arithmeticParser.VARIABLE)
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
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




