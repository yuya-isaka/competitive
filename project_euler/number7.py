import numpy as np  

def is_prime(target, arr):
    for num in arr:
        if target % num == 0:
            return False
    return True

if __name__ == "__main__":
    arr = [2]
    src = 3
    while True:
        if is_prime(src, arr) is True:
            if len(arr) == 10000:
                print('10001th prime number is %d' % src)
                break
            arr.append(src)
            print('%d is prime number' % src)
        
        src += 2
    