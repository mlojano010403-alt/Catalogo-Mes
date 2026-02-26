import os
import webbrowser
import threading
import time

def open_browser():
    time.sleep(2) # Espera a que el servidor suba
    webbrowser.open("http://127.0.0.1:8000/")

if __name__ == "__main__":
    # Iniciamos el hilo para abrir el navegador
    threading.Thread(target=open_browser).start()
    # Ejecutamos el servidor de Django
    os.system("python manage.py runserver")