@echo off  
setlocal enabledelayedexpansion  
  
REM 定义相对路径  
set RELATIVE_PATH=python3106\Lib\site-packages\argostranslate
  
REM 获取当前批处理脚本所在的目录  
set SCRIPT_DIR=%~dp0
  
REM 构造完整的文件路径  
set FILE_PATH=%SCRIPT_DIR%\%RELATIVE_PATH%\settings.py  
  
REM 检查文件是否存在  
if not exist "%FILE_PATH%" (  
    echo 文件 %FILE_PATH% 不存在！  
    exit /b 1  
)  
  
REM 使用 PowerShell 替换文件内容  
powershell -Command "(Get-Content '%FILE_PATH%') -replace 'home_dir = Path.home()', 'home_dir = Path.cwd' | Set-Content '%FILE_PATH%'"  
  
echo 文件 %FILE_PATH% 已成功修改！  
endlocal

pause