import json


def get_menu() -> dict:
    """
    To retrieve all menu from json
    :return: dict
    """
    try:
        with open('front_end/data/menu.json') as f_obj:
            data = json.load(f_obj)
    except:
        data = {}
    return data


def get_product() -> dict:
    """
    To retrieve all product from API
    :return: dict
    """
    try:
        with open('fake_data/fake_data.json') as f_obj:
            data = json.load(f_obj)
    except:
        data = {}
    return data

def get_stockist() -> dict:
    """
    To retrieve all product from API
    :return: dict
    """
    try:
        with open('fake_data/fake_data.json') as f_obj:
            data = json.load(f_obj)
    except:
        data = {}
    return data


def get_historic() -> dict:
    """
    To retrieve all historic from json
    :return: dict
    """
    try:
        with open('front_end/data/historic.json') as f_obj:
            data = json.load(f_obj)
    except:
        data = {}
    return data


def get_marketing() -> dict:
    """
    To retrieve all marketing from json
    :return: dict
    """
    try:
        with open('front_end/data/marketing.json') as f_obj:
            data = json.load(f_obj)
    except:
        data = {}
    return data


def get_renum() -> dict:
    """
    To retrieve all marketing from json
    :return: dict
    """
    try:
        with open('front_end/data/renumeration.json') as f_obj:
            data = json.load(f_obj)
    except:
        data = {}
    return data

def get_adhesion() -> dict:
    """
    To retrieve all marketing from json
    :return: dict
    """
    try:
        with open('front_end/data/adhesion.json') as f_obj:
            data = json.load(f_obj)
    except:
        data = {}
    return data