
# OCR-and-Document-Search-Web-Application-Prototype

## Objective:
To create a OCR and Document search web application where the user will upload a single image containing english and hindi text it must detect those from the image and display them either as plain text or json format. The web
application must also have a document search feature. A simple keyword will be given as input if the provided keyword is present, then display an appropriate message and highlight the keyword in the output.

The website is hosted using Hugging Face Spaces. Try it out [here](https://huggingface.co/spaces/Arch10/OCR).

## Approach

1. **OCR Functionality**:  
   The application utilizes a hybrid approach for detecting text in both **English** and **Hindi**. The models used are:
   - **EasyOCR**: Primarily used for accurate **Hindi text** detection.
   - **General OCR Theory (GOT)**: This model excels at detecting English text but struggles with Hindi. Custom training efforts were made but faced challenges due to resource constraints,config/param mismatch. 

   These two models complement each other, providing accurate recognition for both languages.

2. **Document Search**:  
   After text extraction, users can input a keyword to search within the extracted text. If the keyword is found, it is highlighted in the output.

3. **Gradio Interface**:  
   A user-friendly interface has been built using **Gradio**, allowing users to upload images and retrieve text effortlessly.

4. **ColPali + Qwen2VL7BInstruct**:  
   An alternative approach using **ColPali** (via the **Byaldi** library) and **Qwen2VL7BInstruct** was tested. This approach initially faced issues with configuration and memory, but after optimization, produced satisfactory results. However, resource limitations (RAM/CUDA) restricted its use in the final deployment. Locally, this implementation can be run using **Qwen2VLForConditionalGeneration** and **AutoProcessor**.

## Technologies and Libraries Used:

- **Python**: Primary programming language used for developing the application.
- **EasyOCR**: For OCR tasks involving Hindi text detection.
- **Hugging Face Transformers**: Used for the General OCR Theory (GOT) model and Qwen2VL for multi-modal processing.
- **Gradio**: For building an easy-to-use web interface.
- **Hugging Face Spaces**: Deployed the application on this platform.

## How to Use:

1. Clone the repository:
    ```sh
    git clone https://github.com/ArchismwanChatterjee/OCR-and-Document-Search-Web-Application-Prototype.git
    ```
2. Install the required libraries (for app.py):
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. To execute the `ColPali+Qwen2VL_approach.ipynb` or `OCR_and_Document_Search_Web_Application_using_Gradio.ipynb`, use a platform like Google Colab or any GPU runtime, ensuring that a GPU is connected. Follow the instructions provided within the notebook files.

## Deployment:

The application has been deployed on **Hugging Face Spaces**. To deploy your own instance, follow these steps:

1. **Create a Hugging Face Account**:  
   Sign up on [Hugging Face](https://huggingface.co/join) to create an account.

2. **Create a New Space**:  
   Navigate to the Spaces tab and create a new Space. Select **Gradio** as the interface type.

3. **Upload the Code**:  
   Upload your project files (such as `app.py` and `requirements.txt`) into the Space.

4. **Set Up Dependencies**:  
   In the Space settings, specify the dependencies listed in the `requirements.txt` file.

5. **Run the Application**:  
   Click "Run" to launch your application. If the application requires GPU support (like for GOT), you'll need a premium plan on Hugging Face.

For more details, visit the [Hugging Face Space Documentation](https://huggingface.co/docs/spaces).

## References:

1. [Smol Vision - GitHub](https://github.com/merveenoyan/smol-vision)
2. [GOT-OCR2.0 - GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0)
