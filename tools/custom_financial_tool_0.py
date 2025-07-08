from strands import tool 

@tool
def aapl_stock_comparison(start_year: int = 2022, end_year: int = 2026) -> str:
    """
    Compares Apple (AAPL) stock performance across a given year range.

    Args:
        start_year (int): Starting year for comparison (inclusive)
        end_year (int): Ending year for comparison (inclusive)

    Returns:
        str: Formatted multi-year comparison table for AAPL stock
    """
    aapl_data = [
        {"year": 2022, "stock_price": 180.00, "revenue": 365.8, "net_income": 99.8},
        {"year": 2023, "stock_price": 195.50, "revenue": 394.3, "net_income": 97.0},
        {"year": 2024, "stock_price": 225.00, "revenue": 436.7, "net_income": 93.7},
        {"year": 2025, "stock_price": 210.50, "revenue": 490.1, "net_income": 104.5},
        {"year": 2026, "stock_price": 245.00, "revenue": 522.5, "net_income": 118.2},
    ]
    
    filtered_data = [data for data in aapl_data if start_year <= data["year"] <= end_year]
    
    table = "Year | Stock Price | Revenue ($B) | Net Income ($B)\n-----|--------------|---------------|-----------------\n"
    for data in filtered_data:
        row = "{} | ${:.2f} | {:.1f} | {:.1f}\n".format(
            data["year"], data["stock_price"], data["revenue"], data["net_income"]
        )
        table += row
        
    return table