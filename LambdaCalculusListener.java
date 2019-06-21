// Generated from LambdaCalculus.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LambdaCalculusParser}.
 */
public interface LambdaCalculusListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LambdaCalculusParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(LambdaCalculusParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link LambdaCalculusParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(LambdaCalculusParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link LambdaCalculusParser#abstraction}.
	 * @param ctx the parse tree
	 */
	void enterAbstraction(LambdaCalculusParser.AbstractionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LambdaCalculusParser#abstraction}.
	 * @param ctx the parse tree
	 */
	void exitAbstraction(LambdaCalculusParser.AbstractionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LambdaCalculusParser#application}.
	 * @param ctx the parse tree
	 */
	void enterApplication(LambdaCalculusParser.ApplicationContext ctx);
	/**
	 * Exit a parse tree produced by {@link LambdaCalculusParser#application}.
	 * @param ctx the parse tree
	 */
	void exitApplication(LambdaCalculusParser.ApplicationContext ctx);
	/**
	 * Enter a parse tree produced by {@link LambdaCalculusParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(LambdaCalculusParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LambdaCalculusParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(LambdaCalculusParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LambdaCalculusParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(LambdaCalculusParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LambdaCalculusParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(LambdaCalculusParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LambdaCalculusParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterOperation(LambdaCalculusParser.OperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link LambdaCalculusParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitOperation(LambdaCalculusParser.OperationContext ctx);
}