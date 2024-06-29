# get picture from addres

import json
from geopy.geocoders import Nominatim
from functools import lru_cache
import mapillary.interface as mly

app_name = "hackBCN2024"
CLIENT_TOKEN = "MLY|8097843413583502|75416d010f92347cf1b118b4d2564bd4"
mly.set_access_token(CLIENT_TOKEN)


@lru_cache(maxsize=100)
def get_coordinates(address):
    geolocator = Nominatim(user_agent=app_name)
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None


def get_mapillary_images(lat, lon, radius=60, limit=5):
    data = mly.get_image_looking_at(
        at=dict(
            lng=lon,
            lat=lat,
        ),
        radius=radius,
        # limit=limit,
    )
    print(len(data.features))
    # import pdb;pdb.set_trace()
    ids = [
        dd.properties.id
        for dd in data.features
    ]
    res = 256
    thumbs = []
    for image_id in ids:
        thumb_path = mly.image_thumbnail(image_id=image_id, resolution=res)
        thumbs.append(thumb_path)
    
    generate_image_grid_html(thumbs)


def generate_image_grid_html(image_paths, columns=3, output_file='image_grid.html'):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Grid</title>
        <style>
            .image-grid {
                display: grid;
                grid-template-columns: repeat(AUTO_COLUMNS, 1fr);
                gap: 10px;
            }
            .image-item img {
                width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <div class="image-grid">
    """

    for path in image_paths:
        html_content += f'        <div class="image-item"><img src="{path}" alt="Grid Image"></div>\n'

    html_content += """
        </div>
    </body>
    </html>
    """

    html_content = html_content.replace('AUTO_COLUMNS', str(columns))

    with open(output_file, 'w') as f:
        f.write(html_content)

    print(f"HTML file '{output_file}' has been generated.")


address = "le wagon barcelona"

def get_image(address):
    coordinates = get_coordinates(address)

    if coordinates:
        lat, lon = coordinates
        print(f"Coordinates: {lat}, {lon}")
        
        images = get_mapillary_images(lat, lon)
        if images:
            for image in images:
                print(f"Image ID: {image['id']}")
                print(f"Thumbnail URL: {image['thumb_1024_url']}")
                print("---")
        return images
    else:
        print("Could not find coordinates for the given address.")


if __name__ == "__main__":
    get_image(address)