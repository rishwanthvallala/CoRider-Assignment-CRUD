import unittest
from bson import ObjectId
from app import create_app, db
from app.models.user import User

class UserResourceTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['MONGODB_SETTINGS'] = {
            'host': 'mongodb://mongodb:27017/test_db'
        }
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.connection.drop_database('test_db')

    def tearDown(self):
        db.connection.drop_database('test_db')
        self.ctx.pop()

    def test_get_users_empty(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_user(self):
        user_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        }
        response = self.client.post('/users', json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], user_data['name'])
        self.assertEqual(response.json['email'], user_data['email'])
        self.assertNotIn('password', response.json)

    def test_get_user(self):
        user = User(name='Jane Doe', email='jane@example.com', password='password123').save()
        response = self.client.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], user.name)
        self.assertEqual(response.json['email'], user.email)

    def test_update_user(self):
        user = User(name='Bob Smith', email='bob@example.com', password='password123').save()
        update_data = {
            'name': 'Robert Smith',
            'email': 'robert@example.com'
        }
        response = self.client.put(f'/users/{user.id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], update_data['name'])
        self.assertEqual(response.json['email'], update_data['email'])

    def test_delete_user(self):
        user = User(name='Alice Johnson', email='alice@example.com', password='password123').save()
        response = self.client.delete(f'/users/{user.id}')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(User.objects(id=user.id).first())

    def test_create_user_invalid_data(self):
        invalid_user_data = {
            'name': '',  # Invalid: empty name
            'email': 'invalid-email',  # Invalid: not a proper email
            'password': 'short'  # Invalid: too short password
        }
        response = self.client.post('/users', json=invalid_user_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.json)

    def test_get_nonexistent_user(self):
        nonexistent_id = str(ObjectId())
        response = self.client.get(f'/users/{nonexistent_id}')
        self.assertEqual(response.status_code, 404)

    def test_update_nonexistent_user(self):
        nonexistent_id = str(ObjectId())
        update_data = {'name': 'New Name'}
        response = self.client.put(f'/users/{nonexistent_id}', json=update_data)
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_user(self):
        nonexistent_id = str(ObjectId())
        response = self.client.delete(f'/users/{nonexistent_id}')
        self.assertEqual(response.status_code, 404)

    def test_invalid_user_id(self):
        response = self.client.get('/users/invalid_id')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid user ID')

if __name__ == '__main__':
    unittest.main()