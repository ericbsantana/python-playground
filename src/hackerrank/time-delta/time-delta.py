from datetime import datetime
from time import time


def time_delta(t1, t2):
    formatted_t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    formatted_t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    delta = formatted_t2 - formatted_t1
    return abs(int(delta.total_seconds()))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)

        print(delta)
