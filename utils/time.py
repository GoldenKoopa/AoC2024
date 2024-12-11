from functools import wraps
from time import time
from colorama import Fore
import sys
def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            string = Fore.CYAN + "Total execution time: " + Fore.RED + f"{end_ if end_ > 0 else 0} ms" + Fore.RESET
            print(string, file=sys.stderr)
    return _time_it