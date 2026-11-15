# ---------- Palette (from the design: white / gray / near-black) ----------
WINDOW = "#0d0d0e"
SIDEBAR = "#151516"
MAIN = "#101011"
SURFACE = "#1b1b1d"
SURFACE_HOVER = "#262629"
SURFACE_PRESSED = "#131314"
BORDER = "#2a2a2d"
BORDER_STRONG = "#3d3d41"

TEXT = "#ffffff"
TEXT_NORMAL = "#d6d6d8"
TEXT_MUTED = "#8a8a8e"

ACCENT = "#ffffff"
ACCENT_HOVER = "#e4e4e6"
ACCENT_PRESSED = "#c8c8ca"
ACCENT_TEXT = "#0d0d0e"

# Design fonts: Geist (headline/body), JetBrains Mono (labels).
# Falls back to Windows fonts if they aren't installed.
FONT_UI = '"Geist", "Segoe UI", "Inter", sans-serif'
FONT_LABEL = '"JetBrains Mono", "Cascadia Mono", "Consolas", monospace'

DARK_THEME = f"""
    QMainWindow, QWidget#root {{
        background-color: {WINDOW};
    }}

    QLabel {{
        background: transparent;
        color: {TEXT_NORMAL};
        font-family: {FONT_UI};
        font-size: 13px;
    }}

    /* ---------- Title bar ---------- */
    QFrame#titleBar {{
        background-color: {WINDOW};
    }}
    QLabel#appTitle {{
        color: {TEXT};
        font-size: 14px;
        font-weight: 700;
    }}
    QLabel#logoPlaceholder, QLabel#illustrationPlaceholder {{
        color: {TEXT_MUTED};
        border: 1px dashed {BORDER_STRONG};
        border-radius: 8px;
        font-weight: 700;
    }}

    QPushButton#winButton, QPushButton#closeButton {{
        background-color: transparent;
        color: {TEXT};
        border: none;
        border-radius: 0px;
        padding: 0px;
        font-family: "Segoe MDL2 Assets", "Segoe Fluent Icons";
        font-size: 10px;
        font-weight: 400;
    }}
    QPushButton#winButton:hover {{ background-color: {SURFACE_HOVER}; }}
    QPushButton#winButton:pressed {{ background-color: {SURFACE_PRESSED}; }}
    QPushButton#closeButton:hover {{ background-color: #e81123; color: white; }}
    QPushButton#closeButton:pressed {{ background-color: #b50e1c; color: white; }}

    /* ---------- Sidebar ---------- */
    QFrame#sidebar {{
        background-color: {SIDEBAR};
    }}
    QLabel#category {{
        color: {TEXT_MUTED};
        font-family: {FONT_LABEL};
        font-size: 10px;
        font-weight: 700;
    }}
    QLabel#sidebarHint {{
        color: {TEXT_MUTED};
        font-size: 12px;
    }}
    QFrame#navItemActive {{
        background-color: {ACCENT};
        border-radius: 8px;
    }}
    QLabel#navActiveText {{
        color: {ACCENT_TEXT};
        font-size: 13px;
        font-weight: 700;
    }}
    QLabel#navBadge {{
        background-color: {ACCENT_TEXT};
        color: {TEXT};
        border-radius: 9px;
        padding: 0px 7px;
        font-family: {FONT_LABEL};
        font-size: 10px;
        font-weight: 700;
    }}

    /* ---------- Main panel ---------- */
    QFrame#mainPanel {{
        background-color: {MAIN};
    }}
    QLabel#folderName {{
        color: {TEXT};
        font-size: 15px;
        font-weight: 700;
    }}
    QLabel#folderPath {{
        color: {TEXT_MUTED};
        font-family: {FONT_LABEL};
        font-size: 11px;
    }}
    QLabel#emptyTitle {{
        color: {TEXT};
        font-size: 15px;
        font-weight: 700;
    }}
    QLabel#emptySubtitle {{
        color: {TEXT_MUTED};
        font-size: 12px;
    }}
    QFrame#emptyState {{
        background: transparent;
        border: none;
    }}
    QFrame#gridPlaceholder {{
        background-color: {SURFACE};
        border: 1px dashed {BORDER_STRONG};
        border-radius: 12px;
    }}

    /* ---------- Action bar ---------- */
    QFrame#actionBar {{
        background-color: {SURFACE};
        border-radius: 10px;
    }}
    QLabel#selectionLabel {{
        color: {TEXT_MUTED};
        font-family: {FONT_LABEL};
        font-size: 11px;
    }}

    /* ---------- Status bar ---------- */
    QFrame#statusBar {{
        background-color: {WINDOW};
    }}
    QLabel#statusText {{
        color: {TEXT_MUTED};
        font-family: {FONT_LABEL};
        font-size: 11px;
    }}

    /* ---------- Buttons ---------- */
    QPushButton {{
        background-color: transparent;
        color: {TEXT};
        border: 1px solid {BORDER_STRONG};
        border-radius: 8px;
        padding: 0px 16px;
        font-family: {FONT_UI};
        font-size: 13px;
        font-weight: 600;
    }}
    QPushButton:hover {{
        background-color: {SURFACE_HOVER};
        border-color: {TEXT_MUTED};
    }}
    QPushButton:pressed {{
        background-color: {SURFACE_PRESSED};
    }}
    QPushButton:disabled {{
        color: {TEXT_MUTED};
        border-color: {BORDER};
        background-color: transparent;
    }}

    QPushButton#primaryButton, QPushButton#addButton {{
        background-color: {ACCENT};
        color: {ACCENT_TEXT};
        border: 1px solid {ACCENT};
        font-weight: 700;
    }}
    QPushButton#primaryButton:hover, QPushButton#addButton:hover {{
        background-color: {ACCENT_HOVER};
        border-color: {ACCENT_HOVER};
    }}
    QPushButton#primaryButton:pressed, QPushButton#addButton:pressed {{
        background-color: {ACCENT_PRESSED};
        border-color: {ACCENT_PRESSED};
    }}
    QPushButton#primaryButton:disabled {{
        background-color: {BORDER_STRONG};
        border-color: {BORDER_STRONG};
        color: {TEXT_MUTED};
    }}

    QToolTip {{
        background-color: {SURFACE};
        color: {TEXT};
        border: 1px solid {BORDER};
        padding: 4px 8px;
        font-size: 12px;
    }}
"""