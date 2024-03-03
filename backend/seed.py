from faker import Faker
from app import db, app
from models import User, Landlord, Tenant, Apartment, Booking

fake = Faker()

counties = [
    "Baringo", "Bomet", "Bungoma", "Busia", "Elgeyo-Marakwet", "Embu", "Garissa", "Homa Bay",
    "Isiolo", "Kajiado", "Kakamega", "Kericho", "Kiambu", "Kilifi", "Kirinyaga", "Kisii", "Kisumu",
    "Kitui", "Kwale", "Laikipia", "Lamu", "Machakos", "Makueni", "Mandera", "Marsabit", "Meru",
    "Migori", "Mombasa", "Murang'a", "Nairobi", "Nakuru", "Nandi", "Narok", "Nyamira", "Nyandarua",
    "Nyeri", "Samburu", "Siaya", "Taita-Taveta", "Tana River", "Tharaka-Nithi", "Trans Nzoia",
    "Turkana", "Uasin Gishu", "Vihiga", "Wajir", "West Pokot"
]

apartment_images = [
    "https://source.unsplash.com/800x600/?apartment",
    "https://source.unsplash.com/800x600/?apartment-building",
    "https://source.unsplash.com/800x600/?modern-apartment",
    "https://source.unsplash.com/800x600/?interior",
    "https://source.unsplash.com/800x600/?living-room",
    "https://source.unsplash.com/800x600/?bedroom",
    "https://source.unsplash.com/800x600/?kitchen",
    "https://source.unsplash.com/800x600/?bathroom",
    "https://source.unsplash.com/800x600/?luxury-apartment",
    "https://source.unsplash.com/800x600/?urban-living",
    "https://source.unsplash.com/800x600/?cityscape",
    "https://source.unsplash.com/800x600/?real-estate",
    "https://source.unsplash.com/800x600/?home",
    "https://source.unsplash.com/800x600/?architecture",
    "https://source.unsplash.com/800x600/?building",
    "https://source.unsplash.com/800x600/?apartment-complex",
    "https://source.unsplash.com/800x600/?skyline",
    "https://source.unsplash.com/800x600/?condominium",
    "https://source.unsplash.com/800x600/?cozy",
    "https://source.unsplash.com/800x600/?house",
    "https://source.unsplash.com/800x600/?modern-home",
    "https://source.unsplash.com/800x600/?luxury-living",
    "https://source.unsplash.com/800x600/?high-rise",
    "https://source.unsplash.com/800x600/?view",
    "https://source.unsplash.com/800x600/?penthouse",
    "https://source.unsplash.com/800x600/?apartment-interior",
    "https://source.unsplash.com/800x600/?apartment-view",
    "https://source.unsplash.com/800x600/?furnished-apartment",
    "https://source.unsplash.com/800x600/?skyline-view",
]

# Function to generate fake users
def generate_fake_users(num_users):
    users = []
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        users.append(user)
    return users

# Function to generate fake landlords
def generate_fake_landlords(users):
    landlords = []
    for user in users:
        landlord = Landlord(user=user)
        landlords.append(landlord)
    return landlords

# Function to generate fake tenants
def generate_fake_tenants(users):
    tenants = []
    for user in users:
        tenant = Tenant(user=user)
        tenants.append(tenant)
    return tenants

# Function to generate fake apartments
def generate_fake_apartments(landlords, counties):
    apartments = []
    num_apartments_per_county = len(landlords) // len(counties)
    
    for county in counties:
        for _ in range(num_apartments_per_county):
            landlord = landlords.pop(0)
            image_index = len(apartments) % len(apartment_images)
            image_url = apartment_images[image_index]
            apartment = Apartment(
                landlord=landlord,
                images=image_url,  # Use a single image URL
                address=fake.street_address(),
                description=fake.text(),
                county=county,
                price=fake.random_int(min=500, max=5000),
                bedrooms=fake.random_int(min=1, max=5),
                is_available=fake.boolean(),
            )
            apartments.append(apartment)

    # Add remaining apartments to counties
    remaining_apartments = len(landlords) // len(counties)
    for i in range(remaining_apartments):
        landlord = landlords.pop(0)
        image_index = apartments.index(landlord) % len(apartment_images)
        image_url = apartment_images[image_index]
        apartment = Apartment(
            landlord=landlord,
            images=image_url,  # Use a single image URL
            address=fake.street_address(),
            description=fake.text(),
            county=counties[i % len(counties)],
            price=fake.random_int(min=500, max=5000),
            bedrooms=fake.random_int(min=1, max=5),
            is_available=fake.boolean(),
        )
        apartments.append(apartment)
    
    counties = [
    "Baringo", "Bomet", "Bungoma", "Busia", "Elgeyo-Marakwet", "Embu", "Garissa", "Homa Bay",
    "Isiolo", "Kajiado", "Kakamega", "Kericho", "Kiambu", "Kilifi", "Kirinyaga", "Kisii", "Kisumu",
    "Kitui", "Kwale", "Laikipia", "Lamu", "Machakos", "Makueni", "Mandera", "Marsabit", "Meru",
    "Migori", "Mombasa", "Murang'a", "Nairobi", "Nakuru", "Nandi", "Narok", "Nyamira", "Nyandarua",
    "Nyeri", "Samburu", "Siaya", "Taita-Taveta", "Tana River", "Tharaka-Nithi", "Trans Nzoia",
    "Turkana", "Uasin Gishu", "Vihiga", "Wajir", "West Pokot"
]

    return apartments


# Function to generate fake bookings
def generate_fake_bookings(tenants, apartments):
    bookings = []
    for tenant, apartment in zip(tenants, apartments):
        booking = Booking(
            tenant=tenant,
            apartment=apartment,
            start_date=fake.date_between(start_date='-30d', end_date='today'),
        )
        bookings.append(booking)
    return bookings

def clear_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

# Number of fake users, landlords, tenants, apartments, and bookings
num_users = 40
min_entries_per_user = 4
num_users = max(min_entries_per_user, num_users)
num_landlords = num_users
num_tenants = num_users
num_apartments = num_landlords
num_bookings = min(num_tenants, num_apartments)

# Clear the database
print("Clearing the database...")
clear_database()

# Generate fake users, landlords, tenants, apartments, and bookings
print("Generating fake users...")
fake_users = generate_fake_users(num_users)
print("Generating fake landlords...")
fake_landlords = generate_fake_landlords(fake_users)
print("Generating fake tenants...")
fake_tenants = generate_fake_tenants(fake_users)
print("Generating fake apartments...")
fake_apartments = generate_fake_apartments(fake_landlords,counties)
print("Generating fake bookings...")
fake_bookings = generate_fake_bookings(fake_tenants, fake_apartments)


# Add fake data to the database
with app.app_context():
    db.create_all()

    db.session.add_all(fake_users)
    db.session.add_all(fake_landlords)
    db.session.add_all(fake_tenants)
    db.session.add_all(fake_apartments)
    db.session.add_all(fake_bookings)

    db.session.commit()

print("Fake data has been successfully added to the database.")
