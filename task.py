'''
Инструкция по выполнению задания:
1) Установите зависимости командой "pip install -r requirements.txt" или установите каждую зависимость отдельно
python -m pip install pyjwt aiohttp datetime либо же python3 -m pip install pyjwt aiohttp datetime.
2) Выполните необходимые задания в функциях handle_post() и authenticate().
3) После выполнения заданий запустите сервер командой "python task.py" (или другой, если у вас используется "python3", "python3.9" и т.д.).
4) Сайт будет по-умолчанию доступен по адресу "localhost:8080" в браузере.
5) На сайте введите свою фамилию в поле "Логин", любой пароль в поле "Пароль" и роль в поле "Роль"
    Если задания из п.2 выполнены правильно, то в пункте "Ваш токен:" вам будет выведен сгенерированный токен.
    Скопируйте данный токен, и вставьте его в поле "Введите ваш токен", а затем проверьте его.
    Нажмите на кнопку "Проверить", если всё сделано правильно, вам будет выведен тот логин и роль которые вы вводили.
    Он будет выведен в формате "Вы {login}, ваша роль {user_role}".
'''

from aiohttp import web
import jwt
import datetime

async def handle_index(request):
    return web.FileResponse('index.html')

async def handle_post(request):
    user_data = await request.json()  # Здесь прилетает словарь с полезной нагрузкой

    user_login = user_data.get('login', '')
    user_password = user_data.get('password', '')
    user_role = user_data.get('role', '')

    #YOUR CODE HERE
    # Необходимо создать payload, установить время жизни токена (exp)
    # и сгенерировать закодированный JWT токен.

    data_to_return = {
        'token': encoded_jwt
    }

    return web.json_response(data_to_return)

async def authenticate(request):
    data = await request.json()
    token = data.get('token', '')
    is_successful = False
    result = ''
    try:
        #YOUR CODE HERE
        # Необходимо декодировать токен, обработать истечение срока действия
        # и извлечь информацию о пользователе.
        is_successful = True
        result = f"Вы {user_login}, ваша роль {user_role}"
    except jwt.ExpiredSignatureError:
        #YOUR CODE HERE
        # Обработка истечения срока действия токена

    except jwt.DecodeError:
        #YOUR CODE HERE
        # Обработка ошибок декодирования токена

    data_to_return = {
        'decrypted': result,
        'is_successful': is_successful
    }

    return web.json_response(data_to_return)

app = web.Application()
app.router.add_get('/', handle_index)
app.router.add_post('/handle_post', handle_post)
app.router.add_post('/authenticate', authenticate)
app.router.add_static('/static', path='static')

if __name__ == "__main__":
    web.run_app(app)
