import asyncio
import random

class StreetMonitoringService:
    def __init__(self, city, weather_service):
        self.city = city
        self.weather_service = weather_service

    async def update_street_snow_cover(self):
        while True:
            # Pobierz aktualny current_snow_fall_rate z serwisu pogodowego
            current_snow_fall_rate = self.weather_service.current_snow_fall_rate
            
            # Przejdź przez wszystkie ulice w self.city
            for street_name, street_data in self.city.items():
                # Dodaj (X + Y) do snow_cover dla każdej ulicy
                X = current_snow_fall_rate
                Y = random.uniform(0, 1)
                street_data['snow_cover'] += X + Y

                # Wypisz informację na konsolę
                print(f"Aktualizacja snow_cover dla ulicy {street_name}: {street_data['snow_cover']}")

            # Poczekaj 0.5 sekundy przed kolejną aktualizacją
            await asyncio.sleep(0.5)

# Przykładowe dane - słownik z informacjami o ulicach
city_data = {
    '3Maja': {'snow_cover': 0},
    'Piastowska': {'snow_cover': 0},
    'Warszwska': {'snow_cover': 0}
}

# Symulacja serwisu pogodowego
class WeatherService:
    def __init__(self):
        self.current_snow_fall_rate = 0

    async def run(self):
        while True:
            # Symulacja zmiany current_snow_fall_rate
            self.current_snow_fall_rate = random.uniform(0, 2)
            await asyncio.sleep(5)  # Symulacja czasu między zmianami pogody

# Utwórz instancję serwisu pogodowego
weather_service = WeatherService()

# Utwórz instancję serwisu monitorowania ulic
street_monitoring_service = StreetMonitoringService(city=city_data, weather_service=weather_service)

# Uruchom serwis pogodowy i serwis monitorowania ulic w asynchronicznej pętli
async def main():
    await asyncio.gather(weather_service.run(), street_monitoring_service.update_street_snow_cover())

# Uruchom program
if __name__ == "__main__":
    asyncio.run(main())
