import sys

class BetaReductionFileWriter():
    def __init__(self):
        file = open("app/static/beta_reduction.txt","w+")
        file.write("Beta Reduction Steps\n\r")
    
        self.file = file
    
    def write_to_file(self, string):
        string = self.remove_types(string)

        file_string = string + "\n\r"
        self.file.write(file_string)
        
    def close_file(self):
        self.file.close()

    def remove_types(self,output):
        bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

        output = str(output)
        for string in bad_strings:
            output = output.replace(string,"")
        
        return output
