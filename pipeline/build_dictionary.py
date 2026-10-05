import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pipeline.utils import save_json
from pipeline.expand_antigone_dict import ANTIGONE_FULL_DICT
from pipeline.expand_boite_dict import BOITE_FULL_DICT
from pipeline.expand_hugo_dict import HUGO_FULL_DICT

DICTIONARY_BOITE = {
    # Cultural & Moroccan terms
    "chouafa": {
        "type": "nom féminin",
        "fr_def": "Voyante ou sorcière traditionnelle marocaine qui pratique des rituels divinatoires.",
        "arabic": "العرّافة أو الشوافة، امرأة تدعي معرفة الغيب وتستحضر الأرواح في التقاليد الشعبية.",
        "darija": "الشوافة، مرا كتدعي السحر ولا قراءة الفال وكيديرو عندها الناس طقوس ديال الشعوذة.",
        "english": "traditional Moroccan clairvoyant or fortune-teller"
    },
    "msid": {
        "type": "nom masculin",
        "fr_def": "École coranique traditionnelle où les enfants apprennent à lire, écrire et mémoriser le Coran.",
        "arabic": "المسيد أو الكُتّاب القرآني التقليدي لتعليم الصغار القرآن ومبادئ القراءة والكتابة.",
        "darija": "المسيد ولا الجامع فين كيقراو الدراري الصغار القرآن والكتابة باللوح والصمغ.",
        "english": "traditional Quranic school"
    },
    "fqih": {
        "type": "nom masculin",
        "fr_def": "Maître d'école coranique ou savant religieux musulman.",
        "arabic": "الفقيه، معلم الكتاب أو رجل الدين المتمكن من علوم الفقه والشريعة.",
        "darija": "الفقيه، المعلم ديال المسيد لي كيحفظ الدراري القرآن وكيعاقبهم بالفلقة.",
        "english": "Quranic school teacher / Islamic scholar"
    },
    "haïk": {
        "type": "nom masculin",
        "fr_def": "Grand vêtement traditionnel féminin en étoffe blanche ou écrue dont les femmes se drapent pour sortir.",
        "arabic": "الحايك، لباس نسائي تقليدي ساتر من قماش أبيض أو كريمي يُلف حول كامل الجسم.",
        "darija": "الحايك، التوب الأبيض لي كانت كتلبسو المرة فالمغرب باش تغطي راسها وحوايجها فاش كتخرج للزنقة.",
        "english": "traditional Maghrebi woman's white veil/wrap"
    },
    "doum": {
        "type": "nom masculin",
        "fr_def": "Palmier nain méditerranéen dont les fibres végétales servent à tresser paniers et couffins.",
        "arabic": "الدوم، نبات النخيل القزم تُستعمل أليافه لصنع السلال والحبال التقليدية.",
        "darija": "الدوم، الورق ديال النخل القصير لي كيصاوبو منو القفاف والحصاير.",
        "english": "dwarf palm fibers (used for basketry)"
    },
    "driba": {
        "type": "nom féminin",
        "fr_def": "Ruelle ou venelle étroite en impasse dans une médina marocaine traditionnelle.",
        "arabic": "الدرّيبة، زقاق ضيق متفرع ومسدود في الأحياء العتيقة للمدينة القديمة.",
        "darija": "الدريبة، زنقة ضيقة مسدودة داخل درب من دروبة المدينة القديمة.",
        "english": "narrow alleyway / dead-end in old medina"
    },
    "chapelet": {
        "type": "nom masculin",
        "fr_def": "Objet de dévotion formé d'un cordon de grains que l'on égrène en récitant des prières (tasbih).",
        "arabic": "المسبحة أو السبحة، سلك منظوم بالخرز يُستعمل في التسبيح والذكر.",
        "darija": "التسبيح، السلسلة ديال العقيق لي كيذكرو وكيسبحو بها الله.",
        "english": "prayer beads / rosary"
    },
    "babouches": {
        "type": "nom féminin pluriel",
        "fr_def": "Chaussures traditionnelles en cuir sans talon et à bout plat ou pointu.",
        "arabic": "البَلْغة أو البلغة المغربية، حذاء جلدي تقليدي مسطح بدون كعب.",
        "darija": "البلغة، الحذاء الجلدي التقليدي المغربي لي كيلبسوه الرجال والعيالات.",
        "english": "traditional Moroccan leather slippers"
    },
    "caftan": {
        "type": "nom masculin",
        "fr_def": "Robe traditionnelle longue et ample, souvent richement brodée, portée lors des fêtes et cérémonies.",
        "arabic": "القفطان، ثوب تقليدي فضفاض ومطرز ترتديه النساء في المناسبات والأعياد.",
        "darija": "القفطان المغربي، اللبسة التقليدية الفاسية المخزنية المطروزة لي كتلبس فالأعراس والأعياد.",
        "english": "caftan / traditional embroidered robe"
    },
    "moussem": {
        "type": "nom masculin",
        "fr_def": "Fête religieuse et pèlerinage annuel en l'honneur d'un saint (marabout) au Maroc.",
        "arabic": "الموسم، احتفال ديني وتجاري سنوي يُقام حول ضريح ولي صالح.",
        "darija": "الموسم، الزارة ولا الاحتفال السنوي لي كيدار عند الولي الصالح وكيتجمعو فيه الناس.",
        "english": "Moroccan annual religious festival/pilgrimage"
    },
    "jenn": {
        "type": "nom masculin",
        "fr_def": "Créature surnaturelle invisible selon les croyances populaires et religieuses.",
        "arabic": "الجني، كائن غيبي خارق للطبيعة في المعتقدات الشعبية والإسلامية.",
        "darija": "الجني ولا الجوان، كائنات خفية كيعتاقدو الناس بلي كيسكنو الأماكن المظلمة والحمامات.",
        "english": "jinn / spirit"
    },
    "derb": {
        "type": "nom masculin",
        "fr_def": "Quartier ou ruelle principale reliant plusieurs impasses dans une médina marocaine.",
        "arabic": "الدرب، حي أو زقاق رئيسي في النسيج العمراني للمدينة العتيقة.",
        "darija": "الدرب، الحي ولا الزنقة فين ساكنين الجيران فالمدينة القديمة.",
        "english": "neighborhood alley / quarter"
    },
    "bain maure": {
        "type": "nom masculin",
        "fr_def": "Établissement public de bains de vapeur chauds (hammam traditionnel).",
        "arabic": "الحمام المغربي التقليدي للاستحمام بالبخار والماء الساخن.",
        "darija": "الحمام الشعبي السخون فين كيمشيو العيالات والرجال يتحكو بالصابون البلدي.",
        "english": "traditional Moorish bathhouse / hammam"
    },
    "cadi": {
        "type": "nom masculin",
        "fr_def": "Juge musulman traditionnel appliquant le droit islamique (charia) pour les mariages, successions et litiges.",
        "arabic": "القاضي الشرعي، الحاكم الذي يفصل في قضايا الأسرة والمعاملات وفق الشريعة الإسلامية.",
        "darija": "القاضي الشرعي، لي كان كيكتب عقود الزواج ويفصل بين الناس فالشريعة.",
        "english": "Qadi / Islamic judge"
    },
    "muphti": {
        "type": "nom masculin",
        "fr_def": "Docteur de la loi islamique habilité à émettre des avis juridiques religieux (fatwas).",
        "arabic": "المفتي، عالم الفقه المخول بإصدار الفتاوى والأحكام الشرعية.",
        "darija": "المفتي، العالم الديني المتمكن لي كيفتي للناس فالأمور الدينية المعقدة.",
        "english": "mufti / Islamic legal scholar"
    },
    "chérif": {
        "type": "nom masculin",
        "fr_def": "Descendant du prophète Mahomet, bénéficiant d'un grand respect traditionnel (comme Maâlem Abdeslam).",
        "arabic": "الشريف، من ينحدر من سلالة النبي محمد صلى الله عليه وسلم ويحظى بمكانة محترمة.",
        "darija": "الشريف، لي كينتامي للنسب النبوي الشريف وكان عندو احترام كبير ففاس.",
        "english": "Sharif / noble descendant of the Prophet"
    },
    "patio": {
        "type": "nom masculin",
        "fr_def": "Cour intérieure à ciel ouvert au centre d'une maison marocaine traditionnelle (ouast ed-dar).",
        "arabic": "فناء الدار أو وسط الدار، ساحة داخلية مكشوفة تتوسط الرياض أو المنزل التقليدي.",
        "darija": "وسط الدار ولا الصحن ديال الدار التقليدية لي كيكون محلول فالسما.",
        "english": "central open courtyard"
    },
    "ambre": {
        "type": "nom masculin",
        "fr_def": "Substance aromatique précieuse utilisée pour les parfums et la confection de colliers précieux.",
        "arabic": "العنبر، مادة عطرية ثمينة تُستعمل في التبخير وصناعة العقود والحلي النفيسة.",
        "darija": "العنبر الحر، مادة عطرية غالية كيديروها فالعطور والسلاسل ديال العيالات.",
        "english": "ambergris / precious fragrance"
    },
    "santal": {
        "type": "nom masculin",
        "fr_def": "Bois aromatique précieux d'Orient brûlé comme encens lors des cérémonies.",
        "arabic": "خشب الصندل العطري الفاخر، يُحرق كبخور زكي الرائحة في المناسبات الدينية.",
        "darija": "عود الصندل، خشب كيعطي ريحة البخور زوينة فاش كيتبخر بيه.",
        "english": "sandalwood"
    },
    "solitude": {
        "type": "nom féminin",
        "fr_def": "État d'une personne qui est seule ou qui éprouve un sentiment d'isolement moral et affectif.",
        "arabic": "الوحدة أو العزلة، شعور الفرد بالانعزال النفسي والانفصال الوجداني عن الآخرين.",
        "darija": "الوحدة، الإحساس لي كان عايش فيه سيدي محمد فاش كيحس براسو معزول على الناس.",
        "english": "solitude / loneliness"
    },
    "torpeur": {
        "type": "nom féminin",
        "fr_def": "Diminution de la sensibilité et de l'activité, engourdissement physique ou moral.",
        "arabic": "الخُمول أو السُّبات، حالة من الفتور والبلادة في الحركة أو التفكير.",
        "darija": "الرخاوة والنعاس، حالة فاش كيكون الواحد فاشل وما قادرش يتحرك بحال لي سكران بالنعاس.",
        "english": "torpor / sluggish numbness"
    },
    "léthargie": {
        "type": "nom féminin",
        "fr_def": "Sommeil profond et prolongé ; engourdissement extrême et perte d'énergie.",
        "arabic": "السبات العميق، حالة نوم ثقيل وفقدان كامل للحيوية والنشاط.",
        "darija": "نعاس تقيل بزاف وغياب الحيوية، فحال يلا بنادم غايب على الوعي.",
        "english": "lethargy / deep sleep"
    },
    "baluchon": {
        "type": "nom masculin",
        "fr_def": "Paquet de vêtements ou d'effets personnels noués dans une pièce d'étoffe.",
        "arabic": "صُرَّة الثياب، حزمة من الملابس تُربط في قطعة قماش لحملها في السفر أو الحمام.",
        "darija": "البقجة ولا الرزمة ديال الحوايج لي كيعقدوها فالتوب باش يديروها للحمام ولا للسفر.",
        "english": "bundle / cloth pack"
    },
    "cénotaphe": {
        "type": "nom masculin",
        "fr_def": "Tombeau élevé à la mémoire d'un défunt mais qui ne contient pas son corps (mausolée commémoratif).",
        "arabic": "ضريح تذكاري رمزي يُقام لتكريم ميت دون أن يضم رفاته الحقيقية.",
        "darija": "قبر تذكاري ولا ضريح رمزي كيدار تخليداً لذكرى شي ميت بلا ما تكون فيه الجثة ديالو.",
        "english": "cenotaph / memorial monument"
    },
    "simarre": {
        "type": "nom féminin",
        "fr_def": "Longue robe d'apparat que portaient autrefois les magistrats, prélats ou souverains.",
        "arabic": "جبة واسعة وفضفاضة ذات أكمام طويلة يرتديها القضاة أو الوجهاء في المناسبات الرسمية.",
        "darija": "كسوة واسعة ومطروزة ديال الهيبة كيلبسوها القضاة والعلماء فالأعياد والمحافل.",
        "english": "loose ceremonial robe / chimere"
    },
    "défunt": {
        "type": "nom masculin / adjectif",
        "fr_def": "Personne décédée, mort.",
        "arabic": "المرحوم أو الميت الذي فارق الحياة.",
        "darija": "المرحوم ولا الميت لي توفى.",
        "english": "deceased / late"
    },
    "acariâtre": {
        "type": "adjectif",
        "fr_def": "D'un caractère difficile, querelleur, désagréable et prompt aux disputes.",
        "arabic": "نكد الطباع، سيئ الخلق وشديد المراس، دائم الشجار والتذمر.",
        "darija": "نݣار وقبيح الطبع، كيعجبو الصداع والخصومات على والو.",
        "english": "crabby / ill-tempered / quarrelsome"
    },
    "vitupérer": {
        "type": "verbe intransitif",
        "infinitive": "vitupérer",
        "fr_def": "Proférer des paroles violentes, des reproches véhéments et des injures.",
        "arabic": "كال الشتائم واللعنات، وصبّ جام غضبه بالصراخ والاحتجاج العنيف.",
        "darija": "سب وشتم وبدا كيعاير بصوت عالي وكيغوت من شدة الغضب (بحال لي دارت لالة زبيدة).",
        "english": "to vituperate / rail violently"
    },
    "gourmander": {
        "type": "verbe transitif",
        "infinitive": "gourmander",
        "fr_def": "Réprimander doucement ou gronder avec bienveillance et tendresse.",
        "arabic": "أنّب بلطف وعاتب بود وحنان دون قسوة.",
        "darija": "غوت على شي حد بلطف وحنان، بحال فاش الأم كتعاتب ولدها الصغير بلا ما تعاقبو بقسوة.",
        "english": "to scold gently"
    },
    "se lamenter": {
        "type": "verbe pronominal",
        "infinitive": "se lamenter",
        "fr_def": "Manifester bruyamment sa douleur ou son chagrin par des plaintes et des pleurs.",
        "arabic": "النواح والشكوى، التعبير عن الحزن الشديد بالبكاء وذكر المصائب.",
        "darija": "ندب وبكى وتشكى، كيبكي ويشكي من الزمان والمشاكل ديالو.",
        "english": "to lament / wail"
    },
    "demeurai": {
        "type": "verbe (passé simple)",
        "infinitive": "demeurer",
        "fr_def": "Je restai (dans un lieu ou dans un état donné) ; forme du passé simple.",
        "arabic": "بقيتُ أو مكثتُ (بصيغة الماضي البسيط الأدبي).",
        "darija": "بقيت فواحد البلاصة ولا فواحد الحالة (صيغة الماضي البسيط بالفرنسية).",
        "english": "I remained / I stayed"
    },
    "s'ingénia": {
        "type": "verbe (passé simple)",
        "infinitive": "s'ingénier",
        "fr_def": "Il/Elle chercha tous les moyens possibles, déploya toute son habileté pour réussir.",
        "arabic": "تفنن واحتال واجتهد بكل ذكاء في ابتكار الطرق لتحقيق غايته.",
        "darija": "دار كل ما فجهدو وتحايل بذكاء باش يلقى حل لشي حاجة.",
        "english": "contrived / taxed one's ingenuity"
    },
    "fût": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "être",
        "fr_def": "Forme du subjonctif imparfait du verbe être (3e personne du singulier).",
        "arabic": "صيغة الماضي في صيغة الشك (subjonctif imparfait) من فعل كان.",
        "darija": "صيغة الشك الأدبية من فعل كان (être) كتستعمل فالنصوص الكلاسيكية.",
        "english": "were / might be (imperfect subjunctive of to be)"
    },
    "aperçut": {
        "type": "verbe (passé simple)",
        "infinitive": "apercevoir",
        "fr_def": "Il/Elle vit distinctement ou remarqua soudainement.",
        "arabic": "لمح أو رأى بوضوح فجأة (بصيغة الماضي البسيط).",
        "darija": "شاف ولا لمح شي حاجة بالزربة فصيغة الماضي البسيط الأدبي.",
        "english": "caught sight of / spotted"
    },
    "songeai": {
        "type": "verbe (passé simple)",
        "infinitive": "songer",
        "fr_def": "Je pensai profondément, je méditai.",
        "arabic": "فكرت ملياً وتأملت في خاطري (بصيغة الماضي البسيط).",
        "darija": "فكرت مزيان وتأملت فبالي فصيغة الماضي البسيط الأدبي.",
        "english": "I reflected / I contemplated"
    },
    "prêta": {
        "type": "verbe (passé simple)",
        "infinitive": "prêter",
        "fr_def": "Il accorda son attention (ex: prêta l'oreille).",
        "arabic": "أعار أو أصغى (أعار سمعه وانتباهه بصيغة الماضي البسيط).",
        "darija": "عطا ودنو وتصنت بانتباه فصيغة الماضي البسيط الأدبي.",
        "english": "lent (lent an ear)"
    }
}

