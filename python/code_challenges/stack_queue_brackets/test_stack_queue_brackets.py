import pytest
from stack_queue_brackets import validate_brackets

def test_brackets_match():
    str="{SARA}[]"
    validate_brackets(str)
    actual=True
    excepted=True
    assert actual==excepted

def test_brackets_unmatch():
    str="{SARA}[)"
    validate_brackets(str)
    actual=False
    excepted=False
    assert actual==excepted

def test_one_bracket():
    str="("
    validate_brackets(str)
    actual=False
    excepted=False
    assert actual==excepted

def test_empty():
    str=""
    validate_brackets(str)
    actual=True
    excepted=True
    assert actual==excepted


def test_no_brackets():
    str="SARA"
    validate_brackets(str)
    actual=True
    excepted=True
    assert actual==excepted
