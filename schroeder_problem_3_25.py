import matplotlib.pyplot as plt
import numpy as np

def main():
    t = np.arange(0.1, 2, 0.0001)
    heat_capacity = (1/t)**2*np.exp(1/t)/(np.exp(1/t)-1)**2

    plt.plot(t, heat_capacity)
    plt.show()

main()