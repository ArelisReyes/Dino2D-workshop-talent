import pgzrun
import random

WIDTH = 800
HEIGHT = 600

dino = Actor("run1")
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

def draw():
    global game_over

    if game_over:
        screen.draw.text("GAME OVER", (300, 200), color="black", fontsize=40)
        screen.draw.text("Presiona R para reiniciar", (200, 300), color="black", fontsize=50)
    else:
        screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT/2), (160, 230, 250))
        screen.draw.filled_rect(Rect(0, HEIGHT/2, WIDTH, HEIGHT/2), (90, 250, 150))
        screen.draw.text(f"Puntaje: {score}", (15, 10), color="black", fontsize=30)
        dino.draw()
        for obstaculo in obstaculos:
            obstaculo.draw()

def update():
    global velocidadY, tiempo_obstaculo, tiempoAl, score, game_over, inicio

    if keyboard.SPACE:
        inicio = False

    if inicio == False:
       
        tiempo_obstaculo += 1

        if tiempo_obstaculo > tiempoAl:
            obs = Actor("cactus")
            obs.x = WIDTH + 50
            obs.y = HEIGHT/2
            ob2 = Actor("swordgold")
            ob2.x = WIDTH + 50
            ob2.y = HEIGHT/2
            opciones = [obs, ob2]
            obstaculos.append(random.choice(opciones))
            tiempo_obstaculo = 0
            tiempoAl = random.randint(40, 70)

        for obstaculo in obstaculos:
            obstaculo.x -= 8
            if obstaculo.x < -50:
                obstaculos.remove(obstaculo)
                score += 1

        if keyboard.up and dino.y == HEIGHT/2:
            velocidadY = -15

        dino.y += velocidadY
        velocidadY += gravedad

        if dino.y > HEIGHT/2:
            velocidadY = 0
            dino.y = HEIGHT/2

        if dino.collidelist(obstaculos) == 0:
            game_over = True

        if keyboard.R:
            game_over = False
            obstaculos.clear()
            score = 0

pgzrun.go()
