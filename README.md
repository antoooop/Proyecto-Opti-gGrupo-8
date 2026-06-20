# INF292 - Proyecto Optimización: Red Logística de Distribución (Grupo 8)

Este repositorio contiene la implementación del modelo de Programación Lineal Entera Mixta (PLEM) para el diseño y operación óptima de una red de distribución logística de dos escalones (Plantas $\rightarrow$ Centros de Distribución $\rightarrow$ Zonas de Demanda). El objetivo principal es minimizar de manera exacta los costos fijos de apertura de infraestructura y los costos variables de fletes de transporte.

## Estructura del Proyecto

* **`generador_instancias.py`**: Automatiza la creación de las instancias de prueba. Incorpora la semilla estática (`random.seed(42)`) para replicabilidad y un filtro del "peor escenario" para validar la factibilidad matemática del límite $P$.
* **`mis_instancias/`**: Directorio que contiene las 15 instancias generadas (5 Pequeñas, 5 Medianas y 5 Grandes) en formato `.json`, listas para ser consumidas por el modelo.
* **`solver_gurobi.py`**: Script principal que interactúa con **Gurobi Optimizer** vía `gurobipy`. Lee de forma secuencial la carpeta `mis_instancias/`, construye las restricciones y resuelve los modelos, imprimiendo la tabla consolidada de resultados.
* **`hacer_graficos.py`**: Rutina auxiliar en Python que procesa las métricas de la terminal utilizando `matplotlib` para generar visualizaciones.
* **`grafico_tiempo.png` y `grafico_costos.png`**: Gráficos resultantes utilizados en el informe final y la presentación.


## Requisitos e Instalación

Para ejecutar este proyecto de forma local en tu máquina, necesitas contar con Python 3.10+ y el motor de optimización Gurobi instalado con una licencia activa (académica o comercial).

Instala las librerías necesarias ejecutando en tu terminal:
```bash
pip install gurobipy matplotlib
