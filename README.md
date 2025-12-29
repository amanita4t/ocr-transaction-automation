# ocr-transaction-automation


This project is a Python-based automation tool that extracts transaction details from images using OCR and stores validated results in Google Sheets.

It is designed to reduce manual data entry by automatically reading transaction receipts or screenshots, extracting key information, and saving it in a structured format.

## Features

- OCR-based text extraction using PaddleOCR
- Automatic parsing of transaction details (sender, receiver, amount, date, transaction ID)
- User authentication system (email & password validation)
- Google Sheets integration for persistent storage
- Duplicate transaction detection
- Modular and maintainable Python codebase

## Project Structure

src/
├── auth.py # User authentication & validation
├── sheets.py # Google Sheets operations
├── ocr_processor.py # OCR logic
├── extractor.py # Data extraction & parsing
├── validation.py # Data validation
└── main.py # Application entry point


## How It Works

1. User signs in or creates an account
2. An image containing transaction details is processed using OCR
3. Relevant fields are extracted from the recognized text
4. The transaction is validated and checked for duplicates
5. The data is saved into the user’s Google Sheet

## Installation

```bash
git clone https://github.com/your-username/ocr-transaction-automation.git
cd ocr-transaction-automation
pip install -r requirements.txt

```

## Configuration

Add your Google Service Account JSON file

Update Google Sheets URL in the configuration

Provide the image path to be processed

## Run the Application

python src/main.py

## Use Case

### This system can be used for:

  Financial record automation
  
  Transaction tracking
  
  Receipt processing
  
  Data extraction workflows

## Technologies Used

  Python
  
  PaddleOCR
  
  Google Sheets API
  
  Regex
  
  Automation workflows
