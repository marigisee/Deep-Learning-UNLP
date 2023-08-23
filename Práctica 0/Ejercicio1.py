import pandas as pd

# Creaciom del diccionario
data = {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Jose'],
    'Edad': [20, 26, 18, 22],
    'Pais': ['Argentina', 'Peru', 'Brasil', 'Chile']
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

print('------------------------------------------------------')
# Mostrar los nombres de las columnas
print('Nombre de las columnas:'+str(df.columns))




print('------------------------------------------------------')

# Sea la siguiente persona: Pablo | 30 años | Colombia

pabloData = pd.DataFrame({'Nombre': ['Pablo'], 'Edad': [30], 'Pais': ['Colombia']})

# Forma 1 para agregar la persona al Dataframe
# En esta forma, creamos otro Dataframe pero solamente con los campos pertenecientes a 'Pablo'
# Luego "unimos" dicho Dataframe 'pabloData' con el Dataframe original
df = pd.concat([df, pabloData], ignore_index=True)
df = pd.concat([df, pabloData], ignore_index=True)

print('Dataframe luego de agregar los datos:')
print(df)

print('------------------------------------------------------')
 
# Forma 1 para eliminar un dato 
# Eliminando uno de los pablos utilizando iloc
df = df.iloc[:-1]


# Forma 2 para eliminar un dato 
# Eliminando uno de los pablos utilizando drop()
# df.drop(df.index[-1], inplace=True)

print('Dataframe luego de eliminar los datos:')
print(df)

print('------------------------------------------------------')

#Para modificar el campo país que sea igual a Peru → Perú
df.loc[df['Pais'] == 'Peru', 'Pais'] = 'Perú'


print('Dataframe luego de modificar el campo Peru → Perú :')
print(df)