# -- TODO: Part 2, write an API client so we are able to query
def get_rate(client_id):
    """
    would expect to return a float rate.

    :param client_id: string, e.g. 'client1'
    :return: float, e.g. 0.2
    """
    # Sample code for getting http response. Need to edit
    import requests
    response = requests.get("http://127.0.0.1:5000/rate/" + client_id)
    print(response)
    # Sample end
# -- TODO END: Part 2


# -- TODO: Part 5, write an API client so we are able to upsert client-rate

# -- TODO END: Part 5


# -----------------------Here are tests for API ------------------------
# -------If you want we can any other file call the API functions-------
# -- TODO: Part 3, Test Your API for get rate
# Please add enough testings. Sample:
def test_get_rate():
    print(get_rate('client1'))
    assert get_rate('client1') == 0.2
# -- TODO END: Part 3


# -- TODO: Part 6, Test Your API for upsert client-rate

# -- TODO END: Part 6

# DO NOT DELETE
if __name__ == '__main__':
    test_get_rate()
    # you can add your test functions here
