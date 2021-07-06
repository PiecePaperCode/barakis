import random
import threading
import time

from ogame import OGame
import buildings


running = True
bot_queue: list[OGame] = []


def bot():
    for empire in bot_queue:
        try:
            if not empire.is_logged_in():
                empire.relogin()
            ids = empire.planet_ids()
            for ID in ids:
                for order in buildings.queue(ID, empire):
                    print(order.condition, order.build)
                    if order.condition:
                        empire.build(
                            what=order.build,
                            id=ID
                        )
                        break
        except Exception as e:
            print(e)
            remove(empire.universe, empire.username)
            add(empire.universe, empire.username, empire.password)


def scheduler():
    print('Starting up Barakis Scheduler')
    while running:
        try:
            bot()
        except Exception as e:
            print(e)
        time.sleep(random.randint(20, 120))


thread = threading.Thread(target=scheduler)


def add(uni, username, password) -> bool:
    if active(uni, username):
        return False
    try:
        bot_queue.append(
            OGame(
                uni,
                username,
                password
            )
        )
        return True
    except AssertionError:
        return add(uni, username, password)


def remove(universe, username) -> bool:
    for i, empire in enumerate(bot_queue):
        if empire.universe == universe and empire.username == username:
            del bot_queue[i]
            return True
    return False


def stop() -> bool:
    global bot_queue
    bot_queue = []
    return True


def active(universe, username) -> bool:
    for i, empire in enumerate(bot_queue):
        if empire.universe == universe and empire.username == username:
            return True
    return False
