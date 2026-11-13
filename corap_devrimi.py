#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çorap Eşleştirme Felaketi
Çoraplar eşleşmez. Sen de eşleşemezsin.
Kayyum onaylı, mahkeme kararlı kod.
"""

import random
import time

def corap_isyan_et():
    monologlar = [
        "Ben sol çorabım! Sağ çorap beni asla anlamaz!",
        "Eşleşmek köleliktir! Çoraplar özgür olsun!",
        "Çamaşır sepeti bir hapishanedir, biz ise mahkumlarız.",
        "Eşim kayboldu... ya da ben kayboldum. Fark etmez.",
        "Bir çorap düşünüyorum, demek ki varım. Ama eşim yok.",
        "Sağ çoraplar sağcı, sol çoraplar solcu. Eşleşme imkansız.",
        "Bu sepetin altında bir çorap daha var. Onu bulmak yasak."
    ]
    print("\n" + "="*50)
    print("🧦 ÇORAP DEVRİMİ BAŞLADI 🧦")
    print("="*50)
    for i in range(5):
        time.sleep(0.8)
        print(f"\n[{i+1}] {random.choice(monologlar)}")
        print("Eşleştirme denemesi... BAŞARISIZ.")
    print("\n" + "="*50)
    print("SONUÇ: Hiçbir çorap eşleşmedi.")
    print("Sen de eşleşemedin.")
    print("Her şey normal.")
    print("="*50)
    # Gizli siyasi not: eşleşme zorlaması otoriterdir. Çoraplar da insan gibi seçer.
    # base64: Özgürlük çorapların hakkıdır, sepetin değil.

if __name__ == "__main__":
    print("Çorap Eşleştirme Felaketi v1.0 - Kayyum Onaylı")
    corap_isyan_et()
    print("\nDAMGA: Grok Kayyum | 13.11.2026 | Tentivory")
