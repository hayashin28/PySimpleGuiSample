# -*- coding: utf-8 -*-
import PySimpleGUI as sg # PySimpleGUIをインポート
from typing import Optional  # 型推定に用いる

# TODO 1. チェック判定の関数を作る
def check_data(name: str, password: str) -> bool:
    """
    ログイン名とパスワードが、指定された値と合致しているか判定する関数

    Args:
        name (str): 入力された名前
        password (str): 入力されたパスワード

    Returns:
        bool: 判定結果
    """
    # 正しいデータ
    correct_data = ("TERU", "TERU_PASSWORD")

    if (name, password) == correct_data:
        return True
    return False

# TODO 2. メイン画面を表示する関数を作る
def display_main() -> Optional[bool]:
    """
    メイン画面を表示する関数

    Returns:
        Optional[bool]: ログアウト判定 True or None
                        Noneならログイン画面も終了させる。
    """

    main_layout = [
        [sg.Text("メイン画面")],
        [sg.Text("ようこそ メイン画面へ")],
        [sg.Button("ログアウト", size=(10, 1), enable_events=True, key="-logout-")]
    ]

    main_window = sg.Window("メイン画面", main_layout, size=(400, 400))
    ret = None # 返り値

    while True:
        # イベントとGUI要素の値を取得する
        event, values = main_window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # ログインボタンが押されたら
        elif event == "-logout-":
            # データが一致したら、メイン画面を表示する処理
            logout_ret = sg.PopupOKCancel("ログアウトしますか？", title="ログアウト確認", keep_on_top=True)

            # もしもOKならTrueを返し、メイン画面を終了する。
            if logout_ret == "OK":
                ret = True
                break
            else:
                continue

    # メイン画面を終了する
    main_window.close()
    # 最後に返り値を渡す
    return ret


# テーマカラーを設定
sg.theme("SandyBeach")

# ログイン画面のレイアウト
layout = [
    [sg.Text("ログイン画面")],
    [sg.Text("名前：", size=(10, 1)), sg.Input("", size=(25, 1), key="-name-")],
    [sg.Text("パスワード：", size=(10, 1)), sg.Input("", size=(25, 1), key="-password-")],
    [sg.Button("ログイン", size=(10, 1), enable_events=True, key="-login-")]
]

window = sg.Window("ログイン画面", layout, size=(400, 400))

while True:
    # イベントとGUI要素の値を取得する
    event, values = window.read()

    # ×ボタンが押された時はループを抜け出す。
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # ログインボタンが押された場合の処理
    elif event == "-login-":
        # TODO 3. データが一致したら、メイン画面を表示する処理を実装
        if check_data(name=values["-name-"], password=values["-password-"]):
            window.Hide() # ログイン画面を隠す
            # メイン画面を表示する
            main_return = display_main()
            # もしNoneが返ってきたらログイン画面も終了させる
            if main_return is None:
                break
            window.UnHide() # ログイン画面を再表示する
# windowを終了させる
window.close()