import numpy as np
import matplotlib.pyplot as plt
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

# SIMULATED ANNEALING ALGORITHM
class SimulatedAnnealing:
    """Simulated Annealing optimizer for Rastrigin function"""
    
    def __init__(self, bounds, maxiter=1000, initial_temp=5.0, seed=42):
        """
        Parameters:
            bounds: numpy array of shape (d, 2), bounds for each dimension
            maxiter: int, maximum iterations
            initial_temp: float, initial temperature
            seed: int, random seed for reproducibility
        """
        self.bounds = np.array(bounds, dtype=np.float64)
        self.maxiter = maxiter
        self.initial_temp = initial_temp
        self.dim = self.bounds.shape[0]
        
        np.random.seed(seed)
        
        self.best_solution = None
        self.best_value = np.inf
        self.nfev = 0
        self.n_accepted = 0
        self.n_rejected = 0
        
        # History for visualization
        self.trajectory = []
        self.accepted_points = []
        self.rejected_points = []
        self.best_history = []
        self.temp_history = []
        
    def solve(self):
        """Run Simulated Annealing optimization"""
        start_time = time.time()
        
        # Initialize
        current = np.random.uniform(self.bounds[:, 0], self.bounds[:, 1], self.dim)
        current_value = rastrigin(current)
        self.nfev += 1
        
        self.best_solution = current.copy()
        self.best_value = current_value
        
        self.trajectory.append(current.copy())
        self.accepted_points.append(current.copy())
        self.best_history.append(self.best_value)
        self.temp_history.append(self.initial_temp)
        
        # Main loop
        for iteration in range(self.maxiter):
            temperature = self.initial_temp * (1 - iteration / self.maxiter)
            
            # Generate neighbor
            step_size = 0.5 * (self.bounds[:, 1] - self.bounds[:, 0]) * temperature / self.initial_temp
            neighbor = current + np.random.uniform(-step_size, step_size, self.dim)
            neighbor = np.clip(neighbor, self.bounds[:, 0], self.bounds[:, 1])
            
            # Evaluate
            neighbor_value = rastrigin(neighbor)
            self.nfev += 1
            
            # Acceptance criterion
            delta = neighbor_value - current_value
            
            if delta < 0:
                accept = True
            else:
                acceptance_prob = np.exp(-delta / temperature) if temperature > 0 else 0
                accept = np.random.rand() < acceptance_prob
            
            if accept:
                current = neighbor
                current_value = neighbor_value
                self.n_accepted += 1
                
                if iteration % 10 == 0:
                    self.accepted_points.append(current.copy())
                
                if current_value < self.best_value:
                    self.best_value = current_value
                    self.best_solution = current.copy()
            else:
                self.n_rejected += 1
                if iteration % 10 == 0:
                    self.rejected_points.append(neighbor.copy())
            
            # Store history
            if iteration % 10 == 0:
                self.trajectory.append(current.copy())
                self.best_history.append(self.best_value)
                self.temp_history.append(temperature)
        
        elapsed_time = time.time() - start_time
        return self.best_solution, self.best_value, elapsed_time
    
    def print_results(self):
        """Print optimization results"""
        print(f"\nSimulated Annealing Results:")
        print(f"  Solution: {self.best_solution}")
        print(f"  f(x*): {self.best_value:.6f}")
        print(f"  Function evaluations: {self.nfev}")
        print(f"  Accepted/Rejected: {self.n_accepted}/{self.n_rejected}")
    
    def visualize(self):
        """Visualize SA optimization process (2D only)"""
        if self.dim != 2:
            print("Visualization only available for 2D problems")
            return
        
        fig = plt.figure(figsize=(20, 7))
        
        # Create grid
        x1 = np.linspace(self.bounds[0, 0], self.bounds[0, 1], 200)
        x2 = np.linspace(self.bounds[1, 0], self.bounds[1, 1], 200)
        X1, X2 = np.meshgrid(x1, x2)
        Z = np.array([[rastrigin(np.array([x, y])) 
                        for x, y in zip(x_row, y_row)]
                        for x_row, y_row in zip(X1, X2)])
        
        # Plot 1: Surface with solution
        ax1 = plt.subplot(1, 3, 1)
        contour = ax1.contourf(X1, X2, Z, levels=30, cmap='viridis', alpha=0.8)
        plt.colorbar(contour, ax=ax1, label='f(x₁, x₂)')
        
        ax1.plot(self.best_solution[0], self.best_solution[1],
                'r*', markersize=30, 
                label=f'SA Solution\nx=({self.best_solution[0]:.2f}, {self.best_solution[1]:.2f})\nf={self.best_value:.4f}',
                markeredgecolor='white', markeredgewidth=2)
        
        if len(self.trajectory) > 0:
            ax1.plot(self.trajectory[0][0], self.trajectory[0][1],
                    'go', markersize=15, label='Start',
                    markeredgecolor='white', markeredgewidth=2)
        
        domain_text = f"Domain: [{self.bounds[0,0]:.2f}, {self.bounds[0,1]:.2f}]²"
        ax1.text(0.02, 0.02, domain_text, transform=ax1.transAxes,
                fontsize=10, verticalalignment='bottom',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        ax1.set_xlabel('x₁', fontsize=14)
        ax1.set_ylabel('x₂', fontsize=14)
        ax1.set_title('Rastrigin Function with SA Solution', fontsize=16, fontweight='bold')
        ax1.legend(fontsize=11, loc='upper right')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(self.bounds[0])
        ax1.set_ylim(self.bounds[1])
        
        # Plot 2: Trajectory
        ax2 = plt.subplot(1, 3, 2)
        ax2.contourf(X1, X2, Z, levels=30, cmap='viridis', alpha=0.3)
        
        if len(self.accepted_points) > 0:
            accepted = np.array(self.accepted_points)
            ax2.plot(accepted[:, 0], accepted[:, 1], 
                    'b-', linewidth=1, alpha=0.5, label='Accepted Path', zorder=1)
            ax2.scatter(accepted[:, 0], accepted[:, 1], 
                        c='blue', s=20, alpha=0.6, edgecolors='black', 
                        linewidths=0.5, zorder=2)
        
        if len(self.rejected_points) > 0:
            rejected = np.array(self.rejected_points)
            ax2.scatter(rejected[:, 0], rejected[:, 1], 
                        c='red', s=10, alpha=0.3, marker='x', 
                        label='Rejected', zorder=1)
        
        best_trajectory = []
        for i, val in enumerate(self.best_history):
            if i < len(self.trajectory):
                if i == 0 or val < self.best_history[i-1]:
                    best_trajectory.append(self.trajectory[i])
        
        if len(best_trajectory) > 1:
            best_traj = np.array(best_trajectory)
            ax2.plot(best_traj[:, 0], best_traj[:, 1], 
                    'g-', linewidth=2, alpha=0.8, 
                    label='Best Solution Path', zorder=3)
        
        if len(self.trajectory) > 0:
            ax2.plot(self.trajectory[0][0], self.trajectory[0][1],
                    'go', markersize=15, markeredgecolor='white', markeredgewidth=2,
                    label='Start', zorder=4)
        
        ax2.plot(self.best_solution[0], self.best_solution[1],
                'r*', markersize=30, markeredgecolor='white', markeredgewidth=2,
                label=f'Final (f={self.best_value:.4f})', zorder=5)
        
        ax2.set_xlabel('x₁', fontsize=14)
        ax2.set_ylabel('x₂', fontsize=14)
        ax2.set_title(f'Search Trajectory (Accepted: {self.n_accepted}, Rejected: {self.n_rejected})',
                        fontsize=16, fontweight='bold')
        ax2.legend(fontsize=9, loc='upper right')
        ax2.grid(True, alpha=0.3)
        ax2.set_xlim(self.bounds[0])
        ax2.set_ylim(self.bounds[1])
        
        # Plot 3: Convergence
        ax3 = plt.subplot(1, 3, 3)
        iterations = np.arange(len(self.best_history)) * 10
        ax3_twin = ax3.twinx()
        
        line1 = ax3.plot(iterations, self.best_history, 
                        'b-', linewidth=2, label='Best Value')
        ax3.axhline(y=0, color='g', linestyle='--', linewidth=1, alpha=0.5)
        ax3.fill_between(iterations, self.best_history, 0, alpha=0.2, color='blue')
        
        line2 = ax3_twin.plot(iterations, self.temp_history, 
                            'r-', linewidth=2, alpha=0.7, label='Temperature')
        
        ax3.set_xlabel('Iteration', fontsize=14)
        ax3.set_ylabel('Best Function Value', fontsize=14, color='b')
        ax3_twin.set_ylabel('Temperature', fontsize=14, color='r')
        ax3.tick_params(axis='y', labelcolor='b')
        ax3_twin.tick_params(axis='y', labelcolor='r')
        ax3.set_title('Convergence History', fontsize=16, fontweight='bold')
        ax3.grid(True, alpha=0.3)
        
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax3.legend(lines, labels, fontsize=11, loc='upper right')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Setup
    bounds = np.array([[0.5, 5.62], [0.5, 5.62]])
    maxiter = 1000
    # Run SA
    sa = SimulatedAnnealing(bounds=bounds, maxiter=maxiter, initial_temp=5.0, seed=42)
    solution, value, elapsed_time = sa.solve()
    # Print results
    print(f"\nSolution: {solution}")
    print(f"f(x*): {value:.6f}")
    print(f"Time: {elapsed_time:.3f}s")
    print(f"Evaluations: {sa.nfev}")
    print(f"Accepted/Rejected: {sa.n_accepted}/{sa.n_rejected}")
    # Visualize
    sa.visualize()