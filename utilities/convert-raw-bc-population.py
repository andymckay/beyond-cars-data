import csv

filename = "../canada/statscan/raw-bc-population-data-2021.csv"
output = "../canada/statscan/bc-population-data-2021.csv"
with open(filename) as f:
    with open(output, "w", encoding="utf-8") as o:
        reader = csv.reader(f)
        
        fieldnames = ["age", "total", "male", "female"]
        writer = csv.DictWriter(o, fieldnames=fieldnames)
        writer.writeheader()

        wanted_rows = range(15, 138)
        excluded_rows = [20, 26, 32, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 94, 100, 106, 112, 118, 119, 125, 131]
        for row_number, row in enumerate(reader):
            row_number += 1
            if row:
                if row_number in wanted_rows and row_number not in excluded_rows:
                    total = [0, 0, 0]
                    pointer = 0
                    for col_number, col in enumerate(row):
                        if col_number > 3:
                            total[pointer] += int(col.replace(',', ''))
                            pointer += 1
                            if pointer == len(total):
                                pointer = 0
                        
                        print(col_number, col, pointer, total)
                    
                    writer.writerow({
                        "age": row[0],
                        "total": total[0],
                        "male": total[1],
                        "female": total[2],
                    })
