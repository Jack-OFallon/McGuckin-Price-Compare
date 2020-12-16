import requests

# url_target = 'https://www.target.com/s?searchTerm=854448003877'
# url_homeDepot = 'https://www.homedepot.com'
url_amazon = 'https://www.amazon.com/s?k=719280503582&ref=nb_sb_noss'

# response_target = requests.get(url_target)
# response_homeDepot = requests.get(url_homeDepot)
response_amazon = requests.get(url_amazon)


# print(response_target)
# print(response_homeDepot)
print(response_amazon)#Take an average