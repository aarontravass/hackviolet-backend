import kroger

def location(zip_code: int):
    result = service_client.get_location(zip_code, within_miles=10, limit=10)
    return result