import pandas as pd

def import_data(Online_Retail: str) -> pd.DataFrame:
    """Import the dataset from an Excel or CSV file into a DataFrame."""
    if filename.endswith('.xlsx'):
        return pd.read_excel(Online_Retail.xlsx)
    elif filename.endswith('.csv'):
        return pd.read_csv(Online_Retail.xlsx)
    else:
        raise ValueError("File format not supported. Please use .xlsx or .csv")

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filter the data by removing rows with any missing CustomerID and excluding negative values."""
    filtered_df = df[df['CustomerID'].notnull()]
    filtered_df = filtered_df[(filtered_df['Quantity'] >= 0) & (filtered_df['UnitPrice'] >= 0)]
    return filtered_df

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    """Identify loyal customers based on a minimum purchase threshold."""
    customer_counts = df['CustomerID'].value_counts()
    loyal_customers = customer_counts[customer_counts >= min_purchases]
    return pd.DataFrame(loyal_customers).reset_index().rename(columns={'index': 'CustomerID', 'CustomerID': 'PurchaseCount'})

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate the total revenue per quarter."""
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    quarterly_revenue = df.groupby('Quarter')['Revenue'].sum().reset_index()
    quarterly_revenue['Quarter'] = quarterly_revenue['Quarter'].astype(str)  # Convert Period to string for better readability
    return quarterly_revenue

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """Identify the top_n products with the highest total quantity sold."""
    product_sales = df.groupby('Description')['Quantity'].sum().reset_index()
    top_products = product_sales.nlargest(top_n, 'Quantity').reset_index(drop=True)
    return top_products.rename(columns={'Description': 'Product', 'Quantity': 'TotalQuantitySold'})

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    """Create a summary showing the average quantity and average unit price for each product."""
    product_patterns = df.groupby('Description').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    return product_patterns.rename(columns={'Description': 'Product'})

def answer_conceptual_questions() -> dict:
    """Answer the conceptual questions."""
    return {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"C"},
        "Q4": {"A", "C"},
        "Q5": {"A"}
    }
