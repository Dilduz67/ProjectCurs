import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formated_data

def test_get_data():
    data=get_data()
    assert isinstance(data,list)

def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data[:3],False))==2
    assert len(get_filtered_data(test_data[:3], True)) == 2

def test_get_last_values(test_data):
    assert len(get_last_values(test_data,2))==2

def test_get_formated_data(test_data):
    data=get_formated_data(test_data[:1])
    print(data)
    assert data[0]=="\n        26.08.2019 Перевод организации\n        Maestro 1596 83** **** 5199 -> Счет **9589\n        31957.58 руб.\n        "