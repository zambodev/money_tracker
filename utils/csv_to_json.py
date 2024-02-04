import csv
import json


if __name__ == "__main__":
    with open("./utils/foglio.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        
        data_json = {"expenses":[]}
            
        for obj in data[1:]:
            data_json["expenses"].append({"date":obj[0], "amount":obj[1][4:], "type":obj[2][0], "description":obj[2][3:]})

        with open("./utils/data.json", "w") as out:
            json.dump(data_json, out, ensure_ascii=False)
