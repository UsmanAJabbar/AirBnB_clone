#!/usr/bin/python3
"""Hippity Hoppotus, This Docstring Doesn't Rhyme"""
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
