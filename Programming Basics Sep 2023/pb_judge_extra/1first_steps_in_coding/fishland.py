price_mackerel = float(input())
price_tsatsa = float(input())
weight_palamud = float(input())
weight_safrid = float(input())
weight_midi = int(input())
price_palamud = weight_palamud * (0.6 * price_mackerel + price_mackerel)
price_safrid = weight_safrid * (0.8 * price_tsatsa + price_tsatsa)
price_midi = weight_midi * 7.5
total_price = price_palamud + price_safrid + price_midi
print(f'{total_price:.2f}')
