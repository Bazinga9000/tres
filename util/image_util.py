from PIL import Image

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

def image_row(images: list[Image.Image]) -> Image.Image:
    '''
    Given a set of images, create a single image where the composite images are placed left to right
    '''
    assert images != []

    total_width = sum([i.width for i in images])
    max_height = max([i.height for i in images])

    out = Image.new("RGBA", (total_width, max_height))
    accum = 0

    for im in images:
        out.paste(im, (accum, 0))
        accum += im.width

    return out


def image_column(images: list[Image.Image]) -> Image.Image:
    '''
    Given a set of images, create a single image where the composite images are placed top to bottom
    '''
    assert images != []

    max_width = max([i.width for i in images])
    total_height = sum([i.height for i in images])

    out = Image.new("RGBA", (max_width, total_height))
    accum = 0

    for im in images:
        out.paste(im, (0, accum))
        accum += im.height

    return out
