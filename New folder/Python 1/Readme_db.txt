# Aim: How Can You Use MongoDB for E-Commerce?

. MongoDB is a NoSQL database that stores data in JSON-like documents with dynamic schemas. 
. It simplifies data integration and offers better scalability than traditional relational databases.
. Today’s e-commerce sites need rich data models and dynamic queries. 
. MongoDB provides this, making it a popular choice for many companies.

# E-Commerce Data Models Using MongoDB:
****************************************
Product Catalogs:
*****************
. The product catalog is a record of all the items available for sale on the e-commerce website.

. unique identifier (SKU)
. price
. title
. description
. quantity

# Example of the product document:
***********************************

collection 1:

db.supermarket.insert(
{
  "name" : "SriVenkateshwaraSuperMarket", 
  "address": ["Nellore","nawabpet"],
  "post": 524001, 
  "contactno" : 8912349900
})

collection 2:

db.employee details.insert(
{
  "name" : "praveen",
  "surname": "koveri" ,
  "dob" : 20-08-1995,
  "gender" : "male",
  "education qualification: "B.Com
  "materialsstatus" : "married",
  "mobileno": 7893409654,
  "address" : ["Nellore","mulapet"]
  "post": 52410
},
{
  "name" : "prasanth",
  "surname": "vedavaluru" ,
  "dob" : 20-06-1997,
  "gender" : "male",
  "education qualification: "Diploma"
  "materialsstatus" : "married",
  "mobileno": 8907389209,
  "address" : ["Nellore","dhanalakshmipuram"]
  "post": 52410
},
{
  "name" : "Dhanusha",
  "surname": "Gudla" ,
  "dob" : 09-10-1998,
  "gender" : "female",
  "education qualification: "B.sc"
  "materialsstatus" : "Not-married",
  "mobileno": 9006898028,
  "address" : ["Nellore","kisanagar"]
  "post": 52410
})

Collection 3:

db.coustomer details.insert(
{
  "invoice-id": 750-67-8428,
  "city": "Allur",
  "coustomer type": "member",
  "gender" : "female",
  "productline": ["health",beauty],
  "unitprice": 75.69,
  "quantity": 7,
  "tax 5%": 26.1415,
  "total": 548.9745,
  "date": 10-08-2022,
  "time": 13:06,
  "payment": "Ewallet"
},
{
  "invoice-id": 987-85-7898,
  "city": "Kavali",
  "coustomer type": "Normal",
  "gender" : "male"
  "productline": "Electronic accessories",
  "unitprice": 15.28,
  "quantity": 5,
  "tax 5%": 3.8200,
  "total": 80.2200,
  "date": 15-08-2022,
  "time": 17:06,
  "payment": "cash"
},
{
  "invoice-id": 098-75-5643,
  "city": "Nellore",
  "coustomer type": "normal",
  "gender" : "male"
  "productline": ["sports","travell"],
  "unitprice": 86.31,
  "quantity": 7,
  "tax 5%": 30.2085,
  "total": 634.867,
  "date": 22-08-2022,
  "time": 20:07,
  "payment": "creditcard"
},
})

Collection 4:

db.material details.insert(
{
  "itemname": "Levis Men Navy blue checks shirt",
  "Size": 40,
  "quantity" : 100,
  "id" : 4321,
  "orderdate" :01-09-2022,
  "expectedDelivery" :05-09-2022
  "payment method": "pay on delivery"
},
{ 
  "itemname" : "LouisPhilippe Men Marron Silmfit",
  "Size": 39,
  "quantity":120,
  "id": 987207,
  "orderdate" : 03-09-2022,
  "expectedDelivery" :08-09-2022,
  "payment method": "pay on delivery"
},
{ 
  "itemname": "wrogn men blackjeans slimfit",
  "Size": 36,
  "quantity": 125
  "id": "12893",
  "orderdate" : "10-09-2022",
  "expectedDelivery" :14-09-2022,
  "payment method": "pay on delivery"
})

db.inventory.insert(
{
  "name": "chocolate bar - 100g",
  "price": 10.23,
  "quantity": 2500,
  "categoy": ["chocolate","sweets"]
})

db.inventory.insert(
{
  "name": "Beans (packed)- 250g",
  "price": 6.75,
  "quantity": 6000,
  "categoy": ["vegetables","healthy","organic"]
})

db.inventory.insert(
{
  "name": "Milk - 1ltr",
  "price": 35,
  "quantity": 2000,
  "categoy": ["diary","healthy"]
})

db.inventory.insert(
{
  "name": "Carrots (packed)- 250g",
  "price": 3.75,
  "quantity": 3000,
  "categoy": ["vegetables","healthy","organic"]
})

db.inventory.insert(
{
  "name": "Butter - 500g",
  "price": 25,
  "quantity": 500,
  "categoy": ["diary","healthy","premium"]
})

