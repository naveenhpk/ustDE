import csv


list_item=[{"name":"Banana","price":30},
           {"name":"Boost","price":130},
           {"name":"Fizz","price":30},
           {"name":"Milk","price":20},
           {"name":"Bread","price":80},
           {"name":"Cheese","price":70}]

print("Welcome to VBazar")
print("Press any Number from the Menu")

items={}
def main():
    x=int(input("1.View Item \n 2.Add item to cart \n 3.Update cart \n 4.Remove item from cart \n 5.Exit and print bill"))
    if x==1:
        view(list_item)
    elif x==2:
        add()
    elif x==3:
        update()
    elif x==4:
        remove()
    elif x==5:
        printbill()
    else:
        raise Exception("Invalid selection")

def dcon():
    x=input("do you wnat to continue y/n")
    if x=='y':
        main()
    else:
        raise Exception("Exiting")


def view(list_item):
    for i in list_item:
        print(i['name'], " ", i["price"])
    dcon()


def add():
    for i in list_item:
        print(i['name'], " ", i["price"])
    ag = True
    while ag:
        item = input("select any Item to add").capitalize()
        qty =int(input("Enter the quantity"))
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
    dcon()
def update():
    ag = True
    while ag:
        print("Item  quantity")
        for key, value in items.items():
            print(key, " ", value)
        upitem = input("Enter the item to update").capitalize()
        upqty = int(input("Enter the quantity"))
        items[upitem] = upqty
        print("do you want to update more y/n")
        x = input("")
        if x == 'y':
            ag = True
        else:
            ag = False
    print(items)
    dcon()

def remove():
    ag = True
    while ag:
        try:
            upitem = input("Enter the item to delete").capitalize()
            del items[upitem]
        except:
            print("Item not found")
        print("do you want to delete more y/n")
        x = input("")
        if x == 'y':
            ag = True
        else:
            ag = False
    print(items)
    dcon()

def printbill():
    gtotal = 0
    with open('Bill.csv', mode='w') as pfile:
        pfile_writer = csv.writer(pfile, delimiter=" ", quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        pfile_writer.writerow("{:<10} {:<10} {:<10} {:<10}".format('Items', 'Quantity', 'Price', 'Total'))
        pfile_writer.writerow('*' * 80)
        for i in items:
            name = i
            qty = items[i]
            for x in list_item:
                if x['name'] == name:
                    price = x["price"]
            priceofsingleitem = qty * price
            gtotal += priceofsingleitem
            #
            pfile_writer.writerow("{:<10} {:<10} {:<10} {:<10}".format(i, qty, price, priceofsingleitem))
        pfile_writer.writerow('*' * 80)
        pfile_writer.writerow("{:<10} {:<10} {:<10} {:<10}".format('', '', 'Grand_Total', gtotal))

main()

