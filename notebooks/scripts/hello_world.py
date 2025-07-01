import datetime
# This script prints the current date and time formatted as YYYY-MM-DD HH:MM:SS

def main():
    print(f"Hello World! It is currently {datetime.datetime.now().strftime('%H:%M:%S')}, Look mom, no inputs!")

if __name__ == "__main__":
    main()