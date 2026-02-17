# Tutorial: Configuración de CI/CD para Databricks con GitHub Actions

Esta guía te enseñará paso a paso cómo configurar un repositorio de GitHub con integración a Databricks y un pipeline de CI/CD que ejecute tests automáticamente y despliegue notebooks cuando los tests pasen.

## 📋 Requisitos Previos

- Una cuenta de GitHub
- Acceso a un workspace de Databricks
- Conocimientos básicos de Git

---

## Parte 1: Crear Repositorio en GitHub

### Paso 1: Crear un nuevo repositorio

1. Ve a [GitHub](https://github.com) e inicia sesión
2. Haz clic en el botón **"+"** en la esquina superior derecha
3. Selecciona **"New repository"**
4. Completa los siguientes campos:
   - **Repository name**: `databricks-projects` (o el nombre que prefieras)
   - **Description**: "Databricks workflows, notebooks, and ETL pipelines for data engineering projects"
   - **Visibility**: Public o Private (según tu preferencia)
   - ✅ Marca **"Add a README file"**
   - ✅ Marca **"Add .gitignore"** y selecciona **Python**
5. Haz clic en **"Create repository"**

---

## Parte 2: Configurar Databricks Repos

### Paso 2: Conectar GitHub con Databricks

1. Abre tu workspace de Databricks
2. En el menú lateral izquierdo, haz clic en **"Workspace"**
3. Navega a tu carpeta de usuario (por ejemplo: `Users/tu-email@gmail.com`)
4. Haz clic derecho y selecciona **"Create" → "Repo"**
5. En el diálogo:
   - Selecciona **"GitHub"** como Git provider
   - Si es la primera vez, te pedirá configurar Git credentials

### Paso 3: Configurar Git Credentials (OAuth)

1. En Databricks, ve a **"Settings"** (ícono de engranaje)
2. Selecciona **"Developer"** → **"Git integration"**
3. Haz clic en **"Add credential"**
4. Selecciona **"GitHub"**
5. Haz clic en **"Generate OAuth Token"**
6. Serás redirigido a GitHub para autorizar
7. Haz clic en **"Authorize"**
8. Copia el **código de verificación** que te muestra GitHub
9. Pégalo en Databricks y haz clic en **"Confirm"**

### Paso 4: Instalar Databricks GitHub App

1. Cuando te solicite instalar la aplicación, haz clic en **"Install Databricks"**
2. Selecciona **"All repositories"** o los específicos que quieras
3. Haz clic en **"Install"**
4. Regresa a Databricks

### Paso 5: Vincular el Repositorio

1. Vuelve a crear el Repo en Databricks:
   - Workspace → Tu carpeta → Create → Repo
2. Ingresa la **URL de tu repositorio de GitHub**:
   ```
   https://github.com/tu-usuario/databricks-projects
   ```
3. Haz clic en **"Create"**
4. ¡Tu repo ahora está vinculado a Databricks!

---

## Parte 3: Crear Estructura del Proyecto

### Paso 6: Crear estructura de carpetas

En tu repositorio de GitHub, crea la siguiente estructura:

```
databricks-projects/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline de CI/CD
├── notebooks/
│   └── sample_notebook.py     # Notebook de ejemplo
├── tests/
│   └── test_sample.py         # Tests unitarios
├── requirements.txt           # Dependencias
├── .gitignore
└── README.md
```

### Paso 7: Crear archivo de workflow

1. En GitHub, navega a tu repositorio
2. Haz clic en **"Add file" → "Create new file"**
3. Nombre del archivo: `.github/workflows/ci-cd.yml`
4. Pega el siguiente contenido:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
      - development
  pull_request:
    branches:
      - main

env:
  DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST }}
  DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN }}

jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      
      - name: Run tests
        run: |
          pytest tests/ -v --cov=. --cov-report=xml --cov-report=term
      
      - name: Upload coverage reports
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
          flags: unittests
          name: codecov-umbrella

  deploy:
    name: Deploy to Databricks
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      - name: Install Databricks CLI
        run: |
          pip install databricks-cli
      
      - name: Deploy notebooks to Databricks
        run: |
          # Configure Databricks CLI
          databricks configure --token <<EOF
          ${{ secrets.DATABRICKS_HOST }}
          ${{ secrets.DATABRICKS_TOKEN }}
          EOF
          
          # Sync notebooks to Databricks workspace
          databricks workspace import_dir notebooks/ /Users/TU-EMAIL@gmail.com/databricks-projects/notebooks --overwrite
      
      - name: Run Databricks job (optional)
        run: |
          # Si tienes un job de Databricks para ejecutar
          # databricks jobs run-now --job-id ${{ secrets.DATABRICKS_JOB_ID }}
```

**⚠️ IMPORTANTE**: Reemplaza `TU-EMAIL@gmail.com` con tu email de Databricks.

5. Haz clic en **"Commit changes"**

### Paso 8: Crear tests de ejemplo

1. Crea el archivo `tests/test_sample.py`:

```python
import pytest

