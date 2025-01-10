from the_cat_api.cat_api import TheCatApi

c = TheCatApi(
    api_key="live_1jZeVPv5nP9UgVJxOt0flQEaChF2xqloShK5D6MfPgRlZE7Mt4Yudx2QSeywFBMs"
)
img_list = c.get_kitty()
print(type(img_list))
img_list[0].save_to(path="output", file_name="kitty.jpg")
