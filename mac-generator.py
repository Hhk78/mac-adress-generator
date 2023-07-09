  
#!/usr/bin/python
# -*- coding: utf-8 -*-

from randmac import RandMac
import os, sys, time

def start():
    pass
    start_time = time.time()
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        num = int(input("\n\n\tBir numara girin: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Oluşturulan anahtar sayısı: ", num)
        print("\n")
        for _ in range(0, num):
            example_mac = "00-00-00-00-00-00"
            generated_mac = RandMac(example_mac)            
            print("[+] Oluşturulan 6 baytlık mac adresi: ",generated_mac)
            
        end = round(time.time() - start_time ,2)
        print("\n\n\t[*]Geçen toplam süre:>  ", end ,"sec")
            
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\n\t[/] Sadece sayı girin...")  
        print("\n\n\n\t[*] Tekrar deneyin [*]")
        time.sleep(2)
        start()
    except KeyboardInterrupt:
        print("[+] CTRL+C kombinasyonu tespit edildi [+]")
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
start()
input("\n\n\n\tÇıkış için enter tuşuna basın")
os.system('cls' if os.name == 'nt' else 'clear')
sys.exit()
