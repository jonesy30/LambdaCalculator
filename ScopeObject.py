from CurrentLetter import CurrentLetter

class ScopeObject(object):

    def __init__(self, current_letter):
        self.bound_values = []
        self.original_letters = []
        self.associated_letters = []
        self.current_letter = current_letter

