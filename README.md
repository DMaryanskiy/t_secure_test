# Тестовое задание для компании T-Secure.

## Описание проекта.

Передо мной была поставлена задача реализовать API
с древовидной системой комментариев.
Данный интерфейс предоставляет 3 основные возможности:

1. Регистрация и аутентификация.
2. CRUD постов.
3. CRUD комментариев.

### 1. Регистрация и аутентификация.

Зарегистрироваться можно, отправив POST-запрос:
```
POST api/v1/register
```
Необходимо передать `username`, `email` и `password`.
Аутентификация происходит после отправления POST-запроса по адресу:
```
POST api-auth/login
```
Необходимо передать `username` и `password`.

### 2. CRUD постов.

Список всех постов можно получить по адресу:
```
GET api/v1
```
Создать новый пост может авторизованный пользователь по адресу:
```
POST api/v1/create
```
Необходимо передать параметр `text`.
Посмотреть конкретный пост можно по адресу:
```
GET api/v1/<int:post_id>
```
По этому же адресу автор поста может его изменить или вовсе удалить:
```
PUT api/v1/<int:post_id>
DELETE api/v1/<int:post_id>
```
В запросе на обновление надо передать параметр `text`.

### 3. CRUD комментариев

Поссмотреть комментарий к посту можно по адресу:
```
GET api/v1/<int:post_id>/<int:comment_id>
```
Добавить комментарий или ответ к комментарию можно по соответсвующим запросам:
```
POST api/v1/<int:post_id>/create
POST api/v1/<int:post_id>/<int:prev_comment_id>/create
```
Необходимо передать параметр `text`.
Автор комментария может также изменить его или удалить:
```
PUT api/v1/<int:post_id>/<comment_id>
DELETE api/v1/<int:post_id>/<comment_id>
```