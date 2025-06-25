import os
import json
from openai import OpenAI
from openai.types.chat import ChatCompletionToolParam
from pydantic import ValidationError
from project.models import TravelRequest
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tool_schema: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "extract_travel_request",
        "description": "Extrae los parámetros relevantes para planificar un viaje.",
        "parameters": {
            "type": "object",
            "properties": {
                "destino": {"type": "string"},
                "fecha": {"type": "string"},
                "presupuesto_total": {"type": "number"},
                "intereses": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": ["destino"]
        }
    }
}

def parse_natural_input_to_travel_request(user_input: str) -> TravelRequest:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente que convierte texto de viaje en datos estructurados."
            },
            {"role": "user", "content": user_input}
        ],
        tools=[tool_schema],
        tool_choice={"type": "function", "function": {"name": "extract_travel_request"}},
        temperature=0.2
    )

    try:
        tool_call = response.choices[0].message.tool_calls[0]
        parsed_args = json.loads(tool_call.function.arguments)
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        raise ValueError(f"Error al extraer los argumentos de la respuesta de OpenAI: {e}")

    try:
        return TravelRequest(**parsed_args)
    except ValidationError as e:
        raise ValueError(f"Error validando TravelRequest: {e}")

