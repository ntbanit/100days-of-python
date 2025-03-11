from PIL import Image

# Open the PNG image
img = Image.open("tomato.png")

# Save as ICO
img.save("tomato.ico", format="ICO", sizes=[(60, 60)])