import zlib
import json
import base64

d = "KADENQJvo0dwNHklzo9rHql3fC5lJjnogSazn45Vevnag502vCqsVSYbXY06g7P1iaf2XaohwW1bO0YC/0aubEgvBAIFJUHvV7Hj/Yd32n3zM16EMrrJF9XAiqPkdInHQM12dt7LDCHRlRsiCZg8ezvO60IcQOcEWfIfd2EJufg="
token =d .encode()
token = base64.b64decode(token)
print(token)

