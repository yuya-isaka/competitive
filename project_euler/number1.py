import numpy as np 

if __name__ == "__main__":
    src = np.arange(1, 1000)
    dest = src[ (src % 3 == 0) | (src % 5 == 0) ]
    sum_num = np.sum(dest)

    print('sum is %d' % sum_num)