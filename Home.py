"""
ComfyFlowApp 主页模块
这是整个应用的入口点
"""

import streamlit as st
import os
from loguru import logger
from streamlit_extras.row import row
from modules import page

# 初始化页面环境和布局
page.init_env_default()
page.page_init(layout="centered")

# 设置默认本地用户状态
if 'username' not in st.session_state:
    st.session_state['username'] = 'local'

with st.container():
    # 创建页面头部布局
    header_row = row([0.87, 0.13], vertical_align="bottom")
    header_row.title("""
        Welcome to ComfyFlowApp
        From comfyui workflow to web application in seconds, and share with others.
    """)

    with st.container():
        st.markdown("Hello, Local User :smile:")
        
        # 展示应用介绍信息
        st.markdown("""
                    ### 📌 What is ComfyFlowApp?
                    ComfyFlowApp 是一个 ComfyUI 的扩展工具，帮助用户快速开发和分享基于 ComfyUI 工作流的 Web 应用。
                    """)
        st.markdown("""
                    ### 📌 Why You Need ComfyFlowApp? 
                    ComfyFlowApp 帮助创作者快速开发和分享基于 ComfyUI 工作流的 Web 应用。

                    如果您需要与其他用户分享在 ComfyUI 中开发的工作流，ComfyFlowApp 可以显著降低其他用户使用您的工作流的门槛：
                    - 用户不需要了解 AI 生成模型的原理。
                    - 用户不需要了解 ComfyUI 的使用方法。
                    - 用户不需要配置复杂的环境。
                    """)
        st.markdown("""
                    ### 📌 How to Use ComfyFlowApp?
                    1. 在 ComfyUI 中开发工作流
                    2. 使用 ComfyFlowApp 将工作流转换为 Web 应用
                    3. 分享给其他用户使用
                    """)
        st.markdown("""
                    ### 📌 Use Cases
                    """)
        st.image("./docs/images/how-to-use-it.png", use_column_width=True)
        st.markdown("""
                    :point_right: Follow the repo [ComfyFlowApp](https://github.com/xingren23/ComfyFlowApp) to get the latest updates. 
                    """)
