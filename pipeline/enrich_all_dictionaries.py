# -*- coding: utf-8 -*-
"""
Enrich Boite and Hugo Dictionaries with high-frequency 1Bac words.
"""
import json

NEW_BOITE_WORDS = {
    "pudeur": {
        "type": "nom féminin",
        "fr_def": "Sentiment de réserve, de honte ou de discrétion morale face à ce qui est inconvenant.",
        "arabic": "الحياء أو الحشمة والوقار الأخلاقي وتجنب ما يخدش المروءة.",
        "darija": "الحيا والحشمة، الإنسان لي كيحشم وكيخاف من العيب ومن ربي.",
        "english": "modesty / decency"
    },
    "va-nu-pieds": {
        "type": "nom masculin",
        "fr_def": "Personne misérable, vagabond sans ressources ou individu sans scrupules ni dignité.",
        "arabic": "حافي القدمين؛ صعلوك أو شخص بئيس لا قيمة له ولا أخلاق له.",
        "darija": "بوزبال ولا مشرد ما كيسوا والو، بنادم صعلوك بلا شأن ولا ضمير.",
        "english": "barefoot beggar / scoundrel"
    },
    "mauvaise foi": {
        "type": "locution nominale",
        "fr_def": "Attitude malhonnête de quelqu'un qui nie la vérité en toute connaissance de cause.",
        "arabic": "سوء النية أو الخبث والخداع المتعمد وإنكار الحق جهاراً.",
        "darija": "نية خايبة وتخراج العينين، بنادم كينكر الحق وهو عارف راسو ظالم.",
        "english": "bad faith / dishonesty"
    },
    "agissements": {
        "type": "nom masculin pluriel",
        "fr_def": "Manières d'agir sournoises, intrigues coupables ou mauvaises actions calculées.",
        "arabic": "المكائد أو التصرفات الخبيثة والأفعال الملتوية والمشبوهة.",
        "darija": "التخربيق والفعايل الخايبين والتخلويض ديال شي واحد قبيح.",
        "english": "shady machinations / underhanded deeds"
    },
    "balance": {
        "type": "nom féminin",
        "fr_def": "Allusion islamique au Mîzân : la balance divine pesant les bonnes et mauvaises actions au Jugement Dernier.",
        "arabic": "الميزان؛ ميزان الأعمال يوم القيامة حيث توزن الحسنات والسيئات.",
        "darija": "الميزان ديال يوم الحساب لي غادي يتوزنو فيه أعمال العباد بالحق.",
        "english": "the Scales of Judgment"
    },
    "pacha": {
        "type": "nom masculin",
        "fr_def": "Haut dignitaire et représentant de l'autorité Makhzen gouvernant la ville traditionnelle.",
        "arabic": "الباشا، الحاكم أو القائد الممثل للسلطة المركزية في المدينة.",
        "darija": "الباشا، الحاكم ديال المدينة فالمخزن لي كيحكم بين المتخاصمين.",
        "english": "Pasha / city governor"
    },
    "plaideurs": {
        "type": "nom masculin pluriel",
        "fr_def": "Personnes engagées dans un procès, contestant un litige juridique devant le juge.",
        "arabic": "الخصوم أو المتنازعون الذين يعرضون دعواهم أمام القاضي.",
        "darija": "المتخاصمين لي مداعيين وواقفين قدام الحاكم ولا القاضي.",
        "english": "litigants / disputants"
    },
    "bouleversées": {
        "type": "adjectif / participe",
        "fr_def": "Profondément troublées, bouleversées d'émotion ou de chagrin intense.",
        "arabic": "مصدومات أو مضطربات من شدة الحزن والأسى الشديد.",
        "darija": "مصدومات ومروعات من كثرة الخلعة والحزن والقلق.",
        "english": "deeply shaken / devastated"
    },
    "chenapan": {
        "type": "nom masculin",
        "fr_def": "Gredin, vaurien ou fripon sans morale (qualificatif appliqué à Abdelkader).",
        "arabic": "وغد أو نذل أو لص خسيس لا عهد له.",
        "darija": "شفار ولا ولد الحرام لي كيغدر بالناس وكيخون الأمانة.",
        "english": "rogue / scoundrel"
    },
    "dévider": {
        "type": "verbe transitif",
        "fr_def": "Dérouler et bobiner du fil textile à l'aide d'un dévidoir dans l'artisanat.",
        "arabic": "كَبّ الخيوط أو لفّ الغزل في حِرفة النسيج التقليدي.",
        "darija": "كيدير الخيوط فالمغزل، كيطوي ويقاد الحرير والصوف فخدمة الخياطة.",
        "english": "to wind / reel thread"
    },
    "ourdir": {
        "type": "verbe transitif",
        "fr_def": "Disposer les fils de la chaîne sur un métier à tisser ; au figuré, tramer un complot.",
        "arabic": "سَدْي الخيوط في النول؛ ومجازياً: تدبير مؤامرة أو مكيدة خبيثة.",
        "darija": "كيوجد السدا ديال المنسج، ومجازياً: كيحفر لشي حد بالنية الخايبة.",
        "english": "to warp on a loom / plot"
    },
    "ourdissage": {
        "type": "nom masculin",
        "fr_def": "Opération préliminaire du tissage consistant à préparer les fils de chaîne parallèles.",
        "arabic": "إعداد السدى أو تسدية خيوط القماش على النول التقليدي.",
        "darija": "التوجاد ديال خيوط السدا فالحرفة ديال المنسوجات والحرير.",
        "english": "warping in weaving"
    },
    "navette": {
        "type": "nom féminin",
        "fr_def": "Outil en bois de tisserand contenant la canette de fil qui va et vient entre les fils de chaîne.",
        "arabic": "المكّوك، أداة النساج الخشبية التي تمرر خيوط اللحمة بين خيوط السدى.",
        "darija": "المكوك ديال المعلم الخراز ولا النساج لي كيدوز الخيط بسرعة.",
        "english": "weaver's shuttle"
    },
    "fuseau": {
        "type": "nom masculin",
        "fr_def": "Tige de bois renflée en son milieu servant à filer et tordre la laine ou la soie.",
        "arabic": "المِغْزل، عود خشبي يُستعمل لغزل الصوف أو الحرير ولفّه.",
        "darija": "المغزل لي كيغزلو بيه العيالات الصوف ولا الحرير باليد.",
        "english": "spindle"
    },
    "châtiment": {
        "type": "nom masculin",
        "fr_def": "Peine sévère infligée pour punir une faute morale, religieuse ou juridique.",
        "arabic": "العِقاب الصارم أو الجزاء الرادع على ذنب أو جريمة.",
        "darija": "العقاب القاصح ولا الجزاء الخايب لي كينزل على الظالم.",
        "english": "punishment / retribution"
    },
    "somnambule": {
        "type": "nom / adjectif",
        "fr_def": "Qui agit ou marche en dormant, plongé dans un état inconscient et rêveur.",
        "arabic": "السائر نائماً؛ شخص يتحرك كالمسحور فاقد الوعي بالواقع.",
        "darija": "لي كيتمشى وهو ناعس، ولا بنادم سارح وغايب على الدنيا.",
        "english": "sleepwalker"
    },
    "mausolée": {
        "type": "nom masculin",
        "fr_def": "Monument funéraire somptueux abritant la tombe d'un saint ou d'un personnage vénéré (zawiya / qobba).",
        "arabic": "الضريح أو المزار الشريف لوليّ صالح يزوره الناس للتبرك.",
        "darija": "الضريح ولا الروضة ديال السيد (بحال مولاي إدريس ولا سيدي علي بوغالب).",
        "english": "mausoleum / shrine"
    },
    "amulette": {
        "type": "nom féminin",
        "fr_def": "Petit objet ou papier écrit talismanique porté pour se protéger contre le mauvais œil et les démons.",
        "arabic": "التميمة أو الحجاب الواقي من العين والحسد والمس الشيطاني.",
        "darija": "الحجاب ولا الحروز لي كيعلقو بنادم باش يحميه من العين والجنون.",
        "english": "amulet / talisman"
    },
    "talisman": {
        "type": "nom masculin",
        "fr_def": "Objet doté de vertus magiques protectrices selon les croyances populaires.",
        "arabic": "الطلسم، كتابة أو شكل سحري يُعتقد أنه يحفظ حامله من الشرور.",
        "darija": "الطلسم ولا الكتيبة ديال الفقيه لحفظ الشخص من الأذى.",
        "english": "talisman"
    },
    "vociférer": {
        "type": "verbe transitif / intransitif",
        "fr_def": "Crier, hurler avec colère ou proférer des menaces et injures à voix haute.",
        "arabic": "الصياح والزعيق بغضب والتهديد بكلمات عنيفة جارحة.",
        "darija": "الغوات والزعيق بالغدايد والكلام القاصح فالمخاصمة.",
        "english": "to vociferate / yell angrily"
    },
    "pleureuses": {
        "type": "nom féminin pluriel",
        "fr_def": "Femmes engagées traditionnellement pour crier des lamentations et pleurer aux funérailles.",
        "arabic": "النواحات والندابات؛ نساء يبكين ويولولن في الجنائز بالأجرة.",
        "darija": "الندابات والنواحات لي كيجيو يبكيو ويولولو فالمياتا بالفلوس.",
        "english": "professional mourners / wailers"
    },
    "linceul": {
        "type": "nom masculin",
        "fr_def": "Pièce de toile blanche dans laquelle on enveloppe un cadavre avant la mise en terre (kafan).",
        "arabic": "الكفن الأبيض الذي يُلف فيه الميت قبل دفنه في القبر.",
        "darija": "الكفن الأبيض لي كيتكفن بيه الميت فاش كيموت.",
        "english": "shroud / winding sheet"
    },
    "fossoyeur": {
        "type": "nom masculin",
        "fr_def": "Personne chargée de creuser les tombes dans un cimetière.",
        "arabic": "حفار القبور الذي يهيئ اللحد لدفن الموتى في المقبرة.",
        "darija": "حفار القبور لي كيحفر القبر فالمقبرة للميتين.",
        "english": "gravedigger"
    },
    "zakat": {
        "type": "nom féminin",
        "fr_def": "Aumône légale obligatoire en islam, troisième pilier de la religion musulmane.",
        "arabic": "الزكاة المفروضة على أموال المسلمين لإعطائها للفقراء والمساكين.",
        "darija": "الزكاة لي فرضها ربي باش تعاون المساكين والمحتاجين.",
        "english": "zakat / Islamic obligatory alms"
    },
    "babouches": {
        "type": "nom féminin pluriel",
        "fr_def": "Chaussures traditionnelles marocaines sans quartiers ni talons, en cuir souple.",
        "arabic": "البَلْغة المغربية؛ حذاء جلدي تقليدي مسطح بدون كعب.",
        "darija": "البلغة المغربية ديال الجلد لي كيلبسوها الرجال والعيالات فالأعياد والجمعة.",
        "english": "traditional Moroccan slippers"
    },
    "marabout": {
        "type": "nom masculin",
        "fr_def": "Tombeau d'un saint homme musulman ou le saint personnage lui-même réputé pour sa piété.",
        "arabic": "المرابط أو الولي الصالح أو قبته المزارة للتبرك.",
        "darija": "السيد ولا الولي الصالح لي كيمشيو ليه الناس يزورو.",
        "english": "marabout / saint's shrine"
    },
    "solitude": {
        "type": "nom féminin",
        "fr_def": "État d'isolement physique ou affectif (thème majeur du narrateur Sidi Mohammed).",
        "arabic": "الوحدة والعزلة النفسية والشعور بالانفصال عن محيط الناس.",
        "darija": "الوحدانية والوحشة، فاش كيكون بنادم بوحدو سارح فخيالو بلا صحاب.",
        "english": "solitude / loneliness"
    },
    "commérages": {
        "type": "nom masculin pluriel",
        "fr_def": "Bavardages indiscrets, ragots futiles et médisances échangés par les voisines.",
        "arabic": "القال والقيل والنميمة والغيبة ونقل الأخبار السيئة بين الجيران.",
        "darija": "النميمة والهضرة فالناس وتقرقيب الناب بين الجارات.",
        "english": "gossip / idle talk"
    }
}

