# -*- coding: utf-8 -*-
import json

DEEP_BOITE = {
    "vertige": {"type": "nom masculin", "fr_def": "Étourdissement intense provoqué par le bruit, la foule ou la hauteur.", "arabic": "دوار أو دوخة واضطراب شديد في التوازن والوعي.", "darija": "الدوخة فاش كيدوخ بنادم من قوة الصداع والزحام.", "english": "dizziness / vertigo"},
    "brasero": {"type": "nom masculin", "fr_def": "Récipient métallique (mejmar) où brûlent des braises pour le chauffage ou l'encens.", "arabic": "المِجْمَر أو الكانون التقليدي الذي توضع فيه الجمرات.", "darija": "المجمر ولا الكانون ديال الفحم لي كيديرو فيه العود والحرمل.", "english": "brazier / mejmar"},
    "gargoulette": {"type": "nom féminin", "fr_def": "Cruche poreuse en terre cuite qui maintient l'eau fraîche par évaporation (qolla).", "arabic": "القُلّة؛ إناء فخاري تقليدي لحفظ الماء بارداً وعذباً.", "darija": "القلة ديال الطين لي كيديرو فيها الما باش يبرد.", "english": "clay water jug / qolla"},
    "cauchemars": {"type": "nom masculin pluriel", "fr_def": "Rêves terrifiants provoquant l'angoisse et la panique nocturne de l'enfant.", "arabic": "الكوابيس المروعة المفزعة في المنام.", "darija": "الكوابيس والخلعات لي كيشوفهم بنادم فالنعاس.", "english": "nightmares"},
    "ineffaçable": {"type": "adjectif", "fr_def": "Qui ne peut être effacé ni oublié ; gravé à jamais dans la mémoire.", "arabic": "لا يُمحى ولا يزول من الذاكرة والوجدان.", "darija": "ما كيتمحاش ولا كيتنسى، لاصق فالبال ديما.", "english": "indelible / unerasable"},
    "brouille": {"type": "nom féminin", "fr_def": "Désaccord amer, dispute ou rupture d'amitié entre voisines (Zoubida et Rahma).", "arabic": "الخصومة والنزاع والقطيعة بين المتخاصمين.", "darija": "المخاصمة والقطيعة بين الجارات ولا الصحاب.", "english": "quarrel / falling out"},
    "exaspération": {"type": "nom féminin", "fr_def": "État d'irritation extrême poussé à son paroxysme.", "arabic": "شدة الغيظ والتوتر والغضب العارم.", "darija": "التعصاب والطلوع ديال الدم والفقصة.", "english": "exasperation / rage"},
    "dévot": {"type": "adjectif / nom", "fr_def": "Personne sincèrement attachée aux pratiques religieuses et à la prière.", "arabic": "المتعبد أو الورع التقي الملازم للعبادة.", "darija": "المؤمن ولا المصلي لي قانت لله وديما فالجامع.", "english": "devout / pious"},
    "candélabre": {"type": "nom masculin", "fr_def": "Grand chandelier à plusieurs branches supportant des bougies illuminant la fête.", "arabic": "الثريا أو الشمعدان الفاخر المتفرع الحامل للشموع.", "darija": "الشمعدان الكبير لي كيشعلو فيه الشمع فالمناسبات.", "english": "candelabrum"},
    "extase": {"type": "nom féminin", "fr_def": "État d'émerveillement mystique ou d'admiration spirituelle profonde.", "arabic": "الوجد والنشوة الروحية الصوفية والانجذاب.", "darija": "النشوة والاندهاش الكبير فاش كيطير العقل بالفرحة ولا الذكر.", "english": "ecstasy / mystical trance"},
    "funérailles": {"type": "nom féminin pluriel", "fr_def": "Cérémonie solennelle d'enterrement et prière mortuaire musulmane (Janaza).", "arabic": "مراسيم الجنازة وتشييع الميت إلى المقبرة.", "darija": "الجنازة والدفين ديال الميت بحضور الناس والفقها.", "english": "funeral ceremonies"},
    "lamentations": {"type": "nom féminin pluriel", "fr_def": "Cris de détresse et pleurs bruyants poussés pour pleurer la mort d'un proche.", "arabic": "العويل والنحيب والصراخ حزناً على الميت.", "darija": "النديب والولوال والغوات فاش كيموت الميت.", "english": "lamentations / wailing"},
    "défunt": {"type": "nom masculin", "fr_def": "La personne décédée dont on honore la mémoire (ex: Sidi Mohammed ben Tahar).", "arabic": "المرحوم أو الميت الذي توفي وانتقل إلى رحمة الله.", "darija": "المرحوم ولا الميت لي توفى ومشى عند ربي.", "english": "the deceased / late"},
    "blanchiment": {"type": "nom masculin", "fr_def": "Action de repeindre les murs du Msid à la chaux blanche pour l'Achoura.", "arabic": "تبييض وجير جدران الكتاب استعداداً لعيد عاشوراء.", "darija": "الجير والتبييض ديال الحيوط بالجير الأبيض قبل عاشوراء.", "english": "whitewashing"},
    "chaux": {"type": "nom féminin", "fr_def": "Poudre minérale blanche diluée dans l'eau pour badigeonner les murs traditionnels.", "arabic": "الجير الأبيض المستخدم في طلاء البيوت والمساجد.", "darija": "الجير لي كيخلطوه بالما ويصبغو بيه الحيوط.", "english": "lime / whitewash"},
    "aumône": {"type": "nom féminin", "fr_def": "Don généreux d'argent ou de nourriture offert aux pauvres par dévotion (Sadaqa).", "arabic": "الصدقة والإحسان المالي أو الغذائي للفقراء والمحتاجين.", "darija": "الصدقة لي كيعطيها المحسن لله على وجه الثواب.", "english": "alms / charity"},
    "festin": {"type": "nom masculin", "fr_def": "Repas somptueux et abondant préparé pour une fête ou des invités prestigieux.", "arabic": "الوليمة أو المأدبة الفاخرة الكبيرة العامرة بالطعام.", "darija": "الزردة ولا الوليمة العامرة بالماكلة واللحم والكسكسو.", "english": "feast / banquet"},
    "bijoutiers": {"type": "nom masculin pluriel", "fr_def": "Artisans fabricants et vendeurs de bijoux en argent ou or au souk des bijoutiers.", "arabic": "الصاغة وبائعو الحلي الذهبية والفضية في سوق الصياغين.", "darija": "الصياغية لي كيبيعو الدبالج والفضة والذهب فالقيسارية.", "english": "jewelers"},
    "bracelets": {"type": "nom masculin pluriel", "fr_def": "Bijoux d'argent (dbalij) convoités par Zoubida qui ont causé la violente bagarre au souk.", "arabic": "الأساور أو الدبالج الفضية التقليدية لزينة المرأة.", "darija": "الدبالج ديال الفضة لي كانت باغاهم لالة زبيدة ودارو المشاكل.", "english": "bracelets / bangles"},
    "rixe": {"type": "nom féminin", "fr_def": "Bagarre violente et désordonnée accompagnée d'injures et de coups.", "arabic": "الشجار أو العراك العنيف بالأيدي وتبادل الضرب والشتائم.", "darija": "مدابزة ولا مخاصمة عنيفة بالبونيات والغوات فالزنقة.", "english": "brawl / brawl in market"},
    "tumulte": {"type": "nom masculin", "fr_def": "Grand vacarme confus accompagné de désordre et d'agitation de foule.", "arabic": "الهرج والمرج والضجة الصاخبة والاضطراب العام.", "darija": "الروينة والهرج والغوات والزحام فاش كتنوض الفوضى.", "english": "tumult / uproar"},
    "ruine": {"type": "nom féminin", "fr_def": "Perte totale des économies et de l'argent de Maâlem Abdeslam au souk des tissus.", "arabic": "الإفلاس والخراب المالي وضياع رأس المال بالكامل.", "darija": "الإفلاس وضياع راس المال فاش المعلم عبد السلام توضرو ليه الفلوس.", "english": "financial ruin"},
    "dépouillement": {"type": "nom masculin", "fr_def": "Perte de tous ses biens, pauvreté soudaine et dénuement le plus total.", "arabic": "التجرّد والفقر المدقع بعد فقدان كل الممتلكات والمال.", "darija": "التجريد من كلشي وبنادم كيبقى على الضس بلا ريال.", "english": "destitution / divestment"},
    "moisson": {"type": "nom féminin", "fr_def": "Récolte des céréales à la campagne où le père va trimer comme journalier pour nourrir sa famille.", "arabic": "موسم الحصاد في البوادي لجمع القمح والشعير.", "darija": "الحصاد فالعروبية فين مشى با سيدي محمد يخدم باش يجمع الفلوس.", "english": "harvest"},
    "faucille": {"type": "nom féminin", "fr_def": "Outil manuel en fer courbé et tranchant servant à couper les épis de blé.", "arabic": "المنجل؛ أداة حديدية مقوسة وحادة لحصد الزرع وسنابله.", "darija": "المنجل لي كيحصدو بيه الزرع فالصيف فالعروبية.", "english": "sickle"},
    "voyant": {"type": "nom / adjectif", "fr_def": "Personne aveugle (Sidi El Arafi) douée d'une seconde vue spirituelle et de clairvoyance.", "arabic": "العراف أو البصير روحياً؛ كفيف يرى بقلبه وبصيرته النورانية.", "darija": "الشواف ولا البصير لي كيشوف بقلبو وخا هو عمى.", "english": "seer / clairvoyant"},
    "coquillages": {"type": "nom masculin pluriel", "fr_def": "Petits coquillages marins jetés et lus pour deviner l'avenir par Sidi El Arafi.", "arabic": "الودع؛ صدفات بحرية تُقرأ بها الطوالع للتنبؤ بالمستقبل.", "darija": "الودع لي كيضرب بيه الشواف باش يقرا الفال.", "english": "cowrie shells for divination"},
    "délivrance": {"type": "nom féminin", "fr_def": "Fin de l'épreuve tragique, retour du père victorieux et réouverture de la boîte magique.", "arabic": "الفرج والخلاص وانتهاء الكرب بعودة الأب إلى بيته.", "darija": "الفرج والتيسير فاش رجع الوالد وفرحات الدار وتفتحات البواطة.", "english": "deliverance / relief"},
    "allégresse": {"type": "nom féminin", "fr_def": "Joie très vive, bruyante et communicative partagée par tout le quartier.", "arabic": "البهجة الغامرة والفرح الشديد والانشراح العام.", "darija": "الفرحة الكبيرة والنشاط لي عم الدار فاش رجع المعلم عبد السلام.", "english": "great joy / merriment"}
}

