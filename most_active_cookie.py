import csv
import sys
import re
from os.path import exists
import logging

'''
Author: Aryan Maheshwari
Date: 3/6/2022

Quantcast initial coding assessment.

This program takes in arguments from the command line. The first 
parameter is a csv file. The program reads the csv file and creates a 
dictionary to store the dates and cookies. Then, it analyzes the 
dictionary and finds the most occurring cookies and prints them out.
'''
cookies = {}


class Cookie():
    logging.basicConfig(level=logging.INFO)

    def read_csv_values(self, csv_filepath):
        # read the CSV file and store values
        # date is the key and cookie is the value (as a list)
        logging.info("reading csv file")
        with open(csv_filepath) as csv_file_data:
            csv_reader = csv.reader(csv_file_data, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                cookie = row[0]
                date = row[1].split('T')[0]
                if date in cookies.keys():
                    cookies[date].append(cookie)
                else:
                    cookies[date] = [cookie]

    def lookup_by_date(self, date):
        # input date and find result
        # result(s) will be printed out line by line
        logging.info("searching cookie for given date")
        data = cookies.get(date)
        if data == None:
            return []
        else:
            return self.most_occurring(data)

    def most_occurring(self, data):
        # find most occurring cookie
        # function returns a list because there could be multiple
        logging.info("finding most reoccurring cookie")
        result = []
        cookie_occurrence = {}
        for cookie in data:
            if cookie in cookie_occurrence.keys():
                cookie_occurrence[cookie] += 1
            else:
                cookie_occurrence[cookie] = 1

        max_occurrence = max(cookie_occurrence.values())
        for key, value in cookie_occurrence.items():
            if max_occurrence == value:
                result.append(key)
        return result

    def validate_date(self, date):
        # check whether the date is inputted in the correct format
        pattern = re.compile('\d{4}-\d{2}-\d{2}')
        logging.info("validating date format")
        return pattern.match(date) != None

    def uses():
        # guide user on use
        logging.error("USES: python most_active_cookie.py cookie_log.csv -d 2018-12-08")


if __name__ == '__main__':
    # if there are less than four arguments,
    # meaning the program name, file path, -d, or date
    # is missing, then there will be an error
    cookie = Cookie()
    if len(sys.argv) < 4:
        cookie.uses()
        exit(1)

    if sys.argv[2] != "-d":
        cookie.uses()
        exit(2)
    # a potential error is that the file does not exist
    # check whether the file exists, then proceed
    file_exists = exists(sys.argv[1])
    if file_exists:
        logging.info("csv file exists")
        csv_filepath = sys.argv[1]
        cookie.read_csv_values(csv_filepath)
        # if the date is in the correct format, proceed
        if cookie.validate_date(sys.argv[3]):
            for result in cookie.most_occurring(cookie.lookup_by_date(sys.argv[3])):
                print(result)
        else:
            cookie.uses()
            exit(3)
    else:
        logging.error("ERROR: file does not exist")
        cookie.uses()
        exit(4)
