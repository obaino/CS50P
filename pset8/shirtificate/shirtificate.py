# https://cs50.harvard.edu/python/2022/psets/8/shirtificate/

from fpdf import FPDF
from PIL import Image

img = Image.open("shirtificate.png")
shirt_pdf = FPDF("P", "mm", "A4")
shirt_pdf.add_page()
shirt_pdf.set_font("helvetica", "", 48)
shirt_pdf.cell(0, 15, "CS50 Shirtificate", align="C", new_x="LEFT", new_y="NEXT")
shirt_pdf.image(img, 0)


shirt_pdf.output("shirt_cs50.pdf")