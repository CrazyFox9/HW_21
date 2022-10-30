from classes import Store, Shop, Request

storage_1 = Store(items={"бананы": 20, "собаки": 10, "люди": 10})
shop = Shop(items={"бананы": 10})


while True:
    user_request = input("Введите команду:\n")

    if user_request == "стоп":
        break
    else:
        req = Request(user_request)
        product = req.move()["product"]
        amount = req.move()["amount"]

        if req.move()["from"] == "магазин":
            if storage_1.add(product, amount):
                if shop.remove(product, amount):
                    print("Нужное количество есть на складе")
                    print(f"Курьер забрал {amount} {product} из магазина")
                    print(f"Курьер везет {amount} {product} из магазина на склад")
                    print(f"Курьер доставил {amount} {product} на склад\n")
                else:
                    storage_1.remove(product, amount)

        if req.move()["from"] == "склад":
            if shop.add(product, amount):
                if storage_1.remove(product, amount):
                    print("Нужное количество есть на складе")
                    print(f"Курьер забрал {amount} {product} со склада")
                    print(f"Курьер везет {amount} {product} со склада в магазин")
                    print(f"Курьер доставил {amount} {product} в магазин\n")
                else:
                    shop.remove(product, amount)

        print("На складе хранится:")
        print(storage_1)
        print("В магазине хранится:")
        print(shop)
