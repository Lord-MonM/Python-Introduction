que = """build a canteen, you will use as dictionaries throughout.. you should have menu dictionaries, one for food, one for protein and one for drinks.... welcome a user or group of users and ask them what they would like to order, keep track of the meals, the prices an the people who have ordered them. finally print to them their bills"""
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
bill = {}
bill_drinks={}
while True:
  print("******WELCOME TO OUR CANTEEN*******")    
  print("------------------------------------------\n")
  print("What would you like to buy?")
  menu = int(input("1.food\n2.protein\n3.drinks\n:"))
  count = 1
  count_two = 1
  count_three = 1


  if menu == 1:

    print("name    |    price")
    while count < 4:
      for x in food.values():
        print(count,x.get("name"),x.get("price"),"per portion")
        count+= 1
    choice= int(input("select the number of your choice\n:"))
    if choice == 1:
      portions = int(input("how many portions:"))
      num = 200 * portions
      bill.update({"Food":{"item":"jollof_rice", "price": num}})
      change = input("would you like to add anything else? Y/N:")
      if change == "Y" or change == "y":
        print("What would you like to buy?")
        menu = int(input("1.protein\n2.drinks\n:"))
        if menu == 1:
          while count_two < 4:
            for y in protein.values():
             print(count_two,y.get("name"),y.get("price"))
             count_two+= 1
        choice= int(input("select the number of your choice\n:"))
        if choice == 1:
          bill.update({"Food":{"item":"jollof_rice","price":num}, "Protein":{"item":"meat","price": 150}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
              for y in drinks.values():
                print(count_three,y.get("name"),y.get("price"))
                count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break            
            elif choice == 2:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"jollof_rice","price":num}, "Protein":{"item":"meat","price": 150}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # MEATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        elif choice == 2:
          bill.update({"Food":{"item":"jollof_rice","price":num}, "Protein":{"item":"egg","price": 100}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"jollof_rice","price":num}, "Protein":{"item":"egg","price": 100}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # chickennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        elif choice == 3:
          bill.update({"Food":{"item":"jollof_rice","price":num}, "Protein":{"item":"chicken","price": 300}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
              for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"jollof_rice","price":num}, "Protein":{"item":"chicken","price": 300}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # fishhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        elif choice == 4:
          bill.update({"Food":{"item":"jollof_rice","price":num}, "Protein":{"item":"fish","price": 350}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
              for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"jollof_rice","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"jollof_rice","price":num}, "Protein":{"item":"fish","price": 350}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
        else:
          print("INVALID!!")
      elif change == "N" or change == "n":
        bill.update({"item":"jollof_rice","price": num})
        print("Thank you for patronizing us!, your bill is:")
        print("item    |     amount")
        print("------------------------")
        result = 0
        for z in bill.values():
          total = z.get("price")
          print(z.get("item"),":", total) 
          result+=total
        print("------------------------")  
        print("Total: ", result)
        break
        # FRIEDDDDDDDDDDDDDDDDDDDDD RICEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    elif choice == 2:
      portions = int(input("how many portions:"))
      num = 300 * portions
      bill.update({"Food":{"item":"fried_rice", "price": num}})
      change = input("would you like to add anything else? Y/N:")
      if change == "Y" or change == "y":
        print("What would you like to buy?")
        count_two = 0   
        menu = int(input("1.protein\n2.drinks\n:"))
        if menu == 1:
         while count_two < 4:
           for y in protein.values():
             print(count_two,y.get("name"),y.get("price"))
             count_two+= 1
        choice= int(input("select the number of your choice\n:"))
        if choice == 1:
          bill.update({"Food":{"item":"fried_rice","price":num}, "Protein":{"item":"meat","price": 150}})
          change = input("would you like to add drinks? Y/N: ")
          count_three == 0
          if change == "Y" or change == "y":
            while count_three < 4:
              for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"fried_rice","price":num}, "Protein":{"item":"meat","price": 150}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # MEATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        elif choice == 2:
          bill.update({"Food":{"item":"fried_rice","price":num}, "Protein":{"item":"egg","price": 100}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"fried_rice","price":num}, "Protein":{"item":"egg","price": 100}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # chickennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        elif choice == 3:
          bill.update({"Food":{"item":"fried_rice","price":num}, "Protein":{"item":"chicken","price": 300}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"fried_rice","price":num}, "Protein":{"item":"chicken","price": 300}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # fishhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        elif choice == 4:
          bill.update({"Food":{"item":"fried_rice","price":num}, "Protein":{"item":"fish","price": 350}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"fried_rice","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"fried_rice","price":num}, "Protein":{"item":"fish","price": 350}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
        else:
          print("INVALID!!")
      elif change == "N" or change == "n":
        print("Thank you for patronizing us!, your bill is:")
        print("item    |     amount")
        print("------------------------")
        result = 0
        for z in bill.values():
          total = z.get("price")
          print(z.get("item"),":", total) 
          result+=total
        print("------------------------")  
        print("Total: ", result)
        break
    # ///////////////////////////////////////////////////////////
    elif choice == 3:
      portions = int(input("how many portions:"))
      num = 250 * portions
      bill.update({"Food":{"item":"jollof_spaghetti", "price": num}})
      change = input("would you like to add anything else? Y/N:")
      if change == "Y" or change == "y":
        print("What would you like to buy?")
        count_two = 0   
        menu = int(input("1.protein\n2.drinks\n:"))
        if menu == 1:
         while count_two < 4:
            for y in protein.values():
             print(count_two,y.get("name"),y.get("price"))
             count_two+= 1
        choice= int(input("select the number of your choice\n:"))
        if choice == 1:
          bill.update({"Food":{"item":"jollof_spaghetti","price":num}, "Protein":{"item":"meat","price": 150}})
          change = input("would you like to add drinks? Y/N: ")
          count_three == 0
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"jollof_spaghetti","price":num}, "Protein":{"item":"meat","price": 150}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # MEATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        elif choice == 2:
          bill.update({"Food":{"item":"jollof_spaghetti","price":num}, "Protein":{"item":"egg","price": 100}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"jollof_spaghetti","price":num}, "Protein":{"item":"egg","price": 100}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # chickennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        elif choice == 3:
          bill.update({"Food":{"item":"jollof_spaghetti","price":num}, "Protein":{"item":"chicken","price": 300}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"jollof_spaghetti","price":num}, "Protein":{"item":"chicken","price": 300}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # fishhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        elif choice == 4:
          bill.update({"Food":{"item":"jollof_spaghetti","price":num}, "Protein":{"item":"fish","price": 350}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
               count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"jollof_spaghetti","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"jollof_spaghetti","price":num}, "Protein":{"item":"fish","price": 350}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
        else:
          print("INVALID!!")
      elif change == "N" or change == "n":
        print("Thank you for patronizing us!, your bill is:")
        print("item    |     amount")
        print("------------------------")
        result = 0
        for z in bill.values():
          total = z.get("price")
          print(z.get("item"),":", total) 
          result+=total
        print("------------------------")  
        print("Total: ", result)
        break
      # ///////////////////////////////////////////////////////////
    elif choice == 4:
      portions = int(input("how many portions:"))
      num = 150 * portions
      bill.update({"item":"whiterice and stew","price": num})
      bill.update({"Food":{"item":"fried_rice", "price": num}})
      change = input("would you like to add anything else? Y/N:")
      if change == "Y" or change == "y":
        print("What would you like to buy?")
        count_two = 0   
        menu = int(input("1.protein\n2.drinks\n:"))
        if menu == 1:
         while count_two < 4:
          for y in protein.values():
           print(count_two,y.get("name"),y.get("price"))
          count_two+= 1
        choice= int(input("select the number of your choice\n:"))
        if choice == 1:
          bill.update({"Food":{"item":"whiterice and stew","price":num}, "Protein":{"item":"meat","price": 150}})
          change = input("would you like to add drinks? Y/N: ")
          count_three == 0
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
              print(count_three,y.get("name"),y.get("price"))
              count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"meat","price": 150},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"whiterice and stew","price":num}, "Protein":{"item":"meat","price": 150}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # MEATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        elif choice == 2:
          bill.update({"Food":{"item":"whiterice and stew","price":num}, "Protein":{"item":"egg","price": 100}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
              print(count_three,y.get("name"),y.get("price"))
              count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"egg","price": 100},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"whiterice and stew","price":num}, "Protein":{"item":"egg","price": 100}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # chickennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        elif choice == 3:
          bill.update({"Food":{"item":"whiterice and stew","price":num}, "Protein":{"item":"chicken","price": 300}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
             for y in drinks.values():
              print(count_three,y.get("name"),y.get("price"))
              count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"chicken","price": 300},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"whiterice and stew","price":num}, "Protein":{"item":"chicken","price": 300}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
            # fishhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        elif choice == 4:
          bill.update({"Food":{"item":"whiterice and stew","price":num}, "Protein":{"item":"fish","price": 350}})
          change = input("would you like to add drinks? Y/N: ")
          if change == "Y" or change == "y":
            while count_three < 4:
              for y in drinks.values():
               print(count_three,y.get("name"),y.get("price"))
              count_three+= 1
            choice= int(input("select the number of your choice\n:"))
            if choice == 1:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"pepsi", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 2:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"coca-cola", "price": 200}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)
              break
            elif choice == 3:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"fanta", "price": 300}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result)  
              break
            elif choice == 4:
              bill.update({"Food":{"item":"whiterice and stew","price":num},"Protein":{"item":"fish","price": 350},"Drinks":{"item":"sosa", "price": 350}})
              print("Thank you for patronizing us!, your bill is:")
              print("item    |     amount")
              print("------------------------")
              result = 0
              for z in bill.values():
                total = z.get("price")
                print(z.get("item"),":", total) 
                result+=total
              print("------------------------")  
              print("Total: ", result) 
              break 
            else:
              print("INVALID")
          elif change == "N" or change == "n":
            bill.update({"Food":{"item":"whiterice and stew","price":num}, "Protein":{"item":"fish","price": 350}})
            print("Thank you for patronizing us!, your bill is:")
            print("item    |     amount")
            print("------------------------")
            result = 0
            for z in bill.values():
              total = z.get("price")
              print(z.get("item"),":", total) 
              result+=total
            print("------------------------")  
            print("Total: ", result)  
            break
          else:
            print("INVALID")
        else:
          print("INVALID!!")
      elif change == "N" or change == "n":
        bill.update({"item":"whiterice and stew","price": num})
        print("Thank you for patronizing us!, your bill is:")
        print("item    |     amount")
        print("------------------------")
        result = 0
        for z in bill.values():
          total = z.get("price")
          print(z.get("item"),":", total) 
          result+=total
        print("------------------------")  
        print("Total: ", result)
        break
      # ///////////////////////////////////////////////////////////
    else:
      print("INVALID")  
  elif menu == 2:
    print("sorry,you can't buy any protein without buying food")
  elif menu == 3:
    new = 1
    while new < 4:
      for w in drinks.values():
        soda = w.get("name")
        amount = w.get("price")
        print(new,soda,amount)
        new +=1
    decision = int(input("select the number of your choice: "))
    if decision == 1:
      bill_drinks.update({"drink":{"name":"pepsi","price":350}})
      print("Thank you for patronizing us!, your bill is:")
      print("item    |     amount")
      print("------------------------")
      result = 0
      for z in bill_drinks.values():
       total = w.get("price")
       print(w.get("item"),":", total) 
      result+=total
      print("------------------------")  
      print("Total: ", result)  
      break
    elif decision == 2:
      bill_drinks.update({"drink":{"name":"coca-cola","price":200}})
      print("Thank you for patronizing us!, your bill is:")
      print("item    |     amount")
      print("------------------------")
      result = 0
      for z in bill_drinks.values():
       total = w.get("price")
       print(w.get("item"),":", total) 
      result+=total
      print("------------------------")  
      print("Total: ", result)  
      break
    elif decision == 3:
      bill_drinks.update({"drink":{"name":"fanta","price":300}})
      print("Thank you for patronizing us!, your bill is:")
      print("item    |     amount")
      print("------------------------")
      result = 0
      for z in bill_drinks.values():
       total = w.get("price")
       print(w.get("item"),":", total) 
      result+=total
      print("------------------------")  
      print("Total: ", result)  
      break
    elif decision == 4:
      bill_drinks.update({"drink":{"name":"sosa","price":350}})
      print("Thank you for patronizing us!, your bill is:")
      print("item    |     amount")
      print("------------------------")
      result = 0
      for z in bill_drinks.values():
        total =eval( w.get("price"))
        print(w.get("name"),":", total) 
        result+=total
      print("------------------------")  
      print("Total: ", result)    
      break
  else:
    print("INVALID!")  


    

