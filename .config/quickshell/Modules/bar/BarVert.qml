import Quickshell
import Quickshell.Io
import QtQuick
import Quickshell.Hyprland

Scope {
  id: root
  property string time

  Variants {
    // Create a panel for each connect screen (monitor)
    // see https://quickshell.org/docs/v0.3.0/types/Quickshell/Quickshell/#screens
    id: barvert
    model: Quickshell.screens 

    // this is used with IPC (see IpcHandler below) to toggle bar visibility on/off
    property bool barVisible: true

    PanelWindow {
      required property var modelData
      screen: modelData

      visible: barvert.barVisible
      anchors {
        top: true
        left: true
        right: false
        bottom: true
      }
      margins {
        top: 0
        left: 0
        right: 0
        bottom: 0
      }
      implicitWidth: 40
      
      // this is necessary to differentiate which screen has focus and style each bar respectively
      // can maybe be simplified at some point. See docs on screen and monitor objects 
      property bool barActive: {
          const activeWs = Hyprland.focusedWorkspace
          if (!activeWs) return false
          
          const screenMon = screen.name || screen.id || screen.output || screen.outputName
          const wsMonitor = activeWs.monitor?.name || activeWs.monitor?.id || activeWs.output?.name || activeWs.output?.id
          
          return screenMon !== undefined && wsMonitor !== undefined && screenMon === wsMonitor
      }
      color: Colors.bg
      
      WorkspaceIndicator { screenActive: barActive }

    }

  }

  IpcHandler {
    target: "barvert"

    // toggle bar visibility - call this in shell or keybind with: 
    // $ qs ipc call barvert toggleVisible
    function getVisible(): bool { return barvert.barVisible; }
    function toggleVisible(): void { barvert.barVisible = !getVisible(); }


  }

}

