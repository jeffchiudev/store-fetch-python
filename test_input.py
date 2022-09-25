import user_input
test_dictionary = {}

def test_user_input_case():
    test_input = "one two"
    assert user_input.UserInputToList(test_input) == ['one', 'two']

def test_put_case():
    put_test_list = ['put', 'one', 'two']
    assert user_input.PutFetchLogic(put_test_list, test_dictionary) == {'one': 'two'}

def test_fetch_case():
    test_fetch_dictionary = {'one': 'two'}
    fetch_test_list = ['fetch', 'one', 'two']
    assert user_input.PutFetchLogic(fetch_test_list, test_dictionary) == "two"