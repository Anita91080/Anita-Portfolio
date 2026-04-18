import streamlit as st

# Page Configuration
st.set_page_config(page_title="Anita BPatil | AI & Biomechanics Portfolio", layout="wide")

# Sidebar - Profile & Contact info
with st.sidebar:
    try:
        st.image("anita_professional.png")
    except:
        st.error("Image not found. Ensure 'anita_professional.png' is in your 'aportfolio.py' folder.")
        
    st.title("Anita BPatil")
    st.write("📍 Bengaluru, Karnataka")
    st.write("📧 [anitabpatil91080@gmail.com](mailto:anitabpatil91080@gmail.com)")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/anita-bpatil-1859a0276)")
    st.write("💻 [GitHub](https://github.com/Anita91080)")
    st.write("---")
    st.subheader("Languages")
    st.write("English, Hindi, Kannada")

# Hero Section
st.title("AI & Deep Learning Enthusiast | Gait Analysis Specialist")
st.markdown("""
I am a Computer Science enthusiast passionate about AI and deep learning, with hands-on experience in 
image enhancement and gait analysis. I aspire to innovate in AI-driven solutions that enhance 
quality of life, leveraging my skills in neural networks, data analysis, and cloud AI platforms.
""")

st.write("---")

# Main Content Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Experience", "🛠 Technical Projects", "📊 Skills", "🎓 Education & Awards"])

with tab1:
    st.header("Internships")
    
    # DRDO Internship
    with st.expander("Defence Research & Development Organisation (DRDO)", expanded=True):
        st.subheader("Gait Analysis & Biomechanical Assessment")
        st.caption("August 2025 – June 2026")
        st.write("""
        - **Full-Cycle Assessment:** Configured an 18-sensor wearable inertial system to capture high-fidelity motion data across the full human body.
        - **Data Engineering:** Managed the end-to-end data pipeline, transitioning raw sensor outputs into structured Excel datasets for rigorous noise reduction and preprocessing.
        - **Advanced Visualization:** Engineered custom Power BI dashboards to visualize complex gait cycles, specifically mapping stance and swing phases to identify pathological deviations.
        - **Clinical Support:** Calculated key spatial-temporal parameters (cadence, symmetry, joint kinematics) to translate noisy sensor data into clear walking patterns for clinical diagnosis and personalized rehabilitation.
        """)
        st.info("**Skills:** Data Analysis, Python, Data Preparation, Power BI, SQL")

    # Microsoft/Edunet Internship
    with st.expander("Microsoft-led AI Internship (Edunet Foundation & AICTE)", expanded=False):
        st.subheader("Artificial Intelligence with Azure")
        st.caption("May 2025 – June 2025")
        st.write("""
        - Gained hands-on experience working with Microsoft Azure AI services and learned about cloud-based AI development workflows.
        - Explored real-world applications of artificial intelligence, enhancing understanding of AI solution design across modern industries.
        """)
        st.info("**Skills:** Artificial Intelligence, Machine Learning, Python")

with tab2:
    st.header("Key Technical Projects")
    
    # Image Enhancement
    st.subheader("Image Enhancement using Deep Learning")
    st.caption("March 2024 – August 2024")
    st.write("""
    - Developed and implemented a deep learning-based image restoration pipeline using Python and TensorFlow/Keras to address low-resolution and noise issues.
    - **Architecture:** Leveraged Convolutional Neural Network (CNN) architectures, specifically SRCNN (Super-Resolution CNN), to successfully enhance image clarity and reduce artifacting.
    - **Benchmarking:** Conducted rigorous performance benchmarking using PSNR (Peak Signal-to-Noise Ratio) and SSIM (Structural Similarity Index), ensuring outputs maintained high structural integrity and visual fidelity.
    """)
    st.info("**Skills:** AI, Deep Learning, TensorFlow, Keras")
    
    st.write("---")

    # Gait Data Analysis
    st.subheader("Human Gait Data Analysis Project")
    st.caption("August 2025 – February 2026")
    st.write("""
    - Leveraged Excel and Power BI to preprocess and analyze complex human gait datasets, identifying critical events such as heel strikes and toe-offs.
    - Developed custom Python scripts to automate the visualization of joint angles and clarify walking pattern irregularities.
    - Synthesized metrics into interactive Power BI dashboards to provide actionable insights into knee joint kinematics and overall movement symmetry.
    """)
    st.info("**Skills:** Power BI, SQL, Python")

    st.write("---")

    # Amazon Clone
    st.subheader("Amazon.com Shopping Website Clone")
    st.caption("November 2025 – December 2025")
    st.write("""
    - Developed a high-fidelity front-end clone of the Amazon homepage using HTML and CSS, focusing on a complex, data-heavy e-commerce interface.
    - **Technical Layout:** Implemented advanced CSS techniques, including Flexbox and CSS Grid, to manage multi-layered navigation and responsive product grids.
    - **Design Integrity:** Demonstrated strong command of the Box Model, positioning, and cross-browser styling for a consistent user experience.
    """)
    st.info("**Skills:** HTML, CSS")

with tab3:
    st.header("Technical Stack")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### Data & AI")
        st.write("- Artificial Intelligence & ML")
        st.write("- Deep Learning (CNN / SRCNN)")
        st.write("- Data Analysis & Prep")
        st.write("- Problem Solving")
    with c2:
        st.markdown("### Tools & Software")
        st.write("- Power BI & SQL")
        st.write("- Microsoft Excel")
        st.write("- QT Creator (GUI)")
        st.write("- Azure AI Services")
    with c3:
        st.markdown("### Development")
        st.write("- Python")
        st.write("- HTML & CSS")
        st.write("- Flexbox & CSS Grid")
        st.write("- LaTeX Documentation")

with tab4:
    st.header("Education")
    colA, colB = st.columns([2, 1])
    with colA:
        st.write("**B.Tech in Computer Science and Engineering**")
        st.write("Visveswaraiah Technological University (VTU)")
        st.write("**Score: 8.74 CGPA**")
    with colB:
        st.write("---")
        st.write("**Class XII (Karnataka):** 93% (2022)")
        st.write("**Class X (Karnataka):** 95% (2020)")
    
    st.write("---")
    st.header("Certifications & Awards")
    st.write("- ⭐ **Star Mentee Award:** Certificate of Appreciation for performance by FEE")
    st.write("- 🏆 **Google AI Essentials Certification**")
    st.write("- 🏆 **IBM Z Day 2025:** Security, AI, Data, and Modernization")
    st.write("- 🏆 **Finding Leader In You (FLY) Workshop**")
    st.write("- 🏆 **AI Foundations & Microsoft Excel Analysis**")

# Footer
st.write("---")
st.caption("Anita Appasab BPatil | Professional Portfolio 2026")