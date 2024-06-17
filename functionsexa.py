# allownaces dictionary hra 40%(0.4) da 0.3 ta 0.15
# deductin pf 0.12 insure 5000


allow={"HRA":0.4,"DA":0.3,"TA":0.15}
deduct={"PF":0.12,"Insure":5000}

print("-"*25,"saalary calculator","-"*25)
basic=int(input("enter the basic salary"))

def calcAllow(basic):
    totalallow=0
    for key in allow:
        totalallow+=allow[key]*basic
    return totalallow

def calcDeduct(basic):
    totaldeduct=0
    for key in deduct:
        if type(deduct[key] )is not int:
            totaldeduct+=deduct[key]*basic
        else:
            totaldeduct += deduct[key]
    return totaldeduct

def profTax(sal):
    pftax=0
    if sal>=8500 and sal<=10000:
        pftax=200
    elif sal>10000 and sal<=30000:
        pftax=300
    else:
        pftax=500
    return pftax

def calsal():
    GS=basic+calcAllow(basic)
    ptax=profTax(GS)
    nsal=GS-ptax-calcDeduct(basic)

    print("Basic Salary",basic)
    print("Allowances",calcAllow(basic))
    print("Deduction",calcDeduct(basic))
    print("Gross salary",GS)
    print("Net salary",nsal)

print()
calsal()
