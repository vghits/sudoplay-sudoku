import pygame
from constantes import *
from funciones import *
import copy

pygame.init()

#CREACION DE VENTANA
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("SudoPlay GAME")


#!!!!!!!!!!!!!!!!!!!!!!! BANDERAS !!!!!!!!!!!!!!!!!!!!!!
colision_jugar = False
colision_puntaje = False
colision_dificultad = False
colision_salir = False
bandera_musica = False
colision_celda = False
bandera_titilado = False
seleccion_activa = False
matriz_generada = True
reinicio = False

#!!!!!!!!!!!!!!!!!!!!!!! CONTADORES !!!!!!!!!!!!!!!!!!!!!
contador_dificultad = 0
contador_segundos = 0
contador_minutos = 0
contador_errores = 0
#!!!!!!!!!!!!!!!!!!!!!!! OTROS !!!!!!!!!!!!!!!!!!!!!
pantalla_actual = 1
numero_bliteo = ""
diccionario_rect_celdas = {}
rect_donde_colisiona = None
dificultad_seleccionada = "Facil"
username = ""
pos_txt_user_ingresado = None
lista_nombres = []
lista_puntajes = []


#? FONDO
ancho_pantalla = pantalla.get_width() 
alto_pantalla = pantalla.get_height() 
imagen_fondo = pygame.image.load("fondo_violeta.png").convert_alpha()
imagen_fondo_escalada = pygame.transform.scale(imagen_fondo, (ancho_pantalla, alto_pantalla))

#!!!!!!!!!!!!!!!!!!!!!!! RECTS MENU !!!!!!!!!!!!!!!!!!!!!

rect_boton_jugar = crear_rect_centrado_en_x(pantalla, PORCENTAJE_BOTON_JUGAR_Y, (SIZE_BOT_MENU_W, SIZE_BOT_MENU_H))
rect_boton_ranking = crear_rect_centrado_en_x(pantalla, PORCENTAJE_BOTON_PUNTAJE_Y, (SIZE_BOT_MENU_W, SIZE_BOT_MENU_H))
rect_boton_dificultad = crear_rect_centrado_en_x(pantalla, PORCENTAJE_BOTON_DIFICULTAD_Y, (SIZE_BOT_MENU_W, SIZE_BOT_MENU_H))
rect_boton_salir = crear_rect_centrado_en_x(pantalla, PORCENTAJE_BOTON_SALIR_Y, (SIZE_BOT_MENU_W, SIZE_BOT_MENU_H))


##################################################################################################################################

#!!!!!!!!!!!!!!!!!!!!!!! RECTS PANTALLA DEL JUEGO !!!!!!!!!!!!!!!!!!!!!

rect_blanco = crear_rect(pantalla, (POSICION_RECT_BLANCO_X, POSICION_RECT_BLANCO_Y), (SIZE_RECT_BLANCO_W, SIZE_RECT_BLANCO_H))
rect_boton_home = crear_rect(pantalla, (PORCENTAJE_BOTON_HOME_X, PORCENTAJE_BOTONES_SUDO_Y), (SIZE_W_BOTONES_JUEGO, SIZE_H_BOTONES_JUEGO))

rect_boton_reiniciar = crear_rect(pantalla, (PORCENTAJE_BOTON_REINICIAR_X, PORCENTAJE_BOTONES_SUDO_Y), (SIZE_W_BOTONES_JUEGO, SIZE_H_BOTONES_JUEGO))
rect_timer = crear_rect(pantalla, (PORCENTAJE_TIM_ERR_X, PORCENTAJE_TIMER_Y), (SIZE_W_TIM_ERR, SIZE_H_TIM_ERR))
rect_errores = crear_rect(pantalla, (PORCENTAJE_TIM_ERR_X, PORCENTAJE_ERRORES_Y), (SIZE_W_TIM_ERR, SIZE_H_TIM_ERR))

