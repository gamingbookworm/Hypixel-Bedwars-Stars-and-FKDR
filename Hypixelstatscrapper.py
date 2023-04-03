import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
from selenium import webdriver

# create an instance of the webdriver
driver = webdriver.Firefox()

# Set up Firefox webdriver
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
firefox_driver_path = r"C:\Users\natal\Documents\Firefox driver\geckodriver.exe"
service = Service(firefox_driver_path)

# Set up Excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "Player Stats"
worksheet.append(["Player", "Bedwars Stars", "Solos FKDR", "Doubles FKDR", "3v3v3v3 FKDR", "4v4v4v4 FKDR", "Overall FKDR"])

# List of players to scrape data for
players = ["stevenr8", "propenguin44", "gamingbookworm_4"]

# Scrape data for each player
for player in players:
    # Construct URL for player
    url = f"https://plancke.io/hypixel/player/stats/{player}"
    
    # Get web page
    driver.get(url)
    
    # Wait for page to load
    time.sleep(5)
    
    # Extract data
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    bedwars_stars = soup.find("div", {"data-text": "Bed Wars"}).find_all("span", {"class": "text-orange-500 font-semibold text-lg"})[0].get_text()
    solos_fkdr = soup.find("a", {"data-mode": "BedWars: Solo"}).find("span", {"class": "font-semibold text-lg"}).get_text()
    doubles_fkdr = soup.find("a", {"data-mode": "BedWars: Doubles"}).find("span", {"class": "font-semibold text-lg"}).get_text()
    threes_fkdr = soup.find("a", {"data-mode": "BedWars: 3v3v3v3"}).find("span", {"class": "font-semibold text-lg"}).get_text()
    fours_fkdr = soup.find("a", {"data-mode": "BedWars: 4v4v4v4"}).find("span", {"class": "font-semibold text-lg"}).get_text()
    overall_fkdr = soup.find("a", {"data-mode": "Overall"}).find("span", {"class": "font-semibold text-lg"}).get_text()
    
    # Print data to console
    print(f"{player}: Bedwars Stars: {bedwars_stars}, Solos FKDR: {solos_fkdr}, Doubles FKDR: {doubles_fkdr}, 3v3v3v3 FKDR: {threes_fkdr}, 4v4v4v4 FKDR: {fours_fkdr}, Overall FKDR: {overall_fkdr}")
    
    # Write data to Excel worksheet
    worksheet.append([player, bedwars_stars, solos_fkdr, doubles_fkdr, threes_fkdr, fours_fkdr, overall_fkdr])

# Sort data in Excel worksheet by Overall FKDR column in descending order
worksheet.sort_column = 7
worksheet.sort_descending()

# Save Excel workbook
filepath = r"C:\Users\natal\Documents\output.xlsx"  # Replace 'user' with your actual user name
workbook.save(filepath)

# Close Firefox webdriver
driver.quit()
