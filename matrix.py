from empty import EmptyBlock
class Matrix:
    def __init__(self):
        self.cursor = 0
        self.is_cursor = True
        self.is_block = True
        self.size_x = 1
        self.size_y = 1
        self.content = [EmptyBlock()]
        self.matrix_string = r"matrix"

    def add_element(self, element):
        if self.cursor == len(self.content):
            self.content.append(element)
        else:
            if self.content[self.cursor].add_element(element):
                self.content[self.cursor] = element
    
    def delete(self):
        if self.is_cursor:
            return True
        else:
            self.content[self.cursor].delete()
    
    def add_row(self):
        self.size_y += 1
        for i in range(self.size_x):
            self.content.append(EmptyBlock())

    def remove_row(self):
        if self.size_y > 1:
            self.size_y -= 1
            for i in range(self.size_x):
                self.content.pop()

    def add_column(self):
        new_content = []
        for i in range(len(self.content)):
            new_content.append(self.content[i])
            if i % self.size_x == 0:
                new_content.append(EmptyBlock())
        self.content = new_content
        self.size_x += 1

    def remove_column(self):
        if self.size_x > 1:
            new_content = []
            for i in range(len(self.content)):
                if (i + 1) % self.size_x != 0:
                    new_content.append(self.content[i])
            self.content = new_content
            self.size_x -= 1

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

    def up(self):
        pass

    def down(self):
        pass

    def get_tex_string(self, cursor):
        tex_string = r"\begin{" + self.matrix_string + r"}"
        cursor_used = False
        for i in range(len(self.content)):

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

            if (i + 1) % self.size_x == 0:
                tex_string += r" \\ "
            else:
                tex_string += r" & "


        tex_string += r"\end{" + self.matrix_string + r"}"

        return tex_string, cursor_used
    
    def get_active_element(self):
        if self.is_cursor:
            return self
        else:
            return self.content[self.cursor].get_active_element()

class Pmatrix(Matrix):
    def __init__(self):
        super().__init__()
        self.matrix_string = r"pmatrix"