DICTIONARY_HUGO = {
    # Argot & Criminal Slang (Victor Hugo Ch. 23 & 30)
    "argot": {
        "type": "nom masculin",
        "fr_def": "Langage secret et codé des voleurs, des bagnards et de la pègre criminelle au XIXe siècle.",
        "arabic": "لغة العالَم السُّفلي؛ اللهجة السرية والمشفرة التي يتحدث بها المجرمون والمساجين.",
        "darija": "لوغة الشفارة والمحبوسين، هضرة مشفرة ما كيفهموها غير الحرايفية والمسجونين.",
        "english": "prison slang / cant of criminals"
    },
    "veuve": {
        "type": "nom féminin (argot)",
        "fr_def": "Nom en argot donné à la guillotine (l'échafaud).",
        "arabic": "الأرملة، اسم في لغة السجون يُطلق مجازياً على المقصلة (آلة الإعدام).",
        "darija": "الأرملة، سمية كيعطيوها المساجين للمقصلة (المشنقة ولا الݣيوطين) لي كتقطع الريوس.",
        "english": "the widow (slang for the guillotine)"
    },
    "tronche": {
        "type": "nom féminin (argot)",
        "fr_def": "La tête humaine dans l'argot des forçats.",
        "arabic": "الرأس أو الجمجمة في لغة المساجين وقطاع الطرق.",
        "darija": "الراس، سمية فلوغة الحبس كيقصدو بها راس بنادم لي غادي يتقطع.",
        "english": "head / noggin (slang)"
    },
    "carme": {
        "type": "nom masculin (argot)",
        "fr_def": "L'argent, la monnaie dans le langage argotique des voleurs.",
        "arabic": "النقود أو المال في معجم اللصوص والعصابات.",
        "darija": "الفلوس ولا الصرف فلوغة الحبس والشفارة.",
        "english": "money / cash (slang)"
    },
    "chouriner": {
        "type": "verbe transitif (argot)",
        "infinitive": "chouriner",
        "fr_def": "Poignarder, frapper ou tuer avec un couteau (un chourin).",
        "arabic": "الطعن بالسكين، قتل شخص بواسطة آلة حادة في لغة المجرمين.",
        "darija": "ضرب ولا غرس بالموس والسكين، ذبح ولا طعن بالجنوي.",
        "english": "to stab with a knife"
    },
    "sorgue": {
        "type": "nom féminin (argot)",
        "fr_def": "La nuit dans le jargon des malfaiteurs.",
        "arabic": "الليل أو الظلام في لهجة السجون.",
        "darija": "الليل والظلام فلوغة الشفارة.",
        "english": "night (slang)"
    },
    "tourline": {
        "type": "nom féminin (argot)",
        "fr_def": "La mort ou la guillotine dans le jargon des forçats.",
        "arabic": "الموت أو المقصلة في قاموس المحكومين بالأشغال الشاقة.",
        "darija": "الموت ولا المقصلة فلوغة المحكومين لي غادي يتقطع ليهم الراس.",
        "english": "death / the scaffold (slang)"
    },
    "dab": {
        "type": "nom masculin (argot)",
        "fr_def": "Le père, le maître ou le chef dans l'argot des voleurs.",
        "arabic": "الأب أو الزعيم أو المعلم في لغة اللصوص.",
        "darija": "الوالد ولا الشاف الكبير ديال العصابة فلوغة الشفارة.",
        "english": "father / boss (slang)"
    },
    "fanandel": {
        "type": "nom masculin (argot)",
        "fr_def": "Camarade, compagnon de crime ou de cellule.",
        "arabic": "الرفيق في الجريمة أو زميل الزنزانة في سجون فرنسا القديمة.",
        "darija": "العشير ديال الحبس ولا الشريك فالجريمة بين المساجين.",
        "english": "comrade / pal in crime (slang)"
    },
    "marquant": {
        "type": "nom masculin (argot)",
        "fr_def": "Le procureur ou le juge qui fait accuser et condamner.",
        "arabic": "القاضي أو وكيل الملك الذي يوجه التهم ويطلب الإدانة.",
        "darija": "وكيل الملك ولا القاضي لي كيطيح العقوبات القاصحة فالمحكمة.",
        "english": "prosecutor / judge (slang)"
    },
    "bobe": {
        "type": "nom féminin (argot)",
        "fr_def": "La montre en or ou en argent dérobée par un voleur.",
        "arabic": "الساعة المسروقة في قاموس النشالين واللصوص.",
        "darija": "المكانة المسروقة ديال الذهب فقاموس الشفارة.",
        "english": "watch (stolen, slang)"
    },
    "trimar": {
        "type": "nom masculin (argot)",
        "fr_def": "Le grand chemin, la route où l'on détrousse les voyageurs.",
        "arabic": "الطريق السريع أو الدرب الذي يتعرض فيه المسافرون للسطو.",
        "darija": "الطريق الكبيرة ولا الطريق الخالية لي كيكريسيو فيها قطاع الطرق.",
        "english": "highway / open road (slang)"
    },
    # Penal & Legal Terms
    "grève": {
        "type": "nom féminin",
        "fr_def": "La place de Grève à Paris, lieu historique où se déroulaient les exécutions capitales publiques.",
        "arabic": "ساحة الإعدام التاريخية بباريس (ساحة الغريف) حيث كان يُنفذ الإعدام علناً أمام الجمهور.",
        "darija": "ساحة لاݣريف فباريس فين كانو كيقسمو الريوس وكيعدمو المحكومين قدام الناس كاملين.",
        "english": "Place de Grève (historic execution square in Paris)"
    },
    "bicêtre": {
        "type": "nom propre masculin",
        "fr_def": "Ancienne prison et hospice sinistre de Paris où étaient enfermés les condamnés à mort et forçats.",
        "arabic": "سجن بيسيتر الرهيب بضواحي باريس، حيث كان يُعتقل المحكومون بالإعدام والأشغال الشاقة.",
        "darija": "حبس بيسيتر، واحد من أكفس الحبوسات فباريس لي كانو كيديرو فيه المحكومين بالإعدام.",
        "english": "Bicêtre prison (notorious historic prison in Paris)"
    },
    "conciergerie": {
        "type": "nom féminin",
        "fr_def": "Prison centrale de Paris sur l'île de la Cité où le condamné passe ses ultimes heures avant la Grève.",
        "arabic": "سجن الكونسيرجيري الشهير بباريس، محطة السجين الأخيرة قبل نقله إلى المقصلة.",
        "darija": "حبس لاكونسيرجيري فباريس، المحطة اللخرة لي كيدوز فيها المحكوم ساعاتو اللخرين قبل ما يديوه للإعدام.",
        "english": "Conciergerie prison"
    },
    "ferrade": {
        "type": "nom féminin",
        "fr_def": "Cérémonie violente au cours de laquelle on rivait un carcan de fer au cou des condamnés aux galères.",
        "arabic": "حفل التصفيد بالحديد، عملية تثبيت الأطواق الحديدية الثقيلة حول أعناق المحكومين بالأشغال الشاقة.",
        "darija": "عملية التݣلاص والربيط بالسناسل والحديد على عنق المحكومين بالأشغال الشاقة قبل ما يدوهوم للباغنو.",
        "english": "the irons ceremony / chaining of convicts"
    },
    "carcan": {
        "type": "nom masculin",
        "fr_def": "Collier de fer attaché à un poteau ou à une chaîne pour punir ou entraver un prisonnier.",
        "arabic": "الطوق الحديدي، قيد من حديد يُغلق بإحكام حول عنق السجين.",
        "darija": "الكوليا والقلادة ديال الحديد الثقيل لي كيسدوها على عنق المحبوس.",
        "english": "iron collar / pillory"
    },
    "échafaud": {
        "type": "nom masculin",
        "fr_def": "Estrade en bois sur laquelle est dressée la guillotine pour l'exécution publique.",
        "arabic": "منصة الإعدام الخشبية، المرتفع الذي تُنصب فوقه المقصلة.",
        "darija": "المنصة الخشبية العالية لي كانت كتحط فوقها المقصلة باش كلشي يشوف الإعدام.",
        "english": "scaffold / execution platform"
    },
    "bourreau": {
        "type": "nom masculin",
        "fr_def": "Exécuteur des arrêts de justice chargé de décapiter ou de supplicier les condamnés.",
        "arabic": "السيّاف أو الجلاد، المكلّف الرسمي بتنفيذ حكم القتل وقطع الأعناق.",
        "darija": "السياف ولا الجلاد لي كيطيح المقصلة وكيقطع راس المحكوم.",
        "english": "executioner / headsman"
    },
    "couperet": {
        "type": "nom masculin",
        "fr_def": "Lame lourde et tranchante d'acier triangulaire qui coulisse dans la guillotine pour trancher le cou.",
        "arabic": "شفرة المقصلة الفولاذية الحادة التي تهوي لتقطع عنق المحكوم في ثانية.",
        "darija": "الموس القاطع والتقيل ديال لݣيوطين لي كيطيح من الفوق باش يطير الراس.",
        "english": "blade of the guillotine / cleaver"
    },
    "pourvoyeur": {
        "type": "nom masculin",
        "fr_def": "Personne qui fournit ou alimente (ex: le procureur royal est qualifié de pourvoyeur de l'échafaud).",
        "arabic": "المموّن أو المزوّد، من يمد جهة ما بما تحتاجه (كوكيل الملك الذي يزود المقصلة بالضحايا).",
        "darija": "الممون لي كيجيب السلعة وكيغذي شي حاجة (بحال وكيل الملك لي كيعمر المقصلة بالريوس).",
        "english": "purveyor / supplier"
    },
    "supplice": {
        "type": "nom masculin",
        "fr_def": "Torture corporelle vive ou souffrance morale intense infligée à un condamné.",
        "arabic": "العذاب الأليم أو التنكيل الجسدي والمعنوي الشديد.",
        "darija": "العذاب والمحنة القاصحة بزاف جسدياً ونفسياً.",
        "english": "torment / torture / execution"
    },
    "linceul": {
        "type": "nom masculin",
        "fr_def": "Pièce de toile dans laquelle on enveloppe un cadavre avant de l'inhumer.",
        "arabic": "الكفن، القماش الأبيض الذي يُلف فيه الميت ويوضع به في القبر.",
        "darija": "الكفن الأبيض لي كيتلف فيه الميت قبل ما يتدفن.",
        "english": "shroud / winding sheet"
    },
    "rémission": {
        "type": "nom féminin",
        "fr_def": "Pardon accordé pour une faute ou une peine ; grâce accordée par le souverain.",
        "arabic": "العفو أو المغفرة والصفح عن العقوبة بمرسوم ملكي.",
        "darija": "العفو الملكي والسماحة من عقوبة الإعدام.",
        "english": "remission / presidential pardon"
    },
    "pourrissoir": {
        "type": "nom masculin",
        "fr_def": "Cachot humide et infect où l'on laissait pourrir les prisonniers oubliés.",
        "arabic": "مَطْمَرة التعفين، زنزانة رطبة وسفلى تُترك فيها أجساد المحكومين لتتعفن.",
        "darija": "المطمورة الخانزة فالحبس فين كانو كيحطو بنادم يعفن فالغيس والظلام.",
        "english": "rot-hole / dungeon vault"
    },
    # Conjugated Verbs
    "pût": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "pouvoir",
        "fr_def": "Forme du subjonctif imparfait du verbe pouvoir (3e personne du singulier).",
        "arabic": "صيغة الماضي للشك من فعل قدر أو استطاع (subjonctif imparfait).",
        "darija": "صيغة الماضي فصيغة الشك من فعل قدر (pouvoir).",
        "english": "could / might be able to"
    },
    "fît": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "faire",
        "fr_def": "Forme du subjonctif imparfait du verbe faire (3e personne du singulier).",
        "arabic": "صيغة الماضي للشك من فعل فعل أو صنع (subjonctif imparfait).",
        "darija": "صيغة الماضي فصيغة الشك من فعل دار ولا صنع (faire).",
        "english": "did / might make"
    },
    "vînt": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "venir",
        "fr_def": "Forme du subjonctif imparfait du verbe venir (3e personne du singulier).",
        "arabic": "صيغة الماضي للشك من فعل جاء أو أتى (subjonctif imparfait).",
        "darija": "صيغة الشك الأدبية من فعل جاء (venir).",
        "english": "might come / should come"
    },
    "voulût": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "vouloir",
        "fr_def": "Forme du subjonctif imparfait du verbe vouloir (3e personne du singulier).",
        "arabic": "صيغة الماضي للشك من فعل أراد أو رغب (subjonctif imparfait).",
        "darija": "صيغة الشك الأدبية من فعل بغى ولا أراد (vouloir).",
        "english": "might wish / should desire"
    },
    "décréta": {
        "type": "verbe (passé simple)",
        "infinitive": "décréter",
        "fr_def": "Il ordonna officiellement ou prononça un jugement irrévocable.",
        "arabic": "أصدر أمراً قضائياً أو حكماً رسمياً صارماً (بصيغة الماضي البسيط).",
        "darija": "حكم وقرر رسمياً فصيغة الماضي البسيط الأدبي.",
        "english": "decreed / ordered"
    },
    "abattit": {
        "type": "verbe (passé simple)",
        "infinitive": "abattre",
        "fr_def": "Il fit tomber avec violence ou terrassa moralement.",
        "arabic": "أسقط أو صرع بقوة، وحطم المعنويات (بصيغة الماضي البسيط).",
        "darija": "طيح وسحق بقوة فصيغة الماضي البسيط الأدبي.",
        "english": "struck down / felled"
    }
}

