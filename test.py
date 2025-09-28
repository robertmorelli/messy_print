from fastprint import print_num
from random import randrange
from sys import set_int_max_str_digits
from time import time



def main():
    set_int_max_str_digits(10**9)

    info = "\n\n"


    example = int(''.join(str(randrange(0,10)) for _ in range(3*10**6)))

    start = time()
    print(example)
    elapsed = time() - start
    info += ((f"{elapsed:.3f} python builtin")) + "\n"

    start = time()
    print_num(example)
    elapsed = time() - start
    info += ((f"{elapsed:.3f} approx")) + "\n"


    print(info)




if __name__ == "__main__":
    main()
    
