// Generated from LambdaCalculus.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link LambdaCalculusParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface LambdaCalculusVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(LambdaCalculusParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#application}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitApplication(LambdaCalculusParser.ApplicationContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#abstraction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbstraction(LambdaCalculusParser.AbstractionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#abstraction_term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbstraction_term(LambdaCalculusParser.Abstraction_termContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#function}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction(LambdaCalculusParser.FunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValue(LambdaCalculusParser.ValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable(LambdaCalculusParser.VariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#lambda_variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLambda_variable(LambdaCalculusParser.Lambda_variableContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#number}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumber(LambdaCalculusParser.NumberContext ctx);
	/**
	 * Visit a parse tree produced by {@link LambdaCalculusParser#operation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperation(LambdaCalculusParser.OperationContext ctx);
}