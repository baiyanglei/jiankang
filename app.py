"""
阿野的客厅 — Streamlit 部署入口
将 personal-blog.html 作为完整前端嵌入，保留全部样式与交互。
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ──────────────────────────────────────────────
# 页面配置
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="阿野的客厅",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────
# 隐藏 Streamlit 默认 UI（菜单、页脚、顶部条）
# ──────────────────────────────────────────────
st.markdown(
    """
    <style>
        /* 隐藏主菜单 */
        #MainMenu {visibility: hidden;}
        /* 隐藏页脚 */
        footer {visibility: hidden;}
        /* 隐藏顶部工具栏 */
        header {visibility: hidden;}
        /* 去掉 Streamlit 默认 padding，让 HTML 占满全屏 */
        .stApp {
            padding: 0 !important;
            margin: 0 !important;
        }
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        /* 嵌入的 iframe 去掉默认边框 */
        iframe {
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────
# 读取并嵌入 HTML
# ──────────────────────────────────────────────
html_path = Path(__file__).parent / "personal-blog.html"

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")

    # 用 components.html 嵌入完整 HTML
    # height 设为 1080 起步，配合 scrolling=True 允许内部滚动
    components.html(
        html_content,
        height=1080,
        scrolling=True,
    )
else:
    st.error(f"未找到 {html_path}，请确认文件存在。")
