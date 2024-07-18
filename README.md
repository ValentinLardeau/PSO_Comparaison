# Particle Swarm Optimization (PSO) for Biologically Inspired Computing

## Overview

This project, completed for a class on Biologically Inspired Computing, involves implementing a Particle Swarm Optimization (PSO) algorithm from scratch. The goal was to replace the traditional gradient descent method with PSO and conduct an experiment to analyze the effects of various hyperparameters on the algorithm's performance.

## Objectives

The main objectives of this project are:
1. To understand the principles and mechanics of the Particle Swarm Optimization algorithm.
2. To implement the PSO algorithm from scratch and integrate it into an optimization framework.
3. To replace the gradient descent method with PSO in a given optimization problem.
4. To conduct experiments to investigate the impact of different PSO hyperparameters on the optimization results.

## Particle Swarm Optimization (PSO)

### Algorithm Overview

Particle Swarm Optimization (PSO) is a computational method inspired by the social behavior of birds flocking or fish schooling. It is used to find optimal solutions by iteratively improving a candidate solution with respect to a given measure of quality.

### Key Components

- **Particles**: Represent candidate solutions in the search space.
- **Velocity**: Determines the direction and distance a particle moves in the search space.
- **Position**: Current location of a particle in the search space.
- **Personal Best**: The best solution a particle has achieved so far.
- **Global Best**: The best solution achieved by any particle in the swarm.

### PSO Pseudocode

1. Initialize a swarm of particles with random positions and velocities.
2. Evaluate the fitness of each particle.
3. Update personal and global best positions.
4. Update velocities and positions of particles.
5. Repeat steps 2-4 until a stopping criterion is met.

## Implementation

### Steps

1. **Initialization**:
    - Randomly initialize positions and velocities of the particles.
    - Set initial personal and global best positions.

2. **Fitness Evaluation**:
    - Define a fitness function to evaluate the quality of solutions.

3. **Update Rules**:
    - Update velocities based on personal best, global best, and current velocity.
    - Update positions based on the new velocities.

4. **Iteration**:
    - Repeat the fitness evaluation and update rules for a specified number of iterations or until convergence.

### Code Implementation

The PSO algorithm was implemented in Python. Key modules and libraries used include:
- **NumPy**: For numerical operations and random number generation.
- **Matplotlib**: For visualizing the optimization process and results.

## Hyperparameter Experiment

### Hyperparameters

The hyperparameters investigated include:
- **Number of Particles**: The size of the swarm.
- **Inertia Weight**: Balances global and local exploration.
- **Cognitive Coefficient**: Weight of the personal best influence.
- **Social Coefficient**: Weight of the global best influence.

### Experimental Setup

1. **Define Ranges**: Set ranges for each hyperparameter to be tested.
2. **Run Experiments**: Conduct multiple runs with different combinations of hyperparameters.
3. **Collect Data**: Record the performance metrics for each run.
4. **Analyze Results**: Use statistical methods to analyze the impact of hyperparameters on optimization performance.

## Results and Analysis

- **Performance Metrics**: Include convergence speed, final solution quality, and computational efficiency.
- **Visualization**: Graphs and plots showing the impact of different hyperparameter settings on the optimization process.
- **Insights**: Summary of findings and recommendations for optimal hyperparameter settings.

## Conclusion

This project successfully demonstrated the implementation of the PSO algorithm from scratch and its application to replace the gradient descent method in an optimization problem. The hyperparameter experiments provided valuable insights into the effects of different settings on the algorithm's performance.

## Tools and Technologies

- **Python**: For implementing the PSO algorithm and conducting experiments.
- **NumPy**: For efficient numerical computations.
- **Matplotlib**: For visualizing the optimization process and results.
