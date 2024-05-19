# vida.txt
Repositorio de un programa multifuncional desarrollado en Python3 y Bash, que incluye un calendario, una lista de tareas pendientes (ToDo) basada en el formato del repositorio todo.txt, y funcionalidades de notas. Todos los datos se almacenan en archivos de texto (txt) para facilitar la portabilidad y la compatibilidad. Este repositorio se utiliza para el control de versiones y el seguimiento del desarrollo del programa. 
Todo.txt https://github.com/todotxt




Puedes añadir un alias a tu archivo ~/.bashrc para ejecutar tu script main.py más fácilmente. Aquí te dejo los pasos que puedes seguir:

1. Abre tu archivo ~/.bashrc con tu editor de texto preferido. Por ejemplo, puedes usar nano:

 > sudo nano ~/.bashrc

2. Añade la siguiente línea al final de tu archivo ~/.bashrc, reemplazando /ruta/a/tu/main.py con la ruta completa a tu script main.py:

>  alias miEvento='python3 /ruta/a/tu/main.py'

3. Guarda los cambios y cierra el editor. Si estás usando nano, puedes hacer esto presionando Ctrl+X, luego Y para confirmar los cambios, y finalmente Enter para salir.

4. Para que los cambios surtan efecto, debes ejecutar el siguiente comando:

>  source ~/.bashrc

Ahora puedes usar el comando miEvento en tu terminal para ejecutar tu script main.py. Por ejemplo:

>  miEvento 'Pasear con mi novia'

o

>  miEvento '18-05-2024' 'Pasear con mi novia'
