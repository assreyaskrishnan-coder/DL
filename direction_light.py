# direction_light.py
# Basic automotive example - controlling direction indicators

def direction_light(side):
    if side == "left":
        print("Left indicator ON")
    elif side == "right":
        print("Right indicator ON")
    else:
        print("Hazard lights ON (both indicators)")

if __name__ == "__main__":
    direction_light("left")
