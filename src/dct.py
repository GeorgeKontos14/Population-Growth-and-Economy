from scipy.fft import fft, dct
import numpy as np

def type_2_dct(x, orthogonal = False):
    N = len(x)
    X = np.zeros(N)
    for k in range(N):
        for n in range(N):
            X[k] += 2*x[n]*np.cos(np.pi/N*(n+0.5)*k)
    if orthogonal:
        X[0] = X[0]*1/np.sqrt(2)
    return X 

def main():
    arr = np.array([4.0, 3.0, 5.0, 10.0, 5.0, 3.0])
    print(type_2_dct(arr))
    print(dct(arr))
    print("Orthogonalized:")
    print(type_2_dct(arr, orthogonal= True))
    print(dct(arr, orthogonalize=True))


if __name__ == "__main__":
    main()