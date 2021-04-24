"""import csv

from analyze.process import AnalyzeScreenshot

ae = AnalyzeScreenshot()

def prepare_csv(badCsv, list):
    with open(badCsv, encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',', quotechar='"')
        next(csv_reader)
        for csv_row in csv_reader:
            if '.html/' in csv_row[2]:
                pass
            elif '.txt' in csv_row[0]:
                pass
            elif '.jpg' in csv_row[0]:
                pass
            elif '.png' in csv_row[0]:
                pass
            elif 'svg' in csv_row[0]:
                pass
            elif 'js' in csv_row[0]:
                pass
            elif 'css' in csv_row[0]:
                pass
            elif 'xml' in csv_row[0]:
                pass
            elif '.pdf' in csv_row[0]:
                pass
            elif 'com/whitepaper' in csv_row[0]:
                pass
            elif 'http:' in csv_row[0]:
                pass
            else:
                list.append(csv_row[0])



ae.screenshot('https://www.unsmokeyourworld.com/cr.html/', 'filename','TIMESTAMP')








"""
UYW_CSV = 'UYW_prod_all.csv'
UYM_CSV = 'UYM_prod_all.csv'
NAAT_CSV = 'NAAT_prod_all.csv'
MW_CSV = 'MW_prod_all.csv'
validCsv = 'WE'


def device_site():
    global validCsv
    value = input("Please enter a site name:")

    if value == "UYW":
        a = UYW_CSV
    elif value == "UYM":
        a = UYM_CSV
    elif value == "NAAT":
        a = NAAT_CSV
    elif value == "MW":
        a = MW_CSV
    else:
        print("Please enter valid site name !!!")
        exit()


def main_dom():
    device_site()
    print(validCsv)

if __name__ == '__main__':
    main_dom()
