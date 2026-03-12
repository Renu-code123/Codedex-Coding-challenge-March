###World Wide Web 🌐

def validate_url(address):
    if address.startswith("http://"):
        domain = address[7:]
    elif address.startswith("https://"):
        domain = address[8:]
    else:
        return "invalid"

    if "." not in domain:
        return "invalid"

    for c in domain:
        if not (c.isalnum() or c in "-."):
            return "invalid"

    return "valid"
