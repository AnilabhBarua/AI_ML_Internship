# import the libraries
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

def calc(transactions, min_support, min_confidence):
    # Transform transactions to one-hot encoded format
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    
    # Find frequent itemsets using Apriori algorithm
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    
    # Calculate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    
    return frequent_itemsets, rules

# Dataset Transactions
transactions = [
    ['apple', 'banana'],
    ['apple', 'cake'],
    ['banana', 'cake'],
    ['apple', 'banana', 'cake'],
    ['banana', 'cake', 'ice cream']
]

min_support = 0.4
min_confidence = 0.6

frequent_itemsets, rules = calc(transactions, min_support, min_confidence)

print("FINDING FREQUENT ITEMSETS")
print()
print("Itemsets: ", transactions)
print("Minimum Support =", min_support)
print("Minimum Confidence =", min_confidence)

# Print frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)