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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, NUMBER=14, BOOL=15, VARIABLE=16, 
		ADD=17, SUBTRACT=18, MULTIPLY=19, DIVIDE=20, POWER=21, LBRACKET=22, RBRACKET=23, 
		AND=24, OR=25, GT=26, LT=27, EQ=28, WS=29;
	public static final int
		RULE_term = 0, RULE_application = 1, RULE_abstraction = 2, RULE_abstraction_term = 3, 
		RULE_function = 4, RULE_value = 5, RULE_variable = 6, RULE_number = 7, 
		RULE_boolean_value = 8, RULE_function_type = 9, RULE_ground_type = 10, 
		RULE_operation = 11;
	public static final String[] ruleNames = {
		"term", "application", "abstraction", "abstraction_term", "function", 
		"value", "variable", "number", "boolean_value", "function_type", "ground_type", 
		"operation"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'.'", "'%'", "':'", "'->'", "'Bool'", "'bool'", "'BOOL'", "'Int'", 
		"'int'", "'INT'", "'None'", "'none'", "'NONE'", null, null, null, "'+'", 
		"'-'", "'*'", "'/'", "'^'", "'('", "')'", "'&'", "'|'", "'>'", "'<'", 
		"'=='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, "NUMBER", "BOOL", "VARIABLE", "ADD", "SUBTRACT", "MULTIPLY", 
		"DIVIDE", "POWER", "LBRACKET", "RBRACKET", "AND", "OR", "GT", "LT", "EQ", 
		"WS"
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
			setState(28);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				abstraction();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(25);
				function(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(26);
				value();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(27);
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
			setState(44);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(31);
				abstraction();
				setState(32);
				term();
				}
				break;
			case 2:
				{
				setState(34);
				value();
				setState(35);
				term();
				}
				break;
			case 3:
				{
				setState(37);
				function(0);
				setState(38);
				term();
				}
				break;
			case 4:
				{
				setState(40);
				match(LBRACKET);
				setState(41);
				application(0);
				setState(42);
				match(RBRACKET);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(50);
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
					setState(46);
					if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
					setState(47);
					term();
					}
					} 
				}
				setState(52);
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
		public TerminalNode LBRACKET() { return getToken(LambdaCalculusParser.LBRACKET, 0); }
		public AbstractionContext abstraction() {
			return getRuleContext(AbstractionContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(LambdaCalculusParser.RBRACKET, 0); }
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
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				abstraction_term();
				setState(54);
				match(T__0);
				setState(55);
				term();
				}
				break;
			case LBRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				match(LBRACKET);
				setState(58);
				abstraction();
				setState(59);
				match(RBRACKET);
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

	public static class Abstraction_termContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
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
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(T__1);
			setState(64);
			variable();
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
		public TerminalNode LBRACKET() { return getToken(LambdaCalculusParser.LBRACKET, 0); }
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(LambdaCalculusParser.RBRACKET, 0); }
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
		return function(0);
	}

	private FunctionContext function(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		FunctionContext _localctx = new FunctionContext(_ctx, _parentState);
		FunctionContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_function, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(67);
				value();
				setState(68);
				operation();
				setState(69);
				term();
				}
				break;
			case 2:
				{
				setState(71);
				abstraction();
				setState(72);
				operation();
				setState(73);
				term();
				}
				break;
			case 3:
				{
				setState(75);
				match(LBRACKET);
				setState(76);
				function(0);
				setState(77);
				match(RBRACKET);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(87);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new FunctionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_function);
					setState(81);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(82);
					operation();
					setState(83);
					term();
					}
					} 
				}
				setState(89);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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

	public static class ValueContext extends ParserRuleContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public Boolean_valueContext boolean_value() {
			return getRuleContext(Boolean_valueContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode LBRACKET() { return getToken(LambdaCalculusParser.LBRACKET, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(LambdaCalculusParser.RBRACKET, 0); }
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
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_value);
		try {
			setState(97);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				number();
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 2);
				{
				setState(91);
				boolean_value();
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 3);
				{
				setState(92);
				variable();
				}
				break;
			case LBRACKET:
				enterOuterAlt(_localctx, 4);
				{
				setState(93);
				match(LBRACKET);
				setState(94);
				value();
				setState(95);
				match(RBRACKET);
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
		public Function_typeContext function_type() {
			return getRuleContext(Function_typeContext.class,0);
		}
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
		enterRule(_localctx, 12, RULE_variable);
		try {
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(99);
				match(VARIABLE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(100);
				match(VARIABLE);
				setState(101);
				match(T__2);
				setState(102);
				function_type(0);
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

	public static class NumberContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LambdaCalculusParser.NUMBER, 0); }
		public Function_typeContext function_type() {
			return getRuleContext(Function_typeContext.class,0);
		}
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
		enterRule(_localctx, 14, RULE_number);
		try {
			setState(109);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(105);
				match(NUMBER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(106);
				match(NUMBER);
				setState(107);
				match(T__2);
				setState(108);
				function_type(0);
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

	public static class Boolean_valueContext extends ParserRuleContext {
		public TerminalNode BOOL() { return getToken(LambdaCalculusParser.BOOL, 0); }
		public Function_typeContext function_type() {
			return getRuleContext(Function_typeContext.class,0);
		}
		public Boolean_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolean_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterBoolean_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitBoolean_value(this);
		}
	}

	public final Boolean_valueContext boolean_value() throws RecognitionException {
		Boolean_valueContext _localctx = new Boolean_valueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_boolean_value);
		try {
			setState(115);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(111);
				match(BOOL);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(112);
				match(BOOL);
				setState(113);
				match(T__2);
				setState(114);
				function_type(0);
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

	public static class Function_typeContext extends ParserRuleContext {
		public Ground_typeContext ground_type() {
			return getRuleContext(Ground_typeContext.class,0);
		}
		public List<Function_typeContext> function_type() {
			return getRuleContexts(Function_typeContext.class);
		}
		public Function_typeContext function_type(int i) {
			return getRuleContext(Function_typeContext.class,i);
		}
		public Function_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterFunction_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitFunction_type(this);
		}
	}

	public final Function_typeContext function_type() throws RecognitionException {
		return function_type(0);
	}

	private Function_typeContext function_type(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Function_typeContext _localctx = new Function_typeContext(_ctx, _parentState);
		Function_typeContext _prevctx = _localctx;
		int _startState = 18;
		enterRecursionRule(_localctx, 18, RULE_function_type, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(118);
			ground_type();
			}
			_ctx.stop = _input.LT(-1);
			setState(125);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Function_typeContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_function_type);
					setState(120);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(121);
					match(T__3);
					setState(122);
					function_type(2);
					}
					} 
				}
				setState(127);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
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

	public static class Ground_typeContext extends ParserRuleContext {
		public Ground_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ground_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).enterGround_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LambdaCalculusListener ) ((LambdaCalculusListener)listener).exitGround_type(this);
		}
	}

	public final Ground_typeContext ground_type() throws RecognitionException {
		Ground_typeContext _localctx = new Ground_typeContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_ground_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12))) != 0)) ) {
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

	public static class OperationContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(LambdaCalculusParser.ADD, 0); }
		public TerminalNode SUBTRACT() { return getToken(LambdaCalculusParser.SUBTRACT, 0); }
		public TerminalNode MULTIPLY() { return getToken(LambdaCalculusParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(LambdaCalculusParser.DIVIDE, 0); }
		public TerminalNode POWER() { return getToken(LambdaCalculusParser.POWER, 0); }
		public TerminalNode AND() { return getToken(LambdaCalculusParser.AND, 0); }
		public TerminalNode OR() { return getToken(LambdaCalculusParser.OR, 0); }
		public TerminalNode GT() { return getToken(LambdaCalculusParser.GT, 0); }
		public TerminalNode LT() { return getToken(LambdaCalculusParser.LT, 0); }
		public TerminalNode EQ() { return getToken(LambdaCalculusParser.EQ, 0); }
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
		enterRule(_localctx, 22, RULE_operation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADD) | (1L << SUBTRACT) | (1L << MULTIPLY) | (1L << DIVIDE) | (1L << POWER) | (1L << AND) | (1L << OR) | (1L << GT) | (1L << LT) | (1L << EQ))) != 0)) ) {
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
		case 1:
			return application_sempred((ApplicationContext)_localctx, predIndex);
		case 4:
			return function_sempred((FunctionContext)_localctx, predIndex);
		case 9:
			return function_type_sempred((Function_typeContext)_localctx, predIndex);
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
	private boolean function_type_sempred(Function_typeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37\u0087\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\3\2\3\2\3\2\3\2\5\2\37\n\2\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3/\n\3\3\3\3\3\7\3\63\n\3\f\3\16"+
		"\3\66\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4@\n\4\3\5\3\5\3\5\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6R\n\6\3\6\3\6\3\6\3"+
		"\6\7\6X\n\6\f\6\16\6[\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7d\n\7\3\b\3"+
		"\b\3\b\3\b\5\bj\n\b\3\t\3\t\3\t\3\t\5\tp\n\t\3\n\3\n\3\n\3\n\5\nv\n\n"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\7\13~\n\13\f\13\16\13\u0081\13\13\3\f\3"+
		"\f\3\r\3\r\3\r\2\5\4\n\24\16\2\4\6\b\n\f\16\20\22\24\26\30\2\4\3\2\7\17"+
		"\4\2\23\27\32\36\2\u008c\2\36\3\2\2\2\4.\3\2\2\2\6?\3\2\2\2\bA\3\2\2\2"+
		"\nQ\3\2\2\2\fc\3\2\2\2\16i\3\2\2\2\20o\3\2\2\2\22u\3\2\2\2\24w\3\2\2\2"+
		"\26\u0082\3\2\2\2\30\u0084\3\2\2\2\32\37\5\6\4\2\33\37\5\n\6\2\34\37\5"+
		"\f\7\2\35\37\5\4\3\2\36\32\3\2\2\2\36\33\3\2\2\2\36\34\3\2\2\2\36\35\3"+
		"\2\2\2\37\3\3\2\2\2 !\b\3\1\2!\"\5\6\4\2\"#\5\2\2\2#/\3\2\2\2$%\5\f\7"+
		"\2%&\5\2\2\2&/\3\2\2\2\'(\5\n\6\2()\5\2\2\2)/\3\2\2\2*+\7\30\2\2+,\5\4"+
		"\3\2,-\7\31\2\2-/\3\2\2\2. \3\2\2\2.$\3\2\2\2.\'\3\2\2\2.*\3\2\2\2/\64"+
		"\3\2\2\2\60\61\f\7\2\2\61\63\5\2\2\2\62\60\3\2\2\2\63\66\3\2\2\2\64\62"+
		"\3\2\2\2\64\65\3\2\2\2\65\5\3\2\2\2\66\64\3\2\2\2\678\5\b\5\289\7\3\2"+
		"\29:\5\2\2\2:@\3\2\2\2;<\7\30\2\2<=\5\6\4\2=>\7\31\2\2>@\3\2\2\2?\67\3"+
		"\2\2\2?;\3\2\2\2@\7\3\2\2\2AB\7\4\2\2BC\5\16\b\2C\t\3\2\2\2DE\b\6\1\2"+
		"EF\5\f\7\2FG\5\30\r\2GH\5\2\2\2HR\3\2\2\2IJ\5\6\4\2JK\5\30\r\2KL\5\2\2"+
		"\2LR\3\2\2\2MN\7\30\2\2NO\5\n\6\2OP\7\31\2\2PR\3\2\2\2QD\3\2\2\2QI\3\2"+
		"\2\2QM\3\2\2\2RY\3\2\2\2ST\f\5\2\2TU\5\30\r\2UV\5\2\2\2VX\3\2\2\2WS\3"+
		"\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\13\3\2\2\2[Y\3\2\2\2\\d\5\20\t\2"+
		"]d\5\22\n\2^d\5\16\b\2_`\7\30\2\2`a\5\f\7\2ab\7\31\2\2bd\3\2\2\2c\\\3"+
		"\2\2\2c]\3\2\2\2c^\3\2\2\2c_\3\2\2\2d\r\3\2\2\2ej\7\22\2\2fg\7\22\2\2"+
		"gh\7\5\2\2hj\5\24\13\2ie\3\2\2\2if\3\2\2\2j\17\3\2\2\2kp\7\20\2\2lm\7"+
		"\20\2\2mn\7\5\2\2np\5\24\13\2ok\3\2\2\2ol\3\2\2\2p\21\3\2\2\2qv\7\21\2"+
		"\2rs\7\21\2\2st\7\5\2\2tv\5\24\13\2uq\3\2\2\2ur\3\2\2\2v\23\3\2\2\2wx"+
		"\b\13\1\2xy\5\26\f\2y\177\3\2\2\2z{\f\3\2\2{|\7\6\2\2|~\5\24\13\4}z\3"+
		"\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\25\3\2\2\2"+
		"\u0081\177\3\2\2\2\u0082\u0083\t\2\2\2\u0083\27\3\2\2\2\u0084\u0085\t"+
		"\3\2\2\u0085\31\3\2\2\2\r\36.\64?QYciou\177";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}