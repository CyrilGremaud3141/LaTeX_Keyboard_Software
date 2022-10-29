from text import TextBlock

# sets up the Elements with the corresponding tex-strings

class One(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"1"
        ]
        self.changable = False

class Two(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"2"
        ]
        self.changable = False

class Three(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"3"
        ]
        self.changable = False

class Four(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"4"
        ]
        self.changable = False

class Five(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"5"
        ]
        self.changable = False

class Six(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"6"
        ]
        self.changable = False

class Seven(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"7"
        ]
        self.changable = False

class Eight(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"8"
        ]
        self.changable = False

class Nine(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"9"
        ]
        self.changable = False

class Zero(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"0"
        ]
        self.changable = False

class Divide(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"\div"
        ]
        self.changable = False

class Multiply(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"\cdot "
        ]
        self.changable = False

class Subtract(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"-"
        ]
        self.changable = False

class Add(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"+"
        ]
        self.changable = False

class Equals(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"=",
            r"\approx",
            r"\neq"
        ]
        self.changable = True

class DecimalPoint(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"."
        ]
        self.changable = False

