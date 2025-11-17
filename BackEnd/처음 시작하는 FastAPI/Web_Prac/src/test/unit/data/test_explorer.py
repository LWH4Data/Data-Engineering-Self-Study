# 2. test/unit/data/test_explorer.py
import os
import pytest
from model.explorer import Explorer
from error import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory"
from src.data import creature

@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="yeti", country="CN", area="Himalayas",
        description="Harmless Himalayan",
        aka="Abominable Snowman")

def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_one(sample):
    resp = explorer.get_one(smaple.name)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("boxturtle")

def test_modify(sample):
    explorer.area = "Sesame Street"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    thing: Explorer = Explorer(name="snurfle", country="RU", area="",
        description="some thing", aka="")
    with pytest.raises(Missing):
        _ = explorer.modify(thing.name, thing)

def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorere.delete(sample.name)