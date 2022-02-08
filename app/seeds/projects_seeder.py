from app.models import db, Project


# demo projects
def seed_project():
    bird_house= Project(
        userId=1, 
        title="How to build a bird house.", 
        titleImage="idk", 
        overview="This is how to construct a bird house!",
        category="Crafts"
    )

    casino_clock= Project(
        userId=2, 
        title="Casino'clock - Playing card flap display / clock", 
        titleImage="https://content.instructables.com/ORIG/F8U/KR3T/KZCPHOFJ/F8UKR3TKZCPHOFJ.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=16727930c4e9a859906b057dd58a338d", 
        overview="""
            One of the main difficulty to make a split flap display with 3D printer is the fabrication of flaps. 
            Therefore I used off-the-shelf playing cards for flaps, and made a funny and crazy clock with minimum number of parts. 
            Simple design : each display unit consists of only 3 types of parts. Sensor is not used to find the origin. 
            Funny motion : by arranging cards randomly, you can enjoy busy motion of flaps 
            WiFi time acquisition : current time is acquired via WiFi using ntp
            """,
        category="Circuits"
    )

    one_board_mug= Project(
        userId=3, 
        title="One Board Mug", 
        titleImage="https://content.instructables.com/ORIG/FST/TDM1/KZBA18KY/FSTTDM1KZBA18KY.jpg?auto=webp&frame=1&width=612&height=1024&fit=bounds&md=eb345ed6f0c79b14398aa15b45a9edb5", 
        overview="Create a fun and unique drinking vessel from one board of pine.",
        category="Workshop"
    )

    one_board_mug= Project(
        userId=1, 
        title="Onion Skillet Bacon Cheeseburgers", 
        titleImage="https://content.instructables.com/ORIG/FSA/PGFW/KYK4NWBL/FSAPGFWKYK4NWBL.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=e5c78e47e1d1406d50a53dc73e21b425", 
        overview="""
                    Looking for a delicious stacked-up burger? Then you came to the right place! A bacon cheeseburger with onions cooked in bacon grease!
                    
                    Makes 6 Burgers Prep Time 10 minutes Cook time 30 minutes

                    Ingredients

                    3 Yellow Onions, cut into slices
                    6 Brioche Buns
                    6 Slices Sharp Cheddar
                    8 Slices Thick-Cut Bacon, cut in half
                    1 cup Bread and Butter Pickles
                    For the Patty:

                    1 lb Ground Beef
                    1 lb Ground Pork
                    1 bag Garlic Pepper Crispy Onions, crushed
                    1 tsp Salt
                    1 tsp Red Pepper Flakes
                    1 tsp Parsley
                    For the Sauce:

                    1/2 cup Mayo
                    1/2 cup BBQ Sauce
                    1/4 cup Pickle Juice
                """,
        category="Cooking"
    )

    james_webb_clock= Project(
        userId=2, 
        title="James Webb Space TeleClock", 
        titleImage="https://content.instructables.com/ORIG/FY7/2PZZ/KYVK6ZDO/FY72PZZKYVK6ZDO.jpg?auto=webp&frame=1&width=597&height=1024&fit=bounds&md=77bcb2dcb44a2791d61936b6c3c87b86", 
        overview="""
                    Inspired by the launch of the James Webb Telescope on 24/12/2021, I was driven to make something to commemorate this incredible achievement, hence the James Webb Space Teleclock. The aim was to make a decorative item for the home that resembled the mirror portion of the telescope which in my opinion is not only an engineering marvel but a gorgeous one at that. Making it into a clock was just to make it functional as well :)

                    If you are interested in the 25 years of engineering that went into building the James Webb Telescope I would recommend watching this episode of Real Engineering
                """,
        category="Living"
    )

    db.session.add(bird_house)
    db.session.add(casino_clock)
    db.session.add(one_board_mug)
    db.session.add(james_webb_clock)
    db.session.commit()

def undo_project():
    db.session.execute('TRUNCATE projects RESTART IDENTITY CASCADE;')
    db.session.commit()

