"""Collect open-data lookups for WGS84 N 61.4352530, E 23.7884520 from public APIs.

Usage: python3 fetch_opendata.py [--out data/]

Each source is fetched with a descriptive User-Agent (per OSM/usage policies),
written to data/<source>.json, and summarized to stdout. Sources that are
unreachable or blocked are reported as skipped without aborting the run.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import urllib.parse
import urllib.request

LAT, LON = "61.4352530", "23.7884520"
UA = "geohash-011126-research/1.0 (https://github.com/temetavis/geohash-011126)"


def fetch(source: str, url: str, out_dir: pathlib.Path) -> dict | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            status = resp.status
    except Exception as exc:  # noqa: BLE001
        print(f"[{source}] SKIPPED: {exc}")
        return None
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        payload = {"raw": body}
    payload["_meta"] = {"source": source, "url": url, "status": status}
    (out_dir / f"{source}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"[{source}] OK -> data/{source}.json")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="data", help="output directory")
    args = parser.parse_args()
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    lat, lon = LAT, LON
    sources = {
        "opentopodata_eudem25m": (
            "https://api.opentopodata.org/v1/eudem25m"
            f"?locations={lat},{lon}"
        ),
        "opentopodata_aster30m": (
            "https://api.opentopodata.org/v1/aster30m"
            f"?locations={lat},{lon}"
        ),
        "opentopodata_etopo1": (
            "https://api.opentopodata.org/v1/etopo1"
            f"?locations={lat},{lon}"
        ),
        "opentopodata_srtm30m": (
            "https://api.opentopodata.org/v1/srtm30m"
            f"?locations={lat},{lon}"
        ),
        "opentopodata_srtm90m": (
            "https://api.opentopodata.org/v1/srtm90m"
            f"?locations={lat},{lon}"
        ),
        "geonames_3geonames": f"https://api.3geonames.org/{lat},{lon}.json",
        "zippopotam_fi_33900": "https://api.zippopotam.us/fi/33900",
        "open_meteo_geocoding_tampere": (
            "https://geocoding-api.open-meteo.com/v1/search"
            "?name=Tampere&count=1&language=en&format=json"
        ),
        "open_meteo_forecast": (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true&timezone=auto"
        ),
        "nominatim_reverse": (
            "https://nominatim.openstreetmap.org/reverse"
            f"?format=jsonv2&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
        ),
        "photon_reverse": (
            "https://photon.komoot.io/reverse?lat={lat}&lon={lon}&limit=1".format(lat=lat, lon=lon)
        ),
        "overpass_osm_nodes": (
            "https://overpass-api.de/api/interpreter?data="
            + urllib.parse.quote(
                f"[out:json][timeout:25];node(around:300,{lat},{lon});out 25;"
            )
        ),
        "usgs_earthquakes": (
            "https://earthquake.usgs.gov/fdsnws/event/1/query"
            f"?format=geojson&latitude={lat}&longitude={lon}&maxradiuskm=200&limit=10&orderby=time"
        ),
    }

    for source, url in sources.items():
        fetch(source, url, out_dir)


if __name__ == "__main__":
    main()
