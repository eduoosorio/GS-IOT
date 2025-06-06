
# VisionSafe – Reconhecimento de Gestos em Apagões

## 🎯 Objetivo
O projeto **VisionSafe** tem como objetivo auxiliar pessoas, empresas ou serviços essenciais a reagirem durante quedas de energia elétrica. Através da detecção de gestos com a mão, mesmo em ambientes com baixa iluminação, o sistema emite alertas sonoros e visuais automaticamente.

---

## 🧠 Como Funciona

- Utiliza Python com **MediaPipe** e **OpenCV**.
- Detecta uma mão levantada em frente à câmera ou em vídeo simulado.
- Se o gesto for detectado (pulso acima da cabeça), o sistema:
  - 🔊 Toca um som de alerta (`alert.mp3` ou `alert.wav`)
  - ⚠️ Exibe uma mensagem de socorro na tela

---

## 🖥️ Tecnologias Utilizadas
- Python 3.11+
- MediaPipe
- OpenCV
- playsound

---

## 📂 Estrutura do Projeto

```
GS_IOT/
├── main.py              # Código principal com MediaPipe
├── alert.mp3/.wav       # Som de alerta
├── requirements.txt     # Bibliotecas necessárias
└── README.md            # Este arquivo
```

---

## ▶️ Como Executar

1. Instale os requisitos:
```bash
pip install -r requirements.txt
```

2. Rode o projeto com a webcam:
```bash
python main.py
```

3. Ou rode com um vídeo de demonstração:
- Edite o `main.py` e troque `cv2.VideoCapture(0)` por:
```python
cv2.VideoCapture('video_demo.mp4')
```

4. Levante a mão para simular um pedido de socorro.
5. Pressione `Q` para encerrar.

---

## 👥 Integrantes

- **RM550161** - Eduardo Osorio Filho  
- **RM550610** - Fabio Hideki Kamikihara

---

## 📌 Observações
Este projeto foi desenvolvido para o desafio de Physical Computing com foco em situações de **apagões**. A proposta pode ser estendida para ambientes como hospitais, centros de comando, residências de pessoas com deficiência visual ou idosos.
