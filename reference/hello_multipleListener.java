// Generated from hello_multiple.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link hello_multipleParser}.
 */
public interface hello_multipleListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link hello_multipleParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(hello_multipleParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link hello_multipleParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(hello_multipleParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link hello_multipleParser#hi}.
	 * @param ctx the parse tree
	 */
	void enterHi(hello_multipleParser.HiContext ctx);
	/**
	 * Exit a parse tree produced by {@link hello_multipleParser#hi}.
	 * @param ctx the parse tree
	 */
	void exitHi(hello_multipleParser.HiContext ctx);
}