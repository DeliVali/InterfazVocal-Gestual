import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#Configuración del detector de manos
with mp_hands.Hands(
    #Compureba si es una imagen estaica o no
    static_image_mode=True,
    #Numero de manos a detectar
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    #Cuando se usa el _ en este caso es para ignorar el ultimo valor que se le asigna image.shape 
    image=cv2.VideoCapture(0)
    height,width,_=image.shape
    #Se invierte la imagen para detectar ambas manos y se vuelve a invertir 
    image= cv2.flip(image,1)
    #Se cambia el color de las imagenes ya que las detecciones de imagen se hacen con color rgb
    image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    
    results=hands.process(image_rgb)
    #Handeness impreme si se identificaron ambas manos
    #print("Handedness: ",results.multi_handedness)
    
    #Multi Hand Landmarks imprime todos los puntos claves de las manos
    #print("Hand LandMarks: ",results.multi_hand_landmarks)
    
    #Condición en caso de que no encuentre la mano
    if results.multi_hand_landmarks is not None:
        #-----------------------------------------------------------------------------
        #Dibujando los puntos y conexiones  con mediapipe
         for hands_landmarks in results.multi_hand_landmarks:
            #Dibujp de los landmarks con media pipe
            mp_drawing.draw_landmarks(image,hands_landmarks,mp_hands.HAND_CONNECTIONS
            #Cambio de colores en el dibujo de los landmarks 
            #puntos
            ,mp_drawing.DrawingSpec(color=(255,255,0),thickness=4,circle_radius=5),
            #conexiones
            mp_drawing.DrawingSpec(color=(255,0,255),thickness=2))
        #-------------------------------------------------------------------------------
            #Accediendo a los landmarks de acuerdo a su nombre
            x1=hands_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x 
            print(x1) #imprime las coordenadas de la punta del pulgar
    
    
    image= cv2.flip(image,1)
#Visualización de imagen
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
    