def is_safe(array_line):
      # Check if the sequence is strictly increasing or decreasing
        increasing = all(array_line[i] < array_line[i + 1] for i in range(len(array_line) - 1))
        decreasing = all(array_line[i] > array_line[i + 1] for i in range(len(array_line) - 1))
        
        # Check if the differences between consecutive elements are between 1 and 3
        valid_diff = all(0 < abs(array_line[i] - array_line[i + 1]) < 4  for i in range(len(array_line) - 1))

        return (increasing or decreasing) and valid_diff

def solution_part2(input_file):
    safe_reports = 0

    # Process each line in the input file
    for line in input_file:
        str_array = line.split()
        array_line = list(map(int, str_array))

        # If the array is not safe, try removing each element one at a time
        if is_safe(array_line):
            safe_reports += 1
        else: 
            for i in range(len(array_line)):
                if is_safe(array_line[:i] + array_line[i + 1:]):
                     safe_reports += 1
                     break
    
    return safe_reports