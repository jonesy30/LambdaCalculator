# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\5\2\33")
        buf.write("\n\2\3\3\3\3\5\3\37\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\58\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7K\n\7\3\7\3\7\7")
        buf.write("\7O\n\7\f\7\16\7R\13\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\13\2\3\f\f\2\4\6\b\n\f\16\20\22\24\2\3\3\2\b\f\2")
        buf.write("\\\2\32\3\2\2\2\4\36\3\2\2\2\6-\3\2\2\2\b\67\3\2\2\2\n")
        buf.write("9\3\2\2\2\fJ\3\2\2\2\16S\3\2\2\2\20U\3\2\2\2\22W\3\2\2")
        buf.write("\2\24Y\3\2\2\2\26\33\5\4\3\2\27\33\5\6\4\2\30\33\5\b\5")
        buf.write("\2\31\33\5\f\7\2\32\26\3\2\2\2\32\27\3\2\2\2\32\30\3\2")
        buf.write("\2\2\32\31\3\2\2\2\33\3\3\2\2\2\34\37\5\22\n\2\35\37\5")
        buf.write("\16\b\2\36\34\3\2\2\2\36\35\3\2\2\2\37\5\3\2\2\2 !\5\4")
        buf.write("\3\2!\"\5\24\13\2\"#\5\2\2\2#.\3\2\2\2$%\5\24\13\2%&\5")
        buf.write("\2\2\2&\'\7\3\2\2\'(\5\2\2\2(.\3\2\2\2)*\7\r\2\2*+\5\6")
        buf.write("\4\2+,\7\16\2\2,.\3\2\2\2- \3\2\2\2-$\3\2\2\2-)\3\2\2")
        buf.write("\2.\7\3\2\2\2/\60\5\n\6\2\60\61\7\4\2\2\61\62\5\2\2\2")
        buf.write("\628\3\2\2\2\63\64\7\r\2\2\64\65\5\b\5\2\65\66\7\16\2")
        buf.write("\2\668\3\2\2\2\67/\3\2\2\2\67\63\3\2\2\28\t\3\2\2\29:")
        buf.write("\7\5\2\2:;\5\20\t\2;\13\3\2\2\2<=\b\7\1\2=>\5\b\5\2>?")
        buf.write("\5\2\2\2?K\3\2\2\2@A\5\6\4\2AB\5\2\2\2BK\3\2\2\2CD\5\4")
        buf.write("\3\2DE\5\2\2\2EK\3\2\2\2FG\7\r\2\2GH\5\f\7\2HI\7\16\2")
        buf.write("\2IK\3\2\2\2J<\3\2\2\2J@\3\2\2\2JC\3\2\2\2JF\3\2\2\2K")
        buf.write("P\3\2\2\2LM\f\7\2\2MO\5\2\2\2NL\3\2\2\2OR\3\2\2\2PN\3")
        buf.write("\2\2\2PQ\3\2\2\2Q\r\3\2\2\2RP\3\2\2\2ST\7\6\2\2T\17\3")
        buf.write("\2\2\2UV\7\6\2\2V\21\3\2\2\2WX\7\7\2\2X\23\3\2\2\2YZ\t")
        buf.write("\2\2\2Z\25\3\2\2\2\b\32\36-\67JP")
        return buf.getvalue()


