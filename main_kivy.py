from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivymd import toast
from kivymd.theming import ThemeManager
from kivymd.color_definitions import colors
from kivy.utils import get_color_from_hex

layout = """
<VerticalBox@BoxLayout>
    id: box
    spacing: dp(15)
    orientation: 'vertical'

<ExampleButtons@BoxLayout>:
    orientation: 'vertical'
    spacing: dp(30)
    canvas:
        Color:
            rgba: {main_bg}
        RoundedRectangle:
            size: self.size
            pos: self.pos

    MDToolbar:
        id: toolbar
        title: 'Math and Code'
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        elevation: 10

    BoxLayout:
        orientation: 'vertical'
        height: self.minimum_height

        ScrollView:
            size_hint_y: 0.8
            size_hint_x: 0.8
            pos_hint: {{'center_x': .5}}
            bar_color: {scrollbar_color}

            BoxLayout:
                canvas:
                    Color:
                        rgba: 1, 1, 1, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [dp(10)]
                orientation: 'horizontal'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(48)
                spacing: dp(20)

                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(15)
                    MDLabel:
                        halign: 'center'
                        valign: 'top'
                        text: 'Python-код'

                    MDTextField:
                        multiline: True
                        hint_text: "Введите текст"
                        helper_text_mode: "none"

                MDFloatingActionButton:
                    id: 'btn_convert'
                    icon: 'arrow-right'
                    pos_hint: {{'center_y': .5}}
                    elevation_normal: 8
                    md_bg_color: {red}
                    on_press: app.btn_press('convert')
                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)
                    MDLabel:
                        halign: 'center'
                        valign: 'top'
                        text: 'Математический вид'
                    MDTextField:
                        multiline: True
                        disabled: True
                        hint_text: "Здесь будет результат"
                        helper_text_mode: "none"



        BoxLayout:
            id: box
            padding: dp(20)
            spacing: dp(10)
            orientation: 'horizontal'
            size_hint_y: 0.2
            size_hint_x: 0.7
            pos_hint: {{'center_x': .5}}


            VerticalBox:
                MDFloatingActionButton:
                    id: 'btn_history'
                    icon: 'history'
                    pos_hint: {{'center_x': .5}}
                    elevation_normal: 8
                    md_bg_color: {light_blue}
                    on_press: app.btn_press('history')

                MDLabel:
                    halign: 'center'
                    text: 'История'                    
                    text_color: {light_blue}

            VerticalBox:
                MDFloatingActionButton:
                    id: 'btn_solve_for_n'
                    icon: 'brain'
                    pos_hint: {{'center_x': .5}}
                    elevation_normal: 8
                    md_bg_color: {green}
                    on_press: app.btn_press('solve')

                MDLabel:
                    halign: 'center'
                    text: 'Решение для N'                    
                    text_color: {green}

            VerticalBox:
                MDFloatingActionButton:
                    id: 'btn_export'
                    icon: 'export-variant'
                    pos_hint: {{'center_x': .5}}
                    elevation_normal: 8
                    md_bg_color: {teal}
                    on_press: app.btn_press('export')

                MDLabel:
                    halign: 'center'
                    text: 'Экспорт'                    
                    text_color: {teal}

            VerticalBox:
                MDFloatingActionButton:
                    id: 'btn_help'
                    icon: 'help'
                    pos_hint: {{'center_x': .5}}
                    elevation_normal: 8
                    md_bg_color: {orange}
                    on_press: app.btn_press('help')

                MDLabel:
                    halign: 'center'
                    text: 'Помощь'                    
                    text_color: {orange}

"""
main_bg = get_color_from_hex(colors["Gray"]["300"])
scrollbar_color = get_color_from_hex(colors["BlueGray"]["200"])
red = get_color_from_hex(colors["Red"]["300"])
light_blue = get_color_from_hex(colors["LightBlue"]["400"])
green = get_color_from_hex(colors["Green"]["400"])
teal = get_color_from_hex(colors["Teal"]["400"])
orange = get_color_from_hex(colors["DeepOrange"]["400"])
Builder.load_string(layout.format(
    main_bg=main_bg,
    scrollbar_color=scrollbar_color,
    light_blue=light_blue,
    green=green,
    teal=teal,
    orange=orange,
    red=red
))


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGray'
    theme_cls.accent_palette = 'Red'
    print(get_color_from_hex(colors["Red"]["500"]))
    title = "Example Buttons"
    main_widget = None
    print()

    def build(self):
        items = ["Математический вид, Python - код"]
        return Factory.ExampleButtons()

    def btn_press(self, id):
        if id == "convert":
            toast.toast("Cконвертировать во что нужно!")
        elif id == "history":
            toast.toast("Показать историю")
        elif id == "solve":
            toast.toast("Решить для N")
        elif id == "export":
            toast.toast("Экспорт")
        elif id == "help":
            toast.toast("Меню помощи")
        print(f"The button <{id}> is being pressed")


if __name__ == "__main__":
    Example().run()
