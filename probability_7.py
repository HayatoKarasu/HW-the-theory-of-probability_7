from matplotlib import pyplot as plt

def show():
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()


plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "Теорема Муавра-Лапласса: в теории вероятностей утверждает, что", fontsize=15)
plt.text(0.01, 0.8, "число успехов при многократном повторении одного и того же", fontsize=15)
plt.text(0.01, 0.7, "эксперимента с двумя возможными исходами приблизительно", fontsize=15)
plt.text(0.01, 0.6, "имеет нормальное распределение.", fontsize=15)
form = r"$lim_{n->\infty}P_n(k_1 \leq k \leq k_2) = \frac{1}{\sqrt{2\pi}} * \int_\alpha^\beta e^{-\frac{x^2}{2}} dx$"
plt.text(0.01, 0.5, form, fontsize=15)
form = r"$P(k_1 \leq k \leq k_2) \approx \Phi(\alpha) - \Phi(\beta)$"
plt.text(0.01, 0.4, form, fontsize=15)
form = r"$\alpha = \frac{k_1 - np}{\sqrt{npq}}$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$\beta = \frac{k_2 - np}{\sqrt{npq}}$"
plt.text(0.01, 0.2, form, fontsize=15)

show()

plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "Нормальное распределение - это совокупность значений объектов", fontsize=15)
plt.text(0.01, 0.8, "распределенные вокруг математического ожидания (среднего", fontsize=15)
plt.text(0.01, 0.7, "значения) и чем дальше от среднего значения, тем меньше", fontsize=15)
plt.text(0.01, 0.6, "вероятность появления такого значения.", fontsize=15)
plt.text(0.01, 0.5, "Например:", fontsize=15)
plt.text(0.01, 0.4, "Рост человека. Если сгрупировать большое количество людей", fontsize=15)
plt.text(0.01, 0.3, "по росту, то среднее значение будет 175 см., а значения роста", fontsize=15)
plt.text(0.01, 0.2, "карликов и великанов будет встречаться редко.", fontsize=15)
plt.text(0.01, 0.1, "Или з/п в какой-либо компании тоже можно распределить вокруг", fontsize=15)
plt.text(0.01, 0.01, "среденей з/п - очень низких и высоких з/п будет мало.", fontsize=15)

show()