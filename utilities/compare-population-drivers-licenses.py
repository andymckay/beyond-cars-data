import icbc
import csv

statscan_data = "../canada/statscan/bc-population-data-2021.csv"
icbc_data = "../canada/icbc/age-range-drivers-licenses.csv"
age_ranges = {}

with open(statscan_data) as s:
    pointer = 0
    for line in csv.DictReader(s):
        if line["age"] == 'Under 1 year':
            age = 0
        elif line["age"] == '100 years and over':
            age = 100
        else:
            age = int(line["age"])
        
        group = icbc.age_groupings[pointer]
        key = f'{group[0]}-{group[1]}'
        age_ranges.setdefault(key, 0)
        age_ranges[key] += int(line["total"])
        if age >= group[1]:
            pointer += 1

print(f'Age range|Number of drivers licenses|Population|Percentage without drivers license')
print(f'-|-|-|-|')
print(f'0-15|0|{age_ranges["0-15"]:,}|0%')
with open(icbc_data, encoding="utf-8") as i:
    total_icbc = 0
    total_statscan = age_ranges["0-15"]
    for line in csv.DictReader(i):
        key = line["Age Range"]
        icbc_total = int(line["Number"])
        if key == "86+":
            key = "86-100"
        statscan_total = age_ranges[key]
        percentage_without = round(100 - (icbc_total / statscan_total * 100), 2)
        print(f'{key}|{icbc_total:,}|{statscan_total:,}|{percentage_without}%')
        total_icbc += icbc_total
        total_statscan += statscan_total

    print(f'All|{total_icbc:,}|{total_statscan:,}|{round(100 - (total_icbc / total_statscan * 100), 2)}%')
    