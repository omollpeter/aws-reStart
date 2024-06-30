"""
This scripts find prime numbers in a certain range and store the result
to a file
"""


import sys


def prime_numbers(start, end):
    """
    Finds all prime numbers between start and end
    """
    primes = []
    try:
        start = int(start)
        end = int(end)
        if start >= end:
            raise ValueError("Start should be less than end at all times")
        if start < 2:
            start = 2
        for j in range(start, end + 1):
            divisor = 2
            while divisor <= j // 2:
                if j % divisor == 0:
                    break
                divisor += 1
            else:
                primes.append(j)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print("The values for start and end should be int or float")
        sys.exit(1)
    return primes

def write_prime_numbers_to_file(prime_numbers_list, filename, start, end):
    with open(filename, "w") as file:
        file.write(f"Prime numbers between {start} and {end}\n")
        total = len(prime_numbers_list)
        for number in prime_numbers_list:
            file.write(f"{number}\n")
        file.write("Total => {}".format(total))

def find_and_store_primes(start, end, filename):
    prime_numbers_list = prime_numbers(start, end)
    write_prime_numbers_to_file(prime_numbers_list, filename, start, end)

if __name__ == "__main__":
    find_and_store_primes(1, 250, "results.txt")
