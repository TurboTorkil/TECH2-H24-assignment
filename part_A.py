"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""



def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    total = 0
    # Tried making input function to work with part_B, however it didn't work with the kernel
    #x_input = input()
    #x = [float(numb) for numb in x_input.split()]

    
    for numb in x:
        total += numb
    mean = total / len(x)
    #print(f"Mean: {mean}")
    
    var_sum = 0
    for numb in x:
        var_sum += ((numb - mean) ** 2)
    var = var_sum / len(x)
    #print(f"Variance: {var}")
    
    st_dev = pow(var, 0.5)
    # print(f"std_loops: standard deviation: {st_dev}")

    return st_dev



def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    import math
    
    mean = sum(x) / len(x)
    #print(f"Mean: {mean}")
    variance = sum((x - mean) ** 2 for x in x) / len(x)
    #print(f"Variance: {variance}")
    st_dev = math.sqrt(variance)
    # print(f"std_builtin: standard deviation: {st_dev}")

    return st_dev
        


def std_numpy(x):
    """
    Compute standard deviation of x using Numpy

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """ 

    import numpy as np

    st_dev = np.std(x)

    # print(st_dev)

    return st_dev


x = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    print(std_loops(x))
    print(std_builtin(x))
    print(std_numpy(x))
    