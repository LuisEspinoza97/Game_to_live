# Game_to_live
"Game_to_live" es un programa en Python que se basa en el autómata celular creado por John Conway en 1970.
Utiliza las bibliotecas numpy y matplotlab para simular una población de células que evolucionan de acuerdo con las siguientes reglas:

Una célula muerta con exactamente 3 células vecinas vivas nace, en el siguiente turno estará viva o encendida.

Una célula viva con 2 o 3 células vecinas vivas sigue viva. 

En cualquier otro caso la célula muere o se apaga, por tener menos o más células adyacentes vivas de las reglas anteriores.
  
# Instalacion

VERIFICAR SI PYTHON ESTÁ INSTALADO

Antes de instalar Python, es posible que ya lo tengas instalado en tu sistema. Para verificar si Python está instalado en tu computadora, puedes abrir una terminal (en Windows, puedes abrir el símbolo del sistema o PowerShell) y escribir lo siguiente:

    python --version

Si Python está instalado, se mostrará la versión de Python que estás usando. Si no está instalado, se mostrará un mensaje de error indicando que Python no está reconocido como un comando interno o externo.

INSTALAR PYTHON

Si no tienes Python instalado, puedes descargar la última versión de Python desde el sitio web oficial de Python (https://www.python.org/downloads/). Haz clic en el botón de descarga correspondiente para tu sistema operativo y sigue las instrucciones de instalación.

Durante el proceso de instalación, asegúrate de seleccionar la opción para agregar Python al PATH y pip. Esto permitirá que puedas usar Python desde cualquier lugar en tu sistema.

INSTALAR LAS BIBLIOTECAS

Para ejecutar el programa "Juego de la Vida", necesitarás instalar dos bibliotecas de Python: numpy y matplotlib. Estas bibliotecas pueden instalarse usando el administrador de paquetes pip de Python.

Para instalar pip, abre una terminal y escribe el siguiente comando:

    python -m ensurepip --default-pip

Para instalar las bibliotecas numpy y matplotlib, escribe los siguientes comandos en la terminal:

    pip install numpy

    pip install matplotlib

Si estás utilizando una versión de Python anterior a la 3.4, es posible que necesites usar la versión antigua de pip (pip3) para instalar las bibliotecas:

    pip3 install numpy

    pip3 install matplotlib

DESCARGAR EL CÓDIGO FUENTE DEL PROGRAMA

Ahora que tienes Python y las bibliotecas necesarias instaladas, puedes descargar el código fuente del programa "Juego de la Vida" desde su repositorio en GitHub.

Haz clic en el botón verde "Code" y selecciona "Download ZIP".

Extrae el archivo ZIP descargado en una ubicación conveniente en tu computadora.

EJECUTAR EL PROGRAMA

Para ejecutar el programa "Juego de la Vida", abre una terminal y navega hasta la carpeta donde extrajiste el código fuente del programa. Luego, escribe el siguiente comando en la terminal:

    python game_of_life.py

Esto ejecutará el programa y comenzará a simular el Juego de la Vida en una ventana de matplotlib.

¡Eso es todo! Ahora deberías tener el programa "Juego de la Vida" instalado y funcionando en tu computadora.
