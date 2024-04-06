import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('menu.csv')


print('Идея: Генерация меню по настроению, вкусовым предпочтениям потребителя \n\
      Гипотеза №1: Большая часть блюд из меню является высококалорийной \n\
      Гипотеза №2: Каждое блюдо содержит сахар\n\
      Гипотеза №3: Блюд в категории ("Category") "Coffee & Tea" больше всего\n\
      Гипотеза №4: Средний вес блюд 200 грамм.')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_column', None)


# print(df.info())

# Гипотеза №1: Большая часть блюд из меню является высококалорийной

big_calor = 0
small_calor = 0

for calor in df['Calories']:
    if calor >= 300:
        big_calor += 1
    else:
        small_calor += 1
print('Высококалорийные блюда (более 300 калорий) - ', big_calor)
print('Низкокалорийные блюда (менее 300 калорий) - ', small_calor)
if big_calor > small_calor:
    print('Гипотеза №1 подтверждена')
else:
    print('Гипотеза №1 опровергнута')

df.plot(x = 'Calories', y = 'Category', kind = 'scatter')
plt.show()

# Гипотеза №2: Каждое блюдо содержит сахар
sugar_yes = 0
sugar_no = 0

for sugar in df['Sugars']:
    if sugar > 0:
        sugar_yes += 1
    else:
        sugar_no += 1
print('Блюда содержащие сахар - ', big_calor)
print('Блюда не содержащие сахар - ', small_calor)
if sugar_yes == 0:
    print('Гипотеза №2 подтверждена')
else:
    print('Гипотеза №2 опровергнута')

df['Sugars'].plot(kind = 'hist', bins = 20)
plt.show()

# Гипотеза №3: Блюд в категории ('Category') 'Coffee & Tea' больше всего.
coffe_tea = 0
no_coffe_tea = 0

for cat in df['Category']:
    if cat >= 'Coffee & Tea':
        coffe_tea += 1
    else:
        no_coffe_tea += 1

print('Блюд из категории "Coffee & Tea" - ', coffe_tea)
print('Блюда не из категории "Coffee & Tea"  - ', no_coffe_tea)
if coffe_tea > no_coffe_tea:
    print('Гипотеза №3 подтверждена')
else:
    print('Гипотеза №3 опровергнута')

df['Category'].value_counts().plot(kind = 'pie')
plt.show()

# Гипотеза №4: Средний количество белка в блюдах больше 14.

# blud = 0
# prot = 0
mean_prot = df['Protein'].mean()

# for cat in df['Protein']:
#     blud += 1
#     prot += cat

# mean_prot_2 = prot/blud

print('Среднее количсвто белка в блюдах - ', round(mean_prot, 2))
if mean_prot < 14:
    print('Гипотеза №3 подтверждена')
else:
    print('Гипотеза №3 опровергнута')


df['Protein'].value_counts().plot(kind = 'line')
plt.show()