#TÜM KODLARI CHATGPT 3.5 tarafından yazılmıştır. Readme kısmıda bu duruma Dahildir.

```
  ben bir python uygulması yazacağım . uygulamam kripto para isimleri ve ücretlerini https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json urlsinden çekiyor. Bu url ye istek atacağız.  currency isimi , price diyatı belirtmektedir. Dönen veriler Kripto para isimleri ve fiyatları olacak bu verileri işleyerek en yüksek kripto para fiyatı ve isimlerini kullanıcıya dönmek istiyorum. adım adım ilerleyerek bu kodu bana yaz

```

# En Yüksek Kripto Para Fiyatlarını Bulma Uygulaması

Bu Python uygulaması, belirli bir JSON veri setinden kripto para birimlerinin fiyatlarını çeker, en yüksek fiyatları bulur ve kullanıcıya sunar.

## Kod Açıklamaları

```python
import requests
import json
```

İlk olarak, gerekli kütüphaneleri içe aktarıyoruz: `requests` (veri çekmek için) ve `json` (JSON verilerini işlemek için).

```python
url = "https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"
```

Verileri çekeceğimiz JSON dosyasının URL'sini belirtiyoruz.

```python
response = requests.get(url)
```

Belirtilen URL'ye bir HTTP GET isteği gönderiyoruz ve yanıtı `response` değişkenine atıyoruz.

```python
if response.status_code == 200:
    data = json.loads(response.text)
```

Eğer istek başarılı olduysa (HTTP durum kodu 200 ise), JSON verilerini bir Python sözlüğüne dönüştürüyoruz.

```python
prices = []
```

Fiyatları saklamak için bir liste oluşturuyoruz.

```python
for item in data:
    currency_name = item["currency"]
    price = float(item["price"])
    prices.append((currency_name, price))
```

Her bir kripto para birimi ve fiyatını JSON verilerinden alıyoruz ve bunları bir liste içinde tuple olarak saklıyoruz.

```python
prices.sort(key=lambda x: x[1], reverse=True)
```

Fiyatlara göre sıralama yapıyoruz, en yüksek fiyatları en başta olacak şekilde.

```python
print("En yüksek 10 kripto para birimi ve fiyatları:")
for i, (currency, price) in enumerate(prices[:10], start=1):
    print(f"{i}. {currency}: {price}")
```

En yüksek 10 fiyatı ve kripto para birimini kullanıcıya gösteriyoruz.

## Kullanım

Uygulamayı çalıştırmak için Python ortamında çalıştırın:

```
python highest_crypto_prices.py
```

## Katkı

Katkılarınızı memnuniyetle karşılıyoruz! Projeye katkıda bulunmak için bir Issue açabilir veya bir Pull Request gönderebilirsiniz.





# ÇIKTIMDA EKTEDİR.

1. 42: 21143.73003782
2. BULL2: 14755.0
3. XTZBULL: 14335.0
4. ADABULL: 11287.5
5. WBTC: 9642.31376054
6. BTC: 9515.57891943
7. RBTC: 9513.98849856
8. BTMXBULL: 8300.0
9. TRYBBEAR: 6807.5
10. USDTDOOM: 6585.0

