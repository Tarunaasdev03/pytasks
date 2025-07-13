def swapface():
    import cv2
    import numpy as np
    
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def detect_face(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
        if len(faces) == 0:
            return None, None
    
        x, y, w, h = faces[0] 
        face_region = img[y:y+h, x:x+w]
        return face_region, (x, y, w, h)
    
    
    cap = cv2.VideoCapture(0)
    captured_images = []
    
    print("➡ Press SPACE to capture 2 face images. Press ESC to cancel.")
    
    while len(captured_images) < 2:
        ret, frame = cap.read()
        if not ret:
            break
    
        display_frame = frame.copy()
        cv2.putText(display_frame, f"Press SPACE to capture Image {len(captured_images)+1}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Capture Faces", display_frame)
    
        key = cv2.waitKey(1)
        if key == 32: 
            captured_images.append(frame.copy())
            print(f"✔ Captured Image {len(captured_images)}")
        elif key == 27:  
            print("❌ Cancelled.")
            cap.release()
            cv2.destroyAllWindows()
            exit()
    
    cap.release()
    cv2.destroyAllWindows()
    
    
    if len(captured_images) == 2:
        img1, img2 = captured_images
    
        face1, coords1 = detect_face(img1)
        face2, coords2 = detect_face(img2)
    
        if face1 is None or face2 is None:
            print("❌ Could not detect face in one or both images.")
            exit()
    
       
        face2_resized = cv2.resize(face2, (coords1[2], coords1[3]))
        face1_resized = cv2.resize(face1, (coords2[2], coords2[3]))
    
       
        img1_result = img1.copy()
        img2_result = img2.copy()
    
       
        x1, y1, w1, h1 = coords1
        x2, y2, w2, h2 = coords2
    
        img1_result[y1:y1+h1, x1:x1+w1] = face2_resized
        img2_result[y2:y2+h2, x2:x2+w2] = face1_resized
    
        
        cv2.imshow("Image 1 with Face 2", img1_result)
        cv2.imshow("Image 2 with Face 1", img2_result)
        print("✅ Faces swapped. Press any key to close.")
    
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("⚠ Not enough images were captured.")



swapface()
