from neomodel import (ArrayProperty, RelationshipTo, StringProperty,
                      StructuredNode)


class Descriptor(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    identifier = StringProperty(unique_index=True, required=True)

    tree_numbers = ArrayProperty(StringProperty())

    concepts = RelationshipTo('Concept', 'CONCEPT')
    qualifiers = RelationshipTo('Qualifier', 'QUALIFIER')


class Concept(StructuredNode):
    identifier = StringProperty(unique_index=True, required=True)

    related_numbers = ArrayProperty(StringProperty())

    concept_terms = RelationshipTo('ConceptTerm', 'CONCEPT_TERM')


class ConceptTerm(StructuredNode):
    term = StringProperty(unique_index=True, required=True)
    identifier = StringProperty(unique_index=True, required=True)

    thesauruses = ArrayProperty(StringProperty())


class Qualifier(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    identifier = StringProperty(unique_index=True, required=True)

    tree_numbers = ArrayProperty(StringProperty())

    concepts = RelationshipTo('Concept', 'CONCEPT')
