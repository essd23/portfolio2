import streamlit as st
import requests
from PIL import Image
from send_email import send_email

st.set_page_config(page_title="Portfolio Website", page_icon= ":tada:", layout="wide")

img_chatBot = Image.open("images/ChatBot.PNG")
img_schoolManagment = Image.open("images/student managment system.PNG")
new_img_schoolManagment  = img_schoolManagment .resize((700, 500))
img_todo_webApp = Image.open("images/todo-webapp.PNG")
img_WeatherApp = Image.open("images/WeatherApp.PNG").resize((700, 500))



with st.container():
    st.subheader("Hi, I'm Saheed Akinyemi :wave:")
    st.write("I have a Bachelor's Degree in computer Science. I am a Backend Engineer, Network Engineer ."
             " Aiming to leverage my abilities to successfully fill the vacancy at your company. "
             "Welcome to my portfolio website. Below is a link to my GitHub profile.")
    st.write("[GitHub > ](https://github.com/essd23)")

with st.container():
    st.write("___")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """ 
            
        With over two years experience in as a Backend Engineer I've : 
       - Wrote clean code to develop functional web applications
       - Designed robust APIs to support mobile and desktop clients
       - Managed and optimized scalable distributed systems in the cloud
       - Optimized web applications for performance and scalability
       - Developed automated tests to ensure business needs are met, and allow for regression testing
       
       
       """
        )
 #Projects
with st.container():
    st.write("---")
    st.header("My Python Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_chatBot)
    with text_column:
        st.write("""
        A Chatbot that knows specific topic and answers questions regarding that topic.""")
        st.markdown("[View source code]()")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(new_img_schoolManagment)
    with text_column:
        st.write("""
            A desktop PyQt6 GUI app for managing complex university data with an SQL database backend.""")
        st.markdown("[View source code](https://github.com/essd23/Student-management-system)")
        st.markdown("[View App](https://github.com/essd23/Student-management-system)")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_todo_webApp)
        with text_column:
            st.write("""
                  A simple todo web app hosted by Streamlit designed to improve your productivity.""")
            st.markdown("[View source code](https://github.com/essd23/todowebApp)")
            st.markdown("[View App](https://essd23-todowebapp-web-0xuebo.streamlit.app/)")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_WeatherApp)
        with text_column:
            st.write("""
                     A basic Weather designed with Django framework and a weather API.""")
            st.markdown("[View source code](https://github.com/essd23/django-weather-app)")
            st.markdown("[View App](https://django-weather-app-3t0c.onrender.com/)")



        # CONTACT
    with st.container():
         st.write("---")
         st.header("Get In Touch With Me! ")
         st.write("##")

         with st.form(key="email_forms"):
             user_email = st.text_input("Your email address")
             raw_message = st.text_area("Your message ")
             message = f"""\
         Subject: New email from {user_email}

         From: {user_email}
         {raw_message}
         """
             button = st.form_submit_button()
             print(button)
             if button:
                  send_email(message)
                  st.info("Your email was sent successfully")