NEW_HUGO_WORDS = {
    "bicêtre": {
        "type": "nom propre",
        "fr_def": "Ancienne prison-hospice sinistre au sud de Paris réservée aux aliénés et aux condamnés à mort.",
        "arabic": "سجن بيسيتر؛ سجن ومصحة مرعبة تاريخية كان يُحتجز بها المحكومون بالإعدام في باريس.",
        "darija": "حبس بيسيطر، سجن قديم وقاصح فباريس كانو كيحطو فيه المحكومين بالإعدام قبل ما يقطعو ليهم الراس.",
        "english": "Bicêtre historic prison"
    },
    "échafaud": {
        "type": "nom masculin",
        "fr_def": "Estrade de bois surélevée où est dressée la guillotine pour exécuter publiquement les condamnés.",
        "arabic": "منصة الإعدام الخشبية المرتفعة التي تُنصب عليها المقصلة أمام الجماهير.",
        "darija": "منصة الإعدام الخشبية العالية فين كيحطو المقصلة قدام الناس فالساحة.",
        "english": "scaffold"
    },
    "pourvoi": {
        "type": "nom masculin",
        "fr_def": "Recours juridique suprême formé devant la Cour de cassation pour contester la légalité du jugement.",
        "arabic": "الطعن بالنقض؛ إجراء قانوني أخير لإلغاء الحكم القضائي.",
        "darija": "الطعن فالنقض، آخر طلب كيدير المحامي فالمحكمة العليا باش يبطل حكم الإعدام.",
        "english": "appeal in cassation"
    },
    "grâce": {
        "type": "nom féminin",
        "fr_def": "Pardon royal ou présidentiel annulant ou réduisant la peine de mort d'un condamné.",
        "arabic": "العفو الملكي أو الرئاسي الذي يُسقط عقوبة الإعدام وينقذ حياة المحكوم.",
        "darija": "العفو الملكي، المسامحة الرسمية لي كتعتق رقبة المحكوم بالإعدام من الموت.",
        "english": "royal pardon / clemency"
    },
    "bourreau": {
        "type": "nom masculin",
        "fr_def": "Exécuteur des arrêts criminels, l'homme chargé d'actionner la guillotine (souvent appelé Samson).",
        "arabic": "الجلاد أو السياف المكلف بإنزال شفرة الإعدام على رقاب المحكومين.",
        "darija": "الجلاد، الشخص لي مكلف يقطع الراس بالمقصلة وينفذ حكم الإعدام.",
        "english": "executioner / headsman"
    },
    "guichetier": {
        "type": "nom masculin",
        "fr_def": "Gardien de prison qui surveille les cellules et garde les clés des grilles.",
        "arabic": "حارس الزنزانة أو السجان المكلف بفتح وإغلاق أبواب السجن وحراسة السجناء.",
        "darija": "السجان ولا العساس ديال الكاشو لي عندو السوارت ديال الحبس.",
        "english": "prison turnkey / jailer"
    },
    "ferrements": {
        "type": "nom masculin pluriel",
        "fr_def": "Cérémonie brutale où l'on enchaîne les forçats au cou et aux chevilles avant leur départ pour le bagne.",
        "arabic": "طقس تقييد المساجين وتصفيح السلاسل الثقيلة حول أعناقهم وأرجلهم لترحيلهم للأشغال الشاقة.",
        "darija": "التقييد بالسلاسل والحديد التقيل على العنق والرجلين للمحكومين بالأشغال الشاقة.",
        "english": "shackling / irons ceremony"
    },
    "conciergerie": {
        "type": "nom propre",
        "fr_def": "Ancienne prison royale de Paris sur l'île de la Cité où sont transférés les condamnés avant l'échafaud.",
        "arabic": "سجن الكونسيرجيري؛ السجن التاريخي الذي يقضي فيه المحكوم ساعاته الأخيرة قبل السير للإعدام.",
        "darija": "حبس الكونسيرجيري فقلب باريس، فين كيدوز المحكوم آخر سوايع فحياتو قبل ما يديوه لساحة الݣريف.",
        "english": "Conciergerie prison"
    },
    "charrette": {
        "type": "nom féminin",
        "fr_def": "Voiture à deux roues traînée par un cheval transportant le condamné les mains liées vers la place d'exécution.",
        "arabic": "عربة الإعدام المكشوفة التي تنقل المحكوم المغلول اليدين وسط الجماهير.",
        "darija": "الكروصة ولا العربة لي كيركبو فيها المحكوم مكتف باش يديوه قدام الناس للساحة يتعدم.",
        "english": "tumbril / execution cart"
    },
    "toilette": {
        "type": "nom féminin",
        "fr_def": "Préparation lugubre du condamné : le bourreau lui coupe les cheveux et le col de chemise pour dégager le cou.",
        "arabic": "تواليت الإعدام؛ الطقس الجنائزي المرعب لقص شعر المحكوم وياقة قميصه لكشف رقبته أمام الشفرة.",
        "darija": "طقس التحضير للإعدام، فاش الجلاد كيقطع للمحكوم الشعر والياقة باش العنق يبقى عريان للمقصلة.",
        "english": "toilet of the condemned"
    },
    "grève": {
        "type": "nom propre (Place de Grève)",
        "fr_def": "Célèbre place parisienne (actuelle place de l'Hôtel-de-Ville) où avaient lieu les exécutions capitales publiques.",
        "arabic": "ساحة الإضراب (ساحة لاغريف)؛ الساحة التاريخية في باريس المخصصة لتنفيذ الإعدامات العلنية.",
        "darija": "ساحة لاݣريف فباريس، الساحة لي كانو كيعدمو فيها بنادم قدام عامة الشعب.",
        "english": "Place de Grève execution square"
    },
    "cachot": {
        "type": "nom masculin",
        "fr_def": "Cellule souterraine étroite, humide, sombre et dépourvue de lumière où l'on enferme les prisonniers.",
        "arabic": "الزنزانة الانفرادية أو القبو المعتم المظلم الرطب في قاع السجن.",
        "darija": "الكاشو، زنزانة تحت الأرض مظلمة وفازݣة وخانزة فين كيتسد على المحكوم بوحدو.",
        "english": "dungeon / solitary cell"
    },
    "forçats": {
        "type": "nom masculin pluriel",
        "fr_def": "Criminels condamnés aux peines de travaux forcés et expédiés au bagne de Toulon ou Brest.",
        "arabic": "المحكومون بالأشغال الشاقة المؤبدة أو المؤقتة المصفدون بالحديد.",
        "darija": "المحبوسين ديال الأشغال الشاقة لي كيمشيو محكومين يخدمو بالسلاسل فالبحر.",
        "english": "convicts / galley slaves"
    },
    "spectre": {
        "type": "nom masculin",
        "fr_def": "Apparition fantomatique effrayante ; hantise obsédante de la mort qui ne quitte plus l'esprit du condamné.",
        "arabic": "الشبح أو الطيف المخيف؛ الفكرة الكابوسية القاتلة التي تطارد عقل المحكوم ليلاً ونهاراً.",
        "darija": "الخيال ولا الشبح المفزع لي كيدور فراس المحكوم وما كيخليهش ينعس من الخوف.",
        "english": "specter / phantom"
    },
    "agonie": {
        "type": "nom féminin",
        "fr_def": "Période de souffrance physique et morale précédant immédiatement l'instant de la mort.",
        "arabic": "الاحتضار أو سكرات الموت والعذاب النفسي والجسدي الأخير.",
        "darija": "سكرات الموت والعذاب الأخير فاش الروح كتبغي تخرج ولا بنادم قرب يتعدم.",
        "english": "agony / death throes"
    }
}

def update_dictionaries():
    # 1. Update Boite
    b_path = 'data/la_boite_a_merveilles/dictionary.json'
    with open(b_path, 'r', encoding='utf-8') as f:
        boite_dict = json.load(f)
    
    for word, data in NEW_BOITE_WORDS.items():
        boite_dict[word] = data
    
    with open(b_path, 'w', encoding='utf-8') as f:
        json.dump(boite_dict, f, ensure_ascii=False, indent=2)
    print(f"Updated Boite dictionary: {len(boite_dict)} words.")

    # 2. Update Hugo
    h_path = 'data/le_dernier_jour_dun_condamne/dictionary.json'
    with open(h_path, 'r', encoding='utf-8') as f:
        hugo_dict = json.load(f)
    
    for word, data in NEW_HUGO_WORDS.items():
        hugo_dict[word] = data
            
    with open(h_path, 'w', encoding='utf-8') as f:
        json.dump(hugo_dict, f, ensure_ascii=False, indent=2)
    print(f"Updated Hugo dictionary: {len(hugo_dict)} words.")

if __name__ == '__main__':
    update_dictionaries()
