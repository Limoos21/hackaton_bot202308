import mysql.connector


def get_manager_telegram_ids():  # Для авторизации проверка менеджер
    try:
        cnx = mysql.connector.connect(user='usertest123', password='admin1234',
                                      host='db4free.net', port=3306,
                                      database='bothackaton')
        cursor = cnx.cursor()

        cursor.execute("SELECT telegram_id FROM Manager")

        telegram_ids = [row[0] for row in cursor.fetchall()]

        return telegram_ids

    except mysql.connector.Error as err:
        print(f"Ошибка при подключении к базе данных: {err}")

    finally:
        cursor.close()
        cnx.close()


def get_user_telegram_ids():  # Для авторизации проверка клиент
    try:
        cnx = mysql.connector.connect(user='usertest123', password='admin1234',
                                      host='db4free.net', port=3306,
                                      database='bothackaton')
        cursor = cnx.cursor()

        cursor.execute("SELECT telegram_id FROM User")

        telegram_ids = [row[0] for row in cursor.fetchall()]

        return telegram_ids

    except mysql.connector.Error as err:
        print(f"Ошибка при подключении к базе данных: {err}")

    finally:
        cursor.close()
        cnx.close()


def check_manager_credentials(login, password):
    try:
        cnx = mysql.connector.connect(user='usertest123', password='admin1234',
                                      host='db4free.net', port=3306,
                                      database='bothackaton')
        cursor = cnx.cursor()

        cursor.execute("SELECT COUNT(*) FROM Manager WHERE login = %s AND password = %s", (login, password))

        count = cursor.fetchone()[0]

        return count > 0

    except mysql.connector.Error as err:
        print(f"Ошибка при подключении к базе данных: {err}")

    finally:
        cursor.close()
        cnx.close()


def check_user_credentials(number, password):
    try:
        cnx = mysql.connector.connect(user='usertest123', password='admin1234',
                                      host='db4free.net', port=3306,
                                      database='bothackaton')
        cursor = cnx.cursor()

        cursor.execute("SELECT COUNT(*) FROM User WHERE number = %s AND password = %s", (number, password))

        count = cursor.fetchone()[0]

        return count > 0

    except mysql.connector.Error as err:
        print(f"Ошибка при подключении к базе данных: {err}")

    finally:
        cursor.close()
        cnx.close()


def update_manager_telegram_id(login, password, telegram_id):
    try:
        cnx = mysql.connector.connect(user='usertest123', password='admin1234',
                                      host='db4free.net', port=3306,
                                      database='bothackaton')
        cursor = cnx.cursor()

        if check_manager_credentials(login, password):
            cursor.execute("UPDATE Manager SET telegram_id = %s WHERE login = %s AND password = %s",
                           (telegram_id, login, password))
            cnx.commit()
            return cursor.rowcount > 0

    except mysql.connector.Error as err:
        print(f"Ошибка при подключении к базе данных: {err}")

    finally:
        cursor.close()
        cnx.close()


def update_user_telegram_id(number, password, telegram_id):
    try:
        cnx = mysql.connector.connect(user='usertest123', password='admin1234',
                                      host='db4free.net', port=3306,
                                      database='bothackaton')
        cursor = cnx.cursor()

        if check_user_credentials(number, password):
            cursor.execute("UPDATE User SET telegram_id = %s WHERE number = %s AND password = %s",
                           (telegram_id, number, password))
            cnx.commit()
            return cursor.rowcount > 0

    except mysql.connector.Error as err:
        print(f"Ошибка при подключении к базе данных: {err}")

    finally:
        cursor.close()
        cnx.close()
