import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# QuizGen에 오신 것을 환영합니다!👋")

st.markdown(
    """
    AI를 사용하여 MCQs, 참/거짓, 빈칸 채우기, FAQs 와 같은 다양한 퀴즈를 생성해 보세요.   
    
    ---
    ### About QuizGen
    > * 둘러보기 [문서](https://github.com/ShinHyun-soo/QuizGen)
    > * 연락하기 [메일](mailto:2091126@hansung.ac.kr)
    """
)
import streamlit as st
from streamlit_google_auth import Authenticate
import json

#google_credentials = st.secrets["GOOGLE_CREDENTIALS"]

st.title('Streamlit Google Auth Example')

authenticator = Authenticate(
    secret_credentials_path = 'google_credentials.json',
    cookie_name='my_cookie_name',
    cookie_key='this_is_secret',
    redirect_uri = 'http://localhost:8501',
)

# Catch the login event
authenticator.check_authentification()

# Create the login button
authenticator.login()

if st.session_state['connected']:
    st.image(st.session_state['user_info'].get('picture'))
    st.write('Hello, '+ st.session_state['user_info'].get('name'))
    st.write('Your email is '+ st.session_state['user_info'].get('email'))
    if st.button('Log out'):
        authenticator.logout()