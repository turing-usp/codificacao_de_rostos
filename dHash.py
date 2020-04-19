import cv2


def dHash(image, hashSize=8):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread(image)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1)
    img = img[faces[0][1]:faces[0][1]+faces[0][3], faces[0][0]:faces[0][0]+faces[0][2]]
    cv2.imshow('img', img)
    cv2.waitKey()
	# resize the input image, adding a single column (width) so we
	# can compute the horizontal gradient
    resized = cv2.resize(img, (hashSize + 1, hashSize))
	# compute the (relative) horizontal gradient between adjacent
	# column pixels
    diff = resized[:, 1:] > resized[:, :-1]
	# convert the difference image to a hash
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def Hamming(n1, n2) :  
    x = n1 ^ n2  
    setBits = 0
    while (x > 0) : 
        setBits += x & 1
        x >>= 1     
    return setBits

'''
TESTES

print("Duas fotos do Rodrigo")
print(Hamming(dHash("test.jpg"),dHash("test2.jpg")))

print("Duas fotos do Edu")
print(Hamming(dHash("test3.jpg"),dHash("test4.jpg")))

print("Edu X Rodrigo")
print(Hamming(dHash("test3.jpg"),dHash("test.jpg")))
print(Hamming(dHash("test4.jpg"),dHash("test2.jpg")))
print(Hamming(dHash("test3.jpg"),dHash("test2.jpg")))
print(Hamming(dHash("test4.jpg"),dHash("test.jpg")))
print(Hamming(dHash("test.jpg"),dHash("test.jpg")))
'''