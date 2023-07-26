import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

: # Import the optimization code from scipy.

from scipy import optimize, stats

# Define a function that we will fit to the data. The function
# takes an array of values, x, at which to calculate its values,
# and parameters, m (the slope), c (the y intercept), that we wish to fit.def func(x, m, c):

def func(x,m,c):
    return m * x + c

# Fitting the function to the data is now as simple as one line, where
# [20, 80] is an initial guess of the slope and intercept:

pars, pars_covariance = optimize.curve_fit(func, x, y, [20, 80])

# And the one-sigma variances in the parameters are:

oneSigmaVariances = np.sqrt(np.diag(pars_covariance))

# Finally, plot the data, the error bars, the fit, and the
# parameters of the straight line.

plt.errorbar(x, y, yerr = yerr, fmt = '.', label = 'Data')
plt.plot(x, func(x, pars[0], pars[1]), label='Fit')
plt.text(0, 320, "y = ({:.1f} +/- {:.1f}) * x + ({:.1f} +/- {:.1f})".format(
    pars[0], oneSigmaVariances[0],
    pars[1], oneSigmaVariances[1]))

plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-0.5, 9.5)
plt.legend(loc='lower right')
plt.show()