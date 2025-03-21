import random

def weighted_random_selection(tick, cross):
    M = len(tick)
    N = len(cross)
    
    # Create a combined list with weights
    combined = [(item, 1) for item in tick] + [(item, 3) for item in cross]
    
    # Unpack the items and weights
    items, weights = zip(*combined)
    
    # Use random.choices for weighted random selection
    selected = random.choices(items, weights=weights, k=1)[0]
    
    return selected

# Example usage
tick = [1, 2, 3, 4, 5]
cross = [6,7, 8, 9, 10]

# Test the function
for _ in range(20):  # Let's run it 20 times as an example
    result = weighted_random_selection(tick, cross)
    print(f"Selected: {result}")

# Calculate and print the theoretical probability
M = len(tick)
N = len(cross)
prob_cross = (N * 3) / (N * 3 + M)
print(f"\nTheoretical probability of selecting from cross: {prob_cross:.2f}")

# if the probability is 3 -> 5 -> 8 -> 13
prob_list = [1, 3, 5, 8, 13]
product = 1
for prob in prob_list:
    product *= prob
freq_list = [product // prob for prob in prob_list]
print(f"\nFrequency list: {freq_list}")

cross_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
