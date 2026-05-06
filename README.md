# Solution_Tech.AI — Django Portfolio Website

## 🚀 Quick Start

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install django

# 3. Apply migrations
python manage.py migrate

# 4. Create superuser (for admin panel)
python manage.py createsuperuser

# 5. Run the server
python manage.py runserver
```

Open: http://127.0.0.1:8000

## 📄 Pages
| URL | Description |
|-----|-------------|
| `/` | Home — Hero, Services, Templates, Portfolio, About, Testimonials, Contact |
| `/contact/` | Dedicated Contact page with FAQ |
| `/templates/web/` | All web templates with filter |
| `/templates/mobile/` | All mobile app templates with filter |
| `/admin/` | Django admin — view contact queries |

## 🔑 Admin Panel
- URL: http://127.0.0.1:8000/admin/
- Manage all contact queries submitted via the forms

## ✏️ Customise Your Brand
1. Open `core/templates/core/base.html`
2. Replace `Solution_Tech.AI` with your brand name
3. Update phone: `+91 9997603233`
4. Update email: `hello@solutiontech.ai`
5. Update WhatsApp link: `https://wa.me/919997603233`

## 🎨 Features
- ⚡ Animated hero with typing effect & counter animations
- 🤖 Floating WhatsApp chat widget with bot responses
- 📞 Click-to-call floating button
- 🌗 Full dark-mode design (Orbitron + Syne + DM Sans)
- 📱 Fully mobile-responsive
- 🔍 Template filtering by category
- 📬 Contact form saves to database
- 🛡️ Django admin to view all queries
- ✨ Scroll-reveal animations throughout
- 🖱️ Cursor glow effect
