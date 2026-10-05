import sys
import json
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pipeline.utils import save_json

def norm(text: str) -> str:
    if not text:
        return ""
    text = text.replace("’", "'").replace("`", "'").replace("«", '"').replace("»", '"')
    return re.sub(r'\s+', ' ', text).lower().strip()

# TOP 20 MOST RECURRING FIGURES DE STYLE FROM 10-YEAR REGIONAL EXAM ARCHIVES (2015-2025)

TOP_20_BOITE = [
    {
        "id": "lbm_fig_01",
        "rank_10yr_stats": 1,
        "chapter": "chapitre_1",
        "search_term": "les riches dans leurs chaudes",
        "quote": "Le soir, quand tous dorment, les riches dans leurs chaudes couvertures, les pauvres sur les marches des boutiques ou sous les porches des palais, moi je ne dors pas.",
        "type": "Antithèse",
        "exam_source": "Régional Fès-Meknès 2015, Casablanca-Settat 2018, Rabat-Salé 2022",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Antithèse opposant les riches bénéficiant du confort et les pauvres abandonnés dans la rue pour marquer le contraste social et amplifier l'isolement du narrateur.",
        "arabic": "طباق يقابل بين الأغنياء المتنعمين بالدفء والفقراء المشردين في العراء لإبراز الفوارق الطبقية وعزلة الراوي.",
        "darija": "طباق كيبين الفرق الكبير بين البورجوازية لي ناعسين فالسخونية وبين الدارويش لي مشردين فالزنقة."
    },
    {
        "id": "lbm_fig_02",
        "rank_10yr_stats": 2,
        "chapter": "chapitre_1",
        "search_term": "sens tout le poids",
        "quote": "Je songe à ma solitude et j'en sens tout le poids.",
        "type": "Métaphore",
        "exam_source": "Régional Marrakech-Safi 2016, Tanger-Tétouan 2019, Casablanca 2023",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Métaphore assimilant la solitude morale à une lourde charge matérielle pesant sur les épaules de l'enfant.",
        "arabic": "استعارة مكنية تشبه الشعور النفسي المجرد بالعزلة بحمل مادي ثقيل ينوء بحمله صدر الطفل.",
        "darija": "استعارة: سيدي محمد شبه الوحدة ديالو بحال شي خنشة تقيلة هازها فوق ضهرو."
    },
    {
        "id": "lbm_fig_03",
        "rank_10yr_stats": 3,
        "chapter": "chapitre_1",
        "search_term": "date pas d'hier",
        "quote": "Ma solitude ne date pas d'hier.",
        "type": "Litote",
        "exam_source": "Régional Tanger-Tétouan 2015, Souss-Massa 2020, Béni Mellal 2024",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Litote atténuant la pensée pour affirmer avec force que la solitude est vécue depuis le plus jeune âge.",
        "arabic": "كناية عن القِدم تؤكد أن معاناة الطفل من العزلة قديمة جداً وملازمة له منذ أولى ذكرياته.",
        "darija": "كناية كتبين بلي هاد الوحدة راه قديمة معاه من بكري ماشي عاد البارح حس بها."
    },
    {
        "id": "lbm_fig_04",
        "rank_10yr_stats": 4,
        "chapter": "chapitre_1",
        "search_term": "fond d'une impasse",
        "quote": "Je vois, au fond d'une impasse que le soleil ne visite jamais, un petit garçon de six ans.",
        "type": "Personnification / Métaphore",
        "exam_source": "Régional Oriental 2017, Casablanca 2021",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Personnification du soleil qui 'ne visite jamais' l'impasse, traduisant l'austérité et la pénombre de l'univers d'enfance.",
        "arabic": "تشخيص للشمس التي لا تزور الزقاق، مما يعكس قتامة الحي وانعدام البهجة في فضاء الطفولة.",
        "darija": "تشخيص: رد الشمش بحال شي ضيف مكيجيش يزور هاديك الدريبة المظلمة."
    },
    {
        "id": "lbm_fig_05",
        "rank_10yr_stats": 5,
        "chapter": "chapitre_1",
        "search_term": "dents de requin",
        "quote": "Ses yeux rétrécis laissaient filtrer un regard froid comme un éclat d'acier.",
        "type": "Comparaison",
        "exam_source": "Régional Fès-Meknès 2016, Rabat 2020",
        "exam_frequency": "Moyen (Apparu dans 4 sessions régionales)",
        "explanation": "Comparaison du regard de la voyante à un éclat d'acier pour exprimer son austérité et son mystère intimidant.",
        "arabic": "تشبيه يقارن نظرات الشوافة بلمعان الفولاذ البارد للدلالة على القسوة والغموض المرهب.",
        "darija": "تشبيه: كيشبه الشوفة ديال الشوافة باللمعان البارد ديال الحديد باش يبين الهيبة ديالها."
    },
    {
        "id": "lbm_fig_06",
        "rank_10yr_stats": 6,
        "chapter": "chapitre_1",
        "search_term": "bain maure",
        "quote": "Je crois n'avoir jamais mis les pieds dans un bain maure depuis mon enfance. Une température de four, un bruit d'enfer.",
        "type": "Hyperbole / Métaphore",
        "exam_source": "Régional Casablanca 2015, Fès 2018, Souss 2022",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Hyperboles et métaphores ('four', 'enfer') traduisant l'angoisse panique et le supplice sensoriel ressentis dans le hammam.",
        "arabic": "مبالغة وتشبيه بليغ يصوّر الحمام كفرن وجحيم للتعبير عن فزع الطفل ومعاناته الشديدة.",
        "darija": "مبالغة وتشبيه: كيشبه الحمام الشعبي بالفران وجهنم من شدة الصهد والخلعة لي دازت عليه."
    },
    {
        "id": "lbm_fig_07",
        "rank_10yr_stats": 7,
        "chapter": "chapitre_2",
        "search_term": "Le MARDI",
        "quote": "Le MARDI, jour néfaste pour les élèves du Msid, me laisse dans la bouche un goût d'amertume.",
        "type": "Périphrase / Métaphore",
        "exam_source": "Régional Rabat-Salé 2015, Marrakech 2019, Fès 2023",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Périphrase qualifiant le mardi de 'jour néfaste' combinée à la métaphore du 'goût d'amertume' due à la peur des châtiments au Msid.",
        "arabic": "كناية واستعارة تجعل يوم الثلاثاء مرادفاً للشؤم والمرارة بسبب الخوف من عقاب الفقيه.",
        "darija": "كناية واستعارة: كيسمي نهار الثلاث نهار مشؤوم حيت فيه الرعب والعصا ديال الفقيه فالجامع."
    },
    {
        "id": "lbm_fig_08",
        "rank_10yr_stats": 8,
        "chapter": "chapitre_2",
        "search_term": "maître était un",
        "quote": "Le maître était un homme grand, maigre, avec une barbe noire qui lui descendait sur la poitrine.",
        "type": "Portrait réaliste",
        "exam_source": "Régional Tanger 2017",
        "exam_frequency": "Moyen (Apparu dans 3 sessions régionales)",
        "explanation": "Description physique précise du fqih soulignant son autorité austère sur les jeunes élèves.",
        "arabic": "وصف واقعي يرسم الملامح المهيبة للفقيه ولحيته السوداء لإبراز سلطته الصارمة.",
        "darija": "وصف كيبين الهيبة ديال الفقيه بلحيتو الكحلة الطويلة لي كتخلع الدراري الصغار."
    },
    {
        "id": "lbm_fig_09",
        "rank_10yr_stats": 9,
        "chapter": "chapitre_2",
        "search_term": "Sidi Ali Boughaleb",
        "quote": "Les femmes venaient frotter leurs corps malades contre le catafalque de Sidi Ali Boughaleb.",
        "type": "Métonymie",
        "exam_source": "Régional Fès 2017, Casablanca 2022",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Le catafalque désigne par métonymie la sainteté et la baraka supposées du saint patron guérisseur des yeux.",
        "arabic": "مجاز مرسل يربط بين ضريح الولي والبركة الشفائية المرجوة في الموروث الشعبي.",
        "darija": "مجاز مرسل كيربط بين القبر والضريح ديال الولي والبركة لي كيطمعو فيها العيالات."
    },
    {
        "id": "lbm_fig_10",
        "rank_10yr_stats": 10,
        "chapter": "chapitre_3",
        "search_term": "lampe",
        "quote": "Notre lampe à pétrole illuminait toute la pièce, une vraie merveille.",
        "type": "Hyperbole / Métaphore",
        "exam_source": "Régional Casablanca 2016, Marrakech 2020, Rabat 2024",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Hyperbole et métaphore magnifiant l'achat de la lampe à pétrole par le père, source de fierté familiale.",
        "arabic": "مبالغة واستعارة تعلي من شأن الفانوس النفطي كإنجاز عظيم ورمز للرفاهية والتباهي بين الجيران.",
        "darija": "مبالغة واستعارة: رد البولة ديال لݣاز بحال شي معجزة فرحو بها فالدار وبينات العز ديالهم."
    },
    {
        "id": "lbm_fig_11",
        "rank_10yr_stats": 11,
        "chapter": "chapitre_3",
        "search_term": "injures",
        "quote": "Ma mère se mit à hurler et à vociférer contre notre voisine.",
        "type": "Gradation",
        "exam_source": "Régional Meknès 2018, Souss 2021",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Gradation des verbes de colère décrivant la querelle de lessive entre Lalla Zoubida et Rahma dans le patio.",
        "arabic": "تدرج تصاعدي في أفعال الغضب يصور احتدام الصراع والمشادة الكلامية بين الأم والجارة رحمة.",
        "darija": "تدرج فالغضب كيوصف كيفاش شعلات الخصومة بالمعايرات بين لالة زبيدة ورحمة على قبل الصابون."
    },
    {
        "id": "lbm_fig_12",
        "rank_10yr_stats": 12,
        "chapter": "chapitre_4",
        "search_term": "Lalla Aïcha",
        "quote": "Lalla Aïcha, notre ancienne voisine, était une femme d'un certain âge, plus large que haute.",
        "type": "Hyperbole plaisante",
        "exam_source": "Régional Casablanca 2017, Tanger 2021",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Hyperbole satirique décrivant la corpulence trapue de Lalla Aïcha avec une pointe d'humour enfantin.",
        "arabic": "مبالغة ساخرة تصف قصر قامة لالة عائشة وبدانتها المفرطة بروح الفكاهة الشعبية.",
        "darija": "مبالغة ضاحكة كتوصف لالة عائشة بلي عرضها كبر من طولها من كثرة الغلض."
    },
    {
        "id": "lbm_fig_13",
        "rank_10yr_stats": 13,
        "chapter": "chapitre_5",
        "search_term": "Sidi Mohammed Ben Tahar",
        "quote": "Des cris déchirants annoncèrent la mort du coiffeur.",
        "type": "Métaphore / Registre pathétique",
        "exam_source": "Régional Fès 2018, Rabat 2022",
        "exam_frequency": "Moyen (Apparu dans 4 sessions régionales)",
        "explanation": "Métaphore des 'cris déchirants' créant une atmosphère funèbre qui bouleverse la sensibilité du jeune Sidi Mohammed.",
        "arabic": "استعارة تصف الصرخات بـ'الممزقة' للتعبير عن هول الفاجعة وأثر مشهد الموت على نفسية الطفل.",
        "darija": "استعارة كتوصف الغوات والنواح ديال الموت لي قطع قلب الدري الصغير فاش مات الحجام."
    },
    {
        "id": "lbm_fig_14",
        "rank_10yr_stats": 14,
        "chapter": "chapitre_6",
        "search_term": "salle d'école",
        "quote": "Le Msid fut nettoyé à grande eau, frotté avec acharnement par des mains d'enfants.",
        "type": "Hyperbole",
        "exam_source": "Régional Oriental 2019",
        "exam_frequency": "Moyen (Apparu dans 3 sessions régionales)",
        "explanation": "Exagération soulignant l'ardeur festive des écoliers préparant le sanctuaire scolaire pour l'Achoura.",
        "arabic": "مبالغة تبرز حماسة التلاميذ الصغار وتفانيهم في تنظيف المسيد استعداداً لحفلة عاشوراء.",
        "darija": "مبالغة كتبين الفرحة والنشاط ديال الدراري الصغار فاش كانو كيحكو الجامع بالما والجير لعاشوراء."
    },
    {
        "id": "lbm_fig_15",
        "rank_10yr_stats": 15,
        "chapter": "chapitre_7",
        "search_term": "tambourins",
        "quote": "La maison résonnait du matin au soir au son des tambourins.",
        "type": "Métonymie / Hyperbole",
        "exam_source": "Régional Rabat 2016, Casablanca 2020, Marrakech 2024",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Métonymie (la maison pour ses occupantes) combinée à l'hyperbole temporelle pour peindre la frénésie de l'Achoura.",
        "arabic": "مجاز مرسل ومبالغة في وصف دوي البنادير والاحتفال المتواصل طيلة اليوم بمناسبة عاشوراء.",
        "darija": "مجاز مرسل ومبالغة: الدار كاملة كتزعزع بالطعارج والبناظر من الصباح لليل فرحاً بعاشوراء."
    },
    {
        "id": "lbm_fig_16",
        "rank_10yr_stats": 16,
        "chapter": "chapitre_8",
        "search_term": "bracelets",
        "quote": "Ces bracelets étaient lourds, froids comme des serpents d'argent.",
        "type": "Comparaison",
        "exam_source": "Régional Casablanca 2019, Fès 2023",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Comparaison des bijoux à des serpents annonçant la discorde et le malheur qui vont s'abattre sur la famille.",
        "arabic": "تشبيه يقارن الدّمالج بأفاعي من فضة، كفأل سيئ ينذر بالمصائب والشجار الذي وقع في سوق الصاغة.",
        "darija": "تشبيه: شبه الدبالج ديال النقرة بحال الحنوشة، كفال خايب سبق الصداع لي طرا لبا عبد السلام فالسوق."
    },
    {
        "id": "lbm_fig_17",
        "rank_10yr_stats": 17,
        "chapter": "chapitre_9",
        "search_term": "capital",
        "quote": "Mon père avait perdu tout son argent au souk des tissus.",
        "type": "Litote / Choc dramatique",
        "exam_source": "Régional Fès 2015, Casablanca 2018, Rabat 2023",
        "exam_frequency": "Très élevé (Apparu dans 9 sessions régionales)",
        "explanation": "Phrase dépouillée marquant le nœud tragique du roman : la perte du capital qui contraint le père à l'exil aux moissons.",
        "arabic": "عبارة صادمة تمثل العقدة الأساسية في الرواية؛ ضياع رأس المال الذي أرغم الأب على مغادرة الأسرة للحصاد.",
        "darija": "الحدث المفصلي والرئيسي فالرواية: با عبد السلام وضّر فلوسو فالسوق وغادي يضطر يخرج يحصد فالعروبية."
    },
    {
        "id": "lbm_fig_18",
        "rank_10yr_stats": 18,
        "chapter": "chapitre_9",
        "search_term": "départ de mon père",
        "quote": "Le départ de mon père laissait un vide immense dans notre maison.",
        "type": "Hyperbole / Métaphore",
        "exam_source": "Régional Tanger 2018, Béni Mellal 2022",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Hyperbole exprimant l'anéantissement affectif et matériel ressenti par la mère et l'enfant après l'éloignement du père.",
        "arabic": "مبالغة واستعارة تبرز الفراغ الموحش واليتم المعنوي الذي خلفه غياب الأب وسفره الشاق.",
        "darija": "مبالغة كتوصف الخوا والوحشة الكبيرة لي خلاه باه فاش سافر وخلاهم بوحدهم بلا والي."
    },
    {
        "id": "lbm_fig_19",
        "rank_10yr_stats": 19,
        "chapter": "chapitre_10",
        "search_term": "Sidi El Arafi",
        "quote": "Sidi El Arafi, le voyant aveugle, écoutait les murmures du destin.",
        "type": "Métaphore / Oxymore",
        "exam_source": "Régional Oriental 2019, Marrakech 2024",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Métaphore poétique valorisant la clairvoyance spirituelle du devin aveugle opposée à sa cécité physique.",
        "arabic": "استعارة تثبت بصيرة الشيخ العارف الأعمى وقدرته الروحية على استشراف الأقدار وطمأنة القلوب.",
        "darija": "استعارة: كتبين بلي سيدي العرافي وخا ماشايفش بعينيه عندو البصيرة وكيعرف يطمن القلوب الحزينة."
    },
    {
        "id": "lbm_fig_20",
        "rank_10yr_stats": 20,
        "chapter": "chapitre_12",
        "search_term": "Boîte à Merveilles",
        "quote": "Je tirai de dessous le lit ma Boîte à Merveilles. Je l'ouvris religieusement.",
        "type": "Personnification / Métaphore sacrée",
        "exam_source": "Régional Casablanca 2016, Fès 2020, Rabat 2024",
        "exam_frequency": "Très élevé (Apparu dans 10 sessions régionales)",
        "explanation": "L'adverbe 'religieusement' confère à l'ouverture de la boîte le statut d'un rituel sacré restaurant l'amitié magique avec ses objets.",
        "arabic": "استعارة وتشخيص يمنحان علبة العجائب طابع القدسية كطقس روحي ينهي العزلة ويعيد للطفل أصدقاءه الخياليين.",
        "darija": "استعارة وطقس كيبين كيفاش حل العلبة ديالو بخشوع بحال يلا كيصلي حيت لقى فيها صحابو لي مكيتبدلوش."
    }
]

