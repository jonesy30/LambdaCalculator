class LambdaSessionInformationObject():
    def __init__(self):
        self.input_term = ""
        self.typing_context = ""
        self.beta_steps = ""

    def set_input_term(self, input_term):
        self.input_term = input_term
    
    def set_typing_context(self, typing_context):
        self.typing_context = typing_context
    
    def add_beta_step(self, beta_step):
        beta_step = self.process_term(beta_step)
        self.beta_steps = self.beta_steps + beta_step + "<br>"

    def get_input_term(self):
        return self.input_term
    
    def get_typing_context(self):
        return self.typing_context
    
    def get_beta_steps(self):
        return self.beta_steps

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
