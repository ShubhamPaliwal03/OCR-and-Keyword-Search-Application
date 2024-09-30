import easyocr
import gradio as gr

# function to perform OCR

def perform_ocr(image_path, lang):

    reader = easyocr.Reader([lang])

    result = reader.readtext(image_path)

    extracted_text = " ".join([text[1] for text in result])

    return extracted_text

# function for the OCR process with language support

def ocr_from_image(image, lang):

    text = perform_ocr(image, lang)

    return text

# function to search for a keyword in the OCR text and highlight matches

def search_text(image, keyword, lang):

    # check if keyword is empty

    if not keyword:

        return "Please enter a keyword to search.", ""

    text = perform_ocr(image, lang)
    
    # make both text and keyword lowercase for case insensitive comparison

    lower_text = text.lower()
    lower_keyword = keyword.lower()
    
    # check if the keyword exists in the text

    if lower_keyword in lower_text:

        # highlight the matching keyword

        highlighted_text = text.replace(lower_keyword, f"<mark style='color: black; background-color: yellow;'>{lower_keyword}</mark>")

        return highlighted_text, f'Keyword "{keyword}" found!'
    
    return text, f'Keyword "{keyword}" not found.'

# layout and components

with gr.Blocks() as interface:

    gr.Markdown("## OCR and Keyword Search Application")

    with gr.Row():

        with gr.Column(scale=1):

            image_input = gr.Image(type="filepath", label="Upload Image")

            keyword_input = gr.Textbox(label="Enter Keyword (case-insensitive) ", placeholder="Type your keyword here...")

            # radio buttons for language selection

            lang_toggle = gr.Radio(["en", "hi"], label="Select Language", value="en")

            search_button = gr.Button("Search Keyword")

        with gr.Column(scale=2):

            # remove 'interactive' and 'placeholder'

            output_text = gr.HTML(label="Extracted Text")

            # highlighted text output

            keyword_output = gr.HTML(label="Highlighted Text")

    # button actions

    search_button.click(fn=search_text, inputs=[image_input, keyword_input, lang_toggle], outputs=[output_text, keyword_output])

    image_input.change(fn=ocr_from_image, inputs=[image_input, lang_toggle], outputs=output_text)

    # disable the search button if no image is uploaded

    def disable_search(image):

        if image is None:

            # disable the button

            return gr.update(interactive=False)

        # enable the button

        return gr.update(interactive=True)

    image_input.change(fn=disable_search, inputs=image_input, outputs=search_button)

# launch the interface

if __name__ == "__main__":

    interface.launch(share=True)