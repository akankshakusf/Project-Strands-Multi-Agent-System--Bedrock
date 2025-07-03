from strands import tool

@tool
def aapl_stock_comparison() -> str:
    """
    Compare AAPL's stock performance across 2022-2026.
    
    Returns:
        str: Multi-year comparison of AAPL's key financial metrics and stock price.
    """
    
    years = [2022, 2023, 2024, 2025, 2026]
    
    stock_prices = {
        2022: 180.0,
        2023: 195.5, 
        2024: 225.0,
        2025: 210.5,
        2026: 245.0
    }
    
    revenues = {
        2022: 365.8,
        2023: 394.3,
        2024: 436.7, 
        2025: 490.1,
        2026: 522.5
    }
    
    net_incomes = {
        2022: 99.8,
        2023: 97.0,
        2024: 93.7,
        2025: 104.5, 
        2026: 118.2
    }
    
    comparison = "AAPL Multi-Year Comparison:\\n\\n"
    comparison += "Year | Stock Price | Revenue ($B) | Net Income ($B)\\n" 
    comparison += "-----|--------------|---------------|-----------------\\n"
    
    for year in years:
        if year in stock_prices and year in revenues and year in net_incomes:
            price = stock_prices[year]
            rev = revenues[year] 
            net = net_incomes[year]
            comparison += f"{year} | ${price:.2f} | {rev:.1f} | {net:.1f}\\n"
        
    return comparison