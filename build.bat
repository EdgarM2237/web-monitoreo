.venv/scripts/activate

pip install --upgrade pip

pip install -r requierements.txt

rmdir public

s

reflex init
API_URL=https://web-monitoreo.up.railway.app reflex export --frontend-only

mkdir public

tar -zxvf frontend.zip -C public

del frontend.zip
deactivate
