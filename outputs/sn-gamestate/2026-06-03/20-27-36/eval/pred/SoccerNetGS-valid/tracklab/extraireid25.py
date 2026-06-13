import json

path = "SNGS-001.json"

with open(path, "r") as f:
    data = json.load(f)

points = []

for p in data["predictions"]:
    if p.get("track_id") == 37:
        pitch = p.get("bbox_pitch", {})

        x = pitch.get("x_bottom_middle")
        y = pitch.get("y_bottom_middle")

        if x is not None and y is not None:
            points.append((x, y))

with open("points_track25.py", "w") as f:
    f.write("points = [\n")
    for x, y in points:
        f.write(f"    ({x}, {y}),\n")
    f.write("]\n")

print("Sauvegardé dans points_track25.py")