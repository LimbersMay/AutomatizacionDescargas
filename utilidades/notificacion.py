from plyer import notification

Icono = "iconos/Trabajo.ico"


def iniciar_notificacion(mensaje: str):
    notification.notify(
        title="Asistente",
        message=mensaje,
        app_icon=Icono,
        timeout=8
    )


def mandar_notificacion(cantidad_tareas: int):
    if cantidad_tareas > 0:
        mensaje = f"Hola, he ordenado {cantidad_tareas} archivos de la carpeta de descargas"
        iniciar_notificacion(mensaje)
    


# tareas1 = []
# mandar_notificacion(tareas1)