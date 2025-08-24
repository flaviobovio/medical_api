# Create venv + install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Start the API (for development)
uvicorn main:app --reload