size_espaciado_top = int(alto_pantalla * SIZE_ESPACIADO_RANKING / 100)
#!!!!!!!!!!!!!!!!!!!!!!! RECTS PANTALLA VICTORIA !!!!!!!!!!!!!!!!!!!!!

rect_victoria = crear_rect_centrado_en_x(pantalla, PORCENTAJE_Y_GANADOR, (SIZE_W_GANADOR, SIZE_H_GANADOR))
rect_username = crear_rect_centrado_en_x(pantalla, PORCENTAJE_Y_USER, (SIZE_W_USER, SIZE_H_USER))

#!!!!!!!!!!!!!!!!!!!!!!! RECTS PANTALLA RANKING !!!!!!!!!!!!!!!!!!!!!

rect_rankings = crear_rect_centrado_en_x(pantalla, PORCENTAJE_Y_RANKING, (SIZE_W_RANKING, SIZE_H_RANKING))
rect_volver = crear_rect(pantalla, (PORCENTAJE_X_VOLVER, PORCENTAJE_Y_VOLVER), (SIZE_W_RECT_VOLVER, SIZE_H_RECT_VOLVER))

##############################################################################!

#!!!!!!!!!!!!!!!!!!!!!!! IMAGENES PANTALLA DEL JUEGO !!!!!!!!!!!!!!!!!!!!!!!!

imagen_home = cargar_escalar_imagen("home.png", SIZE_H_IMAGENES_JUEGO, pantalla)
pos_home_x, pos_home_y = obtener_posicion_superficie_centrada(imagen_home, rect_boton_home)

imagen_reiniciar = cargar_escalar_imagen("reiniciar.png", SIZE_H_IMAGENES_JUEGO, pantalla)
pos_reiniciar_x, pos_reiniciar_y = obtener_posicion_superficie_centrada(imagen_reiniciar, rect_boton_reiniciar)

imagen_volver_ranking = cargar_escalar_imagen("simbolo_x.png", SIZE_H_VOLVER_RANKING, pantalla)
pos_x_volver_ranking, pos_y_volver_ranking = obtener_posicion_superficie_centrada(imagen_volver_ranking, rect_volver)


#!!!!!!!!!!!!!!!!!!!!!!! TEXTOS PARA TITULOS !!!!!!!!!!!!!!!!!!!!!!

rect_pantalla = pantalla.get_rect()

txt_titulo, sombra_txt_titulo = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TITULO, "SudoPlay", CELESTE_CLARO, pantalla, sombra = True)
pos_txt_titulo = obtener_posicion_superficie_centrada_en_x(txt_titulo, rect_pantalla, PORCENTAJE_TITULO)

texto_enter, sombra_txt_enter = crear_superficie_texto("Showcard Gothic", SIZE_TXT_ENTER, "Presione ENTER para iniciar", CELESTE_CLARO, pantalla, sombra = True)
pos_txt_enter = obtener_posicion_superficie_centrada_en_x(texto_enter, rect_pantalla, PORCENTAJE_INICIAR)

txt_titulo_menu, sombra_txt_tit_menu = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TITULO_MENU, "SudoPlay", CELESTE_CLARO, pantalla, sombra = True)
pos_txt_tit_menu = obtener_posicion_superficie_centrada_en_x(txt_titulo_menu, rect_pantalla, PORCENTAJE_TITULO_MENU)

txt_version = crear_superficie_texto("Arial", SIZE_TXT_VERSION, "Versión 0.0.1", BLANCO, pantalla, True, True)
txt_version_y = alto_pantalla - txt_version.get_height()
pos_txt_version = (0, txt_version_y)

size_radio_blanco = int(alto_pantalla * PORCENTAJE_RADIO_BLANCO / 100)
size_radio_botones = int(alto_pantalla * PORCENTAJE_RADIO_BOTONES / 100)
size_bordes_botones = int(alto_pantalla * PORCENTAJE_BORDES / 100)
size_radio_boton_volver_ranking = int(alto_pantalla * PORCENTAJE_BORDES / 100)

