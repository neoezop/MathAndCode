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
    topPadding: 15
    anchors.centerIn: parent
    modal: true
    focus: true
    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

    background:     Rectangle {
        radius: 2
        anchors.fill: parent
        color: Material.color(Material.Grey, Material.Shade100)
    }

    ColumnLayout {
        id: columnLayout
        anchors.fill: parent

        Label {
            color: Material.accent
            text: "Решить для N"
            Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
            font.pointSize: 14
            font.bold: true
        }
        TabBar {
            Layout.minimumWidth: 400
            id: bar
            Layout.fillWidth: true
            TabButton {
                text: qsTr("Решение рекурсии")
                checked: true
            }
            TabButton {
                text: qsTr("Вызовы рекурсии")
                checked: true
            }
        }

        StackLayout {
            id: stackLayout
            currentIndex: bar.currentIndex
            Item {
                id: solutionsTab

                Label {
                    color: Material.accent
                    text: "Решение рекурсии для заданного N"
                    horizontalAlignment: Text.AlignHCenter
                    anchors.right: parent.right
                    anchors.rightMargin: 0
                    anchors.left: parent.left
                    anchors.leftMargin: 0
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
                    font.pointSize: 12
                }
            }
            Item {
                id: callsTab
                Label {
                    color: Material.accent
                    text: "Дерево вызовов рекурсии при заданном N"
                    horizontalAlignment: Text.AlignHCenter
                    anchors.right: parent.right
                    anchors.rightMargin: 0
                    anchors.left: parent.left
                    anchors.leftMargin: 0
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
                    font.pointSize: 12
                }
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:1;anchors_height:100;anchors_width:100}
D{i:3;anchors_height:100;anchors_width:100}D{i:2;anchors_height:100;anchors_width:100}
}
##^##*/

