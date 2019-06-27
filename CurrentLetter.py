#taken from https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
class CurrentLetter(object):
    __instance = None
    lowercase_letter = None
    uppercase_letter = None

    @staticmethod
    def getLowerCase():
        if CurrentLetter.__instance == None:
            CurrentLetter()
        CurrentLetter.__instance.lowercase_letter =  CurrentLetter.__instance.lowercase_letter + 1
        if CurrentLetter.__instance.lowercase_letter > 122:
            CurrentLetter.__instance.lowercase_letter = 97
        return chr(CurrentLetter.__instance.lowercase_letter)
    
    @staticmethod
    def getUpperCase():
        if CurrentLetter.__instance == None:
            CurrentLetter()
        CurrentLetter.__instance.uppercase_letter =  CurrentLetter.__instance.uppercase_letter + 1
        if CurrentLetter.__instance.uppercase_letter > 90:
            CurrentLetter.__instance.uppercase_letter = 65
        return chr(CurrentLetter.__instance.uppercase_letter)

    def __init__(self):
        if CurrentLetter.__instance != None:
            raise Exception("Cannot create multiple instances of this class")
        else:
            CurrentLetter.__instance = self
            CurrentLetter.__instance.lowercase_letter = 96
            CurrentLetter.__instance.uppercase_letter = 64
