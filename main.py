# Generate Automatic Script
from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/Poppins-Regular.ttf', 180)
FONT_COLOR = "#0b0b0c"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

def create_certificates(name):
    #function to create certificate
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)

    #Set the height and weight of text
    text_width, text_height = draw.textsize(name, font=FONT_FILE)

    #Set it in center then make adjustment
    draw.text(((WIDTH - text_width) / 2, ((HEIGHT+60) - text_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name +".png")
    print('Certificate has saved of:', name)        

if __name__ == "__main__":

    names = []

with open('names.txt') as f:
    content = f.readlines()
    for item in content:
        names.append(item[:-1].title())
    
    for name in names:
        create_certificates(name)

    print(len(names), "Certificates has been generated.")
