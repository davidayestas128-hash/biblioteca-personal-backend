# biblioteca-personal-backend

Backend de la **Biblioteca Personal de Libros**, desarrollado con **Django REST Framework**.

Proyecto integrador de la asignatura *Herramientas Avanzadas para el Desarrollo de Aplicaciones* — Ciclo II-2026, Universidad Técnica Latinoamericana.

## Repositorio relacionado

Este backend se conecta con el frontend desarrollado en React:
 [biblioteca-personal-frontend](https://github.com/davidayestas128-hash/biblioteca-personal-frontend)

## Descripción

API REST que permite gestionar una colección personal de libros: registro de libros, autores, colecciones personalizadas y reseñas con calificación. Incluye control de concurrencia mediante bloqueo optimista (campo `version` en el modelo `Libro`).

## Tecnologías

- Python / Django
- Django REST Framework
- django-cors-headers
- SQLite (entorno de desarrollo)

## Estructura del proyecto

```
biblioteca-personal-backend/
├── backend/            # Configuración principal del proyecto Django
├── libros/             # App: modelos Libro, Autor
├── colecciones/        # App: modelo Colección
├── resenas/            # App: modelo Reseña
├── requirements.txt
├── .env.example
└── .gitignore
```

## Instalación local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/davidayestas128-hash/biblioteca-personal-backend.git
   cd biblioteca-personal-backend
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno:
   ```bash
   cp .env.example .env
   # completar SECRET_KEY, DEBUG, etc.
   ```

5. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

6. Levantar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

La API quedará disponible en `http://localhost:8000/api/`.

## Conexión con el frontend

El frontend (React + Vite) debe apuntar su variable de entorno `VITE_API_URL` a la URL de este backend (por defecto `http://localhost:8000/api/`). Asegúrate de que `django-cors-headers` tenga habilitado el origen del frontend (por defecto `http://localhost:5173`).

## Endpoints principales

- `/api/libros/`
- `/api/autores/`
- `/api/colecciones/`
- `/api/resenas/`

## Flujo de trabajo (Git)

Estrategia: **GitHub Flow**. La rama `main` está protegida y requiere Pull Request con al menos 1 aprobación antes de fusionar.

Convención de ramas:
- `feature/nombre-funcionalidad` — nuevas funcionalidades
- `fix/nombre-correccion` — correcciones de errores

Convención de commits:
- `feat:` nueva funcionalidad
- `fix:` corrección de errores
- `docs:` documentación
- `refactor:` cambios de estructura sin alterar funcionalidad
- `test:` pruebas

Todo cambio a `main` pasa por un Pull Request revisado por al menos un integrante distinto al autor.

## Integrantes

- Marcela Saraí Ramírez Caceres
- María Celeste Hernández Aguilar
- David Alonso Ayestas Flores

## Historial de cambios de dominio

_(Si el dominio o el alcance del proyecto llega a cambiar durante el ciclo, se documentara aquí con fecha y razón.)_
