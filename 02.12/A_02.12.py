from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

@dataclass
class SnowSweeper:
    id: UUID = field(default_factory=uuid4)
    location: Optional[str] = None
    name: str = field(default="")

snow_sweeper_1 = SnowSweeper(name="Sweeper1", location="3Maja")
snow_sweeper_2 = SnowSweeper(name="Sweeper2", location="Sobieskiego")

print(snow_sweeper_1)
print(snow_sweeper_2)

snow_sweeper_1.location = "NowaLokalizacja"

print(snow_sweeper_1)
print(snow_sweeper_2)
