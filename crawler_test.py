import unittest
import crawler
import random
import json
from crawler import requestAllBusStatic, requestAllBikeRealtime, requestAllBusRealTime, saveToRedis


class TestCrawler(unittest.TestCase):
    def test_requestAllBikeRealtime(self):
        results = requestAllBikeRealtime()
        self.assertTrue(isinstance(results, list))
        for i in range(20):
            result = random.choice(results)
            self.assertTrue(isinstance(result, dict))
            self.assertIsNotNone(result.get('name'))
            self.assertIsNotNone(result.get('latitude'))
            self.assertIsNotNone(result.get('longitude'))
            self.assertIsNotNone(result.get('bike_available'))

    def test_requestAllBusStatic(self):
        results = requestAllBusStatic()
        self.assertTrue(isinstance(results, list))
        for i in range(20):
            result = random.choice(results)
            self.assertTrue(isinstance(result, dict))
            self.assertIsNotNone(result.get('ID'))
            self.assertIsNotNone(result.get('name'))
            self.assertIsNotNone(result.get('latitude'))
            self.assertIsNotNone(result.get('longitude'))
            self.assertTrue(isinstance(result.get('routes'), list))

    def test_saveToRedis(self):
        a = ['a','b']
        b = {'a': 2, 'b': 1}
        saveToRedis('a', a)
        self.assertEqual(crawler.r.get('a').decode('utf-8'), json.dumps(a))
        saveToRedis('b', b)
        self.assertEqual(crawler.r.get('b').decode('utf-8'), json.dumps(b))
        saveToRedis('b', a)
        self.assertEqual(crawler.r.get('b').decode('utf-8'), json.dumps(a))


if __name__ == '__main__':
    unittest.main()
