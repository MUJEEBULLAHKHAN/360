from django import forms
from django.forms import widgets
from .models import *

CHOICES=[('Yes/نعم','Yes/نعم'),
         ('No/لا','No/لا')]
class arcinfoForm(forms.ModelForm):
    company = forms.CharField(label='Company Name :/اسم الشركة')
    owner = forms.CharField(label='Owner Name/اسم المالك')
    contact = forms.CharField(label='Owner Contact :/رقم التواصل بالمالك')
    manager = forms.CharField(label='Manager Name :/اسم المدير')
    managercont = forms.CharField(label='Manager contacts /رقم التواصل بالمدير')
    estimate = forms.ChoiceField(choices=CHOICES,label='Computerized Estimating program :/هل يوجد برنامج تقدير محوسب', widget=forms.RadioSelect())
    
    class Meta:
        model = arcinfo
        fields = '__all__'

class arclocForm(forms.ModelForm):
    address = forms.CharField(label='address عنوان')
    class Meta:
        model = arcloc
        fields = '__all__'

class financialForm(forms.ModelForm):
    labor = forms.CharField(label='Labor Sales / Month /مبيعات اجور اليد / شهريا')
    part = forms.CharField(label='Parts Sales / Month /مبيعات قطع الغيار / شهريا')
    material = forms.CharField(label='Material Sales / Month /مبيعات المواد / شهريا')
    rent = forms.CharField(label='Rent /Month / الإيجار / شهريا')
    productive = forms.CharField(label='Staff Cost /Month Productive :/تكلفة العمالة / شهريا')
    support = forms.CharField(label='Staff Cost /Month Support:/ تكلفة الاداريين / شهريا')
    month = forms.CharField(label='Other Expenses / Month:/مصاريف أخرى / شهريا')
    class Meta:
        model = financial
        fields = '__all__'


class workforceinfoForm(forms.ModelForm):
    PPE = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Staff provided with PPE: /معدات الوقاية الشخصية ')
    denter = forms.CharField(label='Number of Denters :/عدد السمكرية :')
    painter = forms.CharField(label='Number of Painters :/عدد الدهانيين :')
    elec = forms.CharField(label='Number of Mechanic/Elec :/عدد الميكانيكية - الكهربائية ')
    staff = forms.CharField(label='Number of Support staff:/عدد موظفي الادارة')
    workbays = forms.CharField(label='Number of workbays :/عدد اماكن العمل داخل الورشة - الطاقة الاستيعابية للورشة:')
    body = forms.CharField(label='Number of Jobs / Month Bodyshop only :/انتاجية الورشة في ما يخص السمكرة و الدهان - شهريا')
    nonbody = forms.CharField(label='Number of Jobs / Month Non bodyshop only :/ انتاجية الورشة اعمال غير السمكرة و الدهان - شهريا:')
    sqm = forms.CharField(label='Workshop Size Sqm :/ مساحة الورشة - متر مربع:')
    insurance = forms.CharField(label='WP - Insurance % :/% نسبة العمل مع شركات التأمين')
    walkin = forms.CharField(label='WP - Walk-in % :/ % نسبة العمل مع العملاء الكاش - النقدي')
    fleet = forms.CharField(label='WP - Fleet % :/% شركات التي تمتلك اساطيل- شركات تاجير و وغيرها')
    park = forms.CharField(label='Number of Customer Parking :/ عدد مواقف السيارات للعملاء')
    recep = forms.CharField(label='Adequate Reception :/مكتب استقبال مناسب')
    wash = forms.CharField(label='Adequate Washroom - Customers:/ حمام مناسب - للعملاء')
    washstaff = forms.CharField(label='Adequate Washroom - Staff :/حمام مناسب - طاقم عمل')
    scrap = forms.CharField(label='Scrap storage :/منطقة تخزين الاسكراب')
    newpart = forms.CharField(label='New parts Storage :/منطقة تخزين قطع غيار جديدة')
    oilstorage = forms.CharField(label='Used Oil Storage :/منطقة تخزين الزيوت المستعملة')
    class Meta:
        model = workforceinfo
        fields = '__all__'


