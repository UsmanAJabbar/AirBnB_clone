#!/usr/bin/python3
"""Y U Do Dis?"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    -------------
    CLASS: REVIEW
    -------------
    """

    # ------------------------------ #
    #       PUBLIC CLASS ATTRS       #
    # ------------------------------ #
    place_id = ""
    user_id = ""
    text = ""
