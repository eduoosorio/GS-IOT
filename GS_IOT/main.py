import cv2
import mediapipe as mp
import time
from playsound import playsound
import threading

# Iniciar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Função para tocar o som em thread separada
def tocar_alerta():
    playsound('alert.wav')

# Abrir a webcam
cap = cap = cap = cv2.VideoCapture(0)

alerta_disparado = False
while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, _ = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Detectar se a mão está levantada (pulso acima da metade da tela)
            wrist = handLms.landmark[0]
            wrist_y = wrist.y * h

            if wrist_y < h // 2:
                if not alerta_disparado:
                    alerta_disparado = True
                    threading.Thread(target=tocar_alerta).start()

                cv2.putText(img, 'GESTO DETECTADO - SOCORRO ATIVADO!', (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 3)

    cv2.imshow("VisionSafe - Detector de Gesto", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
