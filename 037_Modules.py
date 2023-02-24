# module = a file containing containing python code . May contain functions, classes, etc.
# used with modular programming, which is separate a program into parts.

import module as mod

mod.hello()
mod.bye()

import module
module.hello()
module.bye()

from module import hello,bye
hello()
bye()

from module import *
hello()
bye()

help("modules")
