import logging
import sys

root = logging.getLogger()
root.setLevel("DEBUG")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(asctime)s] %(name)s|%(levelname)s|%(funcName)s:%(lineno)d| %(message)s")
handler.setFormatter(formatter)
root.addHandler(handler)
