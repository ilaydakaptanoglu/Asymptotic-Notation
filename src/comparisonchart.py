import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Shellsort implementasyonu
def shellsort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Test için veri boyutları
sizes = [100, 500, 1000, 5000, 10000, 25000, 50000]
shellsort_times = []
timsort_times = []

print("Algoritma Karşılaştırması Başlıyor...")

for size in sizes:
    # Rastgele veri oluştur
    data = [random.randint(1, 100000) for _ in range(size)]
    
    # Shellsort zaman ölçümü
    data_copy = data.copy()
    start_time = time.time()
    shellsort(data_copy)
    shellsort_time = time.time() - start_time
    shellsort_times.append(shellsort_time)
    
    # Timsort zaman ölçümü (Python'un built-in sort'u)
    data_copy = data.copy()
    start_time = time.time()
    data_copy.sort()  # Bu Timsort kullanır
    timsort_time = time.time() - start_time
    timsort_times.append(timsort_time)
    
    print(f"Boyut: {size:6d} | Shellsort: {shellsort_time:.4f}s | Timsort: {timsort_time:.4f}s")

# Grafik çizimi
plt.figure(figsize=(12, 8))

# Zaman karşılaştırması
plt.subplot(2, 1, 1)
plt.plot(sizes, shellsort_times, 'bo-', label='Shellsort', linewidth=2, markersize=6)
plt.plot(sizes, timsort_times, 'ro-', label='Timsort', linewidth=2, markersize=6)
plt.xlabel('Dizi Boyutu')
plt.ylabel('Zaman (saniye)')
plt.title('Shellsort vs Timsort - Zaman Karşılaştırması')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xscale('log')

# Log ölçekli grafik
plt.subplot(2, 1, 2)
plt.loglog(sizes, shellsort_times, 'bo-', label='Shellsort', linewidth=2, markersize=6)
plt.loglog(sizes, timsort_times, 'ro-', label='Timsort', linewidth=2, markersize=6)
plt.xlabel('Dizi Boyutu (log)')
plt.ylabel('Zaman (saniye, log)')
plt.title('Shellsort vs Timsort - Log Ölçekli Karşılaştırma')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Performans oranı grafiği
plt.figure(figsize=(10, 6))
performance_ratio = [shellsort_times[i] / timsort_times[i] for i in range(len(sizes))]

plt.bar(range(len(sizes)), performance_ratio, color='orange', alpha=0.7)
plt.axhline(y=1, color='red', linestyle='--', label='Eşit Performans')
plt.xlabel('Dizi Boyutu İndeksi')
plt.ylabel('Shellsort Zamanı / Timsort Zamanı')
plt.title('Shellsort ve Timsort Performans Oranı')
plt.xticks(range(len(sizes)), [f'{size}' for size in sizes], rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

# Oran değerlerini yazdır
for i, ratio in enumerate(performance_ratio):
    plt.text(i, ratio + 0.05, f'{ratio:.1f}x', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Sonuç özeti
print("\n" + "="*50)
print("SONUÇ ÖZETİ")
print("="*50)
for i, size in enumerate(sizes):
    ratio = performance_ratio[i]
    faster = "Timsort" if ratio > 1 else "Shellsort"
    print(f"Boyut {size:6d}: Timsort {ratio:.1f} kat daha hızlı" if ratio > 1 
          else f"Boyut {size:6d}: Shellsort {1/ratio:.1f} kat daha hızlı")