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


=======
This project provides a simple CLI tool that converts natural-language travel requests into a structured format.

## Features
- Parses user text with the OpenAI API.
- Validates the data using a Pydantic `TravelRequest` model.

## Installation
1. Create a virtual environment.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables
The tool expects an `OPENAI_API_KEY` value in a `.env` file or the environment:
```bash
OPENAI_API_KEY=your-api-key
```

## Usage
Run the CLI from the project root:
```bash
python -m project.main
```
Enter your travel request when prompted and the structured data will be printed.

## Development
This is an initial version and will evolve. Issues and pull requests are welcome.
