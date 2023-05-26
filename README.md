# Blog
## Task:
```

Цели проекта

1. Создать проект “Блог” для создания постов 
2. Добавить возможности создавать и изменять аккаунт Юзеру
3. Создать возможность добавления постов для Юзеров
4. Добавить возможность управлять постами для Юзеров

```
---
## Technology

1. Django==4.2.1
2. crispy-bootstrap4==2022.1
3. django-crispy-forms==2.0
4. Pillow==9.3.0
---
## Architecture of project

- admin/ - страница Администратора
- register/ - страница регистрации Пользователя
- profile/ - страница аккаунта Пользователя
- profile/profile_update/ - страница изменения данных аккаунта Пользователя
- login/ - страница входа в аккаунт Пользователя
- logout/ - страница выхода из аккаунта Пользователя
- about/ - страница информации о проекте
- post-new/ - страница создания нового постами
- post/<int:pk>/ - страница определённого поста по номеру id(номеру pk)
- post/<int:pk>/update - страница для изменения определённого поста по номеру id
- post/<int:pk>/delete - страница для удаления определённого поста по номеру id