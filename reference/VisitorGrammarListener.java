// Generated from VisitorGrammar.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link VisitorGrammarParser}.
 */
public interface VisitorGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link VisitorGrammarParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(VisitorGrammarParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisitorGrammarParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(VisitorGrammarParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisitorGrammarParser#fromUomCode}.
	 * @param ctx the parse tree
	 */
	void enterFromUomCode(VisitorGrammarParser.FromUomCodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisitorGrammarParser#fromUomCode}.
	 * @param ctx the parse tree
	 */
	void exitFromUomCode(VisitorGrammarParser.FromUomCodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisitorGrammarParser#toUomCode}.
	 * @param ctx the parse tree
	 */
	void enterToUomCode(VisitorGrammarParser.ToUomCodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisitorGrammarParser#toUomCode}.
	 * @param ctx the parse tree
	 */
	void exitToUomCode(VisitorGrammarParser.ToUomCodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisitorGrammarParser#fxRateFunc}.
	 * @param ctx the parse tree
	 */
	void enterFxRateFunc(VisitorGrammarParser.FxRateFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisitorGrammarParser#fxRateFunc}.
	 * @param ctx the parse tree
	 */
	void exitFxRateFunc(VisitorGrammarParser.FxRateFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisitorGrammarParser#currencyPair}.
	 * @param ctx the parse tree
	 */
	void enterCurrencyPair(VisitorGrammarParser.CurrencyPairContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisitorGrammarParser#currencyPair}.
	 * @param ctx the parse tree
	 */
	void exitCurrencyPair(VisitorGrammarParser.CurrencyPairContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisitorGrammarParser#uomConvertFunc}.
	 * @param ctx the parse tree
	 */
	void enterUomConvertFunc(VisitorGrammarParser.UomConvertFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisitorGrammarParser#uomConvertFunc}.
	 * @param ctx the parse tree
	 */
	void exitUomConvertFunc(VisitorGrammarParser.UomConvertFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parens}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParens(VisitorGrammarParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parens}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParens(VisitorGrammarParser.ParensContext ctx);
	/**
	 * Enter a parse tree produced by the {@code fxRate}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFxRate(VisitorGrammarParser.FxRateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code fxRate}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFxRate(VisitorGrammarParser.FxRateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code num}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNum(VisitorGrammarParser.NumContext ctx);
	/**
	 * Exit a parse tree produced by the {@code num}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNum(VisitorGrammarParser.NumContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(VisitorGrammarParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(VisitorGrammarParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code uomFactor}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUomFactor(VisitorGrammarParser.UomFactorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code uomFactor}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUomFactor(VisitorGrammarParser.UomFactorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(VisitorGrammarParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link VisitorGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(VisitorGrammarParser.MulDivContext ctx);
}