txt_ranking, txt_ranking_sombra = crear_superficie_texto("Showcard Gothic", SIZE_TXT_RANKING, "RANKING", AZUL, pantalla,  sombra = True)
pos_txt_ranking = obtener_posicion_superficie_centrada_en_x(txt_ranking, rect_pantalla, PORCENTAJE_Y_TXT_RANKING)



#!!!!!!!!!!!!!!!!!!!!!!! TEXTOS PARA BOTONES O RECTS !!!!!!!!!!!!!!!!!!!!!!

texto_jugar = crear_superficie_texto("Showcard Gothic", SIZE_TXTS_MENU, "JUGAR", CELESTE_CLARO, pantalla)
texto_jugar_oscuro = crear_superficie_texto("Showcard Gothic", SIZE_TXTS_MENU, "JUGAR", AZUL, pantalla)
posicion_texto_jugar = obtener_posicion_superficie_centrada(texto_jugar, rect_boton_jugar)

texto_ranking = crear_superficie_texto("Showcard Gothic", SIZE_TXTS_MENU, "RANKING", CELESTE_CLARO, pantalla)
texto_ranking_oscuro = crear_superficie_texto("Showcard Gothic", SIZE_TXTS_MENU, "RANKING", AZUL, pantalla)
posicion_texto_puntaje = obtener_posicion_superficie_centrada(texto_ranking_oscuro, rect_boton_ranking)

texto_salir = crear_superficie_texto("Showcard Gothic", SIZE_TXTS_MENU, "SALIR", CELESTE_CLARO, pantalla)
texto_salir_oscuro = crear_superficie_texto("Showcard Gothic", SIZE_TXTS_MENU, "SALIR", AZUL, pantalla)
posicion_texto_salir = obtener_posicion_superficie_centrada(texto_salir_oscuro, rect_boton_salir)

texto_dificultad = crear_superficie_texto("Showcard Gothic", SIZE_TXT_DIFICULTAD, "DIFICULTAD", CELESTE_CLARO, pantalla)
texto_dificultad_oscuro = crear_superficie_texto("Showcard Gothic", SIZE_TXT_DIFICULTAD, "DIFICULTAD", AZUL, pantalla)
texto_dificultad_x, texto_dificultad_y = obtener_posicion_superficie_centrada(texto_dificultad_oscuro, rect_boton_dificultad)
texto_dificultad_y = rect_boton_dificultad.centery - texto_dificultad.get_height()
posicion_texto_dificultad = (texto_dificultad_x, texto_dificultad_y)

txt_facil = crear_superficie_texto("Showcard Gothic", SIZE_TXT_DIFICULTAD, "Fácil", CELESTE_CLARO, pantalla)
txt_facil_oscuro = crear_superficie_texto("Showcard Gothic", SIZE_TXT_DIFICULTAD, "Fácil", AZUL, pantalla)
posicion_txt_facil = obtener_posicion_superficie_centrada_en_x(txt_facil, rect_pantalla, PORCENTAJE_Y_NIVELES)


txt_intermedio = crear_superficie_texto("Showcard Gothic", SIZE_TXT_DIFICULTAD, "Intermedio", CELESTE_CLARO, pantalla)
txt_intermedio_oscuro = crear_superficie_texto("Showcard Gothic", SIZE_TXT_DIFICULTAD, "Intermedio", AZUL, pantalla)
posicion_txt_intermedio = obtener_posicion_superficie_centrada_en_x(txt_intermedio, rect_pantalla, PORCENTAJE_Y_NIVELES)


txt_dificil = crear_superficie_texto("Showcard Gothic", SIZE_TXT_DIFICULTAD, "Difícil", CELESTE_CLARO, pantalla)
txt_dificil_oscuro = crear_superficie_texto("Showcard Gothic", SIZE_TXT_DIFICULTAD, "Difícil", AZUL, pantalla)
posicion_txt_dificil = obtener_posicion_superficie_centrada_en_x(txt_dificil, rect_pantalla, PORCENTAJE_Y_NIVELES)

