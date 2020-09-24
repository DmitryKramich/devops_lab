import requests


def get_pulls(state):
    data = get_git_json()
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
    request = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls?per_page=100", auth=(uname, upass))
    data = request.json()
    return data


def get_data_state(data, key):
    array = []
    for item in data:
        if item["state"] == key:
            array.append({"title": item["title"], "num": item["number"], "link": item["html_url"]})
    return array


def get_data_labels(data, key):
    array = []
    for item in data:
        if not "labels" in item or len(item["labels"]) == 0:
            continue
        else:
            if item["labels"][0]["name"] == key:
                array.append({"title": item["title"], "num": item["number"], "link": item["html_url"]})
    return array
