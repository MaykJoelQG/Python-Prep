class Herramienta:
   
    # ---------- Metodo Constructor -----------
    def __init__(self,lista):
        self.lista = lista
   
    # ---------- Funcion Primos -----------
    def lista_numeros_primos(self):
        lista_nueva = []
        for g in lista:
            primo=True
            for i in range(2,g):
                if g%i==0:
                    primo=False
            #return primo
            
            if primo == True:
                lista_nueva.append(g)
        return print(lista_nueva)
    
    # ---------- Funcion Valor Modal -----------
    def contar(self): #creando la funcion
        result = {} # creamos un diccionario donde pondremos los valores sin repetir y la mcantidad de veces se repite
        for i in lista: #analizamos todos los elementos de la lista
            if i not in result: #se an aliza cada elemento del diccionario, si esta o no esta dentro
                result[i] = 0    # Si "NO" está, se agrega al diccionario el valor como clave y su numero de repeticiones como valor (e,h)
            result[i] += 1      # si ya está en el diccionario, se sumara a su valor +1 que es el numero de repeticiones que se encuentran en la lista dada
        #print(result.keys()) # Imprimimos las claves del diccionario, lo cuales son los elelentos de la lista dada sin repeticiones
        
        #leyendo las claves y valores del diccionario
        n = 0 # creamos un variable para almacenar el mayor de los valores
        m = 0 # Creamos una variable donde almacenaremos la clave del mayor valor
        for e, h in result.items(): # Hacemos un for para analizar todas las claves y valores del diccionario
            if h > n: # una condicional para decir si n es mayor al item valor analizaro entonces no me combien n
                n = h # Cambiando n si y solo si h es mayor
                m = e # cambiando m con el key e si y solo si n es mayor que h

        print('El numero',m,'es el numero que mas se ha repetido, repitiendose',n,'veces') #imprimimos el numero que se repitio mas
   
    # ---------- Funcion Termometro -----------
    def termometro(self, grados_origen, grados_destino):
        grados_origen = grados_origen.upper()
        grados_destino = grados_destino.upper()
        for valor in lista:
            if grados_origen == grados_destino:
                print(valor)
            elif grados_origen == 'C' and grados_destino == 'F':
                print(float(valor),'°C Celsius es igual a',(valor*9/5)+32,'°F grados FarenHeith')#
            elif grados_origen == 'C' and grados_destino == 'K':
                print(float(valor),'°C Celsius es igual a',(valor+273.15),'°K grados Kelvin')#
            elif grados_origen == 'K' and grados_destino == 'C':
                print(float(valor), '°K Kelvin es igual a',(valor-273.15),'°C grados Celsius')#
            elif grados_origen == 'K' and grados_destino == 'F':
                print(float(valor), '°K Kelvin es igual a',((valor-273.15)*9/5)+32,'°F grados FarenHeith')#
            elif grados_origen == 'F' and grados_destino == 'C':
                print(float(valor), '°F FarenHeith es igual a',(valor-32)*5/9,'°C grados Celsius')#
            elif grados_origen == 'F' and grados_destino == 'K':
                print(float(valor), '°F FarenHeith es igual a',((valor-32)*5/9)+273.15,'°K grados Kelvin')
    
    # ---------- Funcion  Factorial -----------
    def factoriale(self):
        for num in lista:
            if (type(num) != int):
                print('Verifica el numero que pusiste, solo se admiten enteros')
            elif num < 0:
                print('Pusiste un numero negativo, solo se admiten enteros')    
            elif num <= 1:
                print(1)
            else:        
                # Realizando el Factorial
                n=1
                for i in range(num):
                    n*=(i+1)
                print(n)