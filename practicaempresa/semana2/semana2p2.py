import numpy as np
#vectores
v1= np.array([2,3]) 
v2= np.array([1,4])
#suma de vectores
suma=v1+v2
print("suma de los vectores: ",suma)
escalar=3 
v3=escalar * v1
print("vector multiplicado por escalar: ",v3)
A=np.array([[1,2],
            [3,4]])
B=np.array([[5,6],
            [7,8]])
producto=np.dot(A, B)
print(f"producto de matris:{producto}")
A_transpuesta = A.T
print(f"transpocion de A:\n {A_transpuesta}")
determinante = np.linalg.det(A)
print(f"determinante de A: {determinante}")
valores_propios, vectores_propios=np.linalg.eig(A)
print(f"valores propios: {valores_propios}")
print(f"vectores_propios:\n {vectores_propios}")

