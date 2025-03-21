#Librerias

import os
import pandas as pd 
from functools import reduce

#Ruta del archivo 
file_path = 'C:\\Users\\Usuario\\Desktop\\Pruebas_tecnicas\\MARKETING_ANALYST_PROYECT\\data\\base_clientes.xlsx'

#Extraer archivo y separar BD
excel_file = pd.ExcelFile(file_path)

dataframes_file = {sheet_name: excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names}

df_canales = dataframes_file['canal']
df_canales.columns

df_trx = dataframes_file['transacciones']
df_trx.columns

df_seg = dataframes_file['Segmento']
df_seg.columns

df_perf = dataframes_file['Perfil']
df_perf.columns


# Unimos las bases por el id del cliente 

dataframes_to_merge = [df_canales, df_trx, df_perf, df_seg]

# Unir todos los DataFrames por la columna 'Clientes'

df_fin = reduce(lambda left, right: pd.merge(left, right, on='Clientes', how='inner'), dataframes_to_merge)

#Visualizamos y exportamos el dataframe resultante
print('Muestra aleatoria de 10 registros BD unidas')
df_fin.sample(10)

output_folder = 'salidas'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
output_file = os.path.join(output_folder, 'BD_clientes_final.csv')
df_fin.to_csv(output_file, index= False)