import QtQuick 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Controls.Material.impl 2.13
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.13

Popup {
    id: popup
    //property alias stackLayout: stackLayout
    //contentWidth: stackLayout.layer.
    //contentHeight: columnLayout.implicitHeight
    rightPadding: 20
    bottomPadding: 10
    leftPadding: 20
    topPadding: 20
    anchors.centerIn: parent
    //anchors.fill: parent
    modal: true
    focus: true
    closePolicy: Popup.NoAutoClose

    onAboutToHide: {
        textFieldNInput.text = ""
        //todo return all on hide
        //if(!ma.containsMouse) {
        //    console.log("click outside: commit the changes")
        // }
    }

    background: Rectangle {
        radius: 5
        anchors.fill: parent
        color: Material.color(Material.Grey, Material.Shade100)
    }

    ColumnLayout {
        //maximumHeight: parent.height - 100
        anchors.rightMargin: -1
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.fill: parent
        RowLayout {
            transformOrigin: Item.Center
            spacing: 0
            Layout.fillWidth: true
            Label {
                font.pointSize: 14
                Layout.topMargin: -20
                anchors.right: parent.right
                anchors.left: parent.left
                text: "Решить для N = "
                color: Material.color(Material.Grey, Material.Shade800)
                font.weight: Font.DemiBold
                Layout.alignment: Qt.AlignLeft | Qt.Top
            }
            TextField {
                Layout.topMargin: -10
                font.weight: Font.DemiBold
                color: Material.primary
                id: textFieldNInput
                maximumLength: 10
                Layout.alignment: Qt.AlignLeft | Qt.Top
                placeholderTextColor: Material.color(Material.Indigo,
                                                     Material.Shade100)
                placeholderText: qsTr("Введите N")
                background: null
                selectByMouse: true
                font.pointSize: 14
            }
        }

        MenuSeparator {
            Layout.fillWidth: true
            Layout.topMargin: -20
            topPadding: 0
            bottomPadding: 0
            contentItem: Rectangle {
                implicitWidth: 200
                implicitHeight: 3
                color: "#3F51B5"
            }
        }
        Label {
            id: labelSolveStatus
            text: qsTr("Подсчет возвращаемого значения (или вывода)\nвведенных рекурсий для заданного N.")
            color: Material.color(Material.Grey, Material.Shade600)
            bottomPadding: 0
            topPadding: 7
            visible: false

            anchors.right: parent.right
            anchors.left: parent.left
            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
            font.pointSize: 12
        }


        /*ColumnLayout {
            anchors.right: parent.right
            anchors.left: parent.left
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            anchors.verticalCenter: parent.verticalCenter
            spacing: 5*/

        //todo add load from file and delete buttons (like yandex translate has)
        Label {
            color: Material.accent
            text: "Вывод программы"
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            font.pointSize: 12
            font.bold: true
        }
        ScrollView {
            id: scrollViewResult
            Layout.maximumHeight: appHeight - 275
            Layout.maximumWidth: appWidth - 50
            anchors.right: parent.right
            anchors.left: parent.left

            // Layout.fillWidth: true
            //anchors.left: parent.left
            //anchors.right: scrollViewResult.left
            TextArea {

                id: textSolveResult
                text: ""
                color: Material.color(Material.Grey, Material.Shade800)
                placeholderText: ""
                background: null
                readOnly: true
                selectByKeyboard: true
                selectByMouse: true
                font.pointSize: 9
            }
        }

        //}
        RowLayout {
            spacing: 25
            Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
            Button {
                //Material.background: Material.primary
                id: helpButton
                text: qsTr("Подсчитать")
                font.weight: Font.DemiBold
                font.capitalization: Font.MixedCase
                flat: true
                Material.foreground: Material.Green
                font.pointSize: 10
                Layout.alignment: Qt.AlignRight | Qt.AlignTop
                display: AbstractButton.TextOnly
                TapHandler {
                    onTapped: {
                        if (textFieldNInput.text == "") {
                            errorText = "nInputEmptyError"
                            popupError.open()
                            //PopupEmptyInput
                            // popupEmptyInput.open();
                        } else {
                            converter.countValue(textFieldNInput.text,
                                                 textAreaInput.text,
                                                 isPythonToMath)
                        }
                        //popup.close() //todo open help menu
                    }
                }
            }
            Button {
                id: okButton
                text: qsTr("Закрыть")
                font.weight: Font.DemiBold
                font.capitalization: Font.MixedCase
                flat: true
                Material.foreground: Material.primary
                font.pointSize: 10
                Layout.alignment: Qt.AlignRight | Qt.AlignTop
                display: AbstractButton.TextOnly
                TapHandler {
                    onTapped: popup.close()
                }
            }
        }
    }

    Connections {
        target: converter

        //count for n result here
        onCountValueResult: {
            //textAreaOutput.text = "onCountValueResult";
            //labelSolvePlaceholder.text = countValue[0]
            //textSolveCode.text = countValue[0]
            textSolveResult.text = countValue;
            //labelSolvePlaceholder.text = countValue
            //textAreaOutput.text = countValue;


            /*if (countValue == "nNotIntError")  //error converting python to math, wrong input
            {
                textAreaOutput.text = "";
                errorText = "nNotIntError";
               // popupError.
                popupError.open();
                //popupPyToMathError.open()
            }
            else  //success*/
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:1;anchors_height:100;anchors_width:100}
D{i:3;anchors_height:100;anchors_width:100}D{i:5;anchors_height:100;anchors_width:100}
D{i:4;anchors_height:100;anchors_width:100}
}
##^##*/

