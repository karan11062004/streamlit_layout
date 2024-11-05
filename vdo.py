import streamlit as st
import time

st.set_page_config(layout="wide")

if "uploaded_video" not in st.session_state:
    st.session_state.uploaded_video = None

video_column, button_column = st.columns([4, 1])

with video_column:
    st.header("WELCOME TO TENNIS GAME TRACKER")
    
    uploaded_file = st.file_uploader("Drag and drop your video here", type=["mp4", "mov", "avi"], label_visibility="collapsed")

    if st.session_state.uploaded_video is not None:
        st.video(st.session_state.uploaded_video)
    else:
        st.write("Upload content to enjoy!")

    if uploaded_file is not None:
        progress_bar = st.progress(0)
        for i in range(1, 101):
            time.sleep(0.05)
            progress_bar.progress(i)
        
        st.session_state.uploaded_video = uploaded_file
        st.success("Video uploaded successfully!")

with button_column:
    if st.button("Button 2", use_container_width=True):
        st.markdown("You clicked Button 2.")

    if st.button("Button 3", use_container_width=True):
        st.markdown("You clicked Button 3.")

    if st.button("Button 4", use_container_width=True):
        st.markdown("You clicked Button 4.")
