# Fibonacci Sequence Generator
# Daily coding practice - September 9, 2025

def fibonacci(n):
      """
          Generate fibonacci sequence up to n terms
              """
      if n <= 0:
                return []
elif n == 1:
        return [0]
elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
              next_num = sequence[i-1] + sequence[i-2]
              sequence.append(next_num)

    return sequence

def print_fibonacci(n):
      """
          Print fibonacci sequence in a formatted way
              """
      fib_sequence = fibonacci(n)
      print(f"Fibonacci sequence with {n} terms:")
      print(fib_sequence)

    # Print each number with its position
      for i, num in enumerate(fib_sequence):
                print(f"F({i}) = {num}")

  if __name__ == "__main__":
        # Test the fibonacci function
        terms = 10
        print_fibonacci(terms)

    # Calculate and display the golden ratio approximation
        if terms > 1:
                  fib_seq = fibonacci(terms)
                  golden_ratio = fib_seq[-1] / fib_seq[-2]
                  print(f"\nGolden ratio approximation: {golden_ratio:.6f}")
