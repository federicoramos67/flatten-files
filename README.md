# Flatten Files 📁➡️📄

Una herramienta en Python que extrae **todos los archivos** de una carpeta (y sus subcarpetas) y los copia a una **única carpeta plana**, resolviendo duplicados de forma inteligente.

Perfecto para organizar descargas, fotos, documentos o cualquier estructura anidada.

## 💡 Características

- Soporta modos: **renombrar**, **sobrescribir** o **saltar** duplicados.
- Barra de progreso visual en modo interactivo.
- Funciona tanto en **modo interactivo** como por **línea de comandos (CLI)**.
- Sin dependencias externas (solo librerías estándar de Python).

## 🚀 Cómo usarlo

### Requisitos
- Python 3.6+

### Modo interactivo (paso a paso)
```bash
python flatten_files.py

Modo CLI (rápido)
# Uso básico (renombra duplicados)
python flatten_files.py /ruta/origen /ruta/destino

# Especificar modo
python flatten_files.py /origen /destino overwrite
python flatten_files.py /origen /destino skip

📌 Ejemplo
Antes

fotos/
  ├── verano/
  │   └── img1.jpg
  └── viaje/
      └── img1.jpg  ← duplicado
	  
Después (modo rename):
destino/
  ├── img1.jpg
  └── img1_1.jpg
  
🛠️ Autor
Creado por Federico Ramos (@federicoramos67 )