class repairinfoForm(forms.ModelForm):
    measure = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Estimates with 3D Measurement :/ نظام قياس ثلاثي الابعاد :')
    nonstruct = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Body repair - Non Structural Repairs :/ إصلاح الجسم - الإصلاحات غير الهيكلية ')
    struct = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Body repair - Structural Repairs :/ إصلاح الجسم - الإصلاحات الهيكلية :')
    paint = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Refinishing - Paint - Full :/ خدمات الدهان كاملة:')
    ac = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='General Electric Service / AC :/: خدمات الكهرباء و التكيف')
    body = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Aluminum Body Repair :/ إصلاح الألومنيوم :')
    qc = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='QC Report with 3D measurement :/: تقرير مراقبة الجودة مع قياسات ثلاثية الابعاد')
    brakes = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='General Repairs - Brakes/Suspension :/ الإصلاحات العامة - الفرامل / نظام التعليق :')
    tyre = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Tire Service :/خدمة الإطارات ')
    wheel = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Wheel Alignment :/وزن الاذرعة :')
    computer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Computer Diagnostic / Calibration/Repairs:/التشخيص / المعايرة الحاسوبية :')
    adas = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='ADAS (Advance Driver Assistance System) :/ اصلاح نظام الامان و مساعدة السائق :')
    engine = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Engine / Drive train Overhaul :/إصلاح المحرك / لرفع المحرك و نقله :')
    plastic = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Plastic Parts Repair :/إصلاح الأجزاء البلاستيكية :')
    welder = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Plastic Repair Tools- Hot Stapler, Hot Air Welder, Plastic Brazing:/أدوات إصلاح البلاستيك - دباسة ساخنة ، آلة لحام بالهواء الساخن ، لحام بلاستيك :')
    class Meta:
        model = repairinfo
        fields = '__all__'

class equipinfoForm(forms.ModelForm):
    it = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="IT system for Managing Workshop :/نظام حاسوبي لإدارة الورشة ")
    comp = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Computerized Estimation system :/نظام تقدير حاسوبي")
    access = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to vehicle measurement DATA sheet :/هل يوجد صلاحية للدخول لمعلومات قياسات السيارات من الشركات العالمية (شاصيه)")
    oem = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to OEM Repair Manuals (OEM) :/ الوصول إلى كتيبات إصلاح OEM")
    guide = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to OEM Labor time Guide (OEM) :/الوصول إلى دليل وقت عمل OEM")
    lift = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Two Post Lifts :/ رافعة بعامودين")
    frame = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Frame / Unibody structure alignment system :/ نظام اصلاح الشاصي")
    four = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="FOUR point anchoring system - Unibody :/ نظام إرساء ذو أربع نقاط- قطعة واحدة")
    anchor = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="FOUR point anchoring system - Frame :/نظام إرساء ذو أربع نقاط / إطار")
    ton = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="10 ton Pulling system :/ نظام سحب 10 طن")
    oxy = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Oxy/Acetylene Welding Equipment :/معدات لحام الأكسجين / الأسيتيلين")
    resistance = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Resistance / Spot Welding Equipment :/معدات لحام بتقنيةمقاومة المغنطه")
    heater = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Induction Heater :/ سخان الحث")
    plasma = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Plasma cutter :/ قاطعه بتقنية البلازما")
    mig = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="MIG welder Steel :/ لحام مخصص للفولاذ")
    dent = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Dent Puller - Steel :/ دنت بولير - فولاذ")
    air = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Air compressor :/ ضاغط الهواء")
    chain = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Chain Block / Port-A-Power:/سلسلة السحب")
    charging = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="AC Charging / Recovery Equipment :/ معدات شحن الفريون/ استعادة التيار المتردد")
    kit = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Denter Tools KIT :/ مجموعة أدوات السمكرة")
    dry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Dry Sanding Equipment :/ معدات الصنفرة الجافة")
    hvlp = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="HVLP Spray Guns :/مسدسات الرش HVLP")
    vet = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wet/Dry Vacuum Machines :/ ماكينات تنظيف جاف / رطب")
    booth = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Paint Booth :/ فرن لرش السيارات")
    prep = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Prep Station :/محطة تجهييز المركبة")
    mixing = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Paint Mixing Room fully equipped :/ غرفة خلط الدهان مجهزة بالكامل")
    tools = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Painter Tools Kit :/ طقم أدوات الرش")
    toolkit = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Electrician Tool Kit :/ طقم أدوات كهربائية")
    lifts = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Four Post Lifts - for Wheel Alignment :/ رافعات عامودية - لوزن الاذرعة")
    align = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wheel Aligning Equipment :/ جهاز وزن الاذرعه")
    rise = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Low Rise Lift :/ رافعة منخفضة الارتفاع")
    changer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Tire Changer :/ مغير الاطارات")
    balancer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wheel Balancer :/ ترصيص الكفرات")
    lathe = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Brake Lathe :/ مخرطة الفرامل")
    notes = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Notes : Recommendation for Betterment in tools/service etc. /.ملاحظات : توصية لتحسين الأدوات/ الخدمات وما إلى ذلك")
    ch = forms.MultipleChoiceField(choices=[('reading', 'Reading'),('sports', 'Sports'),('music', 'Music'),('travel', 'Travel'),], widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = equipinfo
        fields = '__all__'
        

ch1=[('N/A - لايوجد', 'N/A - لايوجد'),('4star/اربع نجوم', '4star/اربع نجوم'),]
ch2=[('star/نجمة', 'star/نجمة'),('2star/نجمتين', '2star/نجمتين'),('3star/ثلاث نجوم', '3star/ثلاث نجوم'),('4star/اربع نجوم', '4star/اربع نجوم'),]
ch3=[('N/A - لايوجد', 'N/A - لايوجد'),('3star/ثلاث نجوم', '3star/ثلاث نجوم'),('4star/اربع نجوم', '4star/اربع نجوم'),]

class estabForm(forms.ModelForm):
    lice = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='Obtain all required governmental licenses./الحصول على جميع التراخيص الحكومية اللازمة.')
    saso = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='Apply the standard SASO-1334, related to safety requirements for maintenance and repair workshops./تطبيق المواصفة القياسية رقم 1334-SASO الخاصة بإشتراطات السلامة في ورش الصيانة والاصلاح ')
    undertake = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='Undertake to comply with the list of technical requirements (Annex 5)./التعهد بالالتزام بقائمة المتطلبات الفنية (ملحق)')
    access = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Accessibility to the establishment from the main road./سهولة الوصول للمنشأة من الطريق الرئيسي .')
    subroad = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Accessibility to the establishment from a sub-road./سهولة الوصول للمنشأة من الطريق الفرعي.')
    exits = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Separate entrance and exit./مدخل ومخرج منفصلين للمنشأة.')
    plate = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='Nameplate of the establishment with a harmonious design./لوحة باسم المنشأة مضاءة وبتصميم متناسق.')
    harmo = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Harmonious facade clear of any defects./واجهة متناسقة وخالية من العيوب.')
    light = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='availability of suitable light around the establishment./توفر إضاءة مناسبة حول المنشأة.')
    area = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Private and shaded parking areas./مواقف خاصة ومظللة .')
    place = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='place the classification certificate at the entrance./تثبيت شهادة التصنيف حسب التعليمات عند المدخل.')
    ramps = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide ramps for services of persons with disabilities (according to comprehensive access guide instructions./توفير منحدرات لخدمة الأشخاص ذوي الإعاقة (حسب تعليمات دليل الوصول الشامل).')
    class Meta:
        model = estabinfo
        fields = '__all__'

class recepForm(forms.ModelForm):
    r1 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='computerized system to manage data, customers, vehicles, repair, operations and spare parts/ نظام حاسوبي لإدارة المنشأة يحتوي على بيانات : العملاء والمركبات وعملية الإصلاح والقطع المستبدلة')
    r2 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a quality control system./توفير نظام لإدارة الجودة')
    r3 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a reception area separate from the workshop provided with new suitable furniture./وجود منطقة استقبال مفصولة عن الورشة مزوَّدة بأثاث جيد ومتناسق ، مع خلو الجدران والاسقف والأرضيات من العيوب .')
    r5 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide waiting areas for women only/وجود منطقة مخصصة لانتظار النساء')
    r7 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a hot/cool conditioning system./وجود نظام تكييف حار/بارد.')
    r8 = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Place all operation licenses and classification certificates clearly and according to instructions/ تثبيت جميع رخص التشغيل وشهادة التصنيف بشكل واضح وحسب التعليمات .')
    r10 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Place the guarantee policy clearly/ تثبيت سياسة الضمان بشكل واضح.')
    r12 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Place the communication number for complaints/ تثبيت رقم للتواصل عند وجود شكوى.')
    r14 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide special offices for receiving and delivering vehicles/ وجود مكاتب خاصة باستلام المركبات وأخرى خاصة بالتسليم.')
    r16 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Reception area should be in a good condition/ أن تكون مكاتب الاستقبال بحالة جيدة ومتناسقة.')
    r18 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a suitable number of seats in a good condition for waiting customers/وجود مقاعد متناسقة لانتظار العملاء بعدد كافٍ وبحالة جيدة.')
    r20 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide means of hospitality for customers/توفير ضيافة للعملاء.')
    r21 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide suitable means of entertainment/توفير وسائل مناسبة للتسلية.')
    class Meta:
        model = recepinfo
        fields = '__all__'
        
