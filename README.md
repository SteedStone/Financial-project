# Financial Calculator - Option Premium & FTP Rates

A GUI-based financial calculator built with Python and CustomTkinter for computing option premiums and FTP (Funds Transfer Pricing) rates for mortgage products.

## Overview

This application provides a comprehensive tool for financial calculations related to mortgage pricing and option premiums. It features a modern dark-themed interface and supports various mortgage products with different repricing frequencies.

## Features

- **Interactive GUI**: Modern dark-themed interface built with CustomTkinter
- **Mortgage Calculations**: Support for fixed and floating rate mortgages
- **Multiple Product Types**: 
  - Fixed rate mortgages (5Y-30Y)
  - Floating rate mortgages with various repricing frequencies (1/1/1, 5/5/5, 10/5/5, 20/5/5)
- **Excel Integration**: Import financial data from Excel files (BBG rates)
- **PDF Generation**: Export calculation results to PDF format
- **Real-time Calculations**: Dynamic computation with progress indicators
- **Authentication System**: Secure access control

## Supported Mortgage Products

### Fixed Rate Products
- 5Y, 10Y, 13Y, 15Y, 18Y, 20Y, 25Y, 30Y - FIX

### Floating Rate Products
- 10Y, 15Y, 20Y - 1/1/1
- 10Y, 15Y, 20Y, 25Y - 5/5/5
- 25Y - 10/5/5, 20/5/5

## Installation

### Prerequisites
- Python 3.7+
- Required packages (install via pip):

```bash
pip install customtkinter pandas numpy numpy-financial openpyxl reportlab
```

### Running the Application
```bash
python main.py
```

### Building Executable
Use the provided setup.py with cx_Freeze:
```bash
python setup.py build
```

## Usage

1. **Authentication**: Login with credentials (Username: "Geeks", Password: "12345")
2. **Load Data**: Select an Excel file containing BBG rates data
3. **Set Parameters**:
   - Choose Fixed/Float type
   - Set repricing frequency (for floating rates)
   - Enter annual interest rate
   - Adjust time parameter (T)
4. **Calculate**: Click "Compute" to generate FTP rates
5. **Export**: Generate PDF reports of results

## File Structure

```
├── main.py                 # Main application entry point
├── Appli.py               # Legacy application file
├── Backup/
│   ├── Appli_copy.py      # Core calculation engine
│   └── Test_Apply_Copy.py # Test suite
├── Exemple/               # GUI examples
├── setup.py               # Build configuration
└── *.xlsm                 # Excel calculation files
```

## Technical Details

### Core Components

- **TableauResume**: Results display component with threaded calculations
- **App**: Main application class handling GUI and user interactions
- **Parametres**: Parameter management for calculations
- **GestionFichier**: Excel file handling and data extraction
- **Calculs**: Financial calculation engine

### Key Features

- **Threading**: Non-blocking calculations with progress indicators
- **Real-time Updates**: Dynamic UI updates based on user input
- **Data Validation**: Input validation and error handling
- **PDF Export**: Automated report generation

## Authentication

Default credentials:
- Username: `Geeks`
- Password: `12345`

## Dependencies

- `customtkinter`: Modern GUI framework
- `pandas`: Data manipulation and Excel reading
- `numpy`: Numerical computations
- `numpy-financial`: Financial calculations
- `openpyxl`: Excel file processing
- `reportlab`: PDF generation

## Development

The project follows a modular structure with separation between GUI (main.py) and calculation logic (Backup/Appli_copy.py). Test files are available in the Backup directory.

## Recent Updates

- Code optimization for option premium calculations
- Enhanced calculation engine performance
- Added comprehensive test suite
- Improved error handling and validation

## License

This project is proprietary software developed for financial calculations.