import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


# Exercise data
exercises = [
    {
        "name": "Plank",
        "gif": "Gif Files/plank.jpg",
        "description":                                                  "Oyoqlarini birlashtirgan holda oshqozon ustida yoting, bilaklarni erga qo'ying, tirsaklar yelkalar ostida.\n"
                                                                        "Qorin bo'shlig'ini torting, bog'lang va glute mushaklarini siqib qo'ying.\n"
                                                                        "Tanani poldan ko'taring va boshdan to tovongacha tekis chiziq hosil qiling."
    },

    {
        "name": "Otjimaniye",
        "gif": "Gif Files/Push-ups.gif",
        "description":                                                  "Egiluvchan holatda qo'llar yelkalar ostiga tirsaklar cho'zilgan holda joylashtiriladi.\n" 
                                                                        "Barmoqlar erga tegib, orqa va oyoqlarni tekis tutish. Tanagacha tushiriladi\n" 
                                                                        "yuqori qo'l erga parallel. Keyin harakatni teskari tomonga o'zgartiring va qo'l uzaytirilguncha tanani ko'taring."
    },

    {
        "name": "Cho'kish",
        "gif": "Gif Files/squat.gif",
        "description":"QADAMLAR: o'llaringizni boshingizning orqa tomoniga qo'ying va oyoqlaringizni elkangiz kengligida\n"
        "bir-biridan ajratib turing, oyoqlari bir oz burilib, son bo'g'inini ochish uchun.Sonlaringiz polga parallel bo'lguncha tanangizni pastga tushiring.\n"
        "To'xtatib turing, so'ngra boshlang'ich pozitsiyasiga qayting.Takrorlang."                                                                                                                                                                              
    },
    
    {
        "name": "O'pkalar",
        "gif": "Gif Files/Lunges.gif",
        "description":"1)Oyoqlaringizni kestirib, kenglikda turing, orqangizni tekis, elkangizni orqaga torting va qorin bo'shlig'ingizni mahkam ushlang.\n" 
                      "2)Oldinga bir qadam tashlang va orqa tizzangiz poldan bir oz yuqoriroq bo'lguncha ikkala tizzangizni sekin eging.\n"
                      "3)Orqaga turing va harakatni takrorlang.\n"
                      "4)To'plam tugaguncha oyoqlarni almashtiring."                                                 
    },

    {
        "name": "Burpilar",
        "gif": "Gif Files/burpees.gif",
        "description":"1)Tik turishdan boshlang, qo'llar yon tomonda, oyoqlar bir-biridan kengligida bo'lishi kerak.\n"
                      "2)Oyoqlar oldidagi qo'llarni erga qo'yish uchun cho'kkalab, tizzalarni buking.\n"
                      "3)Tana vaznini qo'llarga qo'yib, oyoqlar elkalaridan to to'piqlarigacha to'g'ri chiziq bilan surish holatiga qaytariladi.\n"                                                                "3)Tana vaznini qo'llarga qo'yib, oyoqlar elkalaridan to to'piqlarigacha to'g'ri chiziq bilan surish holatiga qaytariladi.\n"
                      "4)Keyin oyoqlarni orqaga torting va cho'zilish holatiga qayting\n"
                      "5)Boshlang'ich tik holatiga qayting"                                                                 

    },

    {
        "name": "Alpinistlar",
        "gif": "Gif Files/Mountain Climbs.gif",
        "description":"Bu alpinistlarning asosiy tushunchasi. Plank holatidan bajarilganda, siz navbatma-navbat bir\n"
                      "tizzangizni ko'kragingizga olib kelasiz, keyin yana orqaga qaytib, polga yugurib ketguningizcha har safar tezlikni oshirasiz.\n"
                      "Harakat oddiydek tuyulsa-da, alpinistlar deyarli butun tanani mashq qiladilar va yurak urish tezligini oshiradilar." 
                                                                          
                                                                         
                                                                         
    },

    {
        "name": "Sakrash jaklari",
        "gif": "Gif Files/Jumping Jacks.gif",
        "description":"1)Boshlang'ich holatda, ibratni oqimlariga yotkazilgan holatda turib, qo'l va oyoqlarni yon yonaga joylashtiring.\n"
                      "2)Boshingizni boshqalar bilan bir xil sathda tuting va qoraqamishlarni qo'llab-quvvatlang.\n"
                      "3)Boshlang'ich holatdagi joyingizdan aralash, qo'l va oyoqlarni bir vaqtda yon yonaga kengaytirib chiqaring.\n"
                      "4)Eshiklar va qo'llar yuqoriga qo'tarib, oyoqlarni jidallab yuboring.\n"
                      "5)Oyoqlaringizni o'rga va yon yonaga yopib, qo'llarni boshlang'ich holatga qaytaring.\n"
                      "6)Ushbu harakatni tekrarlangan marta amalga oshiring."
    },

    {
        "name": "V O'tirgan velosipedlar",
        "gif": "Gif Files/Sit Bicycles.gif",
        "description":"V O'tirgan velosipedlar bo'yicha ko'rsatmalar\n" 
                      "1)Oyoqlarini bir oz egilgan holda yoting\n"
                      "2)Yuqori tanangizni ko'taring, shunda u sonlaringiz bilan V shaklini yaratadi.\n"
                      "3)Tanangizni o'ngga burang, o'ng tizzangizni chap tirsagingizga yaqinlashtiring va chap oyog'ingizni to'liq uzating.\n"
                      "4)Boshlang'ich pozitsiyasiga qayting va keyin qarama-qarshi tomonga buriling."
    },

    {
        "name": "Ruscha burilishlar",
        "gif": "Gif Files/Russia Twists.gif",
        "description":"1)Boshlang'ich holatda, yerdan iste'mol qiladigan bir stul yoki matga otiring.\n Oyoqlaringizni yerga qo'yib, oyoqlaringizni yon yonaga yo'llang.\n"
                      "2)Eslatib o'tamiz, belingizni bir tomonga qaytaring, o'ng belingizni chap tomoningizga yo'naltiring.\n"
                      "3)Qo'llaringizni orqaga olib, ibrat bilan birlashtiring. Qo'llaringizni ko'kka qaraganda yon yonaga uzatib chiqaring.\n"
                      "4)Qisqa masofada, belingizni chap tomoningizga yo'naltirib, qo'llaringizni o'ng tomoningizga yo'naltirib chiqaring\n"
                      "5)Ushbu holatni to'g'ri bajaring, belingizni tomon tomoningizga yo'naltiring.\n"
                      "6)Amalning boshqa tomoniga o'tib kelganida, qo'llaringizni o'ng yoki chap tomoningizga uzatib olib, qaytadan birlashtiring.\n"
                      "7)Mashqni tekrarlangan marta amalga oshiring.\n"

    },

    {
        "name": "Baland tizzalar",
        "gif": "Gif Files/High Knees.gif",
        "description":"1)Boshlang'ich holatda, to'rtburchakning boshqa joyiga turib, qo'l va oyoqlarni kengaytirib yotkazing.\n"
                      "2)Boshingizni boshqalar bilan bir xil sathda tutsangiz va qoraqamishlarni qo'llab-quvvatlang.\n"
                      "3)Mashqni boshlash uchun bir oyoqingizni o'rga olib, boshlang'ich holatdagi joyingizdan oyoqlaringizni yuqoriga qo'taring,\n aralashish vaqtida o'ng oyoqingizni yuqoriga ko'taring.\n"
                      "4)Endi o'ng oyoqingizni pastga tushiring va chap oyoqingizni yuqoriga ko'taring.\n"
                      "5)Yuqori ko'ynaklar harakatini tekrarlangan marta amalga oshiring, oyoqlar niqobini yuqoriga ko'tirmoqda davom eting.\n"
                      "6)Oyoqlaringizni tez va qonli harakat bilan o'ynating, jismoniy harakat vaqtida oyoqlaringizni o'rga-qaytga qarab\n almashtirishga harakat qiling.\n"
    },

    {
        "name": "Devor o'tiradi",
        "gif": "Gif Files/Wall sit.gif",
        "description":"1)Boshlang'ich holatda, bir duvonga yoki o'tirilgan stulga yoki stulga qaraganda oyoqlaringizni yuqoriga ko'taring.\n"
                      "2)Boshingizni yuqoriga ko'taring, qoraqamishlarni qo'llab-quvvatlang.\n"
                      "3)Oyoqlaringizni qo'l bilan yordam berib, duvoqa yoki stulga qarab o'tiring. Oyoqlaringizning yerga qadar bo'lishiga e'tibor bering.\n"
                      "4)Oyoq muskullarini ishlatib, oyoqlaringiz bilan yerga yuklaning va oyoqlaringiz 90 darajada bo'lishi kerak.\n"
                      "5)Duvolda o'tirishni o'zgartirish uchun belingizni to'g'ri tuting, boshingiz boshqalarga qaraganda bir xil sathda bo'lishi kerak.\n"
                      "6)Mashqdagi holatingizni to'g'ri saqlang va bir necha soniya davomida o'tiring.\n"
                      "7)Mashqni tekrarlangan marta amalga oshiring.\n"                                                      
    },

    {
        "name": "Tricep cho`kishlari",
        "gif": "Gif Files/Tricep Dips.jpg",
        "description": "Triceps dipslarni quyidagi tartibda bajaring:\n"
                       "1)Boshlang'ich holatda, oyoqlaringizni yerga qo'yib, bir stul yoki platforma orqali oyoqqa yuklangan holatda turib,\n qo'llaringizni stul yoki platforma qarab joylashtiring.\n"
                       "2)Qo'llaringizni oyoqlaringizning yoqimli qismiga olib, tuting va qoraqamishlarni qo'llab-quvvatlang.\n"
                       "3)Boshlang'ich holatdagi joyingizdan aralash, qo'llaringizni orqaga olib, oyoqlaringizni ohozda yuqoriga qo'taring.\n"
                       "4)Oyoqlar bilan yerdan yuklaning, oyoqlaringiz 90 darajada bo'lishi kerak. Qo'llaringiz asosiy kuchli bo'lishi kerak.\n"
                       "5)Qo'llaringizni boshlang'ich holatga qaytaring, belingizni to'g'ri tuting.\n"
                       "6)Triceps dipslarni tekrarlangan marta amalga oshiring.\n"
    },

    {
        "name": "Yon planochka",
        "gif": "Gif Files/Side plank.gif",
        "description": "1)Boshlang'ich holatda, yerda yotib, o'ng tomoningizga qarayotgan holatga kelib oling.\n"
                       "2)O'ng qo'lingizni yerga qo'yib, oyoqingizni yerga qo'yib, o'ng tomoningizga asosiy e'tibor berib,\n o'ng belingizni yerga qo'yib olib, o'ng qo'lingiz va o'ng oyoqingiz orqali o'tirib chiqing.\n"
                       "3)Qoraqamishlaringizni qo'llab-quvvatlang, qo'llaringiz oyoqingiz bilan birlashtirilgan bo'lsin.\n"
                       "4)Yoningizning boshqa tomoniga o'tib kelganida,yon planochkani to'g'ri saqlang.\n"
                       "5)Holatingizni boshqa tomoningizga o'tkazib borish uchun yon planochkani yakuniy holatga kelib turing.\n"
                       "6)Mashqni to'g'ri bajarmoq uchun holatingizni to'g'ri saqlang va\n bir necha soniya davomida turib turing.\n"
                       "7)Mashqni boshqa tomon bilan ham bajaring.\n"                                                       
    },
    
    {
        "name": "O'lik yuklarni ko'tarish",
        "gif": "Gif Files/Deadlifts.gif",
        "description":"1)Oyoqlaringizni elkangiz kengligida ajratib turing va oldingizda polga shtanga qo'ying.\n"
                      "2)Orqangizni tekis va ko'kragini ko'targan holda tizzalaringizni buking va sonlaringizga menteşe qiling.\n Pastga qo'lingizni cho'zing va shtangani yuqori tutqich bilan ushlang, qo'llar elkangiz kengligidan bir oz kengroq.\n"
                      "3)Shtangani poldan ko'tarishni boshlaganingizda, o'zingizning yadroingizni bog'lang va orqangizni tekis tuting.\n To'pig'ingizdan haydab, tizzalaringizni va kestirib, bir vaqtning o'zida oldinga siljiting.\n"
                                                                                                                                       
                                                                               
                                                                              

    },

    {
        "name": "Yelka bosish",
        "gif": "Gif Files/Shoulder press.gif",
        "description": "1)Boshlang'ich holatda, qarangani yo'qotib, boshingizni to'g'ri turib tuting.\n"
                       "2)Qo'l oyoqlarini yanaqo'rg'ani orqasida joylashtiring va oyoqlaringizni qarangandan bir qadam uzoqda joylashtiring.\n"
                       "3)Burchakni oyoqlaringizdan to'g'rilab turib tuting va oyoqlaringizni paxtali joyda joylashtiring.\n"
                       "4)Qo'l oyoqlarini qo'yinga yoying va qo'llaringizni pastga qarab joylashtiring. Bu sizning asosiy boshlang'ich holatingiz bo'ladi.\n"
                       "5)Qo'llaringizni g'alati tomonga qaytaring va qo'llaringizni bog'langan yoki oyoqqa paralel joylashtiring.\n"
                       "6)Qo'llaringizni orqa yo'ldoshiga olib, qo'llaringizni tepaga ko'taring, boshlang'ich holatingizga qaytib turing.\n"
                       "7)Qo'llaringizni yuqoriga ko'tarib, oyoqlaringizni yumshoq joyda saqlab turib tuting.\n"
                       "8)Qo'llaringizni yana pastga qaytaring va boshlang'ich holatingizga qaytib turing.\n"
                       "9)Harakatni to'g'ra kelishga qadar takrorlang va qo'llaringizni bir xil tartibda o'zgartirib turib turing.\n"                                         
    },

    {
        "name": "Bitseps bo`sish",
        "gif": "Gif Files/Bicep Curls.gif",
        "description": "1)Boshlang'ich holatda, qarangani yo'qotib, boshingizni to'g'ri turib tuting.\n"
                       "2)Qo'l oyoqlarini yanaqo'rg'ani orqasida joylashtiring va oyoqlaringizni qarangandan bir qadam uzoqda joylashtiring.\n"
                       "3)Burchakni oyoqlaringizdan to'g'rilab turib tuting va oyoqlaringizni paxtali joyda joylashtiring.\n"
                       "4)Qo'llaringizni burchakni orqa yo'ldoshiga olib, qo'llaringizni pastga qarab joylashtiring.\n Bu sizning asosiy boshlang'ich holatingiz bo'ladi.\n"
                       "5)Qo'llaringizni pastga yo'qotib, avvalo qo'llaringizni burchakni orqa yo'ldoshiga qaytaring va so'ng qo'llaringizni yuqoriga ko'taring.\n Bunday qilib, qo'llaringizni biseps muskullarini jismoniy yorqinlik bilan boshqarib turishingiz kerak.\n"
                       "6)Qo'llaringizni yuqoriga ko'tarib, oyoqlaringizni yumshoq joyda saqlab turib tuting.\n"
                       "7)Qo'llaringizni yana pastga qaytaring va boshlang'ich holatingizga qaytib turing.\n"
                       
    },

    {
        "name": "oyoqni bosish",
        "gif": "Gif Files/Leg Press.gif",
        "description": "1)Boshlang'ich holatda, yugurish yo'lakchasi orqasida yotib, oyoqlaringizni mashinaning yuqori platformasiga qo'ying.\n"
                       "2)Burchakni to'g'ridan-to'g'ri oyoqlaringizdan uzoqroq tuting va quyidagi pozani qabul qiling:\n"
                       "- Oyoqlaringizni bir necha daraja tekislang.\n"
                       "- Burchakni to'g'ridan-to'g'ri oyoqlaringizdan uzoqroq tuting.\n"
                       "3)Qo'llaringizni oyoqlaringizga yoki oyoqlariga qo'ying va qo'llaringizni mashinaning ruliga yoki qo'l dayamalariga qo'ying.\n Bu sizning asosiy boshlang'ich pozitsiyangiz bo'ladi.\n"
                       "4)Oyog'ingizdan to'g'ridan-to'g'ri burchakni saqlab, oyoqlaringizni yuqoriga ko'taring.\n"
                       "5)Oyoqlaringizni pastga tushirgan holda, boshqariladigan mashinaning platformasini pastga ko'tarib ushlab turing.\n Bu yukning pastki chegarasiga yetishiga olib kelishi kerak.\n"
                      
    },

    {
        "name": "Glute ko`priklari",
        "gif": "Gif Files/Glute Bridges.gif",
        "description": "1)Boshlang'ich holatda yotib, oyoqlaringizni barmoq bilan yumshoq joyda o`rnating.\n"
                       "2)Qo`llaringizni yonlamoqda yotib, qo`llaringizni yon tomonga joylashtiring\n va qo`llaringizni yotish yeridan qanchalik uzoqda joylashtirishingizni tanlang.\n"
                       "3)Nafas olishda, oyoqlaringizni yuqoriga ko`tarib turib, eralaringizni yuqoriga qaldiring.\n Bu sizning boshlang'ich holatingiz bo'ladi.\n"
                       "4)Yuqoridan pastga qarab eralaringizni pastga olib tashlang,\n boshlang'ich holatingizga qaytib turib turing.\n"
                       "5)Harakatni to'g'ra kelishga qadar takrorlang\n va eralaringizni bir xil tartibda o'zgartirib turib turing.\n"
    },

    {
        "name": "Buzoq ko`tarilishi",
        "gif": "Gif Files/Culf Raises.jpg",
        "description": "1)Boshlang'ich holatda, oyoqlaringizni yanaqo'rg'ani orqasida joylashtiring va burchakni oyoqlaringizdan to'g'rilab turib tuting.\n Qo'llaringizni yonlamoqda yotib, qo'llaringizni yon tomonga joylashtiring yoki\n qo'llaringizni belingizga bog'langan joyida joylashtiring.\n"
                       "2)Nafas olishda, oyoqlaringizni yuqoriga ko'tarib turib,\n buqalaringizni pastga qo'taring.\n Bu sizning boshlang'ich holatingiz bo'ladi\n."
                       "3)Buqalaringizni yuqoriga ko'tarib, oyoqlaringizni to'g'ri saqlab turib tuting\n."
                       "4)Yuqoridan pastga qarab, boshlang'ich holatingizga qaytib turib turing\n."
                       "5)Harakatni to'g'ra kelishga qadar takrorlang va buqalaringizni bir xil tartibda o'zgartirib turib turing\.n"
    },






]



class ExerciseDropDown(DropDown):
    pass

class ExerciseApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create a dropdown to select exercises
        dropdown = ExerciseDropDown()
        for exercise in exercises:
            button = Button(text=exercise["name"], size_hint_y=None, height=44)
            button.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(button)
        
        select_button = Button(text="Mashqni tanlang", size_hint=(1, 0.1))
        select_button.bind(on_release=dropdown.open)

        layout.add_widget(select_button)

        # Create an Image widget to display the exercise GIF
        exercise_image = Image(source='', size_hint=(1, 0.6))
        layout.add_widget(exercise_image)

        # Create a Label widget to display the exercise description
        exercise_description = Label(text='', size_hint=(1, 0.3))
        layout.add_widget(exercise_description)

        # Function to handle exercise selection
        def select_exercise(instance, exercise_name):
            exercise = next((ex for ex in exercises if ex["name"] == exercise_name), None)
            if exercise:
                exercise_image.source = exercise["gif"]
                exercise_description.text = exercise["description"]

        dropdown.bind(on_select=select_exercise)

        return layout

if __name__ == '__main__':
    ExerciseApp().run()
