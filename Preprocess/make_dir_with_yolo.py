import os 
import glob

f = open("/media/masih/personal/Projects/medicine_/packge_1/labels/train_series1.txt" , "a")


print("Waiting......")
for image in glob.glob(os.getcwd() +"/*.jpg"):
    
    f.writelines(image+"\n")
    image = os.path.basename(image)
    image = int(image.replace(".jpg" , ""))
    
    #print(type(image))

    for label in glob.glob(os.getcwd() +"/*.txt"):
        
        org_label_address = label
        #print(org_label_address)
        label = os.path.basename(label)
        #print(label)
        #print("label ------>>>>>" + str(label))
        label = label.replace(".txt" , "")
        label = int(label)
        
        if(label==image):
            
            #print("fuuuuuck")
            yolo_label = open(org_label_address , "r")
            label = yolo_label.readline()
            #print("MF")
            #yolo_label = yolo_label.readline()
            f.writelines(label+"\n\n")

f.close()

print("Done Hopefully")
