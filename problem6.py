# Meminta nominal
number = int(input("Tolong isi nominal: "))

# Fungsi untuk memeriksa apakah suatu bilangan adalah prima
def prime_number(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

# Fungsi untuk memeriksa apakah suatu bilangan adalah Full Prima
def full_prime(number):
    num_digits = len(str(number))
    
    # Periksa setiap digit untuk memastikan bahwa semuanya adalah bilangan prima
    for _ in range(num_digits):
        digit = number % 10
        if not prime_number(digit):
            return False
        number //= 10
    return True

# Cek apakah bilangan yang dimasukkan adalah Full Prima atau bukan
if full_prime(number):
    print("True")
else:
    print("False")
