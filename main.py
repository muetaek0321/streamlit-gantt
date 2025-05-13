import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

from modules.styles import HIDE_ST_STYLE
from modules.create_ganttchart import create_ganttchart


# 定数
STATE = st.session_state

# スタイルを適用
st.markdown(HIDE_ST_STYLE, unsafe_allow_html=True)

# 初回実行時にデータを読み込み
if "tasks_df" not in STATE:
    STATE.tasks_df = pd.read_csv("./data/task.csv", encoding="cp932")

# ガントチャートを表示
fig = create_ganttchart(STATE.tasks_df)
st.plotly_chart(fig)

# DataFrameを表示
st.dataframe(STATE.tasks_df)

