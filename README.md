# Branch and Bound vs Simulated Annealing for Rastrigin Function Optimization

A comparative study of deterministic (Branch and Bound) and stochastic (Simulated Annealing) algorithms for solving the Rastrigin function optimization problem across multiple dimensions.


## Overview
- **Branch and Bound (BnB)**: A deterministic algorithm that guarantees finding the global minimum within a specified tolerance (ε)
- **Simulated Annealing (SA)**: A stochastic algorithm inspired by metallurgical annealing, fast but without guarantee

The test function is the **Rastrigin function**, a challenging non-convex optimization benchmark with multiple local minima:
```
f(x) = 10d + Σ(xi² - 10cos(2πxi))
Global minimum: f(0,...,0) = 0
```

## Features

- **Branch and Bound Implementation**
  - Guaranteed global minimum within ε tolerance
  - Adaptive box splitting on widest dimension
  - Efficient pruning with lower/upper bounds
  - Corner evaluation for accurate upper bounds
  - 2D visualization of branching process

- **Simulated Annealing Implementation**
  - Metropolis acceptance criterion
  - Linear cooling schedule
  - Adaptive step size based on temperature
  - Search trajectory visualization
  - Convergence history tracking

- **Comprehensive Benchmarking**
  - Dimension scaling tests (2D-5D)
  - Epsilon sensitivity analysis
  - Automated performance comparison
  - Detailed timing and accuracy metrics

### File Descriptions
---
#### 1. `BranchAndBound.py`
**Key Classes:**
- `BranchAndBound`: Main optimizer class
  - `solve()`: Run optimization, returns (solution, value, time)
  - `visualize()`: Create 2D visualization (2D only)
  - `print_results()`: Display optimization results
**Key Parameters:**
- `bounds`: Search domain, shape (d, 2)
- `epsilon`: Stopping tolerance (smaller = more accurate)
---
#### 2. `SimulatedAnnealing.py`
**Key Classes:**
- `SimulatedAnnealing`: Main optimizer class
  - `solve()`: Run optimization, returns (solution, value, time)
  - `visualize()`: Create 3-panel visualization (2D only)
  - `print_results()`: Display optimization results
**Key Parameters:**
- `bounds`: Search domain, shape (d, 2)
- `maxiter`: Number of iterations (e.g., 1000)
- `initial_temp`: Starting temperature (e.g., 5.0)
- `seed`: Random seed for reproducibility
---
#### 3. `Comparing.py`
Benchmark script for systematic performance comparison
**Key Functions:**
- `run_benchmark()`: Run comprehensive tests
  - Returns structured results (list of dicts)
  - Configurable test cases
  - Automatic speedup calculation
---

### Documentation
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [SciPy Optimization](https://docs.scipy.org/doc/scipy/reference/optimize.html)


### Member
- Disthorn Suttawet 66340500019
- Boonyaporn Preechasuth 66340500031