DICTIONARY_ANTIGONE = {
    # Tragedy & Classical Terms
    "sépulture": {
        "type": "nom féminin",
        "fr_def": "Lieu où est déposé un mort ; acte d'ensevelir un corps avec les honneurs rituels.",
        "arabic": "الدفن الشرعي أو القبر؛ إكرام الميت بمواراته الثرى وفق الطقوس الجنائزية الواجبة.",
        "darija": "الدفين وإكرام الميت بالدفن والقبر والطقوس الدينية الواجبة عليه.",
        "english": "burial / sepulchre / formal funeral"
    },
    "ananké": {
        "type": "nom féminin",
        "fr_def": "Le destin inéluctable, la fatalité tragique qui s'impose aux héros de la mythologie grecque.",
        "arabic": "القضاء والقدر الحتمي، الحتمية المأساوية القاهرة في التراجيديا الإغريقية.",
        "darija": "المكتاب المحتوم والقدر التراجيدي لي ما عند الشخصيات كيفاش يهربو منو.",
        "english": "fatal necessity / tragic destiny"
    },
    "ciguë": {
        "type": "nom féminin",
        "fr_def": "Plante très vénéneuse dont le suc toxique servait autrefois à exécuter les condamnés à mort (comme Socrate).",
        "arabic": "الشَّوْكران، نبات سام وقاتل كان يُعطى عصيره للمحكومين بالإعدام في اليونان القديمة.",
        "darija": "عشبة الشوكران المسمومة لي كانو كيسقيوها للمحكومين بالإعدام باش يموتو مسمومين.",
        "english": "hemlock (poisonous plant)"
    },
    "néfaste": {
        "type": "adjectif",
        "fr_def": "Qui apporte le malheur, la ruine ou le désastre.",
        "arabic": "مشؤوم أو نحس، ما يجلب الكوارث والمصائب والدمار.",
        "darija": "مشؤوم ومنحوس، كيجيب غير المصائب والخراب.",
        "english": "ill-fated / harmful / nefarious"
    },
    "hyménée": {
        "type": "nom masculin",
        "fr_def": "Le mariage, l'union conjugale solennelle.",
        "arabic": "الزواج أو القِران المقدس والرباط الزوجي.",
        "darija": "العرس والزواج والرباط بين الراجل والمرا.",
        "english": "matrimony / wedding"
    },
    "charogne": {
        "type": "nom féminin",
        "fr_def": "Corps d'un animal ou d'un être humain en état de décomposition avancée et puante.",
        "arabic": "الجيفة أو الجثة العفنة المنتنة المتروكة في العراء لتأكلها الجوارح والكلاب.",
        "darija": "الجيفة المعفنة المرمية فالخلا لي كتاكلها الكلاب والطيران الجوارح.",
        "english": "carrion / rotting carcass"
    },
    "impie": {
        "type": "adjectif / nom",
        "fr_def": "Qui outrage la religion, qui méprise les devoirs sacrés et les dieux.",
        "arabic": "الفاسق، الكافر، أو المعتدي على حرمة المقدسات والفرائض الإلهية.",
        "darija": "كافر ولا فاسق لي كيتعدى على حرمة الدين ومكيحترمش المقدسات والأصول.",
        "english": "impious / blasphemous / ungodly"
    },
    "forfait": {
        "type": "nom masculin",
        "fr_def": "Crime odieux, acte très grave et impardonnable.",
        "arabic": "الجُرم الشنيع أو الجناية الفظيعة التي لا تُغتفر.",
        "darija": "الجريمة الكبيرة والمنكرة لي كتروع النفوس.",
        "english": "heinous crime / outrage"
    },
    "dérisoire": {
        "type": "adjectif",
        "fr_def": "Tellement minime, insignifiant ou absurde qu'il prête à rire amèrement.",
        "arabic": "تافه أو هزيل ومثير للسخرية والشفقة لشدة ضآلته.",
        "darija": "تافه وبسيط بزاف لدرجة كيبان كيضحك ويبكي فالوقت نفسو.",
        "english": "derisory / laughably insignificant"
    },
    "édile": {
        "type": "nom masculin",
        "fr_def": "Magistrat municipal chargé de l'administration et de l'ordre d'une cité.",
        "arabic": "مسؤول أو حاكم بلدي مكلّف بإدارة شؤون المدينة وضبط النظام.",
        "darija": "مسؤول محلي ولا حاكم ديال المدينة مكلف بتسيير أمور الناس والنظام.",
        "english": "magistrate / municipal official"
    },
    "oisif": {
        "type": "adjectif",
        "fr_def": "Qui est sans occupation, inactif ou qui passe son temps à ne rien faire d'utile.",
        "arabic": "عاطل أو خامل، من لا يمارس عملاً مفيداً ويمضي وقته في الفراغ.",
        "darija": "جالس ما عندو ما يدار، عاطل ومامسوق لتا حاجة وكيضيع الوقت.",
        "english": "idle / unoccupied"
    },
    "hybris": {
        "type": "nom féminin",
        "fr_def": "Dans la tragédie grecque, l'orgueil démesuré et la démesure qui poussent un héros à défier les dieux.",
        "arabic": "العنجهية المفرطة والغرور القاتل الذي يدفع البطل لتحدي الآلهة والقوانين.",
        "darija": "العياقة والتكبر الزايد عن حده لي كيخلي الواحد يتحدى القوانين والقدر حتى كيخرج على راسو.",
        "english": "hubris / excessive pride"
    },
    "superbe": {
        "type": "adjectif",
        "fr_def": "Fier, hautain, plein d'un orgueil noble ou arrogant dans l'affrontement tragique.",
        "arabic": "شامخ، معتز بنفسه، أو متكبر ممتلئ عزة وكبرياء أمام الموت.",
        "darija": "عزيز النفس وشامخ ومكبر شانو قدام الموت والتهديد.",
        "english": "proud / haughty / magnificent"
    },
    "déchoir": {
        "type": "verbe intransitif",
        "infinitive": "déchoir",
        "fr_def": "Perdre son rang, sa dignité, son autorité ou sa valeur morale.",
        "arabic": "الانحطاط والسقوط، فقدان الهيبة والمنزلة والكرامة.",
        "darija": "طاح من عين الناس وفقد الهيبة والشأن والكرامة ديالو.",
        "english": "to decay / lose status / forfeit dignity"
    },
    "abject": {
        "type": "adjectif",
        "fr_def": "Qui mérite le mépris le plus profond par sa bassesse, sa lâcheté ou son infamie.",
        "arabic": "حقير، دنيء وساقط الأخلاق يثير الاشمئزاز.",
        "darija": "حقير ورخيص وخالع من النذالة ديالو.",
        "english": "abject / despicable / vile"
    },
    "souillure": {
        "type": "nom féminin",
        "fr_def": "Tache morale ou impureté religieuse qui profane un lieu ou une lignée.",
        "arabic": "دنس أو رجس أو عار يلطخ الشرف والمقدسات.",
        "darija": "الدنس والعار لي كيوسخ الشرف والدين.",
        "english": "stain / pollution / defilement"
    },
    # Verbal Forms
    "mourût": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "mourir",
        "fr_def": "Forme du subjonctif imparfait du verbe mourir (3e personne du singulier).",
        "arabic": "صيغة الماضي للشك من فعل مات (subjonctif imparfait).",
        "darija": "صيغة الشك الأدبية من فعل مات (mourir).",
        "english": "might die / should die"
    },
    "fussions": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "être",
        "fr_def": "Forme du subjonctif imparfait du verbe être (1re personne du pluriel).",
        "arabic": "صيغة الماضي للشك من فعل كان مع ضمير نحن (subjonctif imparfait).",
        "darija": "صيغة الشك الأدبية ديال فعل كنا (être مع nous).",
        "english": "we were / might be"
    },
    "osât": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "oser",
        "fr_def": "Forme du subjonctif imparfait du verbe oser (3e personne du singulier).",
        "arabic": "صيغة الماضي للشك من فعل تجرأ أو جسر (subjonctif imparfait).",
        "darija": "صيغة الشك الأدبية من فعل زعم ولا تجرأ (oser).",
        "english": "might dare / dared"
    },
    "sût": {
        "type": "verbe (subjonctif imparfait)",
        "infinitive": "savoir",
        "fr_def": "Forme du subjonctif imparfait du verbe savoir (3e personne du singulier).",
        "arabic": "صيغة الماضي للشك من فعل علم أو عرف (subjonctif imparfait).",
        "darija": "صيغة الشك الأدبية من فعل عرف (savoir).",
        "english": "might know / knew"
    }
}

def build_all_dictionaries(base_dir: Path):
    data_dir = base_dir / "data"
    save_json(data_dir / "la_boite_a_merveilles" / "dictionary.json", BOITE_FULL_DICT)
    save_json(data_dir / "le_dernier_jour_dun_condamne" / "dictionary.json", HUGO_FULL_DICT)
    save_json(data_dir / "antigone" / "dictionary.json", ANTIGONE_FULL_DICT)
    print(f"[OK] Built full dictionaries: {len(BOITE_FULL_DICT)} (Boîte), {len(HUGO_FULL_DICT)} (Hugo), {len(ANTIGONE_FULL_DICT)} (Antigone).")

if __name__ == '__main__':
    build_all_dictionaries(Path('.'))
