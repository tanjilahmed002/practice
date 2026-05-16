# --- INITIALIZATION (Data Store kora) ---
# inventory: Dictionary jekhane product er nam key hisabe thake ar tar bhitor dam, poriman thake
inventory = {
    "Laptop": {"price": 50000, "quantity": 5, "category": "Electronics"},
    "Mouse": {"price": 500, "quantity": 10, "category": "Electronics"}
}
# categories: Set use kora hoyeche jate ekebare unique category gulo thake
categories = {"Electronics"}

# --- MAIN SYSTEM LOOP (Main Menu start) ---
while True:
    print("\n" + "═"*35)
    print("      INVENTORY & SHOP SYSTEM")
    print("═"*35)
    print("1. Admin Mode (Full Control)")
    print("2. Customer Mode (View/Buy/Bill)")
    print("3. Exit")
    
    # User-er kach theke choice neya
    main_choice = input("\nEnter your choice: ")

    # ---------------------------------------------------------
    # SECTION: ADMIN (Full Control)
    # ---------------------------------------------------------
    if main_choice == "1":
        # Admin login er jonno username ar password neya hochhe
        admin_user = input("Enter Admin Username: ") # Admin username chawa hochhe
        password = input("Enter Admin Password: ")     # Admin password chawa hochhe
        
        # Username 'admin' ebong Password '1234' kina check kora hochhe
        if admin_user == "admin" and password == "1234": 
            print("\n✅ Admin Access Granted!")
            while True:
                print("\n" + "─"*30)
                print("       ADMIN CONTROL PANEL")
                print("─"*30)
                print("1. Add Product\n2. View All\n3. Delete Product\n4. Logout")
                admin_op = input("Select Option: ")

                # Notun product add korar logic
                if admin_op == "1":
                    name = input("Product Name: ").strip().capitalize() # Namer extra space keta prothom okkhor boro kora
                    price = float(input("Price: ")) # Dashomik shonkha neyar jonno float
                    qty = int(input("Quantity: "))  # Purno shonkhar jonno int
                    cat = input("Category: ").strip().capitalize()
                    
                    # Dictionary-te data entry kora hochhe
                    inventory[name] = {"price": price, "quantity": qty, "category": cat}
                    categories.add(cat) # Set-e category add kora hochhe
                    print(f"✔️ {name} added successfully!")

                # Inventory-te thaka shob product table akare dekhano
                elif admin_op == "2":
                    print(f"\n{'Name':<15} | {'Price':<10} | {'Stock':<6}")
                    print("-" * 35)
                    for n, i in inventory.items():
                        print(f"{n:<15} | {i['price']:<10} | {i['quantity']:<6}")

                # Kono product delete korar logic
                elif admin_op == "3":
                    del_name = input("Name to delete: ").strip().capitalize()
                    if del_name in inventory:
                        del inventory[del_name] # Dictionary theke oi product remove kora
                        print("🗑 Product Removed!")
                    else:
                        print("❌ Not found!")

                # Admin panel theke ber hoye main menu-te jawa
                elif admin_op == "4":
                    break
        else:
            print("❌ Invalid Username or Password!") # Vul login details dile eta dekhabe

    # ---------------------------------------------------------
    # SECTION: CUSTOMER (View/Buy/Bill)
    # ---------------------------------------------------------
    elif main_choice == "2":
        cart = []        # Customer-er kena jinish gulo ei list-e thakbe
        total_bill = 0   # Mot koto taka bill holo tar hisab
        
        while True:
            print("\n" + "─"*30)
            print("       CUSTOMER MENU")
            print("─"*30)
            print("1. View Products\n2. Buy Product\n3. View Bill & Checkout\n4. Back")
            cust_op = input("Select Option: ")

            # Customer-er jonno product list dekhano
            if cust_op == "1":
                print(f"\n{'Product':<15} | {'Price':<10} | {'Status'}")
                print("-" * 35)
                for n, i in inventory.items():
                    # Quantity 0 er beshi hole 'In Stock', na hole 'Out of Stock'
                    status = "In Stock" if i['quantity'] > 0 else "Out of Stock"
                    print(f"{n:<15} | {i['price']:<10} | {status}")

            # Product kinar prokriti logic
            elif cust_op == "2":
                buy_name = input("Enter product name to buy: ").strip().capitalize()
                
                # Product-ti inventory-te ache kina check
                if buy_name in inventory:
                    if inventory[buy_name]['quantity'] > 0: # Stock ache kina check
                        qty_to_buy = int(input(f"How many {buy_name} do you want? "))
                        
                        # Joto-tuku kinte chay toto-tuku stock-e ache kina check
                        if qty_to_buy <= inventory[buy_name]['quantity']:
                            # Stock komiye deya hochhe
                            inventory[buy_name]['quantity'] -= qty_to_buy
                            # Bill calculate kora hochhe
                            item_total = inventory[buy_name]['price'] * qty_to_buy
                            # Cart-e item-er details (nam, qty, total) rakha hochhe
                            cart.append({"name": buy_name, "qty": qty_to_buy, "total": item_total})
                            total_bill += item_total # Main bill-er sathe jog kora
                            print(f"🛒 Added {qty_to_buy} {buy_name} to cart.")
                        else:
                            print("❌ Not enough stock!")
                    else:
                        print("❌ Sorry, out of stock!")
                else:
                    print("❌ Product not found.")

            # Bill print kora ebong reset kora
            elif cust_op == "3":
                if not cart:
                    print("\n🛒 Your cart is empty!")
                else:
                    print("\n" + "═"*30)
                    print("         YOUR BILL")
                    print("═"*30)
                    print(f"{'Item':<15} | {'Qty':<5} | {'Total'}")
                    print("-" * 30)
                    for item in cart:
                        # Cart list theke protiti item print kora hochhe
                        print(f"{item['name']:<15} | {item['qty']:<5} | {item['total']}")
                    print("-" * 30)
                    print(f"GRAND TOTAL: {total_bill} BDT")
                    print("═"*30)
                    print("Thank you for shopping!")
                    # Shopping shesh, tai cart ar bill 0 kore deya hochhe
                    cart = [] 
                    total_bill = 0

            # Customer menu theke main menu-te ferot jawa
            elif cust_op == "4":
                break

    # ---------------------------------------------------------
    # SECTION: EXIT SYSTEM (Program bondho kora)
    # ---------------------------------------------------------
    elif main_choice == "3":
        print("\nExiting System... Have a nice day!")
        break # Loop venge program bondho hoye jabe

    else:
        print("\n❌ Invalid choice! Please select 1, 2, or 3.") # Vul menu option dile warning