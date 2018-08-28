from numba import jit
import time

"""
testing numba performance / general linkage in R
ben escobar, csafe-isu 2k24
@jit essentially speeds up a function its above
src:
    IEEE TRANSACTIONS ON SYSTEMS, MAN, 
    AND CYBERNETICS, VOL. SMC - 13, 
    NO. 1, JANUARY/FEBRUARY 1983 

"""
apples = [[1],[2],[3],[4]]
@jit
def test_process_jit(test_matrix):
    print("test process jit")
    t0 = time.time()
    for i in range(len(test_matrix)):
        for j in range(len(test_matrix[0])):
            print(t0)
    t1 = time.time()
    elapsed = t1-t0
    print("\n",elapsed)
    print("test process jit")

def test_no_r():
    test_process_jit(apples)
