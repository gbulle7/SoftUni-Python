number_pens = int(input())
number_markers = int(input())
ltrs_agent = int(input())
discount = int(input())
pen = 5.80
marker = 7.20
cleaning_agent_per_liter = 1.20
price_pens = number_pens * pen
price_markers = number_markers * marker
price_cleaning_agent = cleaning_agent_per_liter * ltrs_agent
total_cost = (price_pens + price_markers + price_cleaning_agent) - \
             (price_pens + price_markers + price_cleaning_agent) * discount * 0.01
print(total_cost)