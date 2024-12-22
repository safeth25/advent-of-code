# Open input file in read mode
with open("2024/day01/input.txt") as input_file:
    # Initialize two empty lists to store numbers from the two columns
    array_of_int1 = []
    array_of_int2 = []

    for line in input_file:
        # Split line into two values separated by whitespace
        nums = line.split()

        # Append the first value to the first list and second value to the second list as integers
        array_of_int1.append(int(nums[0]))
        array_of_int2.append(int(nums[1]))

# Sort both lists in ascending order
array_of_int1.sort()
array_of_int2.sort()

total_sum = 0

# Compute the absolute distances and add it to the sum
for i in range(len(array_of_int1)):
    total_sum += abs(array_of_int1[i] - array_of_int2[i])

print("Solution part 1: ", total_sum)


mul_total_sum = 0

for i in range(len(array_of_int1)):
    number = array_of_int1[i]
    count = array_of_int2.count(number)
    mul_total_sum += number * count

print("Solution part 2: ", mul_total_sum)