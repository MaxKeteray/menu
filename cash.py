class CashierSystem:
    def __init__(self):
        self.logged_in = False
        self.orders = []

    def login(self):
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")
        # перевірка пароля
        self.logged_in = True
        print("Успішний вхід!")

    def create_order(self):
        if not self.logged_in:
            print("Спочатку увійдіть в систему.")
            return

        product_name = input("Введіть назву товару: ")
        quantity = int(input("Введіть кількість: "))
        price = float(input("Введіть ціну за одиницю: "))

        total_price = quantity * price
        order = {"product_name": product_name, "quantity": quantity, "price": price, "total_price": total_price}
        self.orders.append(order)

        print(f"Замовлення створено: {quantity} x {product_name} за {total_price} грн")

    def display_orders(self):
        if not self.logged_in:
            print("!!!Спочатку увійдіть в систему.!!!")
            return

        if not self.orders:
            print("Немає замовлень.")
            return

        print("Список замовлень:")
        for order in self.orders:
            print(f"{order['quantity']} x {order['product_name']} за {order['total_price']} грн")

    def logout(self):
        self.logged_in = False
        print("Вихід з системи.")

# Приклад використання
cashier_system = CashierSystem()

while True:
    print("\n1. Логін")
    print("2. Створити замовлення")
    print("3. Показати замовлення")
    print("4. Вийти з системи")
    choice = input("Оберіть опцію: ")

    if choice == "1":
        cashier_system.login()
    elif choice == "2":
        cashier_system.create_order()
    elif choice == "3":
        cashier_system.display_orders()
    elif choice == "4":
        cashier_system.logout()
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
