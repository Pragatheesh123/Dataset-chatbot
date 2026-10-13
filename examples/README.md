# Example Questions

Here are a few ways to ask questions about the sales dataset, along with the pandas analysis that can answer them.

## 1. Which product had the highest total sales?

```text
You: Which product had the highest total sales?
```

```python
(df.assign(Product=df["Product"].astype("string").str.strip().str.casefold())
   .groupby("Product")["Total_Sales"]
   .sum()
   .idxmax())
```

```text
AI: Laptop had the highest total sales.
```

This compares the total sales amount for each product.

## 2. How many units did Rahul Singh sell?

```text
You: How many units did Rahul Singh sell?
```

```python
df.loc[
    df["Salesperson"].astype("string")
      .str.strip()
      .str.replace(r"\s+", " ", regex=True)
      .str.casefold()
      .eq("rahul singh"),
    "Quantity"
].sum()
```

```text
AI: Rahul Singh sold 70 units.
```

This adds the `Quantity` values. It is different from counting the number of sales records.

## 3. Which cities had the most Monitor sales?

```text
You: Show the cities with the most Monitor sales and the number of sales in each.
```

```python
(df.assign(
    Product=df["Product"].astype("string").str.strip().str.casefold(),
    City=df["City"].astype("string").str.strip().str.casefold()
)
 .loc[lambda data: data["Product"].eq("monitor")]
 .groupby("City")
 .size()
 .sort_values(ascending=False)
 .head(4))
```

```text
AI: Pune had 6 Monitor sales. Bangalore, Hyderabad, and Delhi had 2 each.
```

The dataset has a tie for the remaining top-city places, so other cities may appear depending on how tied results are ordered.

## 4. What were the four highest-selling products in Chennai?

```text
You: What were the four products with the highest total sales in Chennai?
```

```python
(df.assign(
    Product=df["Product"].astype("string").str.strip().str.casefold(),
    City=df["City"].astype("string").str.strip().str.casefold()
)
 .loc[lambda data: data["City"].eq("chennai")]
 .groupby("Product")["Total_Sales"]
 .sum()
 .sort_values(ascending=False)
 .head(4))
```

```text
AI: Laptop, Smartphone, Printer, and Office Chair had the highest total sales in Chennai.
```

Cleaning capitalization and extra spaces matters because the dataset uses different forms such as `Chennai` and `CHENNAI`.

## 5. What were the total sales for Laptops in Delhi?

```text
You: What were the total sales for Laptops sold in Delhi?
```

```python
df.loc[
    df["Product"].astype("string").str.strip().str.casefold().eq("laptop")
    & df["City"].astype("string").str.strip().str.casefold().eq("delhi"),
    "Total_Sales"
].sum()
```

```text
AI: Laptop sales in Delhi totalled 130,000.
```

## Tips

- Be clear whether you mean total revenue, units sold, or the number of sale records.
- Names, products, and cities may have different capitalization or extra spaces in the dataset.
- These examples use the dataset as it is. Repeated sale records can affect the totals.
