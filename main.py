from PIL import Image
import streamlit as st
import pandas as pd

def open_image(img_path):
    return Image.open(img_path)

def sidebar():
    

    st.session_state["sel_page"] = st.sidebar.radio(
        label="ページ",
        options=["HOME", "Forza Horizon 4", "Euro Truck Simulator 2", "Beat Saber", "Prepar3d"]
    )



def main_page():
    st.title("パソコンゲーム体験 タイムテーブル")
    st.header("5月6日")
    st.table(pd.read_csv("timetable.csv"))

    st.header("5月7日")
    st.table(pd.read_csv("timetable.csv"))


def bs_page():    
    st.title("Beat Saber")
    st.image(open_image("./static/imgs/beatsaber.jpg"), width=None)
    st.video("https://youtu.be/N9KShTMxhUw")
    st.write("explain of game")

def fh4_page():
    st.title("Forza Horizon 4")
    st.image(open_image("./static/imgs/FH4.jpg"), width=None)
    st.write("explain of game")


def ets2_page():
    st.title("Euro Truck Simulator 2")
    st.image(("./static/imgs/ETS2.jpg"), width=None)
    st.write("explain of game")


def p3d_page():
    st.title("Prepar3Dv4 (エアバス A320 フライトシミュレーター)")
    st.image(open_image("./static/imgs/P3D.jpg"), width=None)
    st.write("explain of game")
    


def init():
    st.session_state["sel_page"] = "HOME"
    st.session_state["is_setup"] = True

def debug():
    st.header("header")
    st.subheader("subheader")
    st.write(st.session_state["sel_page"])    

    st.sidebar.title("サイドバータイトル")
    st.sidebar.header("サイドバーヘッダー")
    st.sidebar.subheader("サイドバーサブヘッダー")


if __name__ == "__main__":
    st.set_page_config(
        page_title = "パソコンゲーム体験",
        page_icon=":video_game:"
    )

    if "is_setup" not in st.session_state:
        init()

    sidebar()

    if st.session_state["sel_page"] == "HOME":
        main_page()
    if st.session_state["sel_page"] == "Forza Horizon 4":
        fh4_page()
    if st.session_state["sel_page"] == "Euro Truck Simulator 2":
        ets2_page()
    if st.session_state["sel_page"] == "Beat Saber":
        bs_page()
    if st.session_state["sel_page"] == "Prepar3d":
        p3d_page()


    # debug()