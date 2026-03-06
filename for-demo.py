sayilar=[1,3,5,7,9,12,19,21]
total=0
print("Listedeki 3'ün katı olan sayılar:")
for num in sayilar:
    if num%3==0:
        print(num)
        total+=num
print("3'ün katı olan sayıların toplamı:", total)
print("**"*10)

total=0
for num in sayilar:
    total+=num
print("Listedeki sayıların toplamı:", total)
print("**"*10)

print("En fazla 5 harf içeren şehirler:")
sehirler=['Kocaeli','Istanbul','Ankara','Izmir','Rize']
for sehir in sehirler:
    if(len(sehir)<=5):
        print(sehir)
print("**"*10)

urunler=[
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'}, 
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'}, 
    {'name':'samsung s10','price':'7000'} 
]
total=0
for urun in urunler:
    fiyat=(int(urun['price']))
    total+=fiyat
print("Ürünlerin toplam fiyatı:",total)

print("Fiyatı en fazla 5000 TL olan ürünler:")
for urun in urunler:
    if int(urun['price'])<=5000:
        print( urun['name'])
