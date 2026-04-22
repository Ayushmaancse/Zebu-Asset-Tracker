import unittest
import json
from app import app

class TrackerTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        import app as app_module
        app_module.items = []
        app_module.next_item_id = 1

    def test_flow(self):
        res = self.client.post('/api/assets', data=json.dumps({"name": "Item"}), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/api/assets')
        self.assertEqual(res.status_code, 200)
        res = self.client.put('/api/assets/1', data=json.dumps({"name": "New"}), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        res = self.client.delete('/api/assets/1')
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
