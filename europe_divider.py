import pandas as pd

# Load the dataset
df = pd.read_csv('europe_cities/europe_cities_ru.csv')

# Define the regions
west_europe = [
    'Австрия', 'Бельгия', 'Франция', 'Германия', 'Ирландия', 'Лихтенштейн', 'Люксембург', 'Монако', 'Нидерланды', 'Швейцария', 'Великобритания'
]
east_europe = [
    'Беларусь', 'Болгария', 'Чехия', 'Венгрия', 'Молдова', 'Польша', 'Румыния', 'Россия', 'Словакия', 'Украина'
]
north_europe = [
    'Дания', 'Эстония', 'Финляндия', 'Исландия', 'Латвия', 'Литва', 'Норвегия', 'Швеция'
]
south_europe = [
    'Албания', 'Андорра', 'Босния и Герцеговина', 'Хорватия', 'Греция', 'Италия', 'Косово', 'Мальта', 'Черногория', 'Португалия', 'Сан-Марино', 'Сербия', 'Словения', 'Испания', 'Северная Македония', 'Турция', 'Ватикан', 'Кипр'
]

# Filter the DataFrame for each region
df_west_europe = df[df['Страна'].isin(west_europe)]
df_east_europe = df[df['Страна'].isin(east_europe)]
df_north_europe = df[df['Страна'].isin(north_europe)]
df_south_europe = df[df['Страна'].isin(south_europe)]

# Save each region to a separate CSV file
df_west_europe.to_csv('europe_cities/west_europe.csv', index=False)
df_east_europe.to_csv('europe_cities/east_europe.csv', index=False)
df_north_europe.to_csv('europe_cities/north_europe.csv', index=False)
df_south_europe.to_csv('europe_cities/south_europe.csv', index=False)

print("West Europe:")
print(df_west_europe)
print("\nEast Europe:")
print(df_east_europe)
print("\nNorth Europe:")
print(df_north_europe)
print("\nSouth Europe:")
print(df_south_europe)