from bs4 import BeautifulSoup


def head_left(soup: BeautifulSoup) -> dict:
    data = {}
    head_left_block = soup.find("div", class_="head-left")
    upped_at_block = head_left_block.find("div", class_="subblock upped-at")
    views = head_left_block.find("span", class_="listing-icons views")
    heart = head_left_block.find("span", class_="listing-icons heart")
    comments = head_left_block.find("span", class_="listing-icons comments")

    data["brand_"] = head_left_block.h1.text.replace("Продажа", "").strip()
    if upped_at_block:
        data["upped_at"] = upped_at_block.text.strip()
    if views:
        data["views"] = views.text.strip()
    if heart:
        data["heart"] = heart.text.strip()
    if comments:
        data["comments"] = comments.text.strip()

    return data


def get_price(soup: BeautifulSoup) -> dict:
    sep_main = soup.find("div", class_="sep main")
    usd = sep_main.find("div", class_="price-dollar").text
    kgs = sep_main.find("div", class_="price-som").text
    return {"USD_price": usd, "KGS_price": kgs}


def get_personal(soup: BeautifulSoup) -> dict:
    data = {}

    personal_info = soup.find("div", class_="personal-info details-phone-wrap clr")
    number = personal_info.find("div", class_="number")
    name = personal_info.find("span", class_="i-name")
    activity = personal_info.find("div", class_="i-counter")

    if name:
        data["name"] = name.text.strip()
    if number:
        data["number"] = number.text.strip()
    if activity:
        data["activity"] = activity.text.strip()
    return data


def get_tab_pane(soup: BeautifulSoup) -> dict:
    data = {}
    try:
        tab_pane = soup.find("div", class_="tab-pane fade in active")
        for fild in tab_pane.find_all("div", class_="field-row clr"):
            data[fild.find("div", class_="field-label").text.strip()] = fild.find(
                "div", class_="field-value"
            ).text.strip()
        return data
    except Exception:
        return data


def get_configuration(soup: BeautifulSoup) -> dict:
    configuration = soup.find("div", class_="configuration")
    cat_dict = {}
    try:
        if configuration:
            cat = configuration.find_all("div", class_="name")
            values = configuration.find_all("div", class_="value")
            for k, v in zip(cat, values):
                val = [p.text.strip() for p in v.find_all("p")]
                cat_dict[k.text.strip()] = val
        return cat_dict
    except Exception:
        return cat_dict


def row_aggregate(soup: BeautifulSoup) -> dict:
    data_dict = dict()

    try:
        data_dict.update(head_left(soup))
        data_dict.update(get_price(soup))
        data_dict.update(get_personal(soup))
        data_dict.update(get_tab_pane(soup))
        data_dict.update(get_configuration(soup))
        return data_dict

    except Exception as error:
        return data_dict
