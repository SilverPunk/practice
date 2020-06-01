import matplotlib.pyplot as plt
input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth=5)
plt.scatter(2, 4, s=200)
# Призначення заголовка діаграми і міток осей
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Призначення розміра шрифта, ділення осей
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
