from text import TextBlock
from block import Block

class OpenParenthesis(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \left("
        ]
        self.changable = False

class ClosedParenthesis(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \right)"
        ]
        self.changable = False

class OpenSquareBracket(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \left["
        ]
        self.changable = False

class ClosedSquareBracket(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \right]"
        ]
        self.changable = False

class OpenCurlyBracket(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \left\lbrace"
        ]
        self.changable = False

class ClosedCurlyBracket(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \right\rbrace"
        ]
        self.changable = False

class Percent(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \%",
            r" \textperthousand",
            r" \textpertenthousand"
        ]
        self.changable = True

class Infinit(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"\infty"
        ]
        self.changable = False

class Sine(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \sin \left( ",
                r" \right) "
            ],
            [
                r" \arcsin \left( ",
                r" \right) "
            ]
        ]
        self.changable = True
        self.setup(len(self.tex_strings[self.state]))

class Cosine(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \cos \left( ",
                r" \right) "
            ],
            [
                r" \arccos \left( ",
                r" \right) "
            ]
        ]
        self.changable = True
        self.setup(len(self.tex_strings[self.state]))

class Tangent(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \tan \left( ",
                r" \right) "
            ],
            [
                r" \arctan \left( ",
                r" \right) "
            ],
            [
                r" \cot \left( ",
                r" \right) "
            ]
        ]
        self.changable = True
        self.setup(len(self.tex_strings[self.state]))

class Compare(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" <",
            r" >",
            r" \leq",
            r" \geq"
        ]
        self.changable = True

class Style(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \textbf{",
                r"}"
            ],
            [
                r" \mathrm{",
                r"}"
            ]
        ]
        self.changable = True
        self.setup(len(self.tex_strings[self.state]))

class Space(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \;"
        ]
        self.changable = False

class LineBreak(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \\ "
        ]
        self.changable = False

class Align(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \begin{align}",
                r" \end{align}"
            ],
            [
                r" \begin{alignat}[20]",
                r" \end{alignat}"
            ]
        ]
        self.changable = True
        self.setup(len(self.tex_strings[self.state]))

class AlignPoint(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r"&",
            r"&&"
        ]
        self.changable = True

class KeyboardText(TextBlock):
    def __init__(self, key):
        super().__init__()
        self.tex_strings = [
            key
        ]
        self.changable = False

class MathBB(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \mathbb{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class Arrows(TextBlock):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            r" \rightarrow",
            r" \leftarrow",
            r" \uparrow",
            r" \downarrow",
            r" \Rightarrow",
            r" \Leftarrow",
            r" \Uparrow",
            r" \Downarrow",
            r" \longrightarrow",
            r" \longleftarrow",
            r" \longuparrow",
            r" \longdownarrow",
            r" \Longrightarrow",
            r" \Longleftarrow",
            r" \Longuparrow",
            r" \Longdownarrow",
            r" \leftrightarrow",
            r" \Leftrightarrow",
            r" \longleftrightarrow",
            r" \Longleftrightarrow"
        ]
        self.changable = True