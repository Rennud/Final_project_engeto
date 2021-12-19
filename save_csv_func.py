import csv
import scrape_func



url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103"


## get_data_all_url -> 4 dict with headers as keys
## get_location_code -> 1 dict with key as data and also value as data
# save it to csv
# set up main func



def create_csv(district_url):
    code_location = scrape_func.get_location_code(district_url)
    political_parties = scrape_func.political_parties_dict("https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=535010&xvyber=2103")
    with open('vote_data.csv', 'w', encoding="utf-8", newline="") as csv_file:
        for key, value in political_parties.items():
            writer = csv.writer(csv_file)
            writer.writerow([key, value])
        header = ["CODE", "LOCATION", "REGISTERED", "ENVELOPES", "VALID", key]
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        writer = csv.writer(csv_file)
        for key, value in code_location.items():
            writer.writerow([key, value])





def load_csv(file_name):
    """Output of all data in csv file"""
    list_csv = list()
    try:
        with open(file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for i in reader:
                list_csv.append(i)
                yield list_csv
    except FileNotFoundError:
        print("CAN'T FIND CSV FILE!")
