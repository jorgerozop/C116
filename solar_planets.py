import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img
            "Sol",
            (20, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            ),
cv2.putText(img
            "Mercurio",
            (100, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 4, 215)
            ),
cv2.putText(img
            "Venus",
            (160, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            ),
cv2.putText(img
            "Tierra",
            (220, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            ),
cv2.putText(img
            "Marte",
            (280, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            ),
cv2.putText(img
            "Jupiter",
            (320, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            ),
cv2.putText(img
            "Saturno",
            (380, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            ),
cv2.putText(img
            "Urano",
            (420, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            ),
cv2.putText(img
            "Neptuno",
            (480, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
    
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)
