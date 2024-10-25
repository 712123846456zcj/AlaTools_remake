@echo off  
setlocal enabledelayedexpansion  
  
REM �������·��  
set RELATIVE_PATH=python3106\Lib\site-packages\argostranslate
  
REM ��ȡ��ǰ������ű����ڵ�Ŀ¼  
set SCRIPT_DIR=%~dp0
  
REM �����������ļ�·��  
set FILE_PATH=%SCRIPT_DIR%\%RELATIVE_PATH%\settings.py  
  
REM ����ļ��Ƿ����  
if not exist "%FILE_PATH%" (  
    echo �ļ� %FILE_PATH% �����ڣ�  
    exit /b 1  
)  
  
REM ʹ�� PowerShell �滻�ļ�����  
powershell -Command "(Get-Content '%FILE_PATH%') -replace 'home_dir = Path.home()', 'home_dir = Path.cwd' | Set-Content '%FILE_PATH%'"  
  
echo �ļ� %FILE_PATH% �ѳɹ��޸ģ�  
endlocal

pause