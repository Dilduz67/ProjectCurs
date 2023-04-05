import json
from datetime import datetime
from pprint import pprint

def get_data():
    with open("operations.json","r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def get_filtered_data(data, FILTERED_EMPTY_FROM):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    if FILTERED_EMPTY_FROM:
        data = [x for x in data if 'from in  x']

    return data

def get_last_values(data, COUNT_VALUES):
    data = sorted(data,key=lambda  x: x['date'], reverse=True)
    return data[:COUNT_VALUES]


def get_formated_data(data):
    formated_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row['description']
        if "from" in row:
            sender = row["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
            from_info = ' '.join(sender)
        else:
            from_info, from_bill = "", ""

        recipient = row["to"].split()
        recipient_bill = recipient.pop(-1)

        recipient_bill = f"**{recipient_bill[-4:]}"
        to_info = ' '.join(recipient)
        amount = f"{row['operationAmount']['amount']} {row['operationAmount'] ['currency'] ['name']}"

        formated_data.append(f"""
        {date} {description}
        {from_info} {from_bill} -> {to_info} {recipient_bill}
        {amount}
        """)
    return formated_data



