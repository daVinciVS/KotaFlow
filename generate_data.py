import numpy as np
import pandas as pd
from pathlib import Path

RNG = np.random.default_rng(42)
OUTPUT = Path(r"D:\MOST IMPORTANT\KotaFlow\data\KotaFlow_rides.csv")

# Real hotspot locations per city with relative demand weights
HOTSPOTS = {
    "Jakarta": [
        {"name": "Sudirman-Thamrin",     "lat": -6.2088, "lon": 106.8228, "weight": 0.20},
        {"name": "Kuningan",             "lat": -6.2297, "lon": 106.8317, "weight": 0.12},
        {"name": "Soekarno-Hatta",       "lat": -6.1256, "lon": 106.6559, "weight": 0.10},
        {"name": "Blok M",               "lat": -6.2441, "lon": 106.7987, "weight": 0.10},
        {"name": "Kelapa Gading",        "lat": -6.1581, "lon": 106.9049, "weight": 0.09},
        {"name": "Grogol",               "lat": -6.1676, "lon": 106.7934, "weight": 0.08},
        {"name": "Manggarai Station",    "lat": -6.2139, "lon": 106.8502, "weight": 0.08},
        {"name": "Kemang",               "lat": -6.2607, "lon": 106.8130, "weight": 0.07},
        {"name": "Cempaka Putih",        "lat": -6.1760, "lon": 106.8710, "weight": 0.07},
        {"name": "Pluit",                "lat": -6.1174, "lon": 106.7993, "weight": 0.09},
    ],
    "Yogyakarta": [
        {"name": "Malioboro",            "lat": -7.7928, "lon": 110.3659, "weight": 0.25},
        {"name": "Tugu Station",         "lat": -7.7892, "lon": 110.3664, "weight": 0.15},
        {"name": "UGM Campus",           "lat": -7.7714, "lon": 110.3778, "weight": 0.15},
        {"name": "Prambanan",            "lat": -7.7520, "lon": 110.4914, "weight": 0.10},
        {"name": "Parangtritis",         "lat": -8.0246, "lon": 110.3313, "weight": 0.08},
        {"name": "Kotagede",             "lat": -7.8269, "lon": 110.4002, "weight": 0.08},
        {"name": "Ring Road Utara",      "lat": -7.7511, "lon": 110.3921, "weight": 0.10},
        {"name": "Bandara YIA",          "lat": -7.9025, "lon": 110.0570, "weight": 0.09},
    ],
    "Surabaya": [
        {"name": "Tunjungan Plaza",      "lat": -7.2619, "lon": 112.7378, "weight": 0.18},
        {"name": "Juanda Airport",       "lat": -7.3798, "lon": 112.7876, "weight": 0.15},
        {"name": "Gubeng Station",       "lat": -7.2655, "lon": 112.7520, "weight": 0.13},
        {"name": "Galaxy Mall",          "lat": -7.2876, "lon": 112.7789, "weight": 0.10},
        {"name": "UNAIR Campus",         "lat": -7.2698, "lon": 112.7631, "weight": 0.10},
        {"name": "Pelabuhan Tanjung",    "lat": -7.1985, "lon": 112.7333, "weight": 0.10},
        {"name": "Wonokromo",            "lat": -7.3000, "lon": 112.7369, "weight": 0.09},
        {"name": "Kenjeran",             "lat": -7.2270, "lon": 112.7830, "weight": 0.08},
        {"name": "ITS Campus",           "lat": -7.2819, "lon": 112.7957, "weight": 0.07},
    ],
}

CITY_BASE = {
    "Jakarta":    {"base_demand": 220, "volatility": 55},
    "Yogyakarta": {"base_demand": 85,  "volatility": 22},
    "Surabaya":   {"base_demand": 155, "volatility": 38},
}

WEATHER = ["Clear", "Cloudy", "Rainy", "Drizzle"]
WEATHER_WEIGHTS = [0.45, 0.30, 0.15, 0.10]
WEATHER_MUL = {"Clear": 1.0, "Cloudy": 1.05, "Rainy": 1.30, "Drizzle": 1.18}
N_PER_CITY = 6000


def hour_multiplier(hour, day_type):
    if day_type == "Weekday":
        if 7 <= hour <= 9:   return 1.75
        elif 17 <= hour <= 20: return 1.65
        elif 12 <= hour <= 13: return 1.20
        elif 0 <= hour <= 5:  return 0.40
        else: return 1.0
    else:
        if 10 <= hour <= 14: return 1.50
        elif 19 <= hour <= 22: return 1.30
        elif 0 <= hour <= 7:  return 0.35
        else: return 1.0


def generate_city(city, n):
    spots = HOTSPOTS[city]
    cfg = CITY_BASE[city]
    weights = np.array([s["weight"] for s in spots])
    weights /= weights.sum()

    start = pd.Timestamp("2024-01-01")
    end = pd.Timestamp("2024-03-31 23:59:59")
    offsets = RNG.integers(0, int((end - start).total_seconds()), size=n)
    timestamps = [start + pd.Timedelta(seconds=int(o)) for o in offsets]

    day_types = ["Weekend" if pd.Timestamp(t).dayofweek >= 5 else "Weekday" for t in timestamps]
    hours = [t.hour for t in timestamps]
    weather = RNG.choice(WEATHER, size=n, p=WEATHER_WEIGHTS)

    # Assign each ride to a hotspot
    spot_indices = RNG.choice(len(spots), size=n, p=weights)

    pickup_lats, pickup_lons = [], []
    for idx in spot_indices:
        spot = spots[idx]
        pickup_lats.append(RNG.normal(spot["lat"], 0.012))
        pickup_lons.append(RNG.normal(spot["lon"], 0.012))

    pickup_lats = np.array(pickup_lats)
    pickup_lons = np.array(pickup_lons)
    dropoff_lats = pickup_lats + RNG.normal(0, 0.018, n)
    dropoff_lons = pickup_lons + RNG.normal(0, 0.018, n)

    demand = [
        max(5, int(
            cfg["base_demand"]
            * hour_multiplier(h, d)
            * WEATHER_MUL[w]
            + RNG.normal(0, cfg["volatility"])
        ))
        for h, d, w in zip(hours, day_types, weather)
    ]

    return pd.DataFrame({
        "timestamp":         timestamps,
        "city":              city,
        "pickup_lat":        pickup_lats.round(6),
        "pickup_lon":        pickup_lons.round(6),
        "dropoff_lat":       dropoff_lats.round(6),
        "dropoff_lon":       dropoff_lons.round(6),
        "demand_volume":     demand,
        "weather_condition": weather,
        "day_type":          day_types,
    })


frames = [generate_city(city, N_PER_CITY) for city in HOTSPOTS]
df = pd.concat(frames, ignore_index=True).sort_values("timestamp").reset_index(drop=True)
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)
print("Done. Rows:", len(df))
print("Saved to:", OUTPUT)