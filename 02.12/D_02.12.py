import asyncio
import random

class StreetMonitoringService:
    def __init__(self, city, weather_service):
        self.city = city
        self.weather_service = weather_service

    async def update_street_snow_cover(self):
        while True:
           
            current_snow_fall_rate = self.weather_service.current_snow_fall_rate
            
            
            for street_name, street_data in self.city.items():
                
                X = current_snow_fall_rate
                Y = random.uniform(0, 1)
                street_data['snow_cover'] += X + Y

               
                print(f"Aktualizacja snow_cover dla ulicy {street_name}: {street_data['snow_cover']}")

            
            await asyncio.sleep(0.5)


city_data = {
    '3Maja': {'snow_cover': 0},
    'Piastowska': {'snow_cover': 0},
    'Warszwska': {'snow_cover': 0}
}


class WeatherService:
    def __init__(self):
        self.current_snow_fall_rate = 0

    async def run(self):
        while True:
            self.current_snow_fall_rate = random.uniform(0, 2)
            await asyncio.sleep(5)  


weather_service = WeatherService()


street_monitoring_service = StreetMonitoringService(city=city_data, weather_service=weather_service)


async def main():
    await asyncio.gather(weather_service.run(), street_monitoring_service.update_street_snow_cover())


if __name__ == "__main__":
    asyncio.run(main())
