# pyneeds/__init__.py

# 1. Your original core library utilities
from .utils import *

# 2. Expose the external libraries safely
try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
except ImportError:
    pass

try:
    from art import text2art, art
except ImportError:
    pass

try:
    from playsound3 import playsound
except ImportError:
    pass

try:
    from pydantic import BaseModel, Field
except ImportError:
    pass

try:
    import textual
    from textual.app import App
except ImportError:
    pass

# 3. Expose Ursina components directly for rapid 3D game building
try:
    import ursina
    from ursina import Ursina, Entity, color, camera, Vec3, Text
except ImportError:
    pass
