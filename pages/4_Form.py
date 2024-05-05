import streamlit as st
import json

def load_data(file_path):
    
    """
    Carga datos del archivo JSON especificado.

    Args:
        file_path (str): Ruta del archivo JSON.

    Returns:
        dict: Diccionario con los datos cargados del archivo.
    """
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

# Función para guardar los datos en el archivo JSON
def save_data(data, file_path):
    """
    Guarda datos en el archivo JSON especificado.

    Args:
        data (dict): Diccionario con los datos a guardar.
        file_path (str): Ruta del archivo JSON.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Ruta del archivo JSON
file_path = "registro.json"

# Cargar datos existentes (si existen)
existing_data = load_data(file_path)

st.title("Formulario de Registro")

with st.form("my_form"):
    
    username = st.text_input("Nombre de Usuario:")  # Campo para nombre de usuario
    full_name = st.text_input("Nombre Completo:")   # Campo para nombre
    email = st.text_input("Correo Electrónico:")    # Campo para correo
    birth_date = st.date_input("Fecha de Nacimiento:")   # Campo para fecha de nacimiento
    gender = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])     # Campo para seleccionar el género

    # Botón para enviar el formulario
    submitted = st.form_submit_button("Submit")

# Validacion después del envío del formulario
if submitted:
    if username and full_name and email and birth_date and gender: # Validar campos no vacios
        # Verificar si el usuario ya está registrado por correo electrónico
        if email in existing_data:
            # Si el usuario ya existe, informar
             st.warning("Ya existe un usuario registrado con este mail.")
        else:
            # Sobrescribir el archivo JSON con los datos actualizados
            existing_data = {
                email: {
                    "Nombre de Usuario": username,
                    "Nombre Completo": full_name,
                    "Fecha de Nacimiento": str(birth_date),
                    "Género": gender
                }
            }         
            save_data(existing_data, file_path)   # Guardar datos en JSON
            st.success("Usuario registrado exitosamente.") # Informar carga exitosa
    else:
        # Mostrar un mensaje de advertencia si no se llenaron todos los campos
        st.warning("Por favor complete todos los campos antes de enviar el formulario.")