class empForm(forms.ModelForm):
    EPPE = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='All employees wearing PPE/ ارتداء العاملين أدوات السلامة الشخصية.')
    all = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='All employees wearing a uniform/ارتداء العاملين زي رسمي موحد.')
    use = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Use of personal identification cards/ تعليق البطاقات التعريفية.')
    speak = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide at least one person who speaks Arabic and English/توفير شخص على الأقل يجيد اللغة العربية والإنجليزية')
    aid = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Provide persons trained on first aid and implementing firefighting plan/ توفير أشخاص مدربين على الإسعافات الأولية وتنفيذ خطة مكافحة الحريق .')
    one = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='One engineer at least holding specialized engineering qualifications/وجود مهندس واحد – على الأقل - مختص حاصل على مؤهل هندسي.')
    highly = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide highly qualified maintenance technicians/وجود فنيي صيانة حاصلون على مؤهل علمي.')
    proof = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide an annual plan for training and developing employees and provide a proof with that effect/توفير خطة سنوية لتدريب العاملين وتطويرهم وتقديم ما يثبت ذلك')
    job = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Document employees’ names, along with job descriptions stating the job tasks and required competencies/توثيق أسماء العاملين مع وصف وظيفي يُبين المهام الوظيفية والكفاءة اللازمة .')
    repair = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a record for employees to identify repair operations/وجود سجل للعاملين يوضح عمليات الإصلاح التي قاموا بها')
    class Meta:
        model = empinfo
        fields = '__all__'

