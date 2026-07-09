import streamlit as st
import pandas as pd
import joblib


# =========================
# CONFIGURACIÓN DE LA PÁGINA
# =========================

st.set_page_config(
    page_title="Extortion Prediction AI",
    page_icon="🚔",
    layout="wide"
)


# =========================
# CARGAR MODELO
# =========================

modelo = joblib.load("modelo_extorsiones.pkl")


# =========================
# SIDEBAR
# =========================

st.sidebar.title("🚔 About the Project")

st.sidebar.info(
"""
## Intelligent Extortion Prediction System

This application uses a Machine Learning model
to estimate the number of extortion incidents.

Input variables:

• District
• Month
• Year
• Population
• Number of stores
• Police patrols

Developed with:
Python + Scikit-Learn + Streamlit
"""
)


# =========================
# TÍTULO PRINCIPAL
# =========================

st.title("🚔 Intelligent Extortion Prediction System")

st.markdown(
"""
This system predicts the estimated number of extortion
incidents using a Machine Learning model trained with
historical crime data.
"""
)

st.divider()


# =========================
# FORMULARIO
# =========================

st.subheader("📊 Input Information")


with st.form("prediction_form"):

    col1, col2 = st.columns(2)


    with col1:

        distrito = st.selectbox(
            "District",
            [
                "Comas",
                "Cercado de Lima",
                "SJL",
                "Miraflores",
                "San Borja"
            ]
        )


        anio = st.number_input(
            "Year",
            min_value=2020,
            max_value=2030,
            value=2026
        )


        poblacion = st.number_input(
            "Population",
            value=598000
        )


    with col2:

        mes = st.selectbox(
            "Month",
            [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]
        )


        bodegas = st.number_input(
            "Number of stores",
            value=5200
        )


        patrullajes = st.number_input(
            "Police patrols",
            value=40
        )


    boton = st.form_submit_button(
        "🔍 Predict Extortion Risk"
    )



# =========================
# PREDICCIÓN
# =========================

if boton:


    # Conversión del mes a número

    meses = {
        "January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12
    }


    mes_num = meses[mes]


    # One-Hot Encoding del distrito

    cercado = 0
    comas = 0
    miraflores = 0
    sjl = 0
    sanborja = 0


    if distrito == "Comas":
        comas = 1

    elif distrito == "Cercado de Lima":
        cercado = 1

    elif distrito == "SJL":
        sjl = 1

    elif distrito == "Miraflores":
        miraflores = 1

    elif distrito == "San Borja":
        sanborja = 1



    # Crear dataframe igual al entrenamiento

    nuevo = pd.DataFrame({

        "Mes":[mes_num],

        "Año":[anio],

        "Población":[poblacion],

        "Num_bodegas":[bodegas],

        "Patrullajes":[patrullajes],

        "Distrito_Cercado de Lima":[cercado],

        "Distrito_Comas":[comas],

        "Distrito_Miraflores":[miraflores],

        "Distrito_SJL":[sjl],

        "Distrito_San Borja":[sanborja]

    })



    # Predicción

    prediccion = modelo.predict(nuevo)

    valor = prediccion[0]



    st.divider()

    st.subheader("📈 Prediction Results")


    # Métricas

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Estimated Extortions",
            f"{valor:.0f}"
        )


    with col2:

        st.metric(
            "District",
            distrito
        )


    with col3:

        st.metric(
            "Year",
            anio
        )



    st.divider()


    # Nivel de riesgo

    st.subheader("🚦 Risk Level")


    if valor <= 5:

        st.success(
            "🟢 LOW RISK"
        )


    elif valor <= 12:

        st.warning(
            "🟡 MEDIUM RISK"
        )


    elif valor <= 18:

        st.warning(
            "🟠 HIGH RISK"
        )


    else:

        st.error(
            "🔴 VERY HIGH RISK"
        )



# =========================
# FOOTER
# =========================

st.divider()

st.caption(
"""
Artificial Intelligence Project | Machine Learning Deployment | 2026
"""
)
