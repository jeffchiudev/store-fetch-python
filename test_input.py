import user_input

def test_user_input_case():
    test_input = "one two"
    assert user_input.UserInputToList(test_input) == ['one', 'two']