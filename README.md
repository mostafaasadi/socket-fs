# socket-fs
این پروژه یک شبه‌پیاده‌سازی ساده از پروتکل FTP است که در قالب یک نرم‌افزار سوکت با پایتون نوشته شده است. این نرم‌افزار به شما این امکان را می‌دهد تا فایل‌های خود را دانلود، آپلود و حذف کنید. لازم به ذکر است که این برنامه تنها مشابه FTP عمل می‌کند و FTP نیست.

![screenshot](https://github.com/mostafaasadi/socket-fs/assets/12208050/d02a63f0-29c7-4901-9525-a76c4d1f87f8)


## راه‌اندازی
با اجرای دستورات زیر، برنامه را راه‌اندازی کنید:
```
git clone https://github.com/mostafaasadi/socket-fs/
cd socket-fs
# create and active virtual envirement
pip install -r requirements.txt
```

## تنظیم و اجرا
برای تغییر پورت، بافرسایز و دایرکتوری‌های کلاینت و سرور، در فایل‌های `server.py` و `client.py` قسمت `__main__` بررسی و تغییر دهید.

برای اجرا هر دو فایل `server.py` و `client.py` را اجرا کنید.
```
python server.py
python client.py
```

## مجوز
این پروژه تحت مجوز GPL-3.0 منتشر شده است. برای اطلاعات بیشتر در مورد مجوز، فایل LICENSE را مشاهده کنید.
