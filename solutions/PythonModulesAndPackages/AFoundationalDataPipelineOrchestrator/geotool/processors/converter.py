def wkt_to_coords(wkt: str) -> dict:
    geom = wkt["geometry"]
    position = geom.index("(")
    feature = geom[:position].title()
    coords = geom[position+2:-2].split(", ")
    for step, coord in enumerate(coords): 
        coords[step] = coord.split(" ")
    return {'type': feature, 'coordinates': coords}