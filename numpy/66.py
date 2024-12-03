import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

# Sort the array
sorted_arr = np.sort(arr)

# Use a for loop to format the output with commas
output = ""
for i in range(len(sorted_arr)):
    output += sorted_arr[i]
    if i != len(sorted_arr) - 1:  # Add a comma except for the last element
        output += ", "

print(output)