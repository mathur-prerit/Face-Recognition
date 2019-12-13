import user_dataset as ud
import train_dataset as td
import test_dataset as tstd

a=int(input("Enter your input:\n1. For capturing your dataset\n2.For training your dataset with custom images\n3.Predicting the face of the person\nEnter your choice:\t"))
if a==1:
    ud.cam_capture()
elif a==2:
    td.training()
elif a==3:
    tstd.ftesting()
else:
    print('You provided wrong input')
    print('try again')