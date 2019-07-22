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
<<<<<<< HEAD
		RULE_term = 0, RULE_application = 1, RULE_abstraction = 2, RULE_abstraction_term = 3, 
		RULE_function = 4, RULE_value = 5, RULE_variable = 6, RULE_lambda_variable = 7, 
		RULE_number = 8, RULE_operation = 9;
	public static final String[] ruleNames = {
		"term", "application", "abstraction", "abstraction_term", "function", 
		"value", "variable", "lambda_variable", "number", "operation"
=======
		RULE_term = 0, RULE_parenthesis = 1, RULE_abstraction = 2, RULE_abstraction_term = 3, 
		RULE_application = 4, RULE_function = 5, RULE_value = 6, RULE_variable = 7, 
		RULE_lambda_variable = 8, RULE_number = 9, RULE_operation = 10;
	public static final String[] ruleNames = {
		"term", "parenthesis", "abstraction", "abstraction_term", "application", 
		"function", "value", "variable", "lambda_variable", "number", "operation"
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
		public AbstractionContext abstraction() {
			return getRuleContext(AbstractionContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
<<<<<<< HEAD
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
=======
		public ParenthesisContext parenthesis() {
			return getRuleContext(ParenthesisContext.class,0);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitTerm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_term);
		try {
			setState(27);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
<<<<<<< HEAD
				setState(20);
				abstraction();
=======
				setState(22);
				function();
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
<<<<<<< HEAD
				setState(21);
				function(0);
=======
				setState(23);
				abstraction();
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
<<<<<<< HEAD
				setState(22);
				value();
=======
				setState(24);
				application(0);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
<<<<<<< HEAD
				setState(23);
				application(0);
=======
				setState(25);
				value();
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(26);
				parenthesis();
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

	public static class ParenthesisContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(LambdaCalculusParser.LBRACKET, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(LambdaCalculusParser.RBRACKET, 0); }
		public ParenthesisContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parenthesis; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterParenthesis(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitParenthesis(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitParenthesis(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParenthesisContext parenthesis() throws RecognitionException {
		ParenthesisContext _localctx = new ParenthesisContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_parenthesis);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29);
			match(LBRACKET);
			setState(30);
			term();
			setState(31);
			match(RBRACKET);
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
		public AbstractionContext abstraction() {
			return getRuleContext(AbstractionContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public TerminalNode LBRACKET() { return getToken(LambdaCalculusParser.LBRACKET, 0); }
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(LambdaCalculusParser.RBRACKET, 0); }
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitApplication(this);
			else return visitor.visitChildren(this);
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
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_application, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(27);
				abstraction();
				setState(28);
				term();
				}
				break;
			case 2:
				{
				setState(30);
				value();
				setState(31);
				term();
				}
				break;
			case 3:
				{
				setState(33);
				function(0);
				setState(34);
				term();
				}
				break;
			case 4:
				{
				setState(36);
				match(LBRACKET);
				setState(37);
				application(0);
				setState(38);
				match(RBRACKET);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(46);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ApplicationContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_application);
					setState(42);
					if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
					setState(43);
					term();
					}
					} 
				}
				setState(48);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
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

	public static class AbstractionContext extends ParserRuleContext {
		public Abstraction_termContext abstraction_term() {
			return getRuleContext(Abstraction_termContext.class,0);
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitAbstraction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AbstractionContext abstraction() throws RecognitionException {
		AbstractionContext _localctx = new AbstractionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_abstraction);
		try {
<<<<<<< HEAD
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				abstraction_term();
				setState(50);
				match(T__0);
				setState(51);
				term();
				}
				break;
			case LBRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				match(LBRACKET);
				setState(54);
				abstraction();
				setState(55);
				match(RBRACKET);
				}
				break;
			default:
				throw new NoViableAltException(this);
=======
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			abstraction_term();
			setState(34);
			match(T__0);
			setState(35);
			term();
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
		public Lambda_variableContext lambda_variable() {
			return getRuleContext(Lambda_variableContext.class,0);
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitAbstraction_term(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Abstraction_termContext abstraction_term() throws RecognitionException {
		Abstraction_termContext _localctx = new Abstraction_termContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_abstraction_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
<<<<<<< HEAD
			setState(59);
			match(T__1);
			setState(60);
=======
			setState(37);
			match(T__1);
			setState(38);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
			lambda_variable();
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

	public static class FunctionContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public AbstractionContext abstraction() {
			return getRuleContext(AbstractionContext.class,0);
		}
<<<<<<< HEAD
		public TerminalNode LBRACKET() { return getToken(LambdaCalculusParser.LBRACKET, 0); }
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(LambdaCalculusParser.RBRACKET, 0); }
		public FunctionContext(ParserRuleContext parent, int invokingState) {
=======
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ParenthesisContext parenthesis() {
			return getRuleContext(ParenthesisContext.class,0);
		}
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
		}
		public ApplicationContext(ParserRuleContext parent, int invokingState) {
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitFunction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		return function(0);
	}

	private FunctionContext function(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
<<<<<<< HEAD
		FunctionContext _localctx = new FunctionContext(_ctx, _parentState);
		FunctionContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_function, _p);
=======
		ApplicationContext _localctx = new ApplicationContext(_ctx, _parentState);
		ApplicationContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_application, _p);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			_errHandler.sync(this);
<<<<<<< HEAD
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(63);
				value();
				setState(64);
				operation();
				setState(65);
=======
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(41);
				function();
				setState(42);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
				term();
				}
				break;
			case 2:
				{
<<<<<<< HEAD
				setState(67);
				abstraction();
				setState(68);
				operation();
				setState(69);
=======
				setState(44);
				abstraction();
				setState(45);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
				term();
				}
				break;
			case 3:
				{
<<<<<<< HEAD
				setState(71);
				match(LBRACKET);
				setState(72);
				function(0);
				setState(73);
				match(RBRACKET);
=======
				setState(47);
				value();
				setState(48);
				term();
				}
				break;
			case 4:
				{
				setState(50);
				parenthesis();
				setState(51);
				term();
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(83);
			_errHandler.sync(this);
<<<<<<< HEAD
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
=======
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new FunctionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_function);
					setState(77);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(78);
					operation();
					setState(79);
					term();
					}
					} 
				}
				setState(85);
				_errHandler.sync(this);
<<<<<<< HEAD
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
=======
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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

<<<<<<< HEAD
=======
	public static class FunctionContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitFunction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_function);
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARIABLE:
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(62);
				value();
				setState(63);
				operation();
				setState(64);
				term();
				}
				break;
			case ADD:
			case SUBTRACT:
			case MULTIPLY:
			case DIVIDE:
			case POWER:
				enterOuterAlt(_localctx, 2);
				{
				setState(66);
				operation();
				setState(67);
				term();
				setState(68);
				match(T__2);
				setState(69);
				term();
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

>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
	public static class ValueContext extends ParserRuleContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitValue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitValue(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_value);
		try {
<<<<<<< HEAD
			setState(88);
=======
			setState(75);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
<<<<<<< HEAD
				setState(86);
=======
				setState(73);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
				number();
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 2);
				{
<<<<<<< HEAD
				setState(87);
=======
				setState(74);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitVariable(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
<<<<<<< HEAD
			setState(90);
=======
			setState(77);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitLambda_variable(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Lambda_variableContext lambda_variable() throws RecognitionException {
		Lambda_variableContext _localctx = new Lambda_variableContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_lambda_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
<<<<<<< HEAD
			setState(92);
=======
			setState(79);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitNumber(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
<<<<<<< HEAD
			setState(94);
=======
			setState(81);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LambdaCalculusVisitor ) return ((LambdaCalculusVisitor<? extends T>)visitor).visitOperation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final OperationContext operation() throws RecognitionException {
		OperationContext _localctx = new OperationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_operation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
<<<<<<< HEAD
			setState(96);
=======
			setState(83);
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
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
<<<<<<< HEAD
		case 1:
=======
		case 4:
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
			return application_sempred((ApplicationContext)_localctx, predIndex);
		case 4:
			return function_sempred((FunctionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean application_sempred(ApplicationContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean function_sempred(FunctionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
<<<<<<< HEAD
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16e\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3"+
		"\2\3\2\3\2\3\2\5\2\33\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\5\3+\n\3\3\3\3\3\7\3/\n\3\f\3\16\3\62\13\3\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\5\4<\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\5\6N\n\6\3\6\3\6\3\6\3\6\7\6T\n\6\f\6\16\6W\13"+
		"\6\3\7\3\7\5\7[\n\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\2\4\4\n\f\2"+
		"\4\6\b\n\f\16\20\22\24\2\3\3\2\7\13\2f\2\32\3\2\2\2\4*\3\2\2\2\6;\3\2"+
		"\2\2\b=\3\2\2\2\nM\3\2\2\2\fZ\3\2\2\2\16\\\3\2\2\2\20^\3\2\2\2\22`\3\2"+
		"\2\2\24b\3\2\2\2\26\33\5\6\4\2\27\33\5\n\6\2\30\33\5\f\7\2\31\33\5\4\3"+
		"\2\32\26\3\2\2\2\32\27\3\2\2\2\32\30\3\2\2\2\32\31\3\2\2\2\33\3\3\2\2"+
		"\2\34\35\b\3\1\2\35\36\5\6\4\2\36\37\5\2\2\2\37+\3\2\2\2 !\5\f\7\2!\""+
		"\5\2\2\2\"+\3\2\2\2#$\5\n\6\2$%\5\2\2\2%+\3\2\2\2&\'\7\f\2\2\'(\5\4\3"+
		"\2()\7\r\2\2)+\3\2\2\2*\34\3\2\2\2* \3\2\2\2*#\3\2\2\2*&\3\2\2\2+\60\3"+
		"\2\2\2,-\f\7\2\2-/\5\2\2\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2"+
		"\2\2\61\5\3\2\2\2\62\60\3\2\2\2\63\64\5\b\5\2\64\65\7\3\2\2\65\66\5\2"+
		"\2\2\66<\3\2\2\2\678\7\f\2\289\5\6\4\29:\7\r\2\2:<\3\2\2\2;\63\3\2\2\2"+
		";\67\3\2\2\2<\7\3\2\2\2=>\7\4\2\2>?\5\20\t\2?\t\3\2\2\2@A\b\6\1\2AB\5"+
		"\f\7\2BC\5\24\13\2CD\5\2\2\2DN\3\2\2\2EF\5\6\4\2FG\5\24\13\2GH\5\2\2\2"+
		"HN\3\2\2\2IJ\7\f\2\2JK\5\n\6\2KL\7\r\2\2LN\3\2\2\2M@\3\2\2\2ME\3\2\2\2"+
		"MI\3\2\2\2NU\3\2\2\2OP\f\5\2\2PQ\5\24\13\2QR\5\2\2\2RT\3\2\2\2SO\3\2\2"+
		"\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\13\3\2\2\2WU\3\2\2\2X[\5\22\n\2Y[\5"+
		"\16\b\2ZX\3\2\2\2ZY\3\2\2\2[\r\3\2\2\2\\]\7\5\2\2]\17\3\2\2\2^_\7\5\2"+
		"\2_\21\3\2\2\2`a\7\6\2\2a\23\3\2\2\2bc\t\2\2\2c\25\3\2\2\2\t\32*\60;M"+
		"UZ";
=======
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17X\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\3\2\3\2\3\2\3\2\3\2\5\2\36\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4"+
		"\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\68"+
		"\n\6\3\6\3\6\7\6<\n\6\f\6\16\6?\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\5\7J\n\7\3\b\3\b\5\bN\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\3"+
		"\n\r\2\4\6\b\n\f\16\20\22\24\26\2\3\3\2\b\f\2V\2\35\3\2\2\2\4\37\3\2\2"+
		"\2\6#\3\2\2\2\b\'\3\2\2\2\n\67\3\2\2\2\fI\3\2\2\2\16M\3\2\2\2\20O\3\2"+
		"\2\2\22Q\3\2\2\2\24S\3\2\2\2\26U\3\2\2\2\30\36\5\f\7\2\31\36\5\6\4\2\32"+
		"\36\5\n\6\2\33\36\5\16\b\2\34\36\5\4\3\2\35\30\3\2\2\2\35\31\3\2\2\2\35"+
		"\32\3\2\2\2\35\33\3\2\2\2\35\34\3\2\2\2\36\3\3\2\2\2\37 \7\r\2\2 !\5\2"+
		"\2\2!\"\7\16\2\2\"\5\3\2\2\2#$\5\b\5\2$%\7\3\2\2%&\5\2\2\2&\7\3\2\2\2"+
		"\'(\7\4\2\2()\5\22\n\2)\t\3\2\2\2*+\b\6\1\2+,\5\f\7\2,-\5\2\2\2-8\3\2"+
		"\2\2./\5\6\4\2/\60\5\2\2\2\608\3\2\2\2\61\62\5\16\b\2\62\63\5\2\2\2\63"+
		"8\3\2\2\2\64\65\5\4\3\2\65\66\5\2\2\2\668\3\2\2\2\67*\3\2\2\2\67.\3\2"+
		"\2\2\67\61\3\2\2\2\67\64\3\2\2\28=\3\2\2\29:\f\5\2\2:<\5\2\2\2;9\3\2\2"+
		"\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\13\3\2\2\2?=\3\2\2\2@A\5\16\b\2AB\5"+
		"\26\f\2BC\5\2\2\2CJ\3\2\2\2DE\5\26\f\2EF\5\2\2\2FG\7\5\2\2GH\5\2\2\2H"+
		"J\3\2\2\2I@\3\2\2\2ID\3\2\2\2J\r\3\2\2\2KN\5\24\13\2LN\5\20\t\2MK\3\2"+
		"\2\2ML\3\2\2\2N\17\3\2\2\2OP\7\6\2\2P\21\3\2\2\2QR\7\6\2\2R\23\3\2\2\2"+
		"ST\7\7\2\2T\25\3\2\2\2UV\t\2\2\2V\27\3\2\2\2\7\35\67=IM";
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}