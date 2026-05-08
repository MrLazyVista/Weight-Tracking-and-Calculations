import numpy as np
import matplotlib.pyplot as plt

# 2.2 is the weight factor (calories burned = estmated weight * weight factor)
# 2000 is the estimate base calories burned
# 0.0002 is the estimated calories burned per step per pound of weight
variables = [2.95,1660,0.0002]
starting_weight = 152.25

# calories consumed, steps taken, morning weight
data = [
    [2031, 13851, 153],
    [2031, 4058, 150.9],
    [2031, 2956, 151.3],
    [2031, 14485, 151.3],
    [2031, 13435, 151.6],
    [2031, 15348.5, 152],
    [2056, 3500.5, 151.3],
    [1914, 2710, 151],
    [1914, 2317.5, 152.1],
    [1914, 5495.5, 151.1],
    [1754, 4337, 152.1],
    [1728, 1098, 151.1],
    [1728, 3235, 151.3],
    [1808, 2884.5, 151.2],
    [1728, 2000.5, 150],
    [1728, 3363, 149.4],
    [2028, 2290.5, 148.8],
    [1953, 5154, 149.9],
    [1818, 3221, 151],
    [1978, 3179, 150.2],
    [1859, 4577, 150],
    [1884, 5507.5, 149.6],
    [1854, 3957, 149.4],
    [1826, 3084.5, 149.7],
    [1832, 4548.5, 150],
    [1836, 3024, 150],
    [1836, 5151, 149.4],
    [1851, 3742, 149],
    [1826, 4202.5, 149.4],
    [1838, 5706, 149],
    [1818, 2342.5, 149.1],
    [1783, 4759, 148.1],
    [1788, 4676, 148.6],
    [1790, 3379, 148.6],
    [1826, 2824, 149.6],
    [1763, 2744.5, 148.4],
    [1703, 4034.5, 149.6],
    [1863, 4611, 149.3],
    [1793, 4162, 148.8],
    [1767, 2836, 148.6],
    [1782, 3384, 148.1],
    [1837, 4621, 148.9],
    [1787, 3756.5, 148.1],
    [1822, 3406, 147],
    [1747, 7652, 146.9],
    [1749, 11745, 147.8],
    [1734, 18676, 147.8],
    [1734, 2417, 147.7],
    [1766, 3202, 146.4],
    [1738, 5525, 146.7],
    [1763, 3589.5, 145.2],
    [1768, 4285, 145.1],
    [1737, 5753, 145.2],
    [1730, 16850, 145.1],
    [1722, 2515, 145.1],
    [1719, 2938, 144],
    [2185, 2000, 144.3],
    [2215, 3000, 144],
    [2200, 3000, 144.3],
    [2200, 3000, 144.4],
    [2200, 3000, 145.4],
    [2200, 3000, 146.2],
    [2200, 3000, 146.4],
    [2200, 3000, 145.4],
    [1960, 3000, 145.7],
    [1680, 4272, 146.1],
    [1680, 2885, 146.5],
    [1678, 2746, 144.7],
    [1685, 5892, 145],
    [1680, 7166, 144.5],
    [1733, 5466, 145],
    [1732, 5079.5, 145],
    [1698, 11742, 145.2],
    [1685, 9016, 144.5],
    [1714, 6076, 143.8],
    [1702, 22911, 144.3],
    [1694, 7676, 145],
    [1703, 2690.5, 143.7],
    [1753, 5408, 143.6],
    [1753, 5917, 142.6],
    [1753, 5793, 142],
    [1753, 15039, 142],
    [1707, 3536, 141.8],
    [1712, 6184, 142.4],
    [1772, 4581, 142.4],
    [1877, 8246.5, 142.5],
    [1718, 6702, 142.9],
    [1726, 5051, 142.4],
    [1723, 21240, 142.1],
    [1723, 23101, 140.7],
    [1751, 5917, 140.4],
    [1726, 5812.5, 141],
    [1649, 7845, 140.2],
    [1318, 7462, 140],
    [1691, 8392.5, 141],
    [1729, 9762, 139.2],
    [1741, 14637, 138.8],
    [2145, 12624.5, 138.6],
    [2254, 14755, 138.7],
    [1984, 10957, 140.1],
    [2089, 12000, 140],
    [1834, 10230, 140.4],
    [2241, 16586, 140.7],
    [2256, 17000, 139.9],
    [1991, 10544, 139.1],
    [1999, 13000, 139.2],
    [1897, 9059	,138.9],
    [1927, 10500,139.2],
    [1749, 6000	,139.7]
]
true_weight = []
LowestVariance = float('inf')

