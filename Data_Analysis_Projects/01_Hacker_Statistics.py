"""
Project: Hacker Statistics (Monte Carlo Simulation) - Empire State Building
Objective: 
1. Simulate 500 different random walks based on dice rolls.
2. Visualize the distribution of end-points using a histogram.
3. Calculate the probability of reaching the 60th step or higher.
Key Skills: Data Simulation, Random Walk, Probability Distribution, Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

# numpy and matplotlib imported, seed set
np.random.seed(123)

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        
        # Implement clumsiness (0.1% chance to fall)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create np_aw_t (Transpose for analysis)
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# --- VISUALIZATION ---
# Why Histogram instead of Bar?
# Bar charts compare categories. Histograms show the distribution of numbers.
# We want to see how the final steps are distributed.
# ... (Önceki kodların aynısı)

# Plot histogram of ends, Labels and Title, Ddisplay plot
plt.hist(ends, bins=10, edgecolor='black')
plt.title('Random Walk Simulation: Final Steps Distribution')
plt.xlabel('Final Step Number')
plt.ylabel('Frequency (How many times)')
plt.show()

# --- FINAL CALCULATION ---
# Calculating the probability of reaching step 60 or higher
prob = np.mean(ends >= 60)
print("Probability of reaching the 60th step: " + str(prob * 100) + "%")



