import os
import pandas as pd
from calendar import monthrange
import shutil
from datetime import datetime

# Define los nombres de los meses
months = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# Obtiene el año actual
current_year = datetime.now().year

# Directorio base que depende del año actual
base_dir = str(current_year)

# Nombre del archivo de plantilla
template_file = "template.xlsx"

# Verifica que el archivo de plantilla exista
if not os.path.exists(template_file):
    raise FileNotFoundError(f"El archivo de plantilla '{template_file}' no existe en el directorio actual.")

# Crea el directorio base
os.makedirs(base_dir, exist_ok=True)

# Función para copiar el archivo de plantilla
def copy_template(file_path):
    shutil.copy(template_file, file_path)

# Recorre cada mes y crea sus respectivos días en archivos Excel
for month_index, month_name in enumerate(months):
    # Crea el directorio del mes
    month_dir = os.path.join(base_dir, month_name)
    os.makedirs(month_dir, exist_ok=True)
    
    # Obtiene la cantidad de días del mes
    days_in_month = monthrange(current_year, month_index + 1)[1]
    
    # Crea un archivo Excel por cada día del mes usando la plantilla
    for day in range(1, days_in_month + 1):
        file_path = os.path.join(month_dir, f"{day}.xlsx")
        copy_template(file_path)

print("Directorios y archivos creados con éxito.")

