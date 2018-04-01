import unittest
import crawler
import random
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

        saveToRedis('a', 'b')
        self.assertEqual(crawler.r.get('a'), 'b')
        saveToRedis('a', 'c')
        self.assertEqual(crawler.r.get('a'), 'c')
        saveToRedis('d', 'b')
        self.assertEqual(crawler.r.get('d'), 'b')


if __name__ == '__main__':
    unittest.main()
