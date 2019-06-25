// Generated from LambdaCalculus.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LambdaCalculusParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, VARIABLE=3, NUMBER=4, ADD=5, SUBTRACT=6, MULTIPLY=7, DIVIDE=8, 
		POWER=9, LBRACKET=10, RBRACKET=11, WS=12;
	public static final int
		RULE_term = 0, RULE_value_term = 1, RULE_abstraction = 2, RULE_abstraction_term = 3, 
		RULE_application = 4, RULE_function = 5, RULE_expression = 6, RULE_variable = 7, 
		RULE_lambda_variable = 8, RULE_number = 9, RULE_operation = 10;
	public static final String[] ruleNames = {
		"term", "value_term", "abstraction", "abstraction_term", "application", 
		"function", "expression", "variable", "lambda_variable", "number", "operation"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'.'", "'%'", null, null, "'+'", "'-'", "'*'", "'/'", "'^'", "'('", 
		"')'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, "VARIABLE", "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", 
		"DIVIDE", "POWER", "LBRACKET", "RBRACKET", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "LambdaCalculus.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LambdaCalculusParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class TermContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public AbstractionContext abstraction() {
			return getRuleContext(AbstractionContext.class,0);
		}
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_term);
		try {
			setState(25);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				variable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(23);
				abstraction();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(24);
				application(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Value_termContext extends ParserRuleContext {
		public AbstractionContext abstraction() {
			return getRuleContext(AbstractionContext.class,0);
		}
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public Value_termContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterValue_term(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitValue_term(this);
		}
	}

	public final Value_termContext value_term() throws RecognitionException {
		Value_termContext _localctx = new Value_termContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_value_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			abstraction();
			setState(28);
			number();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AbstractionContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(LambdaCalculusParser.LBRACKET, 0); }
		public AbstractionContext abstraction() {
			return getRuleContext(AbstractionContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(LambdaCalculusParser.RBRACKET, 0); }
		public Abstraction_termContext abstraction_term() {
			return getRuleContext(Abstraction_termContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public AbstractionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_abstraction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterAbstraction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitAbstraction(this);
		}
	}

	public final AbstractionContext abstraction() throws RecognitionException {
		AbstractionContext _localctx = new AbstractionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_abstraction);
		try {
			setState(42);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				match(LBRACKET);
				setState(31);
				abstraction();
				setState(32);
				match(RBRACKET);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(34);
				abstraction_term();
				setState(35);
				match(T__0);
				setState(36);
				function();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(38);
				abstraction_term();
				setState(39);
				match(T__0);
				setState(40);
				term();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Abstraction_termContext extends ParserRuleContext {
		public List<Lambda_variableContext> lambda_variable() {
			return getRuleContexts(Lambda_variableContext.class);
		}
		public Lambda_variableContext lambda_variable(int i) {
			return getRuleContext(Lambda_variableContext.class,i);
		}
		public Abstraction_termContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_abstraction_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterAbstraction_term(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitAbstraction_term(this);
		}
	}

	public final Abstraction_termContext abstraction_term() throws RecognitionException {
		Abstraction_termContext _localctx = new Abstraction_termContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_abstraction_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(T__1);
			setState(46); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(45);
				lambda_variable();
				}
				}
				setState(48); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==VARIABLE );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ApplicationContext extends ParserRuleContext {
		public Value_termContext value_term() {
			return getRuleContext(Value_termContext.class,0);
		}
		public AbstractionContext abstraction() {
			return getRuleContext(AbstractionContext.class,0);
		}
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
		}
		public TerminalNode LBRACKET() { return getToken(LambdaCalculusParser.LBRACKET, 0); }
		public TerminalNode RBRACKET() { return getToken(LambdaCalculusParser.RBRACKET, 0); }
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ApplicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_application; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterApplication(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitApplication(this);
		}
	}

	public final ApplicationContext application() throws RecognitionException {
		return application(0);
	}

	private ApplicationContext application(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ApplicationContext _localctx = new ApplicationContext(_ctx, _parentState);
		ApplicationContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_application, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(51);
				value_term();
				}
				break;
			case 2:
				{
				setState(52);
				abstraction();
				setState(53);
				application(4);
				}
				break;
			case 3:
				{
				setState(55);
				match(LBRACKET);
				setState(57); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(56);
					term();
					}
					}
					setState(59); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << VARIABLE) | (1L << LBRACKET))) != 0) );
				setState(61);
				match(RBRACKET);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(71);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(69);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new ApplicationContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_application);
						setState(65);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(66);
						term();
						}
						break;
					case 2:
						{
						_localctx = new ApplicationContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_application);
						setState(67);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(68);
						expression();
						}
						break;
					}
					} 
				}
				setState(73);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitFunction(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_function);
		try {
			setState(84);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				expression();
				setState(75);
				operation();
				setState(76);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				expression();
				setState(79);
				operation();
				setState(80);
				term();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(82);
				expression();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(83);
				term();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_expression);
		try {
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(86);
				number();
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(87);
				variable();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode VARIABLE() { return getToken(LambdaCalculusParser.VARIABLE, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(VARIABLE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Lambda_variableContext extends ParserRuleContext {
		public TerminalNode VARIABLE() { return getToken(LambdaCalculusParser.VARIABLE, 0); }
		public Lambda_variableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lambda_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterLambda_variable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitLambda_variable(this);
		}
	}

	public final Lambda_variableContext lambda_variable() throws RecognitionException {
		Lambda_variableContext _localctx = new Lambda_variableContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_lambda_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(VARIABLE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LambdaCalculusParser.NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterNumber(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitNumber(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperationContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(LambdaCalculusParser.ADD, 0); }
		public TerminalNode SUBTRACT() { return getToken(LambdaCalculusParser.SUBTRACT, 0); }
		public TerminalNode MULTIPLY() { return getToken(LambdaCalculusParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(LambdaCalculusParser.DIVIDE, 0); }
		public TerminalNode POWER() { return getToken(LambdaCalculusParser.POWER, 0); }
		public OperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitOperation(this);
		}
	}

	public final OperationContext operation() throws RecognitionException {
		OperationContext _localctx = new OperationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_operation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADD) | (1L << SUBTRACT) | (1L << MULTIPLY) | (1L << DIVIDE) | (1L << POWER))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return application_sempred((ApplicationContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean application_sempred(ApplicationContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16e\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\3\2\3\2\3\2\5\2\34\n\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\6\5\61\n\5\r\5\16\5\62\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\6\6<\n\6\r\6\16\6=\3\6\3\6\5\6B\n\6\3\6\3\6\3\6\3\6"+
		"\7\6H\n\6\f\6\16\6K\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7W"+
		"\n\7\3\b\3\b\5\b[\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\3\n\r\2"+
		"\4\6\b\n\f\16\20\22\24\26\2\3\3\2\7\13\2g\2\33\3\2\2\2\4\35\3\2\2\2\6"+
		",\3\2\2\2\b.\3\2\2\2\nA\3\2\2\2\fV\3\2\2\2\16Z\3\2\2\2\20\\\3\2\2\2\22"+
		"^\3\2\2\2\24`\3\2\2\2\26b\3\2\2\2\30\34\5\20\t\2\31\34\5\6\4\2\32\34\5"+
		"\n\6\2\33\30\3\2\2\2\33\31\3\2\2\2\33\32\3\2\2\2\34\3\3\2\2\2\35\36\5"+
		"\6\4\2\36\37\5\24\13\2\37\5\3\2\2\2 !\7\f\2\2!\"\5\6\4\2\"#\7\r\2\2#-"+
		"\3\2\2\2$%\5\b\5\2%&\7\3\2\2&\'\5\f\7\2\'-\3\2\2\2()\5\b\5\2)*\7\3\2\2"+
		"*+\5\2\2\2+-\3\2\2\2, \3\2\2\2,$\3\2\2\2,(\3\2\2\2-\7\3\2\2\2.\60\7\4"+
		"\2\2/\61\5\22\n\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2"+
		"\2\63\t\3\2\2\2\64\65\b\6\1\2\65B\5\4\3\2\66\67\5\6\4\2\678\5\n\6\68B"+
		"\3\2\2\29;\7\f\2\2:<\5\2\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>"+
		"?\3\2\2\2?@\7\r\2\2@B\3\2\2\2A\64\3\2\2\2A\66\3\2\2\2A9\3\2\2\2BI\3\2"+
		"\2\2CD\f\5\2\2DH\5\2\2\2EF\f\4\2\2FH\5\16\b\2GC\3\2\2\2GE\3\2\2\2HK\3"+
		"\2\2\2IG\3\2\2\2IJ\3\2\2\2J\13\3\2\2\2KI\3\2\2\2LM\5\16\b\2MN\5\26\f\2"+
		"NO\5\16\b\2OW\3\2\2\2PQ\5\16\b\2QR\5\26\f\2RS\5\2\2\2SW\3\2\2\2TW\5\16"+
		"\b\2UW\5\2\2\2VL\3\2\2\2VP\3\2\2\2VT\3\2\2\2VU\3\2\2\2W\r\3\2\2\2X[\5"+
		"\24\13\2Y[\5\20\t\2ZX\3\2\2\2ZY\3\2\2\2[\17\3\2\2\2\\]\7\5\2\2]\21\3\2"+
		"\2\2^_\7\5\2\2_\23\3\2\2\2`a\7\6\2\2a\25\3\2\2\2bc\t\2\2\2c\27\3\2\2\2"+
		"\13\33,\62=AGIVZ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}