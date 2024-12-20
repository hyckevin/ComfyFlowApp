"""
页面配置和初始化模块
提供页面布局、样式和环境配置的功能
"""

from loguru import logger
import os
import streamlit as st
import streamlit_extras.app_logo as app_logo
from streamlit_extras.badges import badge
from htbuilder import a, img
from streamlit_extras.stylable_container import stylable_container
from streamlit.source_util import (
    get_pages,
    _on_pages_changed,
    invalidate_pages_cache,
)

def change_mode_pages(mode):
    """
    根据应用模式切换显示的页面
    Args:
        mode: 应用模式，可以是 'Creator' 或其他
    """
    # 获取主脚本路径
    main_script_path = os.path.abspath('../Home.py')
    # 清除页面缓存
    invalidate_pages_cache()
    # 获取所有页面
    all_pages = get_pages(main_script_path)
    
    # 根据模式选择显示的页面
    if mode == "Creator":
        pages = ['Home', 'Workspace', "My_Apps"]
    else:
        pages = [page['page_name'] for _, page in all_pages.items()]
    logger.info(f"pages: {pages}, mode: {mode}")

    # 移除不需要显示的页面
    current_pages = [key for key, value in all_pages.items() if value['page_name'] not in pages]
    for key in current_pages:
        all_pages.pop(key)
            
    _on_pages_changed.send()

def init_env_default():
    """
    初始化环境变量的默认值
    从 streamlit secrets 中读取配置并设置到环境变量
    """
    # 设置应用模式
    if 'MODE' in st.secrets:
        os.environ.setdefault('MODE', st.secrets['MODE'])
    
    # 设置API地址    
    if 'COMFYFLOW_API_URL' in st.secrets:
        os.environ.setdefault('COMFYFLOW_API_URL', st.secrets['COMFYFLOW_API_URL'])
    if 'COMFYUI_SERVER_ADDR' in st.secrets:
        os.environ.setdefault('COMFYUI_SERVER_ADDR', st.secrets['COMFYUI_SERVER_ADDR'])
    
    # 设置Discord OAuth配置（已弃用）
    if 'DISCORD_CLIENT_ID' in st.secrets:
        os.environ.setdefault('DISCORD_CLIENT_ID', st.secrets['DISCORD_CLIENT_ID'])
    if 'DISCORD_CLIENT_SECRET' in st.secrets:
        os.environ.setdefault('DISCORD_CLIENT_SECRET', st.secrets['DISCORD_CLIENT_SECRET'])
    if 'DISCORD_REDIRECT_URI' in st.secrets:
        os.environ.setdefault('DISCORD_REDIRECT_URI', st.secrets['DISCORD_REDIRECT_URI'])


def page_init(layout="wide"):
    """
    初始化页面配置
        mode, studio or creator
        layout: 页面布局方式，默认为宽屏模式
    """
    # 设置页面基本信息
    st.set_page_config(
        page_title="ComfyFlowApp: Load a comfyui workflow as webapp in seconds.", 
        page_icon=":artist:", 
        layout=layout
    )

    # 根据环境变量中的模式更新页面
    change_mode_pages(os.environ.get('MODE'))

    # 添加应用logo
    app_logo.add_logo("public/images/logo.png", height=70)

    # 调整页面上边距
    st.markdown("""
            <style>
                .block-container {
                        padding-top: 1rem;
                        padding-bottom: 0rem;
                        # padding-left: 5rem;
                        # padding-right: 5rem;
                    }
            </style>
            """, unsafe_allow_html=True)
    
    # 隐藏Streamlit默认的菜单和页脚
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # 配置侧边栏
    with st.sidebar:   
        # 显示当前模式
        st.markdown(f"Mode: {os.environ.get('MODE')} :smile:")

        # 设置侧边栏导航的最小高度
        st.sidebar.markdown("""
        <style>
        [data-testid='stSidebarNav'] > ul {
            min-height: 65vh;
        } 
        </style>
        """, unsafe_allow_html=True)

        # 添加社交媒体链接和徽章
        badge(type="github", name="xingren23/ComfyFlowApp", url="https://github.com/xingren23/ComfyFlowApp")
        badge(type="twitter", name="xingren23", url="https://twitter.com/xingren23")
        # 添加Discord邀请链接
        discord_badge_html = str(
            a(href="https://discord.gg/jkrPRNKp5R")(
                img(
                    src="https://img.shields.io/discord/1184762864678998077?style=social&logo=discord&label=join ComfyFlowApp"
                )
            )
        )
        st.write(discord_badge_html, unsafe_allow_html=True)

def stylable_button_container():
    """
    创建一个可自定义样式的按钮容器
    Returns:
        stylable_container: 返回一个带有预定义样式的容器
    """
    return stylable_container(
        key="app_button",
        css_styles=""" 
            button {
                background-color: rgb(28 131 225);
                color: white;
                border-radius: 4px;
                width: 120px;
            }
            button:hover, button:focus {
                border: 0px solid rgb(28 131 225);
            }
        """,
    )

def exchange_button_container():
    """
    创建一个用于交换按钮的容器
    Returns:
        stylable_container: 返回一个带有预定义样式的容器
    """
    return stylable_container(
        key="exchange_button",
        css_styles=""" 
            button {
                background-color: rgb(28 131 225);
                color: white;
                border-radius: 4px;
                width: 200px;
            }
            button:hover, button:focus {
                border: 0px solid rgb(28 131 225);
            }
        """,
    )

def custom_text_area():
    """
    创建一个自定义样式的文本区域
    Returns:
        str: 返回自定义样式的CSS代码
    """
    custom_css = """
            <style>
            textarea {
                height: auto;
                max-height: 250px;
            }
            </style>
        """
    # 将自定义CSS样式添加到Streamlit中
    st.markdown(custom_css, unsafe_allow_html=True)