# God Goals Glory

<div align="center">

**A Modern Django E-commerce Platform**

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-5.1.6-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Deployment](#deployment) • [Contributing](#contributing) • [License](#license)

</div>

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 About

**God Goals Glory** (also known as "BeingThatGuy") is a full-featured Django-based e-commerce platform designed for managing products, orders, reviews, testimonials, and user accounts. The platform includes both customer-facing features and staff management capabilities.

This project provides a complete solution for online retail operations with features like product management, order processing, user authentication, waitlist management, and comprehensive admin controls.

---

## ✨ Features

### Customer Features
- 🛒 **Product Catalog** - Browse products with detailed descriptions, images, and pricing
- 📦 **Order Management** - Complete order processing with multiple size options
- ⭐ **Reviews & Ratings** - Rate and review products (1-5 stars)
- 💬 **Testimonials** - Share experiences with product images
- 👤 **User Accounts** - Custom user profiles with email authentication
- 📧 **Waitlist** - Join product waitlists with automated email notifications
- 📱 **Responsive Design** - Mobile-friendly interface

### Staff Features
- 👥 **Staff Dashboard** - Dedicated staff management interface
- 📊 **Order Processing** - Track and update order stages (Pending, Ready, Delivered)
- 📦 **Inventory Management** - Manage product availability and quantities
- 📨 **Email Templates** - Create and manage waitlist email templates
- 🔐 **Role-based Access** - Separate staff and customer permissions

### Technical Features
- 🔒 **Secure Authentication** - Django's built-in authentication with custom user model
- 📸 **Media Management** - Support for multiple product and testimonial images
- 🌐 **CORS Support** - Cross-Origin Resource Sharing configuration
- 📧 **Email Integration** - SMTP email backend for notifications
- 🐳 **Docker Support** - Containerized deployment ready
- 🔄 **Live Reload** - Browser auto-reload during development

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 5.1.6
- **Language:** Python 3.11+
- **Database:** SQLite (development), PostgreSQL-ready
- **WSGI Server:** Gunicorn

### Key Dependencies
- **django-phonenumber-field** - Phone number validation
- **django-widget-tweaks** - Enhanced form rendering
- **django-cors-headers** - CORS handling
- **Pillow** - Image processing
- **phonenumbers** - International phone number handling

### Deployment
- **Web Server:** Gunicorn
- **Containerization:** Docker
- **Service Management:** Systemd

---

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Virtual environment (recommended)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/gcl140/god.goals.glory.git
   cd god.goals.glory
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requrements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

---

## ⚙️ Configuration

### Environment Variables

For production deployment, configure the following settings in `god_goals/settings.py`:

```python
# Security
SECRET_KEY = 'your-secret-key-here'
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Database (example for PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Email Configuration
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-app-password'

# CORS
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
]
```

### Media and Static Files

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

## 🚀 Usage

### Customer Workflow

1. **Browse Products** - View available products with images and details
2. **Add to Order** - Select size and quantity
3. **Place Order** - Provide delivery address and payment method
4. **Track Order** - Monitor order status (Pending → Ready → Delivered)
5. **Review Products** - Rate and review purchased products

### Staff Workflow

1. **Access Staff Dashboard** - Navigate to `/staff/`
2. **Manage Products** - Add, edit, or remove products
3. **Process Orders** - Update order stages and manage fulfillment
4. **Handle Waitlist** - Send emails to waitlist users
5. **View Analytics** - Monitor sales and inventory

### Admin Panel

Access the Django admin at `/admin/` to:
- Manage users and permissions
- Configure products and inventory
- Review orders and transactions
- Moderate reviews and testimonials

---

## 🐳 Deployment

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t god-goals-glory .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 god-goals-glory
   ```

### Systemd Service

The project includes systemd service files for production deployment:

- `god_goals.service` - Main application service
- `BeingThatGuy.service` - Alternative service configuration

**Install and start the service:**
```bash
sudo cp god_goals.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable god_goals
sudo systemctl start god_goals
```

### Production Checklist

- [ ] Set `DEBUG = False` in settings
- [ ] Configure proper `SECRET_KEY`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Configure production database (PostgreSQL recommended)
- [ ] Set up static file serving (Nginx/Apache)
- [ ] Configure HTTPS/SSL certificates
- [ ] Set up proper email backend
- [ ] Configure CORS for production domains
- [ ] Set up backup strategy
- [ ] Configure logging and monitoring

---

## 📁 Project Structure

```
god.goals.glory/
├── god_goals/              # Main project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL configuration
│   ├── wsgi.py             # WSGI application
│   └── asgi.py             # ASGI application
├── yuzzaz/                 # Main customer-facing app
│   ├── models.py           # Product, Order, Review, Testimonial models
│   ├── views.py            # Customer views
│   ├── urls.py             # Customer URL routes
│   ├── forms.py            # Customer forms
│   └── templates/          # Customer templates
├── staff/                  # Staff management app
│   ├── models.py           # Staff-specific models
│   ├── views.py            # Staff views
│   ├── urls.py             # Staff URL routes
│   └── templates/          # Staff templates
├── media/                  # User-uploaded files
├── static/                 # Static files (CSS, JS, images)
├── manage.py               # Django management script
├── Dockerfile              # Docker configuration
├── requrements.txt         # Python dependencies
└── README.md               # This file
```

---

## 🔌 API Endpoints

### Public Endpoints
- `/` - Home page
- `/products/` - Product listing
- `/product/<id>/` - Product detail
- `/login/` - User login
- `/register/` - User registration
- `/logout/` - User logout

### Customer Endpoints (Authentication Required)
- `/dashboard/` - User dashboard
- `/orders/` - Order history
- `/order/create/` - Create new order
- `/reviews/` - User reviews
- `/testimonials/` - User testimonials

### Staff Endpoints (Staff Permission Required)
- `/staff/` - Staff dashboard
- `/staff/orders/` - Order management
- `/staff/products/` - Product management
- `/staff/waitlist/` - Waitlist management

### Admin Endpoint
- `/admin/` - Django admin panel

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Gift Christian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👤 Contact

**Gift Christian** - Project Maintainer

- Website: [beingthatguy.com](https://beingthatguy.com)
- Email: gftinity01@gmail.com
- GitHub: [@gcl140](https://github.com/gcl140)

---

## 🙏 Acknowledgments

- Django Software Foundation for the excellent web framework
- All contributors who have helped with this project
- The open-source community for various packages used in this project

---

<div align="center">

**Made with ❤️ using Django**

If you found this project helpful, please consider giving it a ⭐️

</div>
