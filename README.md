# INF292 - Proyecto Optimización: Red Logística de Distribución (Grupo 8)

Este repositorio contiene la implementación del modelo de Programación Lineal Entera Mixta (PLEM) para el diseño y operación óptima de una red de distribución logística de dos escalones (Plantas $\rightarrow$ Centros de Distribución $\rightarrow$ Zonas de Demanda). El objetivo principal es minimizar de manera exacta los costos fijos de apertura de infraestructura y los costos variables de fletes de transporte.

## Estructura del Proyecto

* **`generador_instancias.py`**: Automatiza la creación de las 15 instancias de prueba (Pequeñas, Medianas y Grandes) en formato JSON. Incorpora la semilla estática (`random.seed(42)`) para replicabilidad y el filtro del peor escenario de capacidad para el límite $P$.
* **`solver_gurobi.py`**: Script principal que interactúa con **Gurobi Optimizer** vía `gurobipy`. Lee de forma secuencial la carpeta de instancias, construye las restricciones del modelo matemático e imprime la tabla consolidada con variables, restricciones, iteraciones Símplex, nodos de Branch-and-Bound y costos óptimos ($Z$).


## Requisitos e Instalación

Para ejecutar este proyecto de forma local en tu máquina, necesitas contar con Python 3.10+ y el motor de optimización Gurobi instalado con una licencia activa (académica o comercial).

Instala las librerías necesarias ejecutando en tu terminal:
```bash
pip install gurobipy matplotlib
