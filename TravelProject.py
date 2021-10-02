def travel(money):
    food = {"Rice": 50, "Noodle": 35, "Pizza": 300, "Semi-noodle": 10, "Macdonald": 150, "KFC": 200, "Salmon": 500}
    distant = {"Bangkok": 10, "Nonthaburi": 0, "Nakon Patom": 50, "Pathum Tani": 35, "Ayutthaya": 80,
                "Nakhon Nayok": 124, "Chonburi": 100}
    hotel = {"Hotel1": 500, "Hotel2": 700, "Hotel3": 1200, "Hotel4": 2000, "Hotel5": 3000, "Hotel6": 5000,
             "Pool villa": 15000}
    for key, value in food.items():
        if value <= money:
            print(key)


money = 100
travel(money)