# HyperDualNumbers

Python implementation of Hyper-Dual Numbers [1] to calculate exact first and second derivatives.

[1] J. A. Fike and J. J. Alonso. The Development of Hyper-Dual Numbers for Exact Second-Derivative Calculations.
    AIAA paper 2011-886, 49th AIAA Aerospace Sciences Meeting, January 4-7, 2011.
    http://adl.stanford.edu/hyperdual/Fike_AIAA-2011-886.pdf


## Installation

You may want to clone the repository locally and install it via
```bash
python -m pip install . --user
```


## Usage

Within python the HyperDualNumber class may be imported using

```python
from hyperdualnumber import HyperDualNumber as hdn
```

First-derivative example:
```python
# instantiate a variable, to later obtain first derivatives of a function f(x) at x=5
h1 = 1.0
x = hdn(5, eps1=h1)

# define a function f(x)
f = 3*x**2

# f'(x=5)
f_prime = f.eps1/h1
```

Another first-derivative example, now using `eps2`
```python
# instantiate a variable, to later obtain first derivatives of a function f(x) at x=5
h2 = 1.0
x = hdn(5, eps2=h2)

# define a function f(x)
f = 3*x**2

# f'(x=5)
f_prime = f.eps2/h2
```

Second-derivative example:
```python
# instantiate a variable, to later obtain first and second derivatives of a function f(x)
h1 = 1.0
h2 = 1.0
x = hdn(5, eps1=h1, eps2=h2)

# define a function f(x)
f = 3*x**2

# f'(x=5)
f_prime = f.eps1/h1  # == f.eps2/h2

# f''(x=5)
f_pprime = f.eps1eps2/(h1*h2)
```

Note, that the `eps1eps2` property must not be set when declaring a variable like `x` from the above examples.


## Unit testing

From the package's root directory call one of the following
```bash
python -m unittest test.test_hyperdualnumber -v
python -m unittest discover -v
```
You may omit the `-v` flag, if you do not wish verbose output.
