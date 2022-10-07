class TextBlock:
    def __init__(self):
        self.state = 0
        self.is_block = False

    def add_element(self, element):
        return True
    
    def delete(self):
        return True

    def change_element(self):
        self.state = (self.state + 1) % len(self.tex_strings)

    def left(self):
        return True

    def right(self):
        return True

    def get_tex_string(self, cursor):
        return self.tex_strings[self.state], False

    def get_active_element(self):
            return self