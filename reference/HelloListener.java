// Generated from Hello.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link HelloParser}.
 */
public interface HelloListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link HelloParser#hi}.
	 * @param ctx the parse tree
	 */
	void enterHi(HelloParser.HiContext ctx);
	/**
	 * Exit a parse tree produced by {@link HelloParser#hi}.
	 * @param ctx the parse tree
	 */
	void exitHi(HelloParser.HiContext ctx);
}