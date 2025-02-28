from planner_api.models import Destination

cities = [
    ("Rome", 41.9028, 12.4964),
    ("Milan", 45.4642, 9.1900),
    ("Naples", 40.8518, 14.2681),
    ("Turin", 45.0703, 7.6869),
    ("Palermo", 38.1157, 13.3615),
    ("Genoa", 44.4056, 8.9463),
    ("Bologna", 44.4949, 11.3426),
    ("Florence", 43.7696, 11.2558),
    ("Bari", 41.1171, 16.8719),
    ("Venice", 45.4408, 12.3155),
]


for name, latitude, longitude in cities:
    Destination.objects.get_or_create(name=name, latitude=latitude, longitude=longitude)

print(f"{len(cities)} destinations created.")
