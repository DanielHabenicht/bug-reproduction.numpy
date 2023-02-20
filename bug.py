from multiprocessing import Pool, cpu_count
import multiprocessing
import numpy as np
from tqdm import tqdm


def task(num):
    # Just some setup from the codebase the bug seen the first time
    # you might have to increase these for the bug to show.
    T = 10000
    N = 100

    K0 = np.zeros((N, N))
    K1 = np.zeros((N, N))
    Kd = np.zeros((N, N))

    np.fill_diagonal(K0, 0)
    np.fill_diagonal(K1, 1)
    np.fill_diagonal(Kd, 0)

    # Commenting out either of these remove the program hanging
    test1 = np.multiply.outer(K0, np.ones(T))
    test2 = np.multiply.outer(K1, np.ones(T))


if __name__ == "__main__":
    # Also hangs:
    # with multiprocessing.get_context("spawn").Pool(processes=cpu_count() - 1) as p:
    with Pool(processes=cpu_count() - 1) as p:
        # Bug only shows if queing more Jobs than CPU Counts
        jobs = [p.apply_async(func=task, args=[num]) for num in range(cpu_count() + 2)]

        for job in tqdm(jobs):
            job.get()