DEEP_HUGO = {
    "guillotine": {"type": "nom féminin", "fr_def": "Machine d'exécution capitale munie d'un lourd couperet oblique coulissant entre deux montants.", "arabic": "المقصلة؛ آلة الإعدام الشهيرة ذات الشفرة الثقيلة الساقطة لقطع الرؤوس.", "darija": "المقصلة (الݣيوطين)، الآلة لي كتقطع الراس فثانية وحدة.", "english": "guillotine"},
    "cassation": {"type": "nom féminin", "fr_def": "Annulation d'un jugement rendu en violation de la loi par la plus haute cour de justice.", "arabic": "النقض والإبطال؛ إسقاط الحكم القضائي لمخالفته القانون.", "darija": "النقض والإبطال، المحكمة العليا فاش كتبطل حكم المحكمة العادية.", "english": "cassation / annulment"},
    "verdict": {"type": "nom masculin", "fr_def": "Décision solennelle prononcée par les jurés condamnant l'accusé à la peine de mort.", "arabic": "حكم المحكمة أو قرار هيئة المحلفين بإدانة المتهم بالإعدام.", "darija": "الحكم ديال القاضي لي نطق بالإعدام على المتهم.", "english": "verdict"},
    "huissier": {"type": "nom masculin", "fr_def": "Officier ministériel chargé de signifier officiellement le rejet du pourvoi et l'arrêt de mort.", "arabic": "المحضر القضائي الذي يبلّغ المحكوم رسمياً برفض الطعن وتنفيذ الإعدام.", "darija": "المحضر القضائي لي جا للحبس يبلغ المحكوم بلي العفو ترفض والإعدام اليوم.", "english": "bailiff / process server"},
    "geôle": {"type": "nom féminin", "fr_def": "Prison ou cellule sombre, étroite et sinistre fermée par de lourds verrous.", "arabic": "السجن أو المحبس القاتم الموحش المقفل بالأقفال الحديدية.", "darija": "الحبس ولا الزنزانة المظلمة والموحشة.", "english": "jail / dungeon"},
    "chaîne": {"type": "nom féminin", "fr_def": "Lourde liaison métallique reliant les bagnards par le cou sous une pluie battante.", "arabic": "سلسلة الأغلال الحديدية التي تشد أعناق السجناء معاً في ساحة السجن.", "darija": "السنسلة التقيلة ديال الحديد لي كتربط السجناء من عنقهم.", "english": "convict chain"},
    "galères": {"type": "nom féminin pluriel", "fr_def": "Ancienne peine criminelle consistant à ramer sur les vaisseaux royaux, devenue le bagne.", "arabic": "الأشغال الشاقة في سجون الموانئ الحربية في تولون وبريست.", "darija": "أشغال شاقة فالحبس ديال البحر كيدوزها المحكوم فالمحن والموت.", "english": "galleys / penal servitude"},
    "chiourme": {"type": "nom féminin", "fr_def": "L'ensemble des forçats d'un bagne ou l'équipe des gardes-chiourmes armés de bâtons.", "arabic": "جماعة المحكومين بالأشغال الشاقة أو حراسهم الغلاظ المسلحين بالهراوات.", "darija": "المحبوسين ديال البانيو والعساسة القاصحين لي كيسوطو عليهم.", "english": "convict crew / prison guards"},
    "carcan": {"type": "nom masculin", "fr_def": "Collier de fer rivé au cou du forçat pour l'attacher au poteau ou à la chaîne commune.", "arabic": "الطوق الحديدي المحكم حول عنق السجين لربطه في الأغلال.", "darija": "الطوق والݣوليا ديال الحديد لي كتزير على عنق المحبوس بالمطرقة.", "english": "iron collar / pillory"},
    "rivets": {"type": "nom masculin pluriel", "fr_def": "Gros clous métalliques que le forgeron écrase au marteau sur l'enclume tout près du crâne du prisonnier.", "arabic": "مسامير التثبيت الحديدية التي يدقها الحداد بالمطرقة قريباً من رأس السجين.", "darija": "المسامير والبراغي ديال الحديد لي كيضرب الحداد بالمطرقة حدا وذن السجين.", "english": "rivets of shackle"},
    "enclume": {"type": "nom féminin", "fr_def": "Masse de fer sur laquelle on frappe au marteau pour river le collier des forçats.", "arabic": "السندان؛ كتلة الحديد الصلبة التي يطرق عليها الحداد سلاسل السجناء.", "darija": "السندانة ديال الحديد لي كيدق عليها الحداد السلاسل.", "english": "anvil"},
    "infirmerie": {"type": "nom féminin", "fr_def": "Lieu de soins de la prison où le condamné a connu un court moment de répit et de lit propre.", "arabic": "مصحة السجن؛ المكان الذي وجد فيه المحكوم سريرًا نظيفاً وراحة مؤقتة.", "darija": "لانفيرمري ديال الحبس فين كيداواو السجناء المرتاضين.", "english": "prison infirmary"},
    "suaire": {"type": "nom masculin", "fr_def": "Linceul funèbre qui recouvre le corps d'un mort avant sa mise en bière.", "arabic": "الكفن أو الغطاء الجنائزي للميت.", "darija": "الكفن الأبيض ولا الغطا ديال الميت.", "english": "shroud"},
    "supplice": {"type": "nom masculin", "fr_def": "Souffrance morale et physique atroce imposée par la certitude de la décapitation.", "arabic": "العذاب الأليم أو التنكيل الجسدي والنفسي الرهيب.", "darija": "العذاب القاصح والمرار لي كيعيشو المحكوم قبل ما يتقطع راسو.", "english": "torment / execution ordeal"},
    "prêtre": {"type": "nom masculin", "fr_def": "L'ecclésiastique officiel venant réciter mécaniquement des prières sans compassion véritable pour le mourant.", "arabic": "القسيس أو رجل الدين المسيحي المرافق للمحكوم في عربة الإعدام.", "darija": "القسيس لي كيمشي مع المحكوم فالكروصة باش يطلب ليه الرحمة.", "english": "priest"},
    "crucifix": {"type": "nom masculin", "fr_def": "Image du Christ en croix tendue aux lèvres glacées du condamné avant la chute du couperet.", "arabic": "الصليب المقدس الذي يقبله المحكوم في لحظاته الأخيرة.", "darija": "الصليب لي كيعطيو للمحكوم يبوسو قبل ما يطيح عليه الموس.", "english": "crucifix"},
    "populace": {"type": "nom féminin", "fr_def": "Foule voyeuse et cruelle venue assister au spectacle sanglant de la guillotine comme à une fête.", "arabic": "العامة والدهماء المتعطشة للدماء المتجمهرة حول منصة الإعدام.", "darija": "الغاشي ولا بنادم المجموع كيتفرج فالموت بحال إلا فالموسم ولا الفراجة.", "english": "the rabble / bloodthirsty mob"},
    "quatre heures": {"type": "locution temporelle", "fr_def": "L'heure fatidique ultime où retentissent les pas des bourreaux dans le couloir de la prison.", "arabic": "الرابعة تماماً؛ الساعة القاتلة المحددة لتنفيذ الإعدام بالمقصلة.", "darija": "الربعة ديال العشية، الساعة المشؤومة لي غادي يتقطع فيها الراس.", "english": "four o'clock (execution hour)"}
}

def enrich():
    with open('data/la_boite_a_merveilles/dictionary.json', 'r', encoding='utf-8') as f:
        b = json.load(f)
    for k, v in DEEP_BOITE.items():
        b[k] = v
    with open('data/la_boite_a_merveilles/dictionary.json', 'w', encoding='utf-8') as f:
        json.dump(b, f, ensure_ascii=False, indent=2)
    print(f"Boite now has {len(b)} words.")

    with open('data/le_dernier_jour_dun_condamne/dictionary.json', 'r', encoding='utf-8') as f:
        h = json.load(f)
    for k, v in DEEP_HUGO.items():
        h[k] = v
    with open('data/le_dernier_jour_dun_condamne/dictionary.json', 'w', encoding='utf-8') as f:
        json.dump(h, f, ensure_ascii=False, indent=2)
    print(f"Hugo now has {len(h)} words.")

if __name__ == '__main__':
    enrich()
