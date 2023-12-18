import csv

# Sua lista de casos
cases = [
    # Asus
    ([1500, "Casual", "Asus"], "ASUS ExpertBook B1 B1502CBA-EJ0436X"),
    ([2000, "Casual", "Asus"], "ASUS VivoBook 15 F515JA-EJ2882W"),
    ([2500, "Casual", "Asus"], "ASUS VivoBook 15 F515JA-EJ4134"),
    ([3000, "Casual", "Asus"], "ASUS ZenBook 13 OLED UX325EA-KG448W"),
    ([3500, "Work", "Asus"], "ASUS TUF Gaming A15 2023 FA507XI-LP024"),
    ([4000, "Work", "Asus"], "ASUS Chromebook CX1400FKA-EC0078"),
    ([4500, "Work", "Asus"], "ASUS ExpertBook P1512CEA-EJ0083X"),
    ([5000, "Work", "Asus"], "ASUS ZenBook 14 OLED UM3402YA-KM513"),
    ([5500, "Gamer", "Asus"], "ASUS ROG Strix G15 G513RM-HQ012"),
    ([6000, "Gamer", "Asus"], "ASUS ZenBook 14 OLED UM3402YA-KM512WS"),
    ([6500, "Gamer", "Asus"], "ASUS VivoBook Flip TP470EA-EC402W"),
    ([7000, "Gamer", "Asus"], "ASUS ROG Zephyrus G16 2023 GU603VI-N4006"),
    # Lenovo
    ([1500, "Casual", "Lenovo"], "Lenovo IdeaPad 3 15ALC6"),
    ([2000, "Casual", "Lenovo"], "Lenovo IdeaPad 1 15ALC7"),
    ([2500, "Casual", "Lenovo"], "Lenovo ThinkBook 14"),
    ([3000, "Casual", "Lenovo"], "Lenovo V15 G2 ITL"),
    ([3500, "Work", "Lenovo"], "Lenovo IdeaPad 5 15ALC05"),
    ([4000, "Work", "Lenovo"], "Lenovo Ideapad Duet 5 Chromebook Qualcomm Snapdragon"),
    # HP
    ([1500, "Casual", "HP"], "HP 15S-FQ2163NS"),
    ([8000, "Gamer", "HP"], "HP Omen 16-b1022ns"),
    ([2500, "Work", "HP"], "HP Pavilion 15-eh1004ns"),
    ([3500, "Work", "HP"], "HP 15S-fq5101ns"),
    ([3000, "Casual", "HP"], "HP 15S-fq2158ns"),
]

# Caminho do arquivo CSV a ser criado
file_path = 'cases.csv'

# Escrevendo os casos no arquivo CSV
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Price', 'Category', 'Brand', 'Model'])  # Cabeçalho do CSV

    for case in cases:
        data, model = case
        price, category, brand = data
        writer.writerow([price, category, brand, model])

print(f'O arquivo CSV "{file_path}" foi criado com sucesso.')