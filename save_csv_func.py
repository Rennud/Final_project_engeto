import csv
import scrape_func
import pandas as pd

url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103"


def create_csv(district_url):
    code_location = scrape_func.get_location_code(district_url)
    cities_url = scrape_func.get_cities_url(district_url)
    politic_parties_names, values = scrape_func.get_political_parties_dict(cities_url[0])
    names = [i for i in politic_parties_names]
    print(names)
    vote_data = tuple(scrape_func.get_data_all_url(cities_url))
    reg = [i[0] for i in vote_data]
    env = [i[1] for i in vote_data]
    val = [i[2] for i in vote_data]
    votes_parties = [i[4] for i in vote_data]
    print(votes_parties)
    header = ["CODE", "LOCATION", "REGISTERED", "ENVELOPES", "VALUE"]
    with open("testr.csv", "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for i, name in enumerate(names):
            header.append(name)
        writer.writerow(header)
        for key, value in code_location.items():
            writer.writerow([key, value])
        for i[0] in vote_data:
            writer.writerow(i)







    #df.to_csv("vote_data.csv", index=False)

create_csv(url)


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
