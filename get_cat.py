from the_cat_api.cat_api import TheCatApi

c = TheCatApi(
    api_key="live_1jZeVPv5nP9UgVJxOt0flQEaChF2xqloShK5D6MfPgRlZE7Mt4Yudx2QSeywFBMs"
)
img_data = c.get_kitty()[0]
c.fetch_image_data(image=img_data)

img_data.save_to(path="output", file_name="kitty.jpg")