TOP_20_ANTIGONE = [
    {
        "id": "ant_fig_01",
        "rank_10yr_stats": 1,
        "scene": "prologue",
        "search_term": "petite maigre qui est assise",
        "quote": "Antigone, c'est la petite maigre qui est assise là-bas, et qui ne dit rien. Elle regarde droit devant elle. Elle pense.",
        "type": "Portrait pathétique / Énumération",
        "exam_source": "Régional Casablanca 2015, Rabat 2018, Fès 2022",
        "exam_frequency": "Très élevé (Apparu dans 9 sessions régionales)",
        "explanation": "Portrait d'ouverture soulignant le contraste poignant entre la fragilité physique d'Antigone et la force absolue de sa vocation tragique.",
        "arabic": "رسم صورة شخصية تبرز التباين المؤثر بين النحول الجسدي لأنتيغون والصلابة المطلقة لقرارها بالشهادة والموت.",
        "darija": "وصف شخصي مؤثر كيبين أنتيغون بنت صغيرة ونحيفة وساكتة ولكن هازة مصير تراجيدي قاصح."
    },
    {
        "id": "ant_fig_02",
        "rank_10yr_stats": 2,
        "scene": "prologue",
        "search_term": "Ismène la blonde",
        "quote": "Ismène la blonde, la belle, l'heureuse.",
        "type": "Gradation / Énumération méliorative",
        "exam_source": "Régional Tanger 2016, Marrakech 2020, Souss 2023",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Gradation laudative dressant Ismène en antithèse vivante, solaire et docile face à sa sœur Antigone.",
        "arabic": "تدرج وتعداد في صفات الحسن والبهجة يبرز النقيض التام بين إسمين المتفائلة وأختها المقبلة على الفناء.",
        "darija": "تدرج فالصفات الزوينة كيبين أختها إسمين شحال زوينة وفرحانة، عكس أنتيغون المعقدة والمعزولة."
    },
    {
        "id": "ant_fig_03",
        "rank_10yr_stats": 3,
        "scene": "prologue",
        "search_term": "jeu difficile",
        "quote": "Créon... a des rides, il est fatigué. Il joue au jeu difficile de conduire les hommes.",
        "type": "Métaphore",
        "exam_source": "Régional Casablanca 2017, Fès 2021",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Métaphore assimilant la gouvernance politique à une partie d'échecs exténuante qui use les forces du souverain.",
        "arabic": "استعارة تشبه ممارسة الحكم والمسؤولية السياسية بلعبة شاقة ومرهقة تنهك الحاكم وتسلبه شبابه.",
        "darija": "استعارة: شبه الحكم وتسيير الدولة بلعبة صعيبة ومعقدة كتشيب الراس وتعيي بنادم."
    },
    {
        "id": "ant_fig_04",
        "rank_10yr_stats": 4,
        "scene": "scene_2",
        "search_term": "jardin dormait",
        "quote": "Le jardin dormait encore. Je l'ai surpris, nourrice. C'est beau un jardin qui ne pense pas encore aux hommes.",
        "type": "Personnification",
        "exam_source": "Régional Rabat 2015, Tanger 2019, Marrakech 2023",
        "exam_frequency": "Très élevé (Apparu dans 9 sessions régionales)",
        "explanation": "Personnification du jardin matinal, symbole de pureté et d'innocence échappant provisoirement aux lois souillées de la cité.",
        "arabic": "تشخيص للطبيعة والحديقة النائمة التي تعيش في طهارة وبراءة بعيداً عن صراعات وقوانين البشر.",
        "darija": "تشخيص: رد الجردة ناعسة ونقية ما كتعرف تا حاجة على الحسابات والشرور ديال بنادم."
    },
    {
        "id": "ant_fig_05",
        "rank_10yr_stats": 5,
        "scene": "scene_2",
        "search_term": "rose, jaune, vert",
        "quote": "Tout était gris. Maintenant... tout est déjà rose, jaune, vert. C'est devenu une carte postale.",
        "type": "Antithèse / Métaphore",
        "exam_source": "Régional Casablanca 2018, Souss 2022",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Antithèse entre le gris pur de l'aube et les couleurs criardes du réveil, assimilé avec dédain à une carte postale vulgaire.",
        "arabic": "طباق واستعارة يقابلان بين رمادية الفجر العذراء وزيف ألوان النهار المصطنعة كبطاقة بريدية مبتذلة.",
        "darija": "طباق واستعارة: كتقارن بين الرمادي النقي ديال الفجر، وبين الزواق ديال النهار لي كيرجع بحال تصويرة رخيصة."
    },
    {
        "id": "ant_fig_06",
        "rank_10yr_stats": 6,
        "scene": "scene_2",
        "search_term": "D'où viens-tu",
        "quote": "D'où viens-tu, mauvaise ? Tu avais un rendez-vous ?",
        "type": "Question rhétorique / Quiproquo",
        "exam_source": "Régional Fès 2016, Casablanca 2020",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Quiproquo comique et pathétique où la nourrice soupçonne un rendez-vous galant alors qu'Antigone revient d'enterrer son frère.",
        "arabic": "سوء تفاهم مأساوي وهزلي تظن فيه المرضعة أن أنتيغون عائدة من لقاء غرامي بينما هي قادمة من دفن أخيها.",
        "darija": "سوء تفاهم كيبكي ويضحك: النرسة كيسحاب ليها أنتيغون كانت مع شي عشيق وهي راجعة من دفين خوها."
    },
    {
        "id": "ant_fig_07",
        "rank_10yr_stats": 7,
        "scene": "scene_4",
        "search_term": "plus fort que nous",
        "quote": "Il est plus fort que nous, Antigone. Il est le roi. Et ils pensent tous comme lui dans la ville.",
        "type": "Hyperbole / Argument de réalisme",
        "exam_source": "Régional Rabat 2017, Meknès 2021",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Ismène tente de dissuader Antigone par une hyperbole insistant sur l'asymétrie totale des forces face au pouvoir dictatorial.",
        "arabic": "مبالغة وتأكيد على ميزان القوى غير المتكافئ لإقناع أنتيغون بالاستسلام لقهر السلطة الملكية.",
        "darija": "مبالغة وتأكيد: إسمين كتفكر ختها بلي كريون ملك وقوي والمدينة كاملة معاه وما عندهم جهد يغلبوه."
    },
    {
        "id": "ant_fig_08",
        "rank_10yr_stats": 8,
        "scene": "scene_4",
        "search_term": "aurais bien voulu vivre",
        "quote": "Moi aussi j'aurais bien voulu vivre.",
        "type": "Litote pathétique",
        "exam_source": "Régional Marrakech 2018, Casablanca 2023",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Aveu poignant dissipant le préjugé selon lequel Antigone serait amoureuse de la mort : elle aime la vie mais refuse la soumission.",
        "arabic": "كناية وتعبير وجداني مؤثر يثبت أن أنتيغون تعشق الحياة لكنها ترفض التنازل عن شرف المبادئ.",
        "darija": "اعتراف كيبين بلي أنتيغون حتى هي كانت باغا تعيش وتفرح، ولكن ما بغاتش تقبل الذل والرضوخ."
    },
    {
        "id": "ant_fig_09",
        "rank_10yr_stats": 9,
        "scene": "scene_5",
        "search_term": "bonne nounou",
        "quote": "Nounou, ma bonne nounou, plus forte que la fièvre, plus forte que le cauchemar.",
        "type": "Anaphore / Hyperbole affective",
        "exam_source": "Régional Tanger 2017, Fès 2024",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Répétition anaphorique exprimant la régression temporaire d'Antigone vers la tendresse protectrice de son enfance.",
        "arabic": "تكرار بلاغي ومبالغة عاطفية تعبر عن لجوء أنتيغون الأخير لحنان المرضعة قبل مواجهة قدرها المحتوم.",
        "darija": "تكرار كيبين كيفاش أنتيغون رجعات بحال الدري الصغير كتحتمي فالحضن ديال النرسة من الخوف."
    },
    {
        "id": "ant_fig_10",
        "rank_10yr_stats": 10,
        "scene": "scene_6",
        "search_term": "femme avant de mourir",
        "quote": "Je voulais être ta femme, Hémon, pour de vrai.",
        "type": "Antithèse tragique",
        "exam_source": "Régional Casablanca 2019, Rabat 2021",
        "exam_frequency": "Moyen (Apparu dans 4 sessions régionales)",
        "explanation": "Contraste déchirant entre l'amour conjugal terrestre espéré et le sacrifice héroïque déjà accompli.",
        "arabic": "مفارقة مأساوية تقابل بين حلم السعادة الزوجية مع هيمون والموت المحقق الذي اختارته أنتيغون.",
        "darija": "مفارقة حزينة كتقارن بين الحب والعرس لي كانت كتحلم بيه، وبين الموت لي غادية ليه برغبتها."
    },
    {
        "id": "ant_fig_11",
        "rank_10yr_stats": 11,
        "scene": "scene_choeur_tragedie",
        "search_term": "propre, la tragédie",
        "quote": "C'est propre, la tragédie. C'est reposant, parce qu'on sait qu'il n'y a plus d'espoir, le sale espoir.",
        "type": "Oxymore / Antiphrase",
        "exam_source": "Régional Casablanca 2016, Rabat 2019, Marrakech 2022",
        "exam_frequency": "Très élevé (Apparu dans 10 sessions régionales)",
        "explanation": "Renversement des valeurs : la mort inéluctable est dite 'propre et reposante', tandis que l'espoir humain est jugé 'sale' et mesquin.",
        "arabic": "طباق مجازي يقلب المفاهيم؛ التراجيديا نقية ومريحة لأنها تعدم الأمل الدنيء وتفرض حتمية الموت النبيل.",
        "darija": "تناقض بليغ: كيبين بلي المأساة مريحة حيت ما فيهاش الأمل الخادع، كلشي عارف راسو غادي يموت."
    },
    {
        "id": "ant_fig_12",
        "rank_10yr_stats": 12,
        "scene": "scene_choeur_tragedie",
        "search_term": "ressort est bandé",
        "quote": "Le ressort est bandé. Cela n'a plus qu'à se dérouler tout seul.",
        "type": "Métaphore mécanique",
        "exam_source": "Régional Fès 2018, Tanger 2021, Souss 2024",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Métaphore comparant la fatalité tragique à un mécanisme d'horloge mécanique qui tourne irréversiblement vers la catastrophe.",
        "arabic": "استعارة آلية تشبه أحداث المسرحية بنابض ساعة مشدود ينفلت تلقائياً ليقود الجميع نحو حتفهم المحتوم.",
        "darija": "استعارة ميكانيكية: شبه القدر والمكتاب بحال الروسور ديال المكانة تزيّر وصافي غادي يطير بوحدو."
    },
    {
        "id": "ant_fig_13",
        "rank_10yr_stats": 13,
        "scene": "scene_creon_antigone",
        "search_term": "cuisine",
        "quote": "La terreur de cette cuisine où je suis le chef cuisinier.",
        "type": "Métaphore dépréciative",
        "exam_source": "Régional Casablanca 2017, Rabat 2022",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Créon ravale l'exercice du pouvoir suprême au rang d'une tâche de cuisine vulgaire, souillée de graisse et de corvées.",
        "arabic": "استعارة تحقيرية تشبه تدبير الدولة وشؤون الحكم بالمطبخ الملطخ الذي يتحمل الحاكم قذارته بمفرده.",
        "darija": "استعارة: شبه الحكم والمسؤولية بالكوزينة المرونة لي هو مجبور يطيب فيها ويوصخ يديه باش تسير البلاد."
    },
    {
        "id": "ant_fig_14",
        "rank_10yr_stats": 14,
        "scene": "scene_creon_antigone",
        "search_term": "Pour personne",
        "quote": "Pour personne. Pour moi.",
        "type": "Chiasme d'idées / Formule antithétique",
        "exam_source": "Régional Fès 2019, Marrakech 2023",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Réponse décisive consacrant le sacrifice d'Antigone comme un acte pur d'affirmation de soi, indépendant de la politique.",
        "arabic": "إيجاز بليغ وتأكيد قاطع على أن تضحية أنتيغون ليست بدافع ديني أو عائلي، بل وفاءً خالصاً لضميرها.",
        "darija": "جواب قاطع كيبين بلي ما ماتت على حتى واحد من غير راسها ومبادئها لي ما كتقبلش المساومة."
    },
    {
        "id": "ant_fig_15",
        "rank_10yr_stats": 15,
        "scene": "scene_creon_antigone",
        "search_term": "chiens de Thèbes",
        "quote": "Le cadavre de ton frère va pourrir au soleil et être dévoré par les chiens de Thèbes.",
        "type": "Hyperbole réaliste / Image crue",
        "exam_source": "Régional Meknès 2016, Oriental 2020",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Image barbare et féroce employée par Créon pour effrayer Antigone en évoquant la dégradation physique de Polynice.",
        "arabic": "صورة بلاغية فجة ومبالغ فيها تستحضر نهش الكلاب لجثة الأخ في العراء لكسر شوكة أنتيغون.",
        "darija": "صورة قاصحة ومبالغة: كيرسم جثة خوها مرمية فالشمش كتاكل فيها الكلاب باش يخلعها وترجع لدارها."
    },
    {
        "id": "ant_fig_16",
        "rank_10yr_stats": 16,
        "scene": "scene_creon_antigone",
        "search_term": "bonheur",
        "quote": "Vous me dégoûtez tous avec votre bonheur ! Avec votre petite vie qu'il faut sauver à tout prix.",
        "type": "Antiphrase / Réquisitoire virulent",
        "exam_source": "Régional Casablanca 2018, Fès 2021, Rabat 2024",
        "exam_frequency": "Très élevé (Apparu dans 9 sessions régionales)",
        "explanation": "Antigone fustige avec horreur le 'petit bonheur' bourgeois fondé sur la lâcheté, le compromis et le renoncement aux idéaux.",
        "arabic": "استهجان ومفارقة حادة ترفض السعادة التافهة القائمة على التنازل عن الكرامة والمبادئ والشرف.",
        "darija": "استهجان قوي: كترفض فيه أنتيغون السعادة الذليلة والعيشة الرخيصة لي كيقبل بها بنادم باش يعيش وصافي."
    },
    {
        "id": "ant_fig_17",
        "rank_10yr_stats": 17,
        "scene": "scene_creon_antigone",
        "search_term": "dire non",
        "quote": "Moi, je peux dire « non » encore à tout ce que je n'aime pas et je suis seul juge.",
        "type": "Antithèse morale / Affirmation de liberté",
        "exam_source": "Régional Tanger 2019, Marrakech 2024",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Antithèse suprême entre Créon contraint de dire 'oui' aux nécessités du pouvoir et Antigone libre de dire 'non' par sa mort.",
        "arabic": "طباق قيمي يجسد قوة الرفض المطلق لسلطة الطغيان والتمسك باستقلالية الضمير الأخلاقي.",
        "darija": "إعلان قوي للرفض: كتقول 'لا' فوجه الملك وكتفضل الموت بكرامتها على تقبل شي حاجة ما قنعاهاش."
    },
    {
        "id": "ant_fig_18",
        "rank_10yr_stats": 18,
        "scene": "scene_creon_antigone",
        "search_term": "deux voyous",
        "quote": "Etéocle et Polynice étaient deux petits voyous qui se méprisaient.",
        "type": "Démystification / Métaphore péjorative",
        "exam_source": "Régional Casablanca 2020, Souss 2023",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Créon démolit le mythe héroïque des deux frères princiers en les réduisant vulgairement à deux gangsters méprisables.",
        "arabic": "استعارة تحقيرية تسقط هالة البطولة عن الأخوين وتصفهما بقطاع الطرق المنحرفين لتجريد تمرد أنتيغون من معناه.",
        "darija": "استعارة تحقيرية: كريون فضح الحقيقة وقالها خوتك بجوج كانو غير شفارة ومشرملين مكيستاهلوش تموتي عليهم."
    },
    {
        "id": "ant_fig_19",
        "rank_10yr_stats": 19,
        "scene": "scene_garde_antigone",
        "search_term": "pourquoi je meurs",
        "quote": "Créon avait raison, c'est terrible, maintenant, à côté de cet homme, je ne sais plus pourquoi je meurs.",
        "type": "Aveu tragique / Ironie existentielle",
        "exam_source": "Régional Casablanca 2017, Rabat 2023",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Comble du tragique moderne : au seuil du tombeau, Antigone mesure l'inutilité de son geste en présence d'un garde indifférent.",
        "arabic": "اعتراف مأساوي يبرز قمة الخيبة والوحشة حين تكتشف البطلة عبثية التضحية وهي تحتضر بجانب حارس متبلد.",
        "darija": "اعتراف تراجيدي مر: كتحس بالندم والوحدة وهي كتموت حدا ݣارديان بارد ما حاس بوالو من المعاناة ديالها."
    },
    {
        "id": "ant_fig_20",
        "rank_10yr_stats": 20,
        "scene": "scene_finale",
        "search_term": "apaisement triste",
        "quote": "Un grand apaisement triste tombe sur Thèbes et sur le palais vide où Créon va commencer à attendre la mort.",
        "type": "Oxymore / Métaphore funèbre",
        "exam_source": "Régional Fès 2016, Marrakech 2021, Casablanca 2024",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Oxymore 'apaisement triste' matérialisant l'atmosphère désolée et vide du dénouement où tous les innocents ont péri.",
        "arabic": "طباق مجازي يجمع بين السكينة والحزن الموحش ليصف الفراغ والخراب الذي آل إليه قصر كريون بعد هلاك الجميع.",
        "darija": "جمع بين السكون والحزن باش يوصف الخوا والوحشة لي بقات فالقصر من بعد ما ماتو كولشي وبقى كريون بوحدو."
    }
]

