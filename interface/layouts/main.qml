import QtQuick 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Controls.Material.impl 2.13
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.13

ApplicationWindow {
    id: window
    width: 1200
    height: 500
    visible: true
    title: qsTr("Math and Code")
    color: Material.color(Material.Grey, Material.Shade100)

    property bool isPythonToMath: true


    /*ToolBar {
        id: overlayHeader

        z: 1
        width: parent.width
        parent: window.overlay

        Label {
            id: label
            anchors.centerIn: parent
            text: "Qt Quick Controls 2"
        }
    }*/
    Drawer {
        id: drawer

        width: 175
        height: window.height
        modal: false
        interactive: false
        position: 1
        visible: true
        Material.elevation: 5
        ButtonGroup {
            id: buttonGroup
        }
        ListView {
            id: listView
            anchors.fill: parent
            interactive: false
            headerPositioning: ListView.OverlayHeader
            header: Pane {
                id: header
                z: 2
                width: parent.width
                background: Rectangle {
                    color: Material.primary
                }

                Label {
                    font.bold: true
                    font.pixelSize: 14
                    width: parent.width
                    horizontalAlignment: Qt.AlignHCenter
                    verticalAlignment: Qt.AlignVCenter
                    text: qsTr("Math and Code")
                    color: "#ffffff"
                }

                MenuSeparator {
                    parent: header
                    width: parent.width
                    anchors.verticalCenter: parent.bottom
                    visible: !listView.atYBeginning
                }
            }

            // Flickable:
            model: LeftMenuModel {}
            delegate: ItemDelegate {
                icon.source: ic
                text: name
                width: parent.width
                onClicked: {
                    switch (click) {
                    case "solve":
                        solvePopup.open()
                        break
                    case "export":
                        exportPopup.open()
                        break
                    }
                }
            }

            //highlight: Rectangle { color: Material.color(Material.Indigo,Material.Shade100); } //for highlighting curr item


            /*delegate: Button {
                       text: name
                       Material.background : Material.primary
                       icon.source: ic
                       checked: true
                       font.capitalization: Font.MixedCase
                       ButtonGroup.group: buttonGroup
                       width: parent.width

                       HoverHandler {
                           onHoveredChanged: {
                               if (hovered == true)
                                   Material.background = Material.primary
                               else
                                   Material.background = Material.color(
                                               Material.Grey,
                                               Material.Shade200)
                           }
                       }
                   }*/
            ScrollIndicator.vertical: ScrollIndicator {}
        }
    }

    RowLayout {
        id: rowLayout
        anchors.rightMargin: 20
        anchors.leftMargin: 20 + drawer.width
        anchors.bottomMargin: 20
        anchors.topMargin: 20
        anchors.fill: parent

        Rectangle {
            id: cardInput
            color: Material.backgroundColor
            radius: 2
            Layout.fillHeight: true
            Layout.fillWidth: true
            layer.enabled: true
            layer.effect: ElevationEffect {
                elevation: 5
            }

            ColumnLayout {
                anchors.rightMargin: 15
                anchors.leftMargin: 15
                anchors.bottomMargin: 15
                anchors.topMargin: 15
                anchors.fill: parent
                anchors.verticalCenter: parent.verticalCenter
                spacing: 5

                //todo add load from file and delete buttons (like yandex translate has)
                Label {
                    id: inputHeader
                    color: Material.accent
                    text: isPythonToMath ? qsTr("Python код") : qsTr(
                                               "Математическое представление")
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.pointSize: 14
                    font.bold: true
                }
                ComboBox {
                    displayText: currentIndex == -1 ? "Выберите тип задания" : currentText
                    currentIndex: -1
                    Layout.fillHeight: false
                    Layout.fillWidth: true
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
                    Material.elevation: 0
                    model: ["Первый тип задания", "Второй тип задания", "Третий тип задания"]
                }
                Rectangle {
                    id: rectInput
                    Layout.rightMargin: 0
                    border.color: textAreaInput.activeFocus ? Material.primary : Material.color(
                                                                  Material.Grey,
                                                                  Material.Shade200)
                    border.width: 1
                    Layout.minimumWidth: 250
                    Layout.minimumHeight: 300
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
                    ScrollView {
                        id: view
                        padding: 5
                        anchors.fill: parent
                        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
                        ScrollBar.vertical.policy: ScrollBar.AlwaysOff

                        TextArea {
                            id: textAreaInput
                            text: ""
                            placeholderText: isPythonToMath ? qsTr("Введите Python код") : qsTr(
                                                                  "Введите математическое представление")
                            background: null
                        }

                        //is needed to turn Flickable on
                        HoverHandler {
                            onHoveredChanged: {


                                /*if (hovered == true)
                                    rectInput.border.color = Material.primary
                                else
                                    rectInput.border.color = Material.color(
                                                Material.Grey,
                                                Material.Shade200)*/
                            }
                        }
                    }
                }
            }
        }

        ColumnLayout {
            id: column
            Layout.alignment: Qt.AlignHCenter | Qt.AlignTop

            RoundButton {
                Material.background: Material.primary
                id: swapButton
                text: "Swap"
                Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
                display: AbstractButton.IconOnly
                icon.source: "images/swap.png"
                icon.color: "#ffffff"

                //code swap click swaps python and math
                TapHandler {
                    onTapped: isPythonToMath = !isPythonToMath
                }
            }

            RoundButton {
                Material.background: Material.LightGreen
                id: translateButton
                text: "Translate"
                Layout.topMargin: rowLayout.height / 2 - swapButton.height
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                display: AbstractButton.IconOnly
                icon.source: "images/translate.png"
                icon.color: "#ffffff"

                onClicked: {
                    if (textAreaInput.text == "") {
                        //PopupEmptyInput
                        popupEmptyInput.open()
                    } else {
                        converter.convert(textAreaInput.text, isPythonToMath)
                    }
                }
            }
        }

        Rectangle {
            id: cardOutput
            color: Material.backgroundColor
            radius: 2
            Layout.fillHeight: true
            Layout.fillWidth: true
            layer.enabled: true
            layer.effect: ElevationEffect {
                elevation: 5
            }

            ColumnLayout {
                anchors.rightMargin: 15
                anchors.leftMargin: 15
                anchors.bottomMargin: 15
                anchors.topMargin: 15
                anchors.fill: parent
                anchors.verticalCenter: parent.verticalCenter
                spacing: 5

                Label {
                    id: outputHeader
                    color: Material.accent
                    text: isPythonToMath ? qsTr("Математическое представление") : qsTr(
                                               "Python код")
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.pointSize: 14
                    font.bold: true
                }
                Rectangle {
                    id: rectOutput
                    Layout.rightMargin: 0
                    border.color: Material.color(Material.Grey,Material.Shade200)
                    border.width: 1
                    Layout.minimumWidth: 250
                    Layout.minimumHeight: 300
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
                    ScrollView {
                        padding: 5
                        anchors.fill: parent
                        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
                        ScrollBar.vertical.policy: ScrollBar.AlwaysOff

                        TextArea {

                            id: textAreaOutput
                            text: ""
                            enabled: false
                            placeholderText: ""
                            background: null
                        }

                        //is needed to turn Flickable on
                        HoverHandler {
                            onHoveredChanged: {


                                /*if (hovered == true)
                                    rectInput.border.color = Material.primary
                                else
                                    rectInput.border.color = Material.color(
                                                Material.Grey,
                                                Material.Shade200)*/
                            }
                        }
                    }
                }
            }
        }
    }

    // Converter results there
    Connections {
        target: converter

        // Обработчик сигнала сложения
        onConvertResult: {
            // sum было задано через arguments=['sum']
            textAreaOutput.text = convert;
        }
    }

    PopupEmptyInput {
        id: popupEmptyInput
    }

    PopupSolve {
        id: solvePopup
    }

    PopupExport {
        id: exportPopup
    }
}
