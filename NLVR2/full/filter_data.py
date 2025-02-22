import json
import os
import requests
from tqdm import tqdm


def filter_examples(filename):
    n_images = 0
    url_imageid = dict()

    with open(filename) as infile:
        original_examples = [json.loads(line) for line in infile if line]

    filtered_examples = list()

    for example in tqdm(original_examples):
        urls = example["left_url"], example["right_url"]
        try:
            if urls[0] not in url_imageid:
                response = requests.get(urls[0], timeout=20)
                if response.status_code != 200:
                    print("Error downloading image", urls)
                    continue
                # test if it is a valid image
                if not response.headers['Content-Type'].startswith('image'):
                    print("Error downloading image", urls)
                    continue
            if urls[1] not in url_imageid:
                response = requests.get(urls[1], timeout=20)
                if response.status_code != 200:
                    print("Error downloading image", urls)
                    continue
                if not response.headers['Content-Type'].startswith('image'):
                    print("Error downloading image", urls)
                    continue
        except:
            print("Error downloading image", urls)
            continue

        if urls[0] not in url_imageid:
            # download the image
            response = requests.get(urls[0])
            # image id is a 4 digit number. If n_images is 0, the first image will be 0000.jpg
            image_id = str(n_images).zfill(4)
            if response.status_code == 200:
                with open(image_id + '.jpg', 'wb') as f:
                    f.write(response.content)
                url_imageid[urls[0]] = image_id
                n_images += 1
            else:
                raise Exception("Error downloading image", urls[0])
        if urls[1] not in url_imageid:
            # download the image
            response = requests.get(urls[1])
            # image id is a 4 digit number. If n_images is 0, the first image will be 0000.jpg
            image_id = str(n_images).zfill(4)
            if response.status_code == 200:
                with open(image_id + '.jpg', 'wb') as f:
                    f.write(response.content)
                url_imageid[urls[1]] = image_id
                n_images += 1
            else:
                raise Exception("Error downloading image", urls[1])
        example["left_image_id"] = url_imageid[urls[0]]
        example["right_image_id"] = url_imageid[urls[1]]
        filtered_examples.append(example)

    with open(filename.replace(".json", "_filtered.json"), "w") as outfile:
        for example in filtered_examples:
            json.dump(example, outfile)
            outfile.write("\n")
filter_examples("test1.json")
