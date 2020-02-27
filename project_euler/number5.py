import numpy as np 

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)


if __name__ == "__main__":
    src = np.arange(2, 21)
    common_multiple = 1

    for num in src:
        new_common_multiple = lcm(common_multiple, num)
        print('lcm of %d and %d is %d' % (common_multiple, num, new_common_multiple))

        common_multiple = new_common_multiple
    
    print('answer is %d' % common_multiple)


