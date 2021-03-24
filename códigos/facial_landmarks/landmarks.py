import cv2
import dlib
import numpy as np

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    X = []
    features = []

    
    faces = detector(gray)
    for face in faces:
        
        landmarks = predictor(gray, face)
        
        print('Novos pontos para nova imagem:\n')

        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            X.append((x, y))
            #print('Coordenada x: {}, Coordanada y: {}'.format(X[n][0], X[n][1]))
            cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)
        
        '''cv2.line(frame, X[0], X[16], (0, 0, 255), 1)
        cv2.line(frame, X[0], X[36], (0, 0, 255), 1)
        cv2.line(frame, X[45], X[16], (0, 0, 255), 1)
        cv2.line(frame, X[57], X[8], (0, 0, 255), 1)
        cv2.line(frame, X[31], X[2], (0, 0, 255), 1)
        cv2.line(frame, X[35], X[14], (0, 0, 255), 1)
        cv2.line(frame, X[59], X[7], (0, 0, 255), 1)
        cv2.line(frame, X[55], X[9], (0, 0, 255), 1)
        cv2.line(frame, X[51], X[57], (0, 0, 255), 1)
        cv2.line(frame, X[37], X[40], (0, 0, 255), 1)
        cv2.line(frame, X[38], X[41], (0, 0, 255), 1)
        cv2.line(frame, X[43], X[46], (0, 0, 255), 1)
        cv2.line(frame, X[47], X[44], (0, 0, 255), 1)
        cv2.line(frame, X[37], X[19], (0, 0, 255), 1)
        cv2.line(frame, X[44], X[24], (0, 0, 255), 1)
        cv2.line(frame, X[29], X[1], (0, 0, 255), 1)
        cv2.line(frame, X[29], X[15], (0, 0, 255), 1)'''

    #print('\n')

    cv2.imshow("Frame", frame)
    
    X = np.array(X)

    features.append(0.5*(np.linalg.norm(X[42] - X[45])) + (np.linalg.norm(X[36] - X[39])))
    features.append(0.5*(0.5*(np.linalg.norm(X[37] - X[41]) + np.linalg.norm(X[38] - X[40])) + (0.5*(np.linalg.norm(X[43] - X[47]) + np.linalg.norm(X[44] - X[46])))))
    features.append(np.linalg.norm(X[0] - X[16])) 
    features.append(np.linalg.norm(X[2] - X[14])) 
    features.append(np.linalg.norm(X[4] - X[12])) 
    features.append(np.linalg.norm(X[6] - X[10])) 
    features.append(np.linalg.norm(X[6] - X[48]))
    features.append(np.linalg.norm(X[10] - X[54]))
    features.append(np.linalg.norm(X[48] - X[54]))
    features.append(np.linalg.norm(X[62] - X[51]))
    features.append(np.linalg.norm(X[66] - X[57]))
    features.append(np.linalg.norm(X[57] - X[8]))   
    features.append(np.linalg.norm(X[33] - X[51]))   
    features.append(np.linalg.norm(X[31] - X[35]))  
    features.append(0.5*(np.linalg.norm(X[0] - X[2])) + (np.linalg.norm(X[16] - X[14])))
    features.append(0.5*(np.linalg.norm(X[2] - X[4])) + (np.linalg.norm(X[14] - X[12])))
    features.append(0.5*(np.linalg.norm(X[4] - X[6])) + (np.linalg.norm(X[12] - X[10])))
    features.append(0.5*(np.linalg.norm(X[39] - X[31])) + (np.linalg.norm(X[42] - X[45])))
    features.append(np.linalg.norm(X[21] - X[22]))
    features.append(0.5*(np.linalg.norm(X[17] - X[36])) + (np.linalg.norm(X[2] - X[9])))
    features.append(0.5*(np.linalg.norm(X[17] - X[21])) + (np.linalg.norm(X[22] - X[26])))
    features.append(0.5*(np.linalg.norm(X[39] - X[21])) + (np.linalg.norm(X[22] - X[42])))
    features.append(0.5*(np.linalg.norm(X[37] - X[19])) + (np.linalg.norm(X[44] - X[24])))
    features.append(X[19][1] - 0.5*(X[17][1] + X[21][1]))
    features.append(0.5*(np.linalg.norm(X[19] - X[21])) + (np.linalg.norm(X[24] - X[22])))
    features.append(0.5*(np.linalg.norm(X[19] - X[17])) + (np.linalg.norm(X[24] - X[26])))
    features.append(np.linalg.norm(X[39] - X[33]))
    features.append(np.linalg.norm(X[42] - X[33]))
    features.append(0.5*(np.linalg.norm(X[42] - X[54])) + (np.linalg.norm(X[39] - X[48])))
    features.append(0.5*(np.linalg.norm(X[0] - X[36])) + (np.linalg.norm(X[45] - X[16])))

    features = np.array(features)
    features = features/features[2]
    print(features)
    print('\n')

    if cv2.waitKey(0) == 27:
        break