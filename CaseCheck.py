class CaseCheck:
    def check_case(self,expression):

        all_lowercase = True

        expression_list = list(expression)
        for i,letter in enumerate(expression_list):
            if letter.isalpha() and letter.isupper():
                all_lowercase = False
                return all_lowercase
        
        return all_lowercase