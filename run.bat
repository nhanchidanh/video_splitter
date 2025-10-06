@echo off
REM File nay dung de chay chuong trinh Python voi virtual environment
echo Setting up virtual environment...

REM Tao virtual environment neu chua co
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Kich hoat virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Kiem tra va cai dat customtkinter
python -c "import customtkinter" 2>nul
if %errorlevel% neq 0 (
    echo Installing customtkinter...
    pip install customtkinter
)

REM Kiem tra va cai dat opencv-python
python -c "import cv2" 2>nul
if %errorlevel% neq 0 (
    echo Installing opencv-python...
    pip install opencv-python
)

echo Starting Video Frame Extractor...
python video_splitter.py

pause
