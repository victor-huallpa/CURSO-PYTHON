import re
le = 'hola como estas'

le[-5]
print(le[-5])#seleccionamos el muneor de inidici del string o cadena de nuestro texto para imprimir
print(le[-1])

print(le[0:4])#seleccionamos de donde a donde queremos imprimir nuestra cadena o string mediante el indice

a=le.replace('hola','hello')
print(a)
b=a.find('o')# funcion find es para saber en donde empieza la cadena de acuerdo al indice
print(b)

num = "0123456789"
print(num[::2])


s1='estoy en las nuves'
ss1=r'en las'

resul=re.search(ss1, s1)

print (resul)

if resul:
    print('si funciona')
else:
    print('salio mal')
    
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
    
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

name = 'Lizz'
print(name[0:2])

print('1'+'2')