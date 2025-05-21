
#!/usr/bin/env bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Build React
cd frontend/volt
npm install
npm run build
cd ../../
echo "Setup done. Activate venv with 'source .venv/bin/activate'"
