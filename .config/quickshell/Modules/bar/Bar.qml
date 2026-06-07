import Quickshell
import Quickshell.Io
import QtQuick

Scope {
  id: root
  property string time

  Variants {
    // Create a panel for each connect screen (monitor)
    model: Quickshell.screens

    PanelWindow {
      // id: bar
      required property var modelData
      screen: modelData

      anchors {
        top: true
        left: true
        right: true
        bottom: false
      }
      margins {
        top: 0
        left: 0
        right: 0
        bottom: 0
      }
       
      color: "black"

      implicitHeight: 40

      Rectangle {
        id : bar

      }

      SystemClock {
        id: clock
        precision: SystemClock.Minutes
      }

      Text {
        anchors.centerIn: parent
        color: "white"
        text: Qt.formatDateTime(clock.date, "hh:mm:ss | ddd dd MMM")
        // text: root.time
      }
    }
  }

}

