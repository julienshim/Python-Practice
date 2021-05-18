from re import sub

def sanitize_name(name):
    name = sub("-", " ", name)
    return sub("\.", "", name)