import QtQuick 2.13

ListModel {
    id: leftMenuModel
    /*ListElement {
        ic: "images/menu_main.png"
        name: "Главное меню"
        selected: "1"
    }*/
    ListElement {
        ic: "images/solve_for_n.png"
        name: "Решить для N"
        selected: "0"
        click: "solve"
    }
    ListElement {
        ic: "images/export.png"
        name: "Экспорт"
        selected: "0"
        click: "export"
    }
    ListElement {
        ic: "images/history.png"
        name: "История"
       selected: "0"
       click: "history"
    }
    ListElement {
        ic: "images/help.png"
        name: "Помощь"
        selected: "0"
        click: "help"
    }
}
