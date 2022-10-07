from block import Block

class BraceBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \underbrace_{",
                r"}"
            ],
            [
                r" \overbrace^{",
                r"}"
            ]
        ]
        self.changable = True
        self.setup(len(self.tex_strings[self.state]))

class LineBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \underline_{",
                r"}"
            ],
            [
                r" \overline^{",
                r"}"
            ]
        ]
        self.changable = True
        self.setup(len(self.tex_strings[self.state]))

class Superscript(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r"^{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class Subscript(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r"_{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class LogBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \log_{",
                r"} \left(",
                r" \right)"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class LimitBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \lim_{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class SumBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \sum_{",
                r"}^{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class IntegralBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \int_{",
                r"}^{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))


class BoxedBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \boxed{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class SqrtBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \sqrt{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class NsqrtBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \sqrt[",
                r"]{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class VectorBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \vec{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class AbsoluteBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \left\vert",
                r" \right\vert"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class RoundBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \left\lfloor ",
                r" \right\rfloor "
            ],
            [
                r" \left\lceil ",
                r" \right\rceil "
            ]
        ]
        self.changable = True
        self.setup(len(self.tex_strings[self.state]))

class FractionBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \frac{",
                r"}{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))

class EEBlock(Block):
    def __init__(self):
        super().__init__()
        self.tex_strings = [
            [
                r" \cdot 10^{",
                r"}"
            ]
        ]
        self.changable = False
        self.setup(len(self.tex_strings[self.state]))