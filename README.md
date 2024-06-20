# AI Artist 🎨

## Overview

AI Artist is a web application that generates art from user-provided ideas. It uses the Gemini model to enhance the idea and an image generation model to create the artwork. The app is built with Streamlit for a simple and interactive user interface. This project showcases the capabilities of AI in creative processes and can be a valuable addition to your portfolio.

## Features

- Enhance user-provided ideas using the Gemini model.
- Generate images based on enhanced ideas with the ImageGenerator model.
- Download the generated art as a PNG file.
- User-friendly interface with Streamlit.

## Demo

![image](https://github.com/Mr-Vicky-01/AI-Artist/assets/143078285/376eab37-2264-428f-9f46-ffbbda59a762)
Try this app: [Link](https://huggingface.co/spaces/Mr-Vicky-01/AI_Artist)

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mr-Vicky-01/AI-Artist.git
    cd AI-Artist
    ```

2. Install the required libraries:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

### Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the app in your browser and enter your drawing idea.
3. Click "Generate Art" to see the enhanced idea and the generated image.
4. Download the generated art using the provided download button.

## File Structure

- `app.py`: Main application file containing the Streamlit interface.
- `llm.py`: Contains the definition of the `Model` class used for idea enhancement.
- `image_engine.py`: Contains the definition of the `ImageGenerator` class used for image generation.
- `requirements.txt`: Lists the required Python packages for the application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or feedback, feel free to reach out:

- **Email**: pachaiappan1102@gmail.com

## Acknowledgments

- Gemini API for idea enhancement.
- Streamlit for providing an easy-to-use web app framework.
- The open-source community for providing valuable resources and support.
