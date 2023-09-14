# https://cs50.harvard.edu/python/2022/psets/8/shirtificate/

from fpdf import FPDF, Align
from PIL import Image, ImageFont, ImageDraw

user_name = input("Name: ")
text = f"{user_name} took CS50"

img = Image.open("shirtificate.png")
myFont = ImageFont.truetype("Arial", size=24)
new_img = ImageDraw.Draw(img)
new_img = img.resize((round(img.size[0] * 0.91), round(img.size[1] * 0.91)))
width, height = new_img.size
length = myFont.getlength(text)
ImageDraw.Draw(new_img).text(
    ((width - length) / 2, (height - 25) / 3), text, fill=(255, 255, 255), font=myFont
)

# pdf
shirt_pdf = FPDF("P", "mm", "A4")
shirt_pdf.add_page()
shirt_pdf.set_font("helvetica", "", 48)
shirt_pdf.cell(0, 50, "CS50 Shirtificate", align="C")
shirt_pdf.image(new_img, x=Align.C, y=70)


shirt_pdf.output("shirtificate.pdf")
