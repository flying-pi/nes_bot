import os
import threading
from time import sleep
from typing import Optional, Callable, Iterable, Mapping, Any

from communication.Server import Server

HOST = '127.0.0.1'
PORT = 4306


class GameThread(threading.Thread):
    def __init__(self, host: str, port: int, start_marker: threading.Event) -> None:

        super().__init__()
        self.host = host
        self.port = port
        self.start_marker = start_marker

    def run(self):
        while not self.start_marker.wait(1):
            print("whating to server start")
        emulator_root = './../LaiNES/build-LaiNES-Desktop_Qt_5_10_1_clang_64bit-Debug' \
                        '/qtc_Desktop_Qt_5_10_1_clang_64bit_Debug/install-root/'
        emulator_name = f'./LaiNES '
        room_path = 'roms/Gradius.nes'
        os.system(f'cd {emulator_root} && {emulator_name} {room_path} {self.host} {self.port}')
        # pass


def main():
    server = Server()
    start_marker = server.init(HOST, PORT)
    server.start()

    game_thread = GameThread(HOST, PORT,start_marker)
    game_thread.start()
    game_thread.join()


if __name__ == "__main__":
    main()
