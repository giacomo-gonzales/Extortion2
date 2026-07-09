import streamlit as st
import pandas as pd
import joblib


# ==========================
# CONFIGURACIÓN DE LA PÁGINA
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
# BARRA LATERAL
# ==========================

st.sidebar.title("🚔 Sobre el Proyecto")

st.sidebar.info(
"""
Sistema Inteligente de Predicción de Extorsiones.

Este proyecto utiliza Machine Learning
para estimar la cantidad de extorsiones
según diferentes características del distrito.

Variables utilizadas:

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
Aplicación basada en Machine Learning para estimar
la cantidad de extorsiones y determinar el nivel
de riesgo según las características ingresadas.
"""
)

st.divider()


# ==========================
# FORMULARIO DE DATOS
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
            min_value=2020,
            max_value=2030,
            value=2026,
            step=1
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


    # Conversión del mes

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

    distrito_cercado = 0
    distrito_comas = 0
    distrito_miraflores = 0
    distrito_sjl = 0
    distrito_sanborja = 0


    if distrito == "Comas":
        distrito_comas = 1

    elif distrito == "Cercado de Lima":
        distrito_cercado = 1

    elif distrito == "SJL":
        distrito_sjl = 1

    elif distrito == "Miraflores":
        distrito_miraflores = 1

    elif distrito == "San Borja":
        distrito_sanborja = 1



    # Crear datos para el modelo

    datos_nuevos = pd.DataFrame({

        "Mes":[mes_numero],

        "Año":[anio],

        "Distrito_Cercado de Lima":[distrito_cercado],

        "Distrito_Comas":[distrito_comas],

        "Distrito_Miraflores":[distrito_miraflores],

        "Distrito_SJL":[distrito_sjl],

        "Distrito_San Borja":[distrito_sanborja]

    })


    # Predicción

    resultado = modelo.predict(datos_nuevos)

    cantidad_extorsiones = resultado[0]


    st.divider()

    st.subheader("📈 Resultado de la Predicción")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Extorsiones estimadas",
            f"{cantidad_extorsiones:.0f}"
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


    # Nivel de riesgo

    st.subheader("🚦 Nivel de Riesgo")


    if cantidad_extorsiones <= 5:

        st.success(
            "🟢 RIESGO BAJO"
        )


    elif cantidad_extorsiones <= 12:

        st.warning(
            "🟡 RIESGO MEDIO"
        )


    elif cantidad_extorsiones <= 18:

        st.warning(
            "🟠 RIESGO ALTO"
        )


    else:

        st.error(
            "🔴 RIESGO MUY ALTO"
        )



# ==========================
# PIE DE PÁGINA
# ==========================

st.divider()

st.caption(
"Proyecto de Inteligencia Artificial | Machine Learning Deployment | 2026"
)
