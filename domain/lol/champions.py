from marshmallow import fields
from marshmallow.decorators import post_load
from marshmallow.schema import Schema


class Champion(object):
    def __init__(self, id, key, name, title):
        self.id = id
        self.key = key
        self.name = name
        self.title = title

    def __repr__(self):
        return '<Champion(name={self.id!r})>'.format(self=self)


class ChampionSchema(Schema):
    id = fields.Int()
    key = fields.Str()
    name = fields.Str()
    title = fields.Str()

    @post_load
    def make_champion(self, data):
        return Champion(**data)


class ChampionListSchema(Schema):
    type = fields.Str()
    version = fields.Str()
    data = fields.Dict(fields.Nested(ChampionSchema))
