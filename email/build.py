#!/usr/bin/env python3
"""Builds email/portfolio-email.html, the HTML email version of the portfolio.

Edit the content below and run:  python3 email/build.py
Every style is inlined on the element, so the result survives Gmail.
"""
from pathlib import Path

SITE = "https://pavo1151.github.io/portfolio/"
IMG = SITE + "email/img/"

NAME = "עמית אוזן"
TAGLINE = "יצירה, חשיבה, טכנולוגיה ומה שביניהן."
LEDE = ("אני מפתח רעיונות, יוצר חזותית ובונה תהליכים וכלים שהופכים מחשבות "
        "למשהו שאפשר לראות, להבין, לחוות ולהשתמש בו.")
PREHEADER = ("תיק עבודות: הדמיות ואדריכלות, עיצוב פנים, אירועים, מיתוג, "
             "מוצרים דיגיטליים ואמנות.")

EMAIL = "pavone.id.il@gmail.com"
PHONE = "050-995-6660"
PHONE_HREF = "tel:0509956660"
AREA = "מרכז הארץ ובכל הארץ"
WEBSITE = ("האתר של PAVONE", "https://pavoneidil.wixstudio.com/my-site-15")
INSTAGRAM = [
    ("PAVONE · הדמיות ואדריכלות", "@pavone.arch", "https://www.instagram.com/pavone.arch/"),
    ("FORME · מיתוג וגרפיקה", "@forme_il", "https://www.instagram.com/forme_il/"),
]

ABOUT = [
    ("מי אני", "סקרן מטבעי.",
     "אני אוהב ללמוד, לחקור, ליצור ולחבר בין תחומים. לפעמים העבודה מתחילה בלקוח שמחפש פתרון, ולפעמים בשאלה שעוד לא ברור לאן תוביל."),
    ("איך אני חושב", "הדרך חשובה כמו התשובה.",
     "אני מפרק רעיונות, בוחן הנחות ומחפש קשרים שלא נראו בהתחלה. לפעמים אני מתחיל דווקא בניסיון להבין טוב יותר את השאלה."),
    ("איך אני פועל", "ממחשבה למשהו שאפשר לפגוש.",
     "לא כל רעיון צריך להפוך מיד לפרויקט גדול. לפעמים הדרך הטובה ביותר להבין אותו היא לבנות גרסה קטנה, לבחון אותה וללמוד ממנה."),
    ("איך אני מעביר ידע", "להבין, ואז לעזור למישהו אחר להבין.",
     "להבין משהו בעצמי זה שלב אחד. להפוך את ההבנה לנגישה לאדם אחר זה אתגר יצירתי בפני עצמו."),
]

TOPICS = ["אדריכלות והדמיות חוץ", "עיצוב והדמיות פנים", "אירועים",
          "מיתוג וקמפיינים", "מוצרים דיגיטליים", "אמנות ומחקר"]

STATS = [("43", "פרויקטים"), ("6", "תחומים"), ("167", "תמונות וסרטונים")]

HERO = ("hero-gindi.jpg", "משרדי גינדי החזקות", "עיצוב והדמיות פנים",
        "הדמיות פנים למשרדי החברה: קבלה, לאונג', בר ופינות ישיבה, יחד עם תוכנית ההעמדה.")

# rows of two: (image, title, field, text)
PAIRS = [
    [("mazor.jpg", "מזור", "אדריכלות · קנה מידה עירוני",
      "עיר שצומחת מתוך הנוף: שכונה, רחובות ירוקים, טיילת לאורך האגם ובתי אבן ליד הפארק."),
     ("terminal.jpg", "טרמינל אילת", "אדריכלות · מבני ציבור ותרבות",
      "הדמיות חוץ למבנה הטרמינל, לרחבת הכניסה ולחזית המסחרית.")],
    [("beit-asher.jpg", "בית אשר", "עיצוב פנים · בית",
      "הדמיית פנים לבית פרטי: מטבח, מבואה וחדר רחצה."),
     ("pardes.jpg", "חתונה בפרדס", "אירועים · תכנון אירוע",
      "תכנון אירוע בחוץ מהמגרש הריק ועד הערב עצמו: הבר, הלאונג', החופה והשולחנות.")],
]

BRANDS = [
    ("glitch.jpg", "Glitch Ice", "מוצר, אריזה וקמפיין"),
    ("gavish.jpg", "Gavish", "מסעדת המבורגרים"),
    ("lakerain.jpg", "Lakerain", "קוסמטיקה"),
]

