import streamlit as st
st.write("lululululullu")

st.set_page_config(
    page_title="Streamlit Test App",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.streamlit.io/docs",
        "Report a bug": "https://www.streamlit.io/docs",
        "About": "# This is my first app",
    }
)
st.markdown("<h1>Hello<h1>", unsafe_allow_html=True)

st.markdown("""

<style>
    button{
    color: white;
    background: red;
    border: 1px solid #ccc;
    padding: 10px;
    width: 100px;
    }
</style>    
<button>Click me</button>


""",unsafe_allow_html=True)

name = st.text_input("Enter your name")
age = st.number_input("Enter your age",min_value=0,max_value=100,value=25)

if st.button("Submit"):
    st.success("Form submitted successfully")
    st.warning("This is a warning")
    st.error("This is an error")
    st.info("This is an info")
    st.write("Hello", name, "you are", age, "years old")

st.markdown("---")