txt_timer = crear_txt_timer(pantalla, contador_segundos, contador_minutos, SIZE_TXT_TIM_ERR, AZUL_OSCURO)
post_txt_tiempo_x, post_txt_tiempo_y = obtener_posicion_superficie_centrada(txt_timer, rect_timer) 

txt_errores = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TIM_ERR, f"ERRORES | {contador_errores}", AZUL_OSCURO, pantalla)
pos_errores_x, pos_errores_y = obtener_posicion_superficie_centrada(txt_errores, rect_errores)

txt_win = crear_superficie_texto("Showcard Gothic", SIZE_TXT_WIN, "! VICTORIA !", AZUL, pantalla)
posicion_txt_win = obtener_posicion_superficie_centrada_en_x(txt_win, rect_pantalla, PORCENTAJE_WIN)

txt_nick = crear_superficie_texto("Showcard Gothic", SIZE_TXT_NICK, "Ingresa tu nickname", AZUL, pantalla)
posicion_txt_nick = obtener_posicion_superficie_centrada_en_x(txt_nick, rect_pantalla, 38)

txt_user_ingresado = crear_superficie_texto("Showcard Gothic", SIZE_TXT_NICK, "", NEGRO, pantalla)

txt_top = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TOP_NOM_PUNT, "TOP", AZUL, pantalla)
pos_x_top, pos_y_top = calcular_posicion_objeto(pantalla, PORCENTAJE_X_TOP, PORCENTAJE_Y_TOP_NOM_PUNT)

txt_nombre = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TOP_NOM_PUNT, "NOMBRE", AZUL, pantalla)
pos_x_nombre, pos_y_nombre = calcular_posicion_objeto(pantalla, PORCENTAJE_X_NOMBRE_RANKING, PORCENTAJE_Y_TOP_NOM_PUNT)

txt_puntaje = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TOP_NOM_PUNT, "PUNTAJE", AZUL, pantalla)
pos_x_puntaje, pos_y_puntaje = calcular_posicion_objeto(pantalla, PORCENTAJE_X_TU_PUNTAJE, PORCENTAJE_Y_TOP_NOM_PUNT)

txt_tu_puntaje = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TU_PUNTAJE, "", AZUL, pantalla)
pos_x_tu_puntaje, pos_y_tu_puntaje = obtener_posicion_superficie_centrada_en_x(txt_tu_puntaje, rect_pantalla, PORCENTAJE_Y_PUNTAJE_MOSTRADO) 



#!!!!!!!!!!!!!!!!!!!!!!! MUSICA  !!!!!!!!!!!!!!!!!!!!!!
pygame.mixer.music.load("musica_fondo.mp3")
pygame.mixer.music.set_volume(0.6)

#!!!!!!!!!!!!!!!!!!!!!!! SONIDOS  !!!!!!!!!!!!!!!!!!!!!!
sonido_seleccion = cargar_sonido("sonido_seleccion.mp3", 0.2)
sonido_correcto = cargar_sonido("efecto-de-sonido-respuesta-correcta_8jHRRKoD.mp3", 0.2)
sonido_victoria = cargar_sonido("sonido_victoria.mp3", 0.9)
sonido_tipeo = cargar_sonido("sonido_apretar_tecla.mp3", 0.7)

#!!!!!!!!!!!!!!!!!!!!!!! EVENTOS PROPIOS !!!!!!!!!!!!!!!!!!!!!
evento_titilado = pygame.USEREVENT + 1
pygame.time.set_timer(evento_titilado, 350)

evento_timer = pygame.USEREVENT + 2
pygame.time.set_timer(evento_timer, 1000)



