# 🧠 Chatbot with Memory

A simple Python command-line chatbot that remembers previous messages within a session.  
It uses the **NVIDIA API** (via the `OpenAI` SDK) and supports **streaming replies**, multiple **assistant modes**, and automatic **memory pruning** to keep the chat smooth and fast.

---

## 🚀 Features

- 🧩 **Memory** — Remembers the last few turns of the conversation  
- ⚡ **Streaming replies** — Text appears as the model generates it  
- 🧠 **Modes** — Switch between personalities like `ml_tutor`, `sysadmin`, etc.  
- 🧹 **Context pruning** — Keeps recent context, forgets older messages automatically  
- 💬 **Commands** — Simple `/mode`, `/clear`, `/help` commands for control  
