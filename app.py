import gradio as gr

def greet(name):
    return "Hello world " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()