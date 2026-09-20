def solve_linear_system(A, b):
    """Solve Ax = b using Gaussian elimination with partial pivoting."""
    A = [row[:] for row in A] # copy A
    b = b[:] # copy b

    n = len(A)

    # Gaussian elimination
    for k in range(n-1):
        max_pivot = 0
        pivot_row = k

        # Find the largest available pivot
        for p in range(k, n):
            if abs(A[p][k]) > max_pivot:
                max_pivot = abs(A[p][k])
                pivot_row = p

        if max_pivot == 0:
            raise ValueError("System has no unique solution")

        # Swap the pivot row into position
        A[k], A[pivot_row] = A[pivot_row], A[k]
        b[k], b[pivot_row] = b[pivot_row], b[k]

        # Eliminate entries below the pivot
        for i in range(k+1, n):
            m = A[i][k] / A[k][k]

            for j in range(k, n):
                A[i][j] -= m*A[k][j]

            b[i] -= m*b[k]

    # Back substitution
    if A[n-1][n-1] == 0:
        raise ValueError("System has no unique solution")

    x = [0] * n

    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x