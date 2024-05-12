def persegiPanjang(panjang, lebar): # Function Header
    countLuasPersegipanjang = panjang * lebar # Function body
    return countLuasPersegipanjang # Function Return


countPersegiPanjang1 = persegiPanjang(8,2)
print(countPersegiPanjang1)

# TODO
#Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
# Menerima dua buah argumen berupa number, yaitu a dan b.
# Mengembalikan nilai terkecil antara a atau b.
# Bila nilai keduanya sama, kembalikan dengan nilai a.

def minimal(a,b):
  return min(a,b)

print(minimal(6,4))