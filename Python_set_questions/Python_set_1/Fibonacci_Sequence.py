def generate_fibonacci(n):
    fibonacci_list = []  # Step 1
    a, b = 0, 1  # Step 2

    for _ in range(n):  # Step 3
        fibonacci_list.append(a)  # Step 3a
        a, b = b, a + b  # Step 3b and 3c

    return fibonacci_list

# Test the function
n = 10
fibonacci_sequence = generate_fibonacci(n)
print(fibonacci_sequence)
