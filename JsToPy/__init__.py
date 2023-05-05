import builtins

from . import *

# Patch console
builtins.console = console
# Patch require
builtins.require = require
