"""
common functions for validation
"""


def check_lat_lon_elev(station, errors):
    if station['location/X/value_d'] == 0:
        errors.append("Channel longitude seems to be 0. Is this correct???")
    if station['location/X/value_d'] in [None, '']:
        errors.append("No Channel longitude value found.")
    else:
        try:
            if not -180 <= float(station['location/X/value_d']) <= 180:
                errors.append("Channel longitude %s not in range [-180,180]"
                              % station['location/X/value_d'])
        except ValueError:
            errors.append("Channel longitude %s is not a number."
                          % station['location/X/value_d'])

    if station['location/X/units_s'] in [None, '']:
        errors.append("No Station location/X/units_s value found.")

    if station['location/Y/value_d'] == 0:
        errors.append("Channel latitude seems to be 0. Is this correct???")
    if station['location/Y/value_d'] in [None, '']:
        errors.append("No Channel latitude value found.")
    else:
        try:
            if not -90 <= float(station['location/Y/value_d']) <= 90:
                errors.append("Channel latitude %s not in range [-90,90]"
                              % station['location/Y/value_d'])
        except ValueError:
            errors.append("Channel latitude %s is not a number."
                          % station['location/Y/value_d'])

    if station['location/Y/units_s'] in [None, '']:
        errors.append("No Station location/Y/units_s value found.")

    if station['location/Z/value_d'] in [None, '']:
        errors.append("No Channel location/Z/value_d value found.")

    if station['location/Z/units_s'] in [None, '']:
        errors.append("No Station location/Z/units_s value found.")
