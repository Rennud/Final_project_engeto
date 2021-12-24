import csv
import scrape_func


def create_csv(district_url, filename):
    """Function that use functions from scrape_func script, create multiple lists that each list contains data that
    are saved as one column in csv under proper header."""

    code_location = scrape_func.get_location_code(district_url)
    cities_url = scrape_func.get_cities_url(district_url)
    # That is just for help to create a header
    politic_parties_names, values = scrape_func.get_political_parties_dict(cities_url[0])
    names = [i for i in politic_parties_names]
    # Scrape data from all urls
    vote_data = list(scrape_func.get_data_all_url(cities_url))
    # Sort data into lists for the use I need
    code = [i for i in code_location.keys()]
    location = [i for i in code_location.values()]
    registered = [i[0] for i in vote_data]
    envelopes = [i[1] for i in vote_data]
    valid = [i[2] for i in vote_data]
    votes_parties = [i[4] for i in vote_data]
    format_votes = [",".join(i).strip("") for i in votes_parties]
    # I use zip to save the data to csv in the required order
    rows = zip(code, location, registered, valid, envelopes, format_votes)
    # Creating csv file
    header = ["CODE", "LOCATION", "REGISTERED", "ENVELOPES", "VALID"]
    print(f"SAVING TO FILE:{filename} .csv")
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, escapechar=" ", quoting=csv.QUOTE_NONE)
        for name in names:
            header.append(name)
        writer.writerow(header)
        writer.writerows(rows)
