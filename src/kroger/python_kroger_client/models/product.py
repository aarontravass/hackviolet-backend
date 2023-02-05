class Product:
    """ Represents a single grocery product """

    def __init__(self, id, upc, brand, description, image, size, price):
        self.id          = id
        self.upc         = upc
        self.brand       = brand
        self.description = description
        self.image       = image
        self.size        = size
        self.price       = price

    def __str__(self):
        verbose     = False
        description = f"({self.brand}) {self.description}"
        if self.size:
            description += f" - {self.size}: ${self.price}"
        if verbose:
            description += f"\nProduct ID: {self.id}"
            description += f"\nUPC: {self.upc}"
            description += f"\nImage: {self.image}"

        return description

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_json(cls, obj):
        id          = obj.get("productId")
        upc         = obj.get("upc")
        brand       = obj.get("brand")
        description = obj.get("description")
        image       = _get_image_from_images(obj.get("images"))
        size        = _get_product_size(obj.get("items"))
        price       = _get_product_price(obj.get("items"))

        result_obj = {
        "id": id, 
        "upc": upc, 
        "brand": brand, 
        "description": description,
        "image": image, 
        "size": size, 
        "price": price
        }

        return result_obj

    @classmethod
    def from_json1(cls, obj):
        id          = obj.get("productId")
        upc         = obj.get("upc")
        brand       = obj.get("brand")
        description = obj.get("description")
        aisle       = _get_aisle_location(obj.get("aisleLocations"))
        image       = _get_image_from_images(obj.get("images"))
        size        = _get_product_size(obj.get("items"))
        price       = _get_product_price(obj.get("items"))
        stock       = _get_stock_level(obj.get("items"))

        result_obj = {
        "id": id, 
        "upc": upc, 
        "brand": brand, 
        "description": description, 
        "aisle": aisle, 
        "image": image, 
        "size": size, 
        "price": price, 
        "stock": stock
        }

        return result_obj


def _get_aisle_location(aisles):
    # Not sure when this could be more than one, but it's an array & we'll take the first one
    if len(aisles) > 0:
        return _get_aisle(aisles[0])
    else:
        return None

def _get_aisle(aisle):
    ail  = aisle.get("number", "")
    side = aisle.get("side", "")

    return f"Aisle-{ail}, Side-{side}"

def _get_image_from_images(images, perspective='front', size='medium'):
    front_image = next((image for image in images if image.get("perspective") == perspective), None)
    if front_image:
        sizes = front_image.get("sizes", [])
        front_image = next((s.get("url") for s in sizes if s.get("size") == size), None)

    return front_image

def _get_product_size(items):
    # Not sure when this could be more than one, but it's an array & we'll take the first one
    if len(items) > 0:
        return items[0].get("size")
    else:
        return None

def _get_product_price(items):
    # Not sure when this could be more than one, but it's an array & we'll take the first one
    if len(items) > 0:
        return items[0].get("price", {}).get('regular')
    else:
        return None

def _get_stock_level(items):
    # Not sure when this could be more than one, but it's an array & we'll take the first one
    if len(items) > 0:
        return items[0].get("inventory", {}).get('stockLevel')
    else:
        return None