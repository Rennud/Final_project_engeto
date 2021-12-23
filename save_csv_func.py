import csv
import scrape_func


def create_csv(district_url, filename):
    """
    Function that use functions from scrape_func script, create multiple lists that each list contains data that
    are saved as one column in csv under proper header.
    """

    code_location = scrape_func.get_location_code(district_url)
    cities_url = scrape_func.get_cities_url(district_url)
    # That is just for help to create a header
    politic_parties_names, values = scrape_func.get_political_parties_dict(cities_url[1])
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
    ods = [i[0] for i in votes_parties]
    rn_vu = [i[1] for i in votes_parties]
    cos = [i[2] for i in votes_parties]
    cssd = [i[3] for i in votes_parties]
    rc = [i[4] for i in votes_parties]
    stan = [i[5] for i in votes_parties]
    komun = [i[6] for i in votes_parties]
    zel = [i[7] for i in votes_parties]
    rozum = [i[8] for i in votes_parties]
    sso = [i[9] for i in votes_parties]
    bpi = [i[10] for i in votes_parties]
    oda = [i[11] for i in votes_parties]
    pirati = [i[12] for i in votes_parties]
    unie_havel = [i[13] for i in votes_parties]
    ref_eu = [i[14] for i in votes_parties]
    top = [i[15] for i in votes_parties]
    ano = [i[16] for i in votes_parties]
    dv = [i[17] for i in votes_parties]
    spr = [i[18] for i in votes_parties]
    kdu = [i[19] for i in votes_parties]
    csns = [i[20] for i in votes_parties]
    realiste = [i[21] for i in votes_parties]
    sportovci = [i[22] for i in votes_parties]
    dsss = [i[23] for i in votes_parties]
    spd = [i[24] for i in votes_parties]
    spo = [i[25] for i in votes_parties]
    # I use zip to save the data to csv in the required order
    rows = zip(code, location, registered, valid, envelopes, ods, rn_vu, cos, cssd,
               rc, stan, komun, zel, rozum, sso, bpi, oda, pirati, unie_havel, ref_eu,
               top, ano, dv, spr, kdu, csns, realiste, sportovci, dsss, spd, spo)
    # Creating csv file
    header = ["CODE", "LOCATION", "REGISTERED", "ENVELOPES", "VALID"]
    print(f"SAVING TO FILE: {filename}")
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for name in names:
            header.append(name)
        writer.writerow(header)
        writer.writerows(rows)
