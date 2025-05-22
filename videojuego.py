#Librerias necesarias para crear el videojuego
import pygame #libreria para realizar videojuegos
import random #libreria que proporciona funciones para generar números aleatorios y operaciones que tengan que ver con datos al azar
import sys #libreria que permite interactuar con el sistema operativo y con el intérprete de Python

#Configuraciones basicas

#Inicializar la libreria de "Pygame"
pygame.init()

#Configuracion de la pantalla del juego

#dimensiones de la pantalla (Ancho, Alto y tamaño de la dado en pixeles)
Ancho = 800
Alto = 600
TamañoCelda = 50
Pantalla = pygame.display.set_mode((Ancho, Alto)) #funcion que permite crear la ventana del juego de acuerdo al alto y ancho ya establecidos
pygame.display.set_caption(" Videojuego de la culebrita") #Funcion que permite cambiar el nombre de la ventana del juego

# Variables con los colores que se utilizaran en el videojuego en Formato RGB
Blanco = (255, 255, 255)
Rojo = (255, 0, 0)
Verde = (0, 255, 0)
Negro = (0, 0, 0)
Azul = (0, 0, 255)

# clase que permite controlar el tiempo dentro del juego (fps)
Reloj = pygame.time.Clock()

# Fuente de la letra
fuente = pygame.font.SysFont("Arial", 28) 

#Funciones propias que utilizares para crear al personaje, obstaculo, menus, puntaje entre otros

#Funcion Para la letra que va a tener el menú de inicio, la pantalla de game over y la pantalla si completaste las 60 comidas
def texto(texto, color, y_offset=0):
    label = fuente.render(texto, True, color)
    rectangulo = label.get_rect(center=(Ancho // 2, Alto // 2 + y_offset))
    Pantalla.blit(label, rectangulo)

#Funcion para crear el menú principal del juego
def MenuPrincipal():
    Pantalla.fill(Negro) 
    texto(" Bienvenido al juego de la Culebrita ", Azul) 
    texto(" Presiona ESPACIO para comenzar a jugar ", Blanco, 60) 
    texto("Videojuego Creado por HUGO NARANJO", Blanco, 120)
    pygame.display.flip() 
    
    #bucle para que el jugador solo pueda seleccionar "espacio" para que inicie el juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
    
#Funcion para crear al personaje en este caso la serpiente 
def serpiente(Cuerpo_Serpiente):
    for segmento in Cuerpo_Serpiente:
        pygame.draw.rect(Pantalla, Verde, pygame.Rect(segmento[0], segmento[1], TamañoCelda, TamañoCelda)) #función que se utiliza para dibujar un rectángulo en una superficie

#Funcion que permite crear la comida de la serpiente
def Comida(Posicion):
    pygame.draw.rect(Pantalla, Rojo, pygame.Rect(Posicion[0], Posicion[1], TamañoCelda, TamañoCelda))    

#funcion que permite que la comida que el jugador debe alcanzar salgan de forma aleatoria
def PosicionComida(Cuerpo_Serpiente):
    while True:
        azar = [random.randrange(0, Ancho, TamañoCelda), random.randrange(0, Alto, TamañoCelda)]
        if azar not in Cuerpo_Serpiente:
            return azar

#Funcion para la pantalla de Game Over
def PantallaGameOver(Puntaje):
    Pantalla.fill(Negro)
    texto("¡Perdiste, Vuelve a intentarlo!", Rojo,)
    texto(f"Puntaje final: {Puntaje}", Blanco, 80)
    texto("Presiona ESPACIO para reiniciar o ESC para salir", Blanco, 120)
    pygame.display.flip()
#Bucle para que el jugador vea su puntaje y ademas pueda decidir si seguir jugando o cerrar la ventana del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Codigo_Principal()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

"""
Programa Principal 
Aqui se hace una preconfiguracion de la serpiente y del puntaje
"""
def Codigo_Principal():
    Cuerpo_Serpiente = [[100, 100], [80, 100], [60, 100]]
    direccion = "Derecha"
    Cambio = direccion
    Puntaje = 0
    Posicion_Comida = PosicionComida(Cuerpo_Serpiente)
    
#Configuracion de los controles de la serpiente
    while True:
        for teclado in pygame.event.get():
            if teclado.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif teclado.type == pygame.KEYDOWN:
                if teclado.key == pygame.K_w and direccion != "Abajo":
                    Cambio = "Arriba"
                elif teclado.key == pygame.K_s and direccion != "Arriba":
                    Cambio = "Abajo"
                elif teclado.key == pygame.K_a and direccion != "Derecha":
                    Cambio = "Izquierda"
                elif teclado.key == pygame.K_d and direccion != "Izquierda":
                    Cambio = "Derecha"
#Condicion para que halla un final en el juego, al obtener un puntaje de 60 el juego te dice que completaste el videojuego
        if Puntaje == 60:
            Pantalla.fill(Negro)
            texto("Felicidades conseguiste las 60 comidas, ¡completaste el juego!", Azul)
            texto("Puntaje final: {}".format(Puntaje), Blanco, 150)
            texto("Presiona ESPACIO para reiniciar o ESC para salir", Blanco, 100)
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            Codigo_Principal()
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
    
    #Condicion para que el jugador si se golpea con el borde de la venta pieda la partida                
        direccion = Cambio
        head_x, head_y = Cuerpo_Serpiente[0]

        if direccion == "Arriba":
            head_y -= TamañoCelda
        elif direccion == "Abajo":
            head_y += TamañoCelda
        elif direccion == "Izquierda":
            head_x -= TamañoCelda
        elif direccion == "Derecha":
            head_x += TamañoCelda

        new_head = [head_x, head_y]
        
        if (
            head_x < 0 or head_x >= Ancho or
            head_y < 0 or head_y >= Alto or
            new_head in Cuerpo_Serpiente
        ):
            PantallaGameOver(Puntaje)
            return

        Cuerpo_Serpiente.insert(0, new_head)

        if new_head == Posicion_Comida:
            Puntaje += 1
            Posicion_Comida = PosicionComida(Cuerpo_Serpiente)
        else:
            Cuerpo_Serpiente.pop()
#Aqui se llaman todas las funciones necesarias para que el juego funciones como la serpiente, la comida y el puntaje
        Pantalla.fill(Negro)
        Comida(Posicion_Comida)
        serpiente(Cuerpo_Serpiente)
        texto("Puntaje Actual: {}".format(Puntaje) , Blanco, -250,)
        pygame.display.flip()
        Reloj.tick(10)

#Ejecuccion del juego    
MenuPrincipal()
Codigo_Principal()