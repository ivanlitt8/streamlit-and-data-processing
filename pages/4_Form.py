import streamlit as st

st.title("Formulario de Registro")

with st.form("my_form"):
    # Campo para ingresar el nombre de usuario
    username = st.text_input("Nombre de Usuario:")

    # Campo para ingresar el nombre completo
    full_name = st.text_input("Nombre Completo:")

    # Campo para ingresar el correo electrónico
    email = st.text_input("Correo Electrónico:")

    # Campo para ingresar la fecha de nacimiento
    birth_date = st.date_input("Fecha de Nacimiento:")

    # Campo para seleccionar el género
    gender = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])

    # Botón para enviar el formulario
    submitted = st.form_submit_button("Submit")

# Validaciones después del envío del formulario
if submitted:
    # Validación para asegurarse de que se ingrese el nombre de usuario
    if not username:
        st.warning("Por favor, ingrese el nombre de usuario.")

    # Validación para asegurarse de que se ingrese el nombre completo
    if not full_name:
        st.warning("Por favor, ingrese el nombre completo.")

    # Validación para asegurarse de que se ingrese el correo electrónico
    if not email:
        st.warning("Por favor, ingrese el correo electrónico.")

    # Validación para asegurarse de que se ingrese la fecha de nacimiento
    if not birth_date:
        st.warning("Por favor, seleccione la fecha de nacimiento.")

    # Validación para asegurarse de que se seleccione un género
    if not gender:
        st.warning("Por favor, seleccione el género.")


# Mostrar los datos ingresados por el usuario después de enviar el formulario
if submitted and username and full_name and email and birth_date and gender:
    st.success(f"Nombre de Usuario: {username}")
    st.success(f"Nombre Completo: {full_name}")
    st.success(f"Correo Electrónico: {email}")
    st.success(f"Fecha de Nacimiento: {birth_date}")
    st.success(f"Género: {gender}")