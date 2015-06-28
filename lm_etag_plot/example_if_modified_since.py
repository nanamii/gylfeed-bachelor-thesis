from gi.repository import Soup

session = Soup.Session()
message = Soup.Message.new("GET", "http://rss.golem.de/rss.php?feed=ATOM1.0")
message.request_headers.append("if-modified-since", "Mon, 15 Jun 2015 19:37:27 GMT")
session.send_message(message)
date = message.response_headers.get("last-modified")
print(message.status_code, date)

message = Soup.Message.new("GET", "http://rss.golem.de/rss.php?feed=ATOM1.0")
message.request_headers.append("if-modified-since", date)
session.send_message(message)
date = message.response_headers.get("last-modified")
print(message.status_code, date)
