# geohash-011126

Geospatial research for WGS84 coordinates **N 61.4352530, E 23.7884520** (Pirkaharju, Tampere, Finland).

## Contents

- `REPORT.md` — full research report from open data sources
- `coordinates.py` — geohash encoding, UTM/ETRS-TM35FIN/ECEF/DMS conversions (requires `pyproj`)
- `fetch_opendata.py` — fetches open-data lookups (elevation, geocoding) into `data/`
- `data/` — cached API responses with source metadata

## Reproducing

```bash
pip install pyproj
python3 coordinates.py
python3 fetch_opendata.py
```

Geohash of the subject point: `udbvmrfnr15q`
