# courseapp
CourseApp, eğitim kurslarını düzenlemek, görüntülemek ve yönetmek için kullanılan bir web uygulamasıdır. Bu uygulama sayesinde kullanıcılar, farklı kursları inceleyebilir, yeni kurslar ekleyebilir ve var olan kursları düzenleyebilir.

## Özellikler
 
- Kursları görüntüleme
- Yeni kurs ekleme
- Kursları düzenleme
- Kursları silme
- Kurs detaylarına erişim

## Kurulum

1. Projeyi klonlayın:

   ```bash
   git clone https://github.com/talhasaygili13/courseapp.git
   cd courseapp
Sanal ortamı (venv) oluşturun ve etkinleştirin:

python -m venv venv

source venv/bin/activate  # Linux veya macOS

venv\Scripts\activate    # Windows

Gerekli bağımlılıkları yükleyin:

pip install -r requirements.txt

Veritabanını oluşturun ve uygulamayı başlatın:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Tarayıcınızda http://127.0.0.1:8000 adresine giderek uygulamayı görüntüleyebilirsiniz.

Kullanım
Tarayıcınızda http://127.0.0.1:8000 adresine gidin.

Kursları görüntüleyin veya yeni kurs ekleyin.

Kursları düzenleyin veya silin.

Kurs detaylarına erişmek için kurs başlığına tıklayın.


Katkıda Bulunma
Bu projeyi fork edin.
Yeni bir branch oluşturun: git checkout -b yeni-ozellik
Değişikliklerinizi commit edin: git commit -am 'Yeni özellik eklendi'
Branch'inizi push edin: git push origin yeni-ozellik
Bir Pull Request (PR) açın.
