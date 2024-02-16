# Meminta nominal
number = int(input("Tolong isi nominal: "))

# mencari prima
def prime_number(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True


print(prime_number(number))
