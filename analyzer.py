import re

def analyze_financials(text):
    metrics = {}

    revenue_match = re.search(r"(?i)net sales\s+\$?([\d,]+)\.?", text)
    income_match = re.search(r"(?i)net income\s+\$?([\d,]+)\.?", text)
    equity_match = re.search(r"(?i)total shareholders' equity\s+\$?([\d,]+)\.?", text)

    try:
        if revenue_match:
            revenue = int(revenue_match.group(1).replace(",", ""))
            metrics['Omsättning'] = f"{revenue:,} USD"

        if income_match:
            income = int(income_match.group(1).replace(",", ""))
            metrics['Nettoresultat'] = f"{income:,} USD"

        if equity_match:
            equity = int(equity_match.group(1).replace(",", ""))
            metrics['Eget kapital'] = f"{equity:,} USD"

        if income_match and equity_match:
            roe = round((income / equity) * 100, 2)
            metrics['ROE'] = f"{roe}%"

        if income_match and revenue_match:
            margin = round((income / revenue) * 100, 2)
            metrics['Vinstmarginal'] = f"{margin}%"

    except Exception as e:
        print("Fel i analysen:", e)
        return None

    return metrics
