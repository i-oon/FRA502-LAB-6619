import numpy as np
import time

# RASTRIGIN FUNCTION
def rastrigin(x):
    """Rastrigin Function: f(x) = 10d + Σ(xi² - 10cos(2πxi))"""
    x = np.atleast_1d(x).flatten()
    A = 10.
    d = x.shape[0]
    return A * d + np.sum(x**2 - A * np.cos(2. * np.pi * x))

# BRANCH AND BOUND
class BranchAndBound:
    def __init__(self, bounds, epsilon=0.5):
        self.bounds = np.array(bounds, dtype=np.float64)
        self.epsilon = epsilon
        self.dim = self.bounds.shape[0]
        self.best_solution = None
        self.best_value = np.inf
        self.nodes_explored = 0
        
    def compute_lower_bound(self, box):
        A = 10.
        lower_bound = A * self.dim
        for i in range(self.dim):
            a, b = box[i, 0], box[i, 1]
            sq_term = min(a**2, b**2) if a * b >= 0. else 0.
            lower_bound += sq_term - A
        return lower_bound
    
    def _get_corners(self, box):
        import itertools
        if self.dim > 8:
            return [np.array([box[i, np.random.randint(2)] for i in range(self.dim)]) 
                    for _ in range(256)]
        return [np.array([box[i, c] for i, c in enumerate(combo)]) 
                for combo in itertools.product([0, 1], repeat=self.dim)]
    
    def compute_upper_bound(self, box):
        center = np.mean(box, axis=1)
        best_value = rastrigin(center)
        best_point = center.copy()
        
        for corner in self._get_corners(box):
            value = rastrigin(corner)
            if value < best_value:
                best_value = value
                best_point = corner.copy()
        
        return best_value, best_point
    
    def split_box(self, box):
        widths = box[:, 1] - box[:, 0]
        split_dim = np.argmax(widths)
        mid = (box[split_dim, 0] + box[split_dim, 1]) / 2.
        
        box_left = box.copy()
        box_left[split_dim, 1] = mid
        box_right = box.copy()
        box_right[split_dim, 0] = mid
        
        return box_left, box_right
    
    def solve(self, max_iterations=50000, max_time=300):
        start_time = time.time()
        
        initial_lb = self.compute_lower_bound(self.bounds)
        initial_ub, initial_point = self.compute_upper_bound(self.bounds)
        self.best_value = initial_ub
        self.best_solution = initial_point
        
        queue = [(initial_lb, self.bounds.copy())]
        iteration = 0
        
        while queue and iteration < max_iterations:
            if time.time() - start_time > max_time:
                return self.best_solution, self.best_value, max_time, "Timeout"
            
            queue.sort(key=lambda x: x[0])
            lower_bound, current_box = queue.pop(0)
            self.nodes_explored += 1
            iteration += 1
            
            if lower_bound >= self.best_value:
                continue
            
            max_width = np.max(current_box[:, 1] - current_box[:, 0])
            if max_width < self.epsilon:
                ub, point = self.compute_upper_bound(current_box)
                if ub < self.best_value:
                    self.best_value = ub
                    self.best_solution = point.copy()
                continue
            
            box_left, box_right = self.split_box(current_box)
            for new_box in [box_left, box_right]:
                lb = self.compute_lower_bound(new_box)
                ub, point = self.compute_upper_bound(new_box)
                
                if ub < self.best_value:
                    self.best_value = ub
                    self.best_solution = point.copy()
                
                if lb < self.best_value:
                    queue.append((lb, new_box))
        
        elapsed_time = time.time() - start_time
        status = "MaxIter" if iteration >= max_iterations else "Success"
        return self.best_solution, self.best_value, elapsed_time, status

# SIMULATED ANNEALING
class SimulatedAnnealing:
    def __init__(self, bounds, maxiter=1000, initial_temp=5.0, seed=42):
        self.bounds = np.array(bounds)
        self.maxiter = maxiter
        self.initial_temp = initial_temp
        self.dim = len(bounds)
        np.random.seed(seed)
        self.best_solution = None
        self.best_value = np.inf
        
    def solve(self):
        start_time = time.time()
        
        current = np.random.uniform(self.bounds[:, 0], self.bounds[:, 1], self.dim)
        current_value = rastrigin(current)
        
        self.best_solution = current.copy()
        self.best_value = current_value
        
        for iteration in range(self.maxiter):
            temperature = self.initial_temp * (1 - iteration / self.maxiter)
            
            step_size = 0.5 * (self.bounds[:, 1] - self.bounds[:, 0]) * temperature / self.initial_temp
            neighbor = current + np.random.uniform(-step_size, step_size, self.dim)
            neighbor = np.clip(neighbor, self.bounds[:, 0], self.bounds[:, 1])
            
            neighbor_value = rastrigin(neighbor)
            delta = neighbor_value - current_value
            
            if delta < 0 or np.random.rand() < np.exp(-delta / temperature):
                current = neighbor
                current_value = neighbor_value
                
                if current_value < self.best_value:
                    self.best_value = current_value
                    self.best_solution = current.copy()
        
        elapsed_time = time.time() - start_time
        return self.best_solution, self.best_value, elapsed_time

