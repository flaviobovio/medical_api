# Create venv + install deps
# Use Python 3.12
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Start the API (for development)
uvicorn main:app --reload
