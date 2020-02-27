import numpy as np

def is_palindrome(num):
    num = str(num)
    l = len(num)
    for i in range(l//2):
        if num[i] is not num[-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    src = np.arange(100, 1000)
    src = np.dot(src[:, np.newaxis], src[np.newaxis, :])
    src = src.flatten()
    src = np.sort(src)[::-1]

    for num in src:
        if is_palindrome(num) is True:
            print('%s is palindromic number' % num)
            break