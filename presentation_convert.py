from pdf2image import convert_from_path
import shutil
import os

def convert_pdf_to_images(pdf_link: str, folder_path: str):

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    images = convert_from_path(pdf_link)

    for i in range(len(images)):
        
        images[i].save(f'{folder_path}/{str(i)}.jpg', 'JPEG')

    print("Done converting!")
    return folder_path