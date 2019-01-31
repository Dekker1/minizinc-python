from typing import Optional, Callable

from .driver import find_driver, Driver
from .instance import Instance
from .solver import Solver

Instance = Instance
Solver = Solver
load_solver: Callable[[str], Solver] = None

#: Default MiniZinc driver used by the python package
default_driver: Optional[Driver] = None
find_driver(set_default=True)
if default_driver is None:
    import warnings
    warnings.warn("MiniZinc was not found on the system: no default driver could be initialised", RuntimeWarning)

__all__ = ['default_driver', 'load_solver', 'find_driver', 'Driver', 'Instance', 'Solver']