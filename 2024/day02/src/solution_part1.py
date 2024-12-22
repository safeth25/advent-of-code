
def solution_part1(input_file):
    safe_reports = 0

    # Process each line in the input file
    for line in input_file:
        str_array = line.split()
        array_line = list(map(int, str_array))

        # Check if the sequence is strictly increasing or decreasing
        increasing = all(array_line[i] < array_line[i + 1] for i in range(len(array_line) - 1))
        decreasing = all(array_line[i] > array_line[i + 1] for i in range(len(array_line) - 1))
        
        # Check if the differences between consecutive elements are between 1 and 3
        valid_diff = all(0 < abs(array_line[i] - array_line[i + 1]) < 4  for i in range(len(array_line) - 1))

        # If the sequence is either strictly increasing or decreasing and all differences are valid, mark it as safe
        if (increasing or decreasing) and valid_diff:
            safe_reports += 1
    
    return safe_reports