class servicesForm(forms.ModelForm):
    website = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a website describing the establishment’s location, working hours and contact numbers/توفير موقع إليكتروني يوضح موقع المنشأة وساعات العمل وأرقام التواصل .')
    telephone = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a telephone system for easy communication with various departments/توفيير نظام هاتفي (سنترال) يُسهل الاتصال بمختلف أقسام المنشأة .')
    appointment = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide appointment reservation service/توفير خدمة حجز المواعيد.')
    record = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a record of complaints and taken actions/وجود سجل للشكاوى والإجراءات المتخذة بشأنها.')
    system = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='Provide a system for measuring customers satisfaction/توفير نظام لقياس مدى رضا العملاء عن الخدمة المقدَّمة')
    shall = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='Inspect vehicle record condition before being entered in the establishment Shall be documented with the customer/ فحص المركبة تسجيل حالتها باستخدام قائمة تدقيق قبل دخولها للمنشأة، وتوثيق ذلك مع العميل')
    access = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Present to customer written report for performed repairs to clarify the replaced parts, financial costs, guarantee period /إعطاء العملاء تقرير عن عملية الإصلاح يوضح القطع المستبدلة وفترة الضمان وشروطة')
    cost = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Wash the vehicle after finishing the repair/غسيل المركبة بعد عملية الإصلاح.')
    wash = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide e-payment system approved by Saudi Central Bank (SAMA)/توفير وسائل الدفع الإلكتروني المعتمدة من البنك المركزي السعودي ساما -SAMA')
    sama = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide credit cards payment system/توفير نظام دفع النقود باستخدام البطاقات الائتمانية.')
    credit = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a clear and environment friendly strategy for discharging of wastes and spare parts/ توفير سياسة واضحة للتخلص من النفايات وقطع الغيار المستبدلة بطريقة لا تضر بالبيئة ')
    class Meta:
        model = servicesinfo
        fields = '__all__'

class facilitiesForm(forms.ModelForm):
    parka1 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide parking areas for vehicles before or after repair process that shall be shaded and fenced/ مواقف ضمن حدود المنشأة لصف المركبات قبل أو بعد عملية الاصلاح ، على أن تكون مضللة ومسورة ')
    female = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Two clean and in good condition toilets for customers; one for male and the other for females/ دورتي مياه نظيفة وبحالة جيدة، على أن تكون مخصَّصة للعملاء، إحداهما مخصصة للرجال والأخرى للنساء ')
    mosq = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a special area for praying in case there is no near mosque/توفير مساحة خاصة للصلاة عند عدم وجود مسجد قريب.')
    risk = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Provide all equipment in a sound condition, clear of any defects that might represent a risk to its users/جميع الأجهزة بحالة سليمة وخالية من العيوب التي قد تشكل خطرا على مستخدميها.')
    class Meta:
        model = facilitiesinfo
        fields = '__all__'

class deviceForm(forms.ModelForm):
    calibrate = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Calibrate all equipment regularly by a third party/معايرة الأجهزة دورياً عن طريق طرف ثالث .')
    inspect = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Inspect the equipment regularly by the establishment/فحص الأجهزة دورياً من قبل المنشأة ')
    provide = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide the minimum devices and equipment required to perform repair procedures /توفير الحد الأدنى من الأجهزة والمعدات للقيام بعملية الإصلاح')
    class Meta:
        model = deviceinfo
        fields = '__all__'


