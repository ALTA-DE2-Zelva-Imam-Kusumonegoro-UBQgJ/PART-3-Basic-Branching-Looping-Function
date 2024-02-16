# Meminta kata atau frasa
hasil = input("Tolong isi kata atau frasa: ")

def palidrome(kata):
    # Menghapus spasi dan mengubah string menjadi huruf kecil agar tidak sensitive terhadap huruf besar/kecil
    kata = kata.replace(" ", "").lower()
    
    return kata == kata[::-1]

if palidrome(hasil):
    print("True")
else:
    print("False")
