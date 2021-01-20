import csv

header = ["num1", "operator", "num2", "finalnum"]
tempList = []
temp = {}

def writeToCsv(things):
    with open("test.csv", "w") as file:
        csvW = csv.DictWriter(file, fieldnames=header)
        csvW.writeheader()
        csvW.writerows(things)

def main():
    with open("test.csv", "r") as csvFile:
        csvR = csv.DictReader(csvFile)

        for line in csvR:
            temp = {}
            problem = f"{line['num1']}{line['operator']}{line['num2']}"
            # print(problem)
            finalnum = eval(problem)
            temp['num1'], temp['operator'], temp['num2'], temp['finalnum'] = line['num1'], line['operator'], line['num2'], finalnum

            tempList.append(temp)

    writeToCsv(tempList)
main()