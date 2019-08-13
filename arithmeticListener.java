// Generated from arithmetic.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link arithmeticParser}.
 */
public interface arithmeticListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(arithmeticParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(arithmeticParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#multiplyingExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyingExpression(arithmeticParser.MultiplyingExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#multiplyingExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyingExpression(arithmeticParser.MultiplyingExpressionContext ctx);
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
	 * Enter a parse tree produced by {@link arithmeticParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(arithmeticParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(arithmeticParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link arithmeticParser#boolean_value}.
	 * @param ctx the parse tree
	 */
	void enterBoolean_value(arithmeticParser.Boolean_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link arithmeticParser#boolean_value}.
	 * @param ctx the parse tree
	 */
	void exitBoolean_value(arithmeticParser.Boolean_valueContext ctx);
}