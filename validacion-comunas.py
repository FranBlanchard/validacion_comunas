# Lista de comunas de la Región Metropolitana
comunas = [
    "Santiago", "Cerrillos", "Cerro Navia", "Conchalí", "El Bosque",
    "Estación Central", "Huechuraba", "Independencia", "La Cisterna",
    "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes",
    "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa",
    "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel",
    "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín",
    "San Miguel", "San Ramón", "Vitacura",
    "Puente Alto", "Pirque", "San José de Maipo",
    "Colina", "Lampa", "Tiltil",
    "San Bernardo", "Buin", "Paine", "Calera de Tango",
    "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro",
    "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"
]

# Bucle para pedir al usuario la comuna y validarla
comuna_valida = False
while not comuna_valida:
    # Pedir al usuario la comuna
    comuna = input("Ingrese el nombre de la comuna: ")

    # Verificar si la comuna es válida
    if comuna in comunas:
        print("La comuna ingresada es correcta")
        comuna_valida = True
    else:
        print("La comuna ingresada no es correcta, por favor intente nuevamente")