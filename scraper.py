"""
scraper.py: třetí projekt do Engeto Online Python Akademie
author: Petr Janovec
email: p.janovec@seznam.cz
discord: djolefola
"""


import sys
import csv
import requests
from bs4 import BeautifulSoup

class ElectionScraper:

    def __init__(self, url):
        """Inicializace třídy s URL odkazem k volebním výsledkům."""
        self.url = url
        self.soup = self.get_soup(self.url)

    def get_soup(self, url):
        """Stáhne HTML obsah z URL a vrátí jako BS objekt."""
        print("STAHUJI DATA Z URL:", url)
        response = requests.get(url)
        return BeautifulSoup(response.text, "html.parser")

    def extract_district_names(self):
        """Vrací seznam názvů volebních obvodů."""
        return [item.text for item in self.soup.find_all("td", "overflow_name")]

    def extract_district_links(self):
        """Vrací seznam odkazů na detailní stránky jednotlivých obvodů."""
        base_url = "https://volby.cz/pls/ps2017nss/"
        return [base_url + item.a["href"] for item in self.soup.find_all("td", "cislo")]

    def extract_district_ids(self):
        """Vrací seznam identifikátorů (ID) jednotlivých obvodů."""
        return [item.text for item in self.soup.find_all("td", "cislo")]

    def extract_parties(self):
        """Vrací seznam stran kandidujících v daném obvodu."""
        my_district_url = self.extract_district_links()[0]
        my_district_soup = self.get_soup(my_district_url)
        return [party.text for party in my_district_soup.find_all("td", "overflow_name")]

    def fetch_voting_data(self):
        """Vrací seznamy registrovaných voličů, účasti a platných hlasů pro všechny obvody."""
        voters, attendance, valid_votes = [], [], []
        for link in self.extract_district_links():
            district_soup = self.get_soup(link)
            voters.extend([item.text.replace('\xa0', ' ') for item in district_soup.find_all("td", headers="sa2")])
            attendance.extend([item.text.replace('\xa0', ' ') for item in district_soup.find_all("td", headers="sa3")])
            valid_votes.extend([item.text.replace('\xa0', ' ') for item in district_soup.find_all("td", headers="sa6")])
        return voters, attendance, valid_votes

    def extract_vote_count(self):
        """Vrací počet hlasů pro všechny strany v obvodech."""
        votes_list = []
        for link in self.extract_district_links():
            district_soup = self.get_soup(link)
            votes = [item.text for item in district_soup.find_all("td", "cislo", headers=["t1sb3", "t2sb3"])]
            votes_list.append(votes)
        return votes_list

    def generate_csv_rows(self):
        """Generuje obsah CSV souboru jako seznam řádků."""
        rows = []
        districts = self.extract_district_names()
        ids = self.extract_district_ids()
        voters, attendance, valid_votes = self.fetch_voting_data()
        vote_count = self.extract_vote_count()

        for i, (id_, district, voter, attend, valid_vote, vote_perc) in enumerate(zip(ids, districts, voters, attendance, valid_votes, vote_count)):
            rows.append([id_, district, voter, attend, valid_vote] + vote_perc)

        return rows

    def save_to_csv(self, filename):
        """Uloží volební výsledky do CSV souboru."""
        header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy'] + self.extract_parties()
        content = self.generate_csv_rows()

        print("UKLÁDÁM DATA DO SOUBORU:", filename)
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(content)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Neplatný počet argumentů. Ukončuji...')
    else:
        scraper = ElectionScraper(sys.argv[1])
        scraper.save_to_csv(sys.argv[2])
