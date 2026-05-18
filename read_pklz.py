import zipfile
import pickle
import pandas as pd

path = r"C:\Users\houss\sn-gamestate\outputs\sn-gamestate\2026-05-13\00-20-38\states\sn-gamestate.pklz"

with zipfile.ZipFile(path, "r") as z:

    with z.open("021.pkl") as f:
        det = pickle.load(f)

    with z.open("021_image.pkl") as f:
        img = pickle.load(f)

# =========================
# FRAME 1
# =========================

# choose frame
frame_number = 1

# get corresponding image row
image_row = img[img["frame"] == frame_number].iloc[0]

image_id = image_row["id"]

# detections for that frame
frame_det = det[det["image_id"] == image_id].copy()

# extract x,y from bbox_pitch
frame_det["x"] = frame_det["bbox_pitch"].apply(
    lambda d: d.get("x_bottom_middle") if isinstance(d, dict) else None
)

frame_det["y"] = frame_det["bbox_pitch"].apply(
    lambda d: d.get("y_bottom_middle") if isinstance(d, dict) else None
)

print("\nFRAME:", frame_number)
print("IMAGE:", image_row["file_path"])

print("\nPLAYER POSITIONS:")
print(frame_det[["image_id", "category_id", "bbox_conf", "x", "y"]])

print(det.columns)

# =========================
# FRAME 49
# =========================

# choose frame
frame_number = 49

# get corresponding image row
image_row = img[img["frame"] == frame_number].iloc[0]

image_id = image_row["id"]

# detections for that frame
frame_det = det[det["image_id"] == image_id].copy()

# extract x,y from bbox_pitch
frame_det["x"] = frame_det["bbox_pitch"].apply(
    lambda d: d.get("x_bottom_middle") if isinstance(d, dict) else None
)

frame_det["y"] = frame_det["bbox_pitch"].apply(
    lambda d: d.get("y_bottom_middle") if isinstance(d, dict) else None
)

print("\nFRAME:", frame_number)
print("IMAGE:", image_row["file_path"])

print("\nPLAYER POSITIONS:")
print(frame_det[["image_id", "category_id", "bbox_conf", "x", "y"]])

print(det.columns)