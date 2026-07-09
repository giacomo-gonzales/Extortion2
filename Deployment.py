import streamlit as st
import pandas as pd
import joblib


# ==========================
# CONFIGURACIÓN
# ==========================

st.set_page_config(
    page_title="Predicción de Extorsiones",
    page_icon="🚔",
    layout="wide"
)


# ==========================
# CARGAR MODELO
# ==========================

modelo = joblib.load("modelo_extorsiones.pkl")


# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🚔 Sobre el Proyecto")

st.sidebar.info(
"""
Sistema Inteligente de Predicción de Extorsiones.

Modelo de Machine Learning que estima
la cantidad de extorsiones según:

• Distrito
• Mes
• Año

Tecnologías:

• Python
• Scikit-Learn
• Pandas
• Streamlit
"""
)


# ==========================
# TÍTULO
# ==========================

st.title("🚔 Sistema Inteligente de Predicción de Extorsiones")

st.write(
"""
Aplicación de Inteligencia Artificial que utiliza
Machine Learning para estimar la cantidad de
extorsiones en un distrito determinado.
"""
)

st.divider()


# ==========================
# ENTRADAS
# ==========================

st.subheader("📊 Datos de Entrada")


with st.form("formulario_prediccion"):

    columna1, columna2 = st.columns(2)


    with columna1:

        distrito = st.selectbox(
            "Distrito",
            [
                "Comas",
                "Cercado de Lima",
                "SJL",
                "Miraflores",
                "San Borja"
            ]
        )


        anio = st.slider(
            "Año",
            2020,
            2030,
            2026
        )


    with columna2:

        mes = st.selectbox(
            "Mes",
            [
                "Enero",
                "Febrero",
                "Marzo",
                "Abril",
                "Mayo",
                "Junio",
                "Julio",
                "Agosto",
                "Septiembre",
                "Octubre",
                "Noviembre",
                "Diciembre"
            ]
        )


    boton = st.form_submit_button(
        "🔍 Realizar Predicción"
    )


# ==========================
# PREDICCIÓN
# ==========================

if boton:


    # Convertir mes a número

    meses = {
        "Enero":1,
        "Febrero":2,
        "Marzo":3,
        "Abril":4,
        "Mayo":5,
        "Junio":6,
        "Julio":7,
        "Agosto":8,
        "Septiembre":9,
        "Octubre":10,
        "Noviembre":11,
        "Diciembre":12
    }


    mes_numero = meses[mes]


    # Codificación del distrito

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



    # ==========================
    # DATOS PARA EL MODELO
    # ==========================

    datos = pd.DataFrame({

        "Mes":[mes_numero],

        "Año":[anio],

        "Población":[598000],

        "Num_bodegas":[5200],

        "Patrullajes":[40],

        "Distrito_Cercado de Lima":[cercado],

        "Distrito_Comas":[comas],

        "Distrito_Miraflores":[miraflores],

        "Distrito_SJL":[sjl],

        "Distrito_San Borja":[sanborja]

    })


    # Predicción

    resultado = modelo.predict(datos)

    valor = resultado[0]


    st.divider()

    st.subheader("📈 Resultado")


    col1, col2, col3 = st.columns(3)


    with col1:
    
        st.metric(
            "Extorsiones estimadas",
            f"{valor:.0f}"
        )
    
    
    with col2:
    
        st.metric(
            "Distrito",
            distrito
        )
    
    
    with col3:
    
        st.metric(
            "Año",
            anio
        )


    st.divider()


    st.subheader("🚦 Nivel de Riesgo")


    if valor <= 5:

        st.success(
            "🟢 RIESGO BAJO"
        )


    elif valor <= 12:

        st.warning(
            "🟡 RIESGO MEDIO"
        )


    elif valor <= 18:

        st.warning(
            "🟠 RIESGO ALTO"
        )


    else:

        st.error(
            "🔴 RIESGO MUY ALTO"
        )


# ==========================
# PIE
# ==========================

st.divider()

st.caption(
"Proyecto de Inteligencia Artificial | Despliegue de Modelo Machine Learning"
)
