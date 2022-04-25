import os
import shutil
import argparse
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('contest')

args = parser.parse_args()

contest = args.contest
os.makedirs(contest, exist_ok=True)

tasks = list('abcde')
for task in tqdm(tasks):
    url = f"https://atcoder.jp/contests/{contest}/tasks/{contest}_{task}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('title')[0].text
    shutil.copy('template.py', f'{contest}/{title}.py')
