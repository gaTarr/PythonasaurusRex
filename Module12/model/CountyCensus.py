"""CIS189 Python
Author: Greg Tarr
Created: 11/12/2019"""


class CountyCensus:

    def __init__(self, rank, county, per_cap_income, med_house_income, med_fam_income, pop, num_houses):
        self.rank = rank
        self.county = county
        self.per_capita_income = per_cap_income
        self.median_household_income = med_house_income
        self.median_family_income = med_fam_income
        self.population = pop
        self.num_households = num_houses
