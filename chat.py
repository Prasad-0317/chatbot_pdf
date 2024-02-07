from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID": "g.a000fwjT2tDIKSWYIHG3P7STZA9KmBE8aq8HUaR_3gr5jPIettMu3COVdOUdLsw4xUVaMr99QAACgYKATQSAQASFQHGX2MivAyrXF66QA9rSqRa9z3q5xoVAUF8yKosNTnBRzBQTYP30fxKnh3Q0076",
    "__Secure-1PSIDTS" : "sidts-CjIBPVxjSrvvqTCLIVzqEYDbM19bgVfbOdzvi26xG9tbiT0mfFad2fQNSIWwjbE4ZJ45ahAA",
    "__Secure-1PSIDCC" : "ABTWhQEE9HuQMMaDLooKXkBHLDDIYLWNApXgu7Lqh8KPelEZMN-DfXFIFlNBtFj5RT-XhipPvCjG"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input("Enter your query:")
    Reply = bard.get_answer(Query)['content']
    print(Reply)