class LambdaCalculusParser ( Parser ):

    grammarFileName = "LambdaCalculus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'.'", "'%'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VARIABLE", "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", 
                      "DIVIDE", "POWER", "LBRACKET", "RBRACKET", "WS" ]

    RULE_term = 0
    RULE_value = 1
    RULE_function = 2
    RULE_abstraction = 3
    RULE_abstraction_term = 4
    RULE_application = 5
    RULE_variable = 6
    RULE_lambda_variable = 7
    RULE_number = 8
    RULE_operation = 9

    ruleNames =  [ "term", "value", "function", "abstraction", "abstraction_term", 
                   "application", "variable", "lambda_variable", "number", 
                   "operation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VARIABLE=4
    NUMBER=5
    ADD=6
    SUBTRACT=7
    MULTIPLY=8
    DIVIDE=9
    POWER=10
    LBRACKET=11
    RBRACKET=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ValueContext,0)


        def function(self):
            return self.getTypedRuleContext(LambdaCalculusParser.FunctionContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = LambdaCalculusParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_term)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.function()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.abstraction()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.application(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(LambdaCalculusParser.NumberContext,0)


        def variable(self):
            return self.getTypedRuleContext(LambdaCalculusParser.VariableContext,0)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = LambdaCalculusParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LambdaCalculusParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.number()
                pass
            elif token in [LambdaCalculusParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
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

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ValueContext,0)


        def operation(self):
            return self.getTypedRuleContext(LambdaCalculusParser.OperationContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaCalculusParser.TermContext)
            else:
                return self.getTypedRuleContext(LambdaCalculusParser.TermContext,i)


        def LBRACKET(self):
            return self.getToken(LambdaCalculusParser.LBRACKET, 0)

        def function(self):
            return self.getTypedRuleContext(LambdaCalculusParser.FunctionContext,0)


        def RBRACKET(self):
            return self.getToken(LambdaCalculusParser.RBRACKET, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = LambdaCalculusParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LambdaCalculusParser.VARIABLE, LambdaCalculusParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.value()
                self.state = 31
                self.operation()
                self.state = 32
                self.term()
                pass
            elif token in [LambdaCalculusParser.ADD, LambdaCalculusParser.SUBTRACT, LambdaCalculusParser.MULTIPLY, LambdaCalculusParser.DIVIDE, LambdaCalculusParser.POWER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.operation()
                self.state = 35
                self.term()
                self.state = 36
                self.match(LambdaCalculusParser.T__0)
                self.state = 37
                self.term()
                pass
            elif token in [LambdaCalculusParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(LambdaCalculusParser.LBRACKET)
                self.state = 40
                self.function()
                self.state = 41
                self.match(LambdaCalculusParser.RBRACKET)
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

    class AbstractionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def abstraction_term(self):
            return self.getTypedRuleContext(LambdaCalculusParser.Abstraction_termContext,0)


        def term(self):
            return self.getTypedRuleContext(LambdaCalculusParser.TermContext,0)


        def LBRACKET(self):
            return self.getToken(LambdaCalculusParser.LBRACKET, 0)

        def abstraction(self):
            return self.getTypedRuleContext(LambdaCalculusParser.AbstractionContext,0)


        def RBRACKET(self):
            return self.getToken(LambdaCalculusParser.RBRACKET, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_abstraction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction" ):
                listener.enterAbstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction" ):
                listener.exitAbstraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction" ):
                return visitor.visitAbstraction(self)
            else:
                return visitor.visitChildren(self)




    def abstraction(self):

        localctx = LambdaCalculusParser.AbstractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_abstraction)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LambdaCalculusParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.abstraction_term()
                self.state = 46
                self.match(LambdaCalculusParser.T__1)
                self.state = 47
                self.term()
                pass
            elif token in [LambdaCalculusParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(LambdaCalculusParser.LBRACKET)
                self.state = 50
                self.abstraction()
                self.state = 51
                self.match(LambdaCalculusParser.RBRACKET)
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

    class Abstraction_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambda_variable(self):
            return self.getTypedRuleContext(LambdaCalculusParser.Lambda_variableContext,0)


        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_abstraction_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction_term" ):
                listener.enterAbstraction_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction_term" ):
                listener.exitAbstraction_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction_term" ):
                return visitor.visitAbstraction_term(self)
            else:
                return visitor.visitChildren(self)




    def abstraction_term(self):

        localctx = LambdaCalculusParser.Abstraction_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_abstraction_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(LambdaCalculusParser.T__2)
            self.state = 56
            self.lambda_variable()
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

        def abstraction(self):
            return self.getTypedRuleContext(LambdaCalculusParser.AbstractionContext,0)


        def term(self):
            return self.getTypedRuleContext(LambdaCalculusParser.TermContext,0)


        def function(self):
            return self.getTypedRuleContext(LambdaCalculusParser.FunctionContext,0)


        def value(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ValueContext,0)


        def LBRACKET(self):
            return self.getToken(LambdaCalculusParser.LBRACKET, 0)

        def application(self):
            return self.getTypedRuleContext(LambdaCalculusParser.ApplicationContext,0)


        def RBRACKET(self):
            return self.getToken(LambdaCalculusParser.RBRACKET, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_application

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplication" ):
                listener.enterApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplication" ):
                listener.exitApplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplication" ):
                return visitor.visitApplication(self)
            else:
                return visitor.visitChildren(self)



    def application(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LambdaCalculusParser.ApplicationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_application, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 59
                self.abstraction()
                self.state = 60
                self.term()
                pass

            elif la_ == 2:
                self.state = 62
                self.function()
                self.state = 63
                self.term()
                pass

            elif la_ == 3:
                self.state = 65
                self.value()
                self.state = 66
                self.term()
                pass

            elif la_ == 4:
                self.state = 68
                self.match(LambdaCalculusParser.LBRACKET)
                self.state = 69
                self.application(0)
                self.state = 70
                self.match(LambdaCalculusParser.RBRACKET)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LambdaCalculusParser.ApplicationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                    self.state = 74
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 75
                    self.term() 
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            return self.getToken(LambdaCalculusParser.VARIABLE, 0)

        def getRuleIndex(self):
            return LambdaCalculusParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = LambdaCalculusParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambda_variable" ):
                return visitor.visitLambda_variable(self)
            else:
                return visitor.visitChildren(self)




    def lambda_variable(self):

        localctx = LambdaCalculusParser.Lambda_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lambda_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = LambdaCalculusParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = LambdaCalculusParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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
        self._predicates[5] = self.application_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def application_sempred(self, localctx:ApplicationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




