# Reservation-tools

A small collection of browser-based utility tools built for travel and reservation workflows.

## Project Overview

This repository contains several standalone HTML/JavaScript calculators for travel-related support tasks.

## Authority

Developed and maintained by the repository owner as a practical travel and reservation toolkit. The tools are intended for personal use, demonstration, and quick utility workflows.

## Included Tools

- **Main Dashboard**: `index.html`
  - A polished landing page that showcases the available tools.
- **Home Page**: `home.html`
  - A styled welcome page with a hero section and tool descriptions.
- **Age Calculator**: `Age-Calculator/age.html`
  - Calculates exact age in years, months, and days.
  - Supports a custom reference date and displays total months, weeks, and days.
- **Fare Calculator**: `Fare-Calculator/fare.html`
  - Computes AIT, IATA commission, and net fare based on gross fare and base fare.
  - Includes optional markup and a ticket information generator modal.
- **Layover Calculator**: `Layover/Layover.html`
  - Computes layover duration from arrival and departure flight times.
  - Accepts next-day values using `+1` notation and classifies connection status.

## How to Use

### Browser Tools

1. Open the repository folder in your file manager.
2. Launch any HTML file in your browser by double-clicking it or opening it from the browser.
3. Recommended starting points:
   - `index.html` for the tool dashboard
   - `home.html` for a welcome/landing page

## File Structure

- `index.html` - Main dashboard page
- `home.html` - Project landing page
- `Commission.jpeg` - Reference image used by the fare calculator
- `Age-Calculator/`
  - `age.html`
  - `script.js`
  - `style.css`
- `Fare-Calculator/`
  - `fare.html`
  - `script.js`
  - `style.css`
- `Layover/`
  - `Layover.html`
  - `script.js`
  - `style.css`

## Notes

- The tools are built using vanilla HTML, CSS, and JavaScript.
- The fare calculator uses CDN-based Font Awesome icons in `Fare-Calculator/fare.html`.
- The layover calculator supports `HHMM` and next-day time entry with `+1`.

## Improvements

Potential future enhancements:
- Add form validation feedback across all tools.
- Add a shared navigation menu between tools.
- Convert the dashboard into a fully interactive app with direct tool links.

## Copyright

© 2026 Reservation-tools. All rights reserved.
