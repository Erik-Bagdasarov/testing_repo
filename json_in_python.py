import json
from random import randint

str_json = """
{
  "response": {
        "count": 594384, 
        "item": [{
                "user_id": "1",
                "email": "test_1@test.com",
                "name": "test_1",
                "given_name": "Hello_test_1",
                "family_name": "Test_test_1",
                "nickname": "test_1",
                "last_ip": "94.121.163.63",
                "logins_count": 15,
                "created_at": "2016-11-28T14:10:11.338Z",
                "updated_at": "2016-12-02T01:17:29.310Z",
                "last_login": "2016-12-02T01:17:29.310Z",
                "email_verified": true
              },
              {
                "user_id": "2",
                "email": "test_2@test.com",
                "name": "test_2",
                "given_name": "Hello_test_2",
                "family_name": "Test_test_2",
                "nickname": "test_2",
                "last_ip": "94.121.168.53",
                "logins_count": 1,
                "created_at": "2016-11-28T16:00:04.209Z",
                "updated_at": "2016-11-28T16:00:47.203Z",
                "last_login": "2016-11-28T16:00:47.203Z",
                "email_verified": true
              },
              {
                "user_id": "3",
                "email": "aaa@aaa.com",
                "name": "aaa@aaa.com",
                "given_name": "John",
                "family_name": "Dough",
                "nickname": "aaa",
                "last_ip": "94.121.168.53",
                "logins_count": 2,
                "created_at": "2016-11-28T16:12:23.777Z",
                "updated_at": "2016-11-28T16:12:52.353Z",
                "last_login": "2016-11-28T16:12:52.353Z",
                "email_verified": true
              },
              {
                "user_id": "4",
                "email": "a@a.com",
                "name": "a@a.com",
                "given_name": "Jane",
                "family_name": "Dough",
                "nickname": "a",
                "last_ip": "94.121.163.63",
                "logins_count": 3,
                "created_at": "2016-12-01T23:59:16.473Z",
                "updated_at": "2016-12-01T23:59:53.474Z",
                "last_login": "2016-12-01T23:59:53.474Z",
                "email_verified": true
              },
              {
                "user_id": "5",
                "email": "test9999@test.com",
                "given_name": "Dummy",
                "family_name": "User",
                "created_at": "2016-12-09T12:01:23.787Z",
                "updated_at": "2016-12-09T12:01:23.787Z",
                "email_verified": false
              }
              ]
        }
}
"""

data = json.loads(str_json)

# print(type(data))
# print(data['response']['count']['items '])

for items in data['response']['item']:
    # print(items['user_id'], items['given_name'])
    del items['email_verified']
    items['likes'] = randint(500, 550)
    items['dislikes'] = randint(500, 550)
    # print(f"{items['given_name']}: {items['likes']}")

with open('my.json', 'w') as file:
    json.dump(data, file, indent=4)
