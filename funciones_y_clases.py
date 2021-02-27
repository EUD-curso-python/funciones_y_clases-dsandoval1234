import random
import datetime

global1 = 34

def cambiar_global(Var1):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1= Var1
    pass


def anio_bisiesto(anio):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    if anio % 4 != 0: 
      return False
    elif anio % 4 == 0 and anio % 100 != 0: 
      return True
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: 
      return False
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: 
      return True

    pass

def contar_valles(ListaInput):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    ContValles=0
    for i, elemento in enumerate(ListaInput):
      if i==0:
        continue
      else:
        if ListaInput[i]==1 and ListaInput[i-1]==-1:
          ContValles=ContValles+1
        if ListaInput[i]==1 and ListaInput[i-1]==0:
            x=i-1
            while x != 0:
              if ListaInput[x]==-1:
                ContValles=ContValles+1
                break
              elif ListaInput[x]==1:
                break
              else:
                x=x-1
    return ContValles

    pass

def saltando_rocas(ListaInput):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    ContJumps=0
    Posicion=0
    
    while Posicion < len(ListaInput)-2:

      if ListaInput[Posicion+2]==0:
        Posicion=Posicion+2
        ContJumps=ContJumps+1
      else:
        Posicion=Posicion+1
        ContJumps=ContJumps+1

    if Posicion == len(ListaInput)-2:
      ContJumps=ContJumps+1
    return ContJumps

    pass

def pares_medias(ListaInput):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    sacar medias que no tengan par del dic
    '''
    Position=0
    PrimerMedia=0
    SegundaMedia=0
    Tamanio=len(ListaInput)
    Verificar=False
    Diccionar={}
    Key=0
    

    while Tamanio != 0:
      Verificar=False
      PrimerMedia=ListaInput[Position]

      for i, elemento in enumerate(ListaInput):
        if i==0:
          continue
        if ListaInput[i]==PrimerMedia:
          SegundaMedia = i
          Verificar=True
          break
        
      if Verificar==True:
        Aux = ListaInput.pop(SegundaMedia)
        Aux = ListaInput.pop(Position)
        Key=Diccionar.get(PrimerMedia, 0)
        Key=Key+1
        Diccionar[PrimerMedia] = Key
      else:
        Aux = ListaInput.pop(Position)
      
      Tamanio=len(ListaInput)
    
    return Diccionar

    pass


# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'
class ListaComa:
  
  def __init__(self,ListaInput):
    self.Aux=""
    for el in ListaInput:
      self.Aux= self.Aux + "," + str(el)

  def __str__(self):
    return self.Aux[1:]


# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'

class Persona:
  
  def __init__(self,ListaNombres,ListaApellidos):
    self.NombreCompleto=""
    self.nombres=ListaNombres
    self.apellidos=ListaApellidos


    for i, elemento in enumerate(self.nombres):
      self.nombres[i]= str(self.nombres[i])
      self.nombres[i]= self.nombres[i].capitalize() 
    
    for i, elemento in enumerate(self.apellidos):
      self.apellidos[i]= str(self.apellidos[i])
      self.apellidos[i]= self.apellidos[i].capitalize() 

  def nombre_completo(self):
    for el in self.nombres:
      self.NombreCompleto=self.NombreCompleto + " " + el

    for el in self.apellidos:
      self.NombreCompleto=self.NombreCompleto + " " + el
    
    self.NombreCompleto=self.NombreCompleto.strip()
    return self.NombreCompleto

# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.

class Persona1(Persona):
  
  def __init__(self,ListaNombres,ListaApellidos,FecNacimiento):
    Persona.__init__(self,ListaNombres,ListaApellidos)
    self.ANacimiento=FecNacimiento.year
    self.MNacimiento=FecNacimiento.month
    self.DNacimiento=FecNacimiento.day
    self.DiferenciaEdad = int(datetime.date.today().year) - int(self.ANacimiento)

  def edad(self):
    if self.MNacimiento < datetime.date.today().month:
      self.DiferenciaEdad=self.DiferenciaEdad-1
    elif self.MNacimiento == datetime.date.today().month:
      if self.DNacimiento < datetime.date.today().day:
        self.DiferenciaEdad=self.DiferenciaEdad-1
  
    return self.DiferenciaEdad

Jose=Persona1(['Juan', 'David'], ['Torres', 'Salazar'],datetime.date(1985, 2, 27))
x=int(Jose.edad())
print(x)
