from neomodel import (ArrayProperty, One, RelationshipTo, StringProperty,
                      StructuredNode)


class Organisation(StructuredNode):
    name = StringProperty(index=True)
    identifier = StringProperty(unique_index=True)

    tiers = ArrayProperty(StringProperty())

    parent = RelationshipTo('Organisation', 'PARENT', cardinality=One)
