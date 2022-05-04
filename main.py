from PIL import Image
import streamlit as st

def open_image(img_path):
    return Image.open(img_path)

def sidebar():
    st.sidebar.title("サイドバータイトル")
    st.sidebar.header("サイドバーヘッダー")
    st.sidebar.subheader("サイドバーサブヘッダー")

    st.session_state["sel_page"] = st.sidebar.radio(
        label="ページ",
        options=["HOME", "VRゲーム", "レースゲーム", "フライトシューティングゲーム"]
    )

def debug():
    st.write(st.session_state["sel_page"])    

def main_page():
    st.header("HOME ようこそ　ヘッダー")
    st.subheader("サブヘッダー")


def vr_game_page():
    st.header("VRゲーム")
    
    st.subheader("Beat Saber")
    st.image(open_image("./static/imgs/beatsaber.jpg"), width=None)
    st.video("https://youtu.be/N9KShTMxhUw")
    st.write("explain of game")


def car_game_page():
    st.header("レースゲーム")
    
    st.subheader("Forza Horizon 4")
    st.image(open_image("./static/imgs/FH4.jpg"), width=None)
    st.write("explain of game")
    
    st.subheader("Assetto Corsa Competizione")
    st.image(open_image("./static/imgs/ACC.jpg"), width=None)
    st.write("explain of game")

    st.subheader("Euro Truck Simulator 2")
    st.image(open_image("./static/imgs/ETS2.jpg"), width=None)
    st.write("explain of game")


def plane_game_page():
    st.header("フライトシューティングゲーム")
    
    st.subheader("ACE COMBAT 7 SKIES UNKNOWN")
    st.image(open_image("./static/imgs/ACE7.png"), width=None)
    st.write("explain of game")
    
    st.subheader("Prepar3Dv4")
    st.image(open_image("./static/imgs/P3D.jpg"), width=None)
    st.write("explain of game")
    
    # st.subheader("Game 3")
    # st.write("explain of game")


def init():
    st.session_state["sel_page"] = "HOME"
    st.session_state["is_setup"] = True


if __name__ == "__main__":
    if "is_setup" not in st.session_state:
        init()

    st.title("羽咋市 e-sports タイトル")
    
    sidebar()

    if st.session_state["sel_page"] == "HOME":
        main_page()
    if st.session_state["sel_page"] == "VRゲーム":
        vr_game_page()
    if st.session_state["sel_page"] == "レースゲーム":
        car_game_page()
    if st.session_state["sel_page"] == "フライトシューティングゲーム":
        plane_game_page()

    debug()