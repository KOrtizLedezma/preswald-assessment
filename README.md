# Video Game Sales Dashboard — Preswald Assessment

This is a data exploration web app built using [Preswald](https://preswald.com), designed to fulfill the technical requirements of the assessment prompt. It visualizes video game sales data across different platforms and regions using interactive components, filters, and visualizations.

## Assessment Requirements

### 1. Environment Setup
- App built using `preswald` CLI and Python.
- Runs on local development server via `preswald run`.
- Compatible with Google Chrome.

### 2. Dataset Integration
- Dataset used: `vgsales.csv` (video game sales).
- Placed in the `data/` folder.
- Connected via `preswald.toml` under the `[data]` section using:
  ```toml
  [data]
  my_dataset = "data/vgsales.csv"
  ```
  
### 3. App Functionality (hello.py)
- Data Loading: Loaded using `pandas.read_csv()` from the local dataset.
- Data Manipulation:
  - Grouped and summed sales by platform.
  - Applied filters to NA_Sales for interactivity.
- Interactive UI:
  - Includes headings, data tables, and dynamic controls (e.g., slider).
  - Filtered view changes in real time based on user input.
- Visualizations:
  - A bar chart using Plotly to show Global Sales by Platform.
  - Clean layout with emphasis on data readability.

### 4. Export & Deployment
- App was exported as a static HTML site using:
```bash
    preswald export --format html
```
- All assets and layout are preserved in the `export/` folder for distribution or deployment.

## Author
Kenet Ortiz <br/>
Built as part of a technical assessment for Preswald.