# scores
Choice1=[('Inaccessible/لا يسهل الوصول إليه','Inaccessible/لا يسهل الوصول إليه'),('Accessible from a sub-road./يسهل الوصول إليه من الطريق الجانبي','Accessible from a sub-road./يسهل الوصول إليه من الطريق الجانبي'),('Accessible from main road./يسهل الوصول إليه من الطريق الرئيسي.','Accessible from main road./يسهل الوصول إليه من الطريق الرئيسي.')]
Choice2=[('One entrance and exit for repair area./مدخل واحد للدخول ومخرج لمنطقة الإصلاح','One entrance and exit for repair area./مدخل واحد للدخول ومخرج لمنطقة الإصلاح'),('Separate entrance and exit with clear direction signs./مدخل ومخرج منفصلين، ومجمع منفصل مع وجود علامات توجيه واضحة ','Separate entrance and exit with clear direction signs./مدخل ومخرج منفصلين، ومجمع منفصل مع وجود علامات توجيه واضحة ')]
Choice3=[('Parking in front of the establishment on the main road/الوقوف أمام المنشأة على الشارع العام','Parking in front of the establishment on the main road/الوقوف أمام المنشأة على الشارع العام'),('Public parking area in front of the establishment, for at least 3 vehicles./ساحة مواقف عامة أمام المنشأة بوقوف 3 مركبات على الأقل','Public parking area in front of the establishment, for at least 3 vehicles./ساحة مواقف عامة أمام المنشأة بوقوف 3 مركبات على الأقل'),('Five Vehicles Atleast/ بوقوف 5 مركبات على الأقل','Five Vehicles Atleast/ بوقوف 5 مركبات على الأقل')]
Choice4=[('No separate storage facility./عدم وجود مرفق تخزين منفصل','No separate storage facility./عدم وجود مرفق تخزين منفصل'),('Separate storage facility without ventilation./مكان تخزين منفصل بدون تهوية .','Separate storage facility without ventilation./مكان تخزين منفصل بدون تهوية .'),('Separate storage facility for various types and sizes with controllable environmnet and separate storage for material with labels','Separate storage facility for various types and sizes with controllable environmnet and separate storage for material with labels')]
Choice5=[('2 manual hydraulic cranes and mechanic cranes./عدد 2 رافعة هيدروليكية يدوية ورافعات ميكانيكية','2 manual hydraulic cranes and mechanic cranes./عدد 2 رافعة هيدروليكية يدوية ورافعات ميكانيكية'),('At least one manual hydraulic crane and axis platforms/ على الأقل رافعة واحدة ورافعات هيدروليكية يدوية ومنصات المحور','At least one manual hydraulic crane and axis platforms/ على الأقل رافعة واحدة ورافعات هيدروليكية يدوية ومنصات المحور'),('Two cranes at least/على الأقل رافعتين','Two cranes at least/على الأقل رافعتين')]
Choice6=[('Waiting area only/غرفة انتظار فقط','Waiting area only/غرفة انتظار فقط'),('Air-conditioned waiting area./توجد غرفة انتظار مكيفة','Air-conditioned waiting area./توجد غرفة انتظار مكيفة'),('Air-conditioned waiting area provided with beverages, magazines...etc./نعم، مزودة بمكيف هواء ويتوفر بها أحدث المجلات والمرطبات ..إلخ.','Air-conditioned waiting area provided with beverages, magazines...etc./نعم، مزودة بمكيف هواء ويتوفر بها أحدث المجلات والمرطبات ..إلخ.')]
Choice7=[('Toilets for employees only./ حمامات للعاملين فقط','Toilets for employees only./ حمامات للعاملين فقط'),('Toilets for employees and customers./حمامات للعملاء والعاملين','Toilets for employees and customers./حمامات للعملاء والعاملين'),('At least One separate toilet for customers in clean and good condition, with washroom./يوجد على الأقل حمام واحد منفصل للعملاء بحالة نظيفة مع غرفة غسيل.','At least One separate toilet for customers in clean and good condition, with washroom./يوجد على الأقل حمام واحد منفصل للعملاء بحالة نظيفة مع غرفة غسيل.')]
Choice8=[('Alternative vehicles or transportation service or tickets./مركبات بديلة أو خدمة النقل أو تذاكر مواصلات','Alternative vehicles or transportation service or tickets./مركبات بديلة أو خدمة النقل أو تذاكر مواصلات')]
Choice9=[('Contact numbers for workshop./للورشة أرقام تواصل فقط.','Contact numbers for workshop./للورشة أرقام تواصل فقط.'),('Website for the workshop including working hours, location map and contact numbers./للورشة موقع إلكتروني يبين أوقات العمل و خريطة الموقع وأرقام التواصل.','Website for the workshop including working hours, location map and contact numbers./للورشة موقع إلكتروني يبين أوقات العمل و خريطة الموقع وأرقام التواصل.'),('The workshop has Communication system, central appointment system and website, including the working hours, location map and contact numbers./للورشة نظام اتصال وحجز مواعيد مركزي وموقع إلكتروني يُبين أوقات العمل وخريطة الموقع وأ رقام التواصل','The workshop has Communication system, central appointment system and website, including the working hours, location map and contact numbers./للورشة نظام اتصال وحجز مواعيد مركزي وموقع إلكتروني يُبين أوقات العمل وخريطة الموقع وأ رقام التواصل')]