while True:
    # TEXTOS ACTUALIZABLES
    txt_errores = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TIM_ERR, f"ERRORES | {contador_errores}", AZUL_OSCURO, pantalla)
    txt_timer = crear_txt_timer(pantalla, contador_segundos, contador_minutos, SIZE_TXT_TIM_ERR, AZUL_OSCURO)
    txt_user_ingresado = crear_superficie_texto("Showcard Gothic", SIZE_TXT_USER_INGRE, f"{username}", NEGRO, pantalla)
    pos_txt_user_ingresado = obtener_posicion_superficie_centrada(txt_user_ingresado, rect_username)
    
    # FONDO 
    pantalla.blit(imagen_fondo_escalada, (0, 0))
    pantalla.blit(txt_version, pos_txt_version)
    
    # GENERACION MATRIZ

    # MUSICA
    if bandera_musica == False:
        pygame.mixer.music.play(-1)
        bandera_musica = True

    # EVENTOS
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        if pantalla_actual == 1:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    sonido_seleccion.play()
                    pantalla_actual = 2

            if evento.type == evento_titilado:
                bandera_titilado = invertir_bandera(bandera_titilado)


        elif pantalla_actual == 2:


            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    
                    if rect_boton_jugar.collidepoint(evento.pos) == True:
                        sonido_seleccion.play()
                        pantalla_actual = 3
                        pygame.mixer.music.stop()
                        matriz_generada = False

                    elif rect_boton_salir.collidepoint(evento.pos) == True:
                        pygame.quit()
                        quit()

                    elif rect_boton_dificultad.collidepoint(evento.pos) == True:
                        contador_dificultad += 1
                        matriz_generada = False
                        sonido_seleccion.play()

                        if contador_dificultad > 2:
                            contador_dificultad = 0

                        match contador_dificultad:
                            case 0:
                                dificultad_seleccionada = "Facil"
                            case 1:
                                dificultad_seleccionada = "Intermedio"
                            case 2: 
                                dificultad_seleccionada = "Dificil"

                    elif rect_boton_ranking.collidepoint(evento.pos) == True:
                        sonido_seleccion.play()
                        ordenar_jugadores(lista_puntajes, lista_nombres, "DSC")
                        pantalla_actual = 5



            mouse_pos = pygame.mouse.get_pos()
            colision_jugar = rect_boton_jugar.collidepoint(mouse_pos)
            colision_puntaje = rect_boton_ranking.collidepoint(mouse_pos)
            colision_dificultad = rect_boton_dificultad.collidepoint(mouse_pos)
            colision_salir = rect_boton_salir.collidepoint(mouse_pos)


        elif pantalla_actual == 3:


            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if rect_boton_home.collidepoint(evento.pos) == True:
                        sonido_seleccion.play()
                        pantalla_actual = 2
                        bandera_musica = False                            
                    if rect_boton_reiniciar.collidepoint(evento.pos) == True or rect_boton_home.collidepoint(evento.pos) == True:
                        sonido_seleccion.play()
                        matriz_generada = False
                        contador_segundos = 0
                        contador_minutos = 0
                        contador_errores = 0
                        numero_bliteo = ""
                        fila_colision = None
                        columna_colision = None
                        rect_donde_colisiona = None
                        seleccion_activa = False
                        colision_celda = False

                    items_diccionario_rect_celdas = diccionario_rect_celdas.items()
                    for item in items_diccionario_rect_celdas:
                        colision_celda = item[1].collidepoint(evento.pos)
                        if colision_celda == True:
                            fila_colision, columna_colision = item[0]
                            rect_donde_colisiona = item[1]
                            numero_bliteo = matriz_a_completar[fila_colision][columna_colision]        
                            seleccion_activa = True
                            break                                
                        else:
                            rect_donde_colisiona = None
                            seleccion_activa = False

            if seleccion_activa == True:
                if evento.type == pygame.KEYDOWN:
                    match evento.key:
                        case pygame.K_DELETE | pygame.K_BACKSPACE:
                            numero_bliteo = ""
                        case _:
                            if evento.unicode >= chr(49) and evento.unicode <= chr(57):
                                numero_bliteo = int(evento.unicode)
                                if definir_num_correcto(matriz_sudoku[fila_colision][columna_colision], numero_bliteo) == False:
                                    contador_errores += 1
                                else:
                                    sonido_correcto.play()     

            if evento.type == evento_timer:
                contador_segundos += 1
                if contador_segundos == 60:
                    contador_minutos += 1
                    contador_segundos = 0

        elif pantalla_actual == 4:
            if evento.type == pygame.KEYDOWN:
                sonido_tipeo.play()
                if evento.key == pygame.K_RETURN:
                    if len(username) >= 3:
                        guardar_datos_jugador_en_lista(lista_puntajes, lista_nombres, username, puntaje_final)
                        guardar_datos_en_csv(lista_nombres, lista_puntajes)
                        pantalla_actual = 2
                        bandera_musica = False
                        username = ""
                        contador_segundos = 0
                        contador_minutos = 0
                        contador_errores = 0
                        puntaje_final = 0

                elif evento.key == pygame.K_BACKSPACE:
                    username = username[0:-1]
                else:
                    if len(username) < 15:
                        if validar_char_alfanumerico(evento.unicode) != None:
                            username += evento.unicode
            
        elif pantalla_actual == 5:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if rect_volver.collidepoint(evento.pos) == True:
                        sonido_seleccion.play()
                        pantalla_actual = 2
                

    if matriz_generada == False:
        matriz_sudoku, matriz_a_completar, matriz_oculta = generar_matrices_juego(dificultad_seleccionada)
        matriz_generada = True
        


    if pantalla_actual == 1:
        blit_texto_con_sombra(pantalla, txt_titulo, sombra_txt_titulo, pos_txt_titulo)
        
        if bandera_titilado == True:
            blit_texto_con_sombra(pantalla, texto_enter, sombra_txt_enter, pos_txt_enter)

    elif pantalla_actual == 2:
        blit_texto_con_sombra(pantalla, txt_titulo_menu, sombra_txt_tit_menu, pos_txt_tit_menu)

        dibujar_boton_segun_colision(pantalla, rect_boton_jugar, CELESTE_CLARO, colision_jugar, texto_jugar, texto_jugar_oscuro, posicion_texto_jugar)
        dibujar_boton_segun_colision(pantalla, rect_boton_ranking, CELESTE_CLARO, colision_puntaje, texto_ranking, texto_ranking_oscuro, posicion_texto_puntaje)
        dibujar_boton_segun_colision(pantalla, rect_boton_dificultad, CELESTE_CLARO, colision_dificultad, texto_dificultad, texto_dificultad_oscuro, posicion_texto_dificultad)
        dibujar_boton_segun_colision(pantalla, rect_boton_salir, CELESTE_CLARO, colision_salir, texto_salir, texto_salir_oscuro, posicion_texto_salir)


        match dificultad_seleccionada:
            case "Facil":
                dibujar_txt_segun_colision(pantalla, colision_dificultad, txt_facil, txt_facil_oscuro, posicion_txt_facil)

            case "Intermedio":
                dibujar_txt_segun_colision(pantalla, colision_dificultad, txt_intermedio, txt_intermedio_oscuro, posicion_txt_intermedio)

            case "Dificil":
                dibujar_txt_segun_colision(pantalla, colision_dificultad, txt_dificil, txt_dificil_oscuro, posicion_txt_dificil)



        
    elif pantalla_actual == 3:
        pygame.draw.rect(pantalla, BLANCO, rect_blanco, border_radius = size_radio_blanco)

        pygame.draw.rect(pantalla, GRIS, rect_boton_home, border_radius = size_radio_botones)
        pantalla.blit(imagen_home, (pos_home_x, pos_home_y))

        pygame.draw.rect(pantalla, GRIS, rect_boton_reiniciar, border_radius = size_radio_botones)
        pantalla.blit(imagen_reiniciar, (pos_reiniciar_x, pos_reiniciar_y))

        pygame.draw.rect(pantalla, GRIS, rect_timer, border_radius = size_radio_botones)
        pantalla.blit(txt_timer, (post_txt_tiempo_x, post_txt_tiempo_y))

        pygame.draw.rect(pantalla, GRIS, rect_errores, border_radius = size_radio_botones)
        pantalla.blit(txt_errores, (pos_errores_x, pos_errores_y))


        # MATRIZ SUDOKU
        tamaño_celda = calcular_tamaño_rect(pantalla, SIZE_CELDA_W, SIZE_CELDA_H)
        diccionario_rect_celdas = blit_sudoku(pantalla, matriz_oculta, matriz_sudoku, matriz_a_completar, (PORCENTAJE_PRIMERA_CELDA, PORCENTAJE_PRIMERA_CELDA), tamaño_celda, rect_donde_colisiona, SIZE_TXT_NUM_CELDA, AZUL, VERDE, ROJO)

        if colision_celda == True:
            matriz_a_completar[fila_colision][columna_colision] = numero_bliteo

        if matriz_a_completar == matriz_sudoku:
            pantalla_actual = 4
            sonido_victoria.play()
            puntaje_final = calcular_puntaje(dificultad_seleccionada, contador_minutos, contador_segundos, contador_errores)
            numero_bliteo = ""
            fila_colision = None
            columna_colision = None
            rect_donde_colisiona = None
            seleccion_activa = False
            colision_celda = False

    elif pantalla_actual == 4:
        
        pygame.draw.rect(pantalla, BLANCO, rect_victoria, border_radius = size_bordes_botones)

        pantalla.blit(txt_win, posicion_txt_win)
        pantalla.blit(txt_nick, posicion_txt_nick)

        pygame.draw.rect(pantalla, AZUL, rect_username, width = size_bordes_botones, border_radius = size_radio_botones)
        pantalla.blit(txt_user_ingresado, pos_txt_user_ingresado)
        txt_tu_puntaje = crear_superficie_texto("Showcard Gothic", SIZE_TXT_TU_PUNTAJE, f"TU PUNTAJE FUE: {puntaje_final}", AZUL, pantalla)
        pos_x_tu_puntaje, pos_y_tu_puntaje = obtener_posicion_superficie_centrada_en_x(txt_tu_puntaje, rect_pantalla, PORCENTAJE_Y_PUNTAJE_MOSTRADO) 
        pantalla.blit(txt_tu_puntaje, (pos_x_tu_puntaje, pos_y_tu_puntaje))
        




    elif pantalla_actual == 5:

        pygame.draw.rect(pantalla, BLANCO, rect_rankings, border_radius = size_radio_botones)
        blit_texto_con_sombra(pantalla, txt_ranking, txt_ranking_sombra, pos_txt_ranking)


        if len(lista_nombres) != 0:
            blitear_rankings(pantalla, 10, lista_nombres, lista_puntajes, SIZE_TXT_JUGADORES, (PORCENTAJE_X_NOMBRE, PORCENTAJE_Y_NOMBRE_PUNTAJE), (PORCENTAJE_X_PUNTAJE, PORCENTAJE_Y_NOMBRE_PUNTAJE), AZUL, size_espaciado_top, "Showcard Gothic")
            

        
        pygame.draw.rect(pantalla, GRIS, rect_volver, border_radius = size_radio_boton_volver_ranking)
        pantalla.blit(imagen_volver_ranking, (pos_x_volver_ranking, pos_y_volver_ranking))
        pantalla.blit(txt_top, (pos_x_top, pos_y_top))
        pantalla.blit(txt_nombre, (pos_x_nombre, pos_y_nombre))
        pantalla.blit(txt_puntaje, (pos_x_puntaje, pos_y_puntaje))
        


    pygame.display.flip()