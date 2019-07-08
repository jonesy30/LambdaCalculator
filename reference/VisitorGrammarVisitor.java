public class VisitorGrammarVisitor extends VisitorGrammarBaseVisitor<decimal>
{
    @override
    public float VisitParens(MyGrammarParser.ParensContext context)
    {
        return Visit(context.expr());
    }

    @override
    public float VisitNum(MyGrammarParser.NumContext context)
    {
        return decimal.Parse(context.GetText());
    }
 
    @override
    public float VisitAddSub(MyGrammarParser.AddSubContext context)
    {
        // The result of this should always be the operands 
        var left = Visit(context.expr(0));
        var right = Visit(context.expr(1));
        return context.op.Type == MyGrammarParser.ADD ? left + right : left - right;
    }

    @override
    public float VisitMulDiv(MyGrammarParser.MulDivContext context)
    {
        // The result of this should always be the operands 
        var left = Visit(context.expr(0));
        var right = Visit(context.expr(1));
        return context.op.Type == MyGrammarParser.MUL ? left * right : left / right;
    }
}