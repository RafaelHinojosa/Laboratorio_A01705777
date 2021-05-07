# Rafael Hinojosa López
# 05 - 05 - 2021
# Convulusion - Versión 1

import numpy as np

# Matrices
Ker = []
Output = []

# Llenar Matriz
rowMat = int(input('Ingresa el número de filas de la matriz: '));
colMat = int(input('Ingresa el número de columnas de la matriz: '));
padding = int(input('Ingresa el valor para padding: '))

# Matriz de 0s con padding
Mat = np.zeros([(rowMat + (2 * padding)), (colMat + (2 * padding))]);
print(Mat)
print('Llenar Matriz');
for i in range(0, rowMat): 
    print('Fila ' + str(i));
    Mat.append([]);
    for j in range(0, colMat):
        num = int(input());
        Mat[i].append(num);

# Llenar Kernel
rowKer = int(input('Ingresa el número de filas del kernel: '));
colKer = int(input('Ingresa el número de columnas del kernel: '));

print('Llenar Kernel');
for i in range(0, rowKer):
    print('Fila ' + str(i));
    Ker.append([]);
    for j in range(0, colKer):
        num = int(input());
        Ker[i].append(num);

print('Matriz: ' + str(Mat))
print('Kernel: ' + str(Ker))


# Convulsion
# Iterar Matriz
for i in range(0, (rowMat - rowKer + 1)):
    Output.append([]);
    for j in range(0, (colMat - colKer + 1)):
        producto = 0; 
        # Iterar Kernel
        for ik in range(0, rowKer):
            for jk in range(0, colKer): 
                producto += Ker[ik][jk] * Mat[i + ik][j + jk];
        Output[i].append(producto);

# Resultado
print('Output' + str(Output))

# Checar ranges en Convolusion... 
# Hacer matriz np zeroes para imagen y esa sera la padded image...