import solvers

# Interpolation

def nearest_neighbor(x, xs, ys):
    if x < xs[0] or x > xs[-1]:
        raise ValueError("x is outside the lookup-table domain")
    low = 0
    high = len(xs)-2
    while low <= high:
        mid = (low+high)//2
        if xs[mid] < x:
            nn = mid
            low = mid+1
        elif x < xs[mid]:
            high = mid-1
        else:
            nn = mid
            break
    if 2*x <= xs[nn]+xs[nn+1]: # xs[nn] is closer or equally close
        return ys[nn]
    return ys[nn+1] # xs[nn+1] is closer

def linear_interpolation(x, x0, x1, y0, y1):
    m = (y1-y0)/(x1-x0) # slope
    y = y0 + m*(x-x0)
    return y

def quadratic_interpolation(x, x0, x1, x2, y0, y1, y2):
    # Lagrange form
    m0 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
    m1 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
    m2 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))
    y = y0*m0 + y1*m1 + y2*m2
    return y

def polynomial_interpolation(x, xs, ys):
    n = len(xs)-1
    L = [1 for i in range(n+1)] # Values of Lagrange basis polynomials at x
    for i in range(n+1):
        for j in range(n+1):
            if j != i:
                L[i] *= (x-xs[j])/(xs[i]-xs[j])
    y = sum(ys[i]*L[i] for i in range(n+1))
    return y

# Polynomial operations

def fit_polynomial(xs, ys, degree):
    n = len(xs)

    # Construct the Vandermonde matrix
    A = [[1 for j in range(degree+1)] for i in range(n)]
    for i in range(n):
        for j in range(1, degree+1):
            A[i][j] = A[i][j-1] * xs[i]

    # Construct the normal equations
    gram_matrix = [[sum(A[k][i]*A[k][j] for k in range(n)) 
            for j in range(degree+1)] 
            for i in range(degree+1)]
    rhs = [sum(A[k][i]*ys[k] for k in range(n)) 
           for i in range(degree+1)]

    coefficients = solvers.solve_linear_system(gram_matrix, rhs)

    return coefficients

def evaluate_polynomial(x, coefficients):
    pass

# Polynomial approximations

def polynomial_approximation(x, xs, ys, degree):
    coefficients = fit_polynomial(xs, ys, degree)
    return evaluate_polynomial(x, coefficients)

def taylor_approximation():
    pass

def chebyshev_approximation():
    pass

# Rational approximations

def rational_approximation():
    pass

# Lookup-table methods

def lookup_table():
    pass

# Iterative methods

def newton_raphson():
    pass

xs = [0, 1, 2, 3, 4]
ys = [1.1, 2.9, 5.2, 6.8, 9.1]

print(fit_polynomial(xs, ys, 1))