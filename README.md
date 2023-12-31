# Llama-Code Assistant
![code_llama_title-1200x750](https://github.com/Kirouane-Ayoub/Llama-Code-Assistant/assets/145156896/35c84254-d292-4945-b186-72dbbc7e8443)

## About This Project :
**Llama Code Assistant** a tool built using a highly advanced generative text model called **CodeLlama 34B Instruct** This model boasts an impressive scale of 34 billion parameters and is specifically fine-tuned for general code synthesis and comprehension tasks.
Notably, the **CodeLlama 34B Instruct - GGUF** model has been optimized for CPU usage, ensuring efficient performance even on devices without specialized hardware acceleration. It offers invaluable assistance to developers and programmers by generating code, aiding in code understanding, and facilitating coding tasks.

## Code Llama : 
Code Llama is a collection of pre-trained and fine-tuned generative text models ranging in scale from 7 billion to 34 billion parameters. This is the repository for the 34B instruct-tuned version in the Hugging Face Transformers format. This model is designed for general code synthesis and understanding. Links to other models can be found in the index at the bottom. **https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf**

## CodeLlama 34B Instruct - GGUF : 

**CodeLlama 34B Instruct** is available in the **GGUF** format, which is a new format introduced by the **llama.cpp** team in **August 2023**. **GGUF** is a replacement for **GGML**, which is no longer supported by **llama.cpp**. The key benefit of **GGUF** is that it is an extensible, future-proof format that stores more information about the model as metadata. It also includes significantly improved tokenization code, including for the first time full support for special tokens.**https://huggingface.co/TheBloke/CodeLlama-34B-Instruct-GGUF**

## How to Run this tool : 

```
pip install -r requirements.txt
wget https://huggingface.co/TheBloke/CodeLlama-34B-Instruct-GGUF/resolve/main/codellama-34b-instruct.Q4_K_M.gguf
streamlit run app.py

```
