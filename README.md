# Application Mentor - v1.0

Application Mentor — bu ilm yo'lidagilar uchun grant, stipendiya, stajirovka, almashuv va universitetga qabul hujjatlarini ko'rib chiqish uchun mo'ljallangan AI-agent skilli. U hujjat loyihasini tanlov komissiyasining nuqtai nazaridan tekshiradi va qaysi joylarda umumiy, dalilsiz, nomuvofiq yoki maqsad qilingan dastur talablariga mos kelmasligini aniqlaydi.

## Nimalarni ko'rib chiqadi

- CV va rezume
- motivatsion va qoplama xatlari (motivation va cover letters)
- shaxsiy bayonotlar va ariza insholari
- tavsiyanoma xatlari
- o'qish rejasi va ilmiy takliflar (study plans va research proposals)
- ariza va intervyu savollariga berilgan javoblar
- o'zbek stipendiya hujjatlari: tavsiyanoma, tavsifnoma, taqriznoma va obyektivka
- to'lov asosida tashkil etilgan dasturlarning asosiy qonuniyligi (basic legitimacy)

## Asosiy tamoyillar

- So'z chegaralari, talab qilingan bo'limlar, format, sanalar, imzolar va ilovalarni tekshiring — avval uslubni baholashdan oldin ushbu tekshiruvlarni bajaring.
- Fikrlarni maqsad qilingan dasturga va talabadan kelgan hujjatning aniq qatorlariga bog'lang.
- Dalilsiz da'volarni dalilga asoslangan bayonotlarga aylantiring.
- Talabaning ovozini saqlang.
- Hech qachon yutuqlar, ballar, sanalar, ism yoki raqamli natijalarni ixtiro qilmang.
- Zarur faktlar yetishmasa, `[YOZING: ...]` joyboshlovchisidan foydalaning.
- Talaba yozmagan to'liq topshiriq yoki arizani yaratmang.

## Tuzilishi

```text
application-mentor/
├── SKILL.md
├── references/
│   ├── application-questions.md
│   ├── cv-and-resume.md
│   ├── motivation-and-cover-letters.md
│   ├── personal-statement-and-essays.md
│   ├── programs-and-requirements.md
│   ├── prose-and-authenticity.md
│   ├── recommendation-letters.md
│   ├── study-plans-and-research.md
│   └── uzbek-scholarship-documents.md
└── scripts/
    └── read_document.py
```

## Claude Code-ga o'rnatish

`application-mentor` papkasini Claude Code skills katalogiga joylashtiring:

```bash
mkdir -p ~/.claude/skills
cp -R application-mentor ~/.claude/skills/
```

O'rnatgandan so'ng yangi suhbatni boshlang, shunda Claude Code skillni aniqlaydi.

Misol so'rov:

```text
Motivatsion xatimni ko'rib bering. DAAD dasturiga topshiryapman,
500 so'z limit bor.
```

## Hujjat yordamchisi

Birgalikda berilgan skript qo'llab-quvvatlanadigan ariza hujjatlaridan matn va foydali statistika chiqaradi:

```bash
python3 scripts/read_document.py "path/to/document.docx"
python3 scripts/read_document.py "path/to/document.docx" --stats-only
```

U macOS `textutil` utilitasidan `.docx`, `.doc`, `.rtf` va shunga o'xshash formatlar uchun foydalanadi. `.pptx`, `.xlsx`, `.txt` va `.md` fayllarni Pythonning standart kutubxonasi orqali qayta ishlaydi. CV va boshqa formatlangan hujjatlar uchun sahifa tuzilishi muhim bo'lgani sababli PDFlarni mezbon AI vositasida bevosita ko'rib chiqing.

## Litsenziya — faqat tijorat bo'lmagan foydalanish uchun

Majburiy bildirish: Mualliflik huquqi 2026 Feruzbek Baqoyev

Ushbu loyiha [PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0.txt) ostida ommaga taqdim etilgan. Uni ishlatish, o'zgartirish yoki tarqatish orqali siz ushbu havolada berilgan litsenziya shartlariga rozilik bildirasiz.

**Ushbu skill, uning ko'rsatmalari, referenslari yoki skriptini tijorat komponenti sifatida ishlatmang.** Mualliflik huquqi egasidan alohida yozma rozilik bo'lmasa, uni sotish, qayta sotish, pullik mahsulot yoki obuna ichiga kiritish, tijorat xizmati yoki SaaS mahsulotiga integratsiya qilish, yoki pullik qabul, konsultatsiya yoki trening taklifida ishlatish taqiqlanadi.

Shaxsiy o'qish, tadqiqot, tajriba va ta'lim, xayriya, jamoat-tadqiqot, sog'liqni saqlash, atrof-muhit va hukumat muassasalari tomonidan litsenziyada belgilangan chegaralar doirasida foydalanishga ruxsat beriladi.

Tijorat maqsadidagi foydalanish cheklanganligi sababli, texnik jihatdan bu loyiha OSI tomonidan tasdiqlangan ochiq manba emas, balki "manba mavjud" (source-available) loyiha hisoblanadi. OSI tomonidan tasdiqlangan ochiq litsenziyalar tijorat foydalanishga ruxsat berishi kerak.

## Maxfiylik va aniqlik

- Talabalar arizalarini yoki shaxsiy ma'lumotlarni ommaviy muammolarda e'lon qilmang.
- Muammo haqida xabar berishda ixtiyoriy yoki to'liq anonimlashtirilgan misollardan foydalaning.
- Muddati, to'lovlar, stipendiya miqdori, GPA chegaralari, viza qoidalari, reytinglar va dastur talablar o'zgarishi mumkin. Ularni rasmiy yangilangan sahifalarda tekshiring.
- Ushbu loyiha hech qanday universitet, stipendiya, tashkilot yoki hukumat idorasi bilan bog'liq emas.
- Skill tomonidan berilgan fikrlar qabul, moliyalashtirish yoki viza tasdiqini kafolatlamaydi.
