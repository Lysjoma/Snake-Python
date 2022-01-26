import turtle #Modulo que permite la creación del objeto y la ventana.
import time #Modulo que permite importar las librerias que nos dejan manipular el tiempo de ejecución.
import random #Modulo que permite importar las librerias de la clase Random
from tkinter import * #Modulo para poder importar las librerías que permiten desactivar boton maximizar

posponer = 0.1#Constante que nos permite posponer la ejecución, en este caso una milesima de segundo

#Marcador
score = 0 #Puntaje por partida.
highScore = 0 #Mayor puntaje alcanzado en todos los juegos o partidas.

#Configuración de la ventana
vent = turtle.Screen()#Crea una ventana de visualización 
vent.title("Juego de Snake") #Se le asigna un titulo a la ventana
vent.bgcolor("light blue") #Se le asigna un color al fondo (Background)
vent.setup(width=600, height=600) #Se le asigna el tamaño a la ventana en pixeles
vent.tracer(0) #Mejora la calidad de las animaciones
vent.cv._rootwindow.resizable(False, False)#Comando para desactivar boton de maximizar ventana

#Configuración de la cabeza de la serpiente
cabeza = turtle.Turtle() #Creación del objeto que se va a mover(Serpiente)
cabeza.speed(0) #Velocidad de movimiento del objeto cread(Serpiente)
cabeza.shape("square")#Forma de la parte frontal del objeto creado(Cabeza de la serpiente)
cabeza.color("red")#Le da el color al objeto
cabeza.penup()#Comando para que cuando el objeto se mueva no deje un rastro
cabeza.goto(0,0)#Comando para posicionar el objeto. El movimiento se asimila al plano cartesiano, 0,0 es la mitad(x,y).
cabeza.direction = "stop"#Comando para darle dirección al objeto, stop no se mueve, y el resto, le da dirección

#Configuración de la comida de la serpiente
comida = turtle.Turtle() #Creación del objeto (comida)
comida.speed(0) #Velocidad de movimiento del objeto cread(Serpiente)
comida.shape("circle")#Forma del objeto
comida.color("Orange")#Le da color al objeto
comida.penup()#Comando para que cuando el objeto se mueva no deje un rastro
comida.goto(0,100)#Comando para posicionar el objeto.

#Cuerpo de la serpiente
segmentos =[]#lista donde se almacenan los segmentos de la serpiente

#creación del contenido
texto = turtle.Turtle()#Creación de objeto
texto.speed(0)#Velocidad en la que el texto aparece en la pantalla
texto.color("red")#Color de texto
texto.penup()#Esconder rastro
texto.hideturtle()#Esconder la plumilla con la que se escribe el texto
texto.goto(0,260)#Que aparezca el texto en esas coordenadas.
texto.write("Score: 0       High Score: 0",align= "center", font=("Comic Sans MS",24,"bold"))#Texto que comprende contenido, alineación, fuente, tamaño, y tipo(Negrilla, cursiva, subrayado)

#creación del contenido
texto2 = turtle.Turtle()#Creación de objeto
texto2.speed(0)#Velocidad en la que el texto2 aparece en la pantalla
texto2.color("red")#Color de texto2
texto2.penup()#Esconder rastro
texto2.hideturtle()#Esconder la plumilla con la que se escribe el texto2
texto2.goto(0,245)#Que aparezca el texto2 en esas coordenadas.
texto2.write("__" *len("Score: 0       High Score: 0"), align="center",font=("snap Itc",24,"bold"))
#Funciones
def arriba(): 
    if cabeza.direction == "down":#Validaciones para que la serpiente no pueda pasar sobre ella misma
        cabeza.direction = "down"
    else:
        cabeza.direction = "up"   
def abajo():
    if cabeza.direction == "up":
        cabeza.direction == "up"
    else:
        cabeza.direction = "down"  #Funciones para controlar el movimiento de la serpiente
def derecha():
    if cabeza.direction == "left":
        cabeza.direction == "left"
    else:
        cabeza.direction = "right"
def izquierda():
    if cabeza.direction == "right":
        cabeza.direction == "right"
    else:
        cabeza.direction = "left"

#Teclado
vent.listen()#Comando para que el aplicativo ponga atención en cuanto a las acciones del teclado
vent.onkeypress(arriba,"Up") 
vent.onkeypress(abajo,"Down")#Estos comandos permiten que al presionar una tecla en especifico, se produzca una funcion.
vent.onkeypress(derecha,"Right")
vent.onkeypress(izquierda,"Left")

