    # código:    [título,                 plataforma,    género,    edad_recomendada, desarrolladora], 
videojuegos = { 
    'VG001': ['El perfume Axe'     ,        'PS5',      'RPG',            '100+',    'Herni'], 
    'VG002': ['El carrete del Jona',        'PS5',      'Bohemia',         '20+',    'Don Willy'], 
    'VG003': ['Minecraft',                  'PC',       'Sandbox',          '7+',    'Mojang'], 
    'VG004': ['The Legend of Zelda:TOTK',   'Switch',   'Aventura',        '12+',    'Nintendo'], 
    'VG005': ['God of War Ragnarok',        'PS5',      'Acción',          '18+',    'Santa Monica Studio'], 
    'VG006': ['Mario Kart 8',               'Switch',   'Carreras',         '3+',    'Nintendo'], 
    'VG007': ['Fortnite ',                   'PC',       'Battle Royale',   '12+',    'Epic Games'], 
    } 
inventario = {
    'VG001': [59990, 5],
    'VG002': [49990, 10], 
    'VG003': [29990, 0], 
    'VG004': [69990, 3], 
    'VG005': [64990, 7], 
    'VG006': [39990, 15], 
    'VG007': [0, 100], 
    }
nombre=input("ingrese nombre del juego: ").lower()
for clave, valor in videojuegos.items():
    edad_recomendada=valor[3]
    if  valor [0].lower()==nombre  :
        print(f"{nombre}  {valor[3]}")


     
    





# while True:
#             print("""
#                 MENÚ PRINCIPAL 
#             1. Stock por desarrolladora. 
#             2. Búsqueda por plataforma. 
#             3. Actualizar stock. 
#             4. Eliminar videojuego por código. 
#             5. Salir. """)
#             try:
#                     op=int(input("ingrese opcion (1 a 5): "))
                
#                     if op not in (1,2,3,4,5):
#                         print("ingrese una opcion valida...(1 a 5)")
#                     elif op == 1:
#                         print()
#                     elif op == 2:
#                         print()
#                     elif op == 3:
#                         print()
#                     elif op == 4:
#                         print()
#                     elif op == 5:
#                         print("Programa finalizado. ")
#                         break
#                     else:
#                         print("ingrese valor valido de 1 al 5")
#             except ValueError:
#                 print("ingrese opcion valida")




