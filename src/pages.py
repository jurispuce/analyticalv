# Content of the four service pages, per language. Rendered by build.py.
REG = 'https://www.mod.gov.lv/sites/mod/files/document/Kiberdro%C5%A1%C4%ABbas%20auditoru%20saraksts_23_04_2026.pdf'
def ext(u, t): return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'

UI = {
 'lv': dict(eyebrow='Pakalpojums', faq='Biežāk uzdotie jautājumi', back='Visi pakalpojumi', other='Citi pakalpojumi', cta='Sazināties'),
 'en': dict(eyebrow='Service', faq='Frequently asked questions', back='All services', other='Other services', cta='Talk to us'),
}

PAGES = {
 'iso': {
  'path': {'lv': '/iso-27001-ieviesana/', 'en': '/en/iso-27001-implementation/'},
  'lv': dict(
   name='ISO 27001 ieviešana', title='ISO 27001 ieviešana un sertifikācijas atbalsts | Analytica',
   desc='ISO 27001 ieviešana no GAP audita līdz sertifikātam: risku novērtēšana, politikas, iekšējais audits un atbalsts sertifikācijā. Analytica, kopš 2006. gada.',
   h1='ISO 27001 ieviešana',
   lead='Ieviešam informācijas drošības pārvaldības sistēmu atbilstoši ISO/IEC 27001 no pirmā GAP audita līdz sertifikātam. Kopš 2006. gada esam to darījuši valsts iestādēm, IT uzņēmumiem un fintech uzņēmumam.',
   who=('Kad tas ir vajadzīgs', ['Klients vai partneris pieprasa ISO 27001 sertifikātu.', 'Jāizpilda regulējuma prasības (NIS 2, DORA, MK 397), un vajag vienu sistēmu, kas tās aptver.', 'Uzņēmums aug, un drošību vairs nevar pārvaldīt ar atsevišķiem dokumentiem.', 'Sertifikāts jau ir, bet jāpāriet uz ISO/IEC 27001:2022 vai jāsagatavojas uzraudzības auditam.']),
   steps=('Kā notiek ieviešana', True, [('GAP audits', 'Novērtējam esošo situāciju pret standarta 4.–10. sadaļu un A pielikuma kontrolēm.'), ('Plāns un apmācība', 'Sastādām ieviešanas plānu ar termiņiem un atbildīgajiem un apmācām jūsu komandu.'), ('Riski un kontroles', 'Vadām risku novērtēšanu, palīdzam izstrādāt politikas un procedūras un ieviest trūkstošās kontroles.'), ('Iekšējais audits un vadības pārskats', 'Veicam iekšējo auditu kopā ar jūsu auditoriem un sagatavojam vadības pārskatu.'), ('Sertifikācija', 'Atbalstām sertifikācijas auditā un palīdzam novērst konstatētās neatbilstības.')]),
   get=('Ko jūs saņemat', ['GAP audita ziņojums un ieviešanas plāns', 'Risku reģistrs un risku mazināšanas plāns', 'Piemērojamības paziņojums (SoA), politikas un procedūras', 'Iekšējā audita ziņojums un vadības pārskats', 'Ja vēlaties, visa sistēma tiek uzturēta Wingman platformā']),
   faq=[('Cik ilgi ilgst ISO 27001 ieviešana?', 'Tas atkarīgs no organizācijas lieluma un no tā, kas jau ir izdarīts. Pēc GAP audita mēs nosaucam reālu termiņu un darba apjomu.'), ('Vai Analytica izsniedz sertifikātu?', 'Nē. Sertifikātu izsniedz akreditēta sertifikācijas institūcija. Mēs sagatavojam organizāciju un atbalstām to audita laikā.'), ('Vai varat apmācīt arī mūsu darbiniekus?', 'Jā. Sadarbībā ar PECB vadām ISO/IEC 27001 Lead Implementer un Lead Auditor kursus, kā arī pielāgotas apmācības ieviešanas komandām un iekšējiem auditoriem.')],
   proof='Esam palīdzējuši ieviest un sertificēt ISO 27001 valsts aģentūrām, IT integratoriem, programmatūras izstrādātājiem un fintech uzņēmumam.'),
  'en': dict(
   name='ISO 27001 implementation', title='ISO 27001 implementation and certification support | Analytica',
   desc='ISO 27001 implementation from gap audit to certificate: risk assessment, policies, internal audit and certification support. Analytica, Latvia, since 2006.',
   h1='ISO 27001 implementation',
   lead='We build an information security management system to ISO/IEC 27001, from the first gap audit to the certificate. Since 2006 we have done this for state institutions, IT companies and a fintech.',
   who=('When you need it', ['A client or partner asks for an ISO 27001 certificate.', 'You have regulatory duties (NIS 2, DORA, Latvian Cabinet Regulation 397) and want one system that covers them.', 'The company is growing and security can no longer be run from separate documents.', 'You are certified already but need to move to ISO/IEC 27001:2022 or prepare for a surveillance audit.']),
   steps=('How implementation runs', True, [('Gap audit', 'We assess the current state against clauses 4 to 10 of the standard and the Annex A controls.'), ('Plan and training', 'We draw up an implementation plan with dates and owners, and train your team.'), ('Risks and controls', 'We lead the risk assessment and help write policies and procedures and put the missing controls in place.'), ('Internal audit and management review', 'We run the internal audit together with your auditors and prepare the management review.'), ('Certification', 'We support you through the certification audit and help close any nonconformities.')]),
   get=('What you receive', ['Gap audit report and implementation plan', 'Risk register and risk treatment plan', 'Statement of Applicability, policies and procedures', 'Internal audit report and management review', 'If you wish, the whole system maintained in Wingman']),
   faq=[('How long does ISO 27001 implementation take?', 'It depends on the size of the organisation and on what is already in place. After the gap audit we give you a realistic timeline and effort estimate.'), ('Does Analytica issue the certificate?', 'No. An accredited certification body issues the certificate. We prepare the organisation and support it during the audit.'), ('Can you also train our staff?', 'Yes. In partnership with PECB we deliver ISO/IEC 27001 Lead Implementer and Lead Auditor courses, and tailored training for implementation teams and internal auditors.')],
   proof='We have helped state agencies, IT integrators, software houses and a fintech implement and certify ISO 27001.'),
 },
 'mk397': {
  'path': {'lv': '/mk-397-atbilstiba/', 'en': '/en/cabinet-regulation-397-compliance/'},
  'lv': dict(
   name='MK 397 atbilstība', title='MK 397 atbilstība: minimālās kiberdrošības prasības | Analytica',
   desc='Palīdzam izpildīt MK noteikumu Nr. 397 “Minimālās kiberdrošības prasības” un Nacionālās kiberdrošības likuma prasības: novērtējums, dokumentācija, kiberdrošības audits.',
   h1='MK 397 atbilstība',
   lead='Ministru kabineta noteikumi Nr. 397 “Minimālās kiberdrošības prasības” ir spēkā kopš 2025. gada 2. jūlija. Palīdzam saprast, kas no tiem attiecas uz jums, un to izpildīt.',
   who=('Uz ko tas attiecas', ['Būtisko pakalpojumu sniedzēji', 'Svarīgo pakalpojumu sniedzēji', 'IKT kritiskās infrastruktūras īpašnieki un tiesiskie valdītāji', 'Piegādātāji, kuriem klienti prasa pierādīt atbilstību šīm prasībām']),
   steps=('Kā mēs palīdzam', True, [('Statuss un tvērums', 'Noskaidrojam, vai un kādā statusā uz jums attiecas Nacionālās kiberdrošības likums un kuras sistēmas ietilpst tvērumā.'), ('Atbilstības novērtējums', 'Salīdzinām esošo situāciju ar MK 397 prasībām un parādām, kas trūkst.'), ('Dokumentācija un pasākumi', 'Palīdzam izstrādāt kiberrisku pārvaldības dokumentāciju, politikas un procedūras un ieviest trūkstošos pasākumus.'), ('Kiberdrošības pārvaldnieks', 'Ja jums nav sava speciālista, nodrošinām <a href="@@P:manager@@">kiberdrošības pārvaldnieku kā pakalpojumu</a>.'), ('Neatkarīgs audits', 'Veicam kiberdrošības auditu organizācijām, kurām neesam bijuši ieviešanas konsultanti. Analytica ir iekļauta ' + ext(REG, 'kiberdrošības auditoru sarakstā') + '.')]),
   get=('Ko jūs saņemat', ['Atbilstības novērtējums pret MK 397 prasībām ar prioritātēm', 'Rīcības plāns ar termiņiem un atbildīgajiem', 'Izstrādāta vai pilnveidota dokumentācija', 'Audita ziņojums, ja esam jūsu auditors']),
   faq=[('Kas ir MK 397?', 'Tie ir Ministru kabineta 2025. gada 25. jūnija ' + ext('https://likumi.lv/ta/id/361481', 'noteikumi Nr. 397 “Minimālās kiberdrošības prasības”') + '. Tie izdoti saskaņā ar Nacionālās kiberdrošības likumu un nosaka minimālās prasības būtisko un svarīgo pakalpojumu sniedzējiem un IKT kritiskās infrastruktūras īpašniekiem.'), ('Vai ISO 27001 sertifikāts nozīmē atbilstību MK 397?', 'Ne automātiski. ISO 27001 sistēma aptver lielu daļu prasību, taču MK 397 ir arī savas specifiskas prasības. Novērtējumā parādām atšķirības.'), ('Vai Analytica var būt gan konsultants, gan auditors?', 'Vienam klientam nē. Lai audits būtu neatkarīgs, mēs neauditējam to, ko paši esam palīdzējuši ieviest.')],
   proof='Jau pirms MK 397 mēs daudzus gadus auditējām valsts iestāžu informācijas sistēmu atbilstību iepriekšējām prasībām (MK noteikumi Nr. 442).'),
  'en': dict(
   name='Cabinet Regulation 397 compliance', title='Latvia Cabinet Regulation 397 compliance: minimum cybersecurity requirements | Analytica',
   desc='Help with Latvia\'s Cabinet Regulation No. 397 on minimum cybersecurity requirements and the National Cybersecurity Law: assessment, documentation and the cybersecurity audit.',
   h1='Cabinet Regulation 397 compliance',
   lead='Latvia\'s Cabinet Regulation No. 397, "Minimum cybersecurity requirements", has been in force since 2 July 2025. We help you work out which parts apply to you and meet them.',
   who=('Who it applies to', ['Essential service providers', 'Important service providers', 'Owners and legal holders of ICT critical infrastructure', 'Suppliers whose clients ask them to prove they meet these requirements']),
   steps=('How we help', True, [('Status and scope', 'We establish whether the National Cybersecurity Law applies to you, in which status, and which systems are in scope.'), ('Compliance assessment', 'We compare the current state with the requirements of Regulation 397 and show what is missing.'), ('Documentation and measures', 'We help write the cyber risk management documentation, policies and procedures, and put the missing measures in place.'), ('Cybersecurity manager', 'If you have no specialist of your own, we provide a <a href="@@P:manager@@">cybersecurity manager as a service</a>.'), ('Independent audit', 'We carry out the cybersecurity audit for organisations where we have not been the implementation consultant. Analytica is on the ' + ext(REG, 'register of cybersecurity auditors') + '.')]),
   get=('What you receive', ['A prioritised assessment against the requirements of Regulation 397', 'An action plan with dates and owners', 'New or improved documentation', 'The audit report, where we are your auditor']),
   faq=[('What is Regulation 397?', 'It is ' + ext('https://likumi.lv/ta/id/361481', 'Cabinet Regulation No. 397, "Minimum cybersecurity requirements"') + ', adopted on 25 June 2025 under Latvia\'s National Cybersecurity Law. It sets minimum requirements for essential and important service providers and owners of ICT critical infrastructure.'), ('Does an ISO 27001 certificate mean we comply?', 'Not automatically. An ISO 27001 system covers much of what is required, but the regulation has specific requirements of its own. The assessment shows the differences.'), ('Can Analytica be both consultant and auditor?', 'Not for the same client. To keep the audit independent, we do not audit what we helped to implement.')],
   proof='Before Regulation 397 we spent many years auditing state information systems against the earlier requirements (Cabinet Regulation No. 442).'),
 },
 'audits': {
  'path': {'lv': '/drosibas-auditi/', 'en': '/en/security-audits/'},
  'lv': dict(
   name='Drošības auditi', title='Drošības auditi: IT un informācijas sistēmu drošības audits | Analytica',
   desc='Neatkarīgi informācijas sistēmu un IT infrastruktūras drošības auditi, atbilstības auditi un ISO 27001 iekšējie auditi. Analytica ir iekļauta kiberdrošības auditoru sarakstā.',
   h1='Drošības auditi',
   lead='Neatkarīgi informācijas sistēmu un IT infrastruktūras drošības auditi. Pārbaudām gan tehnisko pusi, gan pārvaldību un pasakām, kas jālabo vispirms.',
   who=('Audita veidi', ['Informācijas sistēmas drošības audits', 'Drošības un veiktspējas audits pirms sistēmas nodošanas ekspluatācijā', 'Atbilstības audits pret normatīvajiem aktiem un standartiem (MK 397, ISO/IEC 27001, DORA)', 'ISO/IEC 27001 iekšējais audits', 'Personas datu apstrādes audits', 'Datu centra audits']),
   steps=('Kā notiek audits', True, [('Tvērums un metodika', 'Saskaņojam, kas tiek auditēts, pret kādām prasībām un ar kādām metodēm.'), ('Dokumenti un intervijas', 'Izpētām dokumentāciju un runājam ar sistēmu turētājiem, administratoriem un drošības pārvaldnieku.'), ('Tehniskās pārbaudes', 'Veicam ievainojamību skenēšanu, ielaušanās testus un konfigurāciju pārbaudi, vajadzības gadījumā arī veiktspējas testus.'), ('Ziņojums', 'Aprakstām konstatējumus ar pierādījumiem, riska līmeni un ieteikumiem.'), ('Atkārtota pārbaude', 'Pārliecināmies, ka konstatētie trūkumi ir novērsti.')]),
   get=('Ko jūs saņemat', ['Audita ziņojums ar konstatējumiem, pierādījumiem un riska līmeni', 'Ieteikumi prioritārā secībā', 'Kopsavilkums vadībai', 'Atkārtota pārbaude pēc trūkumu novēršanas']),
   faq=[('Ar ko drošības audits atšķiras no ielaušanās testa?', 'Ielaušanās tests imitē uzbrucēju un meklē izmantojamas ievainojamības. Audits ir plašāks: tas vērtē arī pārvaldību, procesus un atbilstību prasībām. Bieži tests ir audita daļa.'), ('Vai jūs auditējat arī valsts informācijas sistēmas?', 'Jā. Esam auditējuši valsts e-pārvaldes platformas un ministriju informācijas sistēmas, un Analytica ir iekļauta ' + ext(REG, 'kiberdrošības auditoru sarakstā') + '.'), ('Kādus rīkus izmantojat?', 'Kombinējam automatizētu skenēšanu, tostarp ar Qualys, ar manuālu pārbaudi, lai ziņojumā nonāktu tikai pārbaudīti konstatējumi.')],
   proof='Esam veikuši drošības novērtējumus valsts e-iepirkumu platformai, oficiālās elektroniskās adreses sistēmai un ministriju informācijas sistēmām.'),
  'en': dict(
   name='Security audits', title='Security audits of IT and information systems | Analytica',
   desc='Independent security audits of information systems and IT infrastructure, compliance audits and ISO 27001 internal audits. Analytica is on Latvia\'s register of cybersecurity auditors.',
   h1='Security audits',
   lead='Independent security audits of information systems and IT infrastructure. We check both the technology and how it is managed, and tell you what to fix first.',
   who=('Types of audit', ['Security audit of an information system', 'Security and performance audit before a system goes live', 'Compliance audit against law and standards (Cabinet Regulation 397, ISO/IEC 27001, DORA)', 'ISO/IEC 27001 internal audit', 'Personal data processing audit', 'Data centre audit']),
   steps=('How an audit runs', True, [('Scope and method', 'We agree what is audited, against which requirements and with which methods.'), ('Documents and interviews', 'We study the documentation and talk to system owners, administrators and the security manager.'), ('Technical checks', 'We run vulnerability scans, penetration tests and configuration reviews, and performance tests where needed.'), ('Report', 'We describe each finding with evidence, a risk level and a recommendation.'), ('Re-test', 'We confirm that the findings have been fixed.')]),
   get=('What you receive', ['An audit report with findings, evidence and risk levels', 'Recommendations in priority order', 'A summary for management', 'A re-test once the findings are fixed']),
   faq=[('How does a security audit differ from a penetration test?', 'A penetration test imitates an attacker and looks for exploitable weaknesses. An audit is wider: it also assesses management, processes and compliance. A test is often one part of an audit.'), ('Do you audit state information systems?', 'Yes. We have audited national e-government platforms and ministry information systems, and Analytica is on the ' + ext(REG, 'register of cybersecurity auditors') + '.'), ('Which tools do you use?', 'We combine automated scanning, including Qualys, with manual checks, so that only verified findings reach the report.')],
   proof='We have carried out security assessments of the state e-procurement platform, the official electronic address system and ministry information systems.'),
 },
 'manager': {
  'path': {'lv': '/kiberdrosibas-parvaldnieks/', 'en': '/en/cybersecurity-manager/'},
  'lv': dict(
   name='Kiberdrošības pārvaldnieks', title='Kiberdrošības pārvaldnieks kā pakalpojums (CISO ārpakalpojums) | Analytica',
   desc='Kiberdrošības pārvaldnieks kā pakalpojums: risku reģistrs, piegādātāju izvērtēšana, incidentu vadība, apmācības un pārskati vadībai. Analytica, kopš 2006. gada.',
   h1='Kiberdrošības pārvaldnieks kā pakalpojums',
   lead='Pieredzējis kiberdrošības pārvaldnieks jūsu organizācijai bez pilnas slodzes darbinieka izmaksām. Mēs uzņemamies drošības programmas ikdienas vadību un atskaitāmies jūsu vadībai.',
   who=('Kam tas der', ['Organizācijām, kurām Nacionālās kiberdrošības likums prasa norīkot kiberdrošības pārvaldnieku', 'Finanšu sektora uzņēmumiem ar DORA prasībām', 'Uzņēmumiem, kuriem ir ISO 27001 sistēma, bet nav, kas to uztur', 'Uzņēmumiem, kuriem pilna laika drošības vadītājs būtu par daudz']),
   steps=('Ko pārvaldnieks dara', False, [('Riski', 'Uztur risku reģistru un risku mazināšanas plānu.'), ('Piegādātāji', 'Izvērtē piegādātājus un to līgumu drošības prasības.'), ('Incidenti', 'Vada incidentu risināšanu un ziņošanu.'), ('Apmācības', 'Organizē darbinieku kiberdrošības apmācības.'), ('Dokumenti', 'Uztur politikas un procedūras aktuālas.'), ('Pārbaudes', 'Organizē ielaušanās testus un auditus.'), ('Pārskati', 'Regulāri atskaitās vadībai par paveikto un atlikušajiem riskiem.')]),
   get=('Kā tas notiek', ['Iepriekš saskaņots stundu apjoms', 'Viens atbildīgais pārvaldnieks un komanda aiz viņa', 'Darbs un pierādījumi redzami Wingman platformā', 'Ceturkšņa pārskats par paveikto']),
   faq=[('Vai ārpakalpojuma pārvaldnieks atbilst MK 397 prasībām?', 'MK 397 nosaka prasības pārvaldnieka kvalifikācijai un ierobežo, cik subjektiem viena persona var būt pārvaldnieks vienlaikus. Pirms līguma pārbaudām, vai jūsu gadījumā šie nosacījumi izpildās.'), ('Kas notiek, ja pārvaldnieks nav pieejams?', 'Aiz pārvaldnieka ir Analytica komanda, tāpēc zināšanas par jūsu organizāciju nav atkarīgas no viena cilvēka.'), ('Ar ko tas atšķiras no konsultācijām?', 'Konsultants dod ieteikumus. Pārvaldnieks uzņemas drošības programmas izpildi visa gada garumā.')],
   proof='Šo pakalpojumu kopš 2023. gada sniedzam privātam pensiju fondam, un iepriekš to esam snieguši IT pakalpojumu uzņēmumam.'),
  'en': dict(
   name='Cybersecurity manager', title='Cybersecurity manager as a service (outsourced CISO) | Analytica',
   desc='Cybersecurity manager as a service: risk register, supplier reviews, incident handling, training and reporting to management. Analytica, Latvia, since 2006.',
   h1='Cybersecurity manager as a service',
   lead='An experienced cybersecurity manager for your organisation without the cost of a full-time hire. We take on the day-to-day running of the security programme and report to your management.',
   who=('Who it suits', ['Organisations that Latvia\'s National Cybersecurity Law requires to appoint a cybersecurity manager', 'Financial sector companies with DORA duties', 'Companies with an ISO 27001 system and nobody to maintain it', 'Companies for whom a full-time security lead would be too much']),
   steps=('What the manager does', False, [('Risks', 'Keeps the risk register and treatment plan current.'), ('Suppliers', 'Assesses suppliers and the security terms in their contracts.'), ('Incidents', 'Leads incident handling and reporting.'), ('Training', 'Organises cybersecurity training for staff.'), ('Documents', 'Keeps policies and procedures up to date.'), ('Checks', 'Arranges penetration tests and audits.'), ('Reports', 'Reports regularly to management on progress and remaining risks.')]),
   get=('How it works', ['An agreed number of hours', 'One named manager with a team behind them', 'Work and evidence visible in Wingman', 'A quarterly report on what was done']),
   faq=[('Does an outsourced manager satisfy Cabinet Regulation 397?', 'The regulation sets qualification requirements for the manager and limits how many entities one person may serve at the same time. Before signing we check that these conditions are met in your case.'), ('What if the manager is unavailable?', 'The manager has the Analytica team behind them, so knowledge of your organisation does not depend on one person.'), ('How is this different from consulting?', 'A consultant gives recommendations. The manager carries out the security programme through the year.')],
   proof='We have provided this service to a private pension fund since 2023, and earlier to an IT services company.'),
 },
}
ORDER = ['audits', 'mk397', 'iso', 'manager']
