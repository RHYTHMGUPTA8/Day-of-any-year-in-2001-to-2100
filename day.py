# 100-Year Calendar Day Finder (2001 - 2100)

# Mapping of years to their code letters (from the chart)
year_codes = {
    2001: 'A', 2002: 'B', 2003: 'C', 2004: 'K', 2005: 'D', 2006: 'C', 2007: 'D', 2008: 'E', 2009: 'F',
    2010: 'G', 2011: 'F', 2012: 'N', 2013: 'B', 2014: 'F', 2015: 'D', 2016: 'I', 2017: 'G', 2018: 'A',
    2019: 'B', 2020: 'K', 2021: 'L', 2022: 'F', 2023: 'G', 2024: 'H', 2025: 'N',
    # You can extend this dictionary till 2100 using the chart
}

# Month table from the chart (letter → month → number)
month_table = {
    'A': [1, 4, 4, 7, 2, 5, 7, 3, 6, 1, 4, 6],
    'B': [5, 5, 1, 6, 4, 7, 2, 4, 7, 5, 1, 3],
    'C': [3, 6, 2, 4, 7, 2, 5, 3, 6, 1, 4, 6],
    'D': [4, 7, 3, 5, 1, 3, 6, 4, 7, 2, 5, 7],
    'E': [5, 1, 4, 6, 2, 4, 7, 5, 1, 3, 6, 1],
    'F': [6, 2, 5, 7, 3, 5, 1, 6, 2, 4, 7, 2],
    'G': [7, 3, 6, 1, 4, 6, 2, 7, 3, 5, 1, 3],
    'H': [1, 4, 5, 1, 3, 6, 1, 4, 7, 2, 5, 7],
    'I': [2, 5, 6, 2, 4, 7, 2, 5, 1, 3, 6, 1],
    'K': [4, 7, 1, 4, 6, 2, 4, 7, 3, 5, 1, 3],
    'L': [5, 1, 2, 5, 7, 3, 5, 1, 4, 6, 2, 4],
    'M': [6, 2, 3, 6, 1, 4, 6, 2, 5, 7, 3, 5],
    'N': [7, 3, 4, 7, 2, 5, 7, 3, 6, 1, 4, 6],
}

# Day lookup (number → weekday)
day_lookup = {
    1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
    5: "Friday", 6: "Saturday", 7: "Sunday"
}


def find_day(year, month, day):
    # Step 1: Find the year code
    if year not in year_codes:
        return "Year not in range 2001–2100 (or not mapped yet)."
    
    year_code = year_codes[year]
    
    # Step 2: Get the month code number
    month_number = month_table[year_code][month - 1]
    
    # Step 3: Add the date to the month number
    index = (day + month_number - 1) % 7 + 1
    
    # Step 4: Lookup weekday
    return day_lookup[index]


# Example usage
year = int(input("Enter year (2001–2100): "))
month = int(input("Enter month (1–12): "))
day = int(input("Enter day (1–31): "))

print("Day of the week:", find_day(year, month, day))
