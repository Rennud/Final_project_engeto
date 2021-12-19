import sys
import save_csv_func
import scrape_func

url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103"


def main():
    print(f"DOWNLOADING DATA FROM SELECTED URL: {district_url}")
    all_urls = scrape_func.get_cities_url(district_url)
    save_csv_func.create_csv(district_url)

if __name__ == '__main__':
    district_url = sys.argv[1]
    save_to = sys.argv[2]
    main()
else:
    print("RUNNING FILE REQUIRED ENTRY URL AND RUNNING THE FILE REQUIRES THE ENTRY URL AND FILE NAME WHERE YOU WANT "
          "TO SAVE THE DATA")
