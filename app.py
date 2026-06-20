import streamlit as st
import base64
import os

# Configuración inicial
st.set_page_config(page_title="Portafolio CuencaVerde", page_icon="💧", layout="wide")

# Función para cargar la imagen de fondo de manera robusta
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        # Inyectar CSS para el fondo y el efecto Glassmorphism
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        /* Contenedor principal con efecto cristal */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.90) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border-radius: 24px;
            padding: 3rem 4rem !important;
            margin-top: 3rem;
            margin-bottom: 3rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            max-width: 1200px !important;
        }}
        
        /* Ocultar elementos por defecto de Streamlit que rompen el diseño */
        header {{ visibility: hidden; }}
        #MainMenu {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}
        </style>
        """, unsafe_allow_html=True)

# Llamar a la función del fondo (asegúrate de que el nombre del archivo sea exacto)
set_background("embalse.jpg")

# Inyectar CSS personalizado para fuentes y tarjetas
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;800;900&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
    }

    .hero-title {
        font-size: 3rem !important;
        font-weight: 900 !important;
        background: -webkit-linear-gradient(45deg, #065f46, #0284c7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.2rem !important;
        color: #334155;
        font-weight: 800;
        margin-top: 0;
    }

    /* Estilo Premium para la Cita de Liderazgo */
    .quote-box {
        background: linear-gradient(to right, rgba(6, 95, 70, 0.05), rgba(2, 132, 199, 0.05));
        border-left: 5px solid #065f46;
        padding: 2rem;
        border-radius: 0 16px 16px 0;
        margin: 2rem 0;
        font-style: italic;
    }
    
    .quote-text {
        color: #1e293b;
        font-size: 1.3rem;
        font-weight: 600;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .quote-author {
        color: #065f46;
        font-weight: 800;
        font-size: 1rem;
        text-align: right;
    }

    /* Estilo para simular tarjetas corporativas limpias */
    div[data-testid="stAlert"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        color: #1e293b !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
        transition: all 0.3s ease;
        padding: 1.5rem !important;
        height: 100%;
    }
    
    /* El ícono de las alertas se oculta para un look más limpio */
    div[data-testid="stAlert"] svg {
        display: none;
    }

    div[data-testid="stAlert"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
        border-color: #065f46 !important;
    }

    /* Destacar la tarjeta del ROI y Tributaria */
    .highlight-card {
        border: 2px solid #059669 !important;
        background-color: #f0fdf4 !important;
    }

    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        padding: 0.5rem 2rem !important;
        border: none !important;
        box-shadow: 0 4px 14px 0 rgba(5,150,105,0.39) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- CONTENIDO ---

# Cabecera (Hero Section)
col_logo, col_texto = st.columns([1, 4])
with col_logo:
    st.image("CuencaVerde Logo.jpg", width=140)
with col_texto:
    st.markdown('<p class="hero-title">Invertir en la naturaleza es invertir en nuestro futuro</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Portafolio de Valor Compartido y Servicios Especializados para Asociados y Aliados.</p>', unsafe_allow_html=True)
    st.markdown("*Ser aliado de CuencaVerde trasciende la filantropía; es una inversión estratégica en Seguridad Hídrica; Esencial para la Sostenibilidad.*")

# Cita de Liderazgo (Nuevo componente)
st.markdown("""
<div class="quote-box">
    <div class="quote-text">"TENEMOS LA OPORTUNIDAD DE TRANSFORMAR POSITIVAMENTE NUESTRA REALIDAD COLECTIVA DE ESTE MÁGICO TERRITORIO CON EL QUE ESTAMOS COMPROMETIDOS Y ENTRELAZADOS."</div>
    <div class="quote-author">— MC de La Ossa</div>
</div>
""", unsafe_allow_html=True)

# Sección de Beneficios
st.markdown("<h2 style='color:#0f172a; font-weight:800; margin-top:2rem;'>Nuestra Promesa de Valor</h2>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["🌟 Servicios Especializados y Valor Compartido", "📈 Visión Estratégica ESG"])

with tab1:
    st.markdown("### Decálogo de Beneficios Específicos")
    st.write("") # Espaciador
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.success("**1. Visibilidad Institucional**\n\nInclusión destacada en los Informes Anuales de Gestión.")
        st.success("**4. Asesoría en Reportes**\n\nAcompañamiento técnico para Informes de Sostenibilidad.")
        st.success("**7. Neutralidad Hídrica**\n\nHoja de ruta para alcanzar metas de neutralidad climática.")
        
    with c2:
        st.success("**2. Formación de Alto Nivel**\n\nCupos en espacios sobre seguridad hídrica y conservación.")
        st.success("**5. Medición de Impacto**\n\nCálculo especializado de huellas de agua y carbono corporativas.")
        
        # Tarjeta de ROI
        st.success("<div class='highlight-card'></div>**8. Alto Retorno de Inversión (ROI)**\n\nGarantía de que las inversiones con CuencaVerde en conservación, restauración, o en Prácticas Agropecuarias Sostenibles, tienen un **ROI menor a 10 años y una tasa de retorno superior a 1,5**.")

    with c3:
        st.success("**3. Inteligencia de Datos**\n\nAcceso al Sistema de Inteligencia Hidroterritorial.")
        st.success("**6. Gobernanza del Agua**\n\nVoz activa en la Mesa Territorial de Seguridad Hídrica.")
        st.success("**9. Cumplimiento Normativo**\n\nImplementación de la Ley del Árbol (Ley 2173).")
        # Tarjeta Tributaria
        st.success("**10. Beneficios Tributarios**\n\nDescuento en renta del 25% del valor donado (Estatuto Tributario Colombiano, Art. 257).")

with tab2:
    st.markdown("### Beneficios Clave a Largo Plazo")
    c4, c5 = st.columns(2)
    with c4:
        st.info("**Seguridad Hídrica a Largo Plazo**\nGarantiza disponibilidad y calidad del agua para operaciones.")
        st.info("**Fortalecimiento Reputacional**\nEleva el posicionamiento de marca con un compromiso genuino.")
    with c5:
        st.info("**Cumplimiento de Metas ESG**\nAporta a los ODS e indicadores de sostenibilidad.")
        st.info("**Mitigación de Riesgos**\nReduce vulnerabilidad frente a escasez hídrica.")

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# Sección de Contacto
st.subheader("Eficiencia y Transparencia en su Inversión")
st.write("Aseguramos que sus recursos se ejecuten a través de un mecanismo estructurado, auditable y enfocado en generar resultados cuantificables en el territorio.")

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    st.write("") # Espaciador
    st.button("Contactar al equipo de Alianzas", type="primary", use_container_width=True)
