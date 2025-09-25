
# -*- coding: utf-8 -*-
# ==============================================================================
# TÍTULO: MERCADO DE BIENES (CRUZ KEYNESIANA)
# ==============================================================================
"""
Análisis Interactivo del Mercado de Bienes (Economía Abierta - Modelo IS)

Este script visualiza el modelo de la Cruz Keynesiana para una economía abierta.
Permite al usuario manipular componentes clave del Gasto Agregado para
observar su impacto en el Ingreso de Equilibrio de forma interactiva.
"""

# ------------------------------------------------------------------------------
# SECCIÓN 1: IMPORTACIÓN DE LIBRERÍAS
# ------------------------------------------------------------------------------
# Se importan las librerías necesarias para los cálculos numéricos (numpy),
# la creación de gráficos (matplotlib) y los componentes interactivos (ipywidgets).
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# ------------------------------------------------------------------------------
# SECCIÓN 2: FUNCIÓN PRINCIPAL PARA CREAR LA INTERFAZ
# ------------------------------------------------------------------------------
# Se encapsula toda la lógica en una función principal para mantener el código
# organizado y reutilizable.
def crear_grafica_mercado_bienes():
    """
    Crea y devuelve una interfaz de usuario interactiva para el modelo
    del mercado de bienes y servicios en una economía abierta.
    """
    # --- 2.1. Creación de Widgets de la Interfaz ---
    # Aquí se definen todos los elementos interactivos que el usuario verá.

    # 'plot_output' es el lienzo donde se dibujará nuestra gráfica.
    plot_output = widgets.Output()

    # Layout para estandarizar el ancho de los sliders.
    slider_layout = widgets.Layout(width='80%')

    # Creación de etiquetas y sliders para cada parámetro del modelo.
    # Cada slider controla una variable económica.
    gasto_label = widgets.Label("Gasto Público (g0):")
    gasto_slider = widgets.FloatSlider(value=200, min=100, max=300, step=10, layout=slider_layout, readout_format='.0f')

    tasa_label = widgets.Label("Tasa Impositiva (t1):")
    tasa_slider = widgets.FloatSlider(value=0.2, min=0.1, max=0.5, step=0.05, layout=slider_layout, readout_format='.2f')

    inversion_label = widgets.Label("Inversión Autónoma (i0):")
    inversion_slider = widgets.FloatSlider(value=150, min=50, max=250, step=10, layout=slider_layout, readout_format='.0f')

    nx_label = widgets.Label("Export. Netas Autónomas (nx0):")
    nx_slider = widgets.FloatSlider(value=100, min=-50, max=200, step=10, layout=slider_layout, readout_format='.0f')

    # --- 2.2. Función de Dibujo de la Gráfica ---
    # Esta función contiene la lógica económica y de visualización.
    # Se ejecuta cada vez que un slider cambia de valor.
    def dibujar_grafica(g0, t1, i0, nx0):
        # El bloque 'with' asegura que la gráfica se dibuje en el widget 'plot_output'.
        with plot_output:
            # Limpia la gráfica anterior para evitar superposiciones al actualizar.
            plot_output.clear_output(wait=True)

            # Parámetros fijos del modelo.
            c0 = 50   # Consumo autónomo (asumido)
            c1 = 0.6  # Propensión Marginal a Consumir

            # --- Subsección 2.2.1: Cálculos del Modelo Económico ---
            # 'alpha' es el multiplicador keynesiano.
            alpha = 1 / (1 - c1 * (1 - t1))
            # 'A' es la suma de todos los componentes autónomos del gasto.
            A = c0 + i0 + g0 + nx0
            # 'Y_eq' es el ingreso de equilibrio, donde la producción iguala al gasto.
            Y_eq = alpha * A

            # --- Subsección 2.2.2: Creación de la Gráfica con Matplotlib ---
            fig, ax = plt.subplots(figsize=(10, 7))
            
            # MODIFICACIÓN: Se define un rango FIJO para los ejes.
            Y_MAX_FIJO = 2500
            Y_range = np.linspace(0, Y_MAX_FIJO, 100)
            
            # 'DA' es la función de Gasto Agregado (Demanda Agregada).
            DA = A + c1 * (1 - t1) * Y_range
            
            # Dibujar la línea de 45 grados (condición de equilibrio Y = DA).
            ax.plot(Y_range, Y_range, color='black', linestyle='--', alpha=0.7, label='Y = DA (Condición de Equilibrio)')
            # Dibujar la curva de Gasto Agregado.
            ax.plot(Y_range, DA, color='deepskyblue', linewidth=3, label='Gasto Agregado (DA)')
            # Marcar el punto de equilibrio en la gráfica.
            ax.plot(Y_eq, Y_eq, 'o', color='red', markersize=10, label=f'Punto de Equilibrio (Y={Y_eq:.1f})')
            # Añadir líneas de guía punteadas desde el equilibrio hacia los ejes.
            ax.vlines(Y_eq, 0, Y_eq, color='red', linestyle=':', alpha=0.8)
            ax.hlines(Y_eq, 0, Y_eq, color='red', linestyle=':', alpha=0.8)

            # --- Subsección 2.2.3: Estilo y Formato de la Gráfica ---
            ax.set_title(f"Multiplicador: {alpha:.2f} | Ingreso de Equilibrio: {Y_eq:.1f}", fontsize=16)
            ax.set_xlabel("Ingreso / Producción (Y)", fontsize=12)
            ax.set_ylabel("Gasto Agregado (DA)", fontsize=12)
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc="upper left")
            
            # MODIFICACIÓN: Se establecen límites fijos para los ejes X e Y.
            ax.set_xlim(left=0, right=Y_MAX_FIJO)
            ax.set_ylim(bottom=0, top=Y_MAX_FIJO)

            plt.tight_layout() # Ajusta el layout para que no se corten las etiquetas.
            plt.show()         # Muestra la gráfica en el output.

    # --- 2.3. Lógica de Interacción (Observadores) ---
    # Esta sección conecta los sliders con la función de dibujo.
    def on_value_change(change):
        # Llama a la función de dibujo con los valores actuales de todos los sliders.
        dibujar_grafica(gasto_slider.value, tasa_slider.value, inversion_slider.value, nx_slider.value)

    # Se "observa" cada slider; si su 'value' cambia, se llama a la función 'on_value_change'.
    for slider in [gasto_slider, tasa_slider, inversion_slider, nx_slider]:
        slider.observe(on_value_change, names='value')
    
    # --- 2.4. Organización y Visualización de la Interfaz de Usuario (UI) ---
    # Se agrupan los widgets de forma ordenada para presentarlos al usuario.
    
    # Se crea una caja vertical para los controles.
    controles = widgets.VBox([
        widgets.VBox([gasto_label, gasto_slider]),
        widgets.VBox([tasa_label, tasa_slider]),
        widgets.VBox([inversion_label, inversion_slider]),
        widgets.VBox([nx_label, nx_slider])
    ], layout=widgets.Layout(width='400px'))
    
    # Se combinan los controles (izquierda) y la gráfica (derecha) en una caja horizontal.
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))
    
    # --- 2.5. Llamada Inicial para Dibujar la Gráfica ---
    # Se llama a la función una vez al principio para que la gráfica aparezca
    # con los valores iniciales de los sliders.
    on_value_change(None)
    
    # Finalmente, la función devuelve la interfaz completa.
    return ui

