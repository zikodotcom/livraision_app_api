from django.core.management.base import BaseCommand
from zone.models import Zone
from city.models import City
from user.models import User
import random
from django.contrib.auth.hashers import make_password
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

        # TODO Create user admin
        user_data = {"username": "admin", "password": make_password("admin"), "type" : "admin", "is_active" : True, 'first_name': "Mustapha", 'last_name' : "Mustapha"}
        user = User.objects.create(**user_data)
        # TODO Create user client
        client_user = {
                    "username": "client",
                    "password": make_password("client123"),
                    "email_verefied_at": "2024-01-31",
                    "phone": "0612345678",
                    "type": "client",
                    "cin": "AB12345678",
                    "city": "a483a5b6294848d1946f71c644c05ad3",
                    "adresse": "123 Rue Example, Casablanca, Morocco",
                    "company_name": "Example Company",
                    "company_type": "SARL",
                    "bank_name": "Attijariwafa Bank",
                    "bank_account": "123456789012345678901234",
                    "bank_rib": "RIBEXAMPLE1234567890"
                }
        User.objects.create(**client_user)

        for item in morocco_zones:
            zone = Zone.objects.create(zone_name=item['zone'])
            for city in item["cities"]:
                City.objects.create(city_name=city, zone=zone, user=user, price=random.randrange(10, 90))

        self.stdout.write(self.style.SUCCESS('Data created successfully!'))