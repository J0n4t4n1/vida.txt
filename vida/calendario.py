import datetime
import sys

# Traduce el día de la semana al español
dias = {
    "Monday": "lunes",
    "Tuesday": "martes",
    "Wednesday": "miércoles",
    "Thursday": "jueves",
    "Friday": "viernes",
    "Saturday": "sábado",
    "Sunday": "domingo",
}

def obtener_fecha_dia(fecha):
    dia = fecha.strftime("%A")
    dia_es = dias[dia]
    return fecha.strftime("%d-%m-%Y"), dia_es

# Lee el archivo /ruta/calendario.txt y guarda los eventos existentes
eventos = {}
try:
    with open("/ruta/vida/calendario.txt", "r") as f:
        for linea in f:
            linea = linea.strip()
            if linea:  # Verifica que la línea no esté vacía
                if linea.startswith("+"):
                    evento = linea[2:].strip()
                    eventos[fecha_evento].add(evento)
                else:
                    fecha_evento, dia = linea.split()
                    eventos[fecha_evento] = set()
except FileNotFoundError:
    pass

# Si se proporcionó una fecha en la línea de comandos, úsala
if len(sys.argv) > 1 and "-" in sys.argv[1]:
    fecha = datetime.datetime.strptime(sys.argv[1], "%d-%m-%Y")
    evento = " ".join(sys.argv[2:])
else:
    # De lo contrario, usa la fecha actual
    fecha = datetime.datetime.now()
    evento = " ".join(sys.argv[1:])

fecha, dia = obtener_fecha_dia(fecha)

# Añade el evento si no existe ya
if evento:
    if fecha not in eventos:
        eventos[fecha] = set()
    if evento not in eventos[fecha]:
        eventos[fecha].add(evento)

# Escribe los eventos en el archivo /home/joni/Documentos/vida/calendario.txt
with open("/home/joni/Documentos/vida/calendario.txt", "w") as f:
    for fecha in sorted(eventos):
        fecha_datetime = datetime.datetime.strptime(fecha, "%d-%m-%Y")
        fecha, dia = obtener_fecha_dia(fecha_datetime)
        f.write(f"{fecha} {dia}\n")
        for evento in sorted(eventos[fecha]):
            f.write(f"+ {evento}\n")
        f.write("\n")  # Añade un salto de línea adicional después de cada fecha
