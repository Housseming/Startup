import cv2
 
img = cv2.imread("images/image1.png")

h, w = img.shape[:2]
 
out = cv2.VideoWriter(

    "images/image1.mp4",

    cv2.VideoWriter_fourcc(*"mp4v"),

    1,

    (w, h)

)
 
for _ in range(5):

    out.write(img)
 
out.release()
 
print("Video créée : images/image1.mp4")
 