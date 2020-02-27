import numpy as np 

if __name__ == "__main__":
    src = np.arange(1, 101)
    sum_of_square = np.sum(src ** 2)
    square_of_sum = np.sum(src) ** 2

    diff = np.abs(sum_of_square - square_of_sum)

    print('sum_of_square is %d' % sum_of_square)
    print('square_of_sum is  %d' % square_of_sum)
    print('diff is %d' % diff)

    