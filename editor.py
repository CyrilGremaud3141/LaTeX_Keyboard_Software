from empty import EmptyBlock
from copy import deepcopy
import matrix
class TexEditor:
    def __init__(self):
        self.tex_string = ""
        self.content = EmptyBlock()
        self.last_content = deepcopy(self.content)
        self.last_element = None
    
    def add_element(self, element):
        if type(element) == type(self.last_element) and len(element.tex_strings) > 1 and element.changable:
            self.last_element.change_element()
            self.content = deepcopy(self.last_content)
            self.content.add_element(self.last_element)
        else:
            self.last_content = deepcopy(self.content)
            self.content.add_element(element)
            self.last_element = element
        
        if not element.is_block:
            self.content.right()
    
    def delete(self):
        self.content.delete()

    def get_tex_string(self, cursor):
        content, _ = self.content.get_tex_string(cursor)
        return content
    
    def get_active_element(self):
        return self.content.get_active_element()

    def matrixAddColumn(self):
        element = self.get_active_element()
        if type(element) == matrix.Matrix or type(element) == matrix.Pmatrix:
            element.add_column()

    def matrixDelColumn(self):
        element = self.get_active_element()
        if type(element) == matrix.Matrix or type(element) == matrix.Pmatrix:
            element.remove_column()
    
    def matrixAddRow(self):
        element = self.get_active_element()
        if type(element) == matrix.Matrix or type(element) == matrix.Pmatrix:
            element.add_row()

    def matrixDelRow(self):
        element = self.get_active_element()
        if type(element) == matrix.Matrix or type(element) == matrix.Pmatrix:
            element.remove_row()
    
    def clear(self):
        self.content = EmptyBlock()
        self.last_content = deepcopy(self.content)
        self.last_element = None



