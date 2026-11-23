from PIL import Image, ImageDraw, ImageFont, ImageOps

SCENE = "/home/hatch/workspace/makefun/gta6-meme-x-01/media-generation-memex-scene-v1-0-2c50fa2e-ef75-4cce-83ef-0e5e5e1e77ed.png"
GHOST = "/home/hatch/workspace/makefun/gta6-meme-x-01/ghost-mark-1024.png"
FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

canvas = ImageOps.fit(Image.open(SCENE).convert("RGBA"), (1024, 1024), Image.Resampling.LANCZOS)
ghost = Image.open(GHOST).convert("RGBA").resize((280, 280), Image.Resampling.LANCZOS)
canvas.paste(ghost, (372, 372), ghost)
draw = ImageDraw.Draw(canvas)

def put_text(y, text, size, fill, stroke=4):
    font = ImageFont.truetype(FONT_PATH, size)
    draw.text((512, y), text, font=font, fill=fill, anchor="mm", stroke_width=stroke, stroke_fill=(15, 10, 25))

put_text(72, "GRAND THEFT AUTO VI", 66, (255, 255, 255))
put_text(684, "make.fun", 38, (255, 0, 200), stroke=3)
put_text(732, "LOADING VICE CITY... 99%", 28, (255, 255, 255), stroke=3)

bx, by, bw, bh = 162, 758, 700, 34
draw.rectangle([bx, by, bx + bw, by + bh], fill=(20, 10, 30, 210), outline=(255, 255, 255), width=3)
fill_w = int((bw - 8) * 0.99)
draw.rectangle([bx + 4, by + 4, bx + 4 + fill_w, by + bh - 4], fill=(255, 0, 190))

put_text(868, "13 YEARS. 2 DELAYS. 1 DOWNLOAD.", 42, (255, 255, 255))
put_text(942, "WORTH IT.", 64, (255, 215, 0))
canvas.convert("RGB").save("meme.png", format="PNG", optimize=True)
