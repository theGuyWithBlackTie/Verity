import gradio as gr

from src.backend.backend import Backend

class GradioApp:
    def __init__(self, title: str, description: str):

        self.demo = gr.Blocks(title=title, theme=gr.themes.Ocean())
        self.create_interface()

        self.backend = Backend()

    def create_interface(self):
        with self.demo:
            gr.Markdown(f"## Verity: Uncover the truth in your documents")

            # Create two columns, one for uploading files and another to ask and chat about the uploaded files
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### Upload Files")
                    self.file_upload = gr.File(label="Upload your documents here", file_count="multiple", file_types=[".pdf", ".txt", ".docx"], type="filepath")
                    self.upload_button = gr.Button("Start Processing", variant="primary")
                    self.summary_box = gr.Textbox(label="Summary of Uploaded Files", placeholder="Computing Summary...", visible=False)


                with gr.Column(scale=1.5):
                    gr.Markdown("### Ask and Chat")
                    self.query_input = gr.Textbox(label="Ask a question about the uploaded files", placeholder="Type your question here...")
                    self.chat_output = gr.Chatbot(label="Chat Output")

                self.upload_button.click(
                    fn=self.process_files,
                    inputs=self.file_upload,
                    outputs=[self.summary_box, self.summary_box]
                    )
    
    def process_files(self, file_paths):
        # Placeholder for file processing logic
        if not file_paths:
            return "No files uploaded."
        
        summaries = self.backend.generate_introductory_summary(file_paths)
        response = ""
        for file_name, summary in summaries.items():
            response += f"**{file_name}**:\n {summary}\n\n\n"
        return response, gr.update(visible=True)