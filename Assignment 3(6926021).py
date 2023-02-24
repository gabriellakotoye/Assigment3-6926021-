#list of brand of cars available
cars={'Toyota','Tesla','BMW','Porsche','Honda','Hyundai','Audi','Mazda','Lexus',
'Rolls-Royce','Mercedes-Benz','Volkswagen','Kia','Volvo','Peugot','Suzuki','Mitsubishi',
'Mclaren','Nissan','Bugatti','Alfa Romeo','Cadillac','Maserati','Bentley','Lamborghini',
'Aston Martin','Jaguar','Jeep','Ford Mustang','Ferrari'}
models={'GR Supra':20000,'Model Y':25000,'i8 M':75000,'Taycan':30000,
'Accord':15000,'Sonata':16500,'R8':40000,'CX-5':32000,'RX':45000,
'Ghost':300000,'AMG GT':250000,'GTI Roadster':79000,'Cadenza':39500,
'XC90':54000,'200s':43000,'Compact':36000,'XFC':60000,'P1':180000,
'GT-R':65000,'Mistral':5000000,'Guila SWB Zagato':150000,'Eldorado':2000000,
'MC20':90000,'Continental GT':300000,'Autentica':3500000,'DBX 707':350000,
'F-Type':200000,'Wrangler':59000,'Dark Horse':95000,'Futuro':1500000}
#get user input for cars
brandOfCars=input('What brand of car are interested in purchasing? :  ')
#check if brand of car is in available list of cars
if brandOfCars in cars:
    print('Yes, it is available.')
else:
    print('Sorry, it is not available.')
#if brand of car is available, specify model
modelOfCar=input('What specific car model are you interested in?  ')
if modelOfCar in models :
    print('Yes, it is available.')
    priceOfCar=models[modelOfCar]
    print('The price is ${}.'.format(priceOfCar))
else:
    print('Sorry, that model is not available.')

    