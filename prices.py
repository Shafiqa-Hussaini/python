prices = {
    "pen": 15,
    "book": 120,
    "bag": 850
}
print(prices.get("book"))
print(prices.get("ruler", "not found"))
print(prices.get("pen"))