# ログイン画面のレイアウト
import PySimpleGUI as sg

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
        pass

# windowを終了させる
window.close()