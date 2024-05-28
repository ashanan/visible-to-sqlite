import csv
import pathlib
import pytest
from io import StringIO
from sqlite_utils import Database
from visible_to_sqlite import utils


@pytest.fixture
def db():
    return Database(memory=True)

@pytest.fixture
def csv_path():
    return pathlib.Path(__file__).parent / "export.csv"

@pytest.fixture
def single_row_export_csv():
    header = 'observation_date,tracker_name,tracker_category,observation_value \n'
    row = '2024-05-22,Sleep,Sleep,2 '
    return StringIO(header + row)

def test_tables_created(csv_path, db):
    with open(csv_path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        utils.convert_csv_to_sqlite(csvreader, db)

    assert db.table_names() == ['TrackerCategories', 'Trackers', 'Observations']

def test_upsert_creates_new_rows_when_no_match_exists(single_row_export_csv, db):
    csvreader = csv.DictReader(single_row_export_csv)
    utils.convert_csv_to_sqlite(csvreader, db)

    assert db.table("Observations").count == 1
