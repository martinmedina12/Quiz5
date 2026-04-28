class Jugador:
  def __init__(self, nombre, simbolo):
    self.nombre=nombre
    self.simbolo=simbolo
  def jugada (self,pos):
    self.pos=pos
    self.tablero={1:"_1_",2:"_2_",3:"_3_",4:"_4_",5:"_5_",6:"_6_",7:"_7_",8:"_8_",9:"_9_"}
    if self.pos==1:
      self.tablero [1]=self.simbolo
    if self.pos==2:
      self.tablero [2]=self.simbolo
    if self.pos==3:
      self.tablero [3]=self.simbolo
    if self.pos==4:
      self.tablero [4]=self.simbolo
    if self.pos==5:
      self.tablero [5]=self.simbolo
    if self.pos==6:
      self.tablero [6]=self.simbolo
    if self.pos==7:
      self.tablero [7]=self.simbolo
    if self.pos==8:
      self.tablero [8]=self.simbolo
    if self.pos==9:
      self.tablero [9]=self.simbolo
    return self.tablero
n1=input("Jugador 1: Ingrese su nombre: ")
s1=input("Ingrese su simbolo (X, O): ")
n2=input("Jugador 2:Ingrese su nombre: ")
s2=input("Ingrese su simbolo (X, O): ")
tablero={1:"_1_",2:"_2_",3:"_3_",4:"_4_",5:"_5_",6:"_6_",7:"_7_",8:"_8_",9:"_9_"}
print(print(f"{tablero[1]}|{tablero[2]}|{tablero[3]}|\n{tablero[4]}|{tablero[5]}|{tablero[6]}|\n{tablero[7]}|{tablero[8]}|{tablero[9]}"))
p1=int(input("Jugador 1: Ingrese su jugada: "))
p1=Jugador(n1,s1)
p1.jugada(p1)
p2=int(input("Jugador 2: Ingrese su jugada: "))
p2=Jugador(n2,s2)
p2.jugada(p2)
