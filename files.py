import csv

# while True:
#     name = input("what is your name? ").strip().title()
#     village = input("Where are you from? ").title()
#     with open('names.csv', 'a') as file:
#         file.write(f"{name}, {village}\n")
#     prompt = input("Do you want to add another name?(y/n): ")
#     if not prompt == 'y':
#         break

## Reading from a file
info = []

with open("names.csv") as file:
    reader = csv.DictReader(file, fieldnames=["name", "village"])
    for row in reader:
        info.append(row)
print(info)
# I want to add a line