# BENCHMARK RUNNER
def run_benchmark(configs=None, verbose=True):
    """
    Run benchmark tests comparing BnB and SA.
    
    Parameters:
        configs: list of dict, each containing:
            - dim: int, problem dimension
            - bounds: list, base bound for each dimension
            - epsilon: float, BnB tolerance
            - sa_iters: int, SA iterations
            - timeout: float, max time for BnB (seconds)
        verbose: bool, print results table
    
    Returns:
        results: list of dict containing test results
    """
    if configs is None:
        configs = [
            {'dim': 2, 'bounds': [[0.5, 5.62]], 'epsilon': 0.4, 'sa_iters': 1000, 'timeout': 30},
            {'dim': 2, 'bounds': [[0.5, 5.62]], 'epsilon': 0.2, 'sa_iters': 1000, 'timeout': 60},
            {'dim': 2, 'bounds': [[0.5, 5.62]], 'epsilon': 0.1, 'sa_iters': 1000, 'timeout': 120},
            {'dim': 2, 'bounds': [[0.5, 5.62]], 'epsilon': 0.05, 'sa_iters': 1000, 'timeout': 180},
            {'dim': 3, 'bounds': [[0.5, 5.62]], 'epsilon': 0.3, 'sa_iters': 1500, 'timeout': 180},
            {'dim': 4, 'bounds': [[0.5, 5.62]], 'epsilon': 0.3, 'sa_iters': 2000, 'timeout': 300},
            {'dim': 5, 'bounds': [[0.5, 5.62]], 'epsilon': 0.3, 'sa_iters': 2500, 'timeout': 300},
        ]
    
    results = []
    
    if verbose:
        print("\nBenchmark Results (Offset Bounds [0.5, 5.62]^d)")
        print("="*100)
        print(f"{'Dim':<5} {'ε':<6} {'BnB Time':<12} {'BnB f(x)':<12} "
                f"{'SA Time':<12} {'SA f(x)':<12} {'Speedup':<15}")
        print("-"*100)
    
    for config in configs:
        dim = config['dim']
        epsilon = config['epsilon']
        base_bound = config['bounds'][0]
        bounds = np.array([base_bound] * dim)
        
        result = {
            'dim': dim,
            'epsilon': epsilon,
            'bounds': bounds
        }
        
        # Run BnB
        try:
            bnb = BranchAndBound(bounds, epsilon=epsilon)
            _, bnb_value, bnb_time, bnb_status = bnb.solve(max_time=config['timeout'])
            
            result['bnb_time'] = bnb_time
            result['bnb_value'] = bnb_value if bnb_status != "Timeout" else None
            result['bnb_status'] = bnb_status
        except Exception as e:
            result['bnb_time'] = None
            result['bnb_value'] = None
            result['bnb_status'] = 'Error'
        
        # Run SA
        sa = SimulatedAnnealing(bounds, maxiter=config['sa_iters'], seed=42)
        _, sa_value, sa_time = sa.solve()
        
        result['sa_time'] = sa_time
        result['sa_value'] = sa_value
        
        # Calculate speedup
        if result['bnb_time'] and result['bnb_status'] != "Timeout":
            result['speedup'] = result['bnb_time'] / sa_time
            result['faster'] = 'SA' if result['speedup'] > 1 else 'BnB'
        else:
            result['speedup'] = None
            result['faster'] = 'SA'
        
        results.append(result)
        
        # Print row
        if verbose:
            bnb_time_str = f"{result['bnb_time']:.3f}s" if result['bnb_time'] and result['bnb_status'] != "Timeout" else f">{config['timeout']}s"
            bnb_value_str = f"{result['bnb_value']:.4f}" if result['bnb_value'] is not None else "---"
            sa_time_str = f"{sa_time:.3f}s"
            sa_value_str = f"{sa_value:.4f}"
            
            if result['speedup']:
                if result['speedup'] > 1:
                    speedup_str = f"{result['speedup']:.1f}x (SA)"
                else:
                    speedup_str = f"{1/result['speedup']:.1f}x (BnB)"
            else:
                speedup_str = ">100x (SA)"
            
            print(f"{dim:<5} {epsilon:<6.2f} {bnb_time_str:<12} {bnb_value_str:<12} "
                    f"{sa_time_str:<12} {sa_value_str:<12} {speedup_str:<15}")
    
    if verbose:
        print("="*100)
    
    return results

if __name__ == "__main__":
    results = run_benchmark(verbose=True)