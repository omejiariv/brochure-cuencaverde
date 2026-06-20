import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Portafolio CuencaVerde", page_icon="💧", layout="wide")

# Inyectar CSS personalizado para diseño dinámico e impactante
st.markdown("""
<style>
    /* Importar fuente impactante (Montserrat) de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800;900&display=swap');

    /* Aplicar la nueva fuente a toda la aplicación */
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilo para el título principal (Hero) - Texto con Gradiente */
    .hero-title {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: -webkit-linear-gradient(45deg, #059669, #2563eb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }

    /* Subtítulos */
    .hero-subtitle {
        font-size: 1.4rem !important;
        color: #334155;
        font-weight: 800;
        margin-top: 0;
    }

    /* Estilo para simular tarjetas interactivas en los mensajes de success/info/warning */
    div[data-testid="stAlert"] {
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        padding: 1.5rem !important;
    }
    
    /* Efecto Hover (Levantamiento) al pasar el mouse por los beneficios */
    div[data-testid="stAlert"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
    }

    /* Estilo del Botón de contacto */
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
        padding: 0.75rem 2rem !important;
        border: none !important;
        box-shadow: 0 4px 14px 0 rgba(5,150,105,0.39) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stButton"] button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 6px 20px rgba(5,150,105,0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# Cabecera (Hero Section)
col_logo, col_texto = st.columns([1, 4])
with col_logo:
    st.image("CuencaVerde Logo.jpg", width=160)
with col_texto:
    # Uso de HTML para aplicar el diseño avanzado al título
    st.markdown('<p class="hero-title">Invertir en la naturaleza es invertir en nuestro futuro</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Portafolio de Valor Compartido y Servicios Especializados para Asociados y Aliados.</p>', unsafe_allow_html=True)
    st.markdown("*Ser aliado de CuencaVerde trasciende la filantropía; es una inversión estratégica en Seguridad Hídrica; Esencial para la Sostenibilidad.*")

st.divider()

# Sección de Beneficios usando Tabs
st.header("Nuestra Promesa de Valor")
tab1, tab2 = st.tabs(["🌟 Servicios Especializados y Valor Compartido", "📈 Visión Estratégica ESG"])

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
        
        # EL PUNTO ESTRELLA DEL ROI (Usamos warning para que resalte en amarillo/dorado)
        st.warning("**8. Alto Retorno de Inversión (ROI)**\n\nGarantía de que las inversiones con CuencaVerde en conservación, restauración, o en Prácticas Agropecuarias Sostenibles, tienen un **ROI menor a 10 años y una tasa de retorno superior a 1,5**.")

    with c3:
        st.success("**3. Inteligencia de Datos**\n\nAcceso al Sistema de Inteligencia Hidroterritorial.")
        st.success("**6. Gobernanza del Agua**\n\nVoz activa en la Mesa Territorial de Seguridad Hídrica.")
        st.success("**9. Cumplimiento Normativo**\n\nImplementación de la Ley del Árbol (Ley 2173).")
        st.info("**10. Beneficios Tributarios**\n\nDescuento en renta del 25% del valor donado (Estatuto Tributario Colombiano, Art. 257).")

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

# Centramos el botón usando columnas
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    st.button("Contactar al equipo de Alianzas", type="primary", use_container_width=True)
