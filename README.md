# AI Master TaskManager

Un gestor de tareas simple en Python con persistencia JSON, diseñado para uso didáctico y pruebas de calidad.

## 📁 Estructura del proyecto

- `main.py`: Entry point de la aplicación CLI
- `task_manager.py`: Lógica principal (clases `Task` y `TaskManager`)
- `ai_service.py`: API/servicio (si aplica)
- `tasks.json`: Almacenamiento local de tareas
- `tests/`: Pruebas unitarias con pytest

## 🚀 Requisitos

- Python 3.10+ (probado con 3.14)
- Virtualenv recomendado

## 🛠️ Instalación

```powershell
cd c:\Git\ai-master-taskmanager
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install pytest
```

## ▶️ Uso básico (CLI)

```powershell
python main.py add "Mi tarea"      # Añade una tarea
python main.py list                 # Lista tareas
python main.py complete 1           # Marca qué tarea completar
python main.py delete 1             # Elimina tarea
```

## 🧪 Pruebas

```powershell
$env:PYTHONPATH='.'; pytest -q
```

Se crearon pruebas en `tests/test_task_manager.py` cubriendo:
- `add_task`
- `complete_task`
- `delete_task` (exitosa)
- `delete_task` (id no existente)
- Persistencia en JSON

## 📝 API de `TaskManager`

- `TaskManager.FILENAME` (ruta JSON configurable)
- `add_task(description)`
- `list_tasks()`
- `complete_task(id)`
- `delete_task(id)`
- `load_tasks()`
- `save_tasks()`

## 💡 Buenas prácticas

- Usar siempre un entorno virtual
- No versionar el archivo `tasks.json` si es local y temporal
- Filtrar y validar `id` en la capa superior de CLI si se extiende el proyecto

## 📦 Extensiones sugeridas

- Soporte de tareas recurrentes
- Etiquetas / prioridades
- API REST + front-end
- Persistencia en SQLite

