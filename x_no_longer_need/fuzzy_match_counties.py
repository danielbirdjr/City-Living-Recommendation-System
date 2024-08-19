from fuzzywuzzy import process
import pandas as pd

# Load necessary data
city_county_data = pd.read_csv('data/city-county-mapping-dataset.csv')
population_data = pd.read_csv('data/cleaned_population_data.csv')

# Manual mapping for problematic counties
manual_mappings = {
    "yakutat": "Yakutat City and Borough",
    "amelia": "Amelia County",
    "james": "James City County",
    "currituck": "Currituck County",
    "king george": "King George County",
    "plaquemines": "Plaquemines Parish",
    "arlington": "Arlington County",
    "mathews": "Mathews County",
    "skagway": "Skagway Municipality",
    "kenedy": "Kenedy County",
    "new kent": "New Kent County",
    "esmeralda": "Esmeralda County",
    "echols": "Echols County",
    "zapata": "Zapata County",
    "storey": "Storey County",
    "spotsylvania": "Spotsylvania County",
    "kalawao": "Kalawao County",
    "borden": "Borden County",
    "alpine": "Alpine County",
    "jim hogg": "Jim Hogg County",
    "king and queen": "King and Queen County",
    "lander": "Lander County",
    "banner": "Banner County",
    "henrico": "Henrico County",
    "bland": "Bland County",
    "los alamos": "Los Alamos County",
    "goochland": "Goochland County",
    "oscoda": "Oscoda County",
    "mariposa": "Mariposa County",
    "glasscock": "Glasscock County",
    "st. bernard": "St. Bernard Parish",
    "loving": "Loving County",
    "mcmullen": "McMullen County",
    "mccreary": "McCreary County",
    "st. john the baptist": "St. John the Baptist Parish",
    "powhatan": "Powhatan County",
    "eureka": "Eureka County",
    "nye": "Nye County"
}

# Fuzzy matching process
for county in city_county_data['County']:
    if county.lower() in manual_mappings:
        mapped_county = manual_mappings[county.lower()]
        print(f"Manual Mapping - County: {county}, Mapped County: {mapped_county}")
    else:
        matches = process.extract(county, population_data['County'], limit=3)
        print(f"County: {county}, Closest Matches: {matches}")
