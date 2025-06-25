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

## Running as a web service
Install the extra dependencies and start the FastAPI server:
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```
Send POST requests to `/parse` with plain text and the service will return a `TravelRequest` JSON.

To containerize the application:
```bash
docker build -t travel-parser .
docker run -p 8000:8000 travel-parser
```

## Deploying to Heroku
The repository includes a `Procfile` so it can be deployed directly using
Heroku's Python buildpack. After installing the [Heroku CLI](https://devcenter.heroku.com/), run:

```bash
heroku login
heroku create <app-name>
heroku config:set OPENAI_API_KEY=your-api-key --app <app-name>
git push heroku main
```

Heroku will install the requirements, launch the app with Uvicorn, and expose
the `/parse` endpoint at `https://<app-name>.herokuapp.com/parse`.

=======
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

## Publishing
To make the repository available online, initialize Git and push to a remote:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-remote-url>
git push -u origin main
```
