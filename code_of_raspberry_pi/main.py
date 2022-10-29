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


# setup of the input{columns} and output{rows} pins 
gpio.setmode(gpio.BOARD)
input_pins = [13, 15, 16, 18, 19, 21, 22 ,23, 24, 26, 29, 31, 32, 33, 35, 36]
input_pins.reverse()
output_pins = [3, 5, 7, 10, 11, 12]
for pin in input_pins:
    gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

for pin in output_pins:
    gpio.setup(pin, gpio.OUT)


# sets the layout for the editor
layout = [ 
    [greek.Alpha,   greek.Beta,  greek.Gamma,   greek.Delta,   others.OpenParenthesis,   others.ClosedParenthesis,   matrix.Pmatrix,    matrix.Matrix,          others.Percent,           others.Infinit,           others.MathBB,            others.Sine,            others.Cosine,   others.Tangent,     others.Style, "tex"],
    [greek.Epsilon, greek.Zeta,  greek.Eta,     greek.Theta,   others.OpenSquareBracket, others.ClosedSquareBracket, "matrixDelColumn", "matrixAddColumn",      mathBlocks.LogBlock,      mathBlocks.SqrtBlock,     mathBlocks.FractionBlock, mathBlocks.EEBlock,     others.Compare,  numberPad.Divide,   "clear",      "sto1"],
    [greek.Iota,    greek.Kappa, greek.Lambda,  greek.Mu,      others.OpenCurlyBracket,  others.ClosedSquareBracket, "matrixDelRow",    "matrixAddRow",         mathBlocks.LimitBlock,    mathBlocks.NsqrtBlock,    numberPad.Seven,          numberPad.Eight,        numberPad.Nine,  numberPad.Multiply, "delete",     "sto2"],
    [greek.Nu,      greek.Xi,    greek.Omikron, greek.Pi,      others.Align,             mathBlocks.BraceBlock,      "up",              mathBlocks.Superscript, mathBlocks.SumBlock,      mathBlocks.VectorBlock,   numberPad.Four,           numberPad.Five,         numberPad.Six,   numberPad.Subtract, others.Space, "sto3"],
    [greek.Rho,     greek.Sigma, greek.Tau,     greek.Upsilon, others.AlignPoint,        "left",                     others.Arrows,     "right",                mathBlocks.IntegralBlock, mathBlocks.AbsoluteBlock, numberPad.One,            numberPad.Two,          numberPad.Three, numberPad.Add,      "toggle",     "sto4"],
    [greek.Phi,     greek.Chi,   greek.Psi,     greek.Omega,   others.LineBreak,         mathBlocks.LineBlock,       "down",            mathBlocks.Subscript,   mathBlocks.BoxedBlock,    mathBlocks.RoundBlock,    numberPad.Zero,           numberPad.DecimalPoint, "calculate",     numberPad.Equals,   "insert",     "sto5"]
]

# sets the layout for directly writing to the computer
macro = [
    [r"\alpha",   r"\beta",  r"\gamma",  r"\delta",   r"(", r")", r"", r"", r"", r"", r"",  r"",  r"",  r"",      r"", r""],
    [r"\epsilon", r"\zeta",  r"\eta",    r"\theta",   r"[", r"]", r"", r"", r"", r"", r"",  r"",  r"",  r"\div",  r"", r""],
    [r"\iota",    r"\kappa", r"\lambda", r"\mu",      r"{", r"}", r"", r"", r"", r"", r"7", r"8", r"9", r"\cdot", r"", r""],
    [r"\nu",      r"\xi",    r"o",       r"\pi",      r"",  r"",  r"", r"", r"", r"", r"4", r"5", r"6", r"-",     r"", r""],
    [r"\rho",     r"\sigma", r"\tau",    r"\upsilon", r"",  r"",  r"", r"", r"", r"", r"1", r"2", r"3", r"+",     r"", r""],
    [r"\phi",     r"\chi",   r"\psi",    r"\omega",   r"",  r"",  r"", r"", r"", r"", r"0", r".", r"",  r"=",     r"", r""]
]

# defines a list to reset the stored button states
empty_keys = [
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
]

# defines a list to store the button states
pressed_keys = deepcopy(empty_keys)

# defines a list to store the newly pressed buttons since the last update
new_keys = deepcopy(empty_keys)

# defines the editor and the graphical user interface
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
                                    
# runns the main loop of the program
try:
    while True:
        # gives power to the rows (one after another)
        for row, o_pin in enumerate(output_pins):
            # fives power to row
            gpio.output(o_pin, 1)
            # checks the columns if the circuit closed {closed circuit between a row and a column means that the key is pressed}
            for column, i_pin in enumerate(input_pins):
                # if the key is pressed
                if gpio.input(i_pin) == 1:
                    # if the key wasn't pressed before, it gets stored as a new key
                    if not pressed_keys[row][column]:
                        new_keys[row][column] = True
                    # key gets addet to the pressed keys
                    pressed_keys[row][column] = True
                # if the key isn't pressed, it gets removed from the pressed keys
                else:
                    pressed_keys[row][column] = False
            # removes power from row
            gpio.output(o_pin, 0)
        
        # executes commands for the newly pressed keys
        for row in range(len(new_keys)):
            for column, value in enumerate(new_keys[row]):
                # if key was pressed
                if value:
                    # if tho element in the layout belonging to the key is a string, it is a special function and gets executed
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
                    # otherwise it is a element for the editor
                    else:
                        # if the editor is active, it gets added to the editor
                        if app.active_editor:
                            edit.add_element(layout[row][column]())
                        # otherwise it sends the macro string to the seeed xiao
                        else:
                            write(macro[row][column])
        
        # the list of the new keys gets reset
        new_keys = deepcopy(empty_keys)

        # the gui is updated with the new tex string
        tex_string = edit.get_tex_string(cursor=True)
        app.latex_render(tex_string)
        app.window.update()

# resets the used pins when the program is quit
finally:
    gpio.cleanup()


