import pandas as pd
import requests 
from math import radians, sin, cos, sqrt, atan2

file_path = r"supply_chain/cleaned_data (1).csv"

df = pd.read_csv(file_path, encoding="latin1")

df.columns = df.columns.str.strip()

def get_coordinates(country_name):
    try:
        url = f"https://nominatim.openstreetmap.org/search?country={country_name}&format=json"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()

        if len(data) > 0:
            lat, lon = float(data[0]["lat"]), float(data[0]["lon"])
            return lat, lon
        else:
            return None, None 
    except Exception as e:
        return None, None

df["Manufacturing_Country_Lat"], df["Manufacturing_Country_Lon"] = zip(*df["Manufacturing country"].apply(get_coordinates))
df["Warehouse_Country_Lat"], df["Warehouse_Country_Lon"] = zip(*df["Country"].apply(get_coordinates))

df = df.dropna(subset=["Manufacturing_Country_Lat", "Manufacturing_Country_Lon", "Warehouse_Country_Lat", "Warehouse_Country_Lon"])

updated_file_path = "lat and lon.csv"
df.to_csv(updated_file_path, index=False)

def get_distance(supplier_coords, warehouse_coords):
    base_url = "http://router.project-osrm.org/route/v1/driving"

    if None in [supplier_coords, warehouse_coords]:  
        return "N/A"

    lat1, lon1 = supplier_coords
    lat2, lon2 = warehouse_coords
    url = f"{base_url}/{lon1},{lat1};{lon2},{lat2}?overview=false"

    response = requests.get(url)
    data = response.json()

    try:
        distance_meters = data["routes"][0]["distance"]
        distance_km = round(distance_meters / 1000, 2) 
        if distance_km == 0: 
            return "N/A"
        return distance_km
    except (KeyError, IndexError):
        return "N/A"

df["Distance_to_Warehouse"] = df.apply(
    lambda row: get_distance(
        (row["Manufacturing_Country_Lat"], row["Manufacturing_Country_Lon"]),
        (row["Warehouse_Country_Lat"], row["Warehouse_Country_Lon"])
    ), axis=1
)

df = df.dropna(subset=["Distance_to_Warehouse"])

new_updated_file_path = "pure_distance.csv"
df.to_csv(new_updated_file_path, index=False)
