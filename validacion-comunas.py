import unicodedata

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

# Función que normaliza un texto: quita tildes/acentos y pasa a minúsculas
def normalizar(texto):
    # NFKD separa las letras de sus acentos (ej: "á" -> "a" + acento suelto)
    texto_descompuesto = unicodedata.normalize("NFKD", texto)
    # Nos quedamos solo con los caracteres que NO son marcas de acento (combining marks)
    texto_sin_acentos = "".join(
        caracter for caracter in texto_descompuesto if not unicodedata.combining(caracter)
    )
    return texto_sin_acentos.lower().strip()

# Versión normalizada de la lista, para comparar sin tildes ni mayúsculas
comunas_normalizadas = [normalizar(c) for c in comunas]

# Bucle para pedir al usuario la comuna y validarla
comuna_valida = False
while not comuna_valida:
    comuna = input("Ingrese el nombre de la comuna: ")
    comuna_normalizada = normalizar(comuna)

    if comuna_normalizada in comunas_normalizadas:
        print("La comuna ingresada es correcta")
        comuna_valida = True
    else:
        print("La comuna ingresada no es correcta, por favor intente nuevamente")