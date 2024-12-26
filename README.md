# OCR and Keyword Search Application

This is a web application that allows users to upload images and perform Optical Character Recognition (OCR) to extract text. Users can also search for specific keywords in the extracted text, with case-insensitive matching and highlighted results.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Application Locally](#running-the-application-locally)
- [Deployed Link](#deployed-link)
- [License](#license)

## Features

- Upload images for OCR.
- Support for English and Hindi languages.
- Keyword search with case-insensitive matching.
- Highlighting of found keywords in the extracted text.

## Requirements

To run this application, you need the following:

- Python 3.6 or higher
- `easyocr` library
- `gradio` library

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/ocr-keyword-search.git
   cd ocr-keyword-search

2. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv

3. **Activate the Virtual Environment:**

   *On Windows:*

   ```bash
   venv\Scripts\activate
   ```
   
   *On macOS/Linux:*

   ```bash
   source venv/bin/activate

4. **Install the Required Libraries:**

   Create a requirements.txt file in the project directory with the following content:

   ```bash
   gradio
   easyocr
   ```

   Then run:

   ```bash
   pip install -r requirements.txt

## Running the Application Locally

To run the application locally, use the following command:

```bash
python main.py
```
The application will be accessible at http://127.0.0.1:7860 in your web browser.

## Deployed Link

[Link To Live Deployment of Application](https://huggingface.co/spaces/ShubhamPaliwal/OCR_and_Keyword_Search_Application)

## License

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) License

[Link To License](https://github.com/ShubhamPaliwal03/OCR-and-Keyword-Search-Application/blob/main/LICENSE)
