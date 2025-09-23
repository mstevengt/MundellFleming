# Dashboard Interactivo del Modelo Mundell-Fleming

Este proyecto es una herramienta educativa e interactiva para visualizar el **modelo Mundell-Fleming** de una economía abierta con perfecta movilidad de capitales y tipos de cambio flexibles. El dashboard, desarrollado en un Jupyter Notebook con Python, permite a estudiantes y entusiastas de la macroeconomía explorar cómo diferentes shocks de política afectan el equilibrio de la producción (Y) y el tipo de cambio (e).



---

## 🚀 Características Principales

* **Visualización en Cuatro Cuadrantes:** Muestra simultáneamente los cuatro mercados interconectados del modelo:
    1.  **Mercado Cambiario (UIP):** La relación entre la tasa de interés y el tipo de cambio.
    2.  **Equilibrio DD-AA:** El equilibrio principal entre el mercado de bienes (curva DD) y el mercado de activos (curva AA).
    3.  **Mercado de Dinero:** El equilibrio entre la oferta y la demanda de saldos monetarios reales.
    4.  **Demanda Agregada (Cruz Keynesiana):** El equilibrio en el mercado de bienes.
* **Dashboard Interactivo:** Utiliza `ipywidgets` para crear controles deslizantes y casillas de verificación que permiten modificar los parámetros del modelo en tiempo real.
    * 📈 **Shock de Demanda:** Simula una política fiscal (cambios en el gasto público o impuestos).
    * 💵 **Shock Monetario:** Simula una política monetaria (cambios en la oferta de dinero).
    * 🌍 **Tasa de Interés Mundial (i\*):** Ajusta el ancla de la tasa de interés internacional.
* **Mecanismo de Ajuste Dinámico:** ⚙️ Una funcionalidad clave que muestra visualmente, paso a paso, cómo la economía se mueve de un equilibrio inicial (A) a un nuevo equilibrio (B) después de un shock, con anotaciones que explican la secuencia lógica de los eventos.

---

## 🧠 El Modelo

El dashboard conecta las diferentes partes del modelo Mundell-Fleming para mostrar cómo un cambio en un mercado afecta a los demás.

* **Cuadrante 3 (Mercado de Dinero):** Un shock monetario (cambio en $M^s/P$) altera la **tasa de interés interna (i)**.
* **Cuadrante 1 (Mercado Cambiario):** La nueva tasa de interés interna, comparada con la tasa mundial ($i^*$), provoca flujos de capital que alteran el **tipo de cambio (e)** según la Paridad de Tasas de Interés (UIP).
* **Cuadrante 2 (Equilibrio DD-AA):** Los cambios en `e` (que desplazan la curva AA) y los shocks de demanda (que desplazan la curva DD) determinan el nuevo nivel de **producción (Y)** y **tipo de cambio (e)** de equilibrio.
* **Cuadrante 4 (Demanda Agregada):** Muestra cómo los shocks de demanda y los cambios en las exportaciones netas (influenciadas por `e`) impactan el gasto total y el equilibrio de la producción.

---

## 🛠️ Cómo Usarlo

Una vez que ejecutes el código en un entorno de Jupyter, aparecerá el dashboard interactivo.

1.  **Ajusta los Sliders:**
    * Mueve el slider **"Shock Demanda"** para simular una expansión (valor > 0) o contracción (valor < 0) fiscal. Observarás cómo se desplaza la curva DD.
    * Mueve el slider **"Shock Monetario"** para simular una expansión o contracción monetaria. Verás el desplazamiento de la curva AA.
2.  **Activa el Mecanismo de Ajuste:**
    * Marca la casilla **"⚙️ Mostrar Mecanismo de Ajuste"**.
    * Ahora, cuando apliques un shock, el gráfico mostrará el equilibrio inicial en gris y el nuevo equilibrio en color.
    * Aparecerán **flechas y cajas de texto numeradas** que explican la cadena de eventos económicos: por qué cae la tasa de interés, cómo eso deprecia la moneda y por qué finalmente aumenta la producción, por ejemplo.

---

## 💻 Instalación y Ejecución

Para ejecutar este proyecto en tu máquina local, necesitarás tener Python y un entorno de Jupyter.

1.  **Prerrequisitos:**
    * Python 3.x
    * Jupyter Notebook, JupyterLab o VS Code con la extensión de Jupyter.

2.  **Clonar el Repositorio (Opcional):**
    ```bash
    git clone <URL-del-repositorio>
    cd <nombre-del-repositorio>
    ```

3.  **Instalar las Dependencias:**
    Abre una terminal y ejecuta el siguiente comando para instalar las librerías necesarias:
    ```bash
    pip install numpy matplotlib ipywidgets
    ```

4.  **Ejecutar el Notebook:**
    Navega hasta el directorio del proyecto en tu terminal y lanza Jupyter:
    ```bash
    jupyter lab
    ```
    O si usas Jupyter Notebook clásico:
    ```bash
    jupyter notebook
    ```
    Finalmente, abre el archivo `MundellFleming.ipynb` y ejecuta la celda de código.

---

## 📂 Estructura del Código

El código está organizado de manera modular para facilitar su lectura y mantenimiento:

1.  **Importación de Librerías:** Carga `numpy`, `matplotlib` y `ipywidgets`.
2.  **Configuración del Modelo y Estilo:** Centraliza todos los parámetros económicos base (`MODELO_PARAMS`) y la paleta de colores.
3.  **Función de Cálculo (`calcular_modelo`):** Contiene toda la lógica económica. Recibe los shocks como entrada y devuelve un diccionario con todos los datos calculados, separando la matemática de la visualización.
4.  **Funciones de Gráficos (`plot_...`):** Funciones especializadas, cada una responsable de dibujar un cuadrante del dashboard.
5.  **Lógica de Ajuste y Anotaciones (`anotar_ajuste`):** La función que añade las flechas y explicaciones dinámicas cuando se activa el modo de ajuste.
6.  **Función Principal del Dashboard:** Orquesta todo el proceso: llama a los cálculos, configura la figura y coordina a las funciones de graficado.
7.  **Creación de la Interfaz:** Llama a `interact` para conectar los widgets a la función principal del dashboard.
