from PIL import Image, ImageDraw

# Create a blank image with RGBA (transparent) background
size = 512
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw gradient background (blue shades)
for i in range(size // 2):
    color = (
        int(37 + (30 * i / (size // 2))),   # R: 37 to 67
        int(99 + (60 * i / (size // 2))),   # G: 99 to 159
        int(235 - (147 * i / (size // 2))), # B: 235 to 88
        255
    )
    draw.ellipse([i, i, size - i, size - i], fill=color)

# Draw base platform (gold)
draw.rectangle([size*0.35, size*0.88, size*0.65, size*0.92], fill="#fbbf24")
draw.rectangle([size*0.31, size*0.92, size*0.69, size*0.96], fill="#f59e0b")

# Draw main pole (silver)
draw.rectangle([size*0.47, size*0.08, size*0.53, size*0.88], fill="#e5e7eb")

# Draw horizontal beam (white)
draw.rectangle([size*0.18, size*0.13, size*0.82, size*0.17], fill="#ffffff")

# Draw left and right scale pans (white)
draw.pieslice([size*0.13, size*0.23, size*0.29, size*0.39], 0, 180, fill="#f8fafc", outline="#ffffff")
draw.pieslice([size*0.71, size*0.23, size*0.87, size*0.39], 0, 180, fill="#f8fafc", outline="#ffffff")

# Draw chains (white)
for x in [size*0.20, size*0.25]:
    draw.line([x, size*0.17, x, size*0.29], fill="#ffffff", width=6)
for x in [size*0.75, size*0.80]:
    draw.line([x, size*0.17, x, size*0.29], fill="#ffffff", width=6)

# Draw top ornament (gold)
draw.ellipse([size*0.45, size*0.05, size*0.55, size*0.13], fill="#fbbf24")

# Save as PNG
img.save("favicon.png", format="PNG")
print("High-end favicon.png generated successfully!")