import QtQuick
import Quickshell.Hyprland
import "."

// Layout things in a column automatically
Column {
    id: column

    // screenActive is true if current monitor is focused
    required property bool screenActive
    readonly property var cornerRadius: 10
    readonly property var accentPrimary: Colors.green
    readonly property var accentSecondary: Colors.teal

    spacing: 7
    anchors.margins: 7
    anchors.fill: parent

    property var workspaceIcons: [
        "\ue795",               // 1
        "\uf07c",               // 2
        "\uf269",               // 3
        "\ue780",               // 4
        "\uf02d",               // 5
        "\ue70f",               // 6
        "\udb80\uddee",         // 7
        "\uf1b6",               // 8
        "\uF025",               // 9
        "\udb82\udf7b",         // 0
		"\udb80\udfea",			// 11
		"\udb80\udf74"			// 12
    ]

    Repeater {
        model: 12  // Show workspaces 1-10. Each one gets an "index", starts at 0

        // container box for each icon
        Rectangle {
            property var ws: Hyprland.workspaces.values.find(w => w.id === index + 1) // Hyprland workspace object if active (open window present)
            property bool wsActive: Hyprland.focusedWorkspace?.id === (index + 1) // globally focused workspace

            // this is all copilot stuff to get focused monitor stuff working 
            property var wsMonitor: ws?.monitor?.name || ws?.monitor?.id || ws?.output?.name || ws?.output?.id
            property var focusedMonitorId: Hyprland.focusedMonitor?.name || Hyprland.focusedMonitor?.id || Hyprland.focusedMonitor?.output?.name || Hyprland.focusedMonitor?.output?.id || Hyprland.focusedWorkspace?.monitor?.name || Hyprland.focusedWorkspace?.monitor?.id || Hyprland.focusedWorkspace?.output?.name || Hyprland.focusedWorkspace?.output?.id
            property bool wsOnFocusedMonitor: ws && wsMonitor !== undefined && focusedMonitorId !== undefined && wsMonitor === focusedMonitorId

            antialiasing: true
            anchors.horizontalCenter: parent.horizontalCenter
            width: 25
            height: 25
            radius: cornerRadius
            border.width: 1

            // color styling for each workspace indicator (rectangle plus text icon)
            property color bgColor: {
                if (!ws) return Colors.transparent //default (inactive)
                if (!wsOnFocusedMonitor) return Colors.transparent
                if (!wsActive) return Colors.transparent
                if (!screenActive) return Colors.overlay0
                return Colors.text 
            }
            property color borderColor: {
                if (!ws) return Colors.transparent //default (inactive)
                if (!screenActive) return Colors.overlay2 //shows which screen is active
                if (wsOnFocusedMonitor) return Colors.text //shows which workspaces are on which monitor
                if (!wsActive) return Colors.transparent
                // return Colors.text 
            }
            property color textColor: {
                if (!ws) return Colors.surface2     //default (inactive)
                if (!wsActive) return Colors.text   //active workspaces 
                if (!screenActive) return Colors.text //shows which screen is active
                return Colors.bg                    //focused 
            }

            color: bgColor
            border.color: borderColor

            Text {
                color: textColor
                anchors.centerIn: parent
                text: workspaceIcons[index]
                font { pixelSize: 14; bold: true }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: Hyprland.dispatch(`hl.dsp.focus({ workspace = ${index + 1} })`)
            }
        }
    }
}
