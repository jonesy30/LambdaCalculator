public class VisitorGrammarExpressionEvaluator
{
    public float Eval(string inputExpression)
    {
        var stringReader = new StringReader(inputExpression);
        try
        {
            AntlrInputStream inputStream = new AntlrInputStream(stringReader);
            MyGrammarLexer lexer = new VisitorGrammarLexer(inputStream);
            CommonTokenStream tokens = new CommonTokenStream(lexer);
            MyGrammarParser parser = new VisitorGrammarParser(tokens);
            MyGrammarParser.expressionTree expressionTree = parser.expr();// lets parse the whole thing
            MyGrammarVisitor visitor = new VisitorGrammarVisitor(); // now that we have a "parsed expression"
            float result = visitor.Visit(expressionTree);  // let's visit all the nodes.
            return result;
        }
        finally {
            return null;
        }
    }
}