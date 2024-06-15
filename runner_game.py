from pgzhelper import *
import random

WIDTH = 800
HEIGHT = 600

dino = Actor("run1")
dino_imagenes = ["run1", "run2", "run3", "run4", "run5", "run6", "run7", "run8"]
dino.images = dino_imagenes

dino.x = 200
dino.y = 500
dino.fps = 20

obstaculos = []
tiempo_obstaculo = 0

velocidadY = 0
gravedad = 1
score = 0
game_over = False

bienvenida = Actor("bienvenida")
bienvenida.x = 400
bienvenida.y = 300

inicio = True

tiempoAl = random.randint(40, 70)

tracks = ["dark-wings-short", "geek-club-short", "palm-beach-short"]
track = random.randint(0, 2)
music.set_volume(.03)
music.play(tracks[track])

def draw():
    if inicio == True:
        bienvenida.draw()
    else:
        if game_over != True:
            screen.draw.filled_rect(Rect(0, 0, 800, 400), (160, 230, 250))
            screen.draw.filled_rect(Rect(0, 400, 800, 200), (90, 250, 150))
            screen.draw.text(
                "Puntaje: " + str(score), (15, 10), color=(0, 0, 0), fontsize=30, fontname = "stocky"
            )
            dino.draw()
            for obstaculo in obstaculos:
                obstaculo.draw()
        else:
            screen.draw.text("GAME OVER", (300, 200), color=(0, 0, 0), fontsize=40)
            screen.draw.text("Presiona R para reiniciar", (200, 300), color=(0, 0, 0), fontsize=50)


def update():
    global velocidadY, tiempo_obstaculo, tiempoAl, score, game_over, inicio

    if keyboard.SPACE:
        inicio = False

    if inicio == False:
        # dino.next_image()
        dino.animate()

        tiempo_obstaculo += 1

        if tiempo_obstaculo > tiempoAl:
            obs = Actor("cactus")
            obs.x = 850
            obs.y = 430
            ob2 = Actor("swordgold")
            ob2.x = 850
            ob2.y = 430
            opciones = [obs, ob2]
            obstaculos.append(random.choice(opciones))
            tiempo_obstaculo = 0
            tiempoAl = random.randint(40, 70)

        for obstaculo in obstaculos:
            obstaculo.x -= 8
            if obstaculo.x < -50:
                obstaculos.remove(obstaculo)
                score += 1

        if keyboard.up and dino.y == 400:
            velocidadY = -15

        dino.y += velocidadY
        velocidadY += gravedad

        if dino.y > 400:
            velocidadY = 0
            dino.y = 400

        if dino.collidelist(obstaculos) == 0:
            game_over = True

        if keyboard.R:
            game_over = False
            obstaculos.clear()
            score = 0
