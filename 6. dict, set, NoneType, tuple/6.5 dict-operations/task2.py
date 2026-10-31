address = {
    "zip_code": "789012",
    "longitude": 50.1234,
    "street_name": "Broadway"
}

check = ("zip_code", "longitude", "post_code", "street_name", "number_house")
print(*(key in address for key in check), sep="\n")