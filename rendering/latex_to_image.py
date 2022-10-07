import os
"""
Generiert ein auf dem Display darstellbares Bild aus dem generierten Latex string.
"""
class LatexToImage:
    filepath = "conversion_file"
    quality = 1000
    
    # schreibt den string in ein Latex file
    def write_to_latex_file(self, tex_string):
        # oeffnet das Latex file und trennt den Formel Teil heraus (Teil zwischen $ und $)
        with open(f"{self.filepath}.tex", "r") as f:
            content = f.read()
            begin, _, end = content.split("$")
        # schreibt den Latex string in das Dokument und behaelt Anfang und Ende bei.
        with open(f"{self.filepath}.tex", "w") as f:
            f.writelines(f"{begin}${tex_string}${end}")

    # erstellt ein Bild aus dem Latex file
    def convert(self):
        # fuehrt einen Terminal Befehl aug um ein Pdf aus dem Tex file zu erstellen
        os.system(f"pdflatex -interaction=batchmode {self.filepath}.tex")
        # erstellt mit einem Terminal Befehl ein Bild aus dem Pdf
        os.system(f"pdftoppm {self.filepath}.pdf {self.filepath} -png -r {self.quality}")

    # erstellt das Bild und gibt es zurueck
    def make_image(self, tex_string):
        self.write_to_latex_file(tex_string)
        self.convert()
        # das Bild muss noch im richtigen Format zur Darstellung eingelesen werden.
        image = None
        return image



if __name__ == "__main__":
    tex2png = LatexToImage()
    for i in range(100):
        tex2png.make_image("\\alpha \\gamma")
