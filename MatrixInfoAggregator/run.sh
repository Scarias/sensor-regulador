if [[ -d env ]]; then
    python -m venv env
fi

source env/bin/activate
pip install -r requirements.txt

python src/