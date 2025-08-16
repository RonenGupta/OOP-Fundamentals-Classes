from fast_food import Employee, Cashier, Cook, Cleaner, FryCook

cashier = Cashier("Victor", 9319, 0, 0, 0, 0, 1)
cashier.clock_in()
cashier.process_order(1000)
cashier.get_pay()
cashier.clock_out()

cleaner = Cleaner("Levin", 9320, 0, 0, 0, 0, 1)
cleaner.clock_in()
cleaner.clean_area("kitchen")
cleaner.get_pay()
cleaner.clock_out()

frycook = FryCook("Ronen", 9321, 0, 0, 0, 0, 1, "burger")
frycook.clock_in()
frycook.burger(1000)
frycook.get_pay()
frycook.clock_out()