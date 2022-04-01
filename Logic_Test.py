from time import sleep


def greeting():
    print("\nSelamat Datang Di\nToko SukaLaku\n")

def promo():
    print("Promo Harga Murah Hari Ini")
    print ('1. %s Rp.%s' %(item_name[0],item_price[0]))
    print ('2. %s Rp.%s' %(item_name[3],item_price[3]))

def all_prod():
    print("Produk Yang Tersedia Hari Ini")
    print ('1. %s Rp.%s' %(item_name[0],item_price[0]))
    print ('2. %s Rp.%s' %(item_name[1],item_price[1]))
    print ('3. %s Rp.%s' %(item_name[2],item_price[2]))
    print ('4. %s Rp.%s' %(item_name[3],item_price[3]))
    print ('5. %s Rp.%s' %(item_name[4],item_price[4]))
    

def beli():
    print("Silahkan tulis nama barang dan jumlahnya")
    barang = input("Nama Barang = ")
    
    if barang not in item_name:
        print("%s (tidak ada barang tersebut di toko kami)" %barang)
        beli()
    else:
        item_beli.append(barang)
        jumlah = int(input("Jumlah = "))
        qtt_beli.append(jumlah)
        print("%s %s sudah masuk di keranjang belanja" %(jumlah,barang))
        pil2 = input("Apakah anda ingin berbelanja yang lain? (Y/T)")
        if pil2=="Y":
            beli()
        elif pil2=="T":
            total()
        else:
            print("Error!!! Pilihan anda salah")

        

def total():
    print("\n")
    jml_item_beli=(len(item_beli))
    total = 0
    for i in range(0,jml_item_beli):
        amount = item_price[item_name.index(item_beli[i])] * qtt_beli[i]
        hitung.append(amount)
        total = total + amount
    print ("Total harga : Rp. %s " %total)    
    print ("Detail:")
    for x in range(0,jml_item_beli):
        print("%s %s -> Rp. %s" %(qtt_beli[x],item_beli[x],hitung[x]))
    
    
    
    
        

if __name__=="__main__":
    item_name = ['susu','daging','lampu','masker','apel']
    item_price = [50000,20000,15000,25000,30000]
    item_beli =[]
    qtt_beli = []
    hitung = []
    
       
    greeting()
    sleep(1)
    promo()
    pil = input("Apakah Anda Ingin Melihat Produk Lain? (Y/T)")
    if pil=="Y":
        all_prod()
        beli()
    elif pil=="T":
        beli()
    else:
        print("Error!!! Pilihan anda salah")    
    


    
