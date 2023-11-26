import boto3
import fitz
import pytesseract
from PIL import Image

bucket_name = "anna-lybid-s3-demo"
key = "My CV/CV. Anna Lybid. Python developer.pdf"

s3 = boto3.client("s3")

response = s3.get_object(Bucket=bucket_name, Key=key)

pdf_data = response["Body"].read()

pdf_document = fitz.open(stream=pdf_data, filetype='pdf')

first_page = pdf_document.load_page(0)
image = first_page.get_pixmap()

image_path = "images/converted_from_pdf.png"
image.save(image_path)

img = Image.open(image_path)
text = pytesseract.image_to_string(img)

print(text)
