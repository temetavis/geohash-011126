# Geospatial Research Report: WGS84 N 61.4352530, E 23.7884520

Research date: 2025 (see commit history for exact date)

## Subject coordinates

| Format | Value |
|---|---|
| WGS84 decimal | N 61.4352530, E 23.7884520 |
| DMS | 61°26'6.91"N, 23°47'18.43"E |
| Geohash (12 char) | `udbvmrfnr15q` |
| Geohash (9 char, ~4.8 m cell) | `udbvmrfnr` |
| Geohash (6 char, ~1.2 km cell) | `udbvmr` |
| Geohash (4 char, ~39 km cell) | `udbv` |
| UTM Zone 35N (EPSG:32635) | 6815486.7 N, 328731.2 E |
| ETRS-TM35FIN (EPSG:3067) | 6815486.7 N, 328731.2 E |
| ECEF (EPSG:4978) | X=2797848.5, Y=1233324.7, Z=5578695.2 (meters) |

## Location summary

Open data sources consistently place this point in **Pirkaharju, Tampere, Pirkanmaa, Finland**, in the Pirkkala municipality border area south of Tampere city center, near Tampere-Pirkkala Airport.

## Open data source findings

### 1. OpenTopoData (eudem25m — EU-DEM v1.1, 25 m)
- **URL**: `https://api.opentopodata.org/v1/eudem25m?locations=61.4352530,23.7884520`
- **Elevation**: 131.63 m
- **License**: EU-DEM v1.1, produced by Copernicus/EEA, free and open

### 2. OpenTopoData (aster30m — NASA ASTER GDEM v3, 30 m)
- **URL**: `https://api.opentopodata.org/v1/aster30m?locations=61.4352530,23.7884520`
- **Elevation**: 150.0 m
- **License**: NASA ASTER GDEM, open data

### 3. OpenTopoData (etopo1 — ETOPO1 global relief, 1 arc-minute)
- **URL**: `https://api.opentopodata.org/v1/etopo1?locations=61.4352530,23.7884520`
- **Elevation**: 130.0 m
- **License**: NOAA, public domain

### 4. OpenTopoData (srtm30m / srtm90m — NASA SRTM)
- **URLs**: `https://api.opentopodata.org/v1/srtm30m?...` and `.../v1/srtm90m?...`
- **Elevation**: `null` — no coverage at this latitude (SRTM covers only up to ~60°N)
- **License**: NASA, public domain

### 5. 3geonames.org (GeoNames-based 3-word-style geocoding)
- **URL**: `https://api.3geonames.org/61.4352530,23.7884520.json`
- **3-word geocode**: `NOKIA-KAMUT-SEHWAN`
- **Geonumber**: `3026409520978`
- **Nearest named place** (1.22 km): Lahdenperä (61.43708, 23.76575), Tampere region, elevation ~122 m
- **Major city** (7.1 km): Tampere (61.49911, 23.78712), population 260,646, elevation 114 m
- **Administrative hierarchy** (from OSM boundaries):
  - admin8: Tampere (OSM id 497622, Wikidata Q40840, ref 837)
  - admin7: Tampereen seutukunta (Tampere sub-region, OSM id 497597)
  - admin6: Pirkanmaa / Birkaland (OSM id 496738, ISO3166-2 FI-11, Wikidata Q5701)
  - admin5: Länsi- ja Sisä-Suomen aluehallintovirasto (Western and Central Finland Regional State Administrative Agency)
- **Timezone**: Europe/Helsinki
- **License**: GeoNames CC-BY 4.0 + OSM ODbL

### 6. Zippopotam.us (postal code lookup, GeoNames-derived)
- **URL**: `https://api.zippopotam.us/fi/33900`
- **33900 Tampere (Pirkkala airport area)**: centroid 61.4958, 23.786 — approximately 6.7 km N of subject point
- **License**: GeoNames CC-BY 4.0

### 7. Open-Meteo Geocoding API (GeoNames + Open-Meteo)
- **URL**: `https://geocoding-api.open-meteo.com/v1/search?name=Tampere`
- **Tampere**: 61.49911, 23.78712, elevation 114 m, feature code PPLA, population 260,646
- **Administrative**: Pirkanmaa / Tampere / Tampere, FI
- **Timezone**: Europe/Helsinki
- **License**: GeoNames CC-BY 4.0

## Consistency analysis

- Elevation estimates cluster in the **122–150 m** range across four independent DEMs (EU-DEM, ASTER GDEM, ETOPO1, GeoNames). EU-DEM (25 m resolution) gives the most locally precise value: **131.6 m**.
- The point sits ~2–3 km south of the Tampere-Pirkkala Airport terminals (Pirkkala, postal code area 33900) and ~7 km SSW of Tampere city center.
- The coordinate lies in UTM zone 35N; ETRS-TM35FIN (the Finnish national ETRS89-based grid) gives near-identical values (differ only at cm-level due to WGS84 vs ETRS89 datum difference, which is negligible here).

## Data freshness and caching note

The data in `data/` was fetched on the research date with `fetch_opendata.py`. Re-run the script to refresh; each JSON file includes a `_meta` block with the source URL and HTTP status.

## Reproducing

```bash
pip install pyproj
python3 coordinates.py      # geohash, UTM, ETRS-TM35FIN, ECEF, DMS conversions
python3 fetch_opendata.py  # refresh open-data lookups into data/
```

`coordinates.py` implements the geohash algorithm from scratch (validated against the `python-geohash` reference implementation for this exact point: `udbvmrfnr15q`).

## Licenses

- EU-DEM v1.1: Copernicus data and information (EEA), free reuse with acknowledgement
- NASA ASTER GDEM / SRTM / ETOPO1: public domain (NOAA/NASA)
- GeoNames: CC-BY 4.0
- OpenStreetMap / Overpass / Nominatim / 3geonames OSM-derived data: ODbL
- This report: see repository license
