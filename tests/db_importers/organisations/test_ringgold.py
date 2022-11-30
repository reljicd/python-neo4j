import pandas
import pytest

from python_neo4j.db_importers.organisations.ringgold import RinggoldImporter
from python_neo4j.models.organisations import Organisation

INSTITUTIONS_CSV = 'tests/fixtures/ringgold.csv'
CHILD_ID = '1009'
PARENT_ID = '1006'


@pytest.fixture()
def clean_organisations() -> None:
    for org in Organisation.nodes.all():
        org.delete()


def test_ringgold_importer(clean_organisations):
    RinggoldImporter.insert_institutions(INSTITUTIONS_CSV)

    assert len(Organisation.nodes.all()) == len(
        pandas.read_csv(INSTITUTIONS_CSV))
    assert Organisation.nodes.get(
        identifier=CHILD_ID).parent.single().identifier == PARENT_ID
