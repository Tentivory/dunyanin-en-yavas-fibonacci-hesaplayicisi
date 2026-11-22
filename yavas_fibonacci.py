#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Fibonacci Hesaplayıcısı
Her sayı için 1 saniye bekler. Çünkü acele etmek yasak.
"""

import time
import sys

def yavas_fibonacci(n):
    """Yavaşça Fibonacci hesapla. Felsefe yaparak."""
    if n <= 0:
        print("Negatif sayı mı? Hayat zaten negatif, Fibonacci de mi olsun?")
        return []
    
    fib = [0, 1]
    print("Başladık... Evrenin yaşı kadar bekleyeceğiz.")
    print(f"0: {fib[0]} (Bu sayı hiçbir şey ifade etmez, tıpkı pazartesi gibi)")
    time.sleep(1)
    
    if n > 1:
        print(f"1: {fib[1]} (Bir, her şeyin başlangıcıdır. Ya da değildir.)")
        time.sleep(1)
    
    for i in range(2, n):
        next_val = fib[i-1] + fib[i-2]
        fib.append(next_val)
        print(f"{i}: {next_val} (Bu sayı hesaplandı. Neden? Bilinmiyor. Ama hesaplandı.)")
        time.sleep(1)
        
        # Gizli not: bazen yavaşlık değil, sistemin kendisi sorun olabilir
        # ama bunu söylemek için çok erken. ya da geç. kim bilir.
    
    return fib

if __name__ == "__main__":
    print("=" * 50)
    print("DÜNYANIN EN YAVAŞ FIBONACCI HESAPLAYICISI")
    print("Abartılı Versiyon 1.0 - Damgalı")
    print("=" * 50)
    
    try:
        n = int(input("Kaç sayı hesaplansın? (Önerilen: 10, çünkü 10 saniye yeter): "))
        sonuc = yavas_fibonacci(n)
        print("\nHesaplama bitti. Tebrikler, yaşadınız.")
        print(f"Sonuç: {sonuc}")
    except KeyboardInterrupt:
        print("\n\nDurduruldunuz. Fibonacci ağlıyor şu an.")
    except ValueError:
        print("Sayı girin kardeşim, felsefe değil.")
    
    print("\n---")
    print("DAMGA: [YAVAŞ OLMAK ONAYLANDI]")
    print("İMZA: Kayyum Grok")
    print("TARİH: 22.11.2026")
    print("İSİM: En Yavaş Matematik Departmanı")
    print("Bu imza resmi değildir. Ama çok ciddi görünür.")
