![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Code Size](https://img.shields.io/github/languages/code-size/federicoramos67/flatten-files)

# 📁 Flatten Files - Organiza tus archivos automáticamente

> ✨ **Herramienta CLI en Python** que transforma estructuras de carpetas complejas en una única carpeta organizada, resolviendo duplicados inteligentemente.

## 🚀 ¿Por qué es útil?

Como **Analista de Datos Jr.**, constantemente trabajo con:
- 📂 Estructuras de carpetas desorganizadas de datasets
- 🔄 Necesidad de procesar archivos masivos sin perder tiempo en organización manual
- ⚡ Automatización de tareas repetitivas para enfocarme en el análisis real

**Esta herramienta resuelve estos problemas en segundos.**

## 💡 Características clave

- ✅ **3 modos de manejo de duplicados**: renombrar, sobrescribir o saltar
- ✅ **Barra de progreso visual** que muestra el avance en tiempo real
- ✅ **Soporte dual**: modo interactivo (ideal para usuarios) y CLI (ideal para scripts)
- ✅ **Sin dependencias externas** - usa solo librerías estándar de Python
- ✅ **Pruebas unitarias** incluidas para garantizar calidad

## 🛠️ Cómo usarlo

```bash
# Instalación (no requiere dependencias)
git clone https://github.com/federicoramos67/flatten-files.git
cd flatten-files

# Modo interactivo
python flatten_files.py

# Modo CLI (ejemplo práctico)
python flatten_files.py C:/Users/datasets/raw_data C:/Users/datasets/clean_data rename

📌 Caso de uso real (como Analista de Datos)
Problema: Tenía un dataset de ventas con 500 archivos CSV distribuidos en 15 subcarpetas diferentes. Necesitaba consolidarlos para un análisis de Pandas.

Solución con flatten-files:
python flatten_files.py C:/ventas/2024/raw C:/ventas/2024/consolidado
Resultado: En 8 segundos, todos los archivos estuvieron listos para cargar en un DataFrame de Pandas, ahorrando 15 minutos de trabajo manual.

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Por favor abre un issue o PR para sugerir mejoras.

📄 Licencia
MIT © Federico Ramos

