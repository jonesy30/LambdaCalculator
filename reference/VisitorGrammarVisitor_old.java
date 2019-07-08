// Generated from VisitorGrammar.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link VisitorGrammarParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface VisitorGrammarVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link VisitorGrammarParser#number}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumber(VisitorGrammarParser.NumberContext ctx);
	/**
	 * Visit a parse tree produced by {@link VisitorGrammarParser#fromUomCode}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFromUomCode(VisitorGrammarParser.FromUomCodeContext ctx);
	/**
	 * Visit a parse tree produced by {@link VisitorGrammarParser#toUomCode}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToUomCode(VisitorGrammarParser.ToUomCodeContext ctx);
	/**
	 * Visit a parse tree produced by {@link VisitorGrammarParser#fxRateFunc}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFxRateFunc(VisitorGrammarParser.FxRateFuncContext ctx);
	/**
	 * Visit a parse tree produced by {@link VisitorGrammarParser#currencyPair}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCurrencyPair(VisitorGrammarParser.CurrencyPairContext ctx);
	/**
	 * Visit a parse tree produced by {@link VisitorGrammarParser#uomConvertFunc}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUomConvertFunc(VisitorGrammarParser.UomConvertFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code parens}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParens(VisitorGrammarParser.ParensContext ctx);
	/**
	 * Visit a parse tree produced by the {@code fxRate}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFxRate(VisitorGrammarParser.FxRateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code num}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNum(VisitorGrammarParser.NumContext ctx);
	/**
	 * Visit a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddSub(VisitorGrammarParser.AddSubContext ctx);
	/**
	 * Visit a parse tree produced by the {@code uomFactor}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUomFactor(VisitorGrammarParser.UomFactorContext ctx);
	/**
	 * Visit a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMulDiv(VisitorGrammarParser.MulDivContext ctx);
}