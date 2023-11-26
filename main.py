import cv2 as cv
from PIL import Image
import pytesseract

image_file = "Images/s3-bucket-with-cv.jpg"

image = cv.imread(image_file)

if image is not None:
    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Image is not found or could not be opened.")

img = Image.open(image_file)

text = pytesseract.image_to_string(img)

print(text)