adj_weight_factor = np.linspace(variables[0]*0.5, variables[0]*2, 20)
adj_base_calories = np.linspace(variables[1]*0.5, variables[1]*1.5, 100)
adj_calories_per_step = np.linspace(variables[2]*0.5, variables[2]*2, 30)
optimized_variables = variables.copy()

for weight_factor in adj_weight_factor:
    for base_calories in adj_base_calories:
        for calories_per_step in adj_calories_per_step:
            adjusted_variables = [weight_factor, base_calories, calories_per_step]
            adjusted_calories = []
            for i in range(len(data)):
                adjusted_calories.append((data[i][0]                                        # calories consumed
                                        - adjusted_variables[0]*data[i][2]                  # calories burned from weight
                                        - adjusted_variables[1]                             # calories burned as a base
                                        - adjusted_variables[2]*data[i][1]*data[i][2]))     # calories burned per step per bodyweight
                if len(true_weight) == 0:
                    true_weight.append(starting_weight + adjusted_calories[i]/3500)
                else:
                    true_weight.append(true_weight[len(true_weight)-1] + adjusted_calories[i]/3500)
            std = 0
            for i in range(len(true_weight)):
                std += ((data[i][2] - true_weight[i])**2)/len(true_weight)
            if std < LowestVariance:
                LowestVariance = std
                optimized_variables = adjusted_variables.copy()
            true_weight.clear()
            adjusted_calories.clear()
    Progress = (weight_factor - adj_weight_factor[0]) / (adj_weight_factor[-1] - adj_weight_factor[0]) * 100
    print(f"Progress: {Progress:.2f}%       ", end='\r')

print("Optimized Variables: ", [f"{v:.3g}" for v in optimized_variables])
print("Lowest Chi-Squared: ", f"{LowestVariance:.3g}")

# Calculate final true_weight using optimized variables
final_true_weight = []
adjusted_calories = []

for i in range(len(data)):
    adjusted_calories.append((data[i][0]
                            - optimized_variables[0]*data[i][2]
                            - optimized_variables[1]
                            - optimized_variables[2]*data[i][1]*data[i][2]))
    if len(final_true_weight) == 0:
        final_true_weight.append(starting_weight + adjusted_calories[i]/3500)
    else:
        final_true_weight.append(final_true_weight[len(final_true_weight)-1] + adjusted_calories[i]/3500)

# Create comparison plot
plt.figure(figsize=(12, 6))
days = range(1, len(data) + 1)

plt.plot(days, [row[2] for row in data], 'b-', label='Actual Weight', linewidth=2, marker='o', markersize=3)
plt.plot(days, final_true_weight, 'r--', label='Predicted Weight', linewidth=2, marker='s', markersize=3)

plt.xlabel('Day')
plt.ylabel('Weight (lbs)')
plt.title('Actual vs Predicted Weight Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Calculate and display fit statistics
actual_weights = [row[2] for row in data]
rmse = np.sqrt(np.mean((np.array(actual_weights) - np.array(final_true_weight))**2))
mae = np.mean(np.abs(np.array(actual_weights) - np.array(final_true_weight)))

plt.figtext(0.85, 0.75, f'RMSE: {rmse:.3f} lbs\nMAE: {mae:.3f} lbs\nVariance: {LowestVariance:.6f}', 
           fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))

plt.show()
            