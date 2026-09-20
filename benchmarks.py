import math
import functions
import approximations

def generate_dataset(f, a, b, n):
    xs = [a + i*(b-a)/(n-1) for i in range(n)]
    ys = [f(x) for x in xs]
    return xs, ys

def calculate_errors(f, approximation, xs, ys, test_xs):
    errors = []

    for x in test_xs:
        y_approx = approximation(x, xs, ys)
        y_true = f(x)
        errors.append(abs(y_approx-y_true))

    max_error = max(errors)
    rmse = math.sqrt(sum(e**2 for e in errors)/len(errors))

    return max_error, rmse