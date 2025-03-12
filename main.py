from parse_block import row_aggregate

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import os
import time

with open("./data/links.json", "r") as f:
    sub_urls = json.load(f)
    print('___File "./data/links.json" loaded!')


with open("data/dataset.jsonl", "a", encoding="utf-8") as f:
    os.environ["TZ"] = "Asia/Bishkek"
    time.tzset()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    for url in tqdm(sub_urls):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        row = row_aggregate(soup)
        row["link"] = url
        row["current_time"] = current_time
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
