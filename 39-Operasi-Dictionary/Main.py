# Operator Dictionary

data_dict = {
    "ucup": "ucup surucup",
    "tong": "otong surotong",
    "dung": "dudung surudung",
}


# panjang Dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")


# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_key : {CHECKKEY}")


# mengakses value (read) dengan get
print(data_dict["ucup"])
print(data_dict.get("ucup"))
print(data_dict.get("kiss", "key tidak ditemukkan"))  # cek key dengan message


# mengupdate data
data_dict["ucup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasep"
print(data_dict)


data_dict.update({"ucup": "ucup surucup"})
print(data_dict)
data_dict.update({"faqih": "faqihza si keren"})  # kalau gak ada di add aja

print(data_dict)


# mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)
