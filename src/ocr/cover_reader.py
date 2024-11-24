import pytesseract
from PIL import Image
import os
from config import TEESERACT_PATH 

pytesseract.pytesseract.tesseract_cmd = TEESERACT_PATH

def get_bookname_from_ocr(image_directory):
    cover_name_dict = []
    files = os.listdir(image_directory)

    for file in files:
        image_path = os.path.join(image_directory, file)
        
        image = Image.open(image_path)
        string = pytesseract.image_to_string(image, lang='rus')

        cover_name_dict[image_path] = string

    return cover_name_dict

async def corr_image_to_db():
    # connect to db and check coorespondence to db data
    pass

if __name__ == "__main__":
    get_bookname_from_ocr("./uploads")
