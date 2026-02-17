# databricks-projects
Databricks workflows, notebooks, and ETL pipelines for data engineering projects

## CI/CD Pipeline
This repository includes automated CI/CD with GitHub Actions.


## 📚 Documentación

### Tutorial Completo

¿Nuevo en CI/CD con Databricks? Lee nuestro **[Tutorial Completo](TUTORIAL.md)** que incluye:

- ✅ Configuración paso a paso de GitHub y Databricks Repos
- ✅ Implementación de GitHub Actions para tests y deployment
- ✅ Configuración de secrets y tokens
- ✅ Troubleshooting y mejores prácticas
- ✅ Ejemplos de código completos

### Estructura del Proyecto

```
databricks-projects/
├── .github/workflows/     # GitHub Actions CI/CD
├── notebooks/             # Databricks notebooks
├── tests/                 # Tests unitarios
├── requirements.txt       # Dependencias
└── TUTORIAL.md           # Tutorial completo
```

## 🚀 Inicio Rápido

1. Clona este repositorio
2. Sigue las instrucciones en [TUTORIAL.md](TUTORIAL.md)
3. Configura los secrets en GitHub:
   - `DATABRICKS_HOST`
   - `DATABRICKS_TOKEN`
4. Haz push a `main` para activar el pipeline

## 🔄 Pipeline de CI/CD

Cada push a `main` ejecuta:

1. **Tests** - Ejecuta pytest con coverage
2. **Deploy** - Sincroniza notebooks a Databricks (solo si tests pasan)

## 📖 Recursos

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Databricks Repos](https://docs.databricks.com/repos/index.html)
- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html)