choi1=[('Gloves only/قفازات فقط','Gloves only/قفازات فقط'),('Uniform and gloves/زي موحد وقفازات','Uniform and gloves/زي موحد وقفازات'),('Provide all PPE such as uniform, gloves, goggles, safety boots and helmets./تم توفير جميع معدات الحماية الشخصية مثل الزي الموحد والقفازات ونظارات السلامة وأحذية السلامة وقبعات الرأس.','Provide all PPE such as uniform, gloves, goggles, safety boots and helmets./تم توفير جميع معدات الحماية الشخصية مثل الزي الموحد والقفازات ونظارات السلامة وأحذية السلامة وقبعات الرأس.')]
choi2=[('Medicines, bandages, cotton, sterilizers, and other means of quick relief available in a box with a trained first aider./نعم، الأدوية والضمادات والقطن والمعقمات ووسائل المعالجة السريعة الأخرى متوفرة في صندوق ويوجد مسعف إسعافات أولية مدرب.','Medicines, bandages, cotton, sterilizers, and other means of quick relief available in a box with a trained first aider./نعم، الأدوية والضمادات والقطن والمعقمات ووسائل المعالجة السريعة الأخرى متوفرة في صندوق ويوجد مسعف إسعافات أولية مدرب.'),('Medicines, such as bandages, cotton, sterilizers, and other means of quick relief available in a box./نعم، الأدوية مثل الضمادات والقطن والمعقمات ووسائل المعالجة السريعة الأخرى متوفرة في صندوق','Medicines, such as bandages, cotton, sterilizers, and other means of quick relief available in a box./نعم، الأدوية مثل الضمادات والقطن والمعقمات ووسائل المعالجة السريعة الأخرى متوفرة في صندوق')]
choi3=[('Only fans with emergency exit./مراوح فقط مع مخرج طوارئ.','Only fans with emergency exit./مراوح فقط مع مخرج طوارئ.'),('Fans with emergency exit, assembly area, map for fire extinguishers, fire alarms, emergency exit and assembly points./مراوح مع مخرج طوارئ ومنطقة تجمع، خارطة تعريفية للموقع توضح مكان طفايات الحريق ومنبهات إنذار الحريق ومخرج الطوارئ ونقطة التجمع.','Fans with emergency exit, assembly area, map for fire extinguishers, fire alarms, emergency exit and assembly points./مراوح مع مخرج طوارئ ومنطقة تجمع، خارطة تعريفية للموقع توضح مكان طفايات الحريق ومنبهات إنذار الحريق ومخرج الطوارئ ونقطة التجمع.'),('Open Lines with hot/cold ventilation, emergency exit, assembly area, id map for fire extinguisher','Open Lines with hot/cold ventilation, emergency exit, assembly area, id map for fire extinguisher')]
choi4=[('No Suitable lifting equipment, manual lifting heavy material','No Suitable lifting equipment, manual lifting heavy material'),('manual handling equipment available','manual handling equipment available'),('tires holder and cylinder crane available','tires holder and cylinder crane available')]
choi5=[('system complying to civil defence, in addition to system for draining waste','system complying to civil defence, in addition to system for draining waste')]


choii1=[('Use reference tools for internal calibration with records./استخدام أدوات مرجعية للمعايرة داخلياً مع سجلات .','Use reference tools for internal calibration with records./استخدام أدوات مرجعية للمعايرة داخلياً مع سجلات .'),('Calibrate testing and measuring tools through an independent calibration lab regularly with all records. /أدوات القياس والاختبار معايرة من قبل مختبر معايرة مستقل دوريا مع جميع السجلات.','Calibrate testing and measuring tools through an independent calibration lab regularly with all records. /أدوات القياس والاختبار معايرة من قبل مختبر معايرة مستقل دوريا مع جميع السجلات.')]
choii2=[('Inspection and maintenance works are performed without a plan or records/يتم القيام بالفحص والصيانة من دون أي خطة أو سجل.','Inspection and maintenance works are performed without a plan or records/يتم القيام بالفحص والصيانة من دون أي خطة أو سجل.'),('Inspection and maintenance works are performed without a plan, while results of all inspections and services are recorded./يتم القيام بالفحص والصيانة من دون أي خطة. يتم تسجيل نتائج جميع الفحوصات والخدمة الصيانة.','Inspection and maintenance works are performed without a plan, while results of all inspections and services are recorded./يتم القيام بالفحص والصيانة من دون أي خطة. يتم تسجيل نتائج جميع الفحوصات والخدمة الصيانة.'),('Daily Inspection, inspecting based on annual plan, results must be recorded','Daily Inspection, inspecting based on annual plan, results must be recorded')]
choii3=[('A device to test emissions (oil and diesel) ready for utilization./جهاز اختبار الانبعاثات (بنزين وديزل) جاهز للاستخدام.','A device to test emissions (oil and diesel) ready for utilization./جهاز اختبار الانبعاثات (بنزين وديزل) جاهز للاستخدام.')]
choii4=[('Use a trolley to carry the heavy materials./استخدام عربة (ترولي) لحمل المكونات الثقيلة .','Use a trolley to carry the heavy materials./استخدام عربة (ترولي) لحمل المكونات الثقيلة .'),('There shall be suitable cranes for lifting the heavy materials./هناك رافعات مناسبة لرفع المكونات الثقيلة','There shall be suitable cranes for lifting the heavy materials./هناك رافعات مناسبة لرفع المكونات الثقيلة')]
choii5=[('At least manual hydraulic cranes and axis poles./على الأقل. رافعات هيدروليكية يدوية. وأعمدة محور ,','At least manual hydraulic cranes and axis poles./على الأقل. رافعات هيدروليكية يدوية. وأعمدة محور ,'),('At least one 2.5-ton crane and manual hydraulic cranes./على الأقل رافعة واحدة بقدرة 2.5 طن على الأقل، ورافعات هيدروليكية يدوية وأعمدة محور.','At least one 2.5-ton crane and manual hydraulic cranes./على الأقل رافعة واحدة بقدرة 2.5 طن على الأقل، ورافعات هيدروليكية يدوية وأعمدة محور.'),('At least two 2.5-ton cranes./على الأقل رافعتان بقدرة 2.5 طن على الأقل.','At least two 2.5-ton cranes./على الأقل رافعتان بقدرة 2.5 طن على الأقل.')]
choii6=[('Battery charger ideal for recharging batteries 12/24 v/شاحن بطارية مثالي لإعادة شحن بطاريات 12/24 فولت .','Battery charger ideal for recharging batteries 12/24 v/شاحن بطارية مثالي لإعادة شحن بطاريات 12/24 فولت .')]


