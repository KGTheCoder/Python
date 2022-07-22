# Dictionaries 
"""
d = {
    <key>: <value>,
    <key>: <value>,
    .
    .
    .
    <key>: <value>
}
"""

Basketball_teams = {
    'San Francisco' : 'Golden State Warriors',
    'Los Angeles' : 'Lakers',
    'Atlanta' : 'Hawks',
    'Boston' : 'Celtics',
    'Cleveland' : 'Cavaliers'
}

Baseball_teams = dict([
    ('New york', 'Yankees'),
    ('Atlanta', 'Braves'),
    ('Queens', 'New York Mets'),
    ('Boston', 'Red Socks'),
    ('San Francisco', 'Giants')
])

Football_teams = dict(
    Philadelphia = 'Eagles',
    NewEngland = 'Patriots',
    KansasCity = "Chiefs",
    Seattle = 'Seahawks',
    Carolina = 'Panthers'
)

# print(type(Baseball_teams))
# print(Basketball_teams)
# print(Football_teams['Philadelphia'])
# print(Baseball_teams['Atlanta'])
# print(Baseball_teams["Florida"])

Baseball_teams['Los Angeles'] = 'Dodgers'

# print(Baseball_teams)

Football_teams['Philadelphia'] = 'Foxes'

# print(Football_teams)
