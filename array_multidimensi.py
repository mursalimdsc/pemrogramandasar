
# Online Python - IDE, Editor, Compiler, Interpreter

from  array import *
sistem_array = array('i',[10,12,13])
array2       = array('i',[2,4,6])
print(sistem_array[0])
print(sistem_array[2])
print('-------------------------------------')
# insert
sistem_array.insert(1,60)

# perkalian
perkalian = sistem_array[0] * sistem_array[2]
print("Hasil Perkalian antara ", sistem_array[0], "dan", sistem_array[2], "adalah", perkalian)

print("-----------------------------------------")
for x in sistem_array:
    result = x**2
    print ("Bilangan awal ",x, "Hasil Perpangkatan",result)

# penjumlahan
print("-----------------------------------------")
for x in sistem_array:
    for n in array2:
        print (x, "+",n,"x",n,"=",(x+(n*n)))


