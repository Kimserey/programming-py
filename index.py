"""Random python snippets"""

import json

json_data = """
    [{
        "username": "0"
    }, {
        "username": "1"
    }, {
        "username": "2"
    }, {
        "username": "3"
    }]
"""

users = json.loads(json_data)

print(users)
