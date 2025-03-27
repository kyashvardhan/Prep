import cv2
import os
import argparse
from pathlib import Path

def detect_and_crop_faces(image_path, output_dir, face_cascade):
    img = cv2.imread(str(image_path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    cropped_faces = 0

    for idx, (x, y, w, h) in enumerate(faces):
        face = img[y:y+h, x:x+w]
        output_path = output_dir / f"{image_path.stem}_face_{idx+1}.jpg"
        cv2.imwrite(str(output_path), face)
        cropped_faces += 1

    return cropped_faces

def batch_process(input_dir, output_dir):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    total_faces = 0
    for image_file in input_dir.glob("*.*"):
        faces = detect_and_crop_faces(image_file, output_dir, face_cascade)
        print(f"Processed {image_file.name}: Found {faces} faces.")
        total_faces += faces

    print(f"\nTotal faces cropped: {total_faces}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch face detection and cropping.")
    parser.add_argument("--input", required=True, help="Input directory containing images")
    parser.add_argument("--output", required=True, help="Output directory for cropped faces")
    args = parser.parse_args()

    batch_process(args.input, args.output)
