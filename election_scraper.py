import sys
import save_csv_func


def main():
    """
    Main function that start the program
    RUNNING FILE REQUIRES THE ENTRY URL(DISTRICT URL)
    AND FILE NAME UNDER WHICH IT IS SAVED
    """
    print(f"DOWNLOADING DATA FROM SELECTED URL: {district_url}")
    save_csv_func.create_csv(district_url, save_to)
    print("QUITTING: election scraper")


if __name__ == '__main__':
    district_url = sys.argv[1]
    save_to = sys.argv[2]
    main()
else:
    print("RUNNING FILE REQUIRES THE ENTRY URL AND FILE NAME UNDER WHICH IT IS SAVED")
