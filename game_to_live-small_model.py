import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
from matplotlib.widgets import Button

# Tamaño del tablero
width, height = 100, 100
nxC, nyC = 60, 60

# Dimensiones de cada celda
dimCW = width / nxC
dimCH = height / nyC

# Inicializar el estado del juego con células vivas y muertas aleatoriamente
gameState = np.random.choice([0, 1], size=(nxC, nyC))

# Variable para pausar y reanudar el juego
pauseExect = True

# Crear el mapa de colores personalizado
cmap = ListedColormap(['gray', 'white'])

# Crear la figura y el gráfico
fig, ax = plt.subplots()
plt.axis('off')
cax = ax.imshow(gameState, cmap=cmap)

# Función para manejar los clics del ratón en el gráfico
def on_click(event):
    global gameState
    x, y = int(event.ydata), int(event.xdata)
    gameState[x][y] = 1 if gameState[x][y] == 0 else 0
    cax.set_data(gameState)
    fig.canvas.draw()

#pausar    
def on_key_press(event):
    global pauseExect
    if event.key == 'enter':
        pauseExect = not pauseExect

# Función de actualización para la animación del gráfico
def update(frameNum):
    global gameState
    newGameState = gameState.copy()

    if not pauseExect:
        for x in range(nxC):
            for y in range(nyC):
                # Calcular el número de vecinos vivos
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x) % nxC, (y - 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x - 1) % nxC, (y) % nyC] + \
                          gameState[(x + 1) % nxC, (y) % nyC] + \
                          gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                          gameState[(x) % nxC, (y + 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y + 1) % nyC]

                # Reglas del Juego de la Vida
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

    # Actualizar el estado del juego
    gameState = newGameState
    cax.set_data(gameState)
    return cax,

def start_button_callback(event):
    global pauseExect
    pauseExect = False

def create_button_callback(event):
    global gameState, pauseExect
    pauseExect = True
    gameState = np.zeros((nxC, nyC))
    cax.set_data(gameState)
    fig.canvas.draw()

def random_button_callback(event):
    global gameState, pauseExect
    pauseExect = True
    gameState = np.random.choice([0, 1], size=(nxC, nyC))
    cax.set_data(gameState)
    fig.canvas.draw()

def pause_button_callback(event):
    global pauseExect
    pauseExect = not pauseExect

# Crear y posicionar los botones
start_button_ax = plt.axes([0.15, 0.025, 0.1, 0.04])
create_button_ax = plt.axes([0.35, 0.025, 0.1, 0.04])
random_button_ax = plt.axes([0.55, 0.025, 0.1, 0.04])
pause_button_ax = plt.axes([0.75, 0.025, 0.1, 0.04])

start_button = Button(start_button_ax, 'Iniciar')
create_button = Button(create_button_ax, 'Crear')
random_button = Button(random_button_ax, 'Random')
pause_button = Button(pause_button_ax, 'Pausa')

start_button.on_clicked(start_button_callback)
create_button.on_clicked(create_button_callback)
random_button.on_clicked(random_button_callback)
pause_button.on_clicked(pause_button_callback)

# Conectar eventos de clic y pulsación de teclas
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('key_press_event', on_key_press)

# Crear y mostrar la animación
ani = FuncAnimation(fig, update, interval=200, blit=True)
plt.show()