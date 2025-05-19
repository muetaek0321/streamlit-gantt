import streamlit as st
import pandas as pd

from modules.styles import HIDE_ST_STYLE
from modules.create_ganttchart import create_ganttchart
from modules.task_info import add_task_button


# ページのコンフィグ
st.set_page_config(
    page_title="タスク管理",
    page_icon="🤔",
    layout="wide"
)

# 定数
STATE = st.session_state
DATA_PATH = "./data/task.csv"

# スタイルを適用
st.markdown(HIDE_ST_STYLE, unsafe_allow_html=True)

# 初回実行時にデータを読み込み
if "tasks_df" not in STATE:
    STATE.tasks_df = pd.read_csv(DATA_PATH, encoding="cp932")

# ガントチャートを表示
fig = create_ganttchart(STATE.tasks_df)
st.plotly_chart(fig)

# タスクを登録するボタン
add_task_button(DATA_PATH)

# タスクリストを表示
st.dataframe(STATE.tasks_df)

