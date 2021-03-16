def find_min_newton(f_of_x, x0, tol=1e-10, kmax=30, debug=False):
    """Newton's method for finding critical points for multi-dimensional functions using HyperDualNumbers.

    Inputs:
        - f_of_x, string: expression for f(x), e.g.: f = 'x[0]**2 - x[1]**2'
        - x0, float or array of floats: initial guess
        - tol (optional), float: tolerance for convergence
        - kmax (optional), int: max. number of iterations
        - debug (optional), bool: print debug info

    Outputs:
        - x, list of floats: position of critial point
        - _, bool: flag whether method is converged
        - k, int: number of iterations
        - tp, string: type of the critical point
    """
    import numpy as np
    from hyperdualnumber import HyperDualNumber as hdn

    # Initialize perturbations for Hyper Dual Numbers (no real part)
    h = 1.0
    hd1 = hdn(0, eps1=h)
    hd2 = hdn(0, eps2=h)

    # Convert initial vector x to numpy array
    if isinstance(x0, list):
        x_np = np.array(x0, dtype=float)
    elif isinstance(x0, np.ndarray):
        x_np = x0
    elif isinstance(x0, float):
        x_np = np.array([x0], dtype=float)
    else:
        raise TypeError('Only a single float or an array of floats is allowed for x0.')

    # Initialize empty gradient vector and Hessian matrix in their actual size
    grad = np.empty(len(x_np), dtype=float)
    hess = np.empty((len(x_np), len(x_np)), dtype=float)

    # Newton's method
    k = 0
    while k < kmax:

        # Iterate through row index of Hessian matrix
        for i in range(len(x_np)):

            # Iterate through column index of Hessian matrix
            for j in range(i, len(x_np)):

                # Convert numpy array to list for operation with HyperDualNumber.
                # Note that x_np will still be a numpy array afterwards!
                x = x_np.tolist()

                # Perturb / mark the indices for derivation
                x[i] += hd1
                x[j] += hd2

                # Evaluate function
                f = eval(f_of_x)

                # Extract gradient and Hessian from HyperDualNumber f
                grad[i] = f.eps1/h
                hess[i][j] = f.eps1eps2/h**2
                hess[j][i] = hess[i][j]

        if debug:
            print(f'Iteration number {k}:')
            print(f'Gradient:\n{grad}')
            print(f'Hessian:\n{hess}\n')

        # Check if entries of the gradient are below tolerance and stop
        if all([abs(v) < tol for v in grad]):

            # Check eigenvalues of Hessian matrix to indicate type of critical point
            eigenvalues, _ = np.linalg.eig(hess)
            if all([v < 0.0 for v in eigenvalues]):
                tp = 'maximum'
            elif all([v > 0.0 for v in eigenvalues]):
                tp = 'minimum'
            elif all([abs(v) > 0.0 for v in eigenvalues]):
                tp = 'saddle point'
            elif np.linalg.det(hess) == 0.0:
                tp = 'degenerate critical point'

            if debug:
                print(f'Found {tp} in iteration no. {k} at x={x_np}')
            return x_np, True, k, tp

        # Calculate new step of Newton iteration (solve linear system instead of matrix multiplication with inverse of the Hessian)
        delta = -np.linalg.solve(hess, grad)
        x_np = x_np + delta

        # Increment iteration count
        k = k + 1

    if debug:
        print(f'No convergence after max. no. of iterations ({kmax}).')
    return x_np, False, k, ''
