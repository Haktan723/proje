import random
# Hakkınızdaki gerçeklerin listesi
gercekler = [
    "Flutter ile mobil uygulama geliştiriyorum.",
    "Python ve ROS kullanarak projeler yapıyorum.",
    "Teknofest'te ikinci olan bir takımdaydım.",
    "Gelecekte yurtdışında çalışmayı hedefliyorum.",
    "Yazılım geliştirmek benim en büyük hobim."
]
# Rastgele bir gerçek seç ve yazdır
rastgele_gercek = random.choice(gercekler)
print("Kendim hakkında bir gerçek:", rastgele_gercek)


# Meme sözlüğü
meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Kahkaha atarak yere yuvarlanmak",
    "BRB": "Birazdan döneceğim",
    "OMG": "Aman Tanrım!"
}
# Kullanıcıdan bir kelime al
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
# Kelimenin anlamını kontrol et ve sonucu göster
if word in meme_dict:
    print("anlamı:",(meme_dict[word]))
else:
    print("Bu kelime sözlükte bulunamadı!")
