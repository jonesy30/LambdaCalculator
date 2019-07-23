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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, VARIABLE=6, NUMBER=7, ADD=8, SUBTRACT=9, 
		MULTIPLY=10, DIVIDE=11, POWER=12, LBRACKET=13, RBRACKET=14, WS=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "VARIABLE", "NUMBER", "ADD", "SUBTRACT", 
		"MULTIPLY", "DIVIDE", "POWER", "LBRACKET", "RBRACKET", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'.'", "'%'", "':'", "'Bool'", "'Int'", null, null, "'+'", "'-'", 
		"'*'", "'/'", "'^'", "'('", "')'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, "VARIABLE", "NUMBER", "ADD", "SUBTRACT", 
		"MULTIPLY", "DIVIDE", "POWER", "LBRACKET", "RBRACKET", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21L\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4"+
		"\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\6\b\64\n\b\r\b\16"+
		"\b\65\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3"+
		"\20\6\20G\n\20\r\20\16\20H\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17"+
		"\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2\5\4\2C\\c|\3\2\62"+
		";\5\2\13\f\17\17\"\"\2M\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13,\3\2\2\2\r\60\3\2"+
		"\2\2\17\63\3\2\2\2\21\67\3\2\2\2\239\3\2\2\2\25;\3\2\2\2\27=\3\2\2\2\31"+
		"?\3\2\2\2\33A\3\2\2\2\35C\3\2\2\2\37F\3\2\2\2!\"\7\60\2\2\"\4\3\2\2\2"+
		"#$\7\'\2\2$\6\3\2\2\2%&\7<\2\2&\b\3\2\2\2\'(\7D\2\2()\7q\2\2)*\7q\2\2"+
		"*+\7n\2\2+\n\3\2\2\2,-\7K\2\2-.\7p\2\2./\7v\2\2/\f\3\2\2\2\60\61\t\2\2"+
		"\2\61\16\3\2\2\2\62\64\t\3\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2"+
		"\2\65\66\3\2\2\2\66\20\3\2\2\2\678\7-\2\28\22\3\2\2\29:\7/\2\2:\24\3\2"+
		"\2\2;<\7,\2\2<\26\3\2\2\2=>\7\61\2\2>\30\3\2\2\2?@\7`\2\2@\32\3\2\2\2"+
		"AB\7*\2\2B\34\3\2\2\2CD\7+\2\2D\36\3\2\2\2EG\t\4\2\2FE\3\2\2\2GH\3\2\2"+
		"\2HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\20\2\2K \3\2\2\2\5\2\65H\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}