import numpy as np
import itertools
import matplotlib.pyplot as plt
plt.rcParams['axes.facecolor'] = 'black'
import numba
from numba import njit, complex128

# Define the degree range for the polynomials

max_degree = 15

degree_range = range(1, max_degree)

# Generate all possible coefficients of +-1 for each polynomial
all_coefficients = []
for degree in degree_range:
    possible_coefficients = itertools.product([-1, 1], repeat=degree+1)
    all_coefficients += possible_coefficients
    
# Initialize lists to store the real and imaginary parts of the roots
real_parts = []
imag_parts = []


def rootscalc(coeffs):
    return np.roots(coeffs)


# Loop over all the possible coefficients and store the roots of each polynomial
for coefficients in all_coefficients:
    # Find the roots of the polynomial
    ncoeffs = np.array(coefficients)

    roots = rootscalc(ncoeffs)
    
    # Add the real and imaginary parts of the roots to the lists
    real_parts += list(roots.real)
    imag_parts += list(roots.imag)

fig = plt.figure(figsize=(10.2, 6.8), dpi=267)
fig.set_facecolor('black')

# Plot all the roots on the complex plane
plt.scatter(real_parts, imag_parts, s=.05, color='white', edgecolors='none')
plt.title(f"Roots of all polynomials with coefficients of ±1, up to degree {max_degree}")
plt.xlabel("Real axis")
plt.ylabel("Imaginary axis")


# Add origin point and lines where imaginary part and real part are zero
#plt.axhline(y=0, color='white', linestyle='-', linewidth=0.1)
#plt.axvline(x=0, color='white', linestyle='-', linewidth=0.1)
#plt.scatter(0, 0, s=5, color='red', marker='o')

plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

plt.show()
