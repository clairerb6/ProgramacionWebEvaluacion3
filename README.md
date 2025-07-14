# 📚 Evaluación Flask - Programación Web

Este proyecto es una aplicación web desarrollada con **Python Flask** para fines académicos. Incluye dos ejercicios independientes, cada uno con formularios validados tanto en frontend como en backend, base de datos SQLite y protección CSRF mediante **Flask-WTF**.

---

## 🚀 Funcionalidades principales

### ✅ **Ejercicio 1: Formulario de Notas**

- Permite ingresar nombre y RUT del alumno.
- Solicita tres notas (escala 10-70) y porcentaje de asistencia.
- Valida rangos de notas en el navegador (`onblur`) y en el servidor.
- Calcula promedio y determina si el alumno aprueba o reprueba.
- Guarda cada registro en una base de datos SQLite.
- Muestra un historial de todos los registros en una tabla.

### ✅ **Ejercicio 2: Comparador de Nombres**

- Formulario para ingresar hasta tres nombres.
- Evalúa cuál nombre tiene la mayor cantidad de caracteres.
- Muestra el resultado dinámicamente.
- Guarda cada comparación en la base de datos.
- Despliega un historial de comparaciones en tabla.

---

## 🛡️ **Seguridad**

- Validación de formularios con **Flask-WTF**.
- Protección **CSRF** incluida para evitar ataques de tipo *Cross Site Request Forgery*.
- Escapado automático de variables para prevenir *Cross Site Scripting* (XSS).

---

## 🗂️ **Estructura del proyecto**

```
project/
├── app.py
├── database.py
├── ejercicio1/
│   ├── forms.py
│   └── routes.py
├── ejercicio2/
│   ├── forms.py
│   └── routes.py
├── templates/
│   ├── index.html
│   ├── ejercicio1/ejercicio1.html
│   └── ejercicio2/ejercicio2.html
├── static/
│   └── functions.js
└── registros.db
```

---

## ⚙️ **Requisitos**

- Python 3.x
- Flask
- Flask-WTF

Instalar dependencias:

```bash
pip install flask flask-wtf
```

---

## 💻 **Cómo ejecutar**

1. Clona o descarga el repositorio.
2. Inicializa el entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

---

## 📝 **Notas**

- La base de datos `registros.db` se genera automáticamente si no existe.
- Las validaciones en `functions.js` complementan las validaciones del servidor.
- El proyecto está organizado por **Blueprints** para mantener cada ejercicio independiente y modular.

---

## 👩‍💻 **Desarrollado por**

Katherine Flores (Víctor Flores)\
Ingeniera en Informática\
Programación Web - Evaluación 3

---

✨ *¡Gracias por revisar este proyecto!*

