import easygui
import io
from contextlib import redirect_stderr

from settings import language

def enterBox(msg, title, default=""):
    # Suppress cursor movement error message
    with redirect_stderr(io.StringIO()):
        return easygui.enterbox(msg, title, default=default)

def ynBox(msg, title):
    return easygui.ynbox(msg, title, choices=[language.YES, language.NO], default_choice=None)