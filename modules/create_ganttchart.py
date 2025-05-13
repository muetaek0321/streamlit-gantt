import pandas as pd
import plotly.figure_factory as ff
from plotly.graph_objects import Figure


# 定数
COLORS = {
    "完了": "rgb(0, 0, 150)", 
    "作業中": "rgb(0, 0, 50)", 
    "予定": "rgb(0, 0, 250)"
}


def create_ganttchart(
    task_df: pd.DataFrame
) -> Figure:
    """ガントチャートのグラフオブジェクトを作成
    
    Args:
        task_df: 読み込んだタスクリストのDataFrame
        
    Returns:
        Figure: ガントチャートのグラフオブジェクト
    """
    # DataFrameの形式変換
    plot_df = pd.DataFrame([
        dict(Task=task, Start=start, Finish=finish, State=state)
        for task, start, finish, state 
        in zip(task_df["ラベル"], task_df["開始日"], task_df["終了日"], task_df["状況"])
    ])
    
    # ガントチャートを作成
    fig = ff.create_gantt(plot_df, colors=COLORS, index_col='State', 
                          show_colorbar=True, group_tasks=True)
    
    # レイアウトを調整
    fig.update_layout(
        xaxis_rangeselector=None
    )
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1ヶ月", step="month", stepmode="backward"),
                    dict(count=3, label="3ヶ月", step="month", stepmode="backward"),
                    dict(step="all", label="全体表示")
                ])
            ),
            rangeslider=dict(visible=True),  # スライダー表示
            type="date"
        )
    )
    
    return fig

