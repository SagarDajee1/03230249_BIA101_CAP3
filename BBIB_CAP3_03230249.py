################################
# Github Repo link : https://github.com/SagarDajee1/03230249_BIA101_CAP3
# Your Name : Sagar Darjee
# Your Section : BBI "B"
# Your Student ID Number: 03230249
################################
# SOLUTION
# Your Solution Score: 489006
################################
def extract_and_sum(filename):
    total_sum = 0
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            first_digit = ''
            last_digit = ''
            
            # Find the first digit
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            
            # Find the last digit
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            
            if first_digit and last_digit:
                two_digit_number = int(first_digit + last_digit)
                total_sum += two_digit_number
                print(f"Line: {line}, Number: {two_digit_number}")
    
    print(f"The sum of the two-digit numbers is: {total_sum}")




filename = '249.txt' # replace with ur file name
extract_and_sum(filename)