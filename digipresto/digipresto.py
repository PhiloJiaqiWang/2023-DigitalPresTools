from back import Backend
from front import Frontend
import datetime


class DigiPresTo:
    """DigiPresTo app.

    Implemented as a singleton.
    """
    _instance = None
    now = datetime.datetime.now()
    select_lis = []
    lis_before = []
    lis_after = []

    def __init__(self) -> None:
        DigiPresTo._instance = self
