class WinButton: pass
class MacButton: pass
class WinClock: pass
class MacClock: pass

class GUIFactory:
    def __init__(self, os_type):
        self.os_type = os_type
    
    def keyboard_button(self):
        return WinButton() if self.os_type == "windows" else MacButton()
    
    def clock_button(self):
        return WinClock() if self.os_type == "windows" else MacClock()