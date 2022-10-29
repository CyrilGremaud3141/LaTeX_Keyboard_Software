from empty import EmptyBlock



# Block Elements are Elements with a Tex-Code, which contains the Tex-Code of Subelements
class Block:
    # sets some general variables up
    def __init__(self):
        self.state = 0
        self.is_cursor = False
        self.is_block = True

    # sets some block specific variables up (is also called after changed state)
    def setup(self, num_subelements):
        self.cursor = 0
        self.content = []
        for i in range(num_subelements - 1):
            self.content.append(EmptyBlock())

    # adds an element at the position of the cursor.
    def add_element(self, element):
        if self.is_cursor:
            return True
        if self.content[self.cursor].add_element(element):
            self.content[self.cursor] = element
    
    # deletes an element at the position of the cursor
    def delete(self):
        if self.is_cursor:
            return True
        else:
            self.content[self.cursor].delete()

    # changes the state of the element at the cursor position
    def change_element(self):
        self.state = (self.state + 1) % len(self.tex_strings)
        self.setup(len(self.tex_strings[self.state]))

    # moves the cursor to the left; sets yourself the cursor if you try to move out of the block
    def left(self):
        if self.content[self.cursor].left():
            if self.cursor > 0:
                self.cursor -= 1
            else:
                if self.is_cursor:
                    return True
                else:
                    self.is_cursor = True
                    return False
        return False

    # moves the cursor to the right
    def right(self):
        if self.is_cursor:
            self.is_cursor = False
        else:
            if self.content[self.cursor].right():
                if self.cursor < len(self.content) - 1:
                    self.cursor += 1
                else:
                    return True
            return False

    # returns the Tex-string of all subelements and itself. Adds a cursor to the string if this class  is the cursor
    def get_tex_string(self, cursor):
        tex_string = r""
        cursor_used = False
        for i in range(len(self.content)):
            tex_string += self.tex_strings[self.state][i]

            if i == self.cursor and not self.is_cursor:
                substring, c = self.content[i].get_tex_string(cursor)
                if c:
                    cursor_used = True

                if not cursor_used and cursor:
                    substring = r"┃" + substring + r"┃"
                    cursor_used = True
            else:
                substring, _ = self.content[i].get_tex_string(False)
 
            tex_string += substring


        tex_string += self.tex_strings[self.state][-1]

        return tex_string, cursor_used

    # returns the element at the cursor position
    def get_active_element(self):
        if self.is_cursor:
            return self
        else:
            return self.content[self.cursor].get_active_element()