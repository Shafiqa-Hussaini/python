sales = [
    {"product": "Pen", "quantity": 3, "price": 15},
    {"product": "Book", "quantity": 2, "price": 120},
    {"product": "Pen", "quantity": 5, "price": 15},
    {"product": "Bag", "quantity": 1, "price": 850},
    {"product": "Book", "quantity": -1, "price": 120},
    {"product": "Ruler", "quantity": 4, "price": 20}
]

product_revenue = {}
total_revenue = 0
high_value_tx = []
invalid_count = 0

for record in sales:
    qty = record["quantity"]
    price = record["price"]
    product = record["product"]

    # check for invalid record
    if qty <= 0 or price < 0:
        invalid_count += 1
        continue

    rev = qty * price
    total_revenue += rev

    if product in product_revenue:
        product_revenue[product] += rev
    else:
        product_revenue[product] = rev

    if rev >= 200:
        high_value_tx.append(record)

# find top product
top_product = ""
max_rev = -1
for p in product_revenue:
    if product_revenue[p] > max_rev:
        max_rev = product_revenue[p]
        top_product = p

print("Revenue by product:", product_revenue)
print("Total revenue: Tk", total_revenue)
print("Top product:", top_product)
print("High value transactions (>= Tk 200):", high_value_tx)
print("Invalid records:", invalid_count)