db.order.insert(
{
    "title": "Samsung Galaxy",
    "colour": ["blue","blue"],
    "model_number": "A123X",
    "storage": ["64 GB","128 GB"]
    "RAM": ["4 GB",6 GB]
    "processor": "mediatek"
    "description": "The greatest Android phone on the market .....",
},

   camera: {
    "rearcamera": "48 MP"
    "frontcamera": "13 MP"   
},    
  shipping_details: {
    "weight": 350,
    "width": 10,
    "height": 10,
    "depth": 1
},
   other details: {
    "netwok type": ["4G","3G","2G"],
    "simtype": "dual sim",
    "in the box": ["handset","adaptor","charging cable","user manual"],
    "quantity": 99,
    "warranty": "1 year"
},    

  pricing: {
   "selling price": 16,999,
   "extra discount": -4,200,
   "special price": 12,799,
   "shipping fee + secured packaging fee": 50,
   "shipping discount": -4o
   "total amount": 12,799

   payment information:{
      "payment method": "pay on delivery"
},
   shippingAddress: {
      "country": "india",
      "steet 1": "2525 shearbroke east",
      "street 2": "Appartment 40",
      "city": "Hyderabad",
      "state": "Telangana",
      "pin": 524***
 },
    billingAddress: {
      "country": "india",
      "steet 1": "2520 shearbroke east",
      "street 2": "Appartment 31",
      "city": "Hyderabad",
      "state": "Telangana",
      "pin": 524***
},
   "trackingnumber": "IND6875345"
})

db.orders.insert( 
  { 
     "userid": "customer1@gmail.com",
     "paymentstatus": "processed",
     "status": "shipped",
     "amount": 70,
     "items": [ 
  {
    "sku": "HPH"
    "quantity": 1,
    "pice": 29.99,
    "discounts": 1.99,
    "preTax": 28,
    "afterTax": 30
   },
   {
    "sku": "HPP"
    "quantity": 2,
    "pice": 19.99,
    "discounts": 0.99,
    "preTax": 38,
    "afterTax": 40 
   } 
 ],
   "shippingAddress": {
      country: "india",
      steet 1: "2525 shearbroke east",
      street 2: "Appartment 40",
      city: "Hyderabad",
      state: "Telangana",
      pin: 524***
 },
    billingAddress: {
      country: "india",
      steet 1: "2520 shearbroke east",
      street 2: "Appartment 31",
      city: "Hyderabad",
      state: "Telangana",
      pin: 524***
 },
    "trackingnumber": "IN55754765"
} )

db.book.insertOne( 
{ 
    name: "Harry Potter",
    author: "J. K. Rowling",
    skus: [
     {
       sku: "HPH"
       pice: 29.99,
       quantity: 100,
       feature: "hard cover"
    },
       sku: "HPP"
       pice: 19.99,
       quantity: 200,
       feature: "paperback"
    } ]
} )

db.user.insert( 
{ 
    _id: "customer1@gmail.com"
    firstname: "sai",
    lastname: "maneesh",
    shippingAddress: {
      country: "india",
      steet 1: "2525 shearbroke east",
      street 2: "Appartment 40",
      city: "Hyderabad",
      state: "Telangana",
      pin: 524***
 },
    billingAddress: {
      country: "india",
      steet 1: "2520 shearbroke east",
      street 2: "Appartment 31",
      city: "Hyderabad",
      state: "Telangana",
      pin: 524***
 }
} ) 

db.payments.insert( 
  { 
     userid: "customer1@gmail.com",
     type: "credit",
     status: "verified",
     card: 
 {
      type: "visa",
      lastFourNumbers: "1212",
      expiryMonth: 12,
      expiryYear: 2024,
      cvvVerified: "true"       
 }
} )

---------------------------------------------------------------------------------------------------------------------------------------------------------

list of collection 
   
# MONGODB & Tables :

1. Employee  
   1. Aim: Employee working in current organization    
   2. Field :      
      1. employee_name        
      2. employee_id        
      3. dob       
      4. gender        
      5. education       
      6. materials_status        
      7. mobile_number
      8. address

2. Customer        
   1. Aim: Customer Information    
   2. Field:        
      1. invoice_id     
      2. city        
      3. customer_type        
      4. gender        
      5. product_line
      6. unit_price
      7. quantity
      8. tax 5%
      9. Ttotal
      10. data
      11. time
      12. payments

3. Material    
   1. Aim: Material Information    
   2. Field:        
      1. item_name       
      2. size       
      3. quantity        
      4. id        
      5. order_date        
      6. expected_delivery       
      7. tracking_number
      8. payments_method

4. Inventory    
   1. Aim: Inventory Information    
   2. Field:        
      1. name        
      2. quantity        
      3. price        
      4. category       

5. Discounts    
   1. Aim:  Discounts Information    
   2. Feilds:        
      1. product           
      2. quantity        
      3. price        
      4. total        
      5. discounts        
      6. total_amount

6. Bills:
   1. Aim: Bills Information
   2. Field:
      1. discription
      2. quantity
      3. mrp 
      4. rate 
      5. amount
      
7.  Order:
   1. Aim: Order Information
   2. Field:
      1. item_name
      2. quantity
      3. order_date
      4. time       



