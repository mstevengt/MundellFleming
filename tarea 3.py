#   ----------------------------------------------------------------------------
#   Programación I 
#   HW3: coloque las funciones utilizadas en los ejercicios. No
#   defina otras variables o valores en este módulo.
#   ----------------------------------------------------------------------------
import numpy as np
import pandas as pd 
#Importando librerías 

# ----------------------------------------------
# Ejercicio 1
# ----------------------------------------------
def load_mean(filename: str):
    # Cargar el archivo .npy
    data = np.load(filename)
    #Calcular el promedio general del arreglo
    promedio = np.mean(data)
    return promedio

assert abs(load_mean("data.npy") - 316.8075) < 1e-4

# ----------------------------------------------
# Ejercicio 2
# ----------------------------------------------
# Recibe una matriz X con las variables en las columnas y observaciones en las
# filas. El vector columna "y" debe tener la misma cantidad de observaciones  
def ols_estimation(X: np.ndarray, y: np.ndarray):
    # Agregar columna de unos para el intercepto
    n = X.shape[0]
    ones = np.ones((n, 1))
    X_design = np.hstack((ones, X))
    
    # Calcular coeficientes OLS
    X_transpose = X_design.T
    XtX = X_transpose @ X_design
    XtX_inv = np.linalg.inv(XtX)
    Xty = X_transpose @ y
    beta_hat = XtX_inv @ Xty
    
    return beta_hat

# Probar la función con los datos de admission
admission = np.load("admission.npy")
X = admission[:, :-1]
y = admission[:, -1][:, None]

betahat = ols_estimation(X, y)
print(betahat)
# ----------------------------------------------
# Ejercicio 3
# ----------------------------------------------
# Devuelve los puntos que anotaría Curry en un cuarto de juego (1 realización)
def curry_one_quarter():
    # Parámetros de la simulación
    num_simulaciones = 10000
    num_intervalos = 20  #20 intervalos de 30 segundos en un cuarto de juego

    resultados_finales = []
    for i in range(num_simulaciones):
        puntos = 0
        for j in range(num_intervalos):
            # Simular si Curry anota un triple (probabilidad 0.45)
            if np.random.rand() < 0.45:
                puntos += 3
            # Simular si Curry anota un doble (probabilidad 0.55)
            if np.random.rand() < 0.55:
                puntos += 2
        resultados_finales.append(puntos)
    return np.mean(resultados_finales)
print(curry_one_quarter())

# ----------------------------------------------
# Ejercicio 4
# ----------------------------------------------
import numpy as np

def logistic(x0, r, n=100):
    """
    Calcula la secuencia del mapa logístico.

    Args:
        x0 (float): El valor inicial de la secuencia (entre 0 y 1).
        r (float): El parámetro de crecimiento.
        n (int): El número total de iteraciones a generar.

    Returns:
        np.ndarray: Un arreglo de NumPy con los n valores de la secuencia.
    """
    # Se crea un arreglo de ceros para almacenar los resultados
    x = np.zeros(n)
    # Se establece el primer valor como el valor inicial x0
    x[0] = x0
    
    # Se itera para calcular los n-1 valores restantes
    for i in range(1, n):
        # Se aplica la fórmula del mapa logístico
        x[i] = r * x[i-1] * (1 - x[i-1])
        
    return x

def stable_values(r, x0=0.25, n=500):
    """
    Encuentra los valores estables de la secuencia logística para un 'r' dado.

    Primero genera una secuencia larga, descarta los valores iniciales
    (fase transitoria) y luego identifica los valores únicos a los que
    converge la secuencia.

    Args:
        r (float): El parámetro de crecimiento.
        x0 (float): El valor inicial de la secuencia.
        n (int): El número total de iteraciones a generar.

    Returns:
        np.ndarray: Un arreglo de NumPy ordenado con los valores estables
                    (redondeados a 3 decimales).
    """
    # 1. Se genera la secuencia completa usando la función anterior
    sequence = logistic(x0, r, n=n)
    
    # 2. Se descartan los primeros 200 valores (la fase transitoria)
    transient_removed = sequence[200:]
    
    # 3. Se redondean los valores restantes a 3 decimales
    rounded_values = np.round(transient_removed, 3)
    
    # 4. Se obtienen los valores únicos y se devuelven (np.unique también ordena)
    stable = np.unique(rounded_values)
    
    return stable

# ----------------------------------------------
# Ejercicio 5
# ----------------------------------------------

# Number of unique countries
def get_number_unique_countries(df: pd.DataFrame) -> int:
    """
    Calculates the number of unique countries in the DataFrame.
    """
    return df['name'].nunique()

# Top 10 countries with highest local price
def get_top10_local_price(df: pd.DataFrame) -> set:
    """
    Finds the top 10 countries with the highest local_price.
    """
    # Ordena el DataFrame por 'local_price' de mayor a menor
    top_10 = df.sort_values(by='local_price', ascending=False).head(10)
    
    # Extrae los nombres de los países y los convierte a un conjunto
    return set(top_10['name'])

# Median of prices in july 2024
def get_median(df: pd.DataFrame) -> float:
    """
    Calculates the median dollar_price for entries from July 2024.
    """
    # Copia para evitar SettingWithCopyWarning
    df_copy = df.copy()
    
    # Convierte la columna 'date' a formato de fecha para poder filtrar
    df_copy['date'] = pd.to_datetime(df_copy['date'])
    
    # Filtra las filas para quedarte solo con las de julio de 2024
    july_2024_df = df_copy[df_copy['date'].dt.strftime('%Y-%m') == '2024-07']
    
    # Calcula la mediana de la columna 'dollar_price' de los datos filtrados
    return july_2024_df['dollar_price'].median()

# Mean adjusted prices for a given country
def get_mean_adj_price(df: pd.DataFrame, country: str) -> float:
    """
    Calculates the mean adjusted price for a specific country.
    """
    # Filtra el DataFrame para obtener solo las filas del país especificado
    country_df = df[df['name'] == country]
    
    # Calcula la media de la columna 'adj_price' para ese país
    return country_df['adj_price'].mean()