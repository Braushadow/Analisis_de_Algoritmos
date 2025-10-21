#Introducción 

Hola, este es un breve tutorial de como utilizar el programa de busqueda de contraseñas por diccionario y tiempo 
utilizando la tecnica de divide y vencerás


**Tutorial
Al correr el programa, aparecerán 2 pestañas en la GUI, una es de un ataque de diccionario pequeño (puede ser agrandado), 
sin embargo l aparte importante es en la pestaña de divide y vencerás, ahí es donde se puede añadir distintas contraseñas
para que los workers (trabajadores) intenten averiguar las contraseñas en un tiempo determinado. Es posible configurar 
desde la misma GUI las restricciones que se le pueden poner a la hora de ingresar las contraseñas, asi como el tiempo 
en el que se buscarán las contraseñas. 

A diferencia de su antecesor de fuerza bruta, el presente algoritmo permite buscar varias contraseñas a la vez, dandole un hilo 
a cada uno de los workers con el objetivo de que al momento que el algoritmo genera combinaciones aleatorias los workers trabajan 
en paralelo, permitiendo encontrar contraseñas en menor tiempo, justo aqui es donde sucede la parte de divide y vencerás pues antes 
se requeria trabajar con una sola contraseña a la vez. 

La GUI cuenta con un boton para generar una grafica, en la cual es posible observar la velocidad con la que el algoritmo encuentra las 
contraseñas con respecto a la cantidad de caracteres que se le permite ingresar a las contraseñas. 
