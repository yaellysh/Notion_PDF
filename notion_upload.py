import requests


def upload_image_to_notion(notion_token: str, page_id: str, image_url: str):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"

    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28", 
    }

    data = {
        "children": [
            {
            "object": "block",
            "type": "image",
            "image": {
                "type": "external",
                "external": {
                "url": f"{image_url}"
                }
            }
            }
        ]
    }

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code != 200:
        print("Error:", response.json())

