import requests
parameters = {
    'amount': 20,
    'category': 18,
    'type': 'boolean'
}
# Disable SSL verification
requests.packages.urllib3.disable_warnings()
response = requests.get('https://opentdb.com/api.php', params=parameters, verify=False)
response.raise_for_status()

data = response.json()
question_data = data['results']

import html
for question in question_data:
    question["question"] = html.unescape(question["question"])

# print(question_data[0])