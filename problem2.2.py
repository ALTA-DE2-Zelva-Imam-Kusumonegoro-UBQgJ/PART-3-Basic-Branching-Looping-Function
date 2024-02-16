# Meminta nominal
bilangan = int(input("Tolong isi nominal: "))

# Menurun jadi setiap loop dikurang 1 dari bilangan sampai 1
for x in range(bilangan, 0, -1):
    if bilangan % x == 0:
        print(x)
