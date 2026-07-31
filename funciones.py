from random import *
from copy import *
import pygame 
from constantes import *



def crear_matriz(filas: int, columnas: int, valor: any = None) -> list:
    """
    Crea una matriz inicializada en un valor.\n
    filas(int): entero representando las filas de la matriz.\n
    columnas(int): entero representando las columnas de la matriz.\n
    valor(any): valor inicializado en la matriz (por defecto None).\n
    Retorna la matriz inicializada.
    """
    matriz = []
    for _ in range(filas):
        fila = [valor] * columnas
        matriz += [fila]
    return matriz



def cargar_celda_sudoku (matriz: list, fila: int, columna:int, matriz_paralela_correctos = list) -> None:
    """
    Carga la celda de un sudoku.\n
    matriz(list): matriz que será el sudoku.\n
    fila(int): fila donde se encuentra el valor a cargar.\n
    columna(int): columna donde se encuentra el valor a cargar.\n
    matriz_paralela_correctos(list): matriz donde cada celda tiene una lista con los numeros posibles a insertar en esa celda.\n
    No tiene retorno.
    """
    num_ingresado_correctamente = None

    while num_ingresado_correctamente != True:
        num_ingresado_correctamente = False
        while True:
                es_valor_correcto = False
                if len(matriz_paralela_correctos[fila][columna]) != 0:
                    indice_random = randint(0, (len(matriz_paralela_correctos[fila][columna])-1))
                    numero_random = matriz_paralela_correctos[fila][columna][indice_random]

                    if validar_no_repetido_sudoku(numero_random, matriz, fila, columna) == True:
                        es_valor_correcto = True
                    else:
                        matriz_paralela_correctos[fila][columna].remove(numero_random)

                    if es_valor_correcto == True:
                        matriz[fila][columna] = numero_random
                        num_ingresado_correctamente = True
                        break
                else:
                    break

        if num_ingresado_correctamente == False:
                if columna > 0:
                    columna_anterior = columna-1
                    fila_anterior = fila
                else:
                    if fila == 0:                         
                        columna_anterior = columna
                        fila_anterior = fila
                    else:
                        columna_anterior = 8
                        fila_anterior = fila-1

                matriz[fila][columna] = None
                matriz_paralela_correctos[fila][columna] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                cargar_celda_sudoku(matriz, fila_anterior, columna_anterior, matriz_paralela_correctos)



