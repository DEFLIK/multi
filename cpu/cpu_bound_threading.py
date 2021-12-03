import concurrent.futures
from hashlib import md5
from random import choice
import cProfile

pr = cProfile.Profile()
pr.enable()


def calculate():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            pr.disable()
            pr.print_stats(sort=1)
            break


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for i in range(10):
            executor.submit(calculate)


if __name__ == '__main__':
    main()

