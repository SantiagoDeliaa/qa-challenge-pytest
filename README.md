# QA API Challenge - Pytest + Allure

Automatización de pruebas del recurso `/pet` de la API [Swagger Petstore](https://petstore.swagger.io/) usando **Python**, **Pytest** y reportes **Allure**.

---

## Instalación y ejecución

### Prerequisitos

* Python 3.10+
* pip

```bash
# Clonar el repo y pararse en la carpeta
cd qa-challenge-pytest

# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar las pruebas
pytest -v

# Ejecutar con reporte Allure
pytest --alluredir=allure-results

# Para ver el reporte (hay que tener Allure CLI instalado)
allure serve allure-results
```

---

## Reportes con Allure

Cada test tiene decoradores de Allure:

* `@allure.feature`: categoría general
* `@allure.story`: subcategoría del test
* `@allure.description`: descripción de lo que valida el test

---

## Casos de Prueba

* `test_add_pet.py`: Crea una mascota y valida los campos del response
* `test_get_pet_by_id.py`: Consulta una mascota recién creada y valida los datos
* `test_update_pet.py`: Modifica nombre y estado de una mascota y valida que los cambios se reflejan correctamente
* `test_delete_pet.py`: Elimina una mascota y se asegura que no puede ser consultada
* `test_find_by_status.py`: Valida que se puede filtrar por status y que todas las mascotas cumplen ese status

Cada test es **autónomo**: crea, actualiza y elimina recursos dentro del mismo flujo para evitar dependencia entre tests.

---

## CI/CD 

### GitHub Actions (Validaciones Automatizadas)

- Integre este flujo a `GitHub Actions` para `pytest`.
- Cada vez que se realiza un `push` o `pull request`.
- Publica resultados con `Allure`.
- Valida regresiones o errores en el endpoint `/pet` de forma continua.

---

## Notas

* La API tiene varias inconsistentes y demoras en el procesamiento.
* Por ese motivo aplique **reintentos (`retry`) y `sleep()`** despues de operaciones `POST`, `PUT` y `DELETE` para mas robustez.

---

