from neomodel import RelationshipTo, StringProperty, StructuredNode


class FieldOfStudy(StructuredNode):
    normalized_name = StringProperty(unique_index=True, required=True)
    display_name = StringProperty()

    parent = RelationshipTo('FieldOfStudy', 'PARENT')
