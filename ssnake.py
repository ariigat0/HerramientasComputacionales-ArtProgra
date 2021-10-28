import tkinter as tk # Python 2
import tkinter as tk # Python 3
import Imagenes #Libreria especial Creada por mi para la carga de Imagenes
import time #Libreria para el manejo de tiempos y cronometros

class load_window():
    root=object
    def __init__(self): #Declaro el constructor de Clase
        self.root = tk.Tk() #Creo la ventana Tk
        # The image must be stored to Tk or it will be garbage collected.
        imagen=Imagenes.get_imagen("logo2.png",1000,1000) #Llamo la funcion get_imagen para cargar una imagen a python
        label = tk.Label(self.root, image=imagen,bg="black") #creo un label, el cual contendra la imagen
        self.root.geometry("+470+200") #establesco la posicion de la pantalla de carga en el monitor
        self.root.overrideredirect(True) #Le establesco la propiedad de una ventana traslucida
        self.root.lift() #Le digo que al cargarse debera aparecer arriba de todas las ventanas creadas
        self.root.wm_attributes("-topmost", True) #le establesco que no debera poseer los botones de minimizar, maximizar y cierre
        #self.root.wm_attributes("-disabled", True) #Si no estuviera comentada y no existiese la linea anterior desabilitaria las funciones de los botones antes comentados
        self.root.wm_attributes("-transparentcolor", "black") #Le digo que la ventana debera actuar con transparencia en todo tono negro
        label.pack() #cargo el label

        # Establezco eventos para el raton
        self.root.bind("", lambda e:self.exit()) #Si el mouse deja la ventana traslucida
        self.root.bind("",lambda e:self.exit()) #o le doy click sobre la imagen
        #debera ejecutar la funcion exit
        self.root.mainloop()
    def exit(self):
        print 
        time.sleep(5) #espera 5s
        self.root.destroy() #cierra esta ventana
        import Snake #importa la libreria Snake correspondiente al archivo numero 2
        """Nota: La importancia de if __name__=='__main__': 
        en python es el siguiente:
        Si no es colocado e importo dicho archivo como libreria, al momento de hacer la importacion todas
        las instrucciones de dicho archivo se ejecutaran, en mi caso utilizo esa funcionalidad para ejecutar la ventana
        del juego sin mas lineas de codigo, pues como podran observar en ese archivo, esa linea no la utilize.
        De colocarla al momento de hacer la importacion, el codigo escrito no deberia ejecutarse como tal.
        """

c=load_window() #Creo un objeto que a si vez crea la ventana de carga


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys #Importo la libreria sys para manejar comandos del sistema
import Graficos #Importo otra libreria creada por mi
import time #Importo la libreria time para manejar tiempos
import random #importo random para ciertas acciones aleatorias
pygame.init() #Inicio pygame
ventana=pygame.display.set_mode((800,600)) #Establezco un modo de pantalla de 800x600 pixeles
pygame.display.set_caption("My Snake Game") #Establezco el titulo
graficos=Graficos.graficos(ventana) #Creo un objeto de la libreria Graficos pasandole las caracteristicas de la pantalla que ya cree

#variables
fase=0 #Esta variable define las fases del menu. Se explica mas adelante en el codigo
seleccionmenu=0 #Guarda las posibles selecciones hechas en el menu
orientacion=0 #Controla la orientacion de la serpiente. Leer el codigo mas adelante
puntuacion=0 #Maneja la puntuacion, se relaciona con el marcador. Leer y analizar codigo mas adelante
tema=1 #Define el tema por default del juego
seleccionGameOver=0 #Controla la seleccion del juego cuando el jugador ha perdido


