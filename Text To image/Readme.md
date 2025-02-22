# 🚀 Image Generation with Pre-trained Models

Welcome to the **Image Generation with Pre-trained Models** repository! This project demonstrates how to utilize pre-trained generative models like Stable Diffusion to create images from text prompts. These models enable the generation of high-quality images by leveraging powerful deep learning architectures trained on extensive datasets.

## 📖 Table of Contents
- Introduction
- Getting Started
- Prerequisites
- Installation
- Usage
  - Generating Images
  - Examples
- Models
  - Stable Diffusion
- 🤝 Contributing
- 📜 License
- 🙌 Acknowledgements

## 🌟 Introduction
This repository provides a framework for generating images from text prompts using pre-trained generative models. It covers how to use **Stable Diffusion** to create visuals directly from text descriptions. Whether you're an AI enthusiast, a developer, or a designer, this project offers a hands-on approach to exploring the capabilities of generative AI.

## 🛠 Getting Started

### ✅ Prerequisites
Before you begin, ensure you have the following installed:

- **Python 3.7+**
- **Git**
- **Virtualenv** (optional but recommended)

### 📥 Installation
#### 🔹 Clone the Repository
```sh
git clone https://github.com/your-username/image-generation-pretrained-models.git
cd image-generation-pretrained-models
```

## 🎨 Usage

### 🖼 Example Output Image
Below is an example of an image generated using this script:

![Example Output](example_output.png)

### 🏗 Generating Images
Run the following script to generate an image from a text prompt:

```python
import torch
from diffusers import StableDiffusionPipeline
import time

def generate_image(prompt, model_id="CompVis/stable-diffusion-v1-4"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe = pipe.to(device)
    with torch.no_grad():
        image = pipe(prompt).images[0]
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    save_path = f"generated_image_{timestamp}.png"
    image.save(save_path)
    print(f"Image saved to {save_path}")
    return image

if __name__ == "__main__":
    prompt = "A futuristic cityscape at sunset with flying cars and neon lights."
    generated_image = generate_image(prompt)
    generated_image.show()
```

Run the script and check the output folder for the generated image.

---
This document provides an overview and basic instructions to get started with the project. For detailed usage, refer to the documentation inside the repository.
output sample image   ![image](https://github.com/user-attachments/assets/d8cd52e3-4a9c-4865-b938-05379d401024)


