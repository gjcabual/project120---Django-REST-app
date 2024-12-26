# Secure Django REST Framework Applications

A secure communication system between two Django REST Framework applications implementing encryption middleware.

## Project Overview

This project demonstrates secure API development using Django REST Framework with a focus on data encryption between services. It consists of two applications that communicate securely by encrypting and decrypting data during transmission.

## Features

- Secure API endpoints with encryption/decryption middleware
- Message sending and receiving with encryption
- Database integration with Nhost (PostgreSQL)
- Hasura GraphQL integration
- Comprehensive security measures
- Real-time message encryption and decryption

## Technologies Used

- **Backend Framework:**

  - Python 3.x
  - Django
  - Django REST Framework

- **Database:**

  - Nhost (PostgreSQL)
  - Hasura GraphQL Engine

- **Security:**
  - Custom encryption middleware
  - Cryptography library

## Prerequisites

- Python 3.x
- pip (Python package manager)
- PostgreSQL
- Git

## Required Packages

```
django
djangorestframework
django-cors-headers
cryptography
python-decouple
psycopg
psycopg2
requests
```

## Installation

1. Clone the repository:

   ```bash
   git clone [repository-url]
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

## Running the Application

1. Start the sender application (Port 8000):

   ```bash
   python manage.py runserver 8000
   ```

2. Start the receiver application (Different port):
   ```bash
   python manage.py runserver 8001
   ```

### Message Flow

1. Sender inputs name and message at `127.0.0.1:8000`
2. Message is encrypted and stored in database
3. Receiver at `127.0.0.1:8001/receive` can:
   - View encrypted messages
   - Decrypt messages for reading
   - Refresh to get new messages
   - Clear the message display

## Project Structure

```
myproject/
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── message_form.html
│   │   ├── receive.html
│   │   └── sendreceive_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── encryption.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
├── manage.py
└── requirements.txt
```

## Database Access

To verify messages/data in the database:

1. Access the Hasura Console:

   - URL: https://vvdqsgxhsloctbehbapj.hasura.eu-west-2.nhost.run/console/login
   - Admin Secret Key: 44;pS4'o0pky3ZFqA%MdVp2,r33a&l=q

   ![Hasura Login](https://drive.google.com/uc?export=view&id=13PgixcmJeBolN6sp61B6qhFkSOtMWF10)

2. Navigate to Data:

   1. Click "DATA" in the navigation bar

      ![Click Data](https://drive.google.com/uc?export=view&id=1lW-pR9Q5yv6gIdQ1ff9KpnrNDAmS_oGX)

   2. Select "public" schema

      ![Select Schema](https://drive.google.com/uc?export=view&id=1fBN5IzWX25ySLB1tp8WDo7oQdG03suT3)

   3. Select "myapp_message" table

      ![Select Table](https://drive.google.com/uc?export=view&id=1yfZG3dki_uTkr6Av1gL9cDMbOormFqgQ)

   4. View message data in the table

      ![View Data](https://drive.google.com/uc?export=view&id=1wYyrRAJo7elUU7-kGdiHob9Y-bC9PXoG)

   > **Note:** To view the latest messages without being logged out, click "Select rows" in the table view. This refreshes the data without reloading the entire page, which would otherwise log you out.

   ![Get Latest Message](https://drive.google.com/uc?export=view&id=1YBKV3W_xtPCHhrS8_SQQR9hlZCcezT4K)

## API Documentation

### Sender Application (Port 8000)

#### Send Message Endpoint

- **URL:** `/send/`
- **Method:** POST
- **Description:** Sends an encrypted message
- **Fields:**
  - Sender Name
  - Message
- **Process:**
  1. Message is encrypted using custom encryption
  2. Encrypted message is stored in Nhost database
  3. Message is sent to receiver

### Receiver Application (Port 8001)

#### Receive Message Endpoint

- **URL:** `/receive/`
- **Method:** GET
- **Description:** Receives and displays encrypted messages
- **Features:**
  - Refresh: Fetches latest messages from database
  - Decrypt Message: Decrypts selected message for viewing
  - Clear: Clears the message input field

## Security Features

- Data encryption in transit
- Secure key management
- Request/Response encryption middleware
- Database security measures

## Contributors

**GROUP 3:**

- Eisan Carlos Atamosa
- Michelle Malto
- Guilbert Jan Cabual

---

IT 120 - INTEGRATIVE PROGRAMMING TECHNOLOGIES 2
FINAL PROJECT - Django REST Framework Applications with Security Features
