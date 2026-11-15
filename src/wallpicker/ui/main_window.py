from pathlib import Path

from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QFileDialog, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QVBoxLayout, QWidget,
)

from ui.styles import DARK_THEME

RESOURCES = Path(__file__).resolve().parent.parent / "resources"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("Wallpicker")
        self.resize(960, 600)
        self.setMinimumSize(760, 460)
        self.setStyleSheet(DARK_THEME)

        root = QWidget()
        root.setObjectName("root")
        self.setCentralWidget(root)

        outer = QVBoxLayout(root)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)
        outer.addWidget(self._build_titlebar())

        body = QWidget()
        body_row = QHBoxLayout(body)
        body_row.setContentsMargins(0, 0, 0, 0)
        body_row.setSpacing(0)
        body_row.addWidget(self._build_sidebar())
        body_row.addWidget(self._build_main(), 1)
        outer.addWidget(body, 1)

        outer.addWidget(self._build_statusbar())

        # Wire the title bar (must come after the UI is built)
        self.min_button.clicked.connect(self.showMinimized)
        self.max_button.clicked.connect(self.toggle_maximize)
        self.close_button.clicked.connect(self.close)
        self.titlebar.installEventFilter(self)

    # ---------- Title bar ----------
    def _build_titlebar(self):
        self.titlebar = QFrame()
        self.titlebar.setObjectName("titleBar")
        self.titlebar.setFixedHeight(40)

        row = QHBoxLayout(self.titlebar)
        row.setContentsMargins(16, 0, 0, 0)  # controls touch the right edge
        row.setSpacing(10)

        logo = QLabel()
        logo.setFixedSize(24, 24)
        logo.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(str(RESOURCES / "logo.png"))
        if pixmap.isNull():
            logo.setText("X")
            logo.setObjectName("logoPlaceholder")
        else:
            logo.setPixmap(
                pixmap.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )

        title = QLabel("Wallpicker")
        title.setObjectName("appTitle")

        self.min_button = QPushButton("\uE921")
        self.max_button = QPushButton("\uE922")  # "\uE923" = restore icon
        self.close_button = QPushButton("\uE8BB")
        self.min_button.setObjectName("winButton")
        self.max_button.setObjectName("winButton")
        self.close_button.setObjectName("closeButton")
        self.min_button.setToolTip("Minimize")
        self.max_button.setToolTip("Maximize")
        self.close_button.setToolTip("Close")
        for button in (self.min_button, self.max_button, self.close_button):
            button.setFixedSize(46, 40)
            button.setFocusPolicy(Qt.NoFocus)

        row.addWidget(logo)
        row.addWidget(title)
        row.addStretch()
        row.addWidget(self.min_button)
        row.addWidget(self.max_button)
        row.addWidget(self.close_button)
        return self.titlebar

    # ---------- Sidebar ----------
    def _build_sidebar(self):
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(216)

        col = QVBoxLayout(sidebar)
        col.setContentsMargins(12, 16, 12, 12)
        col.setSpacing(6)

        library = QLabel("LIBRARY")
        library.setObjectName("category")
        library.setContentsMargins(4, 0, 0, 0)

        active = QFrame()
        active.setObjectName("navItemActive")
        active.setFixedHeight(36)
        active_row = QHBoxLayout(active)
        active_row.setContentsMargins(12, 0, 10, 0)
        text = QLabel("All Wallpapers")
        text.setObjectName("navActiveText")
        self.count_badge = QLabel("0")
        self.count_badge.setObjectName("navBadge")
        self.count_badge.setFixedHeight(18)
        self.count_badge.setAlignment(Qt.AlignCenter)
        active_row.addWidget(text)
        active_row.addStretch()
        active_row.addWidget(self.count_badge)

        collections = QLabel("COLLECTIONS")
        collections.setObjectName("category")
        collections.setContentsMargins(4, 0, 0, 0)

        hint = QLabel("Custom collections will appear here.")
        hint.setObjectName("sidebarHint")
        hint.setWordWrap(True)
        hint.setContentsMargins(4, 0, 4, 0)

        col.addWidget(library)
        col.addWidget(active)
        col.addSpacing(14)
        col.addWidget(collections)
        col.addWidget(hint)
        col.addStretch()
        return sidebar

    # ---------- Main panel ----------
    def _build_main(self):
        panel = QFrame()
        panel.setObjectName("mainPanel")

        col = QVBoxLayout(panel)
        col.setContentsMargins(20, 16, 20, 16)
        col.setSpacing(14)

        col.addWidget(self._build_toolbar())

        self.empty_state = self._build_empty_state()
        col.addWidget(self.empty_state, 1)

        self.grid_placeholder = self._build_grid_placeholder()
        self.grid_placeholder.hide()
        col.addWidget(self.grid_placeholder, 1)

        col.addWidget(self._build_action_bar())
        return panel

    def _build_toolbar(self):
        toolbar = QWidget()
        toolbar.setFixedHeight(40)

        row = QHBoxLayout(toolbar)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(12)

        self.folder_section = self._build_folder_section()
        self.folder_section.hide()

        self.add_button = QPushButton("+  Add Folder")
        self.add_button.setObjectName("addButton")
        self.add_button.setFixedSize(124, 34)
        self.add_button.setCursor(Qt.PointingHandCursor)
        self.add_button.clicked.connect(self.select_folder)

        row.addWidget(self.folder_section)
        row.addStretch()
        row.addWidget(self.add_button)
        return toolbar

    def _build_folder_section(self):
        section = QWidget()
        col = QVBoxLayout(section)
        col.setContentsMargins(0, 0, 0, 0)
        col.setSpacing(2)

        self.folder_name = QLabel()
        self.folder_name.setObjectName("folderName")
        self.folder_path = QLabel()
        self.folder_path.setObjectName("folderPath")

        col.addWidget(self.folder_name)
        col.addWidget(self.folder_path)
        return section

    def _build_empty_state(self):
        card = QFrame()
        card.setObjectName("emptyState")

        col = QVBoxLayout(card)
        col.setAlignment(Qt.AlignCenter)
        col.setSpacing(6)

        art = QLabel("X")  # TODO: replace with resources/empty_state.png
        art.setObjectName("illustrationPlaceholder")
        art.setFixedSize(56, 56)
        art.setAlignment(Qt.AlignCenter)

        title = QLabel("No folder selected")
        title.setObjectName("emptyTitle")
        subtitle = QLabel("Click Add Folder to get started.")
        subtitle.setObjectName("emptySubtitle")

        col.addWidget(art, alignment=Qt.AlignHCenter)
        col.addWidget(title, alignment=Qt.AlignHCenter)
        col.addWidget(subtitle, alignment=Qt.AlignHCenter)
        return card

    def _build_grid_placeholder(self):
        frame = QFrame()
        frame.setObjectName("gridPlaceholder")
        col = QVBoxLayout(frame)
        col.setAlignment(Qt.AlignCenter)
        note = QLabel("Thumbnail grid goes here (Phase D)")
        note.setObjectName("emptySubtitle")
        col.addWidget(note, alignment=Qt.AlignHCenter)
        return frame

    def _build_action_bar(self):
        bar = QFrame()
        bar.setObjectName("actionBar")
        bar.setFixedHeight(52)

        row = QHBoxLayout(bar)
        row.setContentsMargins(16, 0, 10, 0)
        row.setSpacing(8)

        self.selection_label = QLabel("No wallpaper selected")
        self.selection_label.setObjectName("selectionLabel")

        self.preview_button = QPushButton("Preview")
        self.preview_button.setFixedHeight(32)
        self.preview_button.setEnabled(False)  # enabled in Phase E

        self.set_button = QPushButton("Set as Wallpaper")
        self.set_button.setObjectName("primaryButton")
        self.set_button.setFixedHeight(32)
        self.set_button.setEnabled(False)  # enabled in Phase E

        row.addWidget(self.selection_label)
        row.addStretch()
        row.addWidget(self.preview_button)
        row.addWidget(self.set_button)
        return bar

    # ---------- Status bar ----------
    def _build_statusbar(self):
        bar = QFrame()
        bar.setObjectName("statusBar")
        bar.setFixedHeight(28)

        row = QHBoxLayout(bar)
        row.setContentsMargins(16, 0, 16, 0)

        self.status_label = QLabel("No folder loaded")
        self.status_label.setObjectName("statusText")
        self.status_count = QLabel("0 wallpapers")
        self.status_count.setObjectName("statusText")

        row.addWidget(self.status_label)
        row.addStretch()
        row.addWidget(self.status_count)
        return bar

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def changeEvent(self, event):
        # Keeps the icon correct however the state changed
        # (button, double-click, or Windows snapping)
        if event.type() == QEvent.WindowStateChange:
            self.max_button.setText("\uE923" if self.isMaximized() else "\uE922")
        super().changeEvent(event)

    def eventFilter(self, obj, event):
        if obj is self.titlebar:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.windowHandle().startSystemMove()
                return True
            if event.type() == QEvent.MouseButtonDblClick and event.button() == Qt.LeftButton:
                self.toggle_maximize()
                return True
        return super().eventFilter(obj, event)
    
    # ---- keep your own select_folder method below ----
    def select_folder(self):
        path = QFileDialog.getExistingDirectory(self, "Select Wallpaper Folder")
        if not path:  # user cancelled: keep whatever was selected before
            return

        folder = Path(path)
        self.folder_name.setText(folder.name or str(folder))
        self.folder_path.setText(str(folder))
        self.folder_path.setToolTip(str(folder))

        self.folder_section.show()
        self.empty_state.hide()
        self.grid_placeholder.show()