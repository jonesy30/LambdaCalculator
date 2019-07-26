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
		T__9=10, T__10=11, T__11=12, T__12=13, VARIABLE=14, NUMBER=15, ADD=16, 
		SUBTRACT=17, MULTIPLY=18, DIVIDE=19, POWER=20, LBRACKET=21, RBRACKET=22, 
		WS=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "T__12", "VARIABLE", "NUMBER", "ADD", "SUBTRACT", 
		"MULTIPLY", "DIVIDE", "POWER", "LBRACKET", "RBRACKET", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'.'", "'%'", "':'", "'->'", "'Bool'", "'bool'", "'BOOL'", "'Int'", 
		"'int'", "'INT'", "'None'", "'none'", "'NONE'", null, null, "'+'", "'-'", 
		"'*'", "'/'", "'^'", "'('", "')'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, "VARIABLE", "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
		"POWER", "LBRACKET", "RBRACKET", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31\u0080\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2"+
		"\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16"+
		"\3\17\3\17\3\20\6\20h\n\20\r\20\16\20i\3\21\3\21\3\22\3\22\3\23\3\23\3"+
		"\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\6\30{\n\30\r\30\16\30|\3\30"+
		"\3\30\2\2\31\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16"+
		"\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\3\2\5\4\2C\\c|\3\2"+
		"\62;\5\2\13\f\17\17\"\"\2\u0081\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2"+
		"\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2"+
		"\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2"+
		"\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2"+
		"\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3\61\3\2\2\2\5\63\3\2\2\2\7\65\3\2\2"+
		"\2\t\67\3\2\2\2\13:\3\2\2\2\r?\3\2\2\2\17D\3\2\2\2\21I\3\2\2\2\23M\3\2"+
		"\2\2\25Q\3\2\2\2\27U\3\2\2\2\31Z\3\2\2\2\33_\3\2\2\2\35d\3\2\2\2\37g\3"+
		"\2\2\2!k\3\2\2\2#m\3\2\2\2%o\3\2\2\2\'q\3\2\2\2)s\3\2\2\2+u\3\2\2\2-w"+
		"\3\2\2\2/z\3\2\2\2\61\62\7\60\2\2\62\4\3\2\2\2\63\64\7\'\2\2\64\6\3\2"+
		"\2\2\65\66\7<\2\2\66\b\3\2\2\2\678\7/\2\289\7@\2\29\n\3\2\2\2:;\7D\2\2"+
		";<\7q\2\2<=\7q\2\2=>\7n\2\2>\f\3\2\2\2?@\7d\2\2@A\7q\2\2AB\7q\2\2BC\7"+
		"n\2\2C\16\3\2\2\2DE\7D\2\2EF\7Q\2\2FG\7Q\2\2GH\7N\2\2H\20\3\2\2\2IJ\7"+
		"K\2\2JK\7p\2\2KL\7v\2\2L\22\3\2\2\2MN\7k\2\2NO\7p\2\2OP\7v\2\2P\24\3\2"+
		"\2\2QR\7K\2\2RS\7P\2\2ST\7V\2\2T\26\3\2\2\2UV\7P\2\2VW\7q\2\2WX\7p\2\2"+
		"XY\7g\2\2Y\30\3\2\2\2Z[\7p\2\2[\\\7q\2\2\\]\7p\2\2]^\7g\2\2^\32\3\2\2"+
		"\2_`\7P\2\2`a\7Q\2\2ab\7P\2\2bc\7G\2\2c\34\3\2\2\2de\t\2\2\2e\36\3\2\2"+
		"\2fh\t\3\2\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2j \3\2\2\2kl\7-\2"+
		"\2l\"\3\2\2\2mn\7/\2\2n$\3\2\2\2op\7,\2\2p&\3\2\2\2qr\7\61\2\2r(\3\2\2"+
		"\2st\7`\2\2t*\3\2\2\2uv\7*\2\2v,\3\2\2\2wx\7+\2\2x.\3\2\2\2y{\t\4\2\2"+
		"zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177\b\30\2\2\177\60"+
		"\3\2\2\2\5\2i|\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}