import streamlit as st


@st.dialog("Error")
def error_dialog(
    error_msg: str
) -> None:
    """汎用のエラーダイアログ
    """
    st.write(error_msg, unsafe_allow_html=True)
    _, col2 = st.columns(2)
    with col2:
        if st.button("OK", use_container_width=True):
            st.rerun()