def cargar_matriz_sudoku(matriz: list) -> None:
    """
    Carga una matriz sudoku.\n
    matriz(int): matriz iniciada donde se cargarán los números.\n
    No tiene retorno.
    """
    matriz_paralela = crear_matriz(9, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            cargar_celda_sudoku(matriz, i, j, matriz_paralela)



def validar_no_repetido_submatriz(rango_fila: range, rango_columna: range, matriz: list, valor: any) -> bool:
    """
    Valida que un valor no este repetido en una submatriz.\n
    rango_fila(range): rango representativo de la fila para indicar el bloque.\n
    rango_columna(range): rango representativo de la columna para indicar el bloque.\n
    matriz(list): matriz sudoku a evaluar.
    valor(any): valor a comprobar si esta repetido en la submatriz.\n
    Retorna False en caso de encontrar una repetición, de lo contrario retorna True.
    """
    bandera = True
    for i in rango_fila:
        for j in rango_columna:
            if matriz[i][j] == valor:
                bandera = False
    return bandera


def validar_no_repetido_fila (fila: int, matriz: list, valor: any) -> bool:
    """ 
    Valida que un valor no este repetido en una fila.\n
    fila(int): entero que determina la fila actual a validar.\n
    matriz(list): matriz a comprobar.\n
    valor(any): valor a comprobar si esta repetido en la fila.
    Retorna False si el valor esta repetido, de lo contrario retorna True.
    """
    bandera = True

    for i in range (len(matriz[fila])):
        if valor == matriz[fila][i]:
            bandera = False
            break

    return bandera


def validar_no_repetido_columna (columna: int, matriz: list, valor: any) -> bool:
    """
    Valida que un valor no este repetido en una columna.\n
    columna(int): entero que determina la columna actual a validar.\n
    matriz(list): matriz a comprobar.\n
    valor(any): valor a comprobar si esta repetido en la columna.
    Retorna False si el valor esta repetido, de lo contrario retorna True.
    """
    bandera = True

    for j in range (len(matriz)):
        if valor == matriz[j][columna]:
            bandera = False
            break
        
    return bandera


## REVISAR LOS BLOQUES

def validar_no_repetido_sudoku(valor: int, matriz: list, fila: int, columna: int) -> bool:
    """ 
    Esta funcion valida que un número cumpla con las reglas del sudoku.\n
    
    parametros:\n
    valor(int): numero a validar.\n
    matriz(list): matriz de sudoku a validar.\n
    fila(int): fila donde se encuentra el valor a validar.\n
    columna(int): columna donde se encuentra el valor a validar.\n

    Retorna True si el valor no esta repetido en la fila, columna y submatriz, en caso contrario nos retorna False.\n
    """
    bandera = False
    
    bandera = validar_no_repetido_fila(fila, matriz, valor)

    if bandera == True:
        bandera = validar_no_repetido_columna(columna, matriz, valor)

    #SubMatriz
    if bandera == True:
        bloque_fila = fila // 3  
        bloque_columna = columna // 3  

        bloque = (bloque_fila, bloque_columna)
        match bloque:
            case (0, 0):
                rango_fila = range(0, 3)
                rango_columna = range(0, 3)
            case (0, 1):
                rango_fila = range(0, 3)
                rango_columna = range(3, 6)
            case (0, 2):
                rango_fila = range(0, 3)
                rango_columna = range(6, 9)
            case (1, 0):
                rango_fila = range(3, 6)
                rango_columna = range(0, 3)
            case (1, 1):
                rango_fila = range(3, 6)
                rango_columna = range(3, 6)
            case (1, 2):
                rango_fila = range(3, 6)
                rango_columna = range(6, 9)
                        
            case (2, 0):
                rango_fila = range(6, 9)
                rango_columna = range(0, 3)  
            case (2, 1):
                rango_fila = range(6, 9)
                rango_columna = range(3, 6)
            case (2, 2):
                rango_fila = range(6, 9)
                rango_columna = range(6, 9)

        bandera = validar_no_repetido_submatriz(rango_fila, rango_columna, matriz, valor)

    return bandera




def crear_txt_timer(superficie: pygame.Surface, contador_seg: int, contador_min: int, tamaño_txt: int, color_txt: tuple)-> pygame.Surface:
    """ 
    Crea un texto que muestra el tiempo transcurrido en minutos y segundos\n
    Parametros:\n
    superficie(pygame.Surface): superficie donde se dibuja el texto.\n
    contador_seg(int): contador de segundos transcurridos.\n
    contador_min(int): contador de minutos transcurridos.\n
    tamaño_txt(int): tamaño del texto a mostrar.\n
    color_txt(tuple): color del texto a mostrar.\n
    Retorna: pygame.Surface con el texto del timer.\n
    """

    if contador_seg < 10 and contador_min < 10:
        txt_timer = crear_superficie_texto("Showcard Gothic", tamaño_txt, f"TIEMPO | 0{contador_min}: 0{contador_seg}", color_txt, superficie)

    elif contador_seg < 10:
        txt_timer = crear_superficie_texto("Showcard Gothic", tamaño_txt, f"TIEMPO | {contador_min}: 0{contador_seg}", color_txt, superficie)
    elif contador_min < 10:
        txt_timer = crear_superficie_texto("Showcard Gothic", tamaño_txt, f"TIEMPO | 0{contador_min}: {contador_seg}", color_txt, superficie)

    else:
        txt_timer = crear_superficie_texto("Showcard Gothic", tamaño_txt, f"TIEMPO | {contador_min}: {contador_seg}", color_txt, superficie)
    
    return txt_timer



def cargar_escalar_imagen (ruta: str, porcentaje_size_h, superficie: pygame.Surface) -> pygame.Surface:
    """ 
    Esta funcion carga una imagen desde una ruta especifica y la escala a un porcentaje de la altura de una superficie.\n
    Parametros:\n
    ruta(str): ruta de la imagen que vamos a cargar.\n
    porcentaje_size_h(int): porcentaje de la altura de la superficie donde se va a escalar la imagen.\n
    superficie(pygame.Surface): superficie donde se va a escalar la imagen.\n

    Retorna la imagen escalada.\n
    """
    imagen = pygame.image.load(ruta).convert_alpha()

    ancho_imagen_original = imagen.get_width()
    alto_imagen_original = imagen.get_height()

    alto_superficie = superficie.get_height()

    alto_imagen = porcentaje_size_h * alto_superficie // 100
    ancho_imagen = alto_imagen * ancho_imagen_original // alto_imagen_original

    imagen_escalada = pygame.transform.scale(imagen, (ancho_imagen, alto_imagen))

    return imagen_escalada


def crear_rect_centrado_en_x (superficie: pygame.Surface, posicion_y: int, size: tuple) -> pygame.Rect: 
    """ 
    Esta funcion crea un rect y lo ubica en el centro de X sobre una superficie, y en Y se elige posicion especifica\n
    
    parametros:\n
    superficie(pygame.Surface): superficie donde se dibuja el rectangulo.\n
    posicion_y(int): entero que representa el porcentaje de la altura de la superficie donde se ubica el rectangulo.\n
    size(tuple): tupla con el tamaño del rectangulo en ancho y alto.\n

    Retorna: (pygame.Rect) con la posicion y tamaño del rectangulo.\n
    """
    ancho_pantalla = superficie.get_width() 
    alto_pantalla = superficie.get_height() 
    posicion_rect_y = posicion_y * alto_pantalla / 100

    size_w, size_h = size
    size_w, size_h = calcular_tamaño_rect(superficie, size_w, size_h)

    rect = pygame.Rect(0, posicion_rect_y, size_w, size_h)
    rect.centerx = ancho_pantalla / 2 
    

    return rect


def definir_num_correcto (num_correcto: int, num_usuario: int) -> bool:
    """ 
    Esta funcion recibe un numero correcto y un numero ingresado por el usuario, y devuelve True si son iguales, o devuelve False en caso de ser falso.\n

    Parametros:\n
    num_correcto(int): numero correcto que va en el sudoku.\n
    num_usuario(int): numero que ingreso por el usuario.\n
    
    Retorna True si son iguales, False en caso de no serlo.\n
    """
    if num_correcto == num_usuario:
        correcto = True
    else:
        correcto = False
    
    return correcto



def blit_sudoku (superficie: pygame.Surface, matriz_oculta: list, matriz_correcta:list, matriz_a_completar: list, porcentaje_pos_primera_celda, tamaño_celda: tuple, rect_colision: pygame.Surface, tamaño_num: int,  color_def: tuple, color_correcto: tuple, color_incorrecto: tuple) -> dict:
    """ 
    Esta funcion lo dibuja el tablero de sudoku en una superficie.\n
    parametros:\n
    superficie(pygame.Surface): superficie donde se dibuja el tablero.\n
    matriz_oculta(list): matriz con numeros ocultos del sudoku.\n
    matriz_correcta(list): matriz que contiene los numeros correctos del sudoku.\n
    matriz_a_completar(list): matriz donde se cargan los numeros ingresados por el usuario.\n
    porcentaje_pos_primera_celda(tuple): tupla con los porcentajes de posicion de la primera celda en X e Y.\n
    tamaño_celda(tuple): tupla con el tamaño de la celda en ancho y alto.\n
    rect_colision(pygame.Rect): celda donde se produce una colision.\n
    tamaño_num(int): tamaño del numero que se dibuja dentro de las celdas.\n
    color_def(tuple): color asignado para los numeros por defecto\n
    color_correcto(tuple): color asignado para los numeros ingresados correctamente\n
    color_incorrecto(tuple): color asignado para los numeros ingresados incorrectamente\n
    Retorna un diccionario con de los rects correspondientes a las celdas que estan ocultas. Las claves correspondes a las indices de las celdas.
    """
    
    porcentaje_x_primer_celda, porcentaje_y_primera_celda = porcentaje_pos_primera_celda
    ancho_celda, alto_celda = tamaño_celda
    diccionario_rect_celdas = {}
    rect_celda = crear_rect_posicion_especifica(superficie, porcentaje_x_primer_celda, porcentaje_y_primera_celda, tamaño_celda)
    posicion_en_x_columna_1 = rect_celda.x
        
    for i in range (len(matriz_a_completar)):
            
            if i != 0:
                rect_celda.y += alto_celda+1

            rect_celda.x = posicion_en_x_columna_1

            for j in range (len(matriz_a_completar[i])):

                if rect_celda == rect_colision:     
                    color_celda = (158, 200, 255)  
            
                else:                              
                    color_celda = (255, 255, 255)  

                pygame.draw.rect(superficie, color_celda, rect_celda)



                if matriz_oculta[i][j]  == "":
                    diccionario_rect_celdas[(i, j)] = rect_celda.copy()

                    numero_correcto = matriz_correcta[i][j]
                    numero_usuario = matriz_a_completar[i][j]

                    if definir_num_correcto(numero_correcto, numero_usuario) == True:
                        color_numero = color_correcto
                    else:
                        color_numero = color_incorrecto
                else:         
                    color_numero = color_def # AZUL 
                    
                superficie_numero = crear_superficie_texto("Showcard Gothic", tamaño_num, str(matriz_a_completar[i][j]), color_numero, superficie)
                posicion_numero = obtener_posicion_superficie_centrada(superficie_numero, rect_celda)
                superficie.blit(superficie_numero, posicion_numero)

                rect_celda.x += (ancho_celda+2)


    return diccionario_rect_celdas



def dibujar_boton_segun_colision (superficie: pygame.Surface, rect_boton: pygame.Rect, color_boton: tuple, colision: bool, texto: pygame.Surface, texto_colision: pygame.Surface, pos_texto: tuple) -> None:
        """ 
        Esta funcion dibuja un boton en una superficie, y si hay colision o no, cambia el color del borde y el texto que se muestra.\n
        Parametros:\n
        superficie(pygame.Surface): superficie donde se dibuja el boton.\n
        rect_boton(pygame.Rect): rectangulo donde se dibuja el boton.\n
        color_boton(tuple): color del boton.\n
        colision(bool): bandera que indica si hay colision o no.\n
        texto(pygame.Surface): texto que se muestra cuando no hay colision.\n
        texto_colision(pygame.Surface): texto que se muestra cuando hay colision.\n
        pos_texto(tuple): posicion del texto que se muestra.\n

        No tiene retorno.\n
        """
        alto_pantalla = superficie.get_height() 
        size_bordes = int(alto_pantalla * 1 / 100)
        size_radio = int(alto_pantalla * 3 / 100)

        if colision == False:
            pygame.draw.rect(superficie, color_boton, rect_boton, width = size_bordes, border_radius = size_radio)
            # superficie.blit(texto, pos_texto)
        else:
            pygame.draw.rect(superficie, color_boton, rect_boton, border_radius = size_radio)
            # superficie.blit(texto_colision, pos_texto)

        dibujar_txt_segun_colision(superficie, colision, texto, texto_colision, pos_texto)




def blitear_rankings(superficie: pygame.Surface, cantidad_top: int, lista_nombres: list, lista_puntajes: list, size_txt: int, pos_nombre_1: tuple, pos_puntaje_1: tuple, color: tuple, cantidad_pixeles_espaciado: int, ruta_txt: str) -> None:
    """ 
    Esta funcion dibuja los rankings en una superficie.\n
    Parametros:\n
    superficie(pygame.Surface): superficie donde se dibujan los rankings.\n
    cantidad_top(int): cantidad de jugadores que se muestran en el ranking.\n
    lista_nombres(list): lista con los nombres de los jugadores.\n
    lista_puntajes(list): lista con los puntajes de los jugadores.\n
    size_txt(int): tamaño del texto que se dibuja.\n
    pos_nombre_1(tuple): tupla con los porcentajes de posicion del nombre del primer jugador.\n
    pos_puntaje_1(tuple): tupla con los porcentajes de posicion del puntaje del primer jugador.\n
    color(tuple): color del texto que se dibuja.\n
    cantidad_pixeles_espaciado(int): cantidad de pixeles de espaciado entre los nombres y puntajes.\n
    ruta_txt(str): ruta de la fuente que se usa para dibujar el texto.\n
    No tiene retorno
    """
    lista_nombres_copia = lista_nombres.copy()
    lista_puntajes_copia = lista_puntajes.copy()

    for i in range (len(lista_puntajes_copia)):
        if lista_puntajes_copia[i] == 0:
            lista_nombres_copia.pop(i)
            lista_puntajes_copia.pop(i)

    ancho_superficie = superficie.get_width()
    rect_superficie = superficie.get_rect()
    porcentaje_x_nombre, porcentaje_y_nombre = pos_nombre_1
    porcentaje_x_puntaje, porcentaje_y_puntaje = pos_puntaje_1

    try:
        nombre_a_blitear = lista_nombres_copia[0]
        puntaje_a_blitear = lista_puntajes_copia[0]

        txt_nombre = crear_superficie_texto(ruta_txt, size_txt, nombre_a_blitear, color, superficie)
        pos_x_nombre, pos_y_nombre = obtener_posicion_superficie_centrada_en_x(txt_nombre, rect_superficie, porcentaje_y_nombre)
        pos_x_nombre = porcentaje_x_nombre * ancho_superficie // 100
        alto_nombre = txt_nombre.get_height()

        txt_puntaje = crear_superficie_texto(ruta_txt, size_txt, str(puntaje_a_blitear), color, superficie)
        pos_x_puntaje, pos_y_puntaje = obtener_posicion_superficie_centrada_en_x(txt_puntaje, rect_superficie, porcentaje_y_puntaje)
        pos_x_puntaje = porcentaje_x_puntaje * ancho_superficie // 100
        alto_puntaje = txt_puntaje.get_height()


        top = 0

        for i in range(cantidad_top):
            try:
                nombre_a_blitear = lista_nombres[i]
                puntaje_a_blitear = lista_puntajes[i]
                top = f"{i+1}.          "
            except: 
                nombre_a_blitear = ""
                puntaje_a_blitear = ""
                top = ""
            
            puntaje_a_blitear_str = str(puntaje_a_blitear)
            txt_nombre = crear_superficie_texto(ruta_txt, size_txt, f"{top}{nombre_a_blitear}", color, superficie)
            txt_puntaje = crear_superficie_texto(ruta_txt, size_txt, puntaje_a_blitear_str, color, superficie)

            if i != 0:
                pos_y_nombre += (alto_nombre + cantidad_pixeles_espaciado)
                pos_y_puntaje += (alto_puntaje + cantidad_pixeles_espaciado)

            superficie.blit(txt_nombre, (pos_x_nombre, pos_y_nombre))
            superficie.blit(txt_puntaje, (pos_x_puntaje, pos_y_puntaje))
            
    except:
        pass

        
    


def guardar_datos_jugador_en_lista(lista_puntajes, lista_nombres, nombre_jugador, puntaje_jugador) -> None:
    """ 
    Lo que hace esta funcion es guardar los datos del jugador en una lista con nombres y en una lista paralela con puntajes.\n
    Parametros:\n
    lista_puntajes: lista donde se guardan los puntajes de los jugadores.\n
    lista_nombres: lista donde se guardan los nombres de los jugadores.\n
    RNo tiene retorno.\n
    
    """
    nombre_jugador_minuscula = nombre_jugador.lower()

    if lista_nombres.count(nombre_jugador_minuscula) == 0:
        lista_nombres.append(nombre_jugador_minuscula)
        lista_puntajes.append(puntaje_jugador)
    else:
        indice_nombre_repetido = lista_nombres.index(nombre_jugador_minuscula)
        if lista_puntajes[indice_nombre_repetido] < puntaje_jugador:
            lista_nombres[indice_nombre_repetido] = nombre_jugador_minuscula
            lista_puntajes[indice_nombre_repetido] = puntaje_jugador
        


def invertir_bandera(bandera: bool) -> bool:
    """ 
    Esta funcion cambia el valor de una bandera, si es True pasa a False.\n
    Parametros:\n
    bandera: bool, que cambiaremos.\n
    Retorna el valor cambiado de la bandera.\n
    """
    
    if bandera == True:
        bandera = False
    else:
        bandera = True
    
    return bandera



def cargar_sonido(ruta: str, volumen: float) -> pygame.mixer.Sound:
    """ 
    Esta funcion carga un sonido desde una ruta especifica y se le asigna un volmen especifico\n
    Parametros:\n
    ruta(str): ruta del sonido que vamos a cargar.\n
    volumen(float): valor entre 0 y 1 que representa el volumen del sonido.\n
    Retorna el sonido que cargamos.\n
    """
    sonido = pygame.mixer.Sound(ruta)
    sonido.set_volume(volumen)

    return sonido


def generar_matrices_juego(dificultad: str) -> tuple:
    """ 
    Esta funcion genera las matrices del juego de sudoku.\n

    Parametros:\n
    dificultad(str): dificultad del juego, puede ser Facil, Intermedio o Dificil.\n
    
    Retorna una tupla con tres matrices:\n
    matriz_oculta(list): matriz con numeros ocultos del sudoku.\n
    matriz_sudoku(list): matriz que contiene los numeros correctos del sudoku.\n
    matriz_a_completar(list): matriz donde se cargan los numeros ingresados por el usuario.\n

    """
    matriz_sudoku = crear_matriz(9,9, None)
    cargar_matriz_sudoku(matriz_sudoku)
    matriz_a_completar = ocultar_matriz(matriz_sudoku, dificultad)
    matriz_oculta = deepcopy(matriz_a_completar)

    return matriz_sudoku, matriz_a_completar, matriz_oculta


def validar_char_alfanumerico(caracter: str) -> str | None:
    """ 
    Esta funcion valida si un caracter es alfanumerico (si es una letra o un numero).\n
    
    Parametros:\n
    caracter(str): caracter que validaremos.\n
    
    Retorna el caracter si es alfanumerico, o None en caso de no serlo.

    """   
    validacion = False

    if (caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z") or (caracter >= "1" and caracter <= "9"):
        validacion = True
    
    if validacion == False:
        caracter = None

    return caracter


def crear_rect(superficie: pygame.Surface, posicion: tuple, size: tuple) -> pygame.Rect:
    """ 
    Esta funcion crea un rectangulo con una posicion especifica y un tamaño especifica sobre una superficie.\n
    Parametros:\n
    superficie(pygame.Surface): superficie donde se dibuja el rectangulo.\n
    posicion(tuple): tupla con la posicion del rectangulo en X e Y.\n
    size(tuple): tupla con el tamaño del rectangulo en ancho y alto.\n

    Retorna: (pygame.Rect) con la posicion y tamaño del rectangulo.\n
    """
    pos_rect_x, pos_rect_y = posicion
    pos_rect_x, pos_rect_y = calcular_posicion_objeto(superficie, pos_rect_x, pos_rect_y)

    size_w, size_h = size
    size_w, size_h = calcular_tamaño_rect(superficie, size_w, size_h)

    rect = pygame.Rect(pos_rect_x, pos_rect_y, size_w, size_h)

    return rect


def crear_rect_posicion_especifica (pantalla: pygame.Surface, porcentaje_altura: int, porcentaje_ancho: int, tamaño_rect: tuple) -> pygame.Rect: 
    """   
    Crea un rect y lo ubica en una posicion especifica en X e Y, sobre una superficie.
    parametros:\n
    pantalla(pygame.Surface): superficie donde se crea el rectangulo.\n
    porcentaje_altura(int): porcentaje de la altura de la superficie que representa la posicion Y del rectangulo.\n
    porcentaje_ancho(int): porcentaje del ancho de la superficie que representa la posicion X del rectangulo.\n
    tamaño_rect(tuple): tupla con el tamaño del rectangulo en ancho y alto.\n

    Retorna: (pygame.Rect) con la posicion y tamaño del rectangulo.\n
    
    """
    ancho_pantalla = pantalla.get_width() 
    alto_pantalla = pantalla.get_height() 
    posicion_rect_y = porcentaje_altura * alto_pantalla / 100
    posicion_rect_x = porcentaje_ancho * ancho_pantalla / 100
    ancho_rect, alto_rect = tamaño_rect
    rect = pygame.Rect(posicion_rect_x, posicion_rect_y, ancho_rect, alto_rect)
    

    return rect



def calcular_posicion_objeto(superficie: pygame.Surface, constante_pos_x: int,  constante_pos_y: int)-> tuple:
    """
    "Esta funcion calcula la posicion de un objeto en base a un porcentaje de la superficie.\n

    Parametros:\n
    superficie(pygame.Surface): superficie donde se dibuja el rectangulo.\n
    constante_pos_x(int): porcentaje del ancho de la superficie que representa la posicion X del rectangulo.\n
    constante_pos_y(int): porcentaje del alto de la superficie que representa la posicion Y del rectangulo.\n

    Retorna una tupla con la posicion X e Y del rectangulo.\n
    """
    ancho_superficie = superficie.get_width()
    alto_superficie = superficie.get_height()

    pos_rect_x = ancho_superficie * constante_pos_x / 100 
    pos_rect_y = alto_superficie * constante_pos_y / 100 
    return pos_rect_x, pos_rect_y



def calcular_tamaño_rect(superficie: pygame.Surface, constante_size_w: int,  constante_size_h: int) -> tuple:
    """
    Esta funcion calcula el tamaño de un rectangulo en base a un porcentaje de la superficie.\n
    
    Parametros:\n
    superficie(pygame.Surface): superficie donde se dibuja el rectangulo.\n
    constante_size_w(int): porcentaje del ancho de la superficie que representa el ancho del rectangulo.\n
    constante_size_h(int): porcentaje del alto de la superficie que representa el alto del rectangulo.\n
    
    Retorna una tupla con el ancho y alto del rectangulo.\n
    """
    ancho_superficie = superficie.get_width()
    alto_superficie = superficie.get_height()
    size_w = ancho_superficie * constante_size_w / 100
    size_h = alto_superficie * constante_size_h / 100

    return size_w, size_h


def ordenar_jugadores(lista_puntajes:list, lista_nombres:list, criterio:str) -> None:
    """
    Esta funcion ordena dos listas de jugadores y sus puntajes en base al criterio.\n

    Parametros:\n
    lista_puntajes(list): lista con los puntajes de los jugadores.\n
    lista_nombres(list): lista con los nombres de los jugadores.\n
    criterio(str): criterio de ordenamiento, puede ser "ASC" para ascendente o "DSC" para descendente.\n

    No tiene retorno.\n
    """
    for i in range(len(lista_puntajes) - 1):
        for j in range(i + 1, len(lista_puntajes)):
            if (lista_puntajes[i] > lista_puntajes[j] and criterio == "ASC") or (lista_puntajes[i] < lista_puntajes[j] and criterio == "DSC"):
                aux = lista_puntajes[i]
                lista_puntajes[i] = lista_puntajes[j]
                lista_puntajes[j] = aux

                aux = lista_nombres[i]
                lista_nombres[i] = lista_nombres[j]
                lista_nombres[j] = aux



def guardar_datos_en_csv (lista_nombres, lista_puntajes) -> None:
    """ 
    Esta funcion guarda los nombres y puntajes de los jugadores en un archivo CSV.\n
    Parametros:\n
    lista_nombres(list): lista con los nombres de los jugadores.\n
    lista_puntajes(list): lista con los puntajes de los jugadores.\n
    
    Retorna nada.\n
    """
    jugadores = ""

    for i in range (len(lista_nombres)):
        jugadores += f"{lista_nombres[i]}, {lista_puntajes[i]}\n"

    with open("puntajes.csv", "w") as archivo:
        archivo.write(jugadores)





def calcular_celdas_a_ocultar(dificultad: str, matriz: list) -> int:
    """
    Esta funcion calcula la cantidad de celdas que se van a ocultar en una matriz de sudoku segun la dificultad.\n

    parametros:\n
    dificultad(str): dificultad del juego, puede ser "Facil", "Intermedio" o "Dificil".\n
    matriz(list): matriz de sudoku que se va a ocultar.\n

    Retorna:(int)entero con la cantidad de celdas a ocultar.\n
    """
    cantidad_celdas = 0
    match dificultad:
        case "Facil":
            porcentaje_nums_a_ocultar = 25
        case "Intermedio":
            porcentaje_nums_a_ocultar = 45
        case "Dificil":
            porcentaje_nums_a_ocultar = 60

    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            cantidad_celdas += 1

    cant_num_ocultar = cantidad_celdas * porcentaje_nums_a_ocultar // 100


    return cant_num_ocultar



def ocultar_matriz(matriz: list, dificultad: str) -> list:
    """
    
    Esta funcion oculta numeros de una matriz de sudoku segun la dificultad.\n
    parametros:\n
    matriz(list): matriz de sudoku que se va a ocultar.\n
    dificultad(str): dificultad del juego, puede ser "Facil", "Intermedio" o "Dificil".\n
    Retorna una matriz con los numeros ocultos.\n
    
    """
    contador = 0
    matriz_copia = copy(deepcopy(matriz))

    cant_num_ocultar = calcular_celdas_a_ocultar(dificultad, matriz)
    cant_num_ocultar_submatriz = cant_num_ocultar // 9 


    for i in range (0, 9, 3):

        for j in range (0, 9, 3):
            while contador < cant_num_ocultar_submatriz:
                i_fila_random = randint(i, i+2)
                i_columna_random = randint(j, j+2) 

                if  matriz_copia[i_fila_random][i_columna_random] != "":
                    matriz_copia[i_fila_random][i_columna_random] = ""
                    contador += 1

            contador = 0

    return matriz_copia
    




def crear_superficie_texto (ruta: str, porcentaje_tamaño: int, texto: str, color_texto: tuple, superficie: pygame.Surface, negrita: bool = False, cursiva: bool = False, sombra: bool = False) -> pygame.Surface:
    """ 
    Carga una fuente y crea un texto

    Parametros:\n
    ruta(str): ruta de la fuente que se va a cargar.\n
    porcentaje_tamaño(int): porcentaje del alto de la superficie que representa el tamaño del texto.\n
    texto(str): texto que se va a mostrar.\n
    color_texto(tuple): tupla con el color del texto en formato RGB.\n
    superficie(pygame.Surface): superficie donde se dibuja el texto.\n
    negrita(bool): bandera que indica si el texto es negrita o no.\n
    cursiva(bool): bandera que indica si el texto es cursiva o no.\n
    sombra(bool): bandera que indica si se dibuja una sombra al texto o no.\n
    
    Retorna una superficie con el texto renderizado.\n
    """
    alto_superficie = superficie.get_height()
    size_txt = int(alto_superficie * porcentaje_tamaño / 100)
    ruta = pygame.font.SysFont(ruta, size_txt, negrita, cursiva)
    superficie_texto = ruta.render(texto, True, color_texto)

    
    if sombra == False:
        return superficie_texto
    else:
        superficie_sombra = ruta.render(texto, True, (0, 0, 0))
        return superficie_texto, superficie_sombra





def blit_texto_con_sombra (superficie: pygame.Surface, texto: pygame.Surface, sombra: pygame.Surface, posicion) -> None:
        """ Esta funcion dibuja un texto con una sombra en una superficie.\n

        Parametros:\n
        superficie(pygame.Surface): superficie donde se dibuja el texto.\n
        texto(pygame.Surface): superficie que contiene el texto a dibujar.\n
        sombra(pygame.Surface): superficie que contiene la sombra del texto.\n
        posicion(tuple): tupla con las coordenadas X e Y donde se dibuja el texto.\n

        Retorna nada.\n
        """
        posicion_x, posicion_y = posicion
        superficie.blit(sombra, (posicion_x+3, posicion_y+3))
        superficie.blit(texto, posicion)





def obtener_posicion_superficie_centrada (superficie: pygame.Surface, rect: pygame.Rect) -> tuple:
    """ 
    Obtiene las coordenadas donde una superficie queda centrada en un rect 

    Parametros:\n
    superficie(pygame.Surface): superficie que se centra en el rect.\n
    rect(pygame.Rect): rectangulo donde se centra la superficie.\n

    Retorna: tupla con las coordenadas X e Y de la superficie centrada.\n
    """
    pos_superficie_x = rect.centerx - superficie.get_width() / 2
    pos_superficie_y = rect.centery - superficie.get_height() / 2

    return pos_superficie_x, pos_superficie_y




def obtener_posicion_superficie_centrada_en_x (superficie: pygame.Surface, rect: pygame.Rect, porcentaje_y) -> tuple:
    """ 
    Obtiene las coordeandas donde una superficie queda centrada en un rect pero solo en X, la posicion en Y va por parametros

    Parametros:\n
    superficie(pygame.Surface): superficie que se centra en X.\n
    rect(pygame.Rect): rectangulo donde se centra la superficie.\n
    porcentaje_y(int): porcentaje de la altura del rectangulo que representa la posicion Y de la superficie.\n

    Retorna: tupla con las coordenadas X e Y de la superficie centrada en X.\n
    """
    centro_superficie = superficie.get_width() / 2
    pos_superficie_x = rect.centerx - centro_superficie
    pos_superficie_y = porcentaje_y * rect.height / 100

    return pos_superficie_x, pos_superficie_y



def dibujar_txt_segun_colision (superficie: pygame.Surface, colision: bool, texto: pygame.Surface, texto_colision: pygame.Surface, pos_texto: tuple) -> None:
        """ 
        Esta funcion dibuja un texto en una superficie, y si hay colision o no, cambia el texto que se muestra.\n   

        Parametros:\n
        superficie(pygame.Surface): superficie donde se dibuja el texto.\n
        colision(bool): bandera que indica si hay colision o no.\n
        texto(pygame.Surface): texto que se muestra cuando no hay colision.\n
        texto_colision(pygame.Surface): texto que se muestra cuando hay colision.\n
        pos_texto(tuple): posicion del texto que se muestra.\n

        Retorna nada.\n
        
        """
        if colision == False:
            superficie.blit(texto, pos_texto)
        else:
            superficie.blit(texto_colision, pos_texto)







def calcular_puntaje(dificultad: str, minutos: int, segundos: int, cant_errores: int)-> int:
    """
    Esta funcion calcula el puntaje final del jugador en base a la dificultad, el tiempo y la cantidad de errores que haya cometido el jugador.\n

    Parametros:\n
    dificultad(str): dificultad del juego, puede ser Facil, Intermedio o Dificil.\n
    minutos(int): cantidad de minutos que tardó.\n
    segundos(int): cantidad de segundos que tardó.\n
    cant_errores(int): cantidad de errores cometidos por el jugador.\n

    Retorna el puntaje final del jugador.\n
    
    """
    segundos = (minutos * 60) + segundos
    
    match dificultad:
        case "Facil":
            puntos_por_dif = 2000
            puntos_por_error = 200
            
        case "Intermedio":
            puntos_por_dif = 4000
            puntos_por_error = 150
        case "Dificil":
            puntos_por_dif = 6000
            puntos_por_error = 100
    puntos_por_seg = 1

    puntaje_final = puntos_por_dif - (cant_errores * puntos_por_error)  - (puntos_por_seg * segundos)

    if puntaje_final < 0:
        puntaje_final = 0

    return puntaje_final