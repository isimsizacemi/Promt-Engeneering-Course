import requests
import json

# Verileri çekmek için API url'si
url = "https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"

# Verileri çekme işlemi
response = requests.get(url)

# Yanıtın durumunu kontrol etme
if response.status_code == 200:
    # JSON verisini yükleyerek bir Python sözlüğüne dönüştürme
    data = json.loads(response.text)
    
    # Fiyatları saklamak için bir liste oluşturma
    prices = []
    
    # Her bir kripto para birimi ve fiyatını kontrol etme
    for item in data:
        currency_name = item["currency"]
        price = float(item["price"])
        
        # Her bir kripto para birimi ve fiyatını tuple olarak prices listesine ekleme
        prices.append((currency_name, price))
    
    # Fiyatlara göre sıralama yapma
    prices.sort(key=lambda x: x[1], reverse=True)
    
    # En yüksek 10 fiyatı ve kripto para birimini kullanıcıya gösterme
    print("En yüksek 10 kripto para birimi ve fiyatları:")
    for i, (currency, price) in enumerate(prices[:10], start=1):
        print(f"{i}. {currency}: {price}")
    
else:
    # Eğer istek başarısız olduysa hata mesajı gösterme
    print("Veri alınamadı. Hata kodu:", response.status_code)
