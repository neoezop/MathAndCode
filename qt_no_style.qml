import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Window 2.3
ApplicationWindow{
    title: qsTr('Qml app')
    id: mainWindow
    width:  800
    height: 600
    visible: true

    Row {
        id: row
        x: 281
        y: 78
        width: 709
        height: 442
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        transformOrigin: Item.Center

        Column {
            id: column
            width: 200
            height: 400

            ComboBox {
                id: comboBox
                anchors.right: parent.right
                anchors.left: parent.left
                anchors.top: parent.top
                model: ["1 тип","2 тип","3 тип"]
            }

            TextEdit {
                id: textEdit
                text: qsTr("Text Input")
                anchors.top: comboBox.bottom
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.left: parent.left
                anchors.topMargin: 0
                font.pixelSize: 12
            }
        }
    }


}
