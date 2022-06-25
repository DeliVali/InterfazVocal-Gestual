import cv2
import mediapipe as mp
from threading import Thread
from GestureResponses import GResponses
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Configuración del detector de manos
def mainConfiguration():
    
    with mp_hands.Hands(
        #Compureba si es una imagen estaica o no
        static_image_mode=False,
        #Numero de manos a detectar
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:
    #Configura la camara para la detección de manos
        while True:
            ret,frame=cap.read()
            if ret ==False:
                break
            height,width,_=frame.shape
            
            frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            
            results=hands.process(frame_rgb)
            #Condición en caso de que no encuentre la mano
            if results.multi_hand_landmarks is not None:
            #-----------------------------------------------------------------------------
                for hand_index, hand_info in enumerate(results.multi_handedness):
                    hand_label = hand_info.classification[0].label
                    print(hand_label)
                hands_landmarks=dibujoManos(results,frame)
                #Obtiene el numero y el tipo de dedos alzados
                Status_dedos,count=obtenerCordenadas(hands_landmarks,hand_label)
                #Manda el numero y tipo de dedos levantados y Ejecuta las respuestas
                t2=Thread(GResponses.main(Status_dedos,count))
                t2.start()
                     
                    
                cv2.imshow("Frame",frame)
                if cv2.waitKey(1) & 0xff ==27:
                    break
    cap.release()
    cv2.destroyAllWindows()




def obtenerCordenadas(hands_landmarks,hand_label):
    #Accediendo a los landmarks de acuerdo a su nombre
    

    
    #obtiene los ids de la punta de cada dedo menos el pulgar
    tipsIDS=[mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                        mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    
    #obtiene los ids de la segunda raya de cada dedo menos el pulgar
    pipsIDS=[mp_hands.HandLandmark.INDEX_FINGER_PIP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
                        mp_hands.HandLandmark.RING_FINGER_PIP, mp_hands.HandLandmark.PINKY_PIP]
    #Obtiene las coordenadas del pulgar y la plama
    thumb_tip_x = hands_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    thumb_mcp_x = hands_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
    
        # Se guarda los status de los dedos menos del pulgar
    Status_dedos = { 'INDEX': False, 'MIDDLE': False, 'RING': False,
                        'PINKY': False,'THUMB':False}
    count=0
    
    #hacemos un ciclo que vaya pasando por cada id de las puntas de los dedos
    for fingerTips in tipsIDS:
        #Se guarda el nombre del dedo para cambiar los status
        finger_name = fingerTips.name.split("_")[0]
        #hacemos un ciclo que vaya pasando por cada id de la segunda raya de los dedos
        for fingerPips in pipsIDS:
            #hacemos una comparación para ver si los dedos estan levantados (Si la distancia 
            # en el eje Y de la punta del dedo es menor a la de la segunda raya significa que ese no esta levantado)
            if hands_landmarks.landmark[fingerTips].y < hands_landmarks.landmark[fingerPips].y:
                Status_dedos[finger_name]=True
                # Increment the count of the fingers up of the hand by 1.
                count +=1
                

           
         #Ve si la mano es derecha o izquierda para los pulgares
        if (hand_label.upper()=='RIGHT' and (thumb_tip_x < thumb_mcp_x)) or (hand_label.upper()=='LEFT' and (thumb_tip_x > thumb_mcp_x))  :
            Status_dedos['THUMB']=True
            count +=1
                
    
    return Status_dedos,count/4
              
                
    
    
 
    
    #Hace un ciclo de toda la lista de las puntas para obtener las coordenadas
    
    
        
       
    
    #print(puntaPulgarint) #imprime las coordenadas de la punta del pulgar
    #print(puntaIndiceint) #imprime las coordenadas de la punta del dedo indice
    
    
    
    

def dibujoManos(results,frame):
    #Dibujando los puntos y conexiones  con mediapipe
    for hands_landmarks in results.multi_hand_landmarks:
        #Dibujp de los landmarks con media pipe
        mp_drawing.draw_landmarks(frame,hands_landmarks,mp_hands.HAND_CONNECTIONS)
    return hands_landmarks



