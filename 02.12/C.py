import random
import asyncio

class WeatherService:
    def __init__(self):
        self.current_snow_fall_rate = 0

    async def update_snow_fall_rate(self):
        while True:
            # Losowanie  [0, 2]
            self.current_snow_fall_rate = random.uniform(0, 2)
            
            # 2 s
            await asyncio.sleep(2)

async def main():
    weather_service = WeatherService()
 
    asyncio.create_task(weather_service.update_snow_fall_rate())

    # Pętla 
    while True:
        
        print(f"Current Snow Fall Rate: {weather_service.current_snow_fall_rate}")
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
