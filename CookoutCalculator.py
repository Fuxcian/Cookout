def main():
    #basic variables
    guests = int(input("How many guests are attending? "))
    hotdogs = 10 #hot dogs per package
    buns = 8 #buns per package
    perperson_hotdogs = int(input("How many hot dogs will each person eat? "))
    print(f"If each person eats {perperson_hotdogs} hot dogs, then you'll need: {guests * perperson_hotdogs} hot dogs and buns.")
    
    #calculating packages needed
    hotdog_packages = guests * perperson_hotdogs // hotdogs #calculates how many packages of hot dogs are needed using floor division for whole packages
    if guests * perperson_hotdogs % hotdogs > 0: #calculates if we need an additional package using modulus to check for leftovers
        hotdog_packages += 1 #add one more package if there are leftover hot dogs 
    print(f"You will need {hotdog_packages} packages of hot dogs. ({hotdog_packages * 10} hot dogs)")

    bun_packages = guests * perperson_hotdogs // buns #calculates how many packages of buns are needed using floor division for whole packages
    if guests * perperson_hotdogs % buns > 0: #calculates if we need an additional package using modulus to check for leftovers
        bun_packages += 1 #add one more package if there are leftover buns 
    print(f"You will need {bun_packages} packages of buns. ({bun_packages * 8} buns)")

    #calculates uneaten leftovers
    print("Given how many hotdogs you needed, and how many you can make with what you bought:")
    leftover_hotdogs = (hotdog_packages * hotdogs) - (guests * perperson_hotdogs) #calculates how many hot dogs are left over
    print(f"You will have {leftover_hotdogs} leftover hot dogs.")
    leftover_buns = (bun_packages * buns) - (guests * perperson_hotdogs) #calculates how many buns are left over
    print(f"You will have {leftover_buns} leftover buns.")

#call the main function
main()