while True: #Creo el loop principal del programa
    """Numero de Fases"""
    if fase==0: #Fase 1: Correspondiente al menu en si, al cargarse=
        graficos.Fondo() #Cargare un fondo al programa para borrar los graficos anteriores y actualizar la pantalla
        graficos.Titulo(seleccionmenu) #Carga los textos y mensajes en la pantalla principal, el parametro seleccion menu
        #funciona para manejar la posicion del sombreado segun la opcion a seleccionar en el menu. Analizar codigo del archivo graficos.
        pass
    elif fase==1: #Fase 2: Corresponde al juego en si
        graficos.Fondo() #Borra los graficos anteriores y coloca el fondo
        graficos.ScoreBoard() #Actualiza el marcador
        graficos.Drawcomida() #Dibuja la pepita de comida tras la cual debemos ir
        if graficos.DibujarSnake(orientacion)==1: #dibuja la serpiente mandando como paramentro la orientacion de la misma, esta
            #funcion devolvera un valor, si el valor es uno es que la serpiente colisiono consigo misma y perdimos
            fase=4 #Si esto pasa pasamos a la pantalla de Game Over
        pass
    elif fase==2: #Fase 2: Correspondiente al selector de Temas
        graficos.Fondo() #Borro los graficos anteriores y coloco el fondo
        graficos.temas(tema) #Despliego los textos y mando como parametro la variable tema. Analizar el archivo graficos para funcionamiento de dicho paramentro
        pass
    elif fase ==3: #Fase 3: correspondiente a los creditos
        graficos.Fondo() #Borro los graficos anteriores y coloco el fondo
        graficos.Creditos() #Muestro los textos correspondientes
        pass
    elif fase==4: #Fase 4: Correspondiente a la pantalla de Game Over
        graficos.gameover(seleccionGameOver) #Despliego los textos y mando como parametro la seleccion del juegador (continuar/rendirse). Analizar codigo

    """Comandos Pygame General"""
    for evento in pygame.event.get(): #Declaro un for para recorrer o checar toda accion por teclado y/o mouse
        if evento.type==QUIT: #Si se le pica a la x de la ventana
            pygame.quit() #Cierro pygame
            sys.exit() #Mato el proceso del programa
        elif evento.type==KEYDOWN: #Sino: si e presionado una tecla
            """Instrucciones para la fase 0"""
            if fase==0: #Chela si la variable fase a cambiado a 0, si si
                if evento.key==pygame.K_DOWN: #Checa si se presiono la tecla flecha_abajo
                    if seleccionmenu==0: #si si, si la seleccion es 0
                        seleccionmenu=1 #Cambio la seleccion a 1
                    elif seleccionmenu==1: #Si es 1 la seleccion
                        seleccionmenu=2 #La cambio a 2
                    elif seleccionmenu==2: #Misma tematica
                        seleccionmenu=0
                elif evento.key == pygame.K_UP: #Si se presiono la tecla flecha Arriba
                    if seleccionmenu==2: #Si, si, si la seleccion es 2
                        seleccionmenu=1 #cambio la seleccion a 1
                    elif seleccionmenu==1: #Misma tematica
                        seleccionmenu=0
                    elif seleccionmenu==0:
                        seleccionmenu=2
                elif evento.key == pygame.K_z: #Si se presiona la tecla z
                    if seleccionmenu==0: #Si la seleccion es 0
                        fase=1 #Entra a la fase 1
                    elif seleccionmenu==1: #Si es 1
                        fase=2 #entra a la fase 2
                    elif seleccionmenu==2: #Si es 2
                        fase=3 #Entra a la fase 3
                """Instrucciones para fase 1"""
            elif fase==1: #Si estamos en la fase 1
                """En esta fase deberemos checar constantemente las pulsaciones del teclado para dirigir a la serpiente."""
                """Imaginar la orientacion correspondiente a los angulos de un circulo. 0°:derecha 90°: Arriba 180°:Izquierda 270°:Abajo"""
                if (evento.key==K_s or evento.key==K_DOWN) and orientacion!=90: #Si se presiona K o flecha_abajo y la orientacion es diferente de 90, la condicion adicional es para evitar que se regrese por donde vino (se vaya en reversa)
                    orientacion=270 #La orientacion se setea a 270
                if (evento.key==K_w or evento.key==K_UP) and orientacion!=270:#Mismas tematicas
                    orientacion=90
                if (evento.key==K_a or evento.key==K_LEFT) and orientacion!=0:
                    orientacion=180
                if (evento.key==K_d or evento.key==K_RIGHT) and orientacion!=180:
                    orientacion=0
                """Instrucciones para fase 2"""
            elif fase==2:
                if evento.key==pygame.K_DOWN: #Si se presiona la tecla Flecha_Arriba
                    if tema==1: #Si el tema es 1
                        tema=2 #Cambia al tema 2
                    elif tema==2: #Mismas tematicas
                        tema=3
                    elif tema==3:
                        tema=4
                    elif tema==4:
                        tema=1
                elif evento.key == pygame.K_UP: #Si es flecha abajo
                    if tema==4: #Misma tematica que el anterior pero en orden inverso
                        tema=3
                    elif tema==3:
                        tema=2
                    elif tema==2:
                        tema=1
                    elif tema==1:
                        tema=4
                elif evento.key == pygame.K_x: #Si se presiona x
                    fase=0 #Se vuelve al menu o fase 0
                """Instrucciones para fase 3"""
            elif fase==3: #Fase 3: Creditos
                if evento.key==pygame.K_x: #Si se presiona x
                    fase=0 #Regresa al menu
                """Instrucciones para fase 4"""
            elif fase==4: #Fase 4: Game Over
                if evento.key==pygame.K_DOWN: #Si se presiona Flecha_Abajo
                    if seleccionGameOver==0:#Si la seleccion es 0
                        seleccionGameOver=1 #cambio la seleccion a 1
                    elif seleccionGameOver==1: #Y continua las mismas tematicas
                        seleccionGameOver=0
                elif evento.key == pygame.K_UP:
                    if seleccionGameOver==0:
                        seleccionGameOver=1
                    elif seleccionGameOver==1:
                        seleccionGameOver=0
                elif evento.key == pygame.K_z: #Si se presiona z
                    if seleccionGameOver==0: #Si la seleccion finalizo en 0
                        fase=1 #Regreso a la fase 1
                    elif seleccionGameOver==1: #Si no
                        fase=0 #Regreso al menu
                    del graficos.lrecs[:] #Tras esto borro el array lrecs. Analizar codigo en Graficos
                    orientacion=random.choice([0,180]) #Y la proxima vez que se cargue el juego estableceremos una orientacion al azar
    pygame.display.update() #Actualizo la pantalla
    time.sleep(0.07) #Duerme el programa por 0.07 segundos
    pass

