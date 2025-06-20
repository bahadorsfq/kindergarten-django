document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('.sidebar .menu a');
    const contentBox = document.querySelector('.content-box');

    links.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();

            // حذف کلاس active از همه لینک‌ها
            links.forEach(l => l.classList.remove('active'));
            // اضافه کردن کلاس active به لینک انتخاب‌شده
            this.classList.add('active');

            // تغییر محتوای content-box بر اساس لینک کلیک‌شده
            const text = this.textContent.trim();
            switch (text) {
                case '👤 پروفایل':
                    contentBox.innerHTML = `<h2>پروفایل کودک</h2><p>نام: علی کوچولو<br>سن: ۵ سال</p>`;
                    break;
                case '📈 نمودار پیشرفت':
                    contentBox.innerHTML = `<h2>نمودار پیشرفت</h2><p>در حال بارگذاری نمودار...</p>`;
                    break;
                case '🖼️ گزارش تصویری':
                    contentBox.innerHTML = `<h2>گزارش تصویری</h2><p>گالری تصاویر فعالیت‌های اخیر کودک.</p>`;
                    break;
                case '🍽️ برنامه غذایی':
                    contentBox.innerHTML = `<h2>برنامه غذایی</h2><ul><li>صبحانه: نان و پنیر</li><li>نهار: خورشت سبزی</li></ul>`;
                    break;
                case '🎨 موضوع هفته':
                    contentBox.innerHTML = `<h2>موضوع هفته</h2><p>رنگ‌ها و شکل‌ها 🌈</p>`;
                    break;
                case '💰 مالی':
                    contentBox.innerHTML = `<h2>وضعیت مالی</h2><p>مبلغ پرداختی: ۲,۰۰۰,۰۰۰ ریال</p>`;
                    break;
                case '🚪 خروج':
                    contentBox.innerHTML = `<h2>خروج</h2><p>شما از حساب خود خارج شدید.</p>`;
                    break;
                default:
                    contentBox.innerHTML = `<p>برای مشاهده اطلاعات، یکی از گزینه‌های سمت راست را انتخاب کنید.</p>`;
            }
        });
    });
});
document.querySelectorAll('.submenu li').forEach(item => {
    item.addEventListener('click', function (e) {
        e.stopPropagation(); // جلوگیری از اجرای رویداد والد
        const tab = this.getAttribute('data-tab');
        const contentBox = document.querySelector('.content-box');

        // می‌تونی اینجا متن‌ها رو بر اساس tab سفارشی کنی
        const messages = {
            yoga: "محتوای مربوط به یوگا برای رشد جسمی کودکان.",
            language: "زبان عمومی برای تقویت مهارت‌های ارتباطی.",
            gardening: "باغبانی برای آشنایی با طبیعت.",
            cooking: "آشپزی برای یادگیری مهارت‌های زندگی.",
            storytelling: "قصه‌خوانی برای تقویت تخیل.",
            singing_hymns: "سرود خوانی برای تقویت آواز",
            rain_of_thoughts: "بارش افکار برای ایده پردازی",
            game: "بازی های گروهی ",
            paint: "مهارت های نقاشی",
            social_etiquette: "آداب اجتماعی برای تقویت دوستیابی وارتباطات",
            legality: "قانونمندی و احترام به حقوق دیگران",
            threadable: "درست کردن گردنبند و تسبیح و دستبند و ...",
            science_concepts: "مفاهیم علوم برای ذهن های کنجکاو",
            pottery_workshop: "سفالگری ",
            mathematical_concepts: "آموزش مفاهیم ریاضی",
            printing_workshop: "کارگاه چاپ",
            manual_work: "کاردستی ها",
            creative_display: "نمایش های خلاقانه،تئاتر و...",
        };

        const content = messages[tab] || `شما گزینه «${this.textContent}» را انتخاب کردید.`;
        contentBox.innerHTML = `<p>${content}</p>`;
    });
});

