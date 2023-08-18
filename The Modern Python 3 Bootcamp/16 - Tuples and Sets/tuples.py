# Tuples ar commonly used of UNCHANGING data:
months = ('January','February','March',"April","May",'June','July','August','september','October','December')
for month in months:
    print(month)
    
i = len(months)-1
while i >= 0:
    print(months[i])
    i -= 1

# Tuples can be used as keys in dictionaries:
location = {
    (35.6895,39.6917):"Tokyo Office",
    (40.7128,74.0060):"New York Office",
    (37.7749,122.4194):"San Francisco Office",
}

# Some dictionaries methods like  .item() return tuples
cat = {"name": 'Biscuit', "age":0.5, "Favorite_toy":"my chopstick"}
i = cat.items()
print(i)
# dict_items([('name', 'Biscuit'), ('age', 0.5), ('Favorite_toy', 'my chopstick')])
                #   tuple             tuple              tuple