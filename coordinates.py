LAT, LON = 61.4352530, 23.7884520

BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"


def geohash(lat, lon, precision=12):
    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    is_even, bit, ch, bits = True, 0, 0, 0
    hash_str = ""
    while len(hash_str) < precision:
        if is_even:
            mid = (lon_interval[0] + lon_interval[1]) / 2
            if lon >= mid:
                ch = (ch << 1) | 1
                lon_interval = (mid, lon_interval[1])
            else:
                ch = ch << 1
                lon_interval = (lon_interval[0], mid)
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2
            if lat >= mid:
                ch = (ch << 1) | 1
                lat_interval = (mid, lat_interval[1])
            else:
                ch = ch << 1
                lat_interval = (lat_interval[0], mid)
        is_even = not is_even
        bits += 1
        if bits == 5:
            hash_str += BASE32[ch]
            bits = ch = 0
    return hash_str


def main():
    from pyproj import Transformer

    print(f"Input coordinates: N {LAT}, E {LON}")
    print(f"Geohash: {geohash(LAT, LON)}")

    utm = Transformer.from_crs("EPSG:4326", "EPSG:32635", always_xy=True)
    x, y = utm.transform(LON, LAT)
    print(f"UTM zone 35N (EPSG:32635): {y:.1f} N, {x:.1f} E")
    rlon, rlat = utm.transform(x, y, direction="INVERSE")
    print(f"UTM roundtrip: {rlat:.7f}, {rlon:.7f}")

    wgs84_cart = Transformer.from_crs("EPSG:4979", "EPSG:4978", always_xy=True)
    gx, gy, gz = wgs84_cart.transform(LON, LAT, 0.0)
    print(f"ECEF (EPSG:4978): X={gx:.1f} Y={gy:.1f} Z={gz:.1f}")

    etrs = Transformer.from_crs("EPSG:4326", "EPSG:3067", always_xy=True)
    e, n = etrs.transform(LON, LAT)
    print(f"ETRS-TM35FIN (EPSG:3067): N={n:.1f} E={e:.1f}")

    def to_dms(value: float, pos: str, neg: str) -> str:
        hemi = pos if value >= 0 else neg
        value = abs(value)
        d = int(value)
        m = int((value - d) * 60)
        s = (value - d) * 3600 - m * 60
        return f"{d}\u00b0{m}'{s:.2f}\"{hemi}"

    print(f"DMS: {to_dms(LAT, 'N', 'S')} {to_dms(LON, 'E', 'W')}")


if __name__ == "__main__":
    main()
