from run_experiment import *


def run_full_experiment():
    n_values = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    m_values = [100, 120, 140, 160, 180, 200, 220, 240]
    num_samples = 100

    results = {}

    for n in n_values:
        for m in m_values:
            r = calculate_r(n, m, num_samples)
            results[(n, m)] = r
            print(f"n={n}, m={m}, r={r}")

    return results

run_full_experiment()