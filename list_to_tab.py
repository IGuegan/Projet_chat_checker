from lib_checker import get_file_content, clean_text

tab = clean_text(get_file_content('insulte.txt'),[], [])
print(tab)
toprint = 'insultes = {\n'
for mot in tab:
    toprint += '"'+mot+'",\n'
toprint += "}"
toprint = toprint.replace(',\n}','\n}')
destination_file = open('insulte.py', "a", encoding="utf-16")
destination_file.write(toprint)
destination_file.close()