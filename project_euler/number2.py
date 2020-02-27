import numpy as np 

def fibonacci(arr, max_num):
    x = arr[-2]
    y = arr[-1]

    if x + y < max_num:
        arr.append(x+y)
        fibonacci(arr, max_num)



if __name__ == "__main__":
    arr = [1,2]
    max_num = 4000000
    fibonacci(arr, max_num)

    arr = np.array(arr)
    sum_num = np.sum(arr[(arr % 2 == 0)])

    print('sum is %d' % sum_num)

        




    
    
