import QtQuick
import Quickshell.Hyprland
import "."

// Layout things in a column automatically
Column {
    id: column

    // screenActive is true if current monitor is focused
    required property bool screenActive

    spacing: 7
    anchors.margins: 7
    readonly property var cornerRadius: 10
    readonly property var accentPrimary: Colors.green
    readonly property var accentSecondary: Colors.teal
    anchors.fill: parent

    property var workspaceIcons: [
        "\ue795",
        "\uf07c",
        "\uf269",
        "\ue780",
        "\udb80\udf31",
        "\uf02d",
        "\udb80\uddee",
        "\uf1b6",
        "\uF025",
        "\udb82\udf7b",
    ]

    Repeater {
        model: 10  // Show workspaces 1-10. Each one gets an "index", starts at 0

        // container box for each icon
        Rectangle {
            property var ws: Hyprland.workspaces.values.find(w => w.id === index + 1) // workspace object if active
            property bool wsActive: Hyprland.focusedWorkspace?.id === (index + 1) // globally focused workspace

            antialiasing: true
            anchors.horizontalCenter: parent.horizontalCenter
            width: 25
            height: 25
            radius: cornerRadius
            border.width: 1

            color: screenActive ? (wsActive ? Colors.text : Colors.bg) : (wsActive ? Colors.surface2 : Colors.bg)
            border.color: ws ? (screenActive ? ( wsActive ? Colors.text : Colors.surface2) : Colors.surface2) : Colors.transparent

            Text {
                anchors.centerIn: parent
                text: workspaceIcons[index]
                color: screenActive ? (wsActive ? Colors.bg : Colors.overlay0) : (wsActive ? Colors.bg : Colors.surface2)
                font { pixelSize: 14; bold: true }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: Hyprland.dispatch(`hl.dsp.focus({ workspace = ${index + 1} })`)
            }
        }
    }
}
