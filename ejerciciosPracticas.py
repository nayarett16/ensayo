    # código:    [título,                 plataforma,    género,    edad_recomendada, desarrolladora], 
videojuegos = { 
    'VG001': ['El perfume Axe'     ,        'PS5',      'RPG',            '100+',    'Herni'], 
    'VG002': ['El carrete del Jona',        'PS5',      'Bohemia',         '20+',    'Don Willy'], 
    'VG003': ['Minecraft',                  'PC',       'Sandbox',          '7+',    'Mojang'], 
    'VG004': ['The Legend of Zelda:TOTK',   'Switch',   'Aventura',        '12+',    'Nintendo'], 
    'VG005': ['God of War Ragnarok',        'PS5',      'Acción',          '18+',    'Santa Monica Studio'], 
    'VG006': ['Mario Kart 8',               'Switch',   'Carreras',         '3+',    'Nintendo'], 
    'VG007': ['Fortnite',                   'PC',       'Battle Royale',   '12+',    'Epic Games'], 
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

    
def  stock_por_desarrolladora(): 
    usuario=input("ingrese desarolladora (eje:Nintendo): ").lower()
    for clave,valor in videojuegos.items():
        if valor[4].lower()==usuario:
            desarroladora=valor[4]
            stock=inventario.get(clave,1)
            print(f"Nombre Desarrolladora:{desarroladora} y su stock es:{stock}")
  

def búsqueda_por_plataforma(): 
    plataforma=input("ingrese plantaforma (ej: “PS5”, “PC”, “Switch”): ").lower()
    for clave,valor in videojuegos.items():
        if valor[1].lower()==plataforma:
            nombre=valor[1]
            cantidad=inventario.get(clave,1)
            print(f"plataforma:{nombre} y su stock:{cantidad}")



def actualizar_stock():
    actualizar=int(input("ingrese codigo: ")) 
    for c , v in videojuegos.items():
        if c[0]==actualizar:
            print(videojuegos,0)
        




def eliminar_videojuego():
    eliminar=input("ingrese juego a eliminar: ").lower()
    for clave , valor in videojuegos.items():
        if valor[0].lower()==eliminar:
            videojuegos.remove(eliminar)







    while True:
        print("""
            MENÚ PRINCIPAL 
        1. Stock por desarrolladora. 
        2. Búsqueda por plataforma. 
        3. Actualizar stock. 
        4. Eliminar videojuego por código. 
        5. Salir. """)

        op=int(input("ingrese opcion (1 a 5): "))


        if op == 1:
            stock_por_desarrolladora()
        elif op == 2:
            búsqueda_por_plataforma()
        elif op == 3:
            actualizar_stock()
        elif op == 4:
            eliminar_videojuego()
        elif op == 5:
            print("Programa finalizado. ")
            break
        else:
            print("ingrese valor valido de 1 al 5")



