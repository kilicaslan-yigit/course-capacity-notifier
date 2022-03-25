# Copyright 2022 by Yigit Kilicaslan.
# All rights reserved.
# This file is part of the Course Capacity Notifier,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# This is an educational project in order to develop the computer scince skills
# use it on your own responsibility.

from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import messagebox
from random import randint
from time import sleep
import sys
import urllib.parse as urlparse


class Notifier:

    def __init__(self, couser_url):
        self.course_url= couser_url
        self.set_crm()

    def set_crm(self):
        parsed = urlparse.urlparse(self.course_url)
        self.crn_in = urlparse.parse_qs(parsed.query)['crn_in'][0]

    def checkCourse(self):
        print('Capacity for',str(self.crn_in),'is ', end='')
        page = requests.get(self.course_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table',attrs={'summary':'This layout table is used to present the seating numbers.'})
        cells = soup.find_all('td',attrs={'class':'dddefault'})
        num_remanig = int(cells[3].text) 
        print(num_remanig)
        if num_remanig > 0:
            root = tk.Tk()
            root.withdraw()
            massage = 'Good things happened! CRN:' + self.crn_in + ' found' 
            messagebox.showwarning('alert title', massage)
            return True
        else: 
            return False

    def run(self,num_of_exect):

        for i in range(num_of_exect):
            self.checkCourse()
            random = randint(30,100)
            print('Re-try in:', random, 'seconds')
            sleep(random)

    
if __name__ == '__main__':

    try:
        course_url = sys.argv[1]
        notifier = Notifier(course_url)
        if sys.argv[2]:
            num_of_exect = int(sys.argv[2])
            notifier.run(num_of_exect)
        else:
            notifier.run(10000)

    except:
        print('Run with the url of the course you want to check for course capacty like the line bellow;')
        print('-python main.py "http://suis.sabanciuniv.edu/prod/bwckschd.p_disp_detail_sched?term_in=202101&crn_in=10099"')