Dino Run
Dino Run es un juego simple en el que el jugador controla a un dinosaurio que debe saltar sobre obstáculos y evitar chocar con ellos. El objetivo es lograr la mayor cantidad de puntos posible antes de que el jugador pierda.

Este juego fue creado con el módulo Pygame Zero.

Cómo jugar
El juego comienza con una pantalla de bienvenida que se muestra. Para comenzar a jugar, el jugador debe presionar la barra espaciadora. Una vez que comienza el juego, el dinosaurio comenzará a correr automáticamente. El jugador debe presionar la barra espaciadora para saltar sobre obstáculos.

Si el jugador choca con un obstáculo, el juego termina y se muestra la pantalla de Game Over. Para reiniciar el juego, el jugador debe presionar la tecla 'R'.

Cómo funciona el código
El código se divide en dos funciones principales: draw() y update().

La función draw() se encarga de dibujar los gráficos del juego en la pantalla. Esta función verifica si el juego ha terminado y muestra la pantalla de Game Over si es así. Si el juego sigue en marcha, dibuja el cielo y el suelo, el puntaje actual y el dinosaurio y obstáculos.

La función update() maneja la lógica del juego. Actualiza la posición del dinosaurio y de los obstáculos en cada fotograma, verifica si el jugador ha chocado con un obstáculo y actualiza el puntaje. También maneja la entrada del jugador y reinicia el juego si se presiona la tecla 'R'.

Además, hay algunas variables globales que controlan el estado del juego, como la lista de obstáculos, el puntaje y el estado de Game Over.

En resumen, Dino Run es un juego simple pero divertido que muestra algunos de los conceptos básicos de la programación de juegos en Python.
