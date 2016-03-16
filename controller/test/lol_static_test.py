import unittest

import simplejson

from lol.champions import ChampionSchema
from rest import create_app


class LoLStaticTest(unittest.TestCase):
    def setUp(self):
        app = create_app('config')
        self.app = app.test_client()
        self.app.testing = True
        self.headers = [('Content-Type', 'application/json')]

    def test_show_all_champs(self):
        # WHEN
        response = self.app.get('/lol/static/champions')
        # THEN
        self.assertEqual(response.status_code, 200)
        champions = simplejson.loads(response.data.decode("utf-8"))
        self.assertEqual(len(champions['data']), 129)

    def test_show_one_champ_and_yours_skins(self):
        # WHEN Find SONA
        response = self.app.get('/lol/static/champions/37?champData=skins')
        # THEN
        self.assertEqual(response.status_code, 200)
        champion = ChampionSchema().load(simplejson.loads(response.data.decode("utf-8")), partial=True).data
        self.assertEqual(champion.name, 'Sona')
        self.assertEqual(len(champion.skins), 8)

    def test_show_one_champ_without_skins(self):
        # WHEN Find SONA
        response = self.app.get('/lol/static/champions/37')
        # THEN
        self.assertEqual(response.status_code, 200)
        champion = ChampionSchema().load(simplejson.loads(response.data.decode("utf-8")), partial=True).data
        self.assertEqual(champion.name, 'Sona')
        self.assertIsNone(champion.skins)
