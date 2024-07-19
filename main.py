# Sözlüğe daha fazla kelime ekleyelim
meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "BRB": "Kısa süreliğine ayrılmak",
    "AFK": "Klavye başında olmamak",
    "GTG": "Gitmem gerek",
    "IDK": "Bilmiyorum",
    "TBH": "Dürüst olmak gerekirse",
    "IMO": "Bence",
    "OMG": "Aman Tanrım"
}

# Selamlama mesajı ve talimatlar
print("Merhaba! Bu program, anlamadığınız kelimelerin anlamlarını bulmanıza yardımcı olacak.")
print("Lütfen anlamak istediğiniz kelimeleri hepsini büyük harflerle yazın.")
print("Program size toplam 5 kelime sorma hakkı verecek.\n")

# Kullanıcıya 5 kez kelime sorma
for i in range(5):
    word = input(f"({i+1}/5) Anlamadığınız bir kelime yazın: ")

    if word in meme_dict:
        meaning = meme_dict[word]
        print(f"{word}: {meaning}\n")
    else:
        print(f"{word} kelimesinin anlamı bulunamadı.\n")

print("Program sona erdi. Teşekkürler!")
