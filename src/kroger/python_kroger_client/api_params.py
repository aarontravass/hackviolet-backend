param_map = {
    'brand': 'filter.brand',
    'chain': 'filter.chain',
    'fulfillment': 'filter.fulfillment',
    'limit': 'filter.limit',
    'location_id': 'filter.locationId',
    'product_id': 'filter.product_id',
    'term': 'filter.term',
    'within_miles': 'filter.radiusInMiles',
    'zipcode': 'filter.zipCode.near',
}

def get_mapped_params(params):
    """ Maps a dictionary of parameters (ignoring `self`) to the API's expected key value """
    return { param_map[key] : value for key, value in params.items() if key != 'self'}