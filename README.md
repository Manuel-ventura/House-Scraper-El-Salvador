# 🏠 House Scraper El Salvador

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scrapy](https://img.shields.io/badge/Scrapy-2.5%2B-brightgreen)

Welcome to the **House Scraper El Salvador** project! This is a web scraping project built using Scrapy to extract real estate listings from Encuentra24. The project focuses on extracting details such as location, title, description, price, and property specifications from the website to analyze real estate trends in El Salvador.

## 🚀 Features

- Extracts detailed real estate listings
- Gathers property specifications: location, title, description, price, size, bedrooms, parking spots, and bathrooms
- Follows pagination to scrape multiple pages of listings

## 🌐 Website

We are scraping data from [Encuentra24](https://www.encuentra24.com/el-salvador-es/bienes-raices-venta-de-propiedades-casas?q=f_currency.USD%7Cwithcat.bienes-raices-venta-de-propiedades-casas,bienes-raices-venta-de-propiedades-apartamentos).

## 📂 Project Structure

```
House-Scraper-El-Salvador/
├── env/                # Virtual environment folder (not included in the repo)
├── pricescraper/       # Scrapy project folder
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── pricespider.py
├── scrapy.cfg          # Scrapy configuration file
└── .gitignore          # Git ignore file
```

## 🛠️ Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Manuel-ventura/House-Scraper-El-Salvador.git
    cd House-Scraper-El-Salvador
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the scraper**:
    ```bash
    scrapy crawl pricespider
    ```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 📧 Contact

Feel free to reach out for any questions or suggestions!

---

Happy Scraping! 🕷️✨
