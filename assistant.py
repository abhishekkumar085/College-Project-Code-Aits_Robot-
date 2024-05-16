import speech_recognition as sr
import pyttsx3
import datetime
from time import sleep
from multiprocessing import Process

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# print(voices[0].id)

rate = engine.getProperty('rate') #voice speed
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak('welcome to Aaravali College. Please tell me How may i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio)
        print( query)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        # print(query)
        # speak(query)
    except Exception as e:
        # print(e)
        print("Say that again please...")
    return query
    sleep(2)
if __name__ == "__main__":
    wishMe()
    while True:

        
            try:
                query = takeCommand().lower()
                if 'hello robo' in query:
                    speak("hello i am there")

                elif 'hello' in query:
                    speak("hello")

                elif 'hod of computer' in query:
                    speak("doctor jeetendra singh")

                elif 'hod of civil' in query:
                    speak("sachin sharma")


                elif 'hod of mechanical' in query:
                    speak("veejendra shankla")


                elif 'who made you' in query:
                    speak("deepak, abhishek, rumaan")
                elif 'kisne banaya' in query:
                    speak("bihar schoolars")
                elif 'thank you' in query:
                    speak("Welcome sir")    


                elif 'hod of electrical' in query:
                    speak("doctor bheru das")

                elif 'director of aravali' in query:
                    speak("doctor hemant dhabhai") 
                
                # elif "time" in query:
                #     time=datetime.now() 
                #     print(time)


                elif 'how are you' in query:
                    speak("i am fine, please tel me how may i help you")
            
                elif 'what is your name' in query:
                    speak("my name is a i t s robot") 
                elif "what's your name" in query:
                    speak("my name is a i t s robot") 
                elif "what's your nick name" in query:
                    speak("my name is Respo robot") 
                elif "what is your nick name" in query:
                    speak("my name is Respo robot") 
                elif 'who are you' in query:
                    speak("I am a i t s robot") 
                elif "who is the owner of" in query:
                    speak("mister ohm prakash agarwal")
                elif "who is the owner of aits" in query:
                    speak("mister ohm prakash agarwal")
                
                elif "financial secretary" in query:
                    speak("mister amit agarwal")
                elif "finance secretary" in query:
                    speak("mister amit agarwal")
                elif "who is the financial secretary of aits" in query:
                    speak("mister amit agarwal")
                elif "who is the financial secretary of aravali" in query:
                    speak("mister amit agarwal")
                elif "secretary" in query:
                    speak("mister n. l. khetan.")
                elif "who is the secretary of aravali" in query:
                    speak("mister n. l. khetan.")
                elif "who is the secretary of a i t s" in query:
                    speak("mister n. l. khetan.")
                elif "who is the director of aravali institute" in query:
                    speak("doctor hemant dha bhai.")
                elif "who is the director of aravali institute technical studies" in query:
                    speak("doctor hemant dha bhai.")
                elif "who is the director of aits" in query:
                    speak("doctor hemant dha bhai.")
                elif "director of vision" in query:
                    speak("doctor sadhana mandoli.")
                elif "principle of vedanshi" in query:    
                    speak("mister utsav jain")
                elif "who is the principle of vedanshi college" in query:
                    speak("mister utsav jain")
                elif "registrar" in query:
                    speak("mister abhas mathur.")
                elif "who is the registrar of aravali institute of technical studies" in query:
                    speak("mister abhas mathur.")
                elif "who is the registrar of aits" in query:
                    speak("mister abhas mathur.")
                elif "examination controller" in query:
                    speak("mister gaurav purohit.")
                elif "who is the examination controller of aravali institute of technical studies" in query:
                    speak("mister gaurav purohit.")
                elif "who is the examination controller of aits" in query:
                    speak("mister gaurav purohit.")
                elif "dean of" in query:
                    speak("mrs. sangita sharma.")
                elif "who is the dean of aravali institute technical studies" in query:
                    speak("mrs. sangita sharma.")
                elif "who is the dean of aravali institute" in query:
                    speak("mrs. sangita sharma.")
                elif "hod of electronics" in query:
                    speak("mister abhas mathur.")
                elif "who is the hod of electronics and comunication department" in query:
                    speak("mister abhas mathur.")
                elif "who is the hod of electronics and comunication branch" in query:
                    speak("mister abhas mathur.")
                elif "who is the hod of ece" in query:
                    speak("mister abhas mathur.")
                elif "who is the hod of electrical department" in query:
                    speak("doctor bherudas vairagi")
                elif "who is the hod of electrical" in query:
                    speak("doctor bherudas vairagi")
                elif "who is the hod of electrical branch" in query:
                    speak("doctor bherudas vairagi")
                elif "who is the hod of double e" in query:
                    speak("doctor bherudas vairagi")
                elif "who is the hod of civil department" in query:
                    speak("mister sachin sharma")
                elif "who is the hod of civil branch" in query:
                    speak("mister sachin sharma")
                elif "who is the hod of civil" in query:
                    speak("mister sachin sharma")
                elif "who is the hod of ce" in query:
                    speak("mister sachin sharma")
                elif "who is the hod of mechanical department" in query:
                    speak("doctor vijyendra shankhala")
                elif "who is the hod of mechanical" in query:
                    speak("doctor vijyendra shankhala")
                elif "who is the hod of mechanical branch" in query:
                    speak("doctor vijyendra shankhala")
                elif "who is the hod of me" in query:
                    speak("doctor vijyendra shankhala")
                elif "who is the hod of basic science department" in query:
                    speak("mister abhash mathur")
                elif "hod of basic science" in query:
                    speak("mister abhash mathur")
                elif "head of library" in query:
                    speak("mister vipin pandya")
                elif "who is the head of library" in query:
                    speak("mister vipin pandya")
                elif "hod of mca" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "who is the hod of mca department" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "who is the hod of computer science" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "who is the hod of computer science department" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "who is the hod of computer science branch" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "hod of cs" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "who is the hod of artificial inteligence" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "hod of artificial" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "who is the hod of artificial inteligence branch" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "hod of ai" in query:
                    speak("doctor jitendra singh chouhan.")
                elif "head of cultural events" in query:
                    speak("the cultural events' head is mr. gauravpurohit.")
                elif "who is the head of training and placement cel" in query:
                    speak("mister ajay vashisth is head of training and placement.")
                elif "where is aravali" in query:
                    speak("it is located at a distance of 11 km from udaipur city and oposite to umarda railway station, udaipur")
                elif "aits situated" in query:
                    speak("it is located at a distance of 11 km from udaipur city and oposite to umarda railway station, udaipur")
                elif "strength of students" in query:
                    speak("5000 students in aravali institute")
                elif "what is the strength of students in aits" in query:
                    speak("5000 students in aravali institute technical studies")
                elif "what is the strength of students in aits" in query:
                    speak("5000 students in a i t s")
                elif "courses are available" in query:
                    speak("there are seven courses available in aravali institute")
                elif "how many courses are available in aravali institute technical studies" in query:
                    speak("there are seven courses available in aravali institute technical studies")
                elif "how many courses are available in aits" in query:
                    speak("there are seven courses available")
                elif "how many times aravali had awarded at state and national level" in query:
                    speak("fiften times ")
                elif "awarded at state level" in query:
                    speak("fiften times ")
                elif "awarded at national level" in query:
                    speak("fiften times ")
                elif "university aproved the aravali" in query:
                    speak("aproved by  a i c t e .")
                elif "courses are provided in vision school" in query:
                    speak("four courses are provided in vision school of management.")
                elif "why vision school of management is best" in query:
                    speak("many facilities provided in comparison to other college.")
                elif "where is vision school of management" in query:
                    speak("vision school of management situated in chitorgarh.")
                elif "college timing" in query:
                    speak("9:00 am to 4:00 pm ")
                elif "what is college timing" in query:
                    speak("9:00 am to 4:00 pm")
                elif "courses are available" in query:
                    speak("mba, bca, ba and b.sc, mtech btech diploma.")
                elif "how many colleges are in aravali group" in query:
                    speak("there are seven colleges in aravali group.")
                elif "colleges are in aravali group" in query:
                    speak("there are seven colleges in aravali group.")
                elif "name of the colleges in aravali group" in query:
                    speak("1. aravali institute of technical studies.           2. aravali teacher training college.                3. aravali college of teachers training.         4. vision school of management. 5.aravali comerce & science college.  6.vedanshicollege of nursing.7. nerjamodi school.")
                elif "name of aravali group" in query:
                    speak("1. aravali institute of technical studies.           2. aravali teacher training college.                3. aravali college of teachers training.         4. vision school of management. 5.aravali comerce & science college.  6.vedanshicollege of nursing.7. nerjamodi school.")
                elif "why student join aravali institute of technical studies" in query:
                    speak("because aravali institute is the best college in udaipur.")
                elif "faculties in aravali" in query:
                    speak("more than 120 faculties in aravali institute of technical studies.")
                elif "faculty in aravali" in query:
                    speak("more than 120 faculties in aravali institute of technical studies.")
                elif "how many faculties in aits" in query:
                    speak("more than 120 faculties")
                elif "seats are in computer science" in query:
                    speak("60 seats in computer science.")
                elif "seats in" in query:
                    speak("60 seats")
                elif "how many seats are in computer science branch" in query:
                    speak("60 seats")
                elif "how many seats are in computer science enginering" in query:
                    speak("60 seats")
                elif "how many seats are in cs" in query:
                    speak("60 seats")
                elif "how many seats are in artificial inteligence" in query:
                    speak("60 seats")
                elif "how many seats are in artificial inteligence branch" in query:
                    speak("60 seats")
                elif "how many seats are in artificial inteligence enginering" in query:
                    speak("60 seats")
                elif "how many seats are in ai" in query:
                    speak("60 seats")
                elif "how many seats are in civil branch" in query:
                    speak("60 seats")
                elif "how many seats are in civil enginering" in query:
                    speak("60 seats")
                elif "how many seats are in electronics and comunication enginering" in query:
                    speak("30 seats in electronics and comunication enginering.")
                elif "how many seats are in ece" in query:
                    speak("30 seats")
                elif "how many seats are in mechanical enginering" in query:
                    speak("60 seats in mechanical enginering.")
                elif "how many seats are in electrical enginering" in query:
                    speak("60 seats in electrical enginering.")
                elif "seats are in thermal" in query:
                    speak("18 seats in thermal enginering.")
                elif "seats are in production" in query:
                    speak("24 seats in production enginering.")
                elif "how many seats are in digital comunication" in query:
                    speak("24 seats in digital comunication.")
                elif "how many seats are in software enginering" in query:
                    speak("24 seats in software enginering.")
                elif "how is the campus placement" in query:
                    speak("best in the placement record")
                elif "how is the campus placement in aits" in query:
                    speak("best in the placement record")
                elif "transportation facilities available" in query:
                    speak("yes there is transportation facilities available for al the students")
                elif "how many buses are available" in query:
                    speak("there are six buses available in college.")
                elif "wi fi available in campus" in query:
                    speak("yes there is  wi fi available in campus")
                elif "library available" in query:
                    speak("of course there is a digital library for students.")
                elif "all books are available in library" in query:
                    speak("yes there is al types of boks are available in library.")
                elif "cafeteria available" in query:
                    speak("yes there is  cafeteria available in college campus")
                elif "college have hostel facility" in query:
                    speak("yes college provides hostel facility for boys & girls separately.")
                elif "play ground is available" in query:
                    speak("yes in college campus play ground is available.")
                elif "gym facility available" in query:
                    speak("yes gym facility is available for students.")
                elif "labs available" in query:
                    speak("yes there are labs for al the branches separately in college")
                elif "is there atm facility available" in query:
                    speak("atm is available in college premises.")
                elif "which type of facilities provided in class rooms" in query:
                    speak("clas rooms are specious well ventilated with natural light and adequate electrical facility.")
                elif "what kind of facilities were provided in class rooms" in query:
                    speak("class rooms are specious wel ventilated with natural light and adequate electrical facility.")
                elif "is there teaching facility good" in query:
                    speak("this college has an excelent teaching faculty with highly qualified and wel experienced staf")
                elif "teacher supportive" in query:
                    speak("yes ,teachers are suportive")
                elif "incharge of account section" in query:
                    speak("mister cheten chepa")
                elif "parents teachers meeting conduct" in query:
                    speak("yes! p.t meting is held periodicaly.")
                elif "spiritual environment" in query:
                    speak("yes, a temple of lord ganesha and godesaraswati is situated in campus to kep up religious culture. ganesh festival and saraswatipoja are popular function.")
                elif "open theater facility" in query:
                    speak("yes there is a theater having seting arangement of 1500 people & wel equiped stageof 2400 sq.ft.")
                elif "workshop facility" in query:
                    speak("yes there is workshop available with modern machines like carpentry, smithy, moulding, forging fiting and machine shop.")
                elif "which type of special facility provided on women's day" in query:
                    speak("college is organizing games and sports for girls and also provides snacks for refreshment.")
                elif "which type of special facility available in arooma function" in query:
                    speak("special diner on arooma night for al the students.")
                elif "what are the special facilities available in cafeteria" in query:
                    speak("students get personal things in cafeteria like  soap, oil, pen, register etc.")
                elif "auditorium available" in query:
                    speak("yes there is an auditorium available in college campus for seminars.")
                elif "power backup facility available or not" in query:
                    speak("yes there is a power backup facility available in college campus.") 
                elif "is there personal vehicles are allowed in hostel campus" in query:
                    speak("no")
                elif "is there an erp facility available or not" in query:
                    speak("yes there is an erp facility available.")
                elif "what are the special facilities available for entertainment" in query:
                    speak("arooma function conduct for students not only for entertainment. it is also for good mission or vision.")
                elif "are medical facilities available in the college" in query:
                    speak("yes medical facilities are available in college.")
                elif "what are the facility available for guest" in query:
                    speak("there is a one room for out siders and visitors.")
                elif "what is the facility available for girls in college" in query:
                    speak("there is a common room available for girls.")
                elif "what kind of library facility available for student" in query:
                    speak("there is a library card through which student can issue books for 15days fre of cost.")
                elif "is there any other facility" in query:
                    speak("yes student can buy notepads and files from account section.")
                elif "which type of facilities available in summer" in query:
                    speak("students get 24hrs. cold water during sumer at free of cost.")
                elif "which type of scholarship available for the students" in query:
                    speak("students get scholarships from rajasthan, j&k, bihar jharkhand & other state governments.")
                elif "is there any scholarship available from college for bright students" in query:
                    speak("yes,50% of in the tution fe is waived who got above 90% in board exams.")
                elif "how many clubs are there" in query:
                    speak("there are five clubs viz. art of living club ,cultural club ,literary club, adventure club & technical club.")
                elif "vision and mission of technical club" in query:
                    speak("its vision and mission is to work technicaly.")
                elif "vision and mission of cultural club" in query:
                    speak("its vision and mission is to do al cultural activities.")
                elif "vision and mission of art of living club" in query:
                    speak("its vision and mission is to treat equaly, develop personality. ")
                elif "vision and mission of adventure club" in query:
                    speak("its aim is to conduct al the sports and adventures activities.")
                elif "vision and mission of literary club" in query:
                    speak("its aim is to conduct stage performances in literacy language.")
                elif "head of adventure club" in query:
                    speak("mr pramod kumar")
                elif "head of cultural club" in query:
                    speak("mrs bhumika shrimali")
                elif "head of art of living club" in query:
                    speak("mr.narayan singh")
                elif "head of literary club" in query:
                    speak("doctor anju sharma")
                elif "president of technical club 2018" in query:
                    speak("murtaza lukawala")
                elif "president of cultural club 2018" in query:
                    speak("bikash duta")
                elif "president of art of living club 2018" in query:
                    speak("madhusudhan soni")
                elif "president of adventure club 2018" in query:
                    speak("devashis ranjan")
                elif "president of literary club 2018" in query:
                    speak("shalini radhakrishna")
                elif "vice president of technical club 2018" in query:
                    speak("harsh")
                elif "vice president of cultural club 2018" in query:
                    speak("avinash sharma")
                elif "vice president of art of living club 2018" in query:
                    speak("piyush auditchya")
                elif "vice president of adventure club 2018" in query:
                    speak("ruchit gautam")
                elif "vice president of literary club 2018" in query:
                    speak("piyush auditchya")
                elif "vice president of cultural club 2018" in query:
                    speak("avinash sharma")
                elif "secretary of technical club 2018" in query:
                    speak("gopal krishna mandal")
                elif "secretary of cultural club 2018" in query:
                    speak("anjali jain")
                elif "secretary of adventure club 2018" in query:
                    speak("kush pratap")
                elif "secretary of literary club 2018" in query:
                    speak("salim")
                elif "secretary of art of living club 2018" in query:
                    speak("shivani")
                elif "duration of each president in a club" in query:
                    speak("one year.")
                elif "colour of cultural" in query:
                    speak("burgundy colour is the symbol of cultural group.")
                elif "colour of adventure" in query:
                    speak("navy blue is the symbol of adventure group.")
                elif "colour of literary" in query:
                    speak("orange colour is the symbol of literary group.")
                elif "colour of art of living club" in query:
                    speak("yellow colour is the symbol of living group.")
                elif "colour of technical club" in query:
                    speak("black colour is the symbol of technical group.")
                elif "activities conducted by technical club" in query:
                    speak("quiz, pt, debates were conducted by this club.")
                elif "activities conducted by adventure club in" in query:
                    speak("kabbadi, basketbal,cricket, kho kho, table tenis were conducted by  this club.")
                elif "activities conducted by adventure club" in query:
                    speak("kabbadi, basketbal,cricket, kho kho, table tenis were conducted by  this club.")
                elif "activities conducted by art of living club in" in query:
                    speak("yoga and aasanas, seminar for peace were conducted by this club.")
                elif "activities conducted by art of living club" in query:
                    speak("yoga and aasanas, seminar for peace were conducted by this club.")
                elif "activities conducted by literary club" in query:
                    speak("esay, debates and poetry were  conducted by this club")
                elif "activities conducted by literary club in" in query:
                    speak("esay, debates and poetry were  conducted by this club")
                elif "activities conducted by cultural club" in query:
                    speak("mehendi, poster,colage,rangoli were conducted by this group.")
                elif "activities conducted by cultural club in" in query:
                    speak("mehendi, poster,colage,rangoli were conducted by this group.")
                elif "activities conducted by adventure club in" in query:
                    speak("kabbadi, basketbal,cricket,kho kho, table tenis are conducted by this club.")
                elif "activities conducted by cultural club in" in query:
                    speak("mehendi,poster,colage,rangoli were conducted by this group.")      
                elif "formation of clubs" in query:
                    speak("in 2018 all clubs were formed.")
                elif "formation of all clubs" in query:
                    speak("in 2018 all clubs were formed.")
                elif "arooma and freshers party are conducted by which club" in query:
                    speak("these conducted by cultural group in each year.")
                elif "number of club members in technical club" in query:
                    speak("20")
                elif "members in technical club" in query:
                    speak("20")
                elif "number of club members in cultural club" in query:
                    speak("45")
                elif "members in cultural club" in query:
                    speak("45")
                elif "numbers of club members in art of living club" in query:
                    speak("30")
                elif "members in art of living club" in query:
                    speak("30")
                elif "numbers of club members in literary club" in query:
                    speak("25")
                elif "members in literary club" in query:
                    speak("25")
                elif "members in adventure club" in query:
                    speak("35")
                elif "which club is going to conduct arooma in 2019" in query:
                    speak("cultural club will conduct in 2019.")
                elif "which club conducted drama for women on womens day in 2018" in query:
                    speak("art of living club.")
                elif "which day is alloted for wearing club uniform" in query:
                    speak("saturday is alloted for wearing club uniform.")
                elif "on which day meetings of technical club are held" in query:
                    speak("on tuesday this clubs meetings are held.")
                elif "meeting of technical club" in query:
                    speak("on tuesday this clubs meetings are held.")
                elif "on which day meetings are held for cultural club" in query:
                    speak("on wednesday this clubs meetings are held.")
                elif "meeting of cultural club" in query:
                    speak("on wednesday this clubs meetings are held.")
                elif "on which day meetings are held for adventure club" in query:
                    speak("on friday this clubs meetings are held.")
                elif "meeting of adventure club" in query:
                    speak("on friday this clubs meetings are held.")
                elif "on which day meetings are held for art of living club" in query:
                    speak("on monday this clubs meetings are held for club.")
                elif "meeting of art of living club" in query:
                    speak("on monday this clubs meetings are held for club.")
                elif "on which day meetings are held for literary club" in query:
                    speak("on thursday meetings are held for this club.")
                elif "meeting of literary club" in query:
                    speak("on thursday meetings are held for this club.")
                
                elif "which club is organizing a donation campaign in 2019" in query:
                    speak("art of living club is organizing.")
                elif "marathons are conducted by which group" in query:
                    speak("art of living group.")
                elif "volunteers in arooma will be from which group" in query:
                    speak("volunteers wil be from cultural group.")
                elif "last year dandiya nights was conducted by which club" in query:
                    speak("cultural club organized it")
                elif "motive of all clubs" in query:
                    speak("main motive is to make people aware and participate in each activity and become aware.")
                elif "who is the controller of al these clubs" in query:
                    speak("mr. hemant dha bhai (director)")
                elif "from which university is aravali affiliated" in query:
                    speak("aits is affiliated from rtu and bter.") 
                elif "aravali affiliated" in query:
                    speak("a i t s is affiliated from rtu and bter.") 
                elif "what is the area of your campus" in query:
                    speak("our campus is spread in 15 acre.")
                elif "when has your institute been established" in query:
                    speak("our institute has been established in 2008.")
                elif "established" in query:
                    speak("our institute has been established in 2008.")
                elif "how many buildings are in your campus" in query:
                    speak("6 separate buildings are there in our campus.")
                elif "buildings" in query:
                    speak("6 separate buildings are there in our campus.")
                elif "have any playground in your campus" in query:
                    speak("separate playground is available for different sports.")
                elif "is hostel facility available in your campus" in query:
                    speak("yes, hostel facility is available in our campus with mess.")
                elif "hostel facility" in query:
                    speak("yes, hostel facility is available in our campus with mess.")
                elif "is your campus having canteen" in query:
                    speak("yes, canteen is available in our campus.")
                elif "does your campus provide night stay facility for parents" in query:
                    speak("yes, we provide night stay facility for student's parents in campus")
                elif "is lateral entry available" in query:
                    speak("yes, lateral entry is available for b.tech and diploma both.")
                elif "is library available in your campus" in query:
                    speak("yes, we have a hi tech library with more than 50000 boks, journals etc.")
                elif "do you provide traveling facility for hostelers to go outside from campus" in query:
                    speak("yes. we provide bus facility to go outside.")
                elif "is garden available in your campus" in query:
                    speak("yes, in our campus lush green gardens are available for yoga & walking.")
                elif "do you provide extra clases for hostelers in night in your campus" in query:
                    speak("yes, we provide extra clases for hostelers.")
                elif "do you allow student phone in" in query:
                    speak("yes, we allow.")
                elif "do you allow students to keep personal vehicle" in query:
                    speak("yes, we allow keeping personal vehicle.")    
                elif "is here students form different state" in query:
                    speak("yes, students of 15 states is studying here.")
                elif "have students permission to celebrate their regional festival" in query:
                    speak("yes, we also coperate to celebrate.")
                elif "what is the timing of closing the campus gate" in query:
                    speak("the closing time is generaly 8 pm and it changes acording to season.")
                elif "have students to take any special permission to go out from campus" in query:
                    speak("yes, you have to take a gate pas from your hostel encharge.")
                elif "have your campus ragging free" in query:
                    speak("yes, our campus is fuly ragging free.")
                elif "ragging free" in query:
                    speak("yes, our campus is fuly ragging free.")
                elif "our campus ragging free" in query:
                    speak("yes, our campus is fuly ragging free.")
                elif "who is warden of pratap hostel" in query:
                    speak("mister rahul gangwani.")
                elif "who is the warden of pratap hostel" in query:
                    speak("mister rahul gangwani.")
                elif "who is warden of boys hostel" in query:
                    speak("mister mister pramod Kumaar.")
                elif "who is the warden of boys hostel" in query:
                    speak("mister pramod choudhary.")
                elif "who is warden of raman hostel" in query:
                    speak("mister pramod choudhary.")
                elif "who is the warden of raman hostel" in query:
                    speak("mister pramod choudhary.")
                elif "who is the chief warden of" in query:
                    speak("mister pramod choudhary.")
                elif "who is warden of aravali girls hostel" in query:
                    speak("nihala chauhan")
                elif "who is the warden of girls" in query:
                    speak("nihala chauhan")  
                elif "how many courses do you provide in aits" in query:
                    speak("we provide four programs like b tech, m tech, m c a and diploma.")
                elif "how many courses" in query:
                    speak("we provide four programs like b tech, m tech, m c a and diploma.")
                elif "how many courses provide" in query:
                    speak("we provide four programs like b tech, m tech, m c a and diploma.")
                elif "how many courses" in query:
                    speak("we provide four programs like b tech,m tech, m c a and diploma.")    
                elif "how many branches are available in b tech" in query:
                    speak("five branches are available in b.tech.")
                elif "how many branches are available in diploma" in query:
                    speak("four branches are in diploma.")
                elif "how many branches are available in mtech" in query:
                    speak("we offer four branches in m.tech.")
                elif "how many seats are available in b.tech electronics and comunication" in query:
                    speak("30 seats are available.")
                elif "how many seats are available in btech" in query:
                    speak("90 seats are available.")
                elif "how many seats are available in btech civil engineering" in query:
                    speak("60 seats are available.")
                elif "how many seats are available in btech electrical engineering" in query:
                    speak("60 seats are available.")
                elif "how many seats are available in b.tech computer science engineering" in query:
                    speak("60 seats are available.")
                elif "how many seats are available in diploma civil engineering" in query:
                    speak("60 seats are available.")
                elif "how many seats are available in diploma electrical engineering" in query:
                    speak("60 seats are available.")
                elif "how many seats are available in diploma mechanical engineering" in query:
                    speak("60 seats are available.")
                elif "how many seats are available in diploma computer science engineering" in query:
                    speak("60 seats are available.")
                elif "how many seats are available in thermal engineering" in query:
                    speak("18 seats are available.")
                elif "how many seats are available in production engineering" in query:
                    speak("24 seats are available.")
                elif "how many seats are available in digital comunication" in query:
                    speak("24 seats are available.")
                elif "how many seats are available in power electronics and electric drives" in query:
                    speak("24 seats are available.")
                elif "how many seats are available in software engineering" in query:
                    speak("24 seats are available.")
                elif "how many seats are available in mca" in query:
                    speak("60 seats are available.")
                elif "what is the course duration of btech" in query:
                    speak("the course duration of b.tech is 4 years (8 semesters).")
                elif "what is the course duration of mtech" in query:
                    speak("the course duration of m.tech is 2 years (4 semesters).")
                elif "what is the course duration of diploma" in query:
                    speak("the course duration of diploma is 3 years.")
                elif "what is the course duration of mca" in query:
                    speak("mca is a 2 years program.")
                elif "what are eligibility criteria for btech" in query:
                    speak("you have pased 12th with minimum 45% in pcm.")
                elif "what are eligibility criteria for mtech" in query:
                    speak("you have pased b.tech/ b.e in relevant branch.")
                elif "what are eligibility criteria for diploma" in query:
                    speak("you have pased 10th with minimum 45% from any recognised board.")
                elif "what are eligibility criteria for mca" in query:
                    speak("you have to pas 12th with mathematics and graduation in b.sc, bca, b.com.")
                elif "what is the fee structure of btech" in query:
                    speak("you have to pay 35000 rupees per sem. ")
                elif "what is the fee structure of mtech" in query:
                    speak("you have to pay 35000 rupees per sem. ")
                elif "what is the fee structure of mca" in query:
                    speak("you have to pay 35000 rupees per sem. ")
                elif "what is the fee structure of diploma" in query:
                    speak("you have to pay 28000 rupees per sem. ")
                elif "is lateral entry available" in query:
                    speak("yes, lateral entry is available for b.tech and diploma.")
                elif "is your organisation a member of rotary club" in query:
                    speak("yes, our organisation is a member of rotary club, udaipur. ")
                elif "how many clubs in" in query:
                    speak("six clubs are in our organisation.")
                elif "do you conduct industrial visits" in query:
                    speak("yes, our students visit industry on regular interval.")
                elif "do you offer certification programs for students" in query:
                    speak("yes, we offer certification programs.")
                elif "do you provide hands on training in different areas of engineering" in query:
                    speak("yes. we provide hands on training.")
                elif "do you conduct guest lectures" in query:
                    speak("yes, we conduct guest lectures.")
                elif "do you have holiday on every saturday" in query:
                    speak("no, we don't have holiday on saturday.")
                elif "have you colaboration with industries" in query:
                    speak("yes.")
                elif "do you provide noc for those students who get placement during academic session" in query:
                    speak("yes, we provide noc who get placement from campus.")
                elif "is aits is aproved by aicte" in query:
                    speak("yes")
                elif "is aravali aproved by aicte" in query:
                    speak("yes")
                elif "from which university is aits affiliated" in query:
                    speak("rajasthan technical university,kota and bter")
                elif "why aits is better than other college" in query:
                    speak("experienced & qualified faculties& staff with strong focus on teaching. senior profesors/faculties are available for regular teaching.")
                elif "how many courses are offered by this college" in query:
                    speak("we offer courses such that diploma, b.tech, m.tech,mca")
                elif "what is duration of btech course" in query:
                    speak("four year(8 semesters)")
                elif "how many streams are available in btech" in query:
                    speak("computer engineering, electronics and comunication engineering, civil engineering, electrical engineering, mechanical engineering.")
                elif "how many branches are available in btech" in query:
                    speak("computer engineering, electronics and comunication engineering, civil engineering, electrical engineering, mechanical engineering.")
                elif "what are the eligibility criteria of btech" in query:
                    speak("you have qualified senior secondary with at least 45% marks with physics,chemistryand mathematics and any one compulsory subject like computer, biology.")
                elif "what is duration of m.tech course" in query:
                    speak("two year(4 semesters)")
                elif "how many streams are available in mtech" in query:
                    speak("thermal engineering, production engineering, digital comunication, softwareengineering, power electronics and electric drives")
                elif "how many branches are available in mtech" in query:
                    speak("thermal engineering, production engineering, digital comunication, softwareengineering, power electronics and electric drives")
                elif "how many years is mca course" in query:
                    speak("three year ")
                elif "how many seats are in mca course" in query:
                    speak("60 seats are available.")
                elif "what are the eligibility criteria of mtech course" in query:
                    speak("you have qualified b.tech/be in relevant branch.")
                elif "what are the eligibility criteria of diploma course" in query:
                    speak("you would be qualified 10th clas from any recognized board.")
                elif "what is the fees structure for diploma per year" in query:
                    speak("twenty eight thousand per year.")
                elif "m.tech programis available in aravali institute of technical studies" in query:
                    speak("yes m.tech program is available.")
                elif "how many hostels are available in aravali campus" in query:
                    speak("there are two hostels available in aravali campus: raman hostel and pratap hostel.")
                elif "how many boys can live in one room in pratap hostel" in query:
                    speak("four boys can live in one room.")
                elif "what are the facilities available in hostel" in query:
                    speak("many facilities are available in hostel such as tv room, gym facility, study room facility, security etc.")
                elif "is wi fi available in hostel" in query:
                    speak("yes, wi fi is available 24 hours with high speed.")
                elif "what is the capacity of pratap hostel" in query:
                    speak("the capacity of pratap hostel is 330 boys.")
                elif "is there medical facility in your hostel" in query:
                    speak("yes, we provide medical facility in hostel.")
                elif "how many boys can live in raman hostel" in query:
                    speak("the capacity of raman hostel is 210 boys.")
                elif "is girls hostel facility available in aits campus" in query:
                    speak("yes")
                elif "is security available in girls hostel" in query:
                    speak("yes")
                elif "who is the warden of the girls hostel" in query:
                    speak("ms. nihala chauhan is warden of girls hostel.")
                elif "where is the girls hostel" in query:
                    speak("in aravali campus")
                elif "do you provide the traveling facility for girls hostel" in query:
                    speak("yes")

                elif "travelling facility" in query:
                    speak("yes")    
                elif "how many girls can stay in a room in girls hostel" in query:
                    speak("here, two types of room available like 4 and 3 siter.")
                elif "what is the dinner time in girls hostel" in query:
                    speak("7:30 pm to 8:30 pm")
                elif "girls can stay" in query:
                    speak("here, two types of room available like 4 and 3 siter.")
                elif "dinner time" in query:
                    speak("7:30 pm to 8:30 pm")    
                elif "can students use electric items in girls hostel" in query:
                    speak("no")
                elif "use electric items" in query:
                    speak("no")
                elif "is wi fi available in girls hostel" in query:
                    speak("yes")
                elif "wi fi is available " in query:
                    speak("yes")
                elif "what is the breakfast time in girls hostel" in query:
                    speak(" 8:30 to 9:00 am")
                elif "breakfast time" in query:
                    speak(" 8:30 to 9:00 am")
                elif "is there separate room facility for first year students in girls hostel" in query:
                    speak("no")
                elif "separate room facility" in query:
                    speak("no")
                elif "is there medical facility in girls hostel" in query:
                    speak("no")
                elif "medical facility" in query:
                    speak("no")
                elif "medical treatment" in query:
                    speak("no")
                elif "is the drinking water facility in girls hostel" in query:
                    speak("yes")
                elif "is there ambulance facility in girls hostel" in query:
                    speak("no")
                elif "drinking water facility" in query:
                    speak("yes")
                elif "ambulance facility" in query:
                    speak("no")
                elif "is the facility of gym in girls hostel" in query:
                    speak("no")
                elif "gym facility for girls" in query:
                    speak("no")
                elif "does the girls hostel have newspaper facility" in query:
                    speak("no")
                elif "newspaper facility" in query:
                    speak("no")
                elif "do you allow girls parents to stay in the hostel" in query:
                    speak("no, we don't allow.")
                elif "allow girls parents to stay in the hostel" in query:
                    speak("no, we don't allow.")
                elif "is the feature of separate bathrooms in girls hostel" in query:
                    speak("yes")
                elif "is the facility of study room available in girls hostel" in query:
                    speak("no")
                elif "separate bathrooms in girls" in query:
                    speak("yes")
                elif "study room available in girls" in query:
                    speak("no")
                elif "what is the closing timing of the girls hostel" in query:
                    speak("in the sumer 8:00pm and winter 7:00pm ")
                elif "what is the closing timing of the girls" in query:
                    speak("in the sumer 8:00pm and winter 7:00pm ")
                elif "how many softwares are available in aravali college" in query:
                    speak("in cs turbo ,linux,internet lab.in civil&mech autocad.ece&ee matlab,cadlab,xilinx")
                elif "software available" in query:
                    speak("in cs turbo ,linux,internet lab.in civil&mech autocad.ece&ee matlab,cadlab,xilinx")
                elif "softwares are available" in query:
                    speak("in cs turbo ,linux,internet lab.in civil&mech autocad.ece&ee matlab,cadlab,xilinx")
                elif "in which year summer training is done in b tech" in query:
                    speak("b tech students start their summer training in 3rd year.")
                elif "in which year summer training is done in diploma" in query:
                    speak("diploma student get their summer training in 2nd year.")
                elif "time duration of b.tech sumer training" in query:
                    speak("the time duration of summer training in b tech is 60 days.")
                elif "time duration of sumer training" in query:
                    speak("the time duration of summer training is 60 days.")
                elif "time duration of diploma summer training" in query:
                    speak("the time duration of summer training in diploma is 60 days.")
                elif "in which year training is done in bsc nursing" in query:
                    speak("bsc nursing students start their summer training in 2rd year.")
                elif "in which year training is done in bed." in query:
                    speak("b.ed. students start their training in 2nd year.")
                elif "does your college provide training" in query:
                    speak("yes our college provide training")
                elif "time duration of bsc nursing training" in query:
                    speak("b.sc nursing students complete their training in 3 months.")
                elif "who is the advisor of training" in query:
                    speak("not available")
                elif "advisor of training" in query:
                    speak("not available")
                elif "advantages of doing training" in query:
                    speak("students  got clear practical concept, productive skil development, discipline maintenance,")
                elif "advantages of training" in query:
                    speak("students  got clear practical concept, productive skil development, discipline maintenance,")
                elif "will students be placed in the same companies from which they got training" in query:
                    speak("yes of course but it completely depend on students performance.")
                elif "placed in the same companies they provide" in query:
                    speak("yes of course but it completely depend on students performance.")
                elif "from where civil students will get the training" in query:
                    speak("lnt,pwd,autocad course, any private construction company,jk cement ,birla cement")
                elif "civil students get the training" in query:
                    speak("lnt,pwd,autocad course, any private construction company,jk cement ,birla cement")
                elif "from where the mechanical students will get the training" in query:
                    speak("autocad , slodworks courses, hcl, bhel, cel, bel, ntpc, indian railway")
                elif "mechanical students get the training" in query:
                    speak("autocad , slodworks courses, hcl, bhel, cel, bel, ntpc, indian railway")
                elif "from where the ece students get the training" in query:
                    speak("electronics company like r&d company and in comunication like bsnl ,bpo,ebedded system  bhel , indian railways, matlab, xilinx, orcad.")
                elif "from where the cs students get the training" in query:
                    speak("jaipur dot square, in php, java, dot net courses, and many private companies.")
                elif "from where the electrical student wil get the training" in query:
                    speak("bhel, cel, bel, indian railways and gs station.")
                elif "cs students get the training" in query:
                    speak("jaipur dot square, in php, java, dot net courses, and many private companies.")
                elif "where the electrical student will get the training" in query:
                    speak("bhel, cel, bel, indian railways and gs station.")
                elif "where the students go for training" in query:
                    speak("we provide training in various companies acording to their branch.                 ")
                elif "is it compulsory to do training from college side" in query:
                    speak("no its not compulsory to do training from college side.")
                elif "compulsory to do training from" in query:
                    speak("no its not compulsory to do training from college side.")
                elif "what is the main motive of training" in query:
                    speak("when you go for job interview then 1st thing hr asks is about your training.")
                elif "motive of training" in query:
                    speak("when you go for job interview then 1st thing hr asks is about your training.")
                elif "is training compulsory" in query:
                    speak("yes, it is compulsory as mentioned in the rtu guidelines.")
                elif "what is the main motive of training" in query:
                    speak("when you go for job interview then 1st thing hr asks is about your training.")
                elif "training is compulsory" in query:
                    speak("yes, it is compulsory as mentioned in the rtu guidelines.")
                elif "what are the expected outcomes" in query:
                    speak("your primary goal is to improve and develop learning solutions.")
                elif "what are managements expectations" in query:
                    speak("your responsibility is to know youre their busines, then develop a training solution &see the outcomes.")
                elif "what will the training cost" in query:
                    speak("its depends on company.")
                elif "training cost" in query:
                    speak("its depends on company.")
                elif "what qualities does a company expect in a trainer" in query:
                    speak("methodical and well planed, well in comunication.")
                elif "how are training needs identified" in query:
                    speak("we provide certificate of each every training to individual students.")
                elif "what is the difference between training and learning" in query:
                    speak("training is the giving of knowledge and learning is the proces of observing that increase skils ")
                elif "difference between training and learning" in query:
                    speak("training is the giving of knowledge and learning is the proces of observing that increase skils ")
                elif "what are the college facilities available for training" in query:
                    speak("with every training session we have asesment for every student and provide a test for every students")
                elif "describe recent job training activities you facilitated" in query:
                    speak("college recently provided nptel training.")
                elif "what do you consider the key criteria for training" in query:
                    speak("basic knowledge.")
                elif "key criteria for training" in query:
                    speak("basic knowledge.")
                elif "how you evaluate the result of training" in query:
                    speak("basis of training knowledge which they got.")
                elif "do they offer jobs for students after training" in query:
                    speak("yes, maximum students got job after training.")
                elif "offer jobs for students after training" in query:
                    speak("yes, maximum students got job after training.")
                elif "what is the usp of college for training purpose" in query:
                    speak("25+ training and every training there have industrial visit.")
                elif "in how many companies ece students gone to do training in last some year" in query:
                    speak("ece students gone to do their training in 8+companies in last some years.")
                elif "companies ece students gone for training" in query:
                    speak("ece students gone to do their training in 8+companies in last some years.")
                elif "in how many companies electrical students gone to do training in last some year" in query:
                    speak("electrical students gone to did their training in 7+ companies in last some years.")
                elif "in how many companies cse students gone to do training in last some years " in query:
                    speak("cse students gone to did their training in 12+ companies in last some years.")
                elif "in how many companies cs students gone to do training in last some years " in query:
                    speak("ce students gone to do their training in 4+ companies in last some years.")
                elif "in how many companies mechanical students gone to do training in last some years " in query:
                    speak("mechanical students gone to do their training in 6+ companies in last some years.")
                elif "electrical students gone to do training" in query:
                    speak("electrical students gone to did their training in 7+ companies in last some years.")
                elif "cse students gone to do training" in query:
                    speak("cse students gone to did their training in 12+ companies in last some years.")
                elif "cs students gone to do training" in query:
                    speak("ce students gone to do their training in 4+ companies in last some years.")
                elif "mechanical students gone to do training" in query:
                    speak("mechanical students gone to do their training in 6+ companies in last some years.")
                elif "how many training workshops where conducted in session 2018 19 for ece" in query:
                    speak("six")
                elif "how many training workshops where conducted in session 2018 19 for electrical" in query:
                    speak("seven")
                elif "how many training workshops where conducted in session 2018 19 for civil" in query:
                    speak("twelve")
                elif "how many training workshops where conducted in session 2018 19 for mechanical" in query:
                    speak("four")
                elif "training workshops conducted for ece" in query:
                    speak("six")
                elif "training workshops conducted for electrical" in query:
                    speak("seven")
                elif "training workshops where conducted for civil" in query:
                    speak("twelve")
                elif "training workshops where conducted for mechanical" in query:
                    speak("four")
                elif "are multinational companies visiting your college" in query:
                    speak("yes")
                elif "multinational companies" in query:
                    speak("yes")
                elif "which type of training was given by college to the students to face interview" in query:
                    speak("yes, so many multinational companies visited in our college.")
                elif "which type of training was given by college" in query:
                    speak("yes, so many multinational companies visited in our college.")    
                elif "are the students geting noc in final year if they placed in any company" in query:
                    speak("yes the student get noc in final year, if they placed in any company..")
                elif "students geting noc in final year" in query:
                    speak("yes the student get noc in final year, if they placed in any company.")
                elif "how many projects have been selected in distic level from your college" in query:
                    speak(" ")
                elif "how many projects have been selected in distic level" in query:
                    speak(" ")
                elif "is any student got any rank in rajasthan technical university from your college" in query:
                    speak("yes,many students got rank in rajasthan technical university from our college.")
                elif "any student got any rank in rajasthan technical university" in query:
                    speak("yes,many students got rank in rajasthan technical university from our college.")
                elif "is any student got any rank in board of technical education rajasthan from your college" in query:
                    speak("yes, students got rank in board of technical education rajasthan from our college.")
                elif "any student got any rank in board of technical education rajasthan" in query:
                    speak("yes, students got rank in board of technical education rajasthan from our college.")
                
                elif "companies which companies" in query:
                    speak("secure meters ltd. wonder cement,rosava engineers, arcgate,wizobit& many more.")
                elif "what is the best achievement of your college" in query:
                    speak("our student nehapaneri, got gold medal from rtu.")
                elif "do non technical companies also visited in your college" in query:
                    speak("yes,non technical companies also visited in our college.")
                elif "name some non technical companies which visit in your college" in query:
                    speak("rang technologies, fusion, dronacharya, avins etc.")
                elif "how many national level projects have been selected from your college" in query:
                    speak("1 project")
                elif "how many state level projects have been selected from your college" in query:
                    speak("4 project")
                elif "what is the average placement of your college in the year 2017  18" in query:
                    speak("seventy five percent")
                elif "what is the average placement of your college in the year 2018 19" in query:
                    speak("eighty percent")
                elif "how long an internship can be" in query:
                    speak("it about 10 weeks to 3 months or the duration of one semester or quarter is a comon internship length.")
                elif "does your college have membership with any industry or organisation" in query:
                    speak("yes, our college has membership with indian space research and organisation and other organisations as wel.")
                elif "does your college have membership with any organisation" in query:
                    speak("yes, our college has membership with indian space research and organisation and other organisations as wel.")
                elif "does your college have membership" in query:
                    speak("yes, our college has membership with indian space research and organisation and other organisations as wel.")

                elif "is aravali awarded by any organisation or government institute" in query:
                    speak("yes, our college have been awarded so many times like, 1.  education  leadership award 2012, 2. bharat shiksha award 2013, ")
                elif "name some core companies which visited in your college for electronics and comunications branch only" in query:
                    speak("lipidata, pyrotech, tempson etc.")
                elif "name some core companies which visited in your college for computer science branch only" in query:
                    speak("wizorbit,argate,paytm")
                elif "name some core companies which visited in your college for civil branch only" in query:
                    speak("avins ")
                elif "name some core companies which visited in your college for mechanical branch only" in query:
                    speak("jayshree polymer,roljak asia ltd.")
                elif "is every student get chance to place in this college" in query:
                    speak("yes")
                elif "only all clear students placed or backlog students also placed in college" in query:
                    speak("both(depend upon the company norms and policies)")
                elif "how many companies visited in the year 2016" in query:
                    speak("25 companies")
                elif "how many companies visited in the year 2017" in query:
                    speak("30 companies")
                elif "how many companies visited in the year 2018" in query:
                    speak("50 companies")
                elif "how many companies visited in the year 2022" in query:
                    speak("50 companies")
                elif "how many students are placed in the year 2018" in query:
                    speak("70+ students placed in the year 2018.")
                elif "how many students are placed in the year 2022" in query:
                    speak("70+ students placed in the year 2022.")
                elif "is your college providing stream vise placement to students" in query:
                    speak("yes")
                elif "industrial visits are helpful in placement of students" in query:
                    speak("yes,if the same company come for placement it wil be helpful.")
                elif "proper training of interview skils and personality development traits are necesary to have in every student" in query:
                    speak("yes")
                elif "is it necesary to have good comunication skills for placement activity" in query:
                    speak("yes")
                elif "is every student should have practical knowledge or explosure necesary to have placement in company" in query:
                    speak("yes ,depend upon company")
                elif "what are eligibility criteria to get placement in any company for all clear students" in query:
                    speak("students should have 60% in x,xii ,b.tech (i,ii,iii year ) with god comunication skils,pleasent personality.")
                elif "what are eligibility criteria to get placement in any company for backlog students" in query:
                    speak("students dont have more than 1 back and also have god comunication skils.")
                elif "what is the maximum package of your college" in query:
                    speak("4 lpa")
                elif "what is the minimum package of your college" in query:
                    speak("15 lpa")
                elif "how many times your college organized a job fair" in query:
                    speak("5 times")
                elif "is your college is organizing job fair" in query:
                    speak("yes")
                elif "are students aware about the industry rules and regulations and working environment" in query:
                    speak("yes")
                elif "is students are encouraged for entrepreneurship" in query:
                    speak("yes")
                elif "how many students is entrepreneur" in query:
                    speak("fifteen")
                elif "industry oriented practical training are given to the students" in query:
                    speak("yes")
                elif "is students are wel versed with the upcoming new technology" in query:
                    speak("yes")
                elif "how many companies have visited in job fair in the year 2014 15" in query:
                    speak("8 companies")
                elif "how many companies have visited in job fair in the year 2015 16" in query:
                    speak("8 companies")
                elif "how many companies have visited in job fair in the year 2016 17" in query:
                    speak("10 companies")
                elif "how many companies have visited in job fair in the year 2017 18" in query:
                    speak("12 companies")
                elif "how many companies have visited in job fair in the year 2018 19" in query:
                    speak("42 companies")
                elif "what is the qiv rating of your college" in query:
                    speak("first, declared by rtu")
                elif "how many training does your college provide" in query:
                    speak("our college provides 15 plus training.")
                elif "how many times your college doestake the students for industrial visit" in query:
                    speak("our college takes the students more than 20 times for industrial visit.")
                elif "what is the highest package provided by your college" in query:
                    speak("78 lakh and more than that.")
                elif "in past 4 years how many students got placement by your college" in query:
                    speak("we have 500 plus selection in past 4 years.")
                elif "who is the head of training and placement cel" in query:
                    speak("")
                elif "who is the head of e cell" in query:
                    speak("")
                elif "who is the head of carier cell" in query:
                    speak(" ")
                elif "who is the head of women cell" in query:
                    speak("")
                elif "who is the head of anti ragging cell" in query:
                    speak(" ")
                elif "who is the head of student monitoring cell" in query:
                    speak("")
                elif "how can we identify that you are providing training to students" in query:
                    speak("you can check live videos and photos on our aravalifacebok page.")
                elif "how can parent monitor their child activities in college" in query:
                    speak("they can monitor their child activity on erp including subject wise atendance, marks etc.")
                elif "is there any mou between college and the company" in query:
                    speak("yes")
                elif "what is academic achievement of your college" in query:
                    speak("one")
                elif "how many workshops were conducted in session 2018 19 for electronic branch" in query:
                    speak("one")
                elif "how many workshops were conducted in session 2018 19 for civil branch" in query:
                    speak("one")
                elif "how many workshops were conducted in session 2018 19 for mechanical branch" in query:
                    speak("one")
                elif "how many workshops were conducted in session 2018 19 for electrical branch" in query:
                    speak("one")
                elif "how many seminars were conducted in session 2018 19 for electonic branch" in query:
                    speak("ten")
                elif "how many seminars were conducted in session 2018 19 for computer science branch" in query:
                    speak("fifteen")
                elif "how many seminars were conducted in session 2018 19 for eletrical branch" in query:
                    speak("fifteen")
                elif "how many seminar were conducted in session 2018 19 for civil branch" in query:
                    speak("eight")
                elif "how many seminars were conducted in session 2018 19 for mechanial branch" in query:
                    speak("seven")
                elif "where is aravali situated" in query:
                    speak("It is located at a distance of 11 km from Udaipur city and opposite to Umarda Railway Station, udaipur")
                elif "where is aravali" in query:
                    speak("It is located at a distance of 11 km from Udaipur city and opposite to Umarda Railway Station, udaipur")
                elif "how many students in" in query:
                    speak("there are 5000 students is aravali college")
                elif "how many branches in" in query:
                    speak("there are 6 branches is aravali college")         
                elif "how many teachers" in query:
                    speak("there are 150 teachers in aravali college")
                elif "how many faculty" in query:
                    speak("there are 150 faculty in aravali college")
                elif "how many clubs in" in query:
                    speak("there are 6 clubs in aravali college")    
                elif "name of all clubs" in query:
                    speak("technical club, art of living club, literary club, adventure club, art of culture club, rotary club in aravali college")
                elif "president of technical club" in query:
                    speak("Raushan Kumar")         
                elif "president of art of culture club" in query:
                    speak("pappu yadav") 
                elif "president of art of living club" in query:
                    speak("Aditya")      
                elif "president of literary club" in query:
                    speak("Rajesh gurjar")          
                elif "president of adventure club" in query:
                    speak("sonu kumaar")              
                elif "president of rotract club" in query:
                    speak("vaibhaw mathur")            
                elif "president of adsw club" in query:
                    speak("vaibhaw mathur")       
                elif "how many rooms in" in query:
                    speak("95")       
                elif "where is robotics lab" in query:
                    speak("Room Number 218 ")            
                elif "where is cs department" in query:
                    speak("third floor")                                                 
                elif "where is computer science department" in query:
                    speak("third floor") 

                elif "where is mechanical department" in query:
                    speak("fourth floor") 
                elif "where is electrical department" in query:
                    speak("third floor")        
                elif "where is civil department" in query:
                    speak("second floor")     
                elif "where is artificial intelligence department" in query:
                    speak("third floor")                    
                elif "what is the highest package of ece" in query:
                    speak("10 lackh per anum")
                elif "what is the highest package of cs" in query:
                    speak("10 lackh per anum")
                elif "what is the highest package of civil engineering" in query:
                    speak("8 lackh per anum")
                elif "what is the highest package of mechanical engineering" in query:
                    speak("8 lackh per anum")
                elif "what is the highest package of electrical engineering" in query:
                    speak("8 lackh per anum")
                elif "what is the highest package of computer science" in query:
                    speak("10 lackh per anum")
                elif "what is the highest package of electrical engineering diploma" in query:
                    speak("5 lackh per anum")
                elif "what is the highest package of mechanical engineering diploma" in query:
                    speak("5 lackh per anum")
                elif "what is the highest package of civil engineering diploma" in query:
                    speak("5 lackh per anum")
                elif "which certified program your college offered to cse branch" in query:
                    speak("matlab certification program, embedded system design, dot   net certification program, oracle certification program.")
                elif "which certified program your college offered to electrical engineering branch" in query:
                    speak("matlab certification program, embedded system design")
                elif "which certified program your college offered to civil engineering" in query:
                    speak("auto cad, staad pro certification program")
                elif "which certified program your college offered to mechanical engineering" in query:
                    speak("auto cad")
                elif "how many industrial visits conducted in session 2018 19 for eletcronics and comunication branch" in query:
                    speak("two")
                elif "how many industrial visits were conducted in session 2018 19 for ece branch" in query:
                    speak("two")
                elif "how many industrial visits were conducted in session 2018 19 for electrical branch" in query:
                    speak("five")
                elif "how many industrial visits were conducted in session 2018 19 for computer  branch" in query:
                    speak("three")
                elif "how many industrial visits were conducted in session 2018 19 for civil branch" in query:
                    speak("four ")
                elif "how many industrial visits were conducted in session 2018 19 for mehanical branch" in query:
                    speak("six")
                elif "how many trainings were conducted in session 2018 19 for ece branch" in query:
                    speak("eight")
                elif "where is situated" in query:
                    speak("udaipur city , near umarda railway station")   
                elif "where is located" in query:
                    speak("udaipur city , near umarda railway station")    
 
                elif "what is the localtion" in query:
                    speak("udaipur city , near umarda railway station")    
                elif "how many teachers in computer science" in query:
                    speak("30,teachers")
                elif "how many teachers in cs" in query:
                    speak("30,teachers")    
                elif "how many teachers in civil" in query:
                    speak("30,teachers")
                elif "how many teachers in mechanical" in query:
                    speak("30,teachers")
                elif "how many teachers in electrical" in query:
                    speak("30,teachers")    
                elif "ok thanks" in query:
                    speak("it's my pleasure")

                elif "ok by" in query:
                    speak("ok bye")

                elif "is aits aproved by naac" in query:
                    speak("yes, with grade B")
                elif "is aits aproved by nba" in query:
                    speak("coming soon")
        
                elif "what is computer science engineering" in query:
                    speak("Computer Science Engineering (CSE) is an academic programme that integrates the field of Computer Engineering and Computer Science. It is one of the most sought after courses amongst engineering students.")

                elif "what is electrical engineering" in query:
                    speak("electrical engineering is an engineering decipline concerned with the study , design,and application of equipment devices and system which use electricity.")

                elif "what is civil engineering" in query:
                    speak("civil engineering is a professional engineering discipline that deals with the design ,construction and maintainance of physical and naturally built environment including public works .such as roads, bridge,dams,airport etc....")

                elif "what is mechanical engineering" in query:
                    speak("the branch of engineering dealing with the design construction and use of machine")

                elif "what is artificial intelligence engineering" in query:
                    speak("artificial intelligence engineering is a field of research and practice that combine the principles of sysytems engineering software engineering , computer science , human centered design to create artificial system")


                elif " " in query:
                    speak("can not understand, please ask me again")
                elif "KeyboardInterrupt" in query:
                    exit()
                else:
                    speak("can not understand, please restart again")

            except:
                # speak("can not understand, please restart again)
                pass

           
                        



 