from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import time 


def bin_coeff(n, m):
    num, denom = 1, 1
    if (m == 0 or m == n):
        return 1
    else:
        for k in range(0, m):
            num *= (n-k)
            denom *= k+1
        return num // denom


def make_table(total_energy, N_A, N_B):
    table_header = "q_A, multi_A, q_B, multi_B, multi_tot".split(", ")
    calculations = {k:[] for k in table_header}

    for q_A in range(0, total_energy+1):

        multiplicity_A = bin_coeff(q_A + N_A - 1, q_A)
        multiplicity_B = bin_coeff(total_energy - q_A + N_B - 1, total_energy - q_A)

        calculations["q_A"] += [q_A]
        calculations["multi_A"] += [multiplicity_A]
        calculations["q_B"] += [total_energy - q_A]
        calculations["multi_B"] += [multiplicity_B] 
        calculations["multi_tot"] += [multiplicity_A*multiplicity_B]

    table = pd.DataFrame(calculations)
    print(table)
    print(f"Total microstates: {table['multi_tot'].sum()}")
    return calculations


def make_histogram(data):
    multi_tot_heights = data["multi_tot"]
    q_As = data["q_A"]
    plt.bar(q_As, height=multi_tot_heights)
    plt.xticks(q_As)
    plt.xlabel(r"$q_{A}$")
    plt.ylabel(r"$\Omega_{total}$")
    plt.show()


def main():
    microstates_data = make_table(total_energy=8, N_A=3, N_B=10)
    make_histogram(data=microstates_data)


t1 = time.perf_counter()
main()
print(f"Run time: {time.perf_counter() - t1} seconds")