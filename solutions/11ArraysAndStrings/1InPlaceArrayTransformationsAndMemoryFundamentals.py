image_strip = [10, 250, 128, 5, 200, 150, 80]

def invert_and_mirror(pixel_array):
    len_array = len(pixel_array)
    for step, value in enumerate(pixel_array):
        if (step < len_array / 2):
            opposite = len(image_strip) - (step+1)
            pixel_array[step] = 255 - pixel_array[opposite]
            pixel_array[opposite] = 255 - value
    return pixel_array

print(invert_and_mirror(image_strip))