#Class which is used to store information being passed between webpages - stores input lambda ter, typing context and beta steps
class LambdaSessionInformationObject():
    
    #Initialise values when the object is created
    def __init__(self):
        self.input_term = ""
        self.typing_context = "no context for this term"
        self.beta_steps = ""

    #Set the input term
    def set_input_term(self, input_term):
        self.input_term = input_term
    
    #Set the final typing context when the evaluator is finished evaluating
    def set_typing_context(self, typing_context):
        if typing_context != "":
            self.typing_context = typing_context
    
    #Throughout the evaluation process, the code repeatedly adds beta steps giving a description of what's going on
    #Add the beta step to the existing string along with a HTML break-line character
    def add_beta_step(self, beta_step):
        #Remove any types from the beta-step and replace % with lambda terms for readability
        beta_step = self.process_term(beta_step)
        self.beta_steps = self.beta_steps + beta_step + "<br>"

    #Return the input string (the incoming lambda term)
    def get_input_term(self):
        return self.input_term
    
    #Return the typing context for the evaluation
    def get_typing_context(self):
        return self.typing_context
    
    #Get the beta steps for the evaluation
    def get_beta_steps(self):
        return self.beta_steps

    #Method which removes types from a string and converts % to a lamdba symbol
    #Used to make beta steps more readable by the user, since the inner code uses % as a lambda symbol
    def process_term(self,output):
        bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

        output = str(output)
        for string in bad_strings:
            output = output.replace(string,"")

        output_list = list(output)
        for i,character in enumerate(output_list):
            if character == '%':
                output_list[i] = 'λ'
        
        output_processed = "".join(output_list)
        
        return output_processed
