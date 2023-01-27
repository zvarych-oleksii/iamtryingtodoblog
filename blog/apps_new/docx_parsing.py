import os
import zipfile
import docx
import random
import string
from django.conf import settings


def docx_file_parse(document):
    """
    Creating list: lst for values from parsed file
    Reading text from document by docx module
    Extend image from document and create dict with value == path to image
    Updating dicts
    :param file document: Docx file for parsing
    :return: dict: With object data
    """
    lst = []
    for paragraphs in docx.Document(document).paragraphs:
        if paragraphs.text != '':
            lst.append(paragraphs.text.replace(" ", "").split(':'))
    image = {"Image": str(extend_image(document, settings.MEDIA_ROOT))}
    model_info = dict(lst)
    return {**image, **model_info}


def extend_image(docx, img_dir):
    """
    Unzipping by zipfile module
    Loop for while wouldn't find image file in list of files
    Creating name of image by func generate_random_string
    Creating image in directory and reading it
    :param file docx: file for extend
    :param str img_dir: path where to save the image
    :return: dst_f.name: path to extended image
    """
    zipf = zipfile.ZipFile(docx)
    filelist = zipf.namelist()
    for fname in filelist:
        _, extension = os.path.splitext(fname)
        if extension in [".jpg", ".jpeg", ".png", ".bmp"]:
            img_name = generate_random_string(7) + extension
            dst_fname = os.path.join(img_dir, os.path.basename(img_name))
            with open(dst_fname, "wb") as dst_f:
                dst_f.write(zipf.read(fname))
            break
    zipf.close()
    return dst_f.name


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
