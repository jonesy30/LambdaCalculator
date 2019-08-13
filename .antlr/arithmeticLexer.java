// Generated from c:\Users\Yola\git\LambdaCalculator\arithmetic.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class arithmeticLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUMBER=1, BOOL=2, VARIABLE=3, ADD=4, SUBTRACT=5, MULTIPLY=6, DIVIDE=7, 
		POWER=8, LBRACKET=9, RBRACKET=10, AND=11, OR=12, GT=13, LT=14, EQ=15, 
		WS=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"NUMBER", "BOOL", "VARIABLE", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
		"POWER", "LBRACKET", "RBRACKET", "AND", "OR", "GT", "LT", "EQ", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'", 
		"'&'", "'|'", "'>'", "'<'", "'=='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "NUMBER", "BOOL", "VARIABLE", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
		"POWER", "LBRACKET", "RBRACKET", "AND", "OR", "GT", "LT", "EQ", "WS"
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


	public arithmeticLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "arithmetic.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22g\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\6\2%\n"+
		"\2\r\2\16\2&\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3D\n\3\3\4\3\4\3"+
		"\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3"+
		"\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\6\21b\n\21\r\21\16\21c\3\21"+
		"\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16"+
		"\33\17\35\20\37\21!\22\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2m\2"+
		"\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2"+
		"\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2"+
		"\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3$\3\2\2"+
		"\2\5C\3\2\2\2\7E\3\2\2\2\tG\3\2\2\2\13I\3\2\2\2\rK\3\2\2\2\17M\3\2\2\2"+
		"\21O\3\2\2\2\23Q\3\2\2\2\25S\3\2\2\2\27U\3\2\2\2\31W\3\2\2\2\33Y\3\2\2"+
		"\2\35[\3\2\2\2\37]\3\2\2\2!a\3\2\2\2#%\t\2\2\2$#\3\2\2\2%&\3\2\2\2&$\3"+
		"\2\2\2&\'\3\2\2\2\'\4\3\2\2\2()\7V\2\2)*\7T\2\2*+\7W\2\2+D\7G\2\2,-\7"+
		"v\2\2-.\7t\2\2./\7w\2\2/D\7g\2\2\60\61\7V\2\2\61\62\7t\2\2\62\63\7w\2"+
		"\2\63D\7g\2\2\64\65\7H\2\2\65\66\7C\2\2\66\67\7N\2\2\678\7U\2\28D\7G\2"+
		"\29:\7h\2\2:;\7c\2\2;<\7n\2\2<=\7u\2\2=D\7g\2\2>?\7H\2\2?@\7c\2\2@A\7"+
		"n\2\2AB\7u\2\2BD\7g\2\2C(\3\2\2\2C,\3\2\2\2C\60\3\2\2\2C\64\3\2\2\2C9"+
		"\3\2\2\2C>\3\2\2\2D\6\3\2\2\2EF\t\3\2\2F\b\3\2\2\2GH\7-\2\2H\n\3\2\2\2"+
		"IJ\7/\2\2J\f\3\2\2\2KL\7,\2\2L\16\3\2\2\2MN\7\61\2\2N\20\3\2\2\2OP\7`"+
		"\2\2P\22\3\2\2\2QR\7*\2\2R\24\3\2\2\2ST\7+\2\2T\26\3\2\2\2UV\7(\2\2V\30"+
		"\3\2\2\2WX\7~\2\2X\32\3\2\2\2YZ\7@\2\2Z\34\3\2\2\2[\\\7>\2\2\\\36\3\2"+
		"\2\2]^\7?\2\2^_\7?\2\2_ \3\2\2\2`b\t\4\2\2a`\3\2\2\2bc\3\2\2\2ca\3\2\2"+
		"\2cd\3\2\2\2de\3\2\2\2ef\b\21\2\2f\"\3\2\2\2\6\2&Cc\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}