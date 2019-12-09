import QtQuick 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Controls.Material.impl 2.13
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.13

Popup {
    id: popup
    rightPadding: 0
    bottomPadding: 30
    leftPadding: 0
     topPadding: 0
    anchors.centerIn: parent
    modal: true
    focus: true
    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

    background: Rectangle {
        radius: 2
        anchors.fill: parent
        color: Material.color(Material.Grey, Material.Shade100)
    }

    ColumnLayout {
        id: columnLayout
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.fill: parent

        Label {

            font.bold: true
            font.pointSize: 16
            horizontalAlignment: Text.AlignHCenter
            anchors.right: parent.right
            anchors.left: parent.left
            text: "Ошибка!"
            color: "#ffffff"
            background: Rectangle {
                color: Material.primary
            }
        }

        Label {
            text: "Ввод не может быть пустым"
            Layout.rightMargin: 20
            Layout.leftMargin: 20
            horizontalAlignment: Text.AlignHCenter
            anchors.right: parent.right
            anchors.left: parent.left
            Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
            font.pointSize: 12
        }

        Button {
            Material.background: Material.primary
            id: okButton
            text: "OK"
            flat: true
            font.pointSize: 10
            Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
            display: AbstractButton.TextOnly
            TapHandler {
                onTapped: popup.close()
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:2;anchors_height:100;anchors_width:100}
D{i:1;anchors_height:100;anchors_width:100}D{i:4;anchors_height:100;anchors_width:100}
D{i:3;anchors_height:100;anchors_width:100}
}
##^##*/

