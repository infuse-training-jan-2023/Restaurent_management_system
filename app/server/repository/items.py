import base64

async def get_image(file: str) -> str:
    with open(file, "rb") as imageFile:
        base_encoded_img = base64.b64encode(imageFile.read())
    return base_encoded_img

async def insert_items():
    samosa = await get_image("app/server/images/samosa.webp")
    vadapav = await get_image("app/server/images/Vada-Pav-scaled.jpg")
    items_list = [
            {"item_name":"coke", "description": "A fried South Asian pastry with a savoury filling, including ingredients such as spiced potatoes, onions, and peas.","price":20,"quantity":2,"img": samosa,"tag":"snacks","type":"veg"},
            {"item_name":"sprite", "description": "The dish consists of a deep fried potato dumpling placed inside a bread bun.","price":30,"quantity":2,"img": vadapav,"tag":"snacks","type":"veg"}
    ]
