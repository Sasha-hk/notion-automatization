#!/bin/bash


BASE_DIR=$PWD

echo "Install packages..."
pip install -r requirements.txt

echo "[+] Create run.sh"
echo "#!/bin/bash

while read line; do
  export \$line
done < ${BASE_DIR}/.env

python3 ${BASE_DIR}/app.py" > run.sh

chmod +x run.sh

echo "[+] Done!"
echo "[!] Create .env file"
