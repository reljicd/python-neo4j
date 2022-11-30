import pytest

from python_neo4j.models.organisations import Organisation


@pytest.fixture()
def setup_organisations() -> None:
    for org in Organisation.nodes.all():
        org.delete()

    child = Organisation(name='child')
    child.save()
    parent = Organisation(name='parent')
    parent.save()

    child.parent.connect(parent)


def test_find(setup_organisations):
    child = Organisation.nodes.get(name='child')

    assert child


def test_parent(setup_organisations):
    child = Organisation.nodes.get(name='child')

    assert child.parent
