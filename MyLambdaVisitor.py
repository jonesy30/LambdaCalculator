from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorPartial import calculate_alpha
from Stack import Stack
from antlr4 import *
#from antlr4.IntervalSet import Interval
from antlr4.TokenStreamRewriter import TokenStreamRewriter
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
    from .LambdaCalculusLexer import LambdaCalculusLexer
else:
    from LambdaCalculusParser import LambdaCalculusParser
    from LambdaCalculusLexer import LambdaCalculusLexer
import re
import sys

class MyLambdaVisitor(LambdaCalculusVisitor):
    
    ##Normal order reduction idea:
    #For application, get function and incoming expression from children and substitute
    #If there is still redexes left in the expression, visit corresponding children
    #This supports my use of visitors and not listeners

    def __init__(self,tokens):
        super()
        self.incoming_values = Stack() #This definitely needs renamed
        self.tokens = tokens
        #self.rewriter = TokenStreamRewriter(self.tokens)

    # def visit(self,tree):
    #     print("Am I here...?")
    #     print(tree)
    #     super().visit(tree)

    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):

        #TODO: CHANGE THIS TO CHECK FOR AN ABSTRACTION AS A CHILD, AND CHECK TO SEE IF THE CHILD IS ACTUALLY BEING CHANGED THROUGH THIS
        #TODO: When this is working (lol - optimism) - how do I decide what node I should become?
            #I guess this is done for me when I recreate the tree based on my input?
            #Do I need to be careful with [?/x] conversion here?
        
        #[a,b] = ctx.getSourceInterval()
        #print("Get tokenstreamrewriter text = "+self.rewriter.getText("default",a,b))

        #self.rewriter.replace("default",0,19,"Hello?")

        print("Application = "+ctx.getText())

        parentesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parentesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()

        expression = ctx.getChild(1).getText()
        #I'm pretty sure I need to visit this branch, because that just makes sense -- what if there's a term on this branch that needs evaluated?
        #But when do I visit it - do I visit it after I've got the application at the top?
        #Do I need to just keep it as a "node" placeholder and go back through the result, visiting any unvisited nodes until I have a complete string?
        #Maybe this? This sounds right
        #expression = self.visit(ctx.getChild(1))
        print("Expression in application = "+expression)
        self.incoming_values.push(expression) 
        #NOTE: what if a non-evaluator?
        #NOTE: have I fixed this? I may have done

        before_size = self.incoming_values.get_size()
        function = self.visit(ctx.getChild(0))
        after_size = self.incoming_values.get_size()

        #Ok, so this is a string not a node
        #print("In application "+str(ctx.getText()) +", type of function = "+str(type(ctx.getChild(0))))
        #print("What happens if I visit function again?")
        #self.incoming_values.push("Hello!")
        #print(str(self.visit(function)))

        # returned_function = function
        # if isinstance(ctx.getChild(0),LambdaCalculusParser.AbstractionContext):
        #     print("I am an abstraction - remove expression")
        # else:
        #     print("Not an abstraction -- keep expression")
        #     returned_function = function + expression
        #     self.incoming_values.pop()

        #returned_function = function
        #print("Text = "+returned_function.getText())

        # for node in returned_function:
        #     print("Text = "+node.getText())

        returned_function = []
        print("Function = "+str(function))

        for node in function:
            print("Term output = "+str(node))
            print("Type = "+str(type(node)))

            returned_function.append(node)

        print("Returned function = "+str(returned_function))

        print("Expression = "+expression)
        if before_size == after_size:
            # returned_function = function + expression
            # #returned_function.append(expression)
            # self.incoming_values.pop()
            returned_function.append(expression)
            self.incoming_values.pop()


        #returned_function = self.visit(ctx.getChild(0))
        #print("Function get child 2 = "+returned_function)

        print("Returned value in application = "+str(returned_function))

        #I think this has to be here, because I want to change myself to a new type depending on the input
        #But I still need to fix the term * term issue (left recursion)
        # stream = InputStream(returned_function)
        # lexer = LambdaCalculusLexer(stream)
        # #lexer = LambdaCalculusLexer(StdinStream())
        # tokens = CommonTokenStream(lexer)
        # parser = LambdaCalculusParser(tokens)
        # tree = parser.term()

        # ctx.removeLastChild()
        # ctx.addChild(tree.getChild(0))

        # print()
        # print("Adding tree")
        # print(str(type(tree)))
        # print("Node = "+tree.getChild(0).getText()+" type = "+str(type(tree.getChild(0))))

        # print()

        # print("In application "+str(ctx.getText()) +", type of function = "+str(type(ctx.getChild(0))))
        # print("My child = "+str(ctx.getChild(0).getText()))
        # print("Child type = "+str(type(ctx.getChild(0))))

        return returned_function

    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        return ctx.getText()

    # Visit a parse tree produced by LambdaCalculusParser#parenthesis.
    def visitParenthesis(self, ctx:LambdaCalculusParser.ParenthesisContext):
        #Label
        #print("P: "+ctx.getText())
        visit_children = self.visit(ctx.getChild(1))
        return "" + ctx.getChild(0).getText() + visit_children + ctx.getChild(2).getText()

        #return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()

    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        #return self.visitChildren(ctx)
        return ctx.getText()

    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        print("T: "+ctx.getText())

        # self.rewriter.replaceIndex(0,"DO SOMETHING")
        # self.rewriter.deleteIndex(0)

        # start_point = ctx.getSourceInterval()[0]
        # print("start point = "+str(start_point))
        # end_point = ctx.getSourceInterval()[1]
        # print("end point = "+str(end_point))

        # #ok, so I'm getting here, I'm getting the right tokens at least. I'm just not managing to replace anything.
        # token_stream = self.rewriter.getTokenStream()
        # #print("Ctx token = "+ctx.getToken(LambdaCalculusParser.TermContext,1))

        # #ok, this is a way to get the current tokens
        # [start,stop] = ctx.getSourceInterval()
        # self.rewriter.replaceIndex(start,"Hello?")

        # tokens = token_stream.getTokens(start,stop+1)

        # print("Tokens? ")

        # for token in tokens:
        #     token.text = "Hello?"
        #     self.rewriter.replaceSingleToken(token,"HELLO")
        #     print(token.text)
        # print("End of tokens")

        #print(str(token_stream.getText()))
        #print("Index = "+str(token_stream.index))
        #self.rewriter.deleteProgram()
        #print(str(self.rewriter.DEFAULT_PROGRAM_NAME))

        #The abstraction puts lambda terms into [?/x] form, this chunk of code just converts it back before it gets
        #passed to the user for readability
        
        #*************************************
        #NOTE TODO: GO BACK TO THIS AND WORK OUT HOW TO PRINT THE OUTPUT PROPERLY
        # depth = ctx.depth()
        # if depth == 1:
        #     output = str(self.visitChildren(ctx))
        #     container_match = re.search("\[(.*?)\]", output)

        #     while container_match is not None:
        #         bound_match = re.search("\/(.*?)\]", output)
        #         found_bound = bound_match.group(1)
        #         container_to_replace = container_match.group(0)
        #         output = output.replace(container_to_replace,"%"+found_bound+".")
        #         container_match = re.search("\[(.*?)\]", output)
            
        #     return output

        # else:
        #    return self.visitChildren(ctx)

        #NOTE: I should only be converting to text at the end
        depth = ctx.depth()
        if depth == 1:
            output_string = ""
            for term in self.visitChildren(ctx):
                print("Term output = "+str(term))
                print("Type = "+str(type(term)))

                if isinstance(term,str):
                    output_string = output_string + term
                else:
                    output_string = output_string + term.getText()
            
            return output_string
        else:
            returned = []
            for term in self.visitChildren(ctx):
                if isinstance(term, list):
                    for node in term:
                        returned.append(node)
                else:
                    returned.append(term)
            
            return returned
            #output_string = output_string+term.getText()

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        print("Abstraction = "+ctx.getText())

        #Pop the value as soon as you get the abstraction term, before you
        #visit the rest of the children, so the correct term gets associated
        #with the correct input
