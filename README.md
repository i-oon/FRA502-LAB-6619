# Branch and Bound vs Simulated Annealing for Rastrigin Function Optimization

A comparative study of deterministic (Branch and Bound) and stochastic (Simulated Annealing) algorithms for solving the Rastrigin Function Optimization problem across multiple dimensions (2D–5D).
The project analyzes the trade-off between guarantee and scalability, highlighting how deterministic accuracy contrasts with stochastic flexibility.

## Overview
- **Branch and Bound (BnB)**: A deterministic algorithm that systematically explores the search space and guarantees finding the global minimum within a defined tolerance (ε).
- **Simulated Annealing (SA)**: A stochastic algorithm inspired by metallurgical annealing, balancing exploration and exploitation via temperature decay. It runs efficiently with linear time complexity.

The test function is the **Rastrigin function**, a challenging non-convex optimization benchmark with multiple local minima:
```
f(x) = 10d + Σ(xi² - 10cos(2πxi))
Global minimum: f(0,...,0) = 0
```
## Experimental Setup

**Domain Design**
Offset domain [0.5, 5.62]^d is used instead of the standard [-5.12, 5.12]^d, keeping the same range (5.12 units).
This shifts the true global minimum x* = (0,0,…,0) outside but near the boundary (0.5 units away), creating a realistic constrained scenario where the optimum lies near a physical limit.

Test Dimensions: 2D → 5D
BnB ε values: 0.05–0.4
SA Parameters: Linear cooling, adaptive step size, 1000 iterations

## Implementation Features

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

### Members
- Disthorn Suttawet 66340500019
- Boonyaporn Preechasuth 66340500031