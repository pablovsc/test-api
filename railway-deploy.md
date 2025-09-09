# DESPLIEGUE EN RAILWAY - GUÍA PASO A PASO

## 1. PREPARAR ARCHIVOS PARA RAILWAY

Crear archivo Procfile:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Actualizar main.py para usar PORT de entorno:
```python
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
```

## 2. CREAR CUENTA EN RAILWAY
- Ir a https://railway.app
- Registrarse con GitHub (gratis)

## 3. DESPLEGAR API
- Hacer clic en "New Project"
- Seleccionar "Deploy from GitHub repo"
- Conectar tu repositorio
- Railway detecta automáticamente Python

## 4. AGREGAR BASE DE DATOS
- En el proyecto, hacer clic en "+ New"
- Seleccionar "Database" > "PostgreSQL"
- Railway crea automáticamente las variables de entorno

## 5. CONFIGURAR VARIABLES
Railway configura automáticamente:
- DATABASE_URL
- PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE

## 6. OBTENER URL
Después del despliegue obtienes:
- URL de la API: https://tu-proyecto.railway.app
- Endpoint: https://tu-proyecto.railway.app/api/query

## 7. ACTUALIZAR COPILOT STUDIO
Cambiar localhost por tu URL de Railway:
- Antes: http://localhost:8000/api/query  
- Después: https://tu-proyecto.railway.app/api/query

## LÍMITES GRATUITOS:
- $5 USD de crédito mensual (suficiente para proyectos pequeños)
- 500 horas de ejecución
- 1GB RAM
- 1GB almacenamiento PostgreSQL