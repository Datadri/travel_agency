# Travel Request Parser

This project provides a small command line interface to transform natural language travel requests into structured data. It relies on the OpenAI API and uses Pydantic for validation.

## Features
- Parse user text with the OpenAI API
- Validate parsed fields using a `TravelRequest` Pydantic model
- Expose a simple CLI that prints the resulting structured data

## Requirements
- Python 3.12+
- See `requirements.txt` for the full dependency list

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Provide an `OPENAI_API_KEY` in a `.env` file or as an environment variable.

## Usage
Run the CLI as a module:
```bash
python -m project
```
or execute the script directly:
```bash
python project/main.py
```

Enter your travel request when prompted; the tool will print a structured representation.

## Project Structure
```
project/
    __main__.py      # allows `python -m project`
    main.py          # CLI entry point
    models.py        # Pydantic models
    utils/
        parser.py    # OpenAI based parser
```

## Development
- Format/validate code with `python -m compileall -q project`.
- Tests can be added under a `tests/` folder in the future.
- Contributions and issues are welcome; please open a PR.