ART = ("cosmos.jpg", "המיקרוקוסמוס כהשתקפות", "אמנות ומחקר · The Universe Within",
       "טיפת דם אחת שהתייבשה במשך שנה, נסדקה וקפאה בזמן. תחת המיקרוסקופ היא נראית כמו טופוגרפיה של פלנטה שלמה.")

# ---------------------------------------------------------------- palette
INK, MUTED, PAPER, CARD = "#14151b", "#535866", "#f1efea", "#ffffff"
NIGHT, ON_NIGHT, DIM = "#0b0c11", "#eef0f6", "#a9afbf"
COBALT, EMBER, LINE = "#2b3cff", "#ff5a1f", "#e4e1da"
FONT = "font-family:Heebo,Rubik,Arial,Helvetica,sans-serif;"


def kicker(text, color=EMBER):
    return (f'<p dir="rtl" style="margin:0 0 6px;{FONT}font-size:13px;line-height:18px;'
            f'font-weight:700;letter-spacing:.5px;color:{color};text-align:right;">{text}</p>')


def button(label, href, bg=COBALT, fg="#ffffff", border=None):
    border = border or bg
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="display:inline-table;">'
            f'<tr><td align="center" bgcolor="{bg}" style="background-color:{bg};border:2px solid {border};border-radius:999px;">'
            f'<a href="{href}" target="_blank" style="display:inline-block;padding:12px 26px;{FONT}'
            f'font-size:16px;line-height:20px;font-weight:700;color:{fg};text-decoration:none;border-radius:999px;">'
            f'{label}</a></td></tr></table>')


def section_title(k, title):
    return (f'<tr><td class="card px" dir="rtl" bgcolor="{CARD}" style="background-color:{CARD};padding:36px 32px 8px;text-align:right;">'
            f'{kicker(k)}'
            f'<h2 class="ink" dir="rtl" style="margin:0;{FONT}font-size:24px;line-height:30px;font-weight:800;color:{INK};text-align:right;">{title}</h2>'
            f'</td></tr>')


def work_cell(img, title, field, text):
    return (f'<a href="{SITE}" target="_blank" style="text-decoration:none;display:block;">'
            f'<img src="{IMG}{img}" width="264" alt="{title}" style="display:block;width:100%;max-width:100%;height:auto;border:0;border-radius:10px;"></a>'
            f'<p dir="rtl" style="margin:12px 0 2px;{FONT}font-size:12px;line-height:17px;font-weight:700;color:{COBALT};text-align:right;" class="cob">{field}</p>'
            f'<h3 dir="rtl" style="margin:0 0 4px;{FONT}font-size:18px;line-height:24px;font-weight:800;text-align:right;">'
            f'<a class="ink" href="{SITE}" target="_blank" style="color:{INK};text-decoration:none;">{title}</a></h3>'
            f'<p class="muted" dir="rtl" style="margin:0;{FONT}font-size:14px;line-height:21px;color:{MUTED};text-align:right;">{text}</p>')


def pair_row(pair):
    cols = ""
    for i, w in enumerate(pair):
        sep = '<!--[if mso]></td><td width="280" valign="top"><![endif]-->' if i else ""
        cols += (f'{sep}<div class="col" dir="rtl" style="display:inline-block;width:100%;max-width:280px;vertical-align:top;">'
                 f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
                 f'<td dir="rtl" style="padding:12px;text-align:right;">{work_cell(*w)}</td></tr></table></div>')
    return (f'<tr><td class="card" dir="rtl" bgcolor="{CARD}" style="background-color:{CARD};padding:4px 20px 0;font-size:0;line-height:0;text-align:center;">'
            f'<!--[if mso]><table role="presentation" width="560" cellpadding="0" cellspacing="0" border="0" dir="rtl"><tr><td width="280" valign="top"><![endif]-->'
            f'{cols}<!--[if mso]></td></tr></table><![endif]--></td></tr>')


def contact_row(label, value_html):
    return (f'<tr><td dir="rtl" width="120" valign="top" style="padding:11px 0;border-top:1px solid #2a2d3a;{FONT}font-size:13px;line-height:22px;color:{DIM};text-align:right;">{label}</td>'
            f'<td dir="rtl" valign="top" style="padding:11px 0;border-top:1px solid #2a2d3a;{FONT}font-size:16px;line-height:22px;font-weight:700;color:{ON_NIGHT};text-align:right;">{value_html}</td></tr>')


