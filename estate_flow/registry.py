
def generate_resident_id(data):
    """Generate a new resident ID."""

    resident_id = f"R{data['next_id']:03d}"
    data["next_id"] += 1

    return resident_id


def register_resident(data, name, phone):
    """Register a new resident."""

    name = name.strip()
    phone = phone.strip()

    if not name:
        return False, "Resident name cannot be empty."

    if not phone:
        return False, "Phone number cannot be empty."

    for resident in data["residents"].values():
        if resident["name"].lower() == name.lower():
            return False, "A resident with that name already exists."

    resident_id = generate_resident_id(data)

    data["residents"][resident_id] = {
        "name": name,
        "phone": phone
    }

    return True, resident_id


def find_resident(data, resident_id):
    """Find a resident using their ID."""

    return data["residents"].get(resident_id.strip().upper())


def get_all_residents(data):
    """Return all registered residents."""

    return data["residents"]

