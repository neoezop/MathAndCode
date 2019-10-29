import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Window 2.3
import QtQuick.Controls.Material 2.2

ApplicationWindow{
    title: qsTr('Qml app')
    id: mainWindow
    width:  800
    height: 600
    visible: true
    Material.theme: Material.Light
    Material.accent: Material.Purple

    Column {
        width: 392
        height: 358
        anchors.centerIn: parent

        RadioButton { text: qsTr("Small") }
        RadioButton { text: qsTr("Medium");  checked: true }
        RadioButton { text: qsTr("Large") }

        Button {
            text: qsTr("Button")
            highlighted: true
            Material.accent: Material.Orange
        }
        Button {
            text: qsTr("Button")
            highlighted: true
            Material.background: Material.Teal
        }

        Rectangle {
            color: Material.color(Material.Red)
        }

        Pane {
            width: 120
            height: 120

           Material.elevation: 6

            Label {
                text: qsTr("I'm a card!")
                anchors.centerIn: parent
            }
        }

        Button {
            text: qsTr("Button")
            Material.foreground: Material.Pink
        }

        Pane {
            Material.theme: Material.Dark
            Button {
                text: qsTr("Button")
            }
        }
    }
}
