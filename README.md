# SneakersStoreAiogramBot

<p align="center"> 
  <img width="300" src="https://github.com/munwriter/SneakersStoreAiogramBot/blob/main/.github/logo.png">
</p>
<p align="center"><b>Телеграм бот для продажи товаров</b></p>

# Функционал
Основной функционал бота заключатся в выполнении так называемых CRUD(create, read, update, delete) операций в контексте онлайн магазина.
## Главное меню
В основном интерфейсе пользователю предоставлены кнопки: Корзина, Ассортимент, Поддержка.
<p> 
  <img width="800" src="https://github.com/munwriter/SneakersStoreAiogramBot/blob/main/.github/main_menu.png">
</p>

В версии администратора есть кнопка, позволяющая администрировать проект, а именно добавлять удалять товар.

<p> 
  <img width="800" src="https://github.com/munwriter/SneakersStoreAiogramBot/blob/main/.github/admin_menu.png">
</p>

## Ассортимент
Ассортимент представлен в виде inlain клавиатуры.
<p> 
  <img width="800" height="490" src="https://github.com/munwriter/SneakersStoreAiogramBot/blob/main/.github/assortment.png">
</p>

## Карточка товара
Детальное описание товара представлено как название, описание, фото и стоимость товара. Далее идет предложение о добавление в корзину, где можно добавить товар в корзину или же выйти обратно в меню.
<p> 
  <img width="400" src="https://github.com/munwriter/SneakersStoreAiogramBot/blob/main/.github/product_details.png">
</p>

## Корзина
В корзине имеется список товаров пользователя, а также кнопки для очистки корзины или же возврата в главное меню.
<p> 
  <img width="400" src="https://github.com/munwriter/SneakersStoreAiogramBot/blob/main/.github/shopping_cart.png">
</p>

# Архитектура проекта
...

# Использование
* **Клонирование репозитория**
```
 https://github.com/munwriter/SneakersStoreAiogramBot.git
```
* **Установка зависимостей**
```
  pip install -r requirements.txt
```
* **Создание окружения с токеном бота и id администратора**
```
  TOKEN='{your_token}'
  ADMIN_ID='{admin_id}'
```
* **Запуск бота**
```python
  py run.py
```
