import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formated_data

def test_get_data():
    data=get_data()
    assert isinstance(data,list)

def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data[:3],False))==3
    assert len(get_filtered_data(test_data[:3], True)) == 2

def test_get_last_values(test_data):
    assert len(test_get_last_values(test_data,2))==2

def test_get_formated_data(test_data):
    data=get_formated_data(test_data[:1])
    assert data[0]=="'date': '2019-08-26T10:50:58.294041', 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'id'...46.296404', 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'id': 873106923, ...}, ...]"