#Funciones
def movimiento(): #Funcion para el movimiento de la serpiente
    if cabeza.direction == "up": #Condición para darle dirección a la serpiente
        y = cabeza.ycor()#Con este comando le puedo sacar la coordenada Y a la posición de la serpiente
        cabeza.sety(y+20)#Con sety, mas el valor, declaramos que el objeto se va a mover de a 20 pixeles hacia(arriba).
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "right":
        x = cabeza.xcor()#Se saca la coordenada x, es decir, la horizontal
        cabeza.setx(x+20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)

#Cliclo principal
while True: #En todos los juegos la recomendación es tener bucle, ya que hasta que no demos instrucciones, no finaliza.
    vent.update()#Comando para actualizar la ventana, cada vez que se haga una funcion

    #Perder por tocar una pared
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 250 or cabeza.ycor() < -280: #Se verifica que la cabeza de la serpiente no este tocando una pared.
        time.sleep(1)#Se le da una pausa al juego.
        cabeza.goto(0,0)#Se ubica la serpiente de nuevo en el lugar inicial
        cabeza.direction = "stop" #Se mantiene quieta, hasta que se le de una dirección a la serpiente.

        #Esconder los segmentos.
        for segmento in segmentos:
            segmento.goto(2000,2000)

        #Limpiar lista de segmentos
        segmentos.clear()
        comida.goto(0,100)
        #Resetear Marcador
        texto.clear()#Limpiar el texto
        score = 0#Resetear marcador de partida
        texto.write("Score: {}       High Score: {}".format(score,highScore),align= "center", font=("Comic Sans MS",24,"bold"))#Nuevo texto
    #Colisiones con la comida
    if cabeza.distance(comida) <20:#validar la colisión, 20 es el tamaño por defecto de cada objeto. Distance calcula que la distancia no sea menor al tamaño de cada objeto.
        x= random.randint(-14,14) 
        y= random.randint(-14,11) #Funciones para que la comida siempre este en alineada con la serpiente
        comida.goto(x*20,y*20)

    #Creacion del cuerpo de la serpiente   
        nuevoSegmento = turtle.Turtle() #Creación del objeto que se va a mover(Serpiente)
        nuevoSegmento.speed(0) #Velocidad de movimiento del objeto cread(Serpiente)
        nuevoSegmento.shape("square")#Forma de la parte frontal del objeto creado(Cabeza de la serpiente)
        nuevoSegmento.color("orange")#Le da el color al objeto
        nuevoSegmento.penup()#Comando para que cuando el objeto se mueva no deje un rastro
        segmentos.append(nuevoSegmento) #Cada vez que choca con la comida, se crea un nuevo segmento, y se adiciona al arreglo segmentos

        #Aumento de marcador
        score+=10
        if score > highScore:
            highScore =score
        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, highScore),align= "center", 
        font=("Comic Sans MS",24,"bold"))

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos) #Se calcula el tamaño del arreglo, en este caso de la serpiente
    for index in range(totalSeg -1, 0, -1):#Se recorre el arreglo, desde la ultima posición menos 1, hasta la primera, con saltos de a -1.
        y = segmentos[index -1].ycor()#Se saca la coordenada y del segmento actual menos 1, para que el nuevo lo siga
        x = segmentos[index -1].xcor()#Se saca la coordenada x del segmento actual menos 1, para que el nuevo lo siga
        segmentos[index].goto(x,y)#Se indican las coordenadas, para que el nuevo segmento siga al anterior.

    if totalSeg > 0: #Se valida si la lista tiene elementos
        x =cabeza.xcor() #Se saca la coordenada x de la cabeza de la serpiente
        y =cabeza.ycor() #Se saca la coordenada y de la cabeza de la serpiente
        segmentos[0].goto(x,y) #se mueve el cuerpo hacía donde esta la cabeza

    movimiento()#Invocación del método movimiento creado anteriormente.

    #Colisiones con el cuerpo.
    for segmento in segmentos:
        if segmento.distance(cabeza) < 15: #Valida que la cabeza no tenga una distancia menor a 15 px con su cuerpo, pues cada segmento es de 20 px
            time.sleep(1) #Hace que el aplicativo dure 1 segundo esperando
            cabeza.goto(0,0) #ubica el objeto en estas coordenadas
            cabeza.direction ="stop" #Hace que el objeto serpiente se quede quieta mientras espera instrucciones.

            #Esconder los segmentos.
            for segmento in segmentos:
                segmento.goto(2000,2000)

            #Limpiar lista de segmentos
            segmentos.clear()
            comida.goto(0,100)
            cabeza.direction ="stop"
            #Resetear Marcador
            texto.clear()#Limpiar el texto
            score = 0#Resetear marcador de partida
            texto.write("Score: {}       High Score: {}".format(score,highScore),align= "center", font=("Comic Sans MS",24,"bold"))#Nuevo texto
    time.sleep(posponer)#Con esta declaración el programa se ejecutará más lento.