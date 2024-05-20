# Folder taskı

# 1) Ilk olaraq bir "Example" adında bir kateqoriya (directory) yaradırıq.
# 2)Daha sonra isə bu directorynin içərisində bir  "subdirect"  adında alt kateqoriya(subdirectory) yaradırıq.
# 3)Növbəti addımda bu subdirectorynin içərisinə  bir şəkil və bir text faylı əlavə edirik. 
# (şəkli ilk öncə manual olaraq hal hazırda olduğunuz qovluğun içərisinə sürüşdürüb  daha sonra alt kateqoriyaya əlavə edin, path-ini tapmağda çətinlik çəkməmək üçün)
# 4)daha sonra isə subdirectorynin içərisində olub sonu txt ilə bitən faylları subdirectorydən çıxarıb Example directory-sinə göndərirsiniz.


import os
import shutil

os.makedirs("Example", exist_ok=True)

os.makedirs("Example/subdirect", exist_ok=True)


image_path = "indir.jpeg"
destination_image_path = os.path.join("Example", "subdirect", os.path.basename(image_path))

shutil.copy(image_path, destination_image_path)


text_file_path = os.path.join("Example", "subdirect", "file.txt")
with open(text_file_path, "w") as f:
    f.write("Demo text fayl.")

subdirect_path = os.path.join("Example", "subdirect")
example_path = os.path.join("Example")

for file_name in os.listdir(subdirect_path):
    if file_name.endswith(".txt"):
        full_file_path = os.path.join(subdirect_path, file_name)
        shutil.move(full_file_path, example_path)

print("Done")
