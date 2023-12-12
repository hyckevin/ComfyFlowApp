@echo off
setlocal

:: get current directory
set CUR_DIR=%~dp0
set PROJECT_DIR=%CUR_DIR%..\
cd /d %PROJECT_DIR%

:: set LOGURU_LEVEL to INFO
set LOGURU_LEVEL=INFO
set STREAMLIT_SERVER_PORT=8503
:: set COMFYFLOW_API_URL to https://api.comfyflow.app
set COMFYFLOW_API_URL=https://api.comfyflow.app

:: set discord callback url
set DISCORD_REDIRECT_URI=http://localhost:8503
:: set MODE
set MODE=Explore

:: start server
python -m streamlit run Home.py
pause
endlocal