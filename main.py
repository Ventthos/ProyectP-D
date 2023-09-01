import sys

from PyQt5.uic.properties import QtCore
from PySide6.QtGui import QAction, QPixmap, QFontDatabase, Qt
from PySide6.QtWidgets import *
import pytube
import os
import eyed3
from eyed3.id3.frames import ImageFrame
from moviepy.editor import *
import urllib.request
from tkinter import filedialog

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proyect_P&D")
        self.resize(1200, 720)
        QFontDatabase.addApplicationFont("font\\Donkin.otf")
        self.posicionarElementosDescargas()
        with open("styles.qss", "r") as styles_file:
            styles = styles_file.read()
            events.setStyleSheet(styles)


    def posicionarElementosDescargas(self):
        #Declaracion de elementos principal
        self.layoutPrincipalDesc = QVBoxLayout()
        self.layoutPrincipalDesc.setContentsMargins(100, 0, 100, 100)
        self.widgetPrincipalDesc = QWidget()
        self.widgetPrincipalDesc.setLayout(self.layoutPrincipalDesc)
        self.setCentralWidget(self.widgetPrincipalDesc)

        #Dentro del widget principal
        self.labelTituloDesc = QLabel("Descargador")
        self.labelTituloDesc.setObjectName("labelTituloDesc")
        self.labelTituloDesc.setAlignment(Qt.AlignCenter)
        self.layoutPrincipalDesc.addWidget(self.labelTituloDesc, stretch=1)
        self.contenedorCancionDesc = QHBoxLayout()
        self.layoutPrincipalDesc.addLayout(self.contenedorCancionDesc, stretch=5)
        self.fondoInfoCancionDesc = QWidget()
        self.fondoInfoCancionDesc.setObjectName("fondoInfoCancionDesc")

        self.contenedorCancionDesc.addWidget(self.fondoInfoCancionDesc)

        self.contenedorCancionesInt= QVBoxLayout()
        self.fondoInfoCancionDesc.setLayout(self.contenedorCancionesInt)

        #Configurar barra y el widget de abajo
        self.barraBuscador = QLineEdit()
        self.barraBuscador.setPlaceholderText("URL")
        self.barraBuscador.setObjectName("barraBuscador")

        self.contenedorUtilCanciones = QHBoxLayout()
        self.contenedorCancionesInt.setObjectName("contenedorCancionesInt")


        self.contenedorCancionesInt.addWidget(self.barraBuscador, stretch=1)
        self.contenedorCancionesInt.addLayout(self.contenedorUtilCanciones, stretch=5)

        #Configuracion de la imagen
        self.cancionImagenDesc = QLabel()
        self.cancionImagenDesc.setPixmap(QPixmap("img\\images.jpg"))
        self.cancionImagenDesc.setScaledContents(True)
        self.cancionImagenDesc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.cancionImagenDesc.setObjectName("cancionImagenDesc")
        self.contenedorUtilCanciones.addWidget(self.cancionImagenDesc)

        self.layoutInfoDesc = QVBoxLayout()
        self.contenedorUtilCanciones.addLayout(self.layoutInfoDesc)

        self.tituloTituloDesc = QLabel("Título")
        self.tituloTituloDesc.setObjectName("tituloDesc")
        self.entryTituloDesc = QLineEdit()
        self.entryTituloDesc.setObjectName("entryDesc")

        self.tituloArtistaDesc = QLabel("Artista")
        self.tituloArtistaDesc.setObjectName("tituloDesc")
        self.entryArtistaDesc = QLineEdit()
        self.entryArtistaDesc.setObjectName("entryDesc")


        self.tituloAlbumDesc = QLabel("Álbum")
        self.tituloAlbumDesc.setObjectName("tituloDesc")
        self.entryAlbumDesc = QLineEdit()
        self.entryAlbumDesc.setObjectName("entryDesc")


        self.botonDescarga = QPushButton("Descargar")
        self.botonDescarga.setObjectName("botonDescarga")
        self.botonDescarga.clicked.connect(self.GetVideo)

        self.layoutInfoDesc.addWidget(self.tituloTituloDesc)
        self.layoutInfoDesc.addWidget(self.entryTituloDesc)
        self.layoutInfoDesc.addWidget(self.tituloArtistaDesc)
        self.layoutInfoDesc.addWidget(self.entryArtistaDesc)
        self.layoutInfoDesc.addWidget(self.tituloAlbumDesc)
        self.layoutInfoDesc.addWidget(self.entryAlbumDesc)
        self.layoutInfoDesc.addWidget(self.botonDescarga)

    def GetVideo(self):
        link = self.barraBuscador.text()
        obj = pytube.YouTube(link)
        self.entryTituloDesc.setText(obj.title)
        self.entryArtistaDesc.setText(obj.author)
        self.entryAlbumDesc.setText("Single")

        #Get and set the image from internet
        urllib.request.urlretrieve(obj.thumbnail_url, "thumb.png")
        imageDesc = QPixmap("thumb.png")
        imageDesc = imageDesc.scaled(400, 400, Qt. IgnoreAspectRatio)
        imageDesc.save("thumb.png", "PNG")
        self.cancionImagenDesc.setPixmap(imageDesc)


        """""
        artistaInput.delete(0, END)
        artistaInput.insert(0, obj.author)
        albumInput.delete(0, END)
        albumInput.insert(0, "Single")

        if (duracionCon := obj.length % 60) >= 10:
            duracionMin = f"{obj.length // 60}:{duracionCon}"
        else:
            duracionMin = f"{obj.length // 60}:0{duracionCon}"

        longText2.config(text=duracionMin)

        print(obj.vid_info)
        urllib.request.urlretrieve(obj.thumbnail_url, "thumb.png")
        thumbnailraw = Image.open("thumb.png")
        thumbnailraw = thumbnailraw.resize((350, 350))
        thumbnailraw.save("thumb.png")
        thumbnail = ImageTk.PhotoImage(thumbnailraw, Image.ANTIALIAS)

        labelImage.config(image=thumbnail)
        labelImage.image = thumbnail
    """

    #def setStyles(self):




if __name__ == "__main__":
    events = QApplication()
    ventanaPrincipal = VentanaPrincipal()
    ventanaPrincipal.show()
    sys.exit(events.exec())