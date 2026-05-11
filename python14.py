s={
    "id":101,
    "name":"ram",
    "add":{
        "city":"pune",
        "state":"maharashtra",
        "pin code":123456
    }
}

print(s)
print(s.keys())
print(s["name"])
print(s["add"])
print(s["add"]["state"])
print(type(s["add"]))

for key,values in s.items():
    if type(values)==dict:
        for nest_key,nes_val in values.items():
            print(nest_key)
    print(key)
    
#-------------------------------------------------

t={
    "id":"AB101",
    "marks":[10,20,30]
}
print(t)

for key in t:
    print(key)
    
for k,v in t.items:
    print(k,v)
    
for values in s.value():
    if type(values)==list:
        for items in values:
            print(items)
    print(values)
    
#---------------------------------------------------
s={
    "name":"ram",
    "marks":[77,88,89],
    "sub":("java","python","maths"),
    "add":{
        "pin":123456,
        "city":"pune"
    } 
}

for key,values in s.items():
    
    if type(values)==list:
        for items in values:
            print(items)
    elif type(values)==tuple:
        for items in values:
            print(items)
    elif type(values)==dict:
        for k,v in values.items():
            print(v)
    else:
        print(values)
        
#------------------------------------------------------
#ecommerce website
ecom={
    "grocery":{
        "milk":40,
        "sugar":100,
        "chocolates":70
    },
    "clothes":{
        "tshirts":100,
        "pants":70
    },
    "electronics":{
        "laptop":80000,
        "mobile":10000,
        "washing_machine":60000
    }
}
for k,v in ecom.items():
    if k=="clothes":
        for k,v in v.items():
            print(k,v)
            
for category,items in ecom.items():
    print("category:",category)
    for product,price in items.items():
        print(product,price)
        
total=0

for items in ecom.values():
    for price in items.values():
        total+=price
        
print("Total price:",total)

max_price=0
product_name=""

for items in ecom.values():
    for product,price in items.items():
        if price>max_price:
            max_price=price
            product_name=product
print("Costliest product:",product_name,max_price)