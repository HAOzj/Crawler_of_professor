# crawler related
url = "https://dms.umontreal.ca/fr/la-recherche/axes-de-recherche/statistique"
prefix = "https://dms.umontreal.ca/fr"
href_pattern = "/repertoire-departement/professeurs/portrait/"
classes = ["name", "email", "title"]
classes_next = {"title": "PhD"}
classes_li = ["interests"]

# elastic search related
index = "u_de_montreal"
doc_type = "prof_profile"