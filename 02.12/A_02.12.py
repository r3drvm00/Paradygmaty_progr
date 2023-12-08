from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

@dataclass
class SnowSweeper:
    id: UUID = field(default_factory=uuid4)
    location: Optional[str] = None
    name: str = field(default="")

# Tworzymy dwie różne instancje SnowSweeper z różnymi lokalizacjami
snow_sweeper_1 = SnowSweeper(name="Sweeper1", location="3Maja")
snow_sweeper_2 = SnowSweeper(name="Sweeper2", location="Sobieskiego")

# Wyświetlamy lokalizacje obiektów
print(snow_sweeper_1)
print(snow_sweeper_2)

# Zmieniamy lokalizację tylko w jednej instancji
snow_sweeper_1.location = "NowaLokalizacja"

# Wyświetlamy zaktualizowane lokalizacje obiektów
print(snow_sweeper_1)
print(snow_sweeper_2)