#Graficos:

import pygame
from pygame.locals import *
import time
import random
import sys
pygame.init()

#Defino las librerias, no las volvere a comentar puesto su uso ya se definio con anterioridad

def settext(text,font,size,color): #Defino una funcion para manejar el texto y su formato
    """text: Texto a escribir
    font: Fuente a seleccionar
    size: tamano de letra
    color: color de letra"""
    if font==1: #Si selecciono esta fuente y la guardo en una variable Fuente
        Fuente=pygame.font.Font("fuentes/8-BIT WONDER.TTF",size) #Debera cargar esta fuente
    if font==2: #Misma tematica
        Fuente=pygame.font.Font("fuentes/04B_30__.TTF",size)
    if font==3:
        Fuente= pygame.font.Font("fuentes/Fipps-Regular.otf", size)
    if font==4:
        Fuente= pygame.font.Font("fuentes/baby blocks.ttf", size)
    texto=Fuente.render(text,True,color) #Creo el texto, con el color deseado
    return texto #Retorno el texto ya creado con la fuente deseada

class graficos(): #Defino la clase objetos
    """Defino las variables"""
    ventana=object #Defino una variable ventana que contendra las caracteristicas mandadas por parametro de la clase Snake
    Pcomida = (200, 200) #Defino las coordenadas iniciales de la comida de la serpiente
    puntuacion=0 #Seteo la puntuacion inicial en 0
    secciones= [(80, 80), (80, 100), (80, 120), (80, 140), (80, 160), (80, 180), (80, 200), (80, 220), (80, 240),(80, 260), (80, 280), (80, 300)] #Defino las coordenadas iniciales de los cuadros queconforman el cuerpo de la serpiente, cada par es un cuadro
    lrecs=[] #Defino este array que contendra los cuadros o cuerpo de la serpiente
    selector=0 #Usado para manejar selecciones.

    fondo = (1, 50, 102) #Defino el color del fondo
    COLOR_LETRA = (255, 255, 255) #El color de Letra
    COLOR_OBJETOS = (216, 27, 5) #El color de objetos como los sombreados y esas cosas

    def __init__(self,ventana): #Creo el constructor
        self.ventana=ventana #Copeara lo mandado como parametro al atributo ventana
        pass
    def Fondo(self): #Defino la funcion que dibuja el fondo
        self.ventana.fill(self.fondo) #Dibujo el fondo
    def Titulo(self,seleccion): #Defino la funcion que despliega el titulo "Menu principal"
        """Seleccionmenu se convierte en el parametro seleccion de la funcion"""
        if seleccion==0: #Si la seleccion es 0
            pygame.draw.rect(self.ventana,self.COLOR_OBJETOS,(110,200,430,40)) #Dibujara un rectangulo consombreado sobre estas coordenadas
        elif seleccion==1: #Si es 1
            pygame.draw.rect(self.ventana,self.COLOR_OBJETOS,(110,250,450,40)) #Sobre estas coordenadas
        elif seleccion==2: #Y asi
            pygame.draw.rect(self.ventana,self.COLOR_OBJETOS,(110,300,430,40))

        #Y coloco todos los textos en pantalla
        self.ventana.blit(settext("Snake",1,65,self.COLOR_LETRA),(20,50))
        self.ventana.blit(settext("UN JUGADOR",2,45,self.COLOR_LETRA),(120,200))
        self.ventana.blit(settext("TEMAS",2,45,self.COLOR_LETRA),(120,250))
        self.ventana.blit(settext("CREDITOS", 2, 45, self.COLOR_LETRA), (120, 300))
        self.ventana.blit(settext("Presione Z para seleccionar",1,15,self.COLOR_LETRA),(10,550))
        pass

    def temas(self,tema): #Defino la funcion que controla los temas
        if tema==1: #Si es tema seleccionado es el numero 1
            #Defino el fondo, color de letra y objetos con estos valores
            self.fondo=(1,50,102)
            self.COLOR_LETRA=(255,255,255)
            self.COLOR_OBJETOS=(216,27,5)
            pygame.draw.rect(self.ventana, self.COLOR_OBJETOS, (18, 100, 280, 50)) #Y dibujo un rectangulo de color establecido sobre la seleccion elegida
        elif tema==2: #Misma tematica
            self.fondo=(155,16,0)
            self.COLOR_LETRA=(255,255,255)
            self.COLOR_OBJETOS=(0,142,254)
            pygame.draw.rect(self.ventana, self.COLOR_OBJETOS, (18, 150, 280, 50))
        elif tema==3: #Misma tematica
            self.fondo=(118,56,187)
            self.COLOR_LETRA=(255,255,255)
            self.COLOR_OBJETOS=(255,131,0)
            pygame.draw.rect(self.ventana, self.COLOR_OBJETOS, (18, 200, 280, 50))
        elif tema==4: #Misma tematica
            self.fondo = (0, 214, 0)
            self.COLOR_LETRA = (255, 255, 255)
            self.COLOR_OBJETOS = (255, 195, 0)
            pygame.draw.rect(self.ventana, self.COLOR_OBJETOS, (18, 250, 280, 50))

        #Dibujo en pantalla los textos y elementos con los valores actualizados
        self.ventana.blit(settext("Selecctor de Tema", 2, 45, self.COLOR_LETRA), (20, 10))
        self.ventana.blit(settext("Tema 1", 1, 45, self.COLOR_LETRA), (20, 100))
        self.ventana.blit(settext("Tema 2", 1, 45, self.COLOR_LETRA), (20, 150))
        self.ventana.blit(settext("Tema 3", 1, 45, self.COLOR_LETRA), (20, 200))
        self.ventana.blit(settext("Tema 4", 1, 45, self.COLOR_LETRA), (20, 250))
        self.ventana.blit(settext("Presione x para Guardar y Regresar", 1, 15, self.COLOR_LETRA), (10, 550))


    def Creditos(self): #Funcion que maneja los creditos
        #Simplemente despliega los textos correspondientes
        self.ventana.blit(settext("CREDITOS: ",4,80,self.COLOR_LETRA),(10,30))
        self.ventana.blit(settext("Autor: Braulio Lobo, Sin Fines de Lucro",3,15,self.COLOR_LETRA),(20,250))
        self.ventana.blit(settext("Link: https://www.youtube.com/watch?v=Dm32c_G_Cik",3,15,self.COLOR_LETRA),(20,280))
        self.ventana.blit(settext("Modificado por: Ambrocio Isaias Laureano Castro",3,15,self.COLOR_LETRA), (20, 320))
        self.ventana.blit(settext("Presione x para volver",1,15,self.COLOR_LETRA), (10, 550))

    def gameover(self,seleccion): #Maneja la pantalla de GameOver
        """seleccionGameOver se maneja aqui como el parametro seleccion"""
        self.ventana.blit(settext("Game Over",1,56,self.COLOR_LETRA), (140, 250))
        if seleccion==0: #Si la seleccion es 0 "Continuar"
            #Despliego los textos
            self.ventana.blit(settext("Continuar",1,16,self.COLOR_OBJETOS), (140, 350)) #Pero pinto el color de letra del valor seleccionado de otro color segun el tema del juego
            self.ventana.blit(settext("Me Rindo",1,16,self.COLOR_LETRA), (140, 450))
        elif seleccion==1: #Misma tematica "Merindo"
            self.ventana.blit(settext("Continuar", 1, 16,self.COLOR_LETRA ), (140, 350))
            self.ventana.blit(settext("Me Rindo", 1, 16, self.COLOR_OBJETOS), (140, 450))

        pass
    def DibujarSnake(self,orientacion): #Creo la funcion que dibujara y controlara a la serpiente
        for i in self.secciones: #creo un for que recorrera todas las secciones de la serpiente
            x, y = self.getxy(i) #Obtengo las de cada seccion y las guardo en las variables X y Y

            #Despues agrego a la variable Lrecs (que es como el array que refiere al cuerpo construido de la serpiente) la seccion correspoendiente a dibujar
            self.lrecs.append(pygame.draw.rect(self.ventana,self.COLOR_LETRA,(x+1,y+1,18,18))) #Le digo que se desplegara en la ventana, con el mismo color que las letras, en tal coordenada x y tal coordenada y, con 18 pixeles de ancho por 18 de alto
            if len(self.lrecs)==len(self.secciones): #cada que se repita el ciclo, si el cuerpo de la serpiente es igual de largo a el numero de secciones
                """En otras palabras si ya se dibujo la cola de la sepriente"""
                del self.lrecs[0] #Borro una seccion de la serpiente para simular que va avanzando
            if self.colision() == 1: #Si por casualidad esta choca con una parte de su cuerpo (checar la funcion colision para mayor entendimiento)
                return 1 #Retornaremos 1 para cambiar de fase en el archivo Snake para mostrar la pantalla de GameOver
            """si no se cumple ningula de las anteriores condiciones dibuja la cola o una seccion mas de la serpiente"""
            #Pero antes de eso comprovamos si la serpiente  ha salido de la pantalla
            if self.secciones.index(i)==len(self.secciones)-1: #entonces si ya se ha dibujado la cola de la serpiente
                """Checamos donde se dibujo por ultima vez"""
                if x==0 and orientacion==180: #Si la ultima coordenada en x=0 y va hacia la izquierda
                    x=1000 #La proxima coordenada a usar en x=1000 correspondiente a aparecer del lado derecho de la pantalla
                elif x==800 and orientacion==0: #Si la ultima coordenada en x=800 y va hacia la derecha
                    x=0 #La proxima coordenada a usar en x=0 es decir aparecera la serpiente por el lado izquierdo de la pantalla

                """Mismo aplica para la orientacion en y en forma similar"""
                if y==0 and orientacion==90:
                    y=800
                if y==800 and orientacion==270:
                    y=0

                #Casi Por ultimo
                if orientacion==0: #Si la orientacion es 0
                    self.secciones.append((x+20,y)) #La proxima seccion se dibujara en las coordenadas x+20, y es decir sumaremos 20 pixeles al eje x
                #Situaciones similares con las demas condiciones
                elif orientacion==90:
                    self.secciones.append((x, y-20))
                elif orientacion==180:
                    self.secciones.append((x-20, y))
                elif orientacion==270:
                    self.secciones.append((x, y+20))

                #La letra i dado las caracteristicas del for un python almacenara las coordenadas de la secciona a dibujar de la serpiente
                #en ese instante
                if i!= self.Pcomida: #Si no concide con las coordenadas de donde esta la comida
                    del self.secciones[0] #Borro una coordenada de las secciones para almacenar una nueva al repetir el ciclo
                    del self.lrecs[0] #Borro una parte de la serpiente para meter otra el repetir el ciclo
                    return self.Pcomida #Retorno la posicion de la comida
                else: #Si la cabeza colisiona con la comida, es decir coinciden las coordenadas
                    self.puntuacion=self.puntuacion+1 #Sumo un ponto
                    self.Pcomida= (random.randint(0,25)*20,random.randint(0,25)*20) #Coloco otra pepita de comida en coordenadas random multiplicando los rangos por 20 para que sean multiplos de coordenadas que aparescan en la pantalla y no fuera de la ventana
                    self.Drawcomida() #Mando a dibujar la comida en sus nuevas posiciones
                break
        return 0 #Si llego a este punto significa que la serpiente no se comio a si misma asi que retorno 0

    def Drawcomida(self):
            pygame.draw.rect(self.ventana, self.COLOR_OBJETOS, (self.Pcomida[0], self.Pcomida[1], 18, 18))

    def ScoreBoard(self):
            self.ventana.blit(settext("Score: " + str(self.puntuacion),1,15,self.COLOR_LETRA), (10, 10))

    def getxy(self,c):
        x=c[0] #guardo en x el valor del primer valor del primer par de coordenadas del array secciones
        y=c[1]#guardo en Y el valor del segundo valor del primer par de coordenadas del array secciones
        return x,y #retorno las coordenadas

    def colision(self):
        """Ahora, si suponemos que en el array lrecs se esta guardando el cuerpo de la serpiente entonces:
        el cuerpo debera estar desde la posicion 0 hasta la penultima posicion
        y la cabeza deberia ser la ultima posicion del array

        0 seccion
        X Cabeza
        ~ Lengua jejej

        0 1 2 3 4 5 6
        0 0 0 0 0 0 X~

        """
        cuerpo=self.lrecs[0:len(self.lrecs)-2] #En fin obtengo las coordenadas de todos los cuadros que corresponden al cuerpo
        cabeza=self.lrecs[len(self.lrecs)-1] #Obtengo las coordenadas de la cabeza
        if cabeza in cuerpo: #Si las coordenadas de la cabeza coinciden con alguna coordenada del cuerpo se supone que perdio
            self.puntuacion=0 #entonces la puntuacion se resetea a 0
            del self.secciones[:] #Borro todas las secciones
            #Y vuelvo a colocar las coordenadas iniciales de donde empezo la serpiente
            self.secciones=[(80, 80), (80, 100), (80, 120), (80, 140), (80, 160), (80, 180), (80, 200), (80, 220), (80, 240),(80, 260), (80, 280), (80, 300)]
            return 1 #Y devuelvo un 1, para que se retorne en la funcion DibujarSnake para que a su vez retorne el valor 1 para cambiar a la fase 4 en el archov Snake
        return 0 #Si no sucede solo retorno 0 para que continue normalmente el juego