# ------------------------------------------------------------------------------
# SECCIÓN 3: EJECUCIÓN Y VISUALIZACIÓN
# ------------------------------------------------------------------------------
# Para mostrar la interfaz interactiva en el cuaderno de Jupyter,
# simplemente llamamos a la función principal.
display(crear_grafica_mercado_bienes())










# -*- coding: utf-8 -*-
# ==============================================================================
# TÍTULO: ANÁLISIS INTERACTIVO DEL MERCADO DE DINERO
# ==============================================================================
"""
Análisis Interactivo del Mercado de Dinero (Modelo LM)

Este script visualiza el modelo de equilibrio en el mercado monetario.
Permite al usuario manipular la oferta monetaria, el nivel de ingreso y
el nivel de precios para observar su impacto en la tasa de interés de equilibrio.
"""

# ------------------------------------------------------------------------------
# SECCIÓN 1: IMPORTACIÓN DE LIBRERÍAS
# ------------------------------------------------------------------------------
# Se importan las librerías necesarias para los cálculos numéricos (numpy),
# la creación de gráficos (matplotlib) y los componentes interactivos (ipywidgets).
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# ------------------------------------------------------------------------------
# SECCIÓN 2: FUNCIÓN PRINCIPAL PARA CREAR LA INTERFAZ
# ------------------------------------------------------------------------------
# Se encapsula toda la lógica en una función principal para mantener el código
# organizado y reutilizable.
def crear_grafica_mercado_dinero():
    """
    Crea y devuelve una interfaz de usuario interactiva para el modelo
    del mercado de dinero.
    """
    # --- 2.1. Creación de Widgets de la Interfaz ---
    # Aquí se definen todos los elementos interactivos que el usuario verá.

    # 'plot_output' es el lienzo donde se dibujará nuestra gráfica.
    plot_output = widgets.Output()

    # Layout para estandarizar el ancho de los sliders.
    slider_layout = widgets.Layout(width='80%')

    # Creación de etiquetas y sliders para cada parámetro del modelo.
    oferta_label = widgets.Label("Oferta Monetaria (Ms):")
    oferta_slider = widgets.FloatSlider(value=150, min=50, max=250, step=10, layout=slider_layout, readout_format='.0f')

    ingreso_label = widgets.Label("Nivel de Ingreso (Y):")
    ingreso_slider = widgets.FloatSlider(value=800, min=500, max=1500, step=25, layout=slider_layout, readout_format='.0f')
    
    precio_label = widgets.Label("Nivel de Precios (P):")
    precio_slider = widgets.FloatSlider(value=1, min=0.5, max=2, step=0.1, layout=slider_layout, readout_format='.1f')

    # --- 2.2. Función de Dibujo de la Gráfica ---
    # Esta función contiene la lógica económica y de visualización.
    # Se ejecuta cada vez que un slider cambia de valor.
    def dibujar_grafica(Ms, Y, P):
        # El bloque 'with' asegura que la gráfica se dibuje en el widget 'plot_output'.
        with plot_output:
            # Limpia la gráfica anterior para evitar superposiciones al actualizar.
            plot_output.clear_output(wait=True)

            # Parámetros fijos del modelo de demanda de dinero: L = kY - hi
            k = 0.5   # Sensibilidad de la demanda de dinero al ingreso
            h = 10    # Sensibilidad de la demanda de dinero a la tasa de interés

            # --- Subsección 2.2.1: Cálculos del Modelo Económico ---
            # La oferta real de dinero es la oferta nominal (Ms) dividida por el nivel de precios (P).
            Ms_real = Ms / P
            # Se despeja 'i' de la condición de equilibrio Ms/P = kY - hi.
            i_eq = (k * Y - Ms_real) / h

            # --- Subsección 2.2.2: Creación de la Gráfica con Matplotlib ---
            fig, ax = plt.subplots(figsize=(10, 7))
            
            # Se definen rangos FIJOS para los ejes para una visualización estable.
            I_MAX_FIJO = 50
            M_MAX_FIJO = 500
            i_range = np.linspace(0, I_MAX_FIJO, 100)
            
            # Se calcula la Demanda de Dinero (Md) para cada nivel de 'i'.
            Md = k * Y - h * i_range
            
            # Dibujar la curva de Demanda de Dinero (Md).
            ax.plot(Md, i_range, color='orange', linewidth=3, label=f'Demanda de Dinero (Md)')
            # Dibujar la línea vertical de Oferta Real de Dinero (Ms/P).
            ax.axvline(x=Ms_real, color='skyblue', linewidth=3, linestyle='-', label='Oferta Real (Ms/P)')
            # Marcar el punto de equilibrio.
            ax.plot(Ms_real, i_eq, 'o', color='black', markersize=10, label=f'Equilibrio (i={i_eq:.2f})')
            # Añadir línea de guía horizontal desde el equilibrio.
            ax.hlines(i_eq, 0, Ms_real, color='black', linestyle=':', alpha=0.8)

            # --- Subsección 2.2.3: Estilo y Formato de la Gráfica ---
            ax.set_title(f"Tasa de Interés de Equilibrio: {i_eq:.2f}%", fontsize=16)
            ax.set_xlabel("Cantidad Real de Dinero (M/P)", fontsize=12)
            ax.set_ylabel("Tasa de Interés (i)", fontsize=12)
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc="upper right")
            
            # Se establecen límites fijos para los ejes.
            ax.set_xlim(left=0, right=M_MAX_FIJO)
            ax.set_ylim(bottom=0, top=I_MAX_FIJO)

            plt.tight_layout()
            plt.show()

    # --- 2.3. Lógica de Interacción (Observadores) ---
    # Esta sección conecta los sliders con la función de dibujo.
    def on_value_change(change):
        # Llama a la función de dibujo con los valores actuales de todos los sliders.
        dibujar_grafica(oferta_slider.value, ingreso_slider.value, precio_slider.value)

    # Se "observa" cada slider; si su 'value' cambia, se llama a 'on_value_change'.
    for slider in [oferta_slider, ingreso_slider, precio_slider]:
        slider.observe(on_value_change, names='value')

    # --- 2.4. Organización y Visualización de la Interfaz de Usuario (UI) ---
    # Se agrupan los widgets de forma ordenada para presentarlos al usuario.
    
    # Se crea una caja vertical para los controles.
    controles = widgets.VBox([
        widgets.VBox([oferta_label, oferta_slider]),
        widgets.VBox([ingreso_label, ingreso_slider]),
        widgets.VBox([precio_label, precio_slider])
    ], layout=widgets.Layout(width='400px'))
    
    # Se combinan los controles (izquierda) y la gráfica (derecha) en una caja horizontal.
    ui = widgets.HBox([controles, plot_output], layout=widgets.Layout(align_items='center'))

    # --- 2.5. Llamada Inicial para Dibujar la Gráfica ---
    # Se llama a la función una vez al principio para que la gráfica aparezca
    # con los valores iniciales de los sliders.
    on_value_change(None)

    # Finalmente, la función devuelve la interfaz completa.
    return ui

# ------------------------------------------------------------------------------
# SECCIÓN 3: EJECUCIÓN Y VISUALIZACIÓN
# ------------------------------------------------------------------------------
# Para mostrar la interfaz interactiva en el cuaderno de Jupyter,
# simplemente llamamos a la función principal.
display(crear_grafica_mercado_dinero())
