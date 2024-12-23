import re

def solution_part1(input_file):
        text = input_file.read()

        # Define the regex
        substring = r"mul\((\d{1,3}),(\d{1,3})\)"

        found = re.findall(substring, text)

        # Convert the found string tuples into integer tuple
        int_tuples = [(int(a), int(b)) for a, b in found]
        answer = 0
        # For each tuple (a, b), multiply 'a' and 'b', then add the result to 'answer'
        for a,b in int_tuples:
                answer += a * b 

        print(answer)