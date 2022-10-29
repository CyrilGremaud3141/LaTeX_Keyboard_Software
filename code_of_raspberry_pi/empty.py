# combines the Tex-strings of the subelements
class EmptyBlock:
    # sets up some variables
    def __init__(self):
        self.cursor = 0
        self.content = []
        self.is_block = True

    # adds an element at the position of the cursor
    def add_element(self, element):
        if self.cursor == len(self.content):
            self.content.append(element)
        else:
            if self.content[self.cursor].add_element(element):
                self.content[self.cursor] = element

    # deletes the element at the position of the cursor
    def delete(self):
        if len(self.content) > 0:
            if self.cursor == len(self.content):
                self.content.pop()
                self.cursor -= 1
            else:
                if self.content[self.cursor].delete():
                    self.content.pop(self.cursor)

    # moves left in the editor
    def left(self):
        # if this block has no subelements, move in parent object
        if len(self.content) == 0:
            return True
        # if is at the end of the block (position to add element), you can move to the left but you cant call functions of the object, because it doesn't exist
        if self.cursor == len(self.content):
            self.cursor -= 1
        else:
            if self.content[self.cursor].left():
                if self.cursor > 0:
                    self.cursor -= 1
                else:
                    return True
        return False

    # moves right in the editor
    def right(self):
        if self.cursor < len(self.content):
            if self.content[self.cursor].right():
                self.cursor += 1
        else:
            return True
        return False

    # returnes the combined Tex-strings of all the subelements
    def get_tex_string(self, cursor):
        tex_string = r""
        cursor_used = False
        for i, element in enumerate(self.content):
            if i == self.cursor:
                substring, c = self.content[i].get_tex_string(cursor)
                if c:
                    cursor_used = True

                if not cursor_used and cursor:
                    substring = r"┃" + substring + r"┃"
                    cursor_used = True
            else:
                substring, _ = self.content[i].get_tex_string(False)

            tex_string += substring

        if self.cursor == len(self.content) and len(self.content) != 0 and not cursor_used and cursor:
            tex_string += r"┃┃"
            cursor_used = True

        return tex_string, cursor_used
    
    # returns the active element
    def get_active_element(self):
        if self.cursor == len(self.content):
            return None
        else:
            return self.content[self.cursor].get_active_element()