class ServicesForm(forms.ModelForm):
    loc = forms.MultipleChoiceField(choices=Choice1, widget=forms.CheckboxSelectMultiple,label='Location/الموقع')
    ent = forms.MultipleChoiceField(choices=Choice2, widget=forms.CheckboxSelectMultiple,label='Entrance/المداخل')
    par = forms.MultipleChoiceField(choices=Choice3, widget=forms.CheckboxSelectMultiple,label='Parking area/ساحة المو اقف')
    sto = forms.MultipleChoiceField(choices=Choice4, widget=forms.CheckboxSelectMultiple,label='Storage area/منطقة التخزين')
    mac = forms.MultipleChoiceField(choices=Choice5, widget=forms.CheckboxSelectMultiple,label='Machines / Cranes/الآليات/الرافعات')
    cus = forms.MultipleChoiceField(choices=Choice6, widget=forms.CheckboxSelectMultiple,label='Customers waiting area/غرفة انتظار العملاء')
    toi = forms.MultipleChoiceField(choices=Choice7, widget=forms.CheckboxSelectMultiple,label='Toilets/دورة المياه')
    cli = forms.MultipleChoiceField(choices=Choice8, widget=forms.CheckboxSelectMultiple,label='Client’s transportation/تنقل العميل')
    ser = forms.MultipleChoiceField(choices=Choice9, widget=forms.CheckboxSelectMultiple,label='Customer service/خدمة العملاء')
    
    class Meta:
        model = Services
        fields = '__all__'

class RequirementsForm(forms.ModelForm):
    p = forms.MultipleChoiceField(choices=choi1, widget=forms.CheckboxSelectMultiple,label='PPE/معدات الحماية الشخصية المتوفرة')
    first = forms.MultipleChoiceField(choices=choi2, widget=forms.CheckboxSelectMultiple,label='First aid kit/وسائل الإسعاف الأولية')
    wor = forms.MultipleChoiceField(choices=choi3, widget=forms.CheckboxSelectMultiple,label='Working environment/بيئة العمل')
    hand = forms.MultipleChoiceField(choices=choi4, widget=forms.CheckboxSelectMultiple,label='Handling with spare parts and equipment, availability of assistance to carry the heavy materials/التعامل مع الأجزاء والمعدات، توفر مساعدات الرفع لرفع الأشياء الثقيلة')
    hazr = forms.MultipleChoiceField(choices=choi5, widget=forms.CheckboxSelectMultiple,label='Hazardous goods and drainage system/البضاعة الخطرة ونظام التصريف')
    class Meta:
        model = Requirements
        fields = '__all__'

