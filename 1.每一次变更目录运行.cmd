cd python3106

python.exe -m pip uninstall argostranslate -y
python.exe -m pip uninstall libretranslate -y
python.exe -m pip install --no-cache-dir --no-index --find-links=../LibreTranslate ../LibreTranslate/libretranslate-1.6.1-py3-none-any.whl --no-warn-script-location


pause
