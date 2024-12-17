import streamlit as st
from main_chatbot import create_vector_db, get_qa_chain
from PIL import Image
import time
st.set_page_config(page_title='CHATBOT_LARBI_BELAISSAOUI', layout='wide',
                #    initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
)
import streamlit as st

st.markdown(
    """
    <div style="
        background-color: #36454F; 
        padding: 10px; 
        border-radius: 8px; 
        text-align: center;
    ">
        <h1 style='color:#E48400; font-size: 27px;'>
            🤖🚓_RIVA AUTOMOBILES EL JADIDA_CHATBOT_🚗🤖
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)


# Adding background color to the main container
st.markdown(
    """
    <style>
    body {
        background-color: #62D9CE;  /* This sets the background color to green */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    "<h4 style='color:#CCFF00;text-align: center;'>⏭_Project de Stage PFA : LARBI BELAISSAOUI_⏪</h4>",
    unsafe_allow_html=True
)

def cook_breakfast():
    msg = st.toast('hello🎉')
    time.sleep(1)
    msg.toast('🤗wait... ')
    time.sleep(1)
    msg.toast('just few minits', icon = "🌹")
# Button to create new data styling
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #4DD04D;  /* Tomato color */
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.5s ease;
    }

    div.stButton > button:hover {
        background-color: #BFFF00;  /* Darker shade on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def display_bounded_response(response_text):
    st.markdown(
        f"""
        <div style="
            border: 4px solid #4CAF50;
            border-radius: 8px;
            background-color: #f9f9f9;
            color: #333;
            font-family: 'Arial', sans-serif;
            padding: 15px;
            margin: 15px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            word-wrap: break-word;
        ">
            <span style="text-decoration: underline;">{response_text}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# Define your page functions
def home_page():
    Q = st.chat_input("Ask me anything about the company RIVA AUTO")
    cook_breakfast()

    if Q:
        chain = get_qa_chain()
        response = chain(Q)
        st.markdown("<h3 style='color:green;'>✨_Answer</h3>", unsafe_allow_html=True)
        display_bounded_response(response['result'])
           



def about_page():
    # Display the create new data button
        password = st.text_input("Enter password", type="password")
        # Check the password
        
        if password == "123456":  # Replace with your actual password
            st.success("New data created successfully!")
            # Password is correct, proceed to create new data
            if st.button("Create new data"):
                 create_vector_db()
                 st.write("the operation complited✅")
                 
        else:
            # Incorrect password
            with st.spinner("RIVA AUTO 🚖"):
    # Simulate a long-running operation
                    time.sleep(2)
            st.error("Please try again.❌")

def contact_page():
    st.title("Contact ")
    st.write("🌍site web :https://concessionnaire.renault.ma/riva-auto-jadida.html")
    st.write("📞telephone:05233-42590")
    st.write("📧email:  ech.red1@gmail.com")
    st.write("📌Lot 347 Zone Industrielle Route de Marrakech El Jadida, El Jadida, Doukkala-abda 24000 · 91 km ")
# Map page names to functions
page_names_to_funcs = {
    "Home": home_page,
    "USER_PAGE": about_page,
    "Contact": contact_page
}

# Sidebar with a selectbox
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())

# Call the selected page function directly
page_names_to_funcs[selected_page]()




# Direct image URL (example of Renault logo)
im2=r"https://th.bing.com/th/id/R.c4686d40c203ba06da7257bdd67f65d8?rik=Mq0%2fqO0zTm9zAA&riu=http%3a%2f%2fecolesuperieure.ma%2fwp-content%2fuploads%2f2016%2f06%2ffst.jpg&ehk=xpPkOy0VocvPkZBMATRXwieWT0sBph3Kc98%2b0KzB4uQ%3d&risl=&pid=ImgRaw&r=0"
image_url = "https://www.zamoraautos.com/wp-content/uploads/2021/05/logos-renault-dacia.jpg"
# Adding the image to the sidebar
im1="https://imgs.search.brave.com/KLPJVop4jjaRiPTktoWE5xRCTPIU7oSoG0cYpkZ4PLw/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5nYWxsLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvOS9SZW5h/dWx0LVBORy1DdXRv/dXQucG5n"
with st.sidebar:
    st.image(im2)
    st.image(image_url, caption="Toute l'équipe de RIVA AUTOMOBILES El Jadida vous souhaite la bienvenue. N'hésitez pas à nous contacter ", use_column_width=True)
    st.markdown("<h3 style='color: red;text-align: center;'>les produits </h3>",
                    unsafe_allow_html=True)
    st.image(im1)
    st.image("https://imgs.search.brave.com/6IshAf3cwbz_iaGN-wxw1zHyw-v5CGoRdpLrWxkFQzc/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5nYWxsLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvOS9SZW5h/dWx0LnBuZw") 
    st.image("https://imgs.search.brave.com/ifJU-u6B6M6H8eqtZUniLnsXqmXYYOWv0gJcQAoAc4c/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5nYWxsLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvOS9SZW5h/dWx0LVBORy1JbWFn/ZS1IRC5wbmc")
    st.image("https://imgs.search.brave.com/4BOhHL5YgQrOb62DNW0T1E0EVRiyHuDzodWilVmPBY8/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5nYWxsLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvOS9SZW5h/dWx0LVBORy1QaWMt/QmFja2dyb3VuZC5w/bmc")
    st.image("https://imgs.search.brave.com/2HH7HGHtm-UohiKJIclvpfLjiHXQnB-QObXf24avoO8/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJzLmNvbS9p/bWFnZXMvZmVhdHVy/ZWQvcmVuYXVsdC1w/bmctdW9tamk5MHRw/Zm1sMjRmci5wbmc")
    st.image("https://imgs.search.brave.com/x7dUJitGBIJNdGYuQjVFfISPOzSqwEHb287Z7WqDWqM/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5nYWxsLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvOS9SZW5h/dWx0LVRyYW5zcGFy/ZW50LUJhY2tncm91/bmQucG5n")
    st.image("https://imgs.search.brave.com/LojlvS8JwCqYxAr4X3uDDzn6ruAUWLlczqephX1yE4o/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9wdXJl/cG5nLmNvbS9wdWJs/aWMvdXBsb2Fkcy9s/YXJnZS9wdXJlcG5n/LmNvbS1yZW5hdWx0/LWNhci1sb2dvbG9n/b2Nhci1icmFuZC1s/b2dvc2NhcnNyZW5h/dWx0LWNhci1sb2dv/LTE3MDE1Mjc0Mjg4/MzZmN3ExdS5wbmc")
    st.markdown("<h3 style='white: red;text-align: center;'> pour plus info: </h3>",
                    unsafe_allow_html=True)
    url = "https://www.renault.com"
    st.write(url)
  