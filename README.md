Merhaba!
Ben İngilizce anlamayan kişilerin rahatça kod yazabilmesi için, "piton-konsol" kütüphanesini geliştirdim. Takıldığım yerlerde ve "Burada ne yaparsak Türkçe karakterleri kabul eder?" gibi teknik kısımlarda Gemini'dan yardım alarak bu projeyi tamamladım.
"Neden Türkçe kodlama dili yok? Neden İngilizce bilmeyen kişiler kod yazamıyor?"
Bir gün bu soruları kendime sordum ve harekete geçerek bu kütüphaneyi yaptım. Şunu söylemeliyim ki; kodlama, bazılarınızın filmlerde veya dizilerde gördüğü gibi yukarıdan aşağı akan karmaşık semboller değil, tamamen "mantık" ile ilgilidir. Ve bu kütüphane sayesinde artık İngilizce engeli de kalktı!
Nasıl Yüklenir?
Kod yazma uygulamanızın (pip yükle) bölümünden: piton-konsol yazarak aratın.
Terminal üzerinden: pip install piton-konsol komutunu kullanın.
ÖNEMLİ NOT:
Bu kütüphaneyi kod yazarken çağırmak için import piton_konsol yazmalısınız. Evet, tire değil alt çizgi _ ile!
KULLANIM REHBERİ:
Python'un çekirdek kelimelerini değiştirmek zor olduğu için sistem şöyle çalışır:
Asıl kodunuzu başka bir dosyada düzenleyin ve uzantısını .txt olarak kaydedin. Mümkünse bu dosya hiçbir klasörün içinde olmasın, doğrudan dahili depolamaya koyun. Ardından ana dosyanızın en üstüne import piton_konsol yazarak çalıştırın.
