from pywhatkit import image_to_ascii_art as ch        #imprting the function from pywhatkit as ch

# if it shows any error then enter the full path to the file in the string (eg: img1 = 'c:\\user\\Desktop\\doremo.jpg)

img1 = 'doremon.jpg'  
img2 = 'ironman.jpg'
img3 = 'pikachu.png'
img4 = 'rdjr.jpg'
img5 = 'shinchan.png' 


t1 = 't1.txt'
t2 = 't2.txt'
t3 = 't3.txt'
t4 = 't4.txt'
t5 = 't5.txt'

#converting images into text

ch(img1, t1)  
ch(img2, t2)
ch(img3, t3)
ch(img4, t4)
ch(img5, t5)

#printing completed for our conformation..

print('completed...')
