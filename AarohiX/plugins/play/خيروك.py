import asyncioimport randomfrom AarohiX import appfrom pyrogram.types import (InlineKeyboardButton,                            InlineKeyboardMarkup, Message)from pyrogram import filters, Clienttxt = ["لو خيروك |  بين شراء منزل صغير أو استئجار فيلا كبيرة بمبلغ معقول؟ ","لو خيروك |  أن تعيش قصة فيلم هل تختار الأكشن أو الكوميديا؟ ","لو خيروك |  بين تناول البيتزا وبين الايس كريم وذلك بشكل دائم؟ ","لو خيروك |  بين إمكانية تواجدك في الفضاء وبين إمكانية تواجدك في البحر؟ ","لو خيروك |  بين تغيير وظيفتك كل سنة أو البقاء بوظيفة واحدة طوال حياتك؟ ","لو خيروك |  أسئلة محرجة أسئلة صراحة ماذا ستختار؟ ","لو خيروك |  بين الذهاب إلى الماضي والعيش مع جدك أو بين الذهاب إلى المستقبل والعيش مع أحفادك؟ ","لو كنت شخص اخر هل تفضل البقاء معك أم أنك ستبتعد عن نفسك؟ ","لو خيروك |  بين الحصول على الأموال في عيد ميلادك أو على الهدايا؟ ","لو خيروك |  بين القفز بمظلة من طائرة أو الغوص في أعماق البحر؟ ","لو خيروك |  بين الاستماع إلى الأخبار الجيدة أولًا أو الاستماع إلى الأخبار السيئة أولًا؟ ","لو خيروك |  بين أن تكون رئيس لشركة فاشلة أو أن تكون موظف في شركة ناجحة؟ ","لو خيروك |  بين أن يكون لديك جيران صاخبون أو أن يكون لديك جيران فضوليون؟ ","لو خيروك |  بين أن تكون شخص مشغول دائمًا أو أن تكون شخص يشعر بالملل دائمًا؟ ","لو خيروك |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ ","لو خيروك |  بين استمرار فصل الشتاء دائمًا أو بقاء فصل الصيف؟ ","لو خيروك |  بين العيش في القارة القطبية أو العيش في الصحراء؟ ","لو خيروك |  بين أن تكون لديك القدرة على حفظ كل ما تسمع أو تقوله وبين القدرة على حفظ كل ما تراه أمامك؟ ","لو خيروك |  بين أن يكون طولك 150 سنتي متر أو أن يكون 190 سنتي متر؟ ","لو خيروك |  بين إلغاء رحلتك تمامًا أو بقائها ولكن فقدان الأمتعة والأشياء الخاص بك خلالها؟ ","لو خيروك |  بين أن تكون اللاعب الأفضل في فريق كرة فاشل أو أن تكون لاعب عادي في فريق كرة ناجح؟ ","لو خيروك |  بين ارتداء ملابس البيت لمدة أسبوع كامل أو ارتداء البدلة الرسمية لنفس المدة؟ ","لو خيروك |  بين امتلاك أفضل وأجمل منزل ولكن في حي سيء أو امتلاك أسوأ منزل ولكن في حي جيد وجميل؟ ","لو خيروك |  بين أن تكون غني وتعيش قبل 500 سنة، أو أن تكون فقير وتعيش في عصرنا الحالي؟ ","لو خيروك |  بين ارتداء ملابس الغوص ليوم كامل والذهاب إلى العمل أو ارتداء ملابس جدك/جدتك؟ ","لو خيروك |  بين قص شعرك بشكل قصير جدًا أو صبغه باللون الوردي؟ ","لو خيروك |  بين أن تضع الكثير من الملح على كل الطعام بدون علم أحد، أو أن تقوم بتناول شطيرة معجون أسنان؟ ","لو خيروك |  بين قول الحقيقة والصراحة الكاملة مدة 24 ساعة أو الكذب بشكل كامل مدة 3 أيام؟ ","لو خيروك |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟ ","لو خيروك |  بين وضع أحمر الشفاه على وجهك ما عدا شفتين أو وضع ماسكارا على شفتين فقط؟ ","لو خيروك |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟ ","لو خيروك |  بين تلوين شعرك كل خصلة بلون وبين ارتداء ملابس غير متناسقة لمدة أسبوع؟ ","لو خيروك |  بين تناول مياه غازية مجمدة وبين تناولها ساخنة؟ ","لو خيروك |  بين تنظيف شعرك بسائل غسيل الأطباق وبين استخدام كريم الأساس لغسيل الأطباق؟ ","لو خيروك |  بين تزيين طبق السلطة بالبرتقال وبين إضافة البطاطا لطبق الفاكهة؟ ","لو خيروك |  بين اللعب مع الأطفال لمدة 7 ساعات أو الجلوس دون فعل أي شيء لمدة 24 ساعة؟ ","لو خيروك |  بين شرب كوب من الحليب أو شرب كوب من شراب عرق السوس؟ ","لو خيروك |  بين الشخص الذي تحبه وصديق الطفولة؟ ","لو خيروك |  بين أمك وأبيك؟ ","لو خيروك |  بين أختك وأخيك؟ ","لو خيروك |  بين نفسك وأمك؟ ","لو خيروك |  بين صديق قام بغدرك وعدوك؟ ","لو خيروك |  بين خسارة حبيبك/حبيبتك أو خسارة أخيك/أختك؟ ","لو خيروك |  بإنقاذ شخص واحد مع نفسك بين أمك أو ابنك؟ ","لو خيروك |  بين ابنك وابنتك؟ ","لو خيروك |  بين زوجتك وابنك/ابنتك؟ ","لو خيروك |  بين جدك أو جدتك؟ ","لو خيروك |  بين زميل ناجح وحده أو زميل يعمل كفريق؟ ","لو خيروك |  بين لاعب كرة قدم مشهور أو موسيقي مفضل بالنسبة لك؟ ","لو خيروك |  بين مصور فوتوغرافي جيد وبين مصور سيء ولكنه عبقري فوتوشوب؟ ","لو خيروك |  بين سائق سيارة يقودها ببطء وبين سائق يقودها بسرعة كبيرة؟ ","لو خيروك |  بين أستاذ اللغة العربية أو أستاذ الرياضيات؟ ","لو خيروك |  بين أخيك البعيد أو جارك القريب؟ ","لو خيروك |  يبن صديقك البعيد وبين زميلك القريب؟ ","لو خيروك |  بين رجل أعمال أو أمير؟ ","لو خيروك |  بين نجار أو حداد؟ ","لو خيروك |  بين طباخ أو خياط؟ ","لو خيروك |  بين أن تكون كل ملابس بمقاس واحد كبير الحجم أو أن تكون جميعها باللون الأصفر؟ ","لو خيروك |  بين أن تتكلم بالهمس فقط طوال الوقت أو أن تصرخ فقط طوال الوقت؟ ","لو خيروك |  بين أن تمتلك زر إيقاف موقت للوقت أو أن تمتلك أزرار للعودة والذهاب عبر الوقت؟ ","لو خيروك |  بين أن تعيش بدون موسيقى أبدًا أو أن تعيش بدون تلفاز أبدًا؟ ","لو خيروك |  بين أن تعرف متى سوف تموت أو أن تعرف كيف سوف تموت؟ ","لو خيروك |  بين العمل الذي تحلم به أو بين إيجاد شريك حياتك وحبك الحقيقي؟ ","لو خيروك |  بين معاركة دب أو بين مصارعة تمساح؟ ","لو خيروك |  بين إما الحصول على المال أو على المزيد من الوقت؟ ","لو خيروك |  بين امتلاك قدرة التحدث بكل لغات العالم أو التحدث إلى الحيوانات؟ ","لو خيروك |  بين أن تفوز في اليانصيب وبين أن تعيش مرة ثانية؟ ","لو خيروك |  بأن لا يحضر أحد إما لحفل زفافك أو إلى جنازتك؟ ","لو خيروك |  بين البقاء بدون هاتف لمدة شهر أو بدون إنترنت لمدة أسبوع؟ ","لو خيروك |  بين العمل لأيام أقل في الأسبوع مع زيادة ساعات العمل أو العمل لساعات أقل في اليوم مع أيام أكثر؟ ","لو خيروك |  بين مشاهدة الدراما في أيام السبعينيات أو مشاهدة الأعمال الدرامية للوقت الحالي؟ ","لو خيروك |  بين التحدث عن كل شيء يدور في عقلك وبين عدم التحدث إطلاقًا؟ ","لو خيروك |  بين مشاهدة فيلم بمفردك أو الذهاب إلى مطعم وتناول العشاء بمفردك؟ ","لو خيروك |  بين قراءة رواية مميزة فقط أو مشاهدتها بشكل فيلم بدون القدرة على قراءتها؟ ","لو خيروك |  بين أن تكون الشخص الأكثر شعبية في العمل أو المدرسة وبين أن تكون الشخص الأكثر ذكاءً؟ ","لو خيروك |  بين إجراء المكالمات الهاتفية فقط أو إرسال الرسائل النصية فقط؟ ","لو خيروك |  بين إنهاء الحروب في العالم أو إنهاء الجوع في العالم؟ ","لو خيروك |  بين تغيير لون عينيك أو لون شعرك؟ ","لو خيروك |  بين امتلاك كل عين لون وبين امتلاك نمش على خديك؟ ","لو خيروك |  بين الخروج بالمكياج بشكل مستمر وبين الحصول على بشرة صحية ولكن لا يمكن لك تطبيق أي نوع من المكياج؟ ","لو خيروك |  بين أن تصبحي عارضة أزياء وبين ميك اب أرتيست؟ ","لو خيروك |  بين مشاهدة كرة القدم أو متابعة الأخبار؟ ","لو خيروك |  بين موت شخصية بطل الدراما التي تتابعينها أو أن يبقى ولكن يكون العمل الدرامي سيء جدًا؟ ","لو خيروك |  بين العيش في دراما قد سبق وشاهدتها ماذا تختارين بين الكوميديا والتاريخي؟ ","لو خيروك |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟ ","لو خيروك |  بين نشر تفاصيل حياتك المالية وبين نشر تفاصيل حياتك العاطفية؟ ","لو خيروك |  بين البكاء والحزن وبين اكتساب الوزن؟ ","لو خيروك |  بين تنظيف الأطباق كل يوم وبين تحضير الطعام؟ ","لو خيروك |  بين أن تتعطل سيارتك في نصف الطريق أو ألا تتمكنين من ركنها بطريقة صحيحة؟ ","لو خيروك |  بين إعادة كل الحقائب التي تملكينها أو إعادة الأحذية الجميلة الخاصة بك؟ ","لو خيروك |  بين قتل حشرة أو متابعة فيلم رعب؟ ","لو خيروك |  بين امتلاك قطة أو كلب؟ ","لو خيروك |  بين الصداقة والحب ","لو خيروك |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟ ","لو خيروك |  بين مشاركة المنزل مع عائلة من الفئران أو عائلة من الأشخاص المزعجين الفضوليين الذين يتدخلون في كل كبيرة وصغيرة؟ ",        ]        @app.on_message(filters.command(["لو خيروك","خيروك"], ""))async def khyrok(client: Client, message: Message):      a = random.choice(txt)      await message.reply(        f"{a}")