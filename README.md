# MonthlyExcelGenerator

Este repositorio contiene un script de Python que automatiza la creación de directorios y archivos Excel organizados por meses del año. Utiliza un archivo de plantilla (`template.xlsx`) para generar archivos Excel para cada día del mes.

## Descripción

El script `crear_carpetas_y_archivos_con_plantilla.py` crea una estructura de carpetas basada en el año actual. Dentro de cada carpeta de mes, se genera un archivo Excel para cada día del mes, utilizando un archivo de plantilla predefinido (`template.xlsx`). Esto es útil para mantener registros diarios organizados y consistentes a lo largo del año.

## Requisitos

- Python 3.x
- Bibliotecas de Python: `pandas`, `openpyxl`

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/MonthlyExcelGenerator.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd MonthlyExcelGenerator
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install pandas openpyxl
    ```

## Uso

1. Asegúrate de tener un archivo de plantilla llamado `template.xlsx` en el mismo directorio que el script `crear_carpetas_y_archivos_con_plantilla.py`.

2. Ejecuta el script:

    ```bash
    python crear_carpetas_y_archivos_con_plantilla.py
    ```

   O, si estás utilizando Python 3:

    ```bash
    python3 crear_carpetas_y_archivos_con_plantilla.py
    ```

3. El script creará un directorio con el nombre del año actual. Dentro de este directorio, habrá subcarpetas para cada
