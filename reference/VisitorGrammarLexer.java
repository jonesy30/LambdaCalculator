// Generated from VisitorGrammar.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class VisitorGrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, INT=6, FLOAT=7, STRING_LITERAL=8, 
		NAME=9, IDENTIFIER=10, MUL=11, DIV=12, ADD=13, SUB=14, WS=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "DIGIT", "LETTER", "INT", "FLOAT", 
		"STRING_LITERAL", "NAME", "IDENTIFIER", "MUL", "DIV", "ADD", "SUB", "WS"
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


	public VisitorGrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "VisitorGrammar.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21v\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\tC\n\t\r\t\16\tD\3\n"+
		"\6\nH\n\n\r\n\16\nI\3\n\3\n\6\nN\n\n\r\n\16\nO\3\13\3\13\7\13T\n\13\f"+
		"\13\16\13W\13\13\3\13\3\13\3\f\3\f\3\f\7\f^\n\f\f\f\16\fa\13\f\3\r\6\r"+
		"d\n\r\r\r\16\re\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\6\22q\n\22"+
		"\r\22\16\22r\3\22\3\22\3U\2\23\3\3\5\4\7\5\t\6\13\7\r\2\17\2\21\b\23\t"+
		"\25\n\27\13\31\f\33\r\35\16\37\17!\20#\21\3\2\6\3\2\62;\4\2C\\c|\5\2\62"+
		";C\\c|\4\2\13\f\17\17\2{\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2"+
		"\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2"+
		"\2\3%\3\2\2\2\5,\3\2\2\2\7.\3\2\2\2\t\60\3\2\2\2\13;\3\2\2\2\r=\3\2\2"+
		"\2\17?\3\2\2\2\21B\3\2\2\2\23G\3\2\2\2\25Q\3\2\2\2\27Z\3\2\2\2\31c\3\2"+
		"\2\2\33g\3\2\2\2\35i\3\2\2\2\37k\3\2\2\2!m\3\2\2\2#p\3\2\2\2%&\7H\2\2"+
		"&\'\7Z\2\2\'(\7T\2\2()\7c\2\2)*\7v\2\2*+\7g\2\2+\4\3\2\2\2,-\7*\2\2-\6"+
		"\3\2\2\2./\7+\2\2/\b\3\2\2\2\60\61\7W\2\2\61\62\7q\2\2\62\63\7o\2\2\63"+
		"\64\7E\2\2\64\65\7q\2\2\65\66\7p\2\2\66\67\7x\2\2\678\7g\2\289\7t\2\2"+
		"9:\7v\2\2:\n\3\2\2\2;<\7.\2\2<\f\3\2\2\2=>\t\2\2\2>\16\3\2\2\2?@\t\3\2"+
		"\2@\20\3\2\2\2AC\5\r\7\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\22\3"+
		"\2\2\2FH\5\r\7\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KM\7"+
		"\60\2\2LN\5\r\7\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\24\3\2\2\2"+
		"QU\7)\2\2RT\13\2\2\2SR\3\2\2\2TW\3\2\2\2UV\3\2\2\2US\3\2\2\2VX\3\2\2\2"+
		"WU\3\2\2\2XY\7)\2\2Y\26\3\2\2\2Z_\5\17\b\2[^\5\17\b\2\\^\5\r\7\2][\3\2"+
		"\2\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\30\3\2\2\2a_\3\2\2\2bd"+
		"\t\4\2\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\32\3\2\2\2gh\7,\2\2"+
		"h\34\3\2\2\2ij\7\61\2\2j\36\3\2\2\2kl\7-\2\2l \3\2\2\2mn\7/\2\2n\"\3\2"+
		"\2\2oq\t\5\2\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2\2st\3\2\2\2tu\b\22"+
		"\2\2u$\3\2\2\2\13\2DIOU]_er\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}