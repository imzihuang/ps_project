#!/usr/bin/python
# -*- coding: utf-8 -*-
from api import *
from base import get_session

def verify_code(session, game_cod=""):
    query = model_query(session, "GameCode", {"store_game_code": [game_cod]})
    if query.count() > 0:
        return 1
    return 0

def add_game_code(game_cod):
    """
    :param userinfo: 字典，key必须和models.User匹配
    :return:
    """
    session = get_session()
    try:
        _ = verify_code(session, game_cod)
        if _ != 0:
            return False
        model_user = convert_model("GameCode", {"store_game_code": game_cod})
        session.add(model_user)
        session.commit()
        return True
    except Exception as ex:
        return False
    finally:
        session.close()