from pathlib import Path

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pandas as pd

from modules.styles import ADD_BUTTON_STYLE


# 定数
STATE = st.session_state


def add_task_button(
    data_path: str | Path
) -> None:
    """タスク登録の処理をするボタン
    """
    # ボタンのスタイルの設定
    with stylable_container("add_button", ADD_BUTTON_STYLE):
        add_button_click = st.button("登録", icon="➕")
    
    # ボタンが押された時の処理
    if add_button_click:
        add_task_dialog(data_path)
    

@st.dialog("タスク登録")
def add_task_dialog(
    data_path: str | Path
) -> None:
    """タスクを登録するダイアログ
    """
    # 各項目の入力フォーム
    task_label = st.text_input("ラベル")
    start = st.date_input("開始日")
    end = st.date_input("終了日")
    status = st.selectbox("状況", ["予定", "作業中", "完了"])
    task_description = st.text_input("タスク内容")
    
    # 登録可能かどうかの判定
    if task_label == "":
        st.error("ラベルが未入力です")
        disabled = True
    elif start > end:
        st.error("終了日が開始日より前の日付になっています")
        disabled = True
    else:
        disabled = False
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("登録", type="primary", disabled=disabled, use_container_width=True):
            # csvに追記し保存
            add_task_info = pd.DataFrame(
                {key: [value] for key, value 
                 in zip(STATE.tasks_df.columns, [task_label, start, end, status, task_description])}
            )
            task_df = pd.concat([STATE.tasks_df, add_task_info])
            task_df.to_csv(data_path, encoding="cp932", index=False)
            # session_stateのtask_dfも更新
            STATE.tasks_df = task_df
            
            st.rerun()
    with col2:
        if st.button("キャンセル", use_container_width=True):
            st.rerun()