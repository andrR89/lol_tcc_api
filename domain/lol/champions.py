from marshmallow import fields
from marshmallow.decorators import post_load
from marshmallow.schema import Schema


class Skin(object):
    def __init__(self, id, name, num):
        self.id = id
        self.name = name
        self.num = num

    def __repr__(self):
        return '<Skin(name={self.name!r})>'.format(self=self)


class SkinSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    num = fields.Int()

    @post_load
    def make_skin(self, data):
        return Skin(**data)


class Champion(object):
    def __init__(self, id, key, name, title, skins=None):
        self.id = id
        self.key = key
        self.name = name
        self.title = title
        self.skins = skins

    def __repr__(self):
        return '<Champion(name={self.name!r})>'.format(self=self)


class ChampionSchema(Schema):
    id = fields.Int()
    key = fields.Str()
    name = fields.Str()
    title = fields.Str()
    skins = fields.List(fields.Nested(SkinSchema), required=False, missing=None)

    @post_load
    def make_champion(self, data):
        return Champion(**data)


class ChampionListSchema(Schema):
    type = fields.Str()
    version = fields.Str()
    data = fields.Dict(fields.Nested(ChampionSchema))