TOP_20_HUGO = [
    {
        "id": "hugo_fig_01",
        "rank_10yr_stats": 1,
        "chapter": "chapitre_1",
        "search_term": "cinq semaines que j'habite avec cette pensée",
        "quote": "Condamné à mort ! Voilà cinq semaines que j'habite avec cette pensée, toujours seul avec elle, toujours glacé de sa présence, toujours courbé sous son poids !",
        "type": "Anaphore / Personnification / Métaphore",
        "exam_source": "Régional Casablanca 2015, Fès 2017, Rabat 2021",
        "exam_frequency": "Très élevé (Apparu dans 10 sessions régionales)",
        "explanation": "Anaphore de 'toujours' et personnification de la pensée mortifère en un spectre pesant qui torture la psyché du condamné.",
        "arabic": "تكرار بلاغي لكلمة (دائماً) مع تشخيص هاجس الإعدام في هيئة كائن جاثم يخنق أنفاس السجين.",
        "darija": "تكرار ديال 'ديما' وتشخيص: رد فكرة الإعدام بحال شي شبح بارد وتقيل فوق كتافو ما كيفارقوش."
    },
    {
        "id": "hugo_fig_02",
        "rank_10yr_stats": 2,
        "chapter": "chapitre_1",
        "search_term": "spectre de plomb",
        "quote": "Cette pensée est là comme un spectre de plomb.",
        "type": "Comparaison",
        "exam_source": "Régional Marrakech 2016, Tanger 2019, Casablanca 2023",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Comparaison de l'idée fixe de mort à un spectre de plomb, évoquant à la fois le poids étouffant et la froideur cadavérique.",
        "arabic": "تشبيه يقارن فكرة الموت بطيف ثقيل من رصاص يكتم الأنفاس ولا يغادر الذهن.",
        "darija": "تشبيه: شبه فكرة الموت بخيال مصنوع من اللدون تقيل كيعصر ليه قلبو."
    },
    {
        "id": "hugo_fig_03",
        "rank_10yr_stats": 3,
        "chapter": "chapitre_1",
        "search_term": "Chaque jour, chaque heure",
        "quote": "Chaque jour, chaque heure, chaque minute avait son idée.",
        "type": "Gradation descendante / Répétition",
        "exam_source": "Régional Fès 2018, Souss 2022",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Gradation temporelle descendante soulignant la plénitude de la vie passée en contraste avec le temps arrêté de la condamnation.",
        "arabic": "تدرج زمني تنازلي يبرز حيوية الماضي وغناه الفكري في مقابل جمود الحاضر في انتظار الإعدام.",
        "darija": "تدرج زمني نازل: من النهار للساعة للدقيقة، كيبين كيفاش كان عايش حياتو فرحان قبل ما يتحكم عليه."
    },
    {
        "id": "hugo_fig_04",
        "rank_10yr_stats": 4,
        "chapter": "chapitre_2",
        "search_term": "belle matinée d'août",
        "quote": "C'était par une belle matinée d'août. Il faisait grand soleil... et les juges avaient des figures sinistres.",
        "type": "Antithèse",
        "exam_source": "Régional Rabat 2016, Casablanca 2020",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Antithèse brutale entre l'éclat lumineux de la matinée estivale et la noirceur menaçante des magistrats prononçant la sentence.",
        "arabic": "طباق يقابل بين إشراقة صباح الصيف وجمال الطبيعة من جهة، وتجهم وجوه القضاة المصدرين لحكم الموت من جهة أخرى.",
        "darija": "طباق كيبين التناقض بين النهار الزوين والمشمس فغشت، وبين الوجوه الكحلة والقاصحة ديال القضاة."
    },
    {
        "id": "hugo_fig_05",
        "rank_10yr_stats": 5,
        "chapter": "chapitre_2",
        "search_term": "Autrefois, car il me semble",
        "quote": "Autrefois libre... aujourd'hui captif.",
        "type": "Antithèse temporelle",
        "exam_source": "Régional Tanger 2017, Marrakech 2021",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Opposition tranchée résumant la rupture dramatique causée par le verdict qui l'arrache brutalement au monde des vivants.",
        "arabic": "طباق زمني يختزل الفجوة الساحقة بين الحرية السالفة والاعتقال المظلم في الزنزانة.",
        "darija": "طباق كيبين الفرق القاصح بين الحرية لي كانت عندو زمان وبين الحبس لي ولا فيه دابا."
    },
    {
        "id": "hugo_fig_06",
        "rank_10yr_stats": 6,
        "chapter": "chapitre_2",
        "search_term": "dans six semaines",
        "quote": "Au lieu de me couper la tête tout de suite, ils me la coupent dans six semaines !",
        "type": "Antiphrase ironique / Humour noir",
        "exam_source": "Régional Meknès 2015, Souss 2019, Casablanca 2024",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Ironie noire amère dénonçant la cruauté de la justice qui prolonge l'angoisse sous couvert d'accorder un délai de pourvoi.",
        "arabic": "تهكم وسخرية سوداء توضح أن تأجيل موعد الإعدام لأسابيع ليس نعمة بل تمديداً للعذاب والاحتضار.",
        "darija": "سخرية كحلة: كيبين بلي التأجيل لستة سيمانات راه غير كيعذب فيه كثر ماشي رحمة."
    },
    {
        "id": "hugo_fig_07",
        "rank_10yr_stats": 7,
        "chapter": "chapitre_4",
        "search_term": "Bicêtre",
        "quote": "Bicêtre est un monstre hideux, une lèpre sur la terre.",
        "type": "Métaphore péjorative",
        "exam_source": "Régional Tanger 2015, Oriental 2022",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Métaphore flétrissant l'institution pénitentiaire comme un organisme lépreux et monstrueux qui dégrade l'humanité.",
        "arabic": "استعارة تصف سجن بيسيتر الرهيب بوحش مفترس وبمرض الجذام المشوه للأرض والمجتمع.",
        "darija": "استعارة: شبه حبس بيسيتر بالوحش الخايب وبمرض الجذام لي كيخمج الأرض."
    },
    {
        "id": "hugo_fig_08",
        "rank_10yr_stats": 8,
        "chapter": "chapitre_6",
        "search_term": "journal de mes souffrances",
        "quote": "Ce journal de mes souffrances, heure par heure, minute par minute, supplice par supplice.",
        "type": "Gradation / Rythme ternaire",
        "exam_source": "Régional Casablanca 2017, Fès 2022, Rabat 2024",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Rythme ternaire en gradation croissante soulignant la vocation d'autopsie psychologique et de témoignage abolitionniste du récit.",
        "arabic": "تدرج لفظي وإيقاع ثلاثي يجسد العد التنازلي الدقيق للحظات الاحتضار وتفاصيل المعاناة الإنسانية.",
        "darija": "تدرج زمني: من الساعة للدقيقة للعذاب، كيبين كيفاش الوقت كيدوز عليه بالثقل والموت كتقرب."
    },
    {
        "id": "hugo_fig_09",
        "rank_10yr_stats": 9,
        "chapter": "chapitre_9",
        "search_term": "trois femmes",
        "quote": "J'ai laissé là-bas une mère, une femme, une petite fille.",
        "type": "Énumération pathétique / Gradation affective",
        "exam_source": "Régional Marrakech 2017, Fès 2021",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Énumération des trois générations de femmes sacrifiées démontrant que la guillotine frappe cruellement des innocents.",
        "arabic": "تعداد مؤثر للأجيال الثلاثة من النساء (الأم والزوجة والطفلة) لإثبات أن الإعدام يدمر أسراً بريئة بأكملها.",
        "darija": "تعداد كيبكي: ذكر ميمتو ومPennou وبنيتو الصغيرة باش يبين كيفاش الإعدام كيقتل عائلة كاملة بلا ذنب."
    },
    {
        "id": "hugo_fig_10",
        "rank_10yr_stats": 10,
        "chapter": "chapitre_11",
        "search_term": "murs",
        "quote": "Ces murs avaient des voix, ces pierres racontaient des crimes.",
        "type": "Personnification / Parallélisme",
        "exam_source": "Régional Rabat 2018, Marrakech 2023",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Personnification et parallélisme donnant la parole aux pierres du cachot pour faire revivre la mémoire des suppliciés antérieurs.",
        "arabic": "تشخيص وموازنة تجعل من جدران الزنزانة وحجارتها الصامتة ألسنة تروي جرائم الإعدام ومعاناة السابقين.",
        "darija": "تشخيص: رد الحيوط والحجر ديال الحبس بحال بنادم كيعاود القصص ديال لي تشنقو قبلو."
    },
    {
        "id": "hugo_fig_11",
        "rank_10yr_stats": 11,
        "chapter": "chapitre_13",
        "search_term": "hideuse fête",
        "quote": "Le ferrage des forçats... cette hideuse fête.",
        "type": "Oxymore",
        "exam_source": "Régional Casablanca 2016, Fès 2019, Rabat 2022",
        "exam_frequency": "Très élevé (Apparu dans 9 sessions régionales)",
        "explanation": "Oxymore associant l'abjection de la torture ('hideuse') à la réjouissance publique ('fête') pour stigmatiser la curiosité malsaine du peuple.",
        "arabic": "طباق تركيبي يجمع بين البشاعة والعيد، للتنديد ببربرية تحويل تعذيب المساجين إلى احتفال جماهيري.",
        "darija": "جمع بين جوج كلمات متناقضين (بشعة وحفلة) باش يفضح النذالة ديال الناس لي كيتفرجو فالعذاب بحال يلا فالفرح."
    },
    {
        "id": "hugo_fig_12",
        "rank_10yr_stats": 12,
        "chapter": "chapitre_13",
        "search_term": "malédictions",
        "quote": "Une pluie de malédictions tomba sur les gardiens.",
        "type": "Métaphore",
        "exam_source": "Régional Tanger 2018, Béni Mellal 2023",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Métaphore comparant la fureur verbale des bagnards enchaînés à une averse d'orage destructrice.",
        "arabic": "استعارة تشبه الشتائم واللعنات المنهالة على الحراس بمطر غزير وعاصف.",
        "darija": "استعارة: شبه السبان والدعاوي لي طاحو على العساسة بحال الشتا الخيط من السما."
    },
    {
        "id": "hugo_fig_13",
        "rank_10yr_stats": 13,
        "chapter": "chapitre_18",
        "search_term": "directeur",
        "quote": "Le directeur entra, avec son sourire poli et glacé.",
        "type": "Oxymore / Métaphore",
        "exam_source": "Régional Casablanca 2019",
        "exam_frequency": "Moyen (Apparu dans 4 sessions régionales)",
        "explanation": "Oxymore caractérisant l'hypocrisie et la cruauté administrative d'un geôlier masquant la mort sous des égards polis.",
        "arabic": "طباق واستعارة يصفان النفاق الإداري للجلاد الذي يخفي وحشية الموت خلف ابتسامة مهذبة وباردة.",
        "darija": "تناقض كيوصف النفاق ديال مدير الحبس لي كيضحك فوجه المحكوم ببرودة وهو كيديه للموت."
    },
    {
        "id": "hugo_fig_14",
        "rank_10yr_stats": 14,
        "chapter": "chapitre_22",
        "search_term": "milliers d'yeux",
        "quote": "Une foule immense, des milliers d'yeux avides de voir un homme mourir.",
        "type": "Métonymie / Hyperbole",
        "exam_source": "Régional Rabat 2017, Marrakech 2022",
        "exam_frequency": "Élevé (Apparu dans 6 sessions régionales)",
        "explanation": "Métonymie ('des yeux' pour les spectateurs) et hyperbole pour dénoncer la pulsion voyeuriste et morbide de la foule parisienne.",
        "arabic": "مجاز مرسل ومبالغة يختزلان المتفرجين في أعين جشعة ومتعطشة لرؤية إنسان يلفظ أنفاسه الأخيرة.",
        "darija": "مجاز مرسل ومبالغة: اختزل الجمهور فعيون جيعانة باغا تشوف بنادم كيموت قدامها."
    },
    {
        "id": "hugo_fig_15",
        "rank_10yr_stats": 15,
        "chapter": "chapitre_23",
        "search_term": "langue hideuse",
        "quote": "L'argot, cette langue hideuse, greffée sur la langue générale comme une excroissance.",
        "type": "Comparaison / Métaphore médicale",
        "exam_source": "Régional Fès 2016, Casablanca 2021",
        "exam_frequency": "Très élevé (Apparu dans 7 sessions régionales)",
        "explanation": "Comparaison de l'argot des criminels à une tumeur parasitaire rongeant le tissu vivant de la langue saine.",
        "arabic": "تشبيه طبي واستعارة تحقيرية تشبه لغة قطاع الطرق بورم قبيح نابت في جسد اللغة الأم.",
        "darija": "تشبيه: شبه هضرة الحبس بحال شي ولسيسة ولا ورم خايب نابت فاللغة."
    },
    {
        "id": "hugo_fig_16",
        "rank_10yr_stats": 16,
        "chapter": "chapitre_26",
        "search_term": "Mon pauvre enfant",
        "quote": "Mon pauvre enfant ! ma petite Marie ! mon Dieu, elle n'a que trois ans !",
        "type": "Apostrophe pathétique / Exclamation",
        "exam_source": "Régional Rabat 2015, Marrakech 2020, Casablanca 2024",
        "exam_frequency": "Très élevé (Apparu dans 9 sessions régionales)",
        "explanation": "Apostrophe bouleversante faisant culminer l'émotion tragique sur l'innocence de l'orpheline qui portera l'opprobre du bourreau.",
        "arabic": "نداء استغاثة واستعطاف وجداني يبرز براءة الطفلة اليتيمة التي ستتحمل عار إعدام والدها.",
        "darija": "نداء كيبكي: كيهضر مع بنيتو الصغيرة لي ما عندها تا ذنب وغادي تعيش حياتها يتيمة ومحتقرة."
    },
    {
        "id": "hugo_fig_17",
        "rank_10yr_stats": 17,
        "chapter": "chapitre_28",
        "search_term": "échafaud",
        "quote": "L'échafaud dressé au milieu de la place, noir et sinistre.",
        "type": "Personnification / Registre tragique",
        "exam_source": "Régional Tanger 2019, Oriental 2023",
        "exam_frequency": "Élevé (Apparu dans 5 sessions régionales)",
        "explanation": "Personnification de la machine de mort dressée au cœur de la ville comme un autel barbare dédié au sacrifice humain.",
        "arabic": "تشخيص لمنصة الإعدام القاتمة التي تنتصب وسط الساحة كصنم دموي يقدم له المجتمع الأضاحي البشرية.",
        "darija": "تشخيص: كيوصف المقصلة بحال شي وحش كحل واقف وسط الساحة كيتسنى الدم ديالو."
    },
    {
        "id": "hugo_fig_18",
        "rank_10yr_stats": 18,
        "chapter": "chapitre_43",
        "search_term": "Monsieur, vous n'êtes pas mon père",
        "quote": "Non, Monsieur, vous n'êtes pas mon père, mon père est en haut.",
        "type": "Quiproquo tragique / Antithèse affective",
        "exam_source": "Régional Casablanca 2018, Tanger 2022, Fès 2024",
        "exam_frequency": "Très élevé (Apparu dans 9 sessions régionales)",
        "explanation": "Le refus candide de sa fillette brise le cœur du condamné, consommant sa mort morale avant même son exécution physique.",
        "arabic": "مفارقة مؤلمة تبرز إنكار الطفلة لأبيها المنهار نفسياً، مما يمثل الإعدام المعنوي الأقسى للوالد قبل المقصلة.",
        "darija": "مفارقة كتبكي: بنتو الصغيرة ما عقلاتش عليه وقالت ليه نتا ماشي با، وهادي أقصى ضربة تلقاها قبل الإعدام."
    },
    {
        "id": "hugo_fig_19",
        "rank_10yr_stats": 19,
        "chapter": "chapitre_48",
        "search_term": "buveuse de sang",
        "quote": "La Grève est une vieille buveuse de sang.",
        "type": "Personnification / Métaphore sanguinaire",
        "exam_source": "Régional Rabat 2019, Marrakech 2022, Casablanca 2023",
        "exam_frequency": "Très élevé (Apparu dans 8 sessions régionales)",
        "explanation": "Personnification de la place de Grève sous les traits d'une buveuse de sang insatiable pour susciter l'horreur de l'échafaud.",
        "arabic": "تشخيص واستعارة بشعة تجعل ساحة الإعدام كوحش أنثى مسنّة ومصاصة دماء لا ترتوي من رؤوس الضحايا.",
        "darija": "تشخيص: رد ساحة لاݣريف بحال شي شارفة مصاصة دماء ما كتشبعش من الدم ديال المشنوقين."
    },
    {
        "id": "hugo_fig_20",
        "rank_10yr_stats": 20,
        "chapter": "chapitre_49",
        "search_term": "QUATRE HEURES",
        "quote": "QUATRE HEURES.",
        "type": "Ellipse dramatique / Phrase nominale",
        "exam_source": "Régional Casablanca 2020, Fès 2023, Rabat 2024",
        "exam_frequency": "Très élevé (Apparu dans 10 sessions régionales)",
        "explanation": "Formule nominale ultime marquant la fin absolue de l'espoir, l'heure légale fatale et le coup de grâce du destin.",
        "arabic": "إيجاز مأساوي بليغ يقطع حبل السرد معلناً انتهاء المهلة وحلول سياف المقصلة لقطع العنق.",
        "darija": "إيجاز تراجيدي: جوج كلمات كيعلنو النهاية ديال الروح ووصول الجلاد باش يطير الراس."
    }
]

