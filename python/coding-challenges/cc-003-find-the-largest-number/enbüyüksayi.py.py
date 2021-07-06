numarator=0
dizi=[]
while numarator < 5:
  sayı= int(input('Lütfen sayı giriniz: '))
  dizi.append(sayı)
  numarator = numarator +1
def enbuyuksayı(x):
  enbuyuk = x[0]
  for i in x:
    if i > enbuyuk:
      enbuyuk = i
  return f"Girdiginiz en büyük sayı {i}'dir."
print(enbuyuksayı(dizi))