<<<<<<< HEAD

        #to_substitute = self.visit(ctx.getChild(0))
        parentesis_check = ctx.getChild(0).getText()
        print("Parenthesis check = "+parentesis_check)
        #if I am a parenthesis of myself, just return as I am
        
        print("Child 0 = "+ctx.getChild(0).getText())
        print("Child 1 = "+ctx.getChild(1).getText())
        print("Child 2 = "+ctx.getChild(2).getText())
        
        if parentesis_check == "(":
            #return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()

            return [ctx.getChild(0),self.visit(ctx.getChild(1)),ctx.getChild(2)]
        
        to_substitute = self.visit(ctx.getChild(0))
        incoming = self.incoming_values.pop()
        function = self.visit(ctx.getChild(2))

        print("To subsitute = "+to_substitute)
        print("Function before abstraction = "+str(function))
=======
        to_substitute = self.visit(ctx.getChild(0))
        incoming = self.incoming_values.pop()
        function = self.visit(ctx.getChild(2))
        
        print("Function before abstraction = "+function)
>>>>>>> parent of 14204d1... Making grammar changes so the term directly underneath an application is an abstraction when applicable
        print("Incoming before abstraction = "+str(incoming))

        new_function = function

        #<test>
        print("Function string = "+str(function))
        output_array = []
        for term in function:
            print("Term = "+str(term))
            if isinstance(term,str):
                output_array.append(term)
            else:
                output_array.append(term.getText())

        print("Function now is this:")
        print(str(output_array))
        #</test>

        function_string = ""
        for term in function:
            print("Term output = "+str(term))
            print("Type = "+str(type(term)))

            if isinstance(term,str):
                function_string = function_string + term
            else:
                function_string = function_string + term.getText()
        
        #TO PUT BACK IN - JUST TAKING OUT FOR A TEST
        if incoming != -1:
            #bound_variables_left = re.findall("/(.*?)\]", function)
            bound_variables_left = re.findall("%(.*?)\.",function_string)

            #subst_container_match = re.search("\[(.*?)\]", function)
            subst_container_match = re.search("%(.*?)\.",function_string)
            
            print("Bound variables left = "+str(bound_variables_left))
            print("Subst container match = "+str(subst_container_match))

            if subst_container_match is not None:
                container = subst_container_match.group(0)
                print("Container match = "+container)

                end_value = len(function_string)
                if len(bound_variables_left) > 0:
                    #More than one bound variable -- do something here
                    if to_substitute in bound_variables_left:
                        #Bound variable repeated, need to check for the next instance of it
                        for i,letter in enumerate(function_string):
                            #if letter == '[':
                            if letter == '%':
                                #subst_container_match = re.search("/(.*?)\]", function[i:])
                                subst_container_match = re.search("%(.*?)\.",function_string[i:])
                                bound_value = subst_container_match.group(1)
                                if to_substitute == bound_value:
                                    break
                        end_value = i
                        function = calculate_alpha(to_substitute, function_string, incoming, 0, end_value)
                    else:
                        function = calculate_alpha(to_substitute, function_string, incoming)
                else:
                    function = calculate_alpha(to_substitute, function_string, incoming)

                new_function = function[:end_value].replace(to_substitute,incoming) + function_string[end_value:]
            else:
                new_function = calculate_alpha(to_substitute, function_string, incoming)
                new_function = new_function.replace(to_substitute,incoming)
        else:
            #If there's nothing to substitute, just rewrite the term in form
            #[?/x] and pass back up the tree
            #substitution_form = "[?/"+to_substitute+"]"
            substitution_form = "%"+to_substitute+"."
            new_function = substitution_form + function
        
        print("Function after replacement in abstraction = "+new_function)

        #What do I return here?
        #I think I need to get my interval, change the text of my own tokens, and then return ctx
        #That could work, right?
        #It's going to be a LONG day tomorrow
        #NOTE: this way, I can't guarantee that I am going to contain a lambda variable (I might not any more)
        #But this could actually work!!
        return new_function

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        #print("F: "+ctx.getText())

        parentesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        
        returned = []
        if parentesis_check == "(":
            #return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
            return [ctx.getChild(0).getText(),self.visit(ctx.getChild(1)),ctx.getChild(2).getText()]
        else:
            return [self.visit(ctx.getChild(0)),ctx.getChild(1).getText(),self.visit(ctx.getChild(2))]
            #do I need to return the value of this or the text version (probably the node)
    
        #NOTE: I should be calculating the function here and returning the result
        #return "" + self.visit(ctx.getChild(0)) + ctx.getChild(1).getText() + self.visit(ctx.getChild(2))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        #print("In abstraction term")
        #my_token = ctx
        #self.rewriter.replace(ctx.start,ctx.stop,MyLambdaVisitor(self.tokens).visit(ctx))
        #self.rewriter.replace(ctx,"hello?")
        #programName = ctx.programHeading().getChild(1).getText()
        #print("Program name = "+programName)
        #self.rewriter.replace()
       
        #So this is definitely being called, although I think this is calling visit first which is why it's going into a loop
        #self.rewriter.replace(ctx.start, ctx.stop, self.visit(ctx))
        
        #ctx.start is a token - this is good news? We're getting somewhere
        # self.rewriter.replaceSingleToken(ctx.start,"Hello? Anyone there?")
        # self.rewriter.replaceIndex(0,"DO SOMETHING")
        # [a,b] = ctx.getSourceInterval()
        # print("Interval = "+str(a))
        # print("Interval 2 = "+str(b))

        # #print("Result of rewrite = "+str(self.rewriter.replace(sys.argv[0],a,b,"Hello?")))
        # #self.rewriter.replace(ctx.start,ctx.stop,ctx.getText(),self.visitLambda_variable(ctx))
        # print("Here goes nothing...")
        #         #ok, so I'm getting here, I'm getting the right tokens at least. I'm just not managing to replace anything.
        # token_stream = self.rewriter.getTokenStream()
        # #print("Ctx token = "+ctx.getToken(LambdaCalculusParser.TermContext,1))

        # #ok, this is a way to get the current tokens
        # [start,stop] = ctx.getSourceInterval()
        # self.rewriter.replaceIndex(start,"Hello?")

        # tokens = token_stream.getTokens(start,stop+1)

        # print("Tokens? ")
        # #ok, so this definitely does something
        # ctx.removeLastChild()
        # #child = LambdaCalculusParser.Lambda_variableContext(ctx)
        
        # #ctx.addChild(child)
        

        # for token in tokens:
        #     token.text = "Hello?"
        #     self.rewriter.replaceSingleToken(token,"HELLO")
        #     print(token.text)
        #     print("Type = "+str(token.type))
        #     #self.parser.getVocabulary().getLiteralName(token_num)
        #     print("Type string = "+LambdaCalculusParser.ruleNames[token.type])
        #     #print("Type = "+str(type(token)))
        #     token.type = 10000
        #     print("New type = "+str(token.type))

        # print("End of tokens")

        #self.dump(self.rewriter.replace())

        #print("Stop = "+str(int(ctx.stop)))
        #print("Type of start and stop = "+str(type(ctx.start)))
        
        #print("Abstraction term text = "+ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#lambda_variable.
    def visitLambda_variable(self, ctx:LambdaCalculusParser.Lambda_variableContext):
        #print("Lambda variable = "+ctx.getText())
        return ctx.getText()
    
#NOTE: doing ctx. gives a whole bunch of possible functions
    #well, it used to :(
#NOTE: self is MyVisitor (this seems obvious)
#NOTE: Just always visit children, even if you don't need to, what's the harm?
#NOTE: This could be useful?
    #print("Tree")
    #print(ctx.toStringTree())
    #to print children: ctx.getChildren()
    #to print number of children: ctx.getChildCount()