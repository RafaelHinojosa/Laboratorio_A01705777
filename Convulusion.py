# Rafael Hinojosa López
# 05 - 05 - 2021
# Convulusion - Versión 1

# Valores de prueba
# Mat = [[10, 4, 50, 30, 20],
#         [80, 0, 0, 0, 6],
#         [0, 0, 1, 16, 17],
#         [0, 1, 0, 7, 23],
#         [1, 0, 6, 0, 4]]

# Ker = [[1, 0, 1],
#         [0, 0, 0],
#         [1, 0, 3]]


rowMat = int(input('Ingresa el número de filas de la matriz: '));
colMat = int(input('Ingresa el número de columnas de la matriz: '));

rowKer = int(input('Ingresa el número de filas del kernel: '));
colKer = int(input('Ingresa el número de columnas del kernel: '));

Mat = []
Ker = []
Output = []

# Llenar Matriz
print('Llenar Matriz');
for i in range(0, rowMat): 
    print('Fila ' + str(i));
    Mat.append([]);
    for j in range(0, colMat):
        num = int(input());
        Mat[i].append(num);

# Llenar Kernel
print('Llenar Kernel');
for i in range(0, rowKer):
    print('Fila ' + str(i));
    Ker.append([]);
    for j in range(0, colKer):
        num = int(input());
        Ker[i].append(num);

print('Matriz: ' + str(Mat))
print('Kernel: ' + str(Ker))


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

print('Output' + str(Output))