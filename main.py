import threading
from tkinter import *
from tkinter import ttk
from datetime import datetime, time as Time
from time import sleep
from selenium import webdriver  # for operating the website
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.chrome.options import Options as chromeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import ddddocr  # for detecting the confirm code
import base64   # for reading the image present in base 64

class Player:
    def __init__(self, name, jersey_number: int, qualification, photo_link='') -> None:
        self.name = name
        self.jersey_number = jersey_number
        self.qualification = qualification
        self.photo_link = photo_link


class Team:
    def __init__(self, name, contact_person, email, phone_number) -> None:
        self.name = name
        self.contact_person = contact_person
        self.email = email
        self.phone_number = phone_number


class CompetitionSignUp: 
    def __init__(self, competition_url, account, password) -> None:
        self.competition_url = competition_url
        self.account = account
        self.password = password
        self.__init_driver__()

    def __init_driver__(self) -> None:
        set_up_success = True

        try:
            chrome_option = chromeOptions()
            chrome_option.add_argument('--log-level=3')
            self.driver = webdriver.Chrome(
                executable_path=ChromeDriverManager(
                    version='114.0.5735.90').install(),
                options=chrome_option
            )
        except Exception as e:
            set_up_success = False
            print('Chrome Driver Set Up Error')

        if not set_up_success:
            set_up_success = True

            try:
                edge_option = edgeOptions()
                edge_option.add_argument('--log-level=3')
                self.driver = webdriver.Edge(
                    executable_path=EdgeChromiumDriverManager().install(),
                    options=edge_option
                )
            except Exception as e:
                set_up_success = False
                print('Edge Driver Set Up Error')

        if not set_up_success:
            exit(1)

    def get_group_type_options(self) -> list:
        self.driver.get(self.competition_url)

        group_type_table = self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentBody_DIV_Center"]/div[1]/div[2]/div/table/tbody')

        tr_list = group_type_table.find_elements(By.TAG_NAME, 'tr')
        tr_list = tr_list[1:]

        group_type_list = []

        for tr in tr_list:
            td_list = tr.find_elements(By.TAG_NAME, 'td')
            group_type = td_list[0].text
            group_type_list.append(group_type)

        return group_type_list
    
    def __fill_team_info__(self, team_info: Team) -> None:
        team_info_table = self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentBody_TABLE_Team"]/tbody')

        # 將隊伍資訊填入欄位
        # 要注意有可能有額外的欄位 -> 直接預設亂填 先搶到名額再手動更改

    def __fill_players_info__(self, players_info: list[Player]) -> None:
        players_info_table = self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentBody_TABLE_Player"]/tbody')
        
        # 將球員資訊填入各個欄位

    def sign_up(self, group_type) -> None:
        self.driver.get(self.competition_url)

        group_type_table = self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentBody_DIV_Center"]/div[1]/div[2]/div/table/tbody')
        tr_list = group_type_table.find_elements(By.TAG_NAME, 'tr')
        tr_list = tr_list[1:]

        for tr in tr_list:
            td_list = tr.find_elements(By.TAG_NAME, 'td')

            if td_list[0].text == group_type:
                td_list[0].click() 