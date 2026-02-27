import streamlit as st

Menu=st.sidebar.radio("MENU",["HOME","INTERNSHIP","SKILLS","COLLABORATE","CONTACT"])

if Menu=="HOME":
    st.title("Gautham K - Portfolio")
    Name=st.header("Welcome, I am Gautham Krishnan K")
    st.info("B.Tech-Electronics Engineering [VLSI Design and Technology]")
    st.info("SASTRA Deemed University")
    st.subheader("ABOUT")
    st.text("An electronic engineering student who has a great interest towards computer science and software development pursuing a position at a software company to leverage my knowledge and technical skills. Eager to work on real-time and innovative projects and contribute to the growth of the company.")

elif Menu == "INTERNSHIP":
    st.title("INTERNSHIP")
    st.info("TATA Power Solar: Cell Plant - Cell Process")
    st.markdown("""
- Overview of TOPCon & PERC solar PV cell manufacturing. 
- Shop floor operation in solar PV cell manufacturing unit. 
- Electrical parameters of solar cell. 
- Application of automation in solar PV cell manufacturing unit.
""")
    st.info("Sourcesys - Generative AI")
    st.markdown("""
        - SQL,Python
        - Git, GitHub
        - Numpy,Pandas,MatplotLib
        - Streamlit
""")
    
elif Menu=="SKILLS":
    st.title("SKILLS")
    col1,col2,col3=st.columns(3)
    with col1:
             st.info("Programming Languages")
             st.markdown("""
                - C
                - C++
                - Python
                - SQL
                - HTML
                - CSS
                """)
    with col2:
            st.info("Hardware Desciptive Languages")
            st.markdown("""
                - Verilog
                - SystemVerilog
                """)
    with col3:
             st.info("Software Applications")
             st.markdown("""
                - Sentaurus TCAD 
                - Cadence Virtuoso
                - Visual Studio Code
                - ModelSim 
                - Intel Quartus Prime
                - KiCad
                """)
elif Menu=="COLLABORATE":
      st.title("COLLABRATION")
      name=st.text_input("Enter your name")
      email=st.text_input("Enter your email")
      st.text_input("Your message")
      submit=st.button("Send Message")
      if submit:
            if name and email:
                st.success("Thank you for reaching out! I will contact you soon.")
            else:
                st.error("Please fill in all required fields.")
    
elif Menu=="CONTACT":
    st.title("CONTACT")
    st.info("Email")
    st.markdown("gautham2004k@gmail.com")
    st.info("GitHub")
    st.markdown("https://github.com/gauthamKrishnan30")
    st.info("Streamlit")
    st.markdown("https://share.streamlit.io/user/gauthamkrishnan30")
         


