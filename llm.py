import google.generativeai as genai
from dotenv import load_dotenv
import os

    
# Load environment variables
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Define the GeminiModel class for Gemini LLM
class Model:
    def __init__(self) -> None:
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    def enhance_idea(self, idea):
        prompt = """Give me the Pencil art prompt with this idea using this key words [Contrast: Utilize varying shades of gray to create depth and dimension.
                    Texture: Capture the texture of different surfaces like wood, fabric, or skin.
                    Detail: Focus on intricate details to enhance realism.
                    Shading: Use different pencil pressures to create smooth gradients and sharp contrasts.
                    Light and Shadow: Create the illusion of light sources and how they interact with objects.
                    Composition: Arrange elements within the drawing to create a visually appealing layout.
                    Strokes: Experiment with different pencil strokes (e.g., hatching, cross-hatching, stippling) for texture and shading.
                    Negative Space: Use empty areas to define shapes and create balance.], \n Idea: """ + idea + "\n important note: your response must only contain the idea of classic B&W pencil art, without unnecessary elements like ('Enhanced Art Idea:' and markdown format like '##', '*')"
        response = self.model.generate_content([prompt])
        return response.text