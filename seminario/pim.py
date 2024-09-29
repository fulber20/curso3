lista=[[4,5,7,5,7]
]
contador = 0
for i in lista:
    for numero in i :
        if numero ==7:
            contador +=1
if contador==2:
    print(True)
else:
    print(False)
