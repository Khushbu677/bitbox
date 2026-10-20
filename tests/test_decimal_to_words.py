from tools.decimal_to_words import run


def test_no_argument_given():
    assert run() == "Error: Provide exactly one argument."

def test_positive_number_ones_place():
    assert run(1) == "one"

def test_positive_number_tens_place():
    assert run(12) == "twelve"

def test_positive_number_hundreds_place():
    assert run(123) == "one hundred twenty-three"

def test_positive_number_thousands_place():
    assert run(1234) == "one thousand two hundred thirty-four"

def test_positive_number_million():
    assert run(1200000) == "one million two hundred thousand"

def test_negative_number():
    assert run(-6708) == "negative six thousand seven hundred eight"

def test_non_integer():
    assert run(23.4) == "twenty-three"

def test_string_argument():
    assert run("1234") == "one thousand two hundred thirty-four"

def test_string_argument_negative():
    assert run("-6708") == "negative six thousand seven hundred eight"

def test_number_too_large():
    assert run(10**15) == "Error: number too large"

def test_negative_number_too_large():
    assert run(-(10**15)) == "Error: number too large"

def test_number_too_large_as_string():
    assert run("1000000000000000") == "Error: number too large"

def test_largest_supported_value():
    assert run("999999999999999") == (
        "nine hundred ninety-nine trillion nine hundred ninety-nine billion "
        "nine hundred ninety-nine million nine hundred ninety-nine thousand "
        "nine hundred ninety-nine"
    )



