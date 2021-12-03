from hashlib import md5
from random import choice
import cProfile


pr = cProfile.Profile()
pr.enable()

while True:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("00000"):
        print(s, h)
        break

pr.disable()
pr.print_stats(sort=1)