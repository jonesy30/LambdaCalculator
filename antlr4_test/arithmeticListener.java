// Generated from arithmetic.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link arithmeticParser}.
 */
public interface arithmeticListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#foo}.
	 * @param ctx the parse tree
	 */
	void enterFoo(arithmeticParser.FooContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#foo}.
	 * @param ctx the parse tree
	 */
	void exitFoo(arithmeticParser.FooContext ctx);
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#equation}.
	 * @param ctx the parse tree
	 */
	void enterEquation(arithmeticParser.EquationContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#equation}.
	 * @param ctx the parse tree
	 */
	void exitEquation(arithmeticParser.EquationContext ctx);
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(arithmeticParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(arithmeticParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(arithmeticParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(arithmeticParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#scientific}.
	 * @param ctx the parse tree
	 */
	void enterScientific(arithmeticParser.ScientificContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#scientific}.
	 * @param ctx the parse tree
	 */
	void exitScientific(arithmeticParser.ScientificContext ctx);
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(arithmeticParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(arithmeticParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#relop}.
	 * @param ctx the parse tree
	 */
	void enterRelop(arithmeticParser.RelopContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#relop}.
	 * @param ctx the parse tree
	 */
	void exitRelop(arithmeticParser.RelopContext ctx);
}