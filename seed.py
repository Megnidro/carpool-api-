import os
import django
from faker import Faker
from random import choice

from accounts.models import CustomUser, UserRole, ProfileCustomUser, Address, CarModel

# Configurations initiales pour Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'covoiturage.settings')
django.setup()


# Fonction pour créer des utilisateurs avec des profils associés
def create_users(num_users=10):
    fake = Faker('fr_FR')

    for _ in range(num_users):
        # Création de l'utilisateur
        email = fake.email()
        password = 'password123'  # Mot de passe temporaire
        last_name = fake.last_name()
        first_name = fake.first_name()
        is_staff = False
        is_superuser = False

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            last_name=last_name,
            first_name=first_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )

        # Création du profil associé
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=100)
        genre = choice(['F', 'M'])
        phone_number = fake.phone_number()
        num_permis = fake.random_int(min=10000, max=99999)
        role = choice([UserRole.DRIVER.value, UserRole.PASSENGER.value, UserRole.BOTH.value])
        category = choice(['A', 'B', 'C', 'D', 'E'])
        date_delivrance = fake.date_between(start_date='-10y', end_date='today')
        date_expiration = fake.date_between(start_date='today', end_date='+10y')

        profile = ProfileCustomUser.objects.create(
            user=user,
            birth_date=birth_date,
            genre=genre,
            phone_number=phone_number,
            num_permis=num_permis,
            role=role,
            category=category,
            date_delivrance=date_delivrance,
            date_expiration=date_expiration,
        )

        # Création d'une adresse
        address = Address.objects.create(
            position_name=fake.address(),
            number=fake.building_number(),
            street=fake.street_name(),
            city=fake.city(),
            region=fake.region(),
            country=fake.country(),
            postal_code=fake.postcode(),
            type_of_address=choice(['H', 'O', 'O']),
            author=profile
        )

        # Création d'une voiture (si le rôle est conducteur ou les deux)
        if role == UserRole.DRIVER.value or role == UserRole.BOTH.value:
            car = CarModel.objects.create(
                owner=profile,
                make=fake.vehicle_make(),
                model=fake.vehicle_model(),
                year=fake.year(),
                color=fake.safe_color_name(),
                licence_number=fake.license_plate()
            )

        print(f"Utilisateur créé : {user.email} avec profil, adresse et éventuellement une voiture.")


# Appel de la fonction pour créer les utilisateurs
if __name__ == '__main__':
    create_users()
