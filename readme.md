# digikala_web_crawler

## درباره پروژه
پروژه شامل اسپایدر هایی برای به دست اوردن دیتا از بخش های مختلف دیجی کالا است

## راه اندازی 

### با استفاده از makefile
بعد از کلون کردن پروژه اگر از سیستم عامل های یونیکس بیس مثل لینوکس و مک او اس استفاده می کنید نصب ابزار makeو اجرای دستور از پروژه استفاده کنید
```bash
make
```
یا
```bash
make after_clone
```

### به صورت دستی
در صورتی که علاقه مندید تا خود تمام مراحل لازم را انجام دهید یا از ویندوز استفاده میکنید مراحل زیر را دنبال کنید

این دستور را اجرا کنید تا محیط مجازی شما ساخته شود
```bash
virtualenv venv
```
در صورتی که از لینوکس یا مک او اس استفاده میکنید دستور زیر را اجرا کنید
```bash
source venv/bin/activate
```
در غیر این صورت اگر از ویندوز استفاده میکنید دستور زیر را اجرا کنید
```bash
./venv/bin/activate
```
سپس برای نصب لایبرری های مورد نیاز دستور زیر را اجرا کنید
```bash
pip install -r requirements.txt
```

## اجرای اسپایدر ها
در نهایت برای اجرای هر اسپایدر میتوانید از دستور زیر استفاده کنید خروجی در کنسول نمایش داده می شود
```bash
scrapy runspider spidername
```
برای ذخیره خروجی در فایل از دستور زیر استفاده کنید
```bash
scrapy runspider spidername -o filename.jl
```