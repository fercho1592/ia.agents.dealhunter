from enum import Enum

class ConfigEnum(Enum):
    GEMINI_API_KEY = "gemini_api_key"
    # Agrega aquí más claves según se necesiten

    def __str__(self):
        return self.value

