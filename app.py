import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Portafolio CuencaVerde", page_icon="💧", layout="wide")

# Cabecera (Hero Section)
col_logo, col_texto = st.columns([1, 4])
with col_logo:
    st.image("CuencaVerde Logo_2.jpg", width=180)
with col_texto:
    st.title("Invertir en la naturaleza es asegurar nuestro futuro.")
    st.markdown("#### Portafolio de Valor Compartido y Servicios Especializados para Asociados y Aliados.")
    st.markdown("*Ser aliado de CuencaVerde trasciende la filantropía; es una inversión estratégica para proteger el agua del Valle de Aburrá.*")

st.divider()

# Sección de Beneficios usando Tabs
st.header("Nuestra Promesa de Valor")
tab1, tab2 = st.tabs(["Servicios Especializados y Valor Compartido", "Visión Estratégica ESG"])

with tab1:
    st.markdown("### Decálogo de Beneficios Específicos")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.success("**1. Visibilidad Institucional**\n\nInclusión destacada en los Informes Anuales de Gestión.")
        st.success("**4. Asesoría en Reportes**\n\nAcompañamiento técnico para Informes de Sostenibilidad.")
        st.success("**7. Neutralidad Hídrica**\n\nHoja de ruta para alcanzar metas de neutralidad climática.")
        
    with c2:
        st.success("**2. Formación de Alto Nivel**\n\nCupos en espacios sobre seguridad hídrica y conservación.")
        st.success("**5. Medición de Impacto**\n\nCálculo especializado de huellas de agua y carbono corporativas.")
        st.success("**8. Plataforma Documental**\n\nAcceso a estudios sobre oferta y demanda de agua.")
        st.info("**10. Beneficios Tributarios**\n\nDescuento en renta del 25% del valor donado (Art. 257).")

    with c3:
        st.success("**3. Inteligencia de Datos**\n\nAcceso al Sistema de Inteligencia Hidroterritorial.")
        st.success("**6. Gobernanza del Agua**\n\nVoz activa en la Mesa Territorial de Seguridad Hídrica.")
        st.success("**9. Cumplimiento Normativo**\n\nImplementación de la Ley del Árbol (Ley 2173).")

with tab2:
    st.markdown("### Beneficios Clave a Largo Plazo")
    c4, c5 = st.columns(2)
    with c4:
        st.info("**Seguridad Hídrica a Largo Plazo**\nGarantiza disponibilidad y calidad del agua para operaciones.")
        st.info("**Fortalecimiento Reputacional**\nEleva el posicionamiento de marca con un compromiso genuino.")
    with c5:
        st.info("**Cumplimiento de Metas ESG**\nAporta a los ODS e indicadores de sostenibilidad.")
        st.info("**Mitigación de Riesgos**\nReduce vulnerabilidad frente a escasez hídrica.")

st.divider()

# Sección de Contacto
st.subheader("Eficiencia y Transparencia en su Inversión")
st.write("Aseguramos que sus recursos se ejecuten a través de un mecanismo estructurado, auditable y enfocado en generar resultados cuantificables en el territorio.")
st.button("Contactar al equipo de Alianzas", type="primary")
