


def get_pet_shop_name(pet_shop):
    return(pet_shop['name'])

def get_total_cash(pet_shop):
     return(pet_shop['admin']['total_cash'])

def add_or_remove_cash(pet_shop,amount):
    pet_shop['admin']['total_cash'] = pet_shop['admin']['total_cash'] + amount
    return (pet_shop['admin']['total_cash'])
    
def get_pets_sold(pet_shop):
    return (pet_shop['admin']['pets_sold'])

def increase_pets_sold(pet_shop,amount):
    pet_shop['admin']['pets_sold']+= amount
    return pet_shop['admin']['pets_sold']

def get_stock_count(pet_shop):
    stock=0
    for i in pet_shop['pets']:
        stock+=1
    return stock

def get_pets_by_breed(pet_shop,breed_type):
    breed=[]
    pets_count=[]

    for i in pet_shop['pets']:
        breed.append(i['breed'])

    for i in range(len(breed)):
        if breed_type==breed[i]:
            pets_count.append(breed[i])

        # else:
        #     pass

    return pets_count

def find_pet_by_name(pet_shop,pet_name):
    for pets in pet_shop['pets']:
        if pet_name ==pets['name']:
            return pets
      
def remove_pet_by_name(pet_shop,pet_name):
    for i in pet_shop['pets']:
        if pet_name==i['name']:
            i['name']=None
def add_pet_to_stock(pet_shop,new_pet):
    new_pet={'name':'somename','pet_type':'sometype','breed':'somebreed','price':1}
    pet_shop['pets'].append(new_pet)
    return pet_shop

def get_customer_cash(customer):
    return customer['cash']   

def remove_customer_cash(customer,amount):
    customer['cash']-=amount

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer,new_pet):
    return customer['pets'].append(new_pet)
def customer_can_afford_pet(customer,pet):
    if customer['cash'] >= pet['price']:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop,pet,customers):
    if pet !=None and pet['price']<=customers['cash']:

        customers['pets'].append(pet)
        pet_shop['admin']['pets_sold']+=1
        customers['cash']-=pet['price']
        pet_shop['admin']['total_cash']+=pet['price']
    
    
    


    
