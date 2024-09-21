# Embed PDF presentation in Notion as Individual Images
## Description
The goal of this small project was to automate the process of splitting a PDF presentation into individual images and then embedding these inside a given Notion page to have all my notes for a lecture in one specific place. The splitting of the PDF was simple using the pdf2image Python library, but to use the Notion API to add images to a page, those images must be hosted remotely so I have to write code that uploaded these images to an AWS S3 bucket to then embed within the Notion page as a link.

## Getting Started

### Dependencies
* [sys](https://docs.python.org/3/library/sys.html) (for using command line arguments)
* [shutil](https://docs.python.org/3/library/shutil.html) (for removing local files when done)
* [os](https://docs.python.org/3/library/os.html) (like above, deleting local versions of files/folders)
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (for dealing with AWS S3)
* [requests](https://pypi.org/project/requests/) (for Notion API call)
* [pdf2image](https://pypi.org/project/pdf2image/) (for converting PDF to images)
* [botocore](https://github.com/boto/botocore) (for raising expections for boto3)

### Installing
Files required:
   * main.py
   * presentation_convert.py (splits PDF into images and saves locally)
   * s3_upload.py (uploads images to AWS S3 bucket, returns list of files in bucket)
   * notion_upload.py (uses Notion API to add images to Notion page)

### Executing program
* Run the main program through command line with two arguments:
  * Path to the pdf file
  * ID of the relevent Notion page

```
python3 main 'path/to/pdf' 'notion-page-id'
```
* n.b. to get the ID of the Notion page, click on the three dots, click copy link, and copy everything between 'pagetitle-' and '?': this is the Notion page ID
* Also to use a different S3 bucket just change the name within the main.py file and set up access locally accordingly

## Authors

Yael Lyshkow

## Version History

* 0.1
    * Initial Release
