// Generated from VisitorGrammar.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class VisitorGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, INT=6, FLOAT=7, STRING_LITERAL=8, 
		NAME=9, IDENTIFIER=10, MUL=11, DIV=12, ADD=13, SUB=14, WS=15;
	public static final int
		RULE_number = 0, RULE_fromUomCode = 1, RULE_toUomCode = 2, RULE_fxRateFunc = 3, 
		RULE_currencyPair = 4, RULE_uomConvertFunc = 5, RULE_expr = 6;
	public static final String[] ruleNames = {
		"number", "fromUomCode", "toUomCode", "fxRateFunc", "currencyPair", "uomConvertFunc", 
		"expr"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'FXRate'", "'('", "')'", "'UomConvert'", "','", null, null, null, 
		null, null, "'*'", "'/'", "'+'", "'-'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, "INT", "FLOAT", "STRING_LITERAL", 
		"NAME", "IDENTIFIER", "MUL", "DIV", "ADD", "SUB", "WS"
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
	public String getGrammarFileName() { return "VisitorGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public VisitorGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class NumberContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(VisitorGrammarParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(VisitorGrammarParser.FLOAT, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterNumber(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitNumber(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitNumber(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
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

	public static class FromUomCodeContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(VisitorGrammarParser.NAME, 0); }
		public TerminalNode IDENTIFIER() { return getToken(VisitorGrammarParser.IDENTIFIER, 0); }
		public FromUomCodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fromUomCode; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterFromUomCode(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitFromUomCode(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitFromUomCode(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FromUomCodeContext fromUomCode() throws RecognitionException {
		FromUomCodeContext _localctx = new FromUomCodeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_fromUomCode);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			_la = _input.LA(1);
			if ( !(_la==NAME || _la==IDENTIFIER) ) {
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

	public static class ToUomCodeContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(VisitorGrammarParser.NAME, 0); }
		public TerminalNode IDENTIFIER() { return getToken(VisitorGrammarParser.IDENTIFIER, 0); }
		public ToUomCodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_toUomCode; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterToUomCode(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitToUomCode(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitToUomCode(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ToUomCodeContext toUomCode() throws RecognitionException {
		ToUomCodeContext _localctx = new ToUomCodeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_toUomCode);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			_la = _input.LA(1);
			if ( !(_la==NAME || _la==IDENTIFIER) ) {
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

	public static class FxRateFuncContext extends ParserRuleContext {
		public CurrencyPairContext currencyPair() {
			return getRuleContext(CurrencyPairContext.class,0);
		}
		public FxRateFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fxRateFunc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterFxRateFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitFxRateFunc(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitFxRateFunc(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FxRateFuncContext fxRateFunc() throws RecognitionException {
		FxRateFuncContext _localctx = new FxRateFuncContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_fxRateFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			match(T__0);
			setState(21);
			match(T__1);
			setState(22);
			currencyPair();
			setState(23);
			match(T__2);
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

	public static class CurrencyPairContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(VisitorGrammarParser.NAME, 0); }
		public CurrencyPairContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_currencyPair; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterCurrencyPair(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitCurrencyPair(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitCurrencyPair(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CurrencyPairContext currencyPair() throws RecognitionException {
		CurrencyPairContext _localctx = new CurrencyPairContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_currencyPair);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			match(NAME);
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

	public static class UomConvertFuncContext extends ParserRuleContext {
		public FromUomCodeContext fromUomCode() {
			return getRuleContext(FromUomCodeContext.class,0);
		}
		public ToUomCodeContext toUomCode() {
			return getRuleContext(ToUomCodeContext.class,0);
		}
		public UomConvertFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_uomConvertFunc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterUomConvertFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitUomConvertFunc(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitUomConvertFunc(this);
			else return visitor.visitChildren(this);
		}
	}

	public final UomConvertFuncContext uomConvertFunc() throws RecognitionException {
		UomConvertFuncContext _localctx = new UomConvertFuncContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_uomConvertFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			match(T__3);
			setState(28);
			match(T__1);
			setState(29);
			fromUomCode();
			setState(30);
			match(T__4);
			setState(31);
			toUomCode();
			setState(32);
			match(T__2);
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

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ParensContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParensContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterParens(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitParens(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitParens(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class FxRateContext extends ExprContext {
		public FxRateFuncContext fxRateFunc() {
			return getRuleContext(FxRateFuncContext.class,0);
		}
		public FxRateContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterFxRate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitFxRate(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitFxRate(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class NumContext extends ExprContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public NumContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterNum(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitNum(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitNum(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class AddSubContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(VisitorGrammarParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(VisitorGrammarParser.SUB, 0); }
		public AddSubContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterAddSub(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitAddSub(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitAddSub(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class UomFactorContext extends ExprContext {
		public UomConvertFuncContext uomConvertFunc() {
			return getRuleContext(UomConvertFuncContext.class,0);
		}
		public UomFactorContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterUomFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitUomFactor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitUomFactor(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class MulDivContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(VisitorGrammarParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(VisitorGrammarParser.DIV, 0); }
		public MulDivContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).enterMulDiv(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisitorGrammarListener ) ((VisitorGrammarListener)listener).exitMulDiv(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof VisitorGrammarVisitor ) return ((VisitorGrammarVisitor<? extends T>)visitor).visitMulDiv(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
				{
				_localctx = new NumContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(35);
				number();
				}
				break;
			case T__1:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(36);
				match(T__1);
				setState(37);
				expr(0);
				setState(38);
				match(T__2);
				}
				break;
			case T__0:
				{
				_localctx = new FxRateContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(40);
				fxRateFunc();
				}
				break;
			case T__3:
				{
				_localctx = new UomFactorContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(41);
				uomConvertFunc();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(52);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(50);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(44);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(45);
						((MulDivContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((MulDivContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(46);
						expr(7);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(47);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(48);
						((AddSubContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
							((AddSubContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(49);
						expr(6);
						}
						break;
					}
					} 
				}
				setState(54);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 6:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21:\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5"+
		"\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\5\b-\n\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\65\n\b\f\b\16\b8\13"+
		"\b\3\b\2\3\16\t\2\4\6\b\n\f\16\2\6\3\2\b\t\3\2\13\f\3\2\r\16\3\2\17\20"+
		"\2\67\2\20\3\2\2\2\4\22\3\2\2\2\6\24\3\2\2\2\b\26\3\2\2\2\n\33\3\2\2\2"+
		"\f\35\3\2\2\2\16,\3\2\2\2\20\21\t\2\2\2\21\3\3\2\2\2\22\23\t\3\2\2\23"+
		"\5\3\2\2\2\24\25\t\3\2\2\25\7\3\2\2\2\26\27\7\3\2\2\27\30\7\4\2\2\30\31"+
		"\5\n\6\2\31\32\7\5\2\2\32\t\3\2\2\2\33\34\7\13\2\2\34\13\3\2\2\2\35\36"+
		"\7\6\2\2\36\37\7\4\2\2\37 \5\4\3\2 !\7\7\2\2!\"\5\6\4\2\"#\7\5\2\2#\r"+
		"\3\2\2\2$%\b\b\1\2%-\5\2\2\2&\'\7\4\2\2\'(\5\16\b\2()\7\5\2\2)-\3\2\2"+
		"\2*-\5\b\5\2+-\5\f\7\2,$\3\2\2\2,&\3\2\2\2,*\3\2\2\2,+\3\2\2\2-\66\3\2"+
		"\2\2./\f\b\2\2/\60\t\4\2\2\60\65\5\16\b\t\61\62\f\7\2\2\62\63\t\5\2\2"+
		"\63\65\5\16\b\b\64.\3\2\2\2\64\61\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66"+
		"\67\3\2\2\2\67\17\3\2\2\28\66\3\2\2\2\5,\64\66";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}