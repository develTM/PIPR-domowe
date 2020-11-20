import pytest
from zad1 import max_subarray
from zad2 import encrypt_vigenere, decrypt_vigenere
from zad3 import laborki

#zad 1 kadane
def test_empty():
    assert max_subarray([]) == None

def test_negative():
    assert max_subarray([-1,0, -1, 0]) == None

def test_single():
    assert max_subarray([0, 0, -2, 4, -4, -5, 0, 0, 0]) == [4]

def test_corrupt_data():
    with pytest.raises(Exception):
        max_subarray([-1,'a',5])

def test_proper():
    assert max_subarray([3,3,3,3,0]) == [3,3,3,3]

def test_proper_with_leaps():
    assert max_subarray([3,-2,5,-1,0,4,-8,7,0]) == [3, -2, 5, -1, 0, 4]

from main import *

#zad 2 vigenere cypher
def test_encryption():
    assert encrypt_vigenere('NT OJES TBARDZ OTAJN YTEKS', 'TO JEST BARDZO TAJNY TEKST') == 'GH XNWL UBRUCN HTJWL RXOCL'

def test_decryption():
    assert decrypt_vigenere('NT OJES TBARDZ OTAJN YTEKS', 'GH XNWL UBRUCN HTJWL RXOCL') == 'TO JEST BARDZO TAJNY TEKST'

#zad 3
def test_laborki_A():
    assert laborki([10, 20, 30],[("Adam Abacki", [5, 10, 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", [1, 2, 3])]) == ([('Adam Abacki', 30, 50.0), ('Basia Babacka', 60, 100.0), ('Cecylia Cabacka', 6, 10.0)], 53.3)

def test_laborki_corrupt():
    assert laborki([10, 20, 30],[("Adam Abacki", [5, '1o', 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", 55)]) == ([("Adam Abacki", None, None), ("Basia Babacka", 60, 100), ("Cecylia Cabacka", None, None)], 100)


# wynik
