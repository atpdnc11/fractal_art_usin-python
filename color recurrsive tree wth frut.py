import turtle
import random

# झाड काढण्याचा function
def tree(branchLen, t):
    if branchLen > 5:
        # मोठ्या फांद्यांसाठी तपकिरी रंग, लहान फांद्यांसाठी हिरवा
        if branchLen > 40:
            t.pencolor("brown")  # जाड फांदीसाठी तपकिरी
        else:
            t.pencolor("green")  # पानांसाठी हिरवा

        t.forward(branchLen)  # फांदी पुढे काढ

        # उजवी फांदी
        t.right(20)
        tree(branchLen - random.randint(10, 20), t)  # फांदी लांबी कमी करा आणि random करा

        # डावी फांदी
        t.left(40)
        tree(branchLen - random.randint(10, 20), t)  # random लांबीची डावी फांदी

        t.right(20)
        t.backward(branchLen)  # मागे जा

        # जर लहान फांदी असेल तर पाने/फुलं/फळं टाका
        if branchLen < 40:
            draw_leaf_or_flower(t)

# पाने, फुलं, फळं काढण्याचा function
def draw_leaf_or_flower(t):
    chance = random.randint(1, 5)  # random chance ठरवा

    if chance == 1:
        t.pencolor("red")  # फुलं (लाल)
        t.dot(10)  # फुलासाठी ठिपका
    elif chance == 2:
        t.pencolor("yellow")  # फुलं (पिवळं)
        t.dot(10)
    elif chance == 3:
        t.pencolor("orange")  # फळ (संत्र रंग)
        t.dot(12)  # मोठा ठिपका (फळ)
    elif chance == 4:
        t.pencolor("pink")  # फुलं (गुलाबी)
        t.dot(8)
    else:
        t.pencolor("green")  # पाने
        t.dot(6)

# turtle स्क्रीन सेटअप
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("skyblue")  # आकाशी पार्श्वभूमी
t.left(90)  # turtle वर बघायला लावणं
t.speed(0)  # झपाट्याने काढायला लावणं

# झाड काढा
tree(100, t)

# पूर्ण झाल्यावर turtle लपवा
t.hideturtle()

# स्क्रीन बंद होऊ नये म्हणून
turtle.done()
