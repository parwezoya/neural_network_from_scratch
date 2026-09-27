input = [1,2,3]
weights = [
    [0.2, 0.8, -0.5],
    [0.5, -0.91, 0.26],
    [-0.26, -0.27, 0.17]
]
bias = [2,3,4]
initial_total = 0
final_result = []
for i in range(len(weights)):
    initial_total = 0
    for j in range(len(input)):
     initial_total += input[j] * weights[i][j]
            
    final_total = initial_total + bias[i]
    final_result.append(final_total)

print(final_result)