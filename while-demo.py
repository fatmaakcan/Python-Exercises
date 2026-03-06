sayilar=[1,3,5,7,9,12,19,21]

i=0

while i<len(sayilar):
    print(sayilar[i])
    i+=1

print("****"*10)

sayi_baslangic=int(input("Lutfen bir baslangic degeri giriniz: "))
sayi_bitis=int(input("Lutfen bir bitis degeri giriniz: "))

i=sayi_baslangic

while i<=sayi_bitis:
    i+=1
    if i%2!=0:
        print(i)
print("****"*10)

i=100
while i>0 :
    print(i)
    i-=1

print("****"*10)

numbers=[]

i=0

while i<5:
    sayi=int(input("Bir sayi giriniz: "))
    numbers.append(sayi)
    i+=1
#numbers.sort() metodu ile de siralama kolay bir şekilde yapılabilir.
temp=0
for j in range(len(numbers)-1):
    for i in range(len(numbers)-1-j):
        if numbers[i]>numbers[i+1]:
            temp=numbers[i]
            numbers[i]=numbers[i+1]
            numbers[i+1]=temp
print(numbers)

print("****"*10)

urunler=[]
adet=int(input("Kac adet urun eklemek isiyorsunuz:"))
i=0
while(i<adet):
    urun_adi=input("Urun adi: ")
    urun_fiyati=float(input("Urun fiyati: "))
    urunler.append({
        "urun_adi":urun_adi,
        "urun_fiyati":urun_fiyati
    })
    i+=1
for urun in urunler:
    print(f"Urun adi: {urun['urun_adi']}, Urun fiyati: {urun['urun_fiyati' ]}")
