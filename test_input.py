import user_input
test_dictionary = {}
put_test_list = ['put', 'one', 'two']

def test_user_input_case():
    test_input = "one two"
    assert user_input.UserInputToList(test_input) == ['one', 'two']

def test_put_case():
    assert user_input.PutLogic(put_test_list, test_dictionary) == {'one': 'two'}