def link(text, href, ltr=False):
    d = ' dir="ltr" style="unicode-bidi:embed;' if ltr else ' style="'
    return f'<a href="{href}" target="_blank"{d}color:{ON_NIGHT};text-decoration:underline;">{text}</a>'


parts = []
add = parts.append

# ---- header
add(f'''<tr><td dir="rtl" bgcolor="{NIGHT}" style="background-color:{NIGHT};padding:22px 32px;border-radius:16px 16px 0 0;" class="px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="rtl"><tr>
<td dir="rtl" valign="middle" style="text-align:right;">
<a href="{SITE}" target="_blank" style="text-decoration:none;{FONT}font-size:18px;line-height:28px;font-weight:800;color:{ON_NIGHT};">
<img src="{IMG}mark.png" width="28" height="28" alt="" style="display:inline-block;vertical-align:middle;border:0;width:28px;height:28px;">&nbsp;&nbsp;{NAME}</a></td>
<td dir="rtl" valign="middle" style="text-align:left;">
<a href="{SITE}" target="_blank" style="{FONT}font-size:14px;line-height:28px;font-weight:700;color:{ON_NIGHT};text-decoration:underline;">תיק העבודות</a></td>
</tr></table></td></tr>''')

# ---- hero
add(f'''<tr><td dir="rtl" bgcolor="{NIGHT}" style="background-color:{NIGHT};padding:20px 32px 34px;text-align:right;" class="px">
<h1 dir="rtl" style="margin:0 0 10px;{FONT}font-size:44px;line-height:48px;font-weight:900;color:#ffffff;text-align:right;">{NAME}</h1>
<p dir="rtl" style="margin:0 0 16px;{FONT}font-size:20px;line-height:28px;font-weight:700;color:{EMBER};text-align:right;">{TAGLINE}</p>
<p dir="rtl" style="margin:0 0 24px;{FONT}font-size:16px;line-height:26px;color:{ON_NIGHT};text-align:right;">{LEDE}</p>
{button("לתיק העבודות המלא", SITE)}
</td></tr>
<tr><td bgcolor="{NIGHT}" style="background-color:{NIGHT};padding:0;font-size:0;line-height:0;">
<a href="{SITE}" target="_blank"><img src="{IMG}{HERO[0]}" width="600" alt="{HERO[1]}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>
<tr><td class="card px" dir="rtl" bgcolor="{CARD}" style="background-color:{CARD};padding:18px 32px 0;text-align:right;">
<p class="muted" dir="rtl" style="margin:0;{FONT}font-size:14px;line-height:21px;color:{MUTED};text-align:right;">
<strong class="ink" style="color:{INK};">{HERO[1]}</strong> · {HERO[2]}. {HERO[3]}</p></td></tr>''')

# ---- stats
cells = ""
for i, (n, t) in enumerate(STATS):
    b = f"border-right:1px solid {LINE};" if i else ""
    cells += (f'<td class="line" dir="rtl" width="33%" align="center" style="padding:4px 6px;{b}text-align:center;">'
              f'<p class="ink" style="margin:0;{FONT}font-size:30px;line-height:34px;font-weight:900;color:{INK};">{n}</p>'
              f'<p class="muted" style="margin:2px 0 0;{FONT}font-size:13px;line-height:18px;color:{MUTED};">{t}</p></td>')
add(f'<tr><td class="card px" bgcolor="{CARD}" style="background-color:{CARD};padding:28px 32px 0;">'
    f'<table class="line" role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="rtl" '
    f'style="border-top:1px solid {LINE};border-bottom:1px solid {LINE};"><tr><td colspan="3" style="height:16px;font-size:0;line-height:0;">&nbsp;</td></tr>'
    f'<tr>{cells}</tr><tr><td colspan="3" style="height:16px;font-size:0;line-height:0;">&nbsp;</td></tr></table></td></tr>')

