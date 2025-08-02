from PIL import Image
import discord
import io

def open_rgba(file: str) -> Image.Image:
    out = Image.open(file)
    return out.convert("RGBA")

def compose_files(files: list[str]) -> Image.Image:
    '''
    Given a list of files, create an image by overlaying the files on top of each other.
    '''
    assert files != []
    out = open_rgba(files[0])

    for f in files[1:]:
        foreground = open_rgba(f)
        out.paste(foreground, (0,0), foreground)
    return out

def image_row(images: list[Image.Image], offset: int = 0, center: bool = False) -> Image.Image:
    '''
    Given a set of images, create a single image where the composite images are placed left to right.

    If offset is set, overlay each image on top of the previous one with an overlap of that much.
    If center is set, images will be aligned to the center
    '''
    assert images != []

    total_width = sum([i.width for i in images]) - (offset * len(images))
    max_height = max([i.height for i in images])

    out = Image.new("RGBA", (total_width, max_height))
    accum = 0

    for im in images:
        if center:
            y = (max_height - im.height)//2
        else:
            y = 0
        out.paste(im, (accum, y))
        accum += im.width
        accum -= offset

    return out


def image_column(images: list[Image.Image], offset: int = 0, center: bool = False) -> Image.Image:
    '''
    As image_row, but lays the images top to bottom.
    '''
    assert images != []

    max_width = max([i.width for i in images])
    total_height = sum([i.height for i in images]) - (offset * len(images))

    out = Image.new("RGBA", (max_width, total_height))
    accum = 0

    for im in images:
        if center:
            x = (max_width - im.width)//2
        else:
            x = 0
        out.paste(im, (x, accum))
        accum += im.height
        accum -= offset

    return out

def as_discord_file(im: Image.Image, filename: str) -> discord.File:
    '''
    Convert an image into a discord File.
    '''
    with io.BytesIO() as binary:
        im.save(binary, "PNG")
        binary.seek(0)
        file = discord.File(fp=binary, filename="gamestate.png")

    return file
