import cv2

#initializing camera
cam=cv2.VideoCapture(0)
def capture():

    #naming the application
    cv2.namedWindow("Python webcam picture app")

    #getting image frames of the webcam
    count=0
    while True:
        ret,frame=cam.read()# read frame
        if not ret:
            print("failed to capture image")
            break
        cv2.imshow("webcam", frame) #display image 

        k=cv2.waitKey(1)
        if k%256 == 27: #for escape key to quit
            print("closed....")
            break
        if k%256 == 32: # for space bar to capture the image
            img_name="opencv_frame_{}.png".format(count)
            cv2.imwrite(img_name,frame)
            print("image taken")
            count+=1     

    #releasing the camera
    cam.release
    #removing other windows
    cam.destroyAllWindows()
capture()    