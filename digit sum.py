def calculate_digit_sum(num):
        total = 0
        while num > 0:
            total += num % 10  # Extract the last digit and add to total
            num //= 10  # Remove the last digit
        return total
        
print(calculate_digit_sum(51))
