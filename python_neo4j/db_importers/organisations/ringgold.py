from collections import defaultdict
from typing import Callable, Dict, List

import fire

from python_neo4j.models.organisations import Organisation
from python_neo4j.utils.csv_processor import csv_dict_generator
from python_neo4j.utils.logger import get_logger

LOGGER = get_logger(__name__)
CSV_RINGGOLD_ID = 'ringgold_id'


class RinggoldImporter:
    @classmethod
    def insert_institutions(cls,
                            institutions_csv: str) -> None:
        for i, record in enumerate(list(csv_dict_generator(institutions_csv))):
            if not i % 10000:
                LOGGER.info(f'Working on item {i}')

            cls._insert_institution(record)

    @classmethod
    def _insert_institution(cls, record: Dict) -> None:
        identifier = str(record[CSV_RINGGOLD_ID])
        parent_identifier = (
            str(record['parent_ringgold_id'])
            if record['parent_ringgold_id'] and record[
                'parent_ringgold_id'] > 999
            else None)

        org = Organisation.nodes.get_or_none(identifier=identifier)
        if not org:
            org = Organisation(identifier=identifier)
            org.save()

        org.name = record['name']
        org.save()

        if parent_identifier:
            parent = Organisation.nodes.get_or_none(
                identifier=parent_identifier)
            if not parent:
                parent = Organisation(identifier=parent_identifier)
                parent.save()

            org.parent.connect(parent)

    @classmethod
    def dict_from_csv(cls,
                      dict_to_object: Callable,
                      csv_file: str,
                      csv_id: str = CSV_RINGGOLD_ID) -> Dict[str, List[str]]:
        csv_to_dict = defaultdict(list)

        for record in csv_dict_generator(csv_file):
            record_value = dict_to_object(record)
            if record_value:
                csv_to_dict[str(record[csv_id])].append(record_value)

        return csv_to_dict


if __name__ == '__main__':
    fire.Fire()
