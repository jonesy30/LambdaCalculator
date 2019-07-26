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
		VARIABLE=10, NUMBER=11, ADD=12, SUBTRACT=13, MULTIPLY=14, DIVIDE=15, POWER=16, 
		LBRACKET=17, RBRACKET=18, WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"VARIABLE", "NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "POWER", 
		"LBRACKET", "RBRACKET", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'.'", "'%'", "':'", "'Bool'", "'bool'", "'BOOL'", "'Int'", "'int'", 
		"'INT'", null, null, "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, "VARIABLE", 
		"NUMBER", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "POWER", "LBRACKET", 
		"RBRACKET", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25f\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3"+
		"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n"+
		"\3\n\3\n\3\n\3\13\3\13\3\f\6\fN\n\f\r\f\16\fO\3\r\3\r\3\16\3\16\3\17\3"+
		"\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\6\24a\n\24\r\24\16\24"+
		"b\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r"+
		"\31\16\33\17\35\20\37\21!\22#\23%\24\'\25\3\2\5\4\2C\\c|\3\2\62;\5\2\13"+
		"\f\17\17\"\"\2g\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3"+
		"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7-\3\2"+
		"\2\2\t/\3\2\2\2\13\64\3\2\2\2\r9\3\2\2\2\17>\3\2\2\2\21B\3\2\2\2\23F\3"+
		"\2\2\2\25J\3\2\2\2\27M\3\2\2\2\31Q\3\2\2\2\33S\3\2\2\2\35U\3\2\2\2\37"+
		"W\3\2\2\2!Y\3\2\2\2#[\3\2\2\2%]\3\2\2\2\'`\3\2\2\2)*\7\60\2\2*\4\3\2\2"+
		"\2+,\7\'\2\2,\6\3\2\2\2-.\7<\2\2.\b\3\2\2\2/\60\7D\2\2\60\61\7q\2\2\61"+
		"\62\7q\2\2\62\63\7n\2\2\63\n\3\2\2\2\64\65\7d\2\2\65\66\7q\2\2\66\67\7"+
		"q\2\2\678\7n\2\28\f\3\2\2\29:\7D\2\2:;\7Q\2\2;<\7Q\2\2<=\7N\2\2=\16\3"+
		"\2\2\2>?\7K\2\2?@\7p\2\2@A\7v\2\2A\20\3\2\2\2BC\7k\2\2CD\7p\2\2DE\7v\2"+
		"\2E\22\3\2\2\2FG\7K\2\2GH\7P\2\2HI\7V\2\2I\24\3\2\2\2JK\t\2\2\2K\26\3"+
		"\2\2\2LN\t\3\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\30\3\2\2\2Q"+
		"R\7-\2\2R\32\3\2\2\2ST\7/\2\2T\34\3\2\2\2UV\7,\2\2V\36\3\2\2\2WX\7\61"+
		"\2\2X \3\2\2\2YZ\7`\2\2Z\"\3\2\2\2[\\\7*\2\2\\$\3\2\2\2]^\7+\2\2^&\3\2"+
		"\2\2_a\t\4\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2cd\3\2\2\2de\b\24"+
		"\2\2e(\3\2\2\2\5\2Ob\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}