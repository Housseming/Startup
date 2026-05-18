from ultralytics import YOLO
import cv2
 
image_path = "images/image1.png"
model_path = "pretrained_models/yolo/yolo11m.pt"
 
print("Chargement image:", image_path)
img = cv2.imread(image_path)
 
if img is None:
    print("ERREUR: image introuvable")
    exit()
 
print("Image OK:", img.shape)
 
print("Chargement modèle:", model_path)
model = YOLO(model_path)
 
results = model(img, conf=0.25)
 
print("Nombre de résultats:", len(results))
points=[]
for r in results:
    print("Nombre de boxes:", len(r.boxes))
 
    for i, b in enumerate(r.boxes):
        x1, y1, x2, y2 = b.xyxy.cpu().numpy()[0]
        conf = float(b.conf.cpu().numpy()[0])
        cls = int(b.cls.cpu().numpy()[0])
 
        x = (x1 + x2) / 2
        y = y2
        points.append((x,y))
        print(f"Objet {i}: classe={cls}, conf={conf:.2f}, x={x:.2f}, y={y:.2f}")
 
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
        cv2.circle(img, (int(x), int(y)), 6, (0,0,255), -1)
print(points)
cv2.imwrite("images/result_image1.png", img)
print("Image résultat sauvegardée: images/result_image1.png")