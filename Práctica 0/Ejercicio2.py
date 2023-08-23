import pandas as pd

# Creaciom del diccionario
data = {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Jose'],
    'Edad': [20, 26, 18, 22],
    'Pais': ['Argentina', 'Peru', 'Brasil', 'Chile']
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)


# Sea la siguiente persona: Pablo | 30 años | Colombia

pabloData = pd.DataFrame({'Nombre': ['Pablo'], 'Edad': [30], 'Pais': ['Colombia']})


# Mostrar el DataFrame
print(df)


# Guardar en archivo de texto con delimitador de tabulador
df.to_csv('archivo_delimitador_tab.txt', sep='\t', index=False)

# Guardar en archivo de texto con delimitador de punto y coma
df.to_csv('archivo_delimitador_punto_coma.csv', sep=';', index=False)

# Guardar en archivo Excel
df.to_excel('archivo_excel.xlsx', index=False)

# Guardar en archivo JSON
df.to_json('archivo_json.json', orient='records', indent=4)