# ---- about
add(section_title("קצת עליי", "ארבע יכולות שמובילות את כל מה שאני עושה"))
rows = ""
for i, (k, title, text) in enumerate(ABOUT):
    rows += (f'<tr><td dir="rtl" width="44" valign="top" style="padding:18px 0 0;{FONT}font-size:22px;line-height:28px;font-weight:900;color:{EMBER};text-align:right;">0{i + 1}</td>'
             f'<td dir="rtl" valign="top" style="padding:18px 0 0;text-align:right;">'
             f'<p class="muted" dir="rtl" style="margin:0;{FONT}font-size:13px;line-height:18px;font-weight:700;color:{MUTED};text-align:right;">{k}</p>'
             f'<h3 class="ink" dir="rtl" style="margin:2px 0 4px;{FONT}font-size:18px;line-height:25px;font-weight:800;color:{INK};text-align:right;">{title}</h3>'
             f'<p class="muted" dir="rtl" style="margin:0;{FONT}font-size:15px;line-height:24px;color:{MUTED};text-align:right;">{text}</p></td></tr>')
add(f'<tr><td class="card px" dir="rtl" bgcolor="{CARD}" style="background-color:{CARD};padding:0 32px;">'
    f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="rtl">{rows}</table></td></tr>')

# ---- fields
chips = "".join(
    f'<span class="chip" style="display:inline-block;margin:0 0 8px 8px;padding:6px 14px;border:1px solid {LINE};border-radius:999px;'
    f'{FONT}font-size:14px;line-height:20px;font-weight:700;color:{INK};background-color:{PAPER};">{t}</span>' for t in TOPICS)
add(f'<tr><td class="card px" dir="rtl" bgcolor="{CARD}" style="background-color:{CARD};padding:30px 32px 0;text-align:right;">'
    f'{kicker("תחומי עיסוק")}<div dir="rtl" style="text-align:right;padding-top:4px;">{chips}</div></td></tr>')

# ---- works
add(section_title("תיק עבודות", "עבודות נבחרות"))
add(f'<tr><td class="card" bgcolor="{CARD}" style="background-color:{CARD};height:8px;font-size:0;line-height:0;">&nbsp;</td></tr>')
for p in PAIRS:
    add(pair_row(p))

# ---- brands
BRAND_KICKER = kicker("מיתוג וקמפיינים", COBALT).replace("<p ", '<p class="cob" ', 1)
bcells = ""
for img, title, field in BRANDS:
    bcells += (f'<td dir="rtl" width="33.33%" valign="top" style="padding:0 6px;text-align:right;">'
               f'<a href="{SITE}" target="_blank" style="text-decoration:none;display:block;">'
               f'<img src="{IMG}{img}" width="172" alt="{title}" style="display:block;width:100%;max-width:100%;height:auto;border:0;border-radius:10px;"></a>'
               f'<h3 dir="rtl" style="margin:10px 0 0;{FONT}font-size:15px;line-height:21px;font-weight:800;text-align:right;">'
               f'<a class="ink" href="{SITE}" target="_blank" style="color:{INK};text-decoration:none;">{title}</a></h3>'
               f'<p class="muted" dir="rtl" style="margin:0;{FONT}font-size:13px;line-height:19px;color:{MUTED};text-align:right;">{field}</p></td>')
add(f'<tr><td class="card px" dir="rtl" bgcolor="{CARD}" style="background-color:{CARD};padding:26px 32px 0;text-align:right;">'
    f'{BRAND_KICKER}</td></tr>'
    f'<tr><td class="card pxb" bgcolor="{CARD}" style="background-color:{CARD};padding:6px 26px 0;">'
    f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="rtl"><tr>{bcells}</tr></table></td></tr>')

# ---- art
add(f'''<tr><td class="card px" bgcolor="{CARD}" style="background-color:{CARD};padding:32px 32px 0;">
<a href="{SITE}" target="_blank" style="text-decoration:none;display:block;">
<img src="{IMG}{ART[0]}" width="536" alt="{ART[1]}" style="display:block;width:100%;max-width:100%;height:auto;border:0;border-radius:10px;"></a>
<p class="cob" dir="rtl" style="margin:12px 0 2px;{FONT}font-size:12px;line-height:17px;font-weight:700;color:{COBALT};text-align:right;">{ART[2]}</p>
<h3 dir="rtl" style="margin:0 0 4px;{FONT}font-size:18px;line-height:24px;font-weight:800;text-align:right;"><a class="ink" href="{SITE}" target="_blank" style="color:{INK};text-decoration:none;">{ART[1]}</a></h3>
<p class="muted" dir="rtl" style="margin:0;{FONT}font-size:14px;line-height:21px;color:{MUTED};text-align:right;">{ART[3]}</p>
</td></tr>
<tr><td class="card px" dir="rtl" align="center" bgcolor="{CARD}" style="background-color:{CARD};padding:30px 32px 38px;text-align:center;">
{button("לכל הפרויקטים באתר", SITE)}</td></tr>''')

# ---- contact
crow = contact_row("אימייל", link(EMAIL, "mailto:" + EMAIL, ltr=True))
crow += contact_row("טלפון", link(PHONE, PHONE_HREF, ltr=True))
for label, handle, url in INSTAGRAM:
    crow += contact_row("Instagram", f'{link(handle, url, ltr=True)}<br><span style="font-size:13px;font-weight:400;color:{DIM};">{label}</span>')
crow += contact_row("אתר", link(WEBSITE[0], WEBSITE[1]))
crow += contact_row("אזור פעילות", AREA)
add(f'''<tr><td class="px" dir="rtl" bgcolor="{NIGHT}" style="background-color:{NIGHT};padding:36px 32px 34px;border-radius:0 0 16px 16px;text-align:right;">
<h2 dir="rtl" style="margin:0 0 20px;{FONT}font-size:28px;line-height:34px;font-weight:900;color:#ffffff;text-align:right;">יצירת קשר</h2>
<table role="presentation" cellpadding="0" cellspacing="0" border="0" dir="rtl"><tr>
<td style="padding:0 0 22px 10px;">{button("לכתוב לי", "mailto:" + EMAIL)}</td>
<td style="padding:0 0 22px;">{button("להתקשר", PHONE_HREF, bg=NIGHT, fg=ON_NIGHT, border="#5b6072")}</td>
</tr></table>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="rtl">{crow}</table>
</td></tr>''')

body = "\n".join(parts)

html = f'''<!DOCTYPE html>
<html lang="he" dir="rtl" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<title>{NAME} · תיק עבודות</title>
<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
<style>
/* Progressive enhancement only: every essential style is inline on the elements. */
:root {{ color-scheme: light dark; supported-color-schemes: light dark; }}
body {{ margin:0; padding:0; }}
img {{ -ms-interpolation-mode:bicubic; }}
a[x-apple-data-detectors] {{ color:inherit !important; text-decoration:none !important; }}
@media only screen and (max-width:620px) {{
  .px {{ padding-left:20px !important; padding-right:20px !important; }}
  .pxb {{ padding-left:14px !important; padding-right:14px !important; }}
  .col {{ max-width:100% !important; }}
  h1 {{ font-size:38px !important; line-height:42px !important; }}
}}
@media (prefers-color-scheme: dark) {{
  .paper {{ background-color:#050608 !important; }}
  .card {{ background-color:#14151b !important; }}
  .ink {{ color:#eef0f6 !important; }}
  .muted {{ color:#b4b9c6 !important; }}
  .cob {{ color:#8f9bff !important; }}
  .line {{ border-color:#2a2d3a !important; }}
  .chip {{ background-color:#1d1f29 !important; border-color:#2a2d3a !important; color:#eef0f6 !important; }}
}}
[data-ogsc] .ink {{ color:#eef0f6 !important; }}
[data-ogsc] .muted {{ color:#b4b9c6 !important; }}
[data-ogsc] .cob {{ color:#8f9bff !important; }}
[data-ogsb] .card {{ background-color:#14151b !important; }}
</style>
</head>
<body class="paper" dir="rtl" bgcolor="{PAPER}" style="margin:0;padding:0;background-color:{PAPER};-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;">
<div style="display:none;max-height:0;max-width:0;overflow:hidden;opacity:0;font-size:1px;line-height:1px;color:{PAPER};mso-hide:all;">{PREHEADER}</div>
<table class="paper" role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="rtl" bgcolor="{PAPER}" style="background-color:{PAPER};">
<tr><td align="center" style="padding:24px 10px;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="rtl" align="center" style="width:100%;max-width:600px;margin:0 auto;">
{body}
<tr><td dir="rtl" align="center" style="padding:18px 20px 6px;text-align:center;">
<p class="muted" dir="rtl" style="margin:0;{FONT}font-size:12px;line-height:18px;color:{MUTED};text-align:center;">{NAME} · {TAGLINE}</p>
</td></tr>
</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr>
</table>
</body>
</html>
'''

out = Path(__file__).with_name("portfolio-email.html")
out.write_text(html, encoding="utf-8")
print(out, len(html.encode()), "bytes")
