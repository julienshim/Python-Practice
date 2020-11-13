def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    if is_healthy:
        return f"I'm eating {food}, because my body is a temple."
    return f"I'm eating {food}, because YOLO!"


def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh I overslept. I didn't meant to nap for {num_hours} hours!"
    return f"I'm feeling refreshed after my {num_hours} hour nap."