def test_addition():
    """Test simple addition"""
    assert 1 + 1 == 2

def test_string_concatenation():
    """Test string operations"""
    result = "Hello" + " " + "World"
    assert result == "Hello World"

def test_list_operations():
    """Test list manipulation"""
    my_list = [1, 2, 3]
    my_list.append(4)
    assert len(my_list) == 4
    assert my_list[-1] == 4
```

### Paso 9: Crear requirements.txt

1. Crea el archivo `requirements.txt`:

```
pytest==7.4.3
pytest-cov==4.1.0
databricks-cli==0.18.0
pandas==2.0.3
numpy==1.24.3
```

### Paso 10: Crear notebook de ejemplo

1. Crea el archivo `notebooks/sample_notebook.py`:

```python
# Databricks notebook source
# MAGIC %md
# MAGIC # Sample Databricks Notebook
# MAGIC This is a sample notebook for CI/CD pipeline testing.

# COMMAND ----------

import pandas as pd
from pyspark.sql import SparkSession

# COMMAND ----------

# Create sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['San Jose', 'San Francisco', 'Oakland']
}

df = pd.DataFrame(data)
print(df)

# COMMAND ----------

# Convert to Spark DataFrame
spark_df = spark.createDataFrame(df)
spark_df.show()
```

---

## Parte 4: Configurar Secrets de GitHub

### Paso 11: Crear Access Token en Databricks

1. En Databricks, ve a **"Settings"** → **"Developer"**
2. Selecciona **"Access tokens"**
3. Haz clic en **"Manage"** → **"Generate new token"**
4. Dale un nombre: `GitHub Actions CI/CD`
5. Configura el tiempo de expiración (recomendado: 90 días)
6. Haz clic en **"Generate"**
7. **¡COPIA EL TOKEN INMEDIATAMENTE!** (no podrás verlo después)

### Paso 12: Configurar Secrets en GitHub

1. Ve a tu repositorio en GitHub
2. Haz clic en **"Settings"** → **"Secrets and variables"** → **"Actions"**
3. Haz clic en **"New repository secret"**
4. Crea el primer secret:
   - **Name**: `DATABRICKS_HOST`
   - **Value**: `https://tu-workspace.cloud.databricks.com`
   - Haz clic en **"Add secret"**
5. Crea el segundo secret:
   - **Name**: `DATABRICKS_TOKEN`
   - **Value**: [pega el token que copiaste]
   - Haz clic en **"Add secret"**

---

## Parte 5: Probar el Pipeline

### Paso 13: Hacer un push para activar el workflow

1. Haz cualquier cambio en el README
2. Haz commit y push a la rama `main`
3. Ve a **"Actions"** en tu repositorio de GitHub
4. Verás el workflow ejecutándose

### Paso 14: Verificar resultados

El workflow ejecutará dos jobs:

1. **Run Tests** (✅ ~35 segundos)
   - Instala dependencias
   - Ejecuta pytest
   - Genera reporte de cobertura

2. **Deploy to Databricks** (✅ ~7 segundos)
   - Solo se ejecuta si los tests pasan
   - Solo se ejecuta en pushes a `main`
   - Sincroniza notebooks a Databricks

---

## 🎉 ¡Felicidades!

Ahora tienes un pipeline completo de CI/CD que:

✅ Ejecuta tests automáticamente en cada push  
✅ Verifica la calidad del código  
✅ Despliega notebooks a Databricks solo si los tests pasan  
✅ Mantiene sincronizado tu código entre GitHub y Databricks  

---

## 🔧 Troubleshooting

### Problema: "No such file or directory: 'notebooks/'"

**Solución**: Asegúrate de que la carpeta `notebooks/` existe con al menos un archivo.

### Problema: "Top-level folder can only contain repos"

**Solución**: Verifica que la ruta en el workflow sea correcta:
```bash
/Users/TU-EMAIL@gmail.com/databricks-projects/notebooks
```

### Problema: "Authentication failed"

**Solución**:
1. Verifica que los secrets estén configurados correctamente
2. Regenera el token de Databricks si es necesario
3. Asegúrate de que el token no haya expirado

### Problema: Los tests fallan

**Solución**:
1. Revisa los logs en la pestaña Actions
2. Ejecuta los tests localmente: `pytest tests/ -v`
3. Verifica que todas las dependencias estén en `requirements.txt`

---

## 📚 Recursos Adicionales

- [Documentación de GitHub Actions](https://docs.github.com/en/actions)
- [Documentación de Databricks Repos](https://docs.databricks.com/repos/index.html)
- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html)
- [pytest Documentation](https://docs.pytest.org/)

---

## 🚀 Próximos Pasos

1. Agrega más notebooks y tests
2. Configura notificaciones de Slack para failures
3. Implementa estrategias de branching (dev, staging, prod)
4. Agrega validación de código con linters (flake8, black)
5. Configura Databricks Jobs para ejecutar workflows después del deploy

---

**Autor**: Tutorial creado para `databricks-projects`  
**Fecha**: Febrero 2026  
**Versión**: 1.0
