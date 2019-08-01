// Generated from LambdaCalculus.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LambdaCalculusLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, NUMBER=14, BOOL=15, VARIABLE=16, 
		ADD=17, SUBTRACT=18, MULTIPLY=19, DIVIDE=20, POWER=21, LBRACKET=22, RBRACKET=23, 
		AND=24, OR=25, GT=26, LT=27, EQ=28, WS=29;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "T__12", "NUMBER", "BOOL", "VARIABLE", "ADD", 
		"SUBTRACT", "MULTIPLY", "DIVIDE", "POWER", "LBRACKET", "RBRACKET", "AND", 
		"OR", "GT", "LT", "EQ", "WS"
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


	public LambdaCalculusLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "LambdaCalculus.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37\u00b4\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\3\2\3\2\3\3\3"+
		"\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b"+
		"\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3"+
		"\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\6\17"+
		"r\n\17\r\17\16\17s\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\5\20\u0091\n\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24"+
		"\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33"+
		"\3\34\3\34\3\35\3\35\3\35\3\36\6\36\u00af\n\36\r\36\16\36\u00b0\3\36\3"+
		"\36\2\2\37\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33"+
		"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67"+
		"\359\36;\37\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2\u00ba\2\3\3\2"+
		"\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17"+
		"\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2"+
		"\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3"+
		"\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3"+
		"\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\3"+
		"=\3\2\2\2\5?\3\2\2\2\7A\3\2\2\2\tC\3\2\2\2\13F\3\2\2\2\rK\3\2\2\2\17P"+
		"\3\2\2\2\21U\3\2\2\2\23Y\3\2\2\2\25]\3\2\2\2\27a\3\2\2\2\31f\3\2\2\2\33"+
		"k\3\2\2\2\35q\3\2\2\2\37\u0090\3\2\2\2!\u0092\3\2\2\2#\u0094\3\2\2\2%"+
		"\u0096\3\2\2\2\'\u0098\3\2\2\2)\u009a\3\2\2\2+\u009c\3\2\2\2-\u009e\3"+
		"\2\2\2/\u00a0\3\2\2\2\61\u00a2\3\2\2\2\63\u00a4\3\2\2\2\65\u00a6\3\2\2"+
		"\2\67\u00a8\3\2\2\29\u00aa\3\2\2\2;\u00ae\3\2\2\2=>\7\60\2\2>\4\3\2\2"+
		"\2?@\7\'\2\2@\6\3\2\2\2AB\7<\2\2B\b\3\2\2\2CD\7/\2\2DE\7@\2\2E\n\3\2\2"+
		"\2FG\7D\2\2GH\7q\2\2HI\7q\2\2IJ\7n\2\2J\f\3\2\2\2KL\7d\2\2LM\7q\2\2MN"+
		"\7q\2\2NO\7n\2\2O\16\3\2\2\2PQ\7D\2\2QR\7Q\2\2RS\7Q\2\2ST\7N\2\2T\20\3"+
		"\2\2\2UV\7K\2\2VW\7p\2\2WX\7v\2\2X\22\3\2\2\2YZ\7k\2\2Z[\7p\2\2[\\\7v"+
		"\2\2\\\24\3\2\2\2]^\7K\2\2^_\7P\2\2_`\7V\2\2`\26\3\2\2\2ab\7P\2\2bc\7"+
		"q\2\2cd\7p\2\2de\7g\2\2e\30\3\2\2\2fg\7p\2\2gh\7q\2\2hi\7p\2\2ij\7g\2"+
		"\2j\32\3\2\2\2kl\7P\2\2lm\7Q\2\2mn\7P\2\2no\7G\2\2o\34\3\2\2\2pr\t\2\2"+
		"\2qp\3\2\2\2rs\3\2\2\2sq\3\2\2\2st\3\2\2\2t\36\3\2\2\2uv\7V\2\2vw\7T\2"+
		"\2wx\7W\2\2x\u0091\7G\2\2yz\7v\2\2z{\7t\2\2{|\7w\2\2|\u0091\7g\2\2}~\7"+
		"V\2\2~\177\7t\2\2\177\u0080\7w\2\2\u0080\u0091\7g\2\2\u0081\u0082\7H\2"+
		"\2\u0082\u0083\7C\2\2\u0083\u0084\7N\2\2\u0084\u0085\7U\2\2\u0085\u0091"+
		"\7G\2\2\u0086\u0087\7h\2\2\u0087\u0088\7c\2\2\u0088\u0089\7n\2\2\u0089"+
		"\u008a\7u\2\2\u008a\u0091\7g\2\2\u008b\u008c\7H\2\2\u008c\u008d\7c\2\2"+
		"\u008d\u008e\7n\2\2\u008e\u008f\7u\2\2\u008f\u0091\7g\2\2\u0090u\3\2\2"+
		"\2\u0090y\3\2\2\2\u0090}\3\2\2\2\u0090\u0081\3\2\2\2\u0090\u0086\3\2\2"+
		"\2\u0090\u008b\3\2\2\2\u0091 \3\2\2\2\u0092\u0093\t\3\2\2\u0093\"\3\2"+
		"\2\2\u0094\u0095\7-\2\2\u0095$\3\2\2\2\u0096\u0097\7/\2\2\u0097&\3\2\2"+
		"\2\u0098\u0099\7,\2\2\u0099(\3\2\2\2\u009a\u009b\7\61\2\2\u009b*\3\2\2"+
		"\2\u009c\u009d\7`\2\2\u009d,\3\2\2\2\u009e\u009f\7*\2\2\u009f.\3\2\2\2"+
		"\u00a0\u00a1\7+\2\2\u00a1\60\3\2\2\2\u00a2\u00a3\7(\2\2\u00a3\62\3\2\2"+
		"\2\u00a4\u00a5\7~\2\2\u00a5\64\3\2\2\2\u00a6\u00a7\7@\2\2\u00a7\66\3\2"+
		"\2\2\u00a8\u00a9\7>\2\2\u00a98\3\2\2\2\u00aa\u00ab\7?\2\2\u00ab\u00ac"+
		"\7?\2\2\u00ac:\3\2\2\2\u00ad\u00af\t\4\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b0"+
		"\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2"+
		"\u00b3\b\36\2\2\u00b3<\3\2\2\2\6\2s\u0090\u00b0\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}