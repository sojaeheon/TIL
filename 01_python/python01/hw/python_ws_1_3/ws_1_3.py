users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

def filter_age():
    adult = []
    for user in users:
        if user["age"]>=18:
            adult.append(user)
    print(f'Adults: {adult}')


def filter_active():
    active_users = []
    for user in users:
        if user["is_active"]==True:
            active_users.append(user)
    print(f'Active Users : {active_users}')

def filter_age_active():
    adult_ac = []
    for user in users:
        if user["is_active"]==True and user["age"]>=18:
            adult_ac.append(user)
    print(f'Adult Active Users: {adult_ac}')
