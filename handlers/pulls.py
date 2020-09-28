import requests


def get_pulls(state):
    data = get_git_json()
    return get_complited_data(state, data)


def get_complited_data(state, data):
    if state is None:
        return get_all_data(data)
    switcher = {
        "open": get_data_state(data, "open"),
        "closed": get_data_state(data, "closed"),
        "accepted": get_data_labels(data, "accepted"),
        "needs work": get_data_labels(data, "needs work")
    }
    return switcher.get(state)


def get_git_json():
    uname = "DmitryKramich"
    upass = "************"
    url = "https://api.github.com/repos/alenaPy/devops_lab/pulls?per_page=100&state=all"
    request = requests.get(url, auth=(uname, upass))
    data = request.json()
    return data


def get_data_state(data, key):
    array = []
    for item in data:
        if item["state"] == key:
            array.append(get_array_object(item))
    return array


def get_data_labels(data, key):
    array = []
    for item in data:
        if len(item["labels"]) == 0:
            continue
        else:
            if item["labels"][0]["name"] == key:
                array.append(get_array_object(item))
    return array


def get_all_data(data):
    array = []
    for item in data:
        array.append(get_array_object(item))
    return array


def get_array_object(item):
    return {"title": item["title"],
            "num": item["number"],
            "link": item["html_url"]}
