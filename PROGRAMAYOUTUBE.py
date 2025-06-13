
# Lista donde se guardarán los videos favoritos
videos_favoritos = []

# Función para agregar un nuevo video
def agregar_video():
    codigo = input("Código del video: ")
    titulo = input("Título del video: ")
    autor = input("Autor del video: ")
    duracion = input("Duración del video (ej. 10:25): ")
    fecha = input("Fecha de registro (ej. 2025-06-13): ")

    video = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "duracion": duracion,
        "fecha": fecha
    }

    videos_favoritos.append(video)
    print("✅ Video agregado correctamente.\n")

# Función para listar todos los videos
def listar_videos():
    if not videos_favoritos:
        print("🚫 No hay videos guardados.\n")
        return
    print("📋 Lista de videos favoritos:")
    for video in videos_favoritos:
        print(f"""
Código: {video['codigo']}
Título: {video['titulo']}
Autor: {video['autor']}
Duración: {video['duracion']}
Fecha: {video['fecha']}
-------------------------------""")

# Función para modificar un video por código
def modificar_video():
    codigo = input("Ingresa el código del video a modificar: ")
    for video in videos_favoritos:
        if video["codigo"] == codigo:
            print("🔧 Video encontrado. Ingresa los nuevos datos:")
            video["titulo"] = input("Nuevo título: ")
            video["autor"] = input("Nuevo autor: ")
            video["duracion"] = input("Nueva duración: ")
            video["fecha"] = input("Nueva fecha de registro: ")
            print("✅ Video modificado correctamente.\n")
            return
    print("❌ No se encontró un video con ese código.\n")

# Función para eliminar un video por código
def eliminar_video():
    codigo = input("Ingresa el código del video a eliminar: ")
    for video in videos_favoritos:
        if video["codigo"] == codigo:
            videos_favoritos.remove(video)
            print("🗑 Video eliminado correctamente.\n")
            return
    print("❌ No se encontró un video con ese código.\n")

# Menú principal del programa
def menu():
    while True:
        print("""
🎬 Menú de Videos Favoritos:
1. Agregar video
2. Modificar video
3. Eliminar video
4. Listar videos
5. Salir
""")
        opcion = input("Elige una opción (1-5): ")
        if opcion == "1":
            agregar_video()
        elif opcion == "2":
            modificar_video()
        elif opcion == "3":
            eliminar_video()
        elif opcion == "4":
            listar_videos()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠ Opción no válida. Intenta nuevamente.\n")

# Iniciar el programa
menu()












