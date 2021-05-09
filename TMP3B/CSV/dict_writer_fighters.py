from csv import DictReader, DictWriter

def cm_to_in(cm):
    return round(float(cm) * 0.383701,2)

with open('fighters.csv') as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open ('inches_fighters.csv', "w") as file:
    headers = ["Name", "Country", "Height (in inches)"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for fighter in fighters:
        csv_writer.writerow({
            "Name": fighter["Name"],
            "Country": fighter["Country"],
            "Height (in inches)": cm_to_in(fighter["Height (in cm)"])
        })
