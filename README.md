# Python for AI — Learning Notes and Mini Projects

A personal learning repository for Python fundamentals and small data-oriented exercises while building toward AI application development.

## Contents

- **Python fundamentals** — early exercises covering variables, control flow, collections, functions, and environment variables.
- **Weather data exercise** — requests recent weather data from Open-Meteo, builds a pandas DataFrame, plots temperature ranges, and writes a CSV.
- **Sales analysis exercise** — calculates line totals and a grand total from a CSV using pandas and small helper functions.

This repository is a learning archive rather than a polished application. For a production-style project, see [Invoice Buddy](https://github.com/Xatreus/invoice-buddy).

## Setup

Use Python 3.10 or newer and create a virtual environment:

```bash
git clone https://github.com/Xatreus/python-for-ai.git
cd python-for-ai
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the weather exercise from the repository root:

```bash
python get_data.py
```

The script requests weather data from Open-Meteo and writes a chart and CSV locally. It requires internet access.

Run the sales exercise from its directory after ensuring the expected CSV exists at `sales-analysis/data/sales.csv`:

```bash
cd sales-analysis
python analyzer.py
```

## Notes

- Some files are incomplete practice exercises and may not be executable.
- The requirements file currently includes notebook and interactive-development packages; it can be slimmed down as individual exercises are separated.
- Do not store credentials or private datasets in this repository.

## License

No license is currently declared. Until a license is added, assume standard copyright applies.
