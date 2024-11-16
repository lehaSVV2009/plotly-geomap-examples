# Define the country flags
country_flags = {
    'Албания': '🇦🇱',
    'Андорра': '🇦🇩',
    'Австрия': '🇦🇹',
    'Беларусь': '🇧🇾',
    'Бельгия': '🇧🇪',
    'Босния и Герцеговина': '🇧🇦',
    'Болгария': '🇧🇬',
    'Ватикан': '🇻🇦',
    'Великобритания': '🇬🇧',
    'Венгрия': '🇭🇺',
    'Германия': '🇩🇪',
    'Греция': '🇬🇷',
    'Дания': '🇩🇰',
    'Ирландия': '🇮🇪',
    'Исландия': '🇮🇸',
    'Испания': '🇪🇸',
    'Италия': '🇮🇹',
    'Казахстан': '🇰🇿',
    'Кипр': '🇨🇾',
    'Косово': '🇽🇰',
    'Латвия': '🇱🇻',
    'Лихтенштейн': '🇱🇮',
    'Литва': '🇱🇹',
    'Люксембург': '🇱🇺',
    'Мальта': '🇲🇹',
    'Молдова': '🇲🇩',
    'Монако': '🇲🇨',
    'Нидерланды': '🇳🇱',
    'Северная Македония': '🇲🇰',
    'Норвегия': '🇳🇴',
    'Польша': '🇵🇱',
    'Португалия': '🇵🇹',
    'Румыния': '🇷🇴',
    'Россия': '🇷🇺',
    'Сан-Марино': '🇸🇲',
    'Сербия': '🇷🇸',
    'Словакия': '🇸🇰',
    'Словения': '🇸🇮',
    'Турция': '🇹🇷',
    'Украина': '🇺🇦',
    'Финляндия': '🇫🇮',
    'Франция': '🇫🇷',
    'Хорватия': '🇭🇷',
    'Черногория': '🇲🇪',
    'Чехия': '🇨🇿',
    'Швейцария': '🇨🇭',
    'Швеция': '🇸🇪',
    'Эстония': '🇪🇪',
}

# Add latitude and longitude for each country
city_coords = {
    'Тирана': {'lat': 41.3275, 'lon': 19.8187},
    'Андорра-ла-Велья': {'lat': 42.5078, 'lon': 1.5211},
    'Вена': {'lat': 48.2082, 'lon': 16.3738},
    'Минск': {'lat': 53.9045, 'lon': 27.5615},
    'Брюссель': {'lat': 50.8503, 'lon': 4.3517},
    'Сараево': {'lat': 43.8563, 'lon': 18.4131},
    'София': {'lat': 42.6977, 'lon': 23.3219},
    'Ватикан': {'lat': 41.9029, 'lon': 12.4534},
    'Лондон': {'lat': 51.5074, 'lon': -0.1278},
    'Будапешт': {'lat': 47.4979, 'lon': 19.0402},
    'Берлин': {'lat': 52.5200, 'lon': 13.4050},
    'Афины': {'lat': 37.9838, 'lon': 23.7275},
    'Копенгаген': {'lat': 55.6761, 'lon': 12.5683},
    'Дублин': {'lat': 53.3498, 'lon': -6.2603},
    'Рейкьявик': {'lat': 64.1355, 'lon': -21.8954},
    'Мадрид': {'lat': 40.4168, 'lon': -3.7038},
    'Рим': {'lat': 41.9028, 'lon': 12.4964},
    'Алматы': {'lat': 43.2220, 'lon': 76.8512},
    'Никосия': {'lat': 35.1856, 'lon': 33.3823},
    'Приштина': {'lat': 42.6629, 'lon': 21.1655},
    'Рига': {'lat': 56.9496, 'lon': 24.1052},
    'Вадуц': {'lat': 47.1410, 'lon': 9.5209},
    'Вильнюс': {'lat': 54.6872, 'lon': 25.2797},
    'Люксембург': {'lat': 49.6117, 'lon': 6.1319},
    'Валлетта': {'lat': 35.8997, 'lon': 14.5147},
    'Кишинев': {'lat': 47.0105, 'lon': 28.8638},
    'Монако': {'lat': 43.7384, 'lon': 7.4246},
    'Амстердам': {'lat': 52.3676, 'lon': 4.9041},
    'Скопье': {'lat': 41.9973, 'lon': 21.4280},
    'Осло': {'lat': 59.9139, 'lon': 10.7522},
    'Варшава': {'lat': 52.2297, 'lon': 21.0122},
    'Лиссабон': {'lat': 38.7223, 'lon': -9.1393},
    'Бухарест': {'lat': 44.4268, 'lon': 26.1025},
    'Москва': {'lat': 55.7558, 'lon': 37.6173},
    'Сан-Марино': {'lat': 43.9333, 'lon': 12.4500},
    'Белград': {'lat': 44.7866, 'lon': 20.4489},
    'Братислава': {'lat': 48.1486, 'lon': 17.1077},
    'Любляна': {'lat': 46.0569, 'lon': 14.5058},
    'Стамбул': {'lat': 41.0082, 'lon': 28.9784},
    'Киев': {'lat': 50.4501, 'lon': 30.5234},
    'Хельсинки': {'lat': 60.1695, 'lon': 24.9354},
    'Париж': {'lat': 48.8566, 'lon': 2.3522},
    'Загреб': {'lat': 45.8150, 'lon': 15.9819},
    'Подгорица': {'lat': 42.4410, 'lon': 19.2636},
    'Прага': {'lat': 50.0755, 'lon': 14.4378},
    'Цюрих': {'lat': 47.3769, 'lon': 8.5417},
    'Стокгольм': {'lat': 59.3293, 'lon': 18.0686},
    'Таллин': {'lat': 59.4370, 'lon': 24.7535},
}
