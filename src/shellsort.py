def shellSort(arr):
    n = len(arr)
    
    # 1. Başlangıç aralığını (gap) belirle
    gap = n // 2
    
    # Aralık 0'dan büyük olduğu sürece döngüye devam et
    while gap > 0:
        
        # 2. Her aralık için 'aralıklı ekleme sıralaması' (gapped insertion sort) yap
        for i in range(gap, n):
            
            # Geçerli elemanı kaydet
            temp = arr[i]
            
            # 'j', temp'in doğru konumunu bulana kadar geriye doğru tarama yapar
            j = i
            
            # 'gap' mesafesindeki elemanları karşılaştır ve kaydır
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Geçerli elemanı (temp) doğru konumuna yerleştir
            arr[j] = temp
            
        # 3. Bir sonraki aşama için aralığı küçült
        gap //= 2

    return arr

# ----------------------------------------------
# Örnek 1: Rastgele Sayı Dizisi
# ----------------------------------------------
veri_1 = [12, 34, 54, 2, 3, 10, 88, 1, 7]
print("Örnek 1 - Sıralanmamış Dizi:", veri_1)

shellSort(veri_1)
print("Örnek 1 - Shell Sort ile Sıralanmış Dizi:", veri_1)
# Çıktı: [1, 2, 3, 7, 10, 12, 34, 54, 88]

# ----------------------------------------------
# Örnek 2: Ters Sıralı Dizi (En Kötü Durum Senaryosuna Yakın)
# ----------------------------------------------
veri_2 = [100, 80, 60, 40, 20, 0]
print("\nÖrnek 2 - Sıralanmamış Dizi:", veri_2)

shellSort(veri_2)
print("Örnek 2 - Shell Sort ile Sıralanmış Dizi:", veri_2)
# Çıktı: [0, 20, 40, 60, 80, 100]

# ----------------------------------------------
# Örnek 3: Küçük Dizi ve Negatif Sayılar
# ----------------------------------------------
veri_3 = [-5, 15, -1, 0, 10]
print("\nÖrnek 3 - Sıralanmamış Dizi:", veri_3)

shellSort(veri_3)
print("Örnek 3 - Shell Sort ile Sıralanmış Dizi:", veri_3)
# Çıktı: [-5, -1, 0, 10, 15]