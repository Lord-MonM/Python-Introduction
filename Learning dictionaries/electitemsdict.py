items = {
    "item1": {"name": "micro_Usb", "qty": 30, "cp":1000, "sp":1500},
    "item2": {"name": "typeC_Usb", "qty": 15, "cp":1500, "sp":2000},
    "item3": {"name": "mini_Usb", "qty": 12, "cp":1500, "sp":2000},
    "item4": {"name": "lighting_cable", "qty": 10, "cp":1500, "sp":2000},
    "item5": {"name": "extention_cords", "qty": 11, "cp":2500, "sp":3000},
    "item6": {"name": "auxilliary_cords", "qty": 20, "cp":1000, "sp":1200},
    "item7": {"name": "Adapter_plug", "qty": 21, "cp":1000, "sp":1500},
    "item8": {"name": "Laptop Adaptor", "qty": 13, "cp":2000, "sp":3000},
    "item9": {"name": "AA_Battery", "qty": 9, "cp":500, "sp":750},
    "item10":{"name": "Bulb", "qty": 34, "cp":1300, "sp":1500},
}

print("----------MENU----------")
print("items"   "       qty   " "    price   ")
print("------------------------")
count = 0
for x in items.values():
    item_name = x.get("name")
    item_qty = x.get("qty")
    item_sp = x.get("sp")
    print(item_name,"|", item_qty,"|",item_sp)
    count += item_qty
print("total no of items:",count)

print("Expected profit from each item")
print("------------------------")
print("items"   "|       sp   " "|   cp  |  " " profit ")
print("------------------------")
count_one = 0
for y in items.values():
    item_name = y.get("name")
    item_sp = y.get("sp")
    item_cp = y.get("cp")
    result = item_sp - item_cp
    print(item_name,"||",item_sp, '-', item_cp, "=", result)
    count_one += result
print("profit from all the items combined:","#",count_one)


          


    

