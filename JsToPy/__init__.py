import builtins

from .console import console
from .require import require

# Patch console
builtins.console = console
# Patch require
builtins.require = require

JsToPy = type('JsToPy', (), {'__getattr__': lambda _, name: getattr(builtins, name)})

__main__ = JsToPy()