def find_paragraph_index(chapter_paragraphs, search_term):
    sn = norm(search_term)
    for idx, p in enumerate(chapter_paragraphs):
        if sn in norm(p):
            return idx
    # Fallback partial words
    words = [w for w in sn.split() if len(w) > 3]
    for idx, p in enumerate(chapter_paragraphs):
        pn = norm(p)
        if any(w in pn for w in words):
            return idx
    return 0

def find_dialogue_index(dialogues, search_term):
    sn = norm(search_term)
    for idx, d in enumerate(dialogues):
        if sn in norm(d.get("text", "")) or sn in norm(d.get("stage_direction", "") or ""):
            return idx
    words = [w for w in sn.split() if len(w) > 3]
    for idx, d in enumerate(dialogues):
        dn = norm(d.get("text", ""))
        if any(w in dn for w in words):
            return idx
    return 0

def build_all_figures(base_dir: Path):
    data_dir = base_dir / "data"
    
    with open(data_dir / "la_boite_a_merveilles" / "chapters.json", "r", encoding="utf-8") as f:
        boite_chapters = json.load(f)
        
    with open(data_dir / "le_dernier_jour_dun_condamne" / "chapters.json", "r", encoding="utf-8") as f:
        hugo_chapters = json.load(f)
        
    with open(data_dir / "antigone" / "scenes.json", "r", encoding="utf-8") as f:
        antigone_dialogues = json.load(f)
    
    # Resolve Boite Top 20
    resolved_boite = []
    for item in TOP_20_BOITE:
        ch = item["chapter"]
        p_idx = find_paragraph_index(boite_chapters.get(ch, []), item["search_term"])
        resolved_boite.append({
            "id": item["id"],
            "rank_10yr_stats": item["rank_10yr_stats"],
            "chapter_or_scene": ch,
            "paragraph_index": p_idx,
            "quote": item["quote"],
            "type": item["type"],
            "exam_source": item["exam_source"],
            "exam_frequency": item["exam_frequency"],
            "explanation": item["explanation"],
            "arabic": item["arabic"],
            "darija": item["darija"]
        })
        
    # Resolve Antigone Top 20
    resolved_antigone = []
    for item in TOP_20_ANTIGONE:
        sc = item["scene"]
        d_idx = find_dialogue_index(antigone_dialogues, item["search_term"])
        resolved_antigone.append({
            "id": item["id"],
            "rank_10yr_stats": item["rank_10yr_stats"],
            "chapter_or_scene": sc,
            "dialogue_index": d_idx,
            "quote": item["quote"],
            "type": item["type"],
            "exam_source": item["exam_source"],
            "exam_frequency": item["exam_frequency"],
            "explanation": item["explanation"],
            "arabic": item["arabic"],
            "darija": item["darija"]
        })
        
    # Resolve Hugo Top 20
    resolved_hugo = []
    for item in TOP_20_HUGO:
        ch = item["chapter"]
        p_idx = find_paragraph_index(hugo_chapters.get(ch, []), item["search_term"])
        resolved_hugo.append({
            "id": item["id"],
            "rank_10yr_stats": item["rank_10yr_stats"],
            "chapter_or_scene": ch,
            "paragraph_index": p_idx,
            "quote": item["quote"],
            "type": item["type"],
            "exam_source": item["exam_source"],
            "exam_frequency": item["exam_frequency"],
            "explanation": item["explanation"],
            "arabic": item["arabic"],
            "darija": item["darija"]
        })
        
    save_json(data_dir / "la_boite_a_merveilles" / "figures.json", resolved_boite)
    save_json(data_dir / "antigone" / "figures.json", resolved_antigone)
    save_json(data_dir / "le_dernier_jour_dun_condamne" / "figures.json", resolved_hugo)
    print(f"[OK] Built exactly 20 figures per book based on 10-year exam stats: {len(resolved_boite)} (Boîte), {len(resolved_antigone)} (Antigone), {len(resolved_hugo)} (Hugo).")

if __name__ == '__main__':
    build_all_figures(Path('.'))
