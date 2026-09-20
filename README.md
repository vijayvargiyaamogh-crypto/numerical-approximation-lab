# Numerical Approximation Lab

A numerical methods laboratory for implementing, testing, and comparing algorithms for approximating mathematical functions.

## Motivation

Many numerical algorithms attempt to estimate the value of a function from limited information about that function.

This project explores that problem computationally. A reference implementation of a mathematical function is sampled at a finite set of input values, and approximation algorithms use those samples to estimate the function at new inputs.

The primary goal is to understand the mathematical behavior, accuracy, numerical stability, and computational cost of different approximation methods by implementing them from scratch and experimentally comparing them.

## Project Structure

| File | Purpose |
|---|---|
| `functions.py` | Reference implementations of mathematical functions used as targets for approximation |
| `approximations.py` | Approximation and interpolation algorithms |
| `solvers.py` | General numerical solvers used by approximation methods |
| `benchmarks.py` | Reusable tools for generating datasets and measuring approximation error |
| `experiments.py` | Specific numerical experiments performed during development |
| `plots.py` | Visualization of functions, approximations, and benchmark results |
| `config.py` | Project configuration |
| `main.py` | Main entry point |

## Current Progress

### Interpolation

- Nearest-neighbor interpolation
- Linear interpolation
- Quadratic interpolation
- General polynomial interpolation using the Lagrange form

### Polynomial Approximation

- Polynomial least-squares fitting
- Construction of Vandermonde matrices
- Normal equations
- Polynomial evaluation
- Polynomial approximation

### Numerical Solvers

- Gaussian elimination with partial pivoting
- Back substitution

### Reference Functions

The current reference-function library includes:

- Polynomial and power functions
- Radical functions
- Reciprocal
- Trigonometric functions
- Inverse trigonometric functions
- Hyperbolic functions

The reference functions are used to generate data and calculate the error of approximations. They are not the algorithms being benchmarked.

### Benchmarking

The current benchmarking framework measures approximation accuracy using:

- Maximum absolute error
- Root mean square error (RMSE)

The current experiments use a finite set of function evaluations as the input to an approximation method and evaluate the approximation on a denser, independent set of test points.

## Current Experiment

The first exploratory experiment compares nearest-neighbor interpolation on multiple reference functions.

For the current experiment:

- The sampling domain is `[0.01, 1]`
- 21 sample points are used to construct the approximation data
- 1001 independent test points are used for evaluation
- Accuracy is measured using maximum absolute error and RMSE

This experiment is exploratory rather than a final benchmark protocol. Different functions have different domains, smoothness properties, singularities, and other numerical characteristics, so later experiments will use domains and sampling strategies appropriate to the function and approximation method being studied.

## Design Principles

The project separates the mathematical object being approximated from the algorithm used to approximate it.

`functions.py` therefore contains reference functions, while `approximations.py` contains approximation algorithms.

Benchmarking is also separated from individual experiments. `benchmarks.py` provides reusable tools for measuring accuracy, while `experiments.py` records particular investigations performed with those tools.

This separation is intended to make it possible to compare multiple approximation methods on the same data and multiple functions under controlled experimental conditions.

## Planned Work

- Uniform interfaces for higher-order interpolation methods
- Taylor approximation
- Chebyshev approximation
- Additional approximation methods
- More systematic accuracy experiments
- Numerical stability analysis
- Visualization of approximations and error
- Runtime and performance benchmarking
- Investigation of approximation error bounds
- Improved experimental configuration

## Mathematical and Numerical Questions

As the project develops, experiments will investigate questions such as:

- How does approximation error depend on sampling density?
- How does the smoothness of a function affect approximation accuracy?
- How do singularities and rapidly varying regions affect interpolation?
- How do different interpolation methods compare?
- How closely do empirical errors follow theoretical error bounds?
- How does polynomial degree affect accuracy and numerical stability?
- How do different approximation methods trade accuracy for computational cost?

## Status

This project is under active development. Implementations and experimental methodology will evolve as new numerical methods are added and tested.