class documentationForm(forms.ModelForm):
    ch = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="A checklist is used to record the vehicle’s condition in writing with the customer./تستخدم قائمة تدقيق لتسجيل حالة المركبة كتابيا مع العميل")
    cu = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="The customer’s complaints shall be documented, and procedures shall be applied as required by the customer./يتم تسجيل شكاوى العميل ويُتخذ فيها الإجراء اللازم وفقا لحاجة العميل ")
    me = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Meeting for the employees once every three months to discuss the improvement procedures and clients’ needs./ اجتماع للموظفين مرة على الأقل كل ربع سنة تتم مناقشة إجراءات التحسين واحتياجات العميل")
    do = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="documented evaluation meeting to discuss the objectives and qualification procedures with each employee once per year./ تقييم موثقة لمناقشة الأهداف وإجراءات التأهيل مع كل موظف مرة واحدة في السنة.")
    emp = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="The employees and customers’ satisfaction shall be verified, and the suitable estimated measures shall be applied./يتم التحقق من رضا الموظفين والعملاء ويتم تطبيق التدابير المناسبة المقدرة")
    does = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="The workshop shall have a written guarantee policy clear for all employees and clients./للورشة سياسة ضمان مكتوبة، وهي واضحة للموظفين والعملاء.")
    work = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="The information of all customers and vehicles for all orders shall be registered./بيانات العملاء والمركبات لجميع الطلبات مسجلة")
    info = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Customers should approve repair or maintenance costs, spare parts and labors’ fees before starting work/ الاتفاق مع العميل على تكلفة الإصلاح أو الصيانة و قطع الغيار وأجرة اليد العاملة قبل البدء بالعمل")
    custom = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="The order shall be confirmed in writing by the client./يتم تأكيد الطلب كتابيا من قبل العميل.")
    order = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="technician assigned to perform repair and service orders with required documents according to time schedule./يتم تكليف فني الإصلاح بطلبات ا لإصلاح والخدمة مع الوثائق المطلوبة. يتم هذا وفقا لجدول زمني")
    tech = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Each order shall be finally verified by the person responsible for the workshop or service./يجرى التحقق النهائي لكل طلب من قبل الشخص المسؤول عن الورشة أو الخدمة")
    each = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="The invoice shall be complete, clear and understood by the customer./الفاتورة مكتملة وواضحة ومفهومة من قبل العميل.")
    invoice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="The workshop shall use an electronic management system./تستعمل الورشة نظام إدارة إلكتروني.")
    works = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Does the workshop hold any international certificates for its management system?/هل لدى الورشة أي شهادات دولية لنظام الإدارة الخاص بها؟")

    class Meta:
        model = documentation
        fields = '__all__'

class UtilizedForm(forms.ModelForm):
    ce = forms.CharField(label='Certificate for new spare parts or manufacturer’s certificate./شهادة قطع الغيار الجديدة أو شهادة مص نع.')
    cl = forms.CharField(label='Clear plan for all vehicles’ spare parts through the whole year./خطة واضحة لقطع الغيار لجميع المركبات خلال السنة.')
    th = forms.CharField(label='The workshop shall have a clear written guarantee policy./لدى الورشة سياسة ضمان مكتوبة واضحة.')
    sp = forms.CharField(label='The spare parts shall be stored according to manufacturer’s requirements./تخزين قطع الغيار وفقاً لمتطلبات المصنع ')
    sys = forms.CharField(label='System for handling old parts after being replaced./نظام للتعامل مع القطع القديمة بعد إحلالها')
    plan = forms.CharField(label='Time plan for delivering critical parts./لديه خطة زمنية لتسليم القطع الحرجة.')
    
    class Meta:
        model = Utilized
        fields = '__all__'

class TrainingForm(forms.ModelForm):
    t1 = forms.CharField(label='The employee’s responsibilities should be documented (job description including rules and responsibilities)./ينبغي توثيق مستوى المسؤولية المكلف بها الموظف (وصف الوظيفة متضمن القواعد والمسؤوليات).')
    t2 = forms.CharField(label='Evidence of competency./دليل الكفاءة')
    t3 = forms.CharField(label='A recognized qualification in the establishment’s field of activities (training, certificate ...etc.)/تأهيل معترف به في الأنشطة التي تقوم بها المنشأة (تدريب، شهادة، ... الخ)')
    t4 = forms.CharField(label='Initial training/التدريب الاولي')
    t5 = forms.CharField(label='Continuous training/استمرار التدريب')
    t6 = forms.CharField(label='Reception employee to communicate with customer./لديه موظف استقبال للتواصل مع العميل.')
    t7 = forms.CharField(label='Qualified technicians according to international qualification systems./فنيون مؤهلون وفقاً لأنظمة التأهيل العالمية')
    t8 = forms.CharField(label='Documented The employees’ training history./تاريخ التدريب موثق للموظفين')
    t9 = forms.CharField(label='Documented internal training courses in the list of participants./الدورات الداخلية موثقة بقائمة للمشاركين')

    class Meta:
        model = Training
        fields = '__all__'

class EquipmentForm(forms.ModelForm):
    eq1 = forms.MultipleChoiceField(choices=choii1, widget=forms.CheckboxSelectMultiple,label='Calibrating testing and measuring devices/معايرة أجهزة القياس والاختبار')
    eq2 = forms.MultipleChoiceField(choices=choii2, widget=forms.CheckboxSelectMultiple,label='Periodic maintenance/الصيانة الدورية')
    eq3 = forms.MultipleChoiceField(choices=choii3, widget=forms.CheckboxSelectMultiple,label='Emissions testing device/جهاز اختبار الانبعاثات')
    eq4 = forms.MultipleChoiceField(choices=choii4, widget=forms.CheckboxSelectMultiple,label='Tools to lift the heavy materials/أدوات لرفع المكونات الثقيلة')
    eq5 = forms.MultipleChoiceField(choices=choii5, widget=forms.CheckboxSelectMultiple,label='Equipment Capacity/قدرة المعدات')
    eq6 = forms.MultipleChoiceField(choices=choii6, widget=forms.CheckboxSelectMultiple,label='Battery charger/شاحن بطارية')
    class Meta:
        model = Equipment
        fields = '__all__'