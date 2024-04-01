food = {
    "food_one" :{"name":"jollof_rice","price":"200"},
    "food_two": {"name":"fried_rice","price":"300"},
    "food_three": {"name":"jollof_spaghetti","price":"250"},
    "food_four": {"name":"whiterice and stew","price":"150"}
}
protein = {
    "protein_one" :{"name":"meat","price":"150"},
    "protein_two": {"name":"eggs","price":"100"},
    "protein_three": {"name":"chicken","price":"300"},
    "protein_four": {"name":"fish","price":"350"}
}
drinks = {
    "drinks_one" :{"name":"pepsi","price":"350"},
    "drinks_two": {"name":"coca-cola","price":"200"},
    "drinks_three": {"name":"fanta","price":"300"},
    "drinks_four": {"name":"sosa","price":"350"}
}
bill_protein = {}
bill_drinks={}
bill_food = {}

def Food():
  print("name    |    price")
  count = 1
  while count < 4:
    for x in food.values():
      print(count,x.get("name"),x.get("price"),"per portion")
      count+= 1
    choice= int(input("select the number of your choice\n:"))
    if choice == 1:
      portions = int(input("how many portions:"))
      num = 200 * portions
      bill_food.update({"Food":{"item":"jollof_rice", "price": num}})
    elif choice == 2:
      portions = int(input("how many portions:"))
      num = 300 * portions
      bill_food.update({"Food":{"item":"fried_rice", "price": num}})
    elif choice == 3:
      portions = int(input("how many portions:"))
      num = 250 * portions
      bill_food.update({"Food":{"item":"jollof_spaghetti", "price": num}})
    elif choice == 4:
      portions = int(input("how many portions:"))
      num = 150 * portions
      bill_food.update({"Food":{"item":"whiterice and stew", "price": num}})
    else:
      print("INVALID!!!")   
    #   ////////////////////////////////////////////
def Drink():
  print("name    |    price")
  count = 1
  while count < 4:
    for x in drinks.values():
      print(count,x.get("name"),x.get("price"))
      count+= 1
    choice= int(input("select the number of your choice\n:"))
    if choice == 1:
      bill_drinks.update({"drink":{"item":"pepsi", "price": 350}})
    elif choice == 2:
      bill_drinks.update({"drink":{"item":"coca-cola", "price": 200}})
    elif choice == 3:
      bill_drinks.update({"drink":{"item":"fanta", "price": 300}})
    elif choice == 4:
      bill_drinks.update({"drink":{"item":"sosa", "price": 350}})
    else:
      print("INVALID!!!")   
    #   ////////////////////////////////////////
def Protein():
  print("name    |    price")
  count = 1
  while count < 4:
    for x in protein.values():
      print(count,x.get("name"),x.get("price"))
      count+= 1
    choice= int(input("select the number of your choice\n:"))
    if choice == 1:
      qty = int(input("how many do you want: "))
      num_one = qty * 150
      bill_protein.update({"protein":{"item":"meat", "price": num_one}})
    elif choice == 2:
     qty = int(input("how many do you want: "))
     num_one = qty * 200
     bill_protein.update({"protein":{"item":"eggs", "price": num_one}})
    elif choice == 3:
     qty = int(input("how many do you want: "))
     num_one = qty * 300
     bill_protein.update({"protein":{"item":"chicken", "price": num_one}})
    elif choice == 4:
     qty = int(input("how many do you want: "))
     num_one = qty * 350
     bill_protein.update({"protein":{"item":"fish", "price": num_one}})
    else:
      print("INVALID!!!")   


while True:
  print("******WELCOME TO OUR CANTEEN*******")    
  print("------------------------------------------\n")
  print("What would you like to buy?")
  menu = int(input("1.food\n2.protein\n3.drinks\n:"))
  if menu == 1:
        Food()
        decision = input("would you like anything else Y/N: ")
        if decision == "y".lower():
            print("What would you like to buy?")
            menu = int(input("1.protein\n2.drinks\n:"))
            if menu == 1:
                Protein()
                decision = input("would you like anything else: Y/N")
                if decision == "y".lower():
                    Drink()
                    bill_food.update(bill_protein)
                    bill_food.update(bill_drinks)
                    print("Thank you for patronizing us!, your bill is:")
                    print("item    |     amount")
                    print("------------------------")
                    result = 0
                    for z in bill_food.values():
                            total = z.get("price")
                            print(z.get("item"),":", total) 
                            result+=total
                    print("------------------------")  
                    print("Total: ", result)
                    break            
                elif decision == "n".lower():
                    bill_food.update(bill_protein)
                    print("Thank you for patronizing us!, your bill is:")
                    print("item    |     amount")
                    print("------------------------")
                    result = 0
                    for z in bill_food.values():
                            total = z.get("price")
                            print(z.get("item"),":", total) 
                            result+=total
                    print("------------------------")  
                    print("Total: ", result)
                    break                   
            elif menu == 2:
                    Drink()
                    bill_food.update(bill_drinks)
                    print("Thank you for patronizing us!, your bill is:")
                    print("item    |     amount")
                    print("------------------------")
                    result = 0
                    for z in bill_food.values():
                        total = z.get("price")
                        print(z.get("item"),":", total) 
                        result+=total
                    print("------------------------")  
                    print("Total: ", result)
                    break            
            else:
                print("INVALID!")     
        elif decision == "n".lower():
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill_food.values():
                    total = z.get("price")
                    print(z.get("item"),":", total) 
                    result+=total
            print("------------------------")  
            print("Total: ", result)
            break            
        else:
         print("INVALID!!")  
  elif menu == 2:
        print("you can't buy any protein without food")
  elif menu == 3:
        Drink()      
        print("Thank you for patronizing us!, your bill is:")
        print("item    |     amount")
        print("------------------------")
        result = 0
        for z in bill_food.values():
            total = z.get("price")
            print(z.get("item"),":", total) 
            result+=total
        print("------------------------")  
        print("Total: ", result)
        break            
  else: 
        print("INVALID!!") 
        
      
      
   
