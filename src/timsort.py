RUN = 32

def insertionSort(arr, left, right):
    """
    Belirtilen aralıkta Ekleme Sıralaması uygular.
    TimSort, küçük dizileri sıralamak için Ekleme Sıralaması kullanır.
    """
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def merge(arr, l, m, r):
    """
    arr[l...m] ve arr[m+1...r] iki sıralı alt diziyi birleştirir.
    """
    # Sol ve sağ alt dizilerin boyutlarını hesapla
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l  # Başlangıç indeksleri

    # İki alt diziyi birleştir
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Kalan sol elemanları kopyala
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Kalan sağ elemanları kopyala
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timSort(arr):
    n = len(arr)
    
    # 1. Adım: Çalışmaları (Run) belirle ve Ekleme Sıralaması ile sırala
    for i in range(0, n, RUN):
        insertionSort(arr, i, min((i + RUN - 1), n - 1))

    # 2. Adım: Çalışmaları birleştir (Merge)
    size = RUN
    while size < n:
        # Alt diziyi arr[left...left+2*size-1] birleştir
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            # m sağ tarafta kalmayacaksa birleştir
            if mid < right:
                merge(arr, left, mid, right)
        
        size = 2 * size

# Örnek kullanım
data = [5, 21, 7, 23, 19, 45, 12, 9, 3, 15, 2]
print("Orijinal dizi:", data)

timSort(data)

print("TimSort ile sıralanmış dizi:", data)