import os
import zipfile
import docx
import random
import string
from django.conf import settings


def docx_file_parse(document):
    lst = []
    for paragraphs in docx.Document(document).paragraphs:
        if paragraphs.text != '':
            lst.append(paragraphs.text.replace(" ", "").split(':'))
    image = {"Image": str(extend_image(document, settings.MEDIA_ROOT))}
    model_info = dict(lst)
    return {**image, **model_info}


def extend_image(docx: str, img_dir: str):
    zipf = zipfile.ZipFile(docx)
    filelist = zipf.namelist()
    for fname in filelist:
        _, extension = os.path.splitext(fname)
        if extension in [".jpg", ".jpeg", ".png", ".bmp"]:
            img_name = generate_random_string(7) + extension
            dst_fname = os.path.join(img_dir, os.path.basename(img_name))
            with open(dst_fname, "wb") as dst_f:
                dst_f.write(zipf.read(fname))
            return dst_f.name
            break
    zipf.close()
    pass


def generate_random_string(length: int) -> str:
    """
    Generating random string with given length
    used module random
    variable letters = English alfabet
    """
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


"""  obj = Post_written()
    obj.title = "Title"
    obj.author = request.user.profile
    obj.image = ImageFile(open(image.name, "rb"))
    obj.save()
    os.remove(image.name)
    title = "Title"
    category = Category.all_categories.get(name="Community")
    print(image.name)"""
