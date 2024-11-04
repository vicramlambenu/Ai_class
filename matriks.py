import numpy as np

# Matriks A ukuran 2x3
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Matriks B ukuran 3x4
B = np.array([[7, 8, 9, 10],
              [11, 12, 13, 14],
              [15, 16, 17, 18]])

# Mengalikan Matriks A dan B untuk mendapatkan Matriks C (2x4)
C = np.dot(A, B)

# Menampilkan Matriks A, B, dan hasil perkalian C
print("Matriks A:")
print(A)

print("\nMatriks B:")
print(B)

print("\nHasil perkalian Matriks A dan B (Matriks C):")
print(C)
