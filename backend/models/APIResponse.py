from dataclasses import dataclass, asdict

# Clase unicamente para generar respuestas

@dataclass
class APIResponse:
    ok : bool
    data : list
    count : int
    message : str

    def __init__(self, status, data, count, message):
        self.ok = status
        self.data = data
        self.count = count
        self.message = message

    def to_json(self):
        return asdict(self)
