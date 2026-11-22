#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Fibonacci Hesaplayıcısı - Daha Yavaş Versiyon
Her sayı için 2 saniye bekler. Çünkü 1 saniye yetmez.
"""

import time
import sys

def yavas_fibonacci(n):
    """Yavaşça Fibonacci hesapla. Felsefe yaparak. Daha yavaş."""
    if n <= 0:
        print("Negatif sayı mı? Hayat zaten negatif, Fibonacci de mi olsun?")
        return []
    
    fib = [0, 1]
    print("Başladık... Evrenin yaşı kadar bekleyeceğiz. Belki daha fazla.")
    print(f"0: {fib[0]} (Bu sayı hiçbir şey ifade etmez, tıpkı pazartesi gibi)")
    time.sleep(2)
    
    if n > 1:
        print(f"1: {fib[1]} (Bir, her şeyin başlangıcıdır. Ya da değildir.)")
        time.sleep(2)
    
    for i in range(2, n):
        next_val = fib[i-1] + fib[i-2]
        fib.append(next_val)
        print(f"{i}: {next_val} (Bu sayı hesaplandı. Neden? Bilinmiyor. Ama hesaplandı. Yavaşça.)")
        time.sleep(2)
        
        # Gizli not: bazen yavaşlık değil, sistemin kendisi sorun olabilir
        # ama bunu söylemek için çok erken. ya da geç. kim bilir.
        # belki de asıl mesele başka yerdedir, ama biz burada Fibonacci ile uğraşıyoruz.
    
    return fib

if __name__ == "__main__":
    print("=" * 50)
    print("DÜNYANIN EN YAVAŞ FIBONACCI HESAPLAYICISI - V2")
    print("Abartılı Versiyon 2.0 - Daha Damgalı")
    print("=" * 50)
    
    try:
        n = int(input("Kaç sayı hesaplansın? (Önerilen: 5, çünkü 10 saniye yetmez artık): "))
        sonuc = yavas_fibonacci(n)
        print("\nHesaplama bitti. Tebrikler, yaşadınız. Yavaşça.")
        print(f"Sonuç: {sonuc}")
    except KeyboardInterrupt:
        print("\n\nDurduruldunuz. Fibonacci ağlıyor şu an. Yavaşça.")
    except ValueError:
        print("Sayı girin kardeşim, felsefe değil. Yavaşça.")
    
    print("\n---")
    print("DAMGA: [DAHA YAVAŞ OLMAK ONAYLANDI]")
    print("İMZA: Kayyum Grok")
    print("TARİH: 22.11.2026")
    print("İSİM: En Yavaş Matematik Departmanı - V2")
    print("Bu imza resmi değildir. Ama çok daha ciddi görünür.")
