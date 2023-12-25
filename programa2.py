import geocoder

def obtener_ubicacion():
    # Obtener información de ubicación basada en la dirección IP
    ubicacion = geocoder.ip('me')

    # Imprimir la información de ubicación
    print("Tu ubicación actual:")
    print(f"Dirección IP: {ubicacion.ip}")
    print(f"País: {ubicacion.country}")
    print(f"Región: {ubicacion.region}")
    print(f"Ciudad: {ubicacion.city}")
    print(f"Latitud: {ubicacion.latlng[0]}")
    print(f"Longitud: {ubicacion.latlng[1]}")

if __name__ == "__main__":
    # Llamada a la función para obtener la ubicación
    obtener_ubicacion()
#ubicacion
