from empty import EmptyBlock
from copy import deepcopy
import matrix

class TexEditor:
    # sets up the stored Formula
    def __init__(self):
        self.tex_string = ""
        self.content = EmptyBlock()
        self.last_content = deepcopy(self.content)
        self.last_element = None
    
    # adds an element or changes it if it is pressedt twice in a row
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
    
    # deletes an Element
    def delete(self):
        self.content.delete()

    # gets the whole Texs-string
    def get_tex_string(self, cursor):
        content, _ = self.content.get_tex_string(cursor)
        return content
    
    # gets the active element
    def get_active_element(self):
        return self.content.get_active_element()

    # if the active Element is a matrix, add column to matrix
    def matrixAddColumn(self):
        element = self.get_active_element()
        if type(element) == matrix.Matrix or type(element) == matrix.Pmatrix:
            element.add_column()

    # if the active Element is a matrix, delete column of matrix
    def matrixDelColumn(self):
        element = self.get_active_element()
        if type(element) == matrix.Matrix or type(element) == matrix.Pmatrix:
            element.remove_column()
    
    # if the active Element is a matrix, add row to matrix
    def matrixAddRow(self):
        element = self.get_active_element()
        if type(element) == matrix.Matrix or type(element) == matrix.Pmatrix:
            element.add_row()

    # if the active Element is a matrix, delete row of matrix
    def matrixDelRow(self):
        element = self.get_active_element()
        if type(element) == matrix.Matrix or type(element) == matrix.Pmatrix:
            element.remove_row()
    
    # resets the Editor for a new formula
    def clear(self):
        self.content = EmptyBlock()
        self.last_content = deepcopy(self.content)
        self.last_element = None



