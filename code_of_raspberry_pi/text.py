# elements that contain only a tex-string
class TextBlock:
    # sets up some variables
    def __init__(self):
        self.state = 0
        self.is_block = False

    # tells the parent element to add the new element at this position
    def add_element(self, element):
        return True
    
    # tells the parent element to delete the element at this position
    def delete(self):
        return True

    # changes the state of this element
    def change_element(self):
        self.state = (self.state + 1) % len(self.tex_strings)

    # tells the parent element to move left
    def left(self):
        return True

    # tells the parent element to move right
    def right(self):
        return True

    # returns the tex-string of this element
    def get_tex_string(self, cursor):
        return self.tex_strings[self.state], False

    # returns itself as the active element
    def get_active_element(self):
        return self