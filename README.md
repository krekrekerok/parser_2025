# Mashina.kg Web Scraper

This project scrapes car listings from the Mashina.kg website and saves the links to a JSON file.

## Features

- Scrapes multiple pages of car listings
- Extracts links to individual car pages
- Saves all links to a JSON file
- Shows progress bar during scraping

## Requirements

- Python 3.10+
- Internet connection

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/krekrekerok/parser_2025.git
cd parser_2025
```

### 2. Create a virtual environment

#### For macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Make sure your virtual environment is activated
2. Run the script:

```bash
python get_links.py
```

3. Enter the number of pages you want to scrape when prompted
4. The script will save all car listing links to `links.json` in the project directory

## Project Structure

```
mashina-kg-scraper/
├── get_links.py          # Main script
├── requirements.txt    # Project dependencies
├── links.json          # Output file (generated after running)
└── README.md           # This file
```

## Dependencies

- requests - For making HTTP requests
- beautifulsoup4 - For HTML parsing
- tqdm - For progress bars

## License

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request
