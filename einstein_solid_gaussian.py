"""Interactively illustrate Gaussian behaviour for two Einstein solids with
increasing numbers of oscillators"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sf
import readchar  # will need to be installed.

def entropy(N, q):  # natural log of multiplicity
    return sf.gammaln(N+q-1+1) - sf.gammaln(q+1) - sf.gammaln(N-1+1)

def calc_all(n_a, n_b, q_tot):
    q_a_s = np.array(range(0, q_tot+1))
    es = [(entropy(n_a, q_a) + entropy(n_b, q_tot-q_a)) for q_a
          in q_a_s]
    normalized_multiplicity = np.exp(es)
    return q_a_s, normalized_multiplicity

def main():
    plt.ion()
    plt.rcParams.update({"font.size":16})

    ns = [3, 10, 30, 100]
    i = 0
    while(True):
        n = ns[i]
        n_a = n
        n_b = n
        q_total = n_a * 2
        qs, nms = calc_all(n_a, n_b, q_total)

        ax = plt.gca()
        if n < 10:
            ax.xaxis.set_ticks(np.arange(0, q_total+1, 1))
        label = r"$n = $ " + str(n) + "\n"
        label += r"$q_{\rm tot} = $ " + str(q_total)
        ax.bar(qs, nms, align="center", label=label)
        ax.set_xlabel(r"$q_a$")
        ax.set_ylabel(r"$\Omega$")
        ax.legend()
        plt.pause(0.1)
        print("left arrow to decrease, right arrow to increase, q to quit: ",
              end="", flush=True)
        k = readchar.readkey()
        print("Got it.", flush=True)
        if k == '\x1b[C' and i < len(ns)-1:
            i += 1
        elif k == '\x1b[D' and i > 0:
            i -= 1
        elif k == "q":
            break
        ax.clear()

if __name__ == "__main__":
    main()