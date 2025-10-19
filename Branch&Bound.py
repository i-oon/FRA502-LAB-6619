import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time

# RASTRIGIN FUNCTION
def rastrigin(x):
    """
    Rastrigin Function: f(x) = 10d + Σ(xi² - 10cos(2πxi))
    Global Minimum: f(0, ..., 0) = 0
    """
    x = np.atleast_1d(x).flatten()
    A = 10.
    d = x.shape[0]
    return A * d + np.sum(x**2 - A * np.cos(2. * np.pi * x))

# BRANCH AND BOUND ALGORITHM
class BranchAndBound:
    """Branch and Bound optimizer for Rastrigin function"""
    
    def __init__(self, bounds, epsilon=0.1):
        """
        Parameters:
            bounds: numpy array of shape (d, 2), bounds for each dimension
            epsilon: float, stopping tolerance (smaller = more accurate)
        """
        self.bounds = np.array(bounds, dtype=np.float64)
        self.epsilon = epsilon
        self.dim = self.bounds.shape[0]
        
        self.best_solution = None
        self.best_value = np.inf
        self.nodes_explored = 0
        self.nodes_pruned = 0
        self.history = []
        
    def compute_lower_bound(self, box):
        """Compute lower bound for Rastrigin in the given box"""
        A = 10.
        lower_bound = A * self.dim
        
        for i in range(self.dim):
            a, b = box[i, 0], box[i, 1]
            sq_term = min(a**2, b**2) if a * b >= 0. else 0.
            cos_term = -A
            lower_bound += sq_term + cos_term
        
        return lower_bound
    
    def _get_corners(self, box):
        """Generate all corners of a box"""
        import itertools
        corners = []
        for combo in itertools.product([0, 1], repeat=self.dim):
            corner = np.array([box[i, combo[i]] for i in range(self.dim)])
            corners.append(corner)
        return corners
    
    def compute_upper_bound(self, box):
        """Compute upper bound by evaluating at center and corners"""
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
        """Split box into two sub-boxes along widest dimension"""
        widths = box[:, 1] - box[:, 0]
        split_dim = np.argmax(widths)
        mid = (box[split_dim, 0] + box[split_dim, 1]) / 2.
        
        box_left = box.copy()
        box_left[split_dim, 1] = mid
        box_right = box.copy()
        box_right[split_dim, 0] = mid
        
        return box_left, box_right
    
    def solve(self, max_iterations=10000):
        """Main Branch and Bound algorithm"""
        start_time = time.time()
    
        # Initialize
        initial_lb = self.compute_lower_bound(self.bounds)
        initial_ub, initial_point = self.compute_upper_bound(self.bounds)
        self.best_value = initial_ub
        self.best_solution = initial_point
        
        queue = [(initial_lb, self.bounds.copy())]
        iteration = 0
        
        # Main loop
        while queue and iteration < max_iterations:
            queue.sort(key=lambda x: x[0])
            lower_bound, current_box = queue.pop(0)
            self.nodes_explored += 1
            iteration += 1
            
            # Pruning
            if lower_bound >= self.best_value:
                self.nodes_pruned += 1
                continue
            
            # Check stopping criterion
            max_width = np.max(current_box[:, 1] - current_box[:, 0])
            if max_width < self.epsilon:
                ub, point = self.compute_upper_bound(current_box)
                if ub < self.best_value:
                    self.best_value = ub
                    self.best_solution = point.copy()
                continue
            
            # Branching
            box_left, box_right = self.split_box(current_box)
            for new_box in [box_left, box_right]:
                lb = self.compute_lower_bound(new_box)
                ub, point = self.compute_upper_bound(new_box)
                
                if ub < self.best_value:
                    self.best_value = ub
                    self.best_solution = point.copy()
                
                if lb < self.best_value:
                    queue.append((lb, new_box))
                    self.history.append(new_box.copy())
                else:
                    self.nodes_pruned += 1
        
        elapsed_time = time.time() - start_time
        return self.best_solution, self.best_value, elapsed_time
    
    def print_results(self):
        """Print optimization results"""
        print(f"\nBranch and Bound Results:")
        print(f"  Solution: {self.best_solution}")
        print(f"  f(x*): {self.best_value:.6f}")
        print(f"  Nodes explored: {self.nodes_explored}")
        print(f"  Nodes pruned: {self.nodes_pruned}")
    
    def visualize(self):
        """Visualize the optimization process (2D only)"""
        if self.dim != 2:
            print("Visualization only available for 2D problems")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
        
        # Create grid
        x1 = np.linspace(self.bounds[0, 0], self.bounds[0, 1], 200)
        x2 = np.linspace(self.bounds[1, 0], self.bounds[1, 1], 200)
        X1, X2 = np.meshgrid(x1, x2)
        Z = np.array([[rastrigin(np.array([x, y])) 
                        for x, y in zip(x_row, y_row)]
                        for x_row, y_row in zip(X1, X2)])
        
        # Plot 1: Rastrigin surface with solution
        contour = ax1.contourf(X1, X2, Z, levels=30, cmap='viridis', alpha=0.8)
        plt.colorbar(contour, ax=ax1, label='f(x₁, x₂)')
        
        if self.best_solution is not None:
            ax1.plot(self.best_solution[0], self.best_solution[1],
                    'r*', markersize=30, 
                    label=f'BnB Solution\nx=({self.best_solution[0]:.2f}, {self.best_solution[1]:.2f})\nf={self.best_value:.4f}',
                    markeredgecolor='white', markeredgewidth=2)
        
        domain_text = f"Domain: [{self.bounds[0,0]:.2f}, {self.bounds[0,1]:.2f}]²"
        ax1.text(0.02, 0.02, domain_text, transform=ax1.transAxes,
                fontsize=10, verticalalignment='bottom',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        ax1.set_xlabel('x₁', fontsize=14)
        ax1.set_ylabel('x₂', fontsize=14)
        ax1.set_title('Rastrigin Function with BnB Solution', fontsize=16, fontweight='bold')
        ax1.legend(fontsize=11, loc='upper right')
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Branching process
        ax2.contourf(X1, X2, Z, levels=30, cmap='viridis', alpha=0.3)
        
        step = max(1, len(self.history) // 200)
        for box in self.history[::step]:
            rect = Rectangle((box[0, 0], box[1, 0]),
                            box[0, 1] - box[0, 0],
                            box[1, 1] - box[1, 0],
                            linewidth=0.5, edgecolor='red',
                            facecolor='none', alpha=0.5)
            ax2.add_patch(rect)
        
        if self.best_solution is not None:
            ax2.plot(self.best_solution[0], self.best_solution[1],
                    'r*', markersize=30, markeredgecolor='white', markeredgewidth=2)
        
        ax2.set_xlabel('x₁', fontsize=14)
        ax2.set_ylabel('x₂', fontsize=14)
        ax2.set_title(f'Branching Process ({self.nodes_explored} explored, {self.nodes_pruned} pruned)',
                        fontsize=16, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        ax2.set_xlim(self.bounds[0])
        ax2.set_ylim(self.bounds[1])
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Setup
    bounds = np.array([[0.5, 5.62], [0.5, 5.62]])
    epsilon = 0.2
    # Run BnB
    bnb = BranchAndBound(bounds, epsilon=epsilon)
    solution, value, elapsed_time = bnb.solve()
    # Print results
    print(f"\nSolution: {solution}")
    print(f"f(x*): {value:.6f}")
    print(f"Time: {elapsed_time:.3f}s")
    print(f"Nodes: {bnb.nodes_explored} explored, {bnb.nodes_pruned} pruned")
    # Visualize
    bnb.visualize()