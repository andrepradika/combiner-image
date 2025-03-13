# 🛋️ Image Combiner  

## 📌 About  

**Image Combiner** 🖼️🔗 is a Python script that merges two images—one representing **fabric** and the other a **sofa**—into a single **500x500px composite image**. The script reads a CSV file containing filenames, processes each pair of images, and saves the combined results with a **timestamped filename**.  

## 🚀 Features  

✅ **Batch Processing** – Reads image filenames from a CSV file and processes multiple pairs at once.  
✅ **Automated Image Merging** – Stacks fabric (bottom) and sofa (top) into a new composite image.  
✅ **Timestamped Filenames** – Ensures unique output filenames using the current timestamp.  
✅ **CSV File Update** – Updates the CSV file with the generated image filenames.  

---

## 📦 Installation  

1. **Clone this repository**  

   ```bash
   git clone https://github.com/andrepradika/combiner-image.git
   cd combiner-image
   ```

2. **Install dependencies**  

   ```bash
   pip install pillow
   ```

---

## 🛠️ Usage  

1. **Prepare the required folders and files**  
   - Place **fabric images** in the `file_1/` folder.  
   - Place **sofa images** in the `file_2/` folder.  
   - Ensure the `data.csv` file contains:  

     ```csv
     file_1;file_2
     fabric1.jpg;sofa1.jpg
     fabric2.png;sofa2.png
     ```

2. **Run the script**  

   ```bash
   python main.py
   ```

3. **Check the results**  
   - Combined images are saved in the `output_images/` folder.  
   - `data.csv` is updated with the result filenames.  

---

## 📂 File Structure  

```
image-combiner/
│── file_1/              # Folder containing fabric images
│── file_2/              # Folder containing sofa images
│── output_images/       # Folder where combined images are saved
│── data.csv             # CSV file with input filenames
│── main.py              # Main script
│── README.md            # Documentation
```

---

## 📝 Example Output  

A **fabric** image and a **sofa** image are stacked into a **new composite image** like this:  

🛋️ **Sofa (top)**  
🧵 **Fabric (bottom)**  

---

## 🏷️ Topics  

📄 **CSV Processing** – Reads and updates a CSV file for batch processing.  
🖼️ **Image Manipulation** – Uses `Pillow` to resize and merge images.  
⚡ **Automation** – Automatically combines multiple image pairs.  
🐍 **Python** – Simple, lightweight script for quick processing.  

---

## 📜 License  

This project is open-source under the **MIT License**.  

## Author
andrepradika