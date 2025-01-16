import os
import cv2
import numpy as np
from PIL import Image


def process_image(image_path, output_folder, counter):
    # Wczytaj obraz
    img = cv2.imread(image_path)
    if img is None:
        print(f"Nie można otworzyć pliku: {image_path}")
        return

    # Pobierz wymiary obrazu
    h, w, _ = img.shape

    # Ustal maksymalny wymiar obrazu (aby stał się kwadratem)
    max_side = max(h, w)

    # Dodaj marginesy, aby obraz był kwadratem
    square_img = cv2.copyMakeBorder(
        img,
        (max_side - h) // 2,
        (max_side - h + 1) // 2,
        (max_side - w) // 2,
        (max_side - w + 1) // 2,
        cv2.BORDER_CONSTANT,
        value=[255, 255, 255]  # Białe tło
    )

    # Zapisz obraz wyjściowy
    output_path = os.path.join(output_folder, f"square_{counter:03d}.jpg")
    cv2.imwrite(output_path, square_img)


def process_folder(input_path, output_folder):
    counter = 1

    for root, _, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                image_path = os.path.join(root, file)
                try:
                    process_image(image_path, output_folder, counter)
                    counter += 1
                except Exception as e:
                    print(f"Błąd przetwarzania pliku {image_path}: {e}")


def main():
    input_path = input("Podaj ścieżkę do pliku lub folderu wejściowego: ")
    output_folder = input("Podaj ścieżkę do folderu wyjściowego: ")

    # Upewnij się, że folder wyjściowy istnieje
    os.makedirs(output_folder, exist_ok=True)

    if os.path.isfile(input_path):
        print("Przetwarzanie pojedynczego pliku...")
        process_image(input_path, output_folder, 1)
    elif os.path.isdir(input_path):
        print("Przetwarzanie folderu...")
        process_folder(input_path, output_folder)
    else:
        print("Podano nieprawidłową ścieżkę. Sprawdź, czy plik/folder istnieje.")


if __name__ == "__main__":
    main()
