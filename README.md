# FurCry

FurCry is a Python web application that streamlines the process of spreading awareness about lost and found pets. The app lets a user paste a URL of a webpage containing information about a missing pet and then extracts and displays that information in a neat, shareable format so it can be quickly posted to multiple platforms.

## Key Features

- Paste a URL to an online posting and quickly extract pet details (name, species, breed, age, color, photos, location, contact info, description).
- Present the extracted information in a clean, organized layout for easy copying/resharing.
- Generate shareable cards or text snippets suitable for social platforms.
- Modular pages for quick navigation: home, developer info, and help for pets.
- Scraper utilities in `scraping/` to parse common posting formats.

## Repository Structure

- `index.py` — application entrypoint (web UI runner)
- `requirements.txt` — Python dependencies
- `pages/` — page modules: `home.py`, `developer.py`, `help_pets.py`
- `scraping/` — scraping scripts: `lmp_scraper.py` (scraping/parsing logic)
- `static/` — static assets (images, CSS, JS)
- `README.md` — this file

## Installation

Requirements: Python 3.9+ (Windows example shown).

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

If you plan to run the app with Streamlit, install packages from `requirements.txt` and run Streamlit (if present in dependencies):

```powershell
streamlit run index.py
```

## Usage

1. Open the app in your browser (the app will show the `home` page).
2. Paste the URL of an online posting containing lost/found pet information into the provided input field.
3. The app will fetch and parse the URL (using the scraper in `scraping/lmp_scraper.py`) and display extracted fields:
   - Pet details (species, breed, color, age, sex)
   - Photos (if available)
   - Location and date
   - Reporter/contact information
   - Description and additional notes
4. Review and edit fields if necessary, then copy or download a shareable card/text snippet for posting to social media or local platforms.

Notes:
- The scraper handles common posting formats but may require tweaks to support additional websites. See `scraping/lmp_scraper.py` for parsing logic.
- If the posted URL blocks scraping or requires special headers, update the scraper to include appropriate request headers or browser emulation.

## Development

- Add new site parsers in `scraping/` as needed.
- Add or modify page views under `pages/`.
- Keep dependencies up to date in `requirements.txt` using `pip freeze > requirements.txt`.

## Contributing

1. Fork the repository and create a feature branch.
2. Add tests or manual verification steps for new scrapers.
3. Open a pull request with a clear description of changes.