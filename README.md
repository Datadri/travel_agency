# Travel Request Parser

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
