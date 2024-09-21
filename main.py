from notion_upload import upload_image_to_notion
from s3_upload import upload_image_to_s3, get_s3_image_links
from presentation_convert import convert_pdf_to_images
import sys, shutil, os

def main():

    if len(sys.argv) < 3:
        print("Usage: python main.py <PDF path> <Page ID>")
        sys.exit()

    path = sys.argv[1]
    page_id = sys.argv[2]     

    directory_name = "/Users/yaellyshkow/Desktop/test"

    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' created successfully!")
    except Exception as e:
        print(f"Error creating directory: {e}") 

    folder_name = path.split("/")[-1].strip(".pdf")
    
    folder_path = convert_pdf_to_images(path, directory_name)

    sorted_files = sorted(os.listdir(folder_path), key=lambda x: int(x.split('.')[0]))
    for file in sorted_files:
        file_path = os.path.join(folder_path, file)
        file_name = file_path.split("/")[-1]

        if os.path.isfile(file_path):
            upload_image_to_s3(file_path, 'pptxnotion', f"{folder_name}/{file_name}")

    print("Uploaded to S3!")

    notion_token = os.getenv('NOTION_TOKEN')
    
    bucket_name = 'pptxnotion'
    sorted_aws_files = sorted(get_s3_image_links(bucket_name, folder_name),
                               key=lambda x: int(x.replace("https://pptxnotion.s3.us-east-2.amazonaws.com/", "").split("/")[-1].split('.')[0]))
    
    count = 1
    total = len(sorted_aws_files)
    for image_url in sorted_aws_files:
        upload_image_to_notion(notion_token, page_id, image_url)
        print(f"File {count}/{total} uploaded.")
        count += 1

    print("Images uploaded to Notion!")

    remove_dir(directory_name)
  
    remove_file(path)
    

def remove_file(path: str):
    try:
        os.remove(path)
        print(f"File '{path}' deleted successfully!")
    except FileNotFoundError:
        print(f"File '{path}' does not exist.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def remove_dir(path: str):
    try:
        shutil.rmtree(path)
        print(f"Directory '{path}' deleted successfully!")
    except FileNotFoundError:
        print(f"Directory '{path}' does not exist.")
    except OSError:
        print(f"Directory '{path}' is not empty or cannot be removed.")
    except Exception as e:
        print(f"Error deleting directory: {e}")


if __name__ == "__main__":
    main()