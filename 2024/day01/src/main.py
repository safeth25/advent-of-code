with open("../input.txt") as input_file:
    array_of_int1 = []
    array_of_int2 = []

    for line in input_file:
        nums = line.split()

        array_of_int1.append(int(nums[0]))
        array_of_int2.append(int(nums[1]))

array_of_int1.sort()
array_of_int2.sort()

total_sum = 0

for i in range(len(array_of_int1)):
    total_sum += abs(array_of_int1[i] - array_of_int2[i])

print(total_sum)