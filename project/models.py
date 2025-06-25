from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date
import re

class TravelRequest(BaseModel):
    destino: str = Field(..., description="Ciudad o país de destino del viaje")
    fecha: Optional[str] = Field(
        None,
        description="Fecha del viaje: puede ser una fecha exacta (YYYY-MM-DD), un mes (YYYY-MM) o texto semiestructurado ('segunda semana de octubre')"
    )
    presupuesto_total: Optional[float] = Field(
        None,
        gt=0,
        description="Presupuesto total estimado en euros para todo el viaje"
    )
    intereses: Optional[List[str]] = Field(
        default=[],
        description="Lista de intereses temáticos: cultura, gastronomía, naturaleza, etc."
    )

    @field_validator("fecha")
    def validar_fecha(cls, v):
        # Aceptamos 3 formatos: YYYY-MM-DD, YYYY-MM, o texto libre
        if v is None:
            return v
        if re.match(r"^\d{4}-\d{2}-\d{2}$", v):
            return v  # fecha exacta
        if re.match(r"^\d{4}-\d{2}$", v):
            return v  # solo mes
        if len(v) < 5:
            raise ValueError("Formato de fecha no reconocido")
        return v  # se procesará como texto libre posteriormente

    @field_validator("intereses")
    def normalizar_intereses(cls, v):
        if isinstance(v, str):
            # Si es un string, lo convertimos a lista
            v = [v]
        if not isinstance(v, list):
            raise ValueError("Intereses debe ser una lista o un string")
        if not all(isinstance(i, str) for i in v):
            raise ValueError("Todos los elementos de intereses deben ser strings")
        # Normalizamos los intereses: eliminamos espacios y convertimos a minúsculas

        return [i.strip().lower() for i in v if i.strip()]  

    @field_validator("presupuesto_total")
    def validar_presupuesto(cls, v):
        if isinstance(v, str):
            try:
                v = float(v)
            except ValueError:
                raise ValueError("El presupuesto total debe ser un número")
        if not isinstance(v, (int, float)):
            raise ValueError("El presupuesto total debe ser un número")
        if v is not None and v <= 0:
            raise ValueError("El presupuesto total debe ser un número positivo")
        return v
    
