from django.core.management.base import BaseCommand
from zone.models import Zone
from city.models import City
from user.models import User
import random
class Command(BaseCommand):
    help = 'Add city and zone to database'

    def handle(self, *args, **kwargs):
        morocco_zones = [
            {
                "zone": "Tanger-Tétouan-Al Hoceïma",
                "cities": ["Tangier", "Tetouan", "Al Hoceima", "Chefchaouen", "Larache"]
            },
            {
                "zone": "Oriental",
                "cities": ["Oujda", "Berkane", "Nador", "Taourirt", "Figuig"]
            },
            {
                "zone": "Fès-Meknès",
                "cities": ["Fes", "Meknes", "Taza", "Sefrou", "Moulay Idriss"]
            },
            {
                "zone": "Rabat-Salé-Kénitra",
                "cities": ["Rabat", "Salé", "Kenitra", "Temara", "Skhirat"]
            },
            {
                "zone": "Béni Mellal-Khénifra",
                "cities": ["Beni Mellal", "Khenifra", "Fquih Ben Salah", "Azilal", "Kasba Tadla"]
            },
            {
                "zone": "Casablanca-Settat",
                "cities": ["Casablanca", "Settat", "El Jadida", "Benslimane", "Berrechid"]
            },
            {
                "zone": "Marrakech-Safi",
                "cities": ["Marrakech", "Safi", "Essaouira", "Youssoufia", "Chichaoua"]
            },
            {
                "zone": "Drâa-Tafilalet",
                "cities": ["Errachidia", "Ouarzazate", "Zagora", "Tinghir", "Midelt"]
            },
            {
                "zone": "Souss-Massa",
                "cities": ["Agadir", "Taroudant", "Tiznit", "Oulad Teima", "Tata"]
            },
            {
                "zone": "Guelmim-Oued Noun",
                "cities": ["Guelmim", "Sidi Ifni", "Tan-Tan", "Assa", "Foum Zguid"]
            },
            {
                "zone": "Laâyoune-Sakia El Hamra",
                "cities": ["Laayoune", "Boujdour", "Tarfaya", "Smara", "El Marsa"]
            },
            {
                "zone": "Dakhla-Oued Ed-Dahab",
                "cities": ["Dakhla", "Aousserd", "Bir Gandouz", "Oued Ed-Dahab"]
            }
        ]

        for item in morocco_zones:
            zone = Zone.objects.create(zone_name=item['zone'])
            user = User.objects.all().first()
            for city in item["cities"]:
                City.objects.create(city_name=city, zone=zone, user=user, price=random.randrange(10, 90))

        self.stdout.write(self.style.SUCCESS('Data created successfully!'))