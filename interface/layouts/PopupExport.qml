import QtQuick 2.13
import QtQuick.Controls.Material 2.13
import QtQuick.Dialogs 1.3


FileDialog {
    title: "Экспортировать в файл"
    folder: shortcuts.home
    onAccepted: {
        console.log("You chose: " + fileDialog.fileUrls)
    }
    onRejected: {
        console.log("Canceled")
    }
}

