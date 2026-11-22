from typing import Literal  # Restringir categorías
from pydantic import BaseModel, Field  # Validar entradas

class CustomerInput(BaseModel):  # Esquema de entrada
    tenure: int = Field(ge=0, le=100)  # Meses como cliente
    MonthlyCharges: float = Field(ge=0)  # Cargo mensual
    TotalCharges: float = Field(ge=0)  # Cargo acumulado
    Contract: Literal["Month-to-month", "One year", "Two year"]  # Contrato
    InternetService: Literal["DSL", "Fiber optic", "No"]  # Servicio
