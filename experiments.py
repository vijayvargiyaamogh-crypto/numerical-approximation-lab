import functions
import approximations
import benchmarks

def nearest_neighbor_function_experiment():

    a = 0.01
    b = 1

    n = 21
    test_n = 1001

    xs = [a + i*(b-a)/(n-1) for i in range(n)]
    test_xs = [a + i*(b-a)/(test_n-1) for i in range(test_n)]

    functions_to_test = [
        ("identity", functions.identity),
        ("square", functions.square),
        ("sqrt", functions.sqrt),
        ("reciprocal", functions.reciprocal),
        ("sin", functions.sin),
        ("cos", functions.cos),
        ("tan", functions.tan),
        ("arcsin", functions.arcsin),
        ("arccos", functions.arccos),
        ("arctan", functions.arctan),
        ("sinh", functions.sinh),
        ("cosh", functions.cosh),
        ("tanh", functions.tanh)
    ]

    for name, f in functions_to_test:

        ys = [f(x) for x in xs]

        max_error, rmse = benchmarks.calculate_errors(
            f,
            approximations.nearest_neighbor,
            xs,
            ys,
            test_xs
        )

        print(name, max_error, rmse)

nearest_neighbor_function_experiment()