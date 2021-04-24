import csv
import datetime
import subprocess
import string
import time
from glob import glob
from sys import exit
import sys

from analyze.process import AnalyzeScreenshot

prod_url_list = []
prod_name_list = []
test_url_list = []
test_name_list = []
ready_csv_list = []
list = []

DIR_PROD = 'screenshots/prod'
DIR_TEST = 'screenshots/test'
# URL_PROD = "https://www.pmiscience.com/"
# URL_TEST = "https://pmisciencetst.pconnect.biz/"

UYW = 'https://www.unsmokeyourworld.com/'
UYM = 'https://www.unsmokeyourmind.com/'
NAAT = 'https://www.worldnoashtray.com/'
MW = 'https://www.missionwinnow.com/en/'

UYW_CSV = 'UYW_prod_all.csv'
UYM_CSV = 'UYM_prod_all.csv'
NAAT_CSV = 'NAAT_prod_all.csv'
MW_CSV = 'MW_prod_all.csv'
validCsv = ''
validLenght = 0
level = ''
levelpy = ''

# TIMESTAMP = str(datetime.datetime.now().isoformat()).replace(":", "-")[:10]
TIMESTAMP = str(datetime.datetime.now()).split(".")[0].replace(" ", "__").replace(":", "-")

ae = AnalyzeScreenshot()


def set_variables():
    global validCsv
    global validLenght
    global level
    global levelpy
    valueSiteName = input("Please enter a site name (UYW or UYM or NAAT or MW) : ").upper()
    valueLevel = input("Please enter the level (Before for 'B' or After for 'A') : ").upper()

    if valueLevel == "B":
        level = "baseline=True"
        levelpy = "baseline"
    elif valueLevel == "A":
        level = "level=2"
        levelpy = "level_2"
    else:
        print("Please enter valid value  (Before for 'B' or After for 'A') !!!")
        sys.exit()

    if valueSiteName == "UYW":
        validCsv = UYW_CSV
        validLenght = len(UYW)
    elif valueSiteName == "UYM":
        validCsv = UYM_CSV
        validLenght = len(UYM)
    elif valueSiteName == "NAAT":
        validCsv = NAAT_CSV
        validLenght = len(NAAT)
    elif valueSiteName == "MW":
        validCsv = MW_CSV
        validLenght = len(MW)
    else:
        print("Please enter valid site name (UYM or UYM or NAAT or MW) !!!")
        sys.exit()


def prepare_csv(badCsv, list):
    with open(badCsv, encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',', quotechar='"')
        next(csv_reader)
        for csv_row in csv_reader:
            if '200' in csv_row[2]:
                list.append(csv_row[0])


def check_file_presence(filename):
    while True:
        if filename in glob(f"screenshots/*.png"):
            break
        else:
            time.sleep(0.2)


def read_csv(file, user_list):
    with open(file, encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',', quotechar='"')
        next(csv_reader)
        for csv_row in csv_reader:
            user_list.append(csv_row[0])


"""
def cut_and_add(env_url_list, suffix_url_list, cut):
    for url in env_url_list:
        suffix_url_list.append(str(url[int(cut):]))


def create_common_suffixes_list(user_list_1, user_list_2):
    return list(set(user_list_1).intersection(user_list_2))


def create_url_for_scan(suffixes_list):
    prod_url_scan = []
    for suffix in suffixes_list:
        prod_url_scan.append(f'{URL_PROD}{suffix}')
    return prod_url_scan


def create_screenshots(suffixes_list, timestamp):
    env_urls = create_url_for_scan(suffixes_list)
    for _ in range(0, len(suffixes_list) - 1):
        ae.screenshot(env_urls[_], suffixes_list[_].replace('/', '_'), timestamp)

"""


def main_dom():
    tests = ''
    set_variables()
    prepare_csv(validCsv, prod_url_list)
    env_urls = sorted(prod_url_list)

    for _ in range(0, len(prod_url_list)):
        filename = f'[{_ + 1}] ' + str(env_urls[_])[validLenght:].replace('/', '_') \
            .replace('-', '_') \
            .replace('.', '_') \
            .replace('?', '_') \
            .replace('=', '_') \
            .replace('&', '_') \
            .replace('%', '_') \
            .replace('(', '') \
            .replace(')', '').replace('.html_', '')
        print(f'[{_}] {env_urls[_]}')
        # ae.screenshot(env_urls[_], filename, TIMESTAMP)

        ######################### START CHANGING DATA HERE #########################
        if 'www.unsmokeyourworld.com/cr' in env_urls[_]:

            tests += f'''
        def test_differences_{_}(self):
            self.get("{env_urls[_]}")
            self.click('//button[text()="Sí"]')
            self.check_window(name="{env_urls[_][12:validLenght].replace(".com/","")}", {level})
            '''
        else:
            tests += f'''
        def test_differences_{_}(self):
            self.get("{env_urls[_]}")
            self.check_window(name="{env_urls[_][12:validLenght].replace(".com/","")}", {level})
            '''

    with open("template.txt") as f:
        txt = f.read()
    with open(f'pmi_vt_{levelpy}.py', 'w', encoding='utf-8') as wf:
        wf.write(string.Template(txt).safe_substitute(test=tests))

        subprocess.run(["pytest", f"pmi_vt_{levelpy}.py", "-v", "--maximize-window", "--headless",
                    f"--html={TIMESTAMP}_dom_report.html"])


######################### STOP CHANGING DATA HERE #########################


if __name__ == '__main__':
    main_dom()
