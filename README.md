# Sıfırdan Lineer Regresyon (Linear Regression from Scratch)

Bu proje; herhangi bir makine öğrenmesi kütüphanesi (scikit-learn vb.) kullanılmadan, doğrudan Python ve temel matematiksel formüller ile geliştirilmiş basit bir lineer regresyon modelidir. 

Projenin temel amacı, regresyon analizinin arkasında yatan matematiksel mantığı ve parametre optimizasyon süreçlerini uygulamalı olarak kavramaktır.

---

## Matematiksel Altyapı ve Yöntem

Model, bağımsız değişken $X$ ile bağımlı değişken $y$ arasındaki ilişkiyi aşağıdaki doğru denklemi ile modeller:

$$y = mX + b$$

* **$m$ (Eğim / Slope):** Değişkenler arasındaki ilişkinin yönünü ve miktarını belirler.
* **$b$ (Kesişim / Intercept):** Doğrunun y-eksenini kestiği noktayı temsil eder.

### Parametre Hesaplama Formülleri

Eğim ($m$) ve kesişim ($b$) katsayıları En Küçük Kareler Yöntemi (Ordinary Least Squares) kullanılarak hesaplanır:

$$m = \frac{\sum (X - \bar{X})(y - \bar{y})}{\sum (X - \bar{X})^2}$$

$$b = \bar{y} - m\bar{X}$$

*(Burada $\bar{X}$ ve $\bar{y}$, sırasıyla $X$ ve $y$ değişkenlerinin ortalama değerleridir.)*

---

## Kullanılan Teknolojiler

* **Python:** Saf (pure) Python veri yapıları ve döngüler.
* **Math (Standart Kütüphane):** Ortalamalar ve toplam matris hesaplamaları için.

---

## Kazanımlar

* Makine öğrenmesi algoritmalarının "kara kutu" (black box) mantığından çıkarılarak arka planındaki türev ve optimizasyon süreçlerinin anlaşılması.
* Dış kütüphane bağımlılığı olmadan saf kod ile veri üzerinde tahmin yürütme pratiği.
