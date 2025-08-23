import math
import matplotlib.pyplot as plt
import numpy as np # Using numpy for ranges is more standard and efficient

def f1(n):
    return 5 * n**2 + 20 * n + 100

def f2(n):
    return 0.1 * n**3 + 50 * n**2

def f3(n):
    # Using np.log10 is safer as it handles arrays and edge cases gracefully
    return 1000 * np.log10(n) + 50

# --- Data Preparation using NumPy ---
# Using np.arange is generally preferred for numerical ranges
n_values = np.arange(1, 100)
large_n_values = np.arange(1, 1000)

# Calculate y-values (NumPy allows vectorized operations, no need for list comprehensions)
f1_y = f1(n_values)
f2_y = f2(n_values)
f3_y = f3(n_values)

f1_large_y = f1(large_n_values)
f2_large_y = f2(large_n_values)
f3_large_y = f3(large_n_values)


# --- Plot 1: Initial view (where constants can mislead) ---
plt.figure(figsize=(10, 6))
plt.plot(n_values, f1_y, label='f1(n) = 5n² + ... (O(n²))')
plt.plot(n_values, f2_y, label='f2(n) = 0.1n³ + ... (O(n³))')
plt.plot(n_values, f3_y, label='f3(n) = 1000log(n) + ... (O(log n))')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')
plt.title('Function Growth Rates (Initial View, n=1-99)')
plt.legend()
plt.grid(True)
plt.show()

# --- Plot 2: The "Asymptotic Revelation" (Log Scale for true understanding) ---
plt.figure(figsize=(10, 6))
plt.plot(large_n_values, f1_large_y, label='f1 (O(n²))')
plt.plot(large_n_values, f2_large_y, label='f2 (O(n³))')
plt.plot(large_n_values, f3_large_y, label='f3 (O(log n))')
plt.yscale('log') # The "Time Carpet" stretched to reveal its true patterns
plt.xlabel('Input Size (n)')
plt.ylabel('Operations (Log Scale)')
plt.title('Function Growth Rates (Asymptotic Revelation, Log Scale)')
plt.legend()
plt.grid(True)
plt.show()