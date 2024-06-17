list_item=[{"name":"Banana","price":30},
           {"name":"Boost","price":130},
           {"name":"Fizz","price":30},
           {"name":"Milk","price":20},
           {"name":"Bread","price":80},
           {"name":"Cheese","price":70}]
print("Welcome to VBazar")
print("Press any Number from the Menu")
# cart=[]
items={}
ch=True
while ch:
    x=int(input("1.View Item \n 2.Add item to cart \n 3.Update cart \n 4.Remove item from cart \n 5.Exit and print bill"))
    if x==1:
        # print("Item   Price")
        for i in list_item:
            print(i['name']," ",i["price"])
    elif x==2:
        num=1
        for i in list_item:
            print(num,i['name']," ",i["price"])
            num+=1
        ag=True
        while ag:
            item=input("select any Item to add").capitalize()
            qty=int(input("Enter the quantity"))
            if item in items:
                q=items[item]
                r=q+qty
                items[item]=r
            else:
                items[item] =qty
            print("do you want to add more y/n")
            x=input("")
            if x=='y':
                ag=True
            else:
                ag=False
        # cart.append(items)
        print(items)

    elif x==3:
        # [{'Banana': '2', 'Milk': '5'}]
        ag = True
        while ag:
            print("Item  quantity")
            for key,value in items.items():
                print(key, " ",value)
            upitem=input("Enter the item to update").capitalize()
            upqty=int(input("Enter the quantity"))
            items[upitem]=upqty
            print("do you want to update more y/n")
            x = input("")
            if x == 'y':
                ag = True
            else:
                ag = False
        print(items)
    elif x==4:
        # [{'Banana': '2', 'Milk': '5'}]
        ag = True
        while ag:
            # print("Item  quantity")
            # for key, value in items.items():
            #     print(key, " ", value)
            upitem = input("Enter the item to delete").capitalize()
            del items[upitem]
            print("do you want to delete more y/n")
            x = input("")
            if x == 'y':
                ag = True
            else:
                ag = False
        print(items)
    elif x==5:
        # {'Banana': '2', 'Milk': '5'}
        gtotal=0
        print("{:<10} {:<10} {:<10} {:<10}".format('Items','Quantity','Price','Total'))
        print('*'*40)
        for i in items:
            name=i
            qty=items[i]
            for x in list_item:
                if x['name']==name:
                    price=x["price"]
            priceofsingleitem=qty*price
            gtotal+=priceofsingleitem
            #
            print("{:<10} {:<10} {:<10} {:<10}".format(i, qty,price,priceofsingleitem))
        print('*' * 40)
        print("{:<10} {:<10} {:<10} {:<10}".format('', '', 'Grand_Total', gtotal))
    else:
        break
    print("do y want to continue y/n")
    x = input()
    if x=='y':
        ch=True
    else:
        ch=False




