"""CIS189 Python
Author: Greg Tarr
Created: 11/12/2019"""
import csv
from model.CountyCensus import CountyCensus

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county = {}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        if row[0] == '':
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        county[str(row[1])] = CountyCensus(row[0], row[1], row[2], row[3]
                                           , row[4], row[5], row[6])


    def population_per_household(search_item, county_dict={'key':CountyCensus}):
        """This takes a county to search for, and a dictionary of counties, and searches
        the dictionary for the supplied search value. The population per household in that
        county is then printed to console
        :param search_item: this is the county to search for
        :param county_dict: this is the dictionary of counties to be searched"""
        if search_item in county_dict:
            pop_per_household = float(county_dict[search_item].population.replace(",", "")) \
                                / float(county_dict[search_item].num_households.replace(",", ""))
            print(f'Population per household in {search_item} is {pop_per_household:.2f}')
        else:
            print("No such county exists")


    def get_total_population(county_dict={'key':CountyCensus}):
        """This takes a dictionary of counties, totals the population in each county
        then returns the total result to console
        :param county_dict: this is the dictionary of counties"""
        total_pop = 0
        for co in county_dict:
            total_pop += int(county_dict[co].population.replace(",", ""))
        print(f'Total Population in Iowa: {total_pop}')


if __name__ == '__main__':
    print(county)
    population_per_household('Dallas', county)
    get_total_population(county)
