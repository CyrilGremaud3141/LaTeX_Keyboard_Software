import time
import os
import sys
from copy import deepcopy
import pickle

import greek
import mathBlocks
import numberPad
import matrix
import others

import editor
import gui

from serial_interface import write_to_computer as write
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
input_pins = [13, 15, 16, 18, 19, 21, 22 ,23, 24, 26, 29, 31, 32, 33, 35, 36]
input_pins.reverse()
output_pins = [3, 5, 7, 10, 11, 12]
for pin in input_pins:
    gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

for pin in output_pins:
    gpio.setup(pin, gpio.OUT)


layout = [ 
    [greek.Alpha,   greek.Beta,  greek.Gamma,   greek.Delta,   others.OpenParenthesis,   others.ClosedParenthesis,   matrix.Pmatrix,    matrix.Matrix,          others.Percent,           others.Infinit,           others.MathBB,            others.Sine,            others.Cosine,   others.Tangent,     others.Style, "tex"],
    [greek.Epsilon, greek.Zeta,  greek.Eta,     greek.Theta,   others.OpenSquareBracket, others.ClosedSquareBracket, "matrixDelColumn", "matrixAddColumn",      mathBlocks.LogBlock,      mathBlocks.SqrtBlock,     mathBlocks.FractionBlock, mathBlocks.EEBlock,     others.Compare,  numberPad.Divide,   "clear",      "sto1"],
    [greek.Iota,    greek.Kappa, greek.Lambda,  greek.Mu,      others.OpenCurlyBracket,  others.ClosedSquareBracket, "matrixDelRow",    "matrixAddRow",         mathBlocks.LimitBlock,    mathBlocks.NsqrtBlock,    numberPad.Seven,          numberPad.Eight,        numberPad.Nine,  numberPad.Multiply, "delete",     "sto2"],
    [greek.Nu,      greek.Xi,    greek.Omikron, greek.Pi,      others.Align,             mathBlocks.BraceBlock,      "up",              mathBlocks.Superscript, mathBlocks.SumBlock,      mathBlocks.VectorBlock,   numberPad.Four,           numberPad.Five,         numberPad.Six,   numberPad.Subtract, others.Space, "sto3"],
    [greek.Rho,     greek.Sigma, greek.Tau,     greek.Upsilon, others.AlignPoint,        "left",                     others.Arrows,     "right",                mathBlocks.IntegralBlock, mathBlocks.AbsoluteBlock, numberPad.One,            numberPad.Two,          numberPad.Three, numberPad.Add,      "toggle",     "sto4"],
    [greek.Phi,     greek.Chi,   greek.Psi,     greek.Omega,   others.LineBreak,         mathBlocks.LineBlock,       "down",            mathBlocks.Subscript,   mathBlocks.BoxedBlock,    mathBlocks.RoundBlock,    numberPad.Zero,           numberPad.DecimalPoint, "calculate",     numberPad.Equals,   "insert",     "sto5"]
]

macro = [
    [r"\alpha",   r"\beta",  r"\gamma",  r"\delta",   r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r""],
    [r"\epsilon", r"\zeta",  r"\eta",    r"\theta",   r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r""],
    [r"\iota",    r"\kappa", r"\lambda", r"\mu",      r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r""],
    [r"\nu",      r"\xi",    r"o",       r"\pi",      r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r""],
    [r"\rho",     r"\sigma", r"\tau",    r"\upsilon", r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r""],
    [r"\phi",     r"\chi",   r"\psi",    r"\omega",   r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r"", r""]
]

empty_keys = [
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
]

pressed_keys = deepcopy(empty_keys)
new_keys = deepcopy(empty_keys)

edit = editor.TexEditor()
app = gui.Window(edit)


def storage(filename):
    if app.set_storage:
        with open(os.path.join(sys.path[0], filename), "wb") as sto:
            print(edit.content)
            pickle.dump(edit.content, sto)
    else:
        with open(os.path.join(sys.path[0], filename), "rb") as sto:
            edit.add_element(pickle.load(sto))
            edit.last_element = None
                                    

try:
    while True:
        for row, o_pin in enumerate(output_pins):
            gpio.output(o_pin, 1)
            for column, i_pin in enumerate(input_pins):
                if gpio.input(i_pin) == 1:
                    if not pressed_keys[row][column]:
                        new_keys[row][column] = True
                    pressed_keys[row][column] = True
                else:
                    pressed_keys[row][column] = False
            gpio.output(o_pin, 0)
        for row in range(len(new_keys)):
            for column, value in enumerate(new_keys[row]):
                if value:
                    if type(layout[row][column]) == str:
                        command = layout[row][column]
                        if command == "left":
                            edit.content.left()
                            edit.last_element = None
                        elif command == "right":
                            edit.content.right()
                            edit.last_element = None
                        elif command == "up":
                            exit()
                        elif command == "down":
                            pass
                        elif command == "matrixAddColumn":
                            edit.matrixAddColumn()
                        elif command == "matrixDelColumn":
                            edit.matrixDelColumn()
                        elif command == "matrixAddRow":
                            edit.matrixAddRow()
                        elif command == "matrixDelRow":
                            edit.matrixDelRow()
                        elif command == "insert":
                            write(edit.get_tex_string(False))
                        elif command == "clear":
                            edit.clear()
                        elif command == "delete":
                            edit.delete()
                        elif command == "toggle":
                            app.toggle_editor()
                        elif command == "sto1":
                            storage("sto1.obj")
                        elif command == "sto2":
                            storage("sto2.obj")
                        elif command == "sto3":
                            storage("sto3.obj")
                        elif command == "sto4":
                            storage("sto4.obj")
                        elif command == "sto5":
                            storage("sto5.obj")
                    else:
                        if app.active_editor:
                            edit.add_element(layout[row][column]())
                        else:
                            write(macro[row][column])
        new_keys = deepcopy(empty_keys)
        tex_string = edit.get_tex_string(True)
        app.latex_render(tex_string)
        app.window.update()
finally:
    gpio.cleanup()


