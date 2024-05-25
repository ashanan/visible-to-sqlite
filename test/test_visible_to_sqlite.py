import csv
import pathlib
import pytest
from sqlite_utils import Database
from visible_to_sqlite import utils


@pytest.fixture
def db():
    return Database(memory=True)

@pytest.fixture
def csv_path():
    return pathlib.Path(__file__).parent / "export.csv"

def test_tables_created(csv_path, db):
    with open(csv_path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        utils.convert_csv_to_sqlite(csvreader, db)

    assert db.table_names() == ['TrackerCategories', 'Trackers', 'Observations']
