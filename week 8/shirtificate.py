from fpdf import FPDF

def main():
    name = input("Your name: ")

    pdf = FPDF()
    pdf.add_page()

    #Title
    pdf.set_font("Helvetica", "B", 36)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C")

    #Shirt image
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    #Name on the shirt
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()



