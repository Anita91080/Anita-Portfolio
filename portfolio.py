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
st.title("Aspiring QA Engineer | Manual Testing | Core Java | SQL")
st.markdown("""
I am a Computer Science graduate passionate about Software Testing and Quality Assurance, with knowledge of Manual Testing, Java, and SQL. I am interested in identifying bugs, improving software quality, and learning new testing technologies. I aspire to build a career as a QA Engineer by applying my analytical, problem-solving, and testing skills in real-world projects..
""")

st.write("---")

# Main Content Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Experience", "🛠 Technical Projects", "📊 Skills", "🎓 Education & Awards"])

with tab1:
    st.header("Internships")
    
    # DRDO Internship
    with st.expander("Defence Research & Development Organisation (DRDO)", expanded=True):
        st.subheader("Gait Analysis & Biomechanical Assessment")
        st.caption("August 2025 – May 2026")
        st.write("""
        - **Full-Cycle Assessment:** Configured an 18-sensor wearable inertial system to capture high-fidelity motion data across the full human body.
        - **Data Engineering:** Managed the end-to-end data pipeline, transitioning raw sensor outputs into structured Excel datasets for rigorous noise reduction and preprocessing.
        - **Advanced Visualization:** Engineered custom Power BI dashboards to visualize complex gait cycles, specifically mapping stance and swing phases to identify pathological deviations.
        - **Clinical Support:** Calculated key spatial-temporal parameters (cadence, symmetry, joint kinematics) to translate noisy sensor data into clear walking patterns for clinical diagnosis and personalized rehabilitation.
        """)
        st.info("**Skills:** Data Analysis, Python, Data Preparation, Power BI, SQL")

    

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

    

with tab3:
    st.header("Technical Stack")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### AI & Testing & QA ")
        st.write("- Artificial Intelligence & ML")
        st.write("- Data Analysis")
        st.write("- Manual Testing")
    with c2:
        st.markdown("### Tools & Software")
        st.write("- Power BI ")
        st.write("- SQL")
        st.write("- Microsoft Excel")
    with c3:
        st.markdown("### Development")
        st.write("- Python")
        st.write("- Java")
        

with tab4:
    st.header("Education")
    colA, colB = st.columns([2, 1])
    with colA:
        st.write("**B.Tech in Computer Science and Engineering**")
        st.write("Visveswaraiah Technological University (VTU)")
        st.write("**Score: 8.92 CGPA**")
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
