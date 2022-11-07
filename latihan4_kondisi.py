# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:20:26 2022

@author: salim
"""
#inputan varibel

nama  = input("Masukkan Nama Lengkap: ")
prodi = input("Masukkan Program Studi: ")

nilai = int(input("Masukkan Nilai: "))

if(nilai) >=90:
    print ("Grade A")
else:
    print("Grade B")
    
def pekalian(a,b):
    nilai_a = a
    nilai_b = b
    
    hitung_perkalian = nilai_a*nilai_b
    
    return hitung_perkalian