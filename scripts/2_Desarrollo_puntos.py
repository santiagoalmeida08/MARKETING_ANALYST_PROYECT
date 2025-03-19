
#Librerias 

import pandas as pd 
from matplotlib.pyplot import plot

df = pd.read_csv('C:\\Users\\Usuario\\Desktop\\Pruebas_tecnicas\\MARKETING_ANALYST_PROYECT\\salidas\\BD_clientes_final.csv')
df.sample(10)

""" 2. Cantidad de clientes por Genero. """

df.columns = df.columns.str.lower()
df.columns

df_genero = df['genero'].value_counts().reset_index().rename(columns= {'count' : 'total_personas'})
df_genero

print('Cantidad de personas por genero:')
print(df_genero)

""" 3.  Entendiendo que la compra promedio es cuanto ha comprado
cada cliente en un periodo determinado, ¿cual es el canal con
mejor compra promedio?"""

#Asumiendo que la informacion del dataframe sea de las ventas trimestrales

df_compra = df.groupby(['canal'])['venta'].mean().reset_index() \
                                        .rename(columns = {'venta' : 'compra_promedio'}) \
                                        .sort_values(by= 'compra_promedio', ascending= False)

df_compra['compra_promedio'] = df_compra['compra_promedio'].astype(int)

# Formatear la columna 'compra_promedio' como moneda
df_compra['compra_promedio'] = df_compra['compra_promedio'].apply(lambda x: "${:,}".format(x))

print('..................................')
print('..................................')
print("Top departamentos con mas compras:")
print(df_compra)



""" 4. ¿Cual es el top 3 clientes para cada segmento según la cantidad
de productos que ha llevado?"""

df_top = df.groupby(['segmento','clientes'])['unidades'].sum().reset_index(inplace= False) \
                                                .rename(columns = {'unidades': 'total_unidades'}) 

# Ordenar por segmento y total de unidades en orden descendente
df_top = df_top.sort_values(by=['segmento', 'total_unidades'], ascending=[False, False])

# Obtener el top 3 clientes por segmento
df_top3_por_segmento = df_top.groupby('segmento').head(3)

print('..................................')
print('..................................')
print("Top 3 clientes por segmento:")
print(df_top3_por_segmento)


"""5. Si tenemos 3 bonos de $100.000, a que clientes le darías este
beneficio. Argumentar respuesta."""

"""
    Para premiar a nuestros clientes nos basaremos en 3 la remanencia, permanencia y el volumen 
    de compra; de esta forma lograremos hacer un analisis justo de los clientes en base a su
    compromiso e interaccion con la empresa.
    
    Asi entonces lo ideal es premiar a 
    
    -Clientes leales
    -Clientes que nos visiten con frecuencia
    -Clientes con grandes volumenes de compra
    
"""

# Crear un DataFrame con factores clave para premiar

df_clientes = df.groupby('clientes').agg({
    'permanencia': 'mean',  
    'recencia': 'mean',    
    'unidades': 'sum'      
}).reset_index()

# Ordenar por alta permanencia, baja recencia y alto volumen de compras
df_clientes = df_clientes.sort_values(by=['permanencia', 'recencia', 'unidades'], 
                                      ascending=[False, True, False])

# Seleccionar los 3 mejores clientes
top_3_clientes = df_clientes.head(3)

# Mostrar los resultados
print('..................................')
print('..................................')
print("Clientes seleccionados para los bonos de $100,000:")
print(top_3_clientes)


