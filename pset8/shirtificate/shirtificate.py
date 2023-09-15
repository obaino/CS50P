# https://cs50.harvard.edu/python/2022/psets/8/shirtificate/
# implemented using pillow module

from fpdf import FPDF, Align

user_name = input("Name: ")
text = f"{user_name} took CS50"


# pdf
shirt_pdf = FPDF("P", "mm", "A4")
shirt_pdf.add_page()
shirt_pdf.image("./shirtificate.png", x=Align.C, y=70)
shirt_pdf.set_font("helvetica", "", 48)
shirt_pdf.cell(0, 50, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
shirt_pdf.set_font("helvetica", "B", 24)
shirt_pdf.set_text_color(255,255,255)
text_width = shirt_pdf.get_string_width(text)
shirt_pdf.cell(0, (shirt_pdf.h / 2), text, align="C")


shirt_pdf.output("shirtificate.pdf")
