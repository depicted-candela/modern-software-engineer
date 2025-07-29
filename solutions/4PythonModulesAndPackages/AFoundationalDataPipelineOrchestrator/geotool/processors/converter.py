def wkt_to_coords(wkt: str) -> dict:
    parenthesis = "("
    if wkt.__contains__(parenthesis):
        position = wkt.index("(")
        feature = wkt[:position].title()
        coords = wkt[position+2:-2].split(", ")
        for step, coord in enumerate(coords): 
            coords[step] = coord.split(" ")
        return {'type': feature, 'coordinates': coords}
    return {'type': 'invalid'}