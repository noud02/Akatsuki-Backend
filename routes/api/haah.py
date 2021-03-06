# Stdlib
from io import BytesIO

# External Libraries
from PIL import Image, ImageOps


def handle(req):
    """POST"""
    im = Image.open(BytesIO(req.files[list(req.files.keys())[0]].body))
    w, h = im.size
    im2 = ImageOps.mirror(im.crop((0, 0, w / 2, h)))

    im.paste(im2, (int(w / 2), 0))
    io = BytesIO()
    im.save(io, format='PNG')

    return req.Response(
        body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
