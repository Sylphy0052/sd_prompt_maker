import logging
import logging.handlers

import gradio as gr

from functions.prompt import generate_prompts
from settings import LOG_PATH

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s")
rh = logging.handlers.RotatingFileHandler(LOG_PATH, maxBytes=10000, backupCount=100)
rh.setLevel(logging.DEBUG)
rh.setFormatter(formatter)
logger.addHandler(rh)

with gr.Blocks(title="SD Prompt Maker") as app:
    # 設定

    # 入力

    generate_btn = gr.Button(value="Create", size="lg")
    # 出力
    output_area = gr.Textbox(label="prompts", show_copy_button=True)

    generate_btn.click(fn=generate_prompts, inputs=[], outputs=output_area)

if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=5001)
