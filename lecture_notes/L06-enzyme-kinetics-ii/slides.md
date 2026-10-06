---
title: Enzyme Kinetics II - Inhibition, Cooperativity and Soft Switches
subtitle: TKBM262615 Komputasi Biologi - Lecture 6
author: Matin Nuhamunada
date: 2026-10-14
---

<!-- layout: quote -->
> Physiology proved in the end to be much like engineering, being based on the same ideas of function and design.
> -- A. V. Hill, quoted by Ingalls at the opening of Chapter 3
<!-- notes: Bacakan. Hill adalah orang yang namanya akan kita pakai di Bagian 3 dan 4 hari ini. Kalimat ini cocok untuk kuliah hari ini: sel mengatur enzimnya seperti insinyur memasang katup dan sakelar. Kutipan lengkapnya di halaman pembuka Bab 3 Ingalls; di slide ini dipersingkat. -->

---

# Retrieval - what L05 left you holding
- Double the enzyme: what happens to $V_{max}$? To $K_M$?
- Is $c^{qss}$ a constant?
- When is $K_M$ a binding affinity?
<!-- notes: Dari ingatan. Jawaban: (1) Vmax menggandakan, KM tetap - KM tidak memuat eT; (2) tidak, ia bergantung pada s(t); (3) hanya ketika k2 << k-1. Nomor 1 yang paling dibutuhkan: setiap mekanisme hari ini bekerja dengan menggeser salah satu dari dua konstanta itu. -->

---

# How would you turn a reaction down?
- Brainstorm first, biology later
- Slow route: make less enzyme (minutes to hours)
- Fast route: a molecule binds the enzyme
- Today: the fast route, in two forms, then the switch
<!-- notes: Kumpulkan jawaban dulu sebelum mengajar apa pun. Pilah jawaban menjadi dua kelompok: lambat (genetik, ubah eT) dan cepat (molekul kecil mengikat enzim). Hari ini kelompok kedua. -->

---

<!-- layout: section -->
# Part 1 - Competitive inhibition
- An impostor at the active site

---

# An impostor at the active site
- Looks enough like substrate to bind, but never reacts
- An occupied enzyme makes no product
- Ibuprofen blocks cyclooxygenase: less prostaglandin
- Pain relief, and the stomach side-effect, from one inhibition
- Same site, so the more abundant molecule wins more often
<!-- notes: Prostaglandin terlibat dalam jalur nyeri, pembekuan darah, dan produksi lendir lambung. Efek samping lambung adalah inhibisi yang sama di jaringan yang tidak diinginkan. Kalimat terakhir di slide ini sudah meramalkan seluruh hasil aljabarnya - minta kelas mengingatnya. -->

---

# The scheme: one dead-end complex
$$S + E \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} C \overset{k_2}{\longrightarrow} E + P \qquad I + E \underset{k_{-3}}{\overset{k_3}{\rightleftharpoons}} C_I$$
- $C_I$ leads nowhere except back to $E + I$
- Treat $i$ as fixed: inhibitor far outnumbers enzyme
<!-- notes: Membekukan i adalah manuver variabel-lambat-menjadi-parameter yang sama dengan membekukan kelimpahan enzim. Ingalls membenarkannya dengan menganggap inhibitor jauh lebih berlimpah daripada enzim. -->

---

# QSSA on both complexes
$$c_I = \frac{e\,i}{K_i}, \quad K_i = \frac{k_{-3}}{k_3} \qquad\qquad e = \frac{K_M\,c}{s}$$
- Left: from $dc_I/dt = 0$
- Right: from $dc/dt = 0$, exactly as in L05
- $K_i$ is the inhibitor's dissociation constant
<!-- notes: Kerjakan di papan, minta kelas menyebutkan tiap langkah. dc_I/dt = k3 e i - k-3 c_I = 0 memberi c_I = e i / Ki. dc/dt = k1 s e - (k-1 + k2) c = 0 memberi e = KM c / s. Ki kecil berarti inhibitor mengikat erat. -->

---

# Three-term conservation, then collect
$$e_T = e + c + c_I = \frac{K_M\,c}{s}\left(1 + \frac{i}{K_i}\right) + c$$
- Every enzyme is free, holding S, or holding I
- Multiply by $s$ and collect $c$
<!-- notes: Langkah pengumpulan suku ini sama dengan L05, hanya ada faktor tambahan. e + c_I = e(1 + i/Ki). Kalikan dengan s: eT s = c [KM (1 + i/Ki) + s]. Biarkan kelas yang menyelesaikannya. -->

---

# The competitive rate law
$$v = \frac{V_{max}\,s}{K_M\left(1 + \dfrac{i}{K_i}\right) + s}$$
- Units: the bracket is a pure number
- Check: $i = 0$ gives L05's law back
- Only $K_M$ changed. $V_{max}$ did not
<!-- notes: Dua pemeriksaan murah yang harus menjadi kebiasaan: satuan dan limit. Lalu tanya: apa yang terjadi saat s sangat besar? Penyebut didominasi s, jadi laju tetap mendekati Vmax. -->

---

# Enough substrate always wins
- $V_{max}$ unchanged: at huge $s$ the inhibitor hardly matters
- Effective $K_M$ rises to $K_M(1 + i/K_i)$
- $i = 2$ mM: rate at $s = 0.5$ falls from 5.00 to 1.43
- At $s = 50$ it barely moves: 9.90 to 9.43
- A drug's effect depends on tissue substrate levels
<!-- notes: Angka dengan Vmax = 10 mM/s, KM = 0.5 mM, Ki = 0.4 mM. Tabel lengkapnya di catatan kuliah. Kutip Ingalls: ketika substrat jauh lebih berlimpah daripada inhibitor, inhibisinya hanya berpengaruh sangat kecil. -->

---

<!-- layout: section -->
# Part 2 - Allosteric regulation
- Non-competitive inhibition: a different site, a different fingerprint

---

# A different site removes a constraint
- Competitive inhibitors must resemble the substrate
- Allosteric regulators bind somewhere else and change the shape
- No chemical resemblance needed
- Any molecule can then carry the signal
- Jacob and Monod, 1961; allo = other, steros = shape
<!-- notes: Tekankan kebalikannya dari inhibisi kompetitif. Keharusan mirip substrat adalah batasan keras; alosteri menghapusnya. Karena itu sel bisa meregulasi enzim dengan molekul yang tidak ada hubungannya dengan reaksi itu - itulah yang memungkinkan jaringan regulasi. -->

---

# Independent binding, as a square
$$S + E \rightleftharpoons ES \to E + P \qquad I + E \rightleftharpoons EI$$
$$I + ES \rightleftharpoons ESI \qquad S + EI \rightleftharpoons ESI$$
- S always binds with $k_1, k_{-1}$; I always with $k_3, k_{-3}$
- That repetition is what "independent" means
- Four states; only ES makes product
<!-- notes: Tunjuk konstanta laju yang berulang. Pengikatan substrat memakai k1 dan k-1 baik ada inhibitor maupun tidak; pengikatan inhibitor memakai k3 dan k-3 baik ada substrat maupun tidak. Ini definisi "independen" yang ditulis sebagai konstanta laju, bukan kata-kata. -->

---

# The non-competitive rate law
$$v = \frac{V_{max}}{1 + \dfrac{i}{K_i}}\cdot\frac{s}{K_M + s}$$
- Assume inhibitor binding sits at equilibrium: $[EI] = \frac{i}{K_i}[E]$
- QSSA on ES, then the four-term conservation
- Exact when $k_2 \ll k_{-1}$; otherwise close in shape
<!-- notes: Satu kalimat saja tentang keakuratan: Ingalls menyajikan (3.15) sebagai hasil QSSA; kalau QSSA diselesaikan tepat tanpa asumsi kesetimbangan, hasilnya cocok dengan (3.15) hanya bila k2 << k-1 (rasio 1.011 pada k2 = 0.1, tetapi 1.48 pada k2 = 10). Pemeriksaan numeriknya ada di catatan. Pelajaran kualitatifnya tetap: langit-langit turun, dan substrat tidak bisa mengatasinya. -->

---

# The exact mirror image
$$\text{competitive: } \frac{V_{max}\,s}{K_M\left(1+\frac{i}{K_i}\right) + s} \qquad \text{non-competitive: } \frac{\frac{V_{max}}{1+\frac{i}{K_i}}\,s}{K_M + s}$$
- Same factor $(1 + i/K_i)$ in both
- Competitive: it multiplies $K_M$
- Non-competitive: it divides $V_{max}$
<!-- notes: Tulis keduanya di papan dan lingkari faktornya di masing-masing. Mahasiswa lebih mudah mengingat letak faktor itu daripada dua rumus. Tanya: inhibitor mana yang lebih Anda sukai sebagai obat? Tidak ada satu jawaban benar - perdebatannya yang penting. -->

---

<!-- layout: picture -->
# Two fingerprints, read by eye
![Competitive against non-competitive inhibition](../../build/l06-inhibition.png)
Left: same ceiling, the bend moves. Right: same bend, the ceiling drops.
<!-- notes: Titik-titik adalah titik setengah-maksimum setiap kurva. Kiri: titiknya bergeser ke kanan saat i naik. Kanan: titiknya tetap di s = KM, tetapi langit-langitnya turun. Pada s = 50 mM inhibitor non-kompetitif masih memangkas laju menjadi 1.65 dari 9.90. -->

---

# Hinge question - diagnose the inhibitor
- $V_{max}$ unchanged, $K_M$ tripled. Which kind?
- A: non-competitive
- B: competitive
- C: cooperative (a Hill coefficient)
- D: cannot tell without the chemical structure
<!-- notes: Mini-whiteboard, serentak. Jawaban B. A menukar sidik jarinya. C mencampur bentuk kurva dengan pergeseran KM. D mengabaikan bahwa kedua hukum laju menjawabnya dari angka saja. Pertanyaan lanjutan untuk kelas yang cepat: berapa i/Ki? 1 + i/Ki = 3, jadi 2. Istirahat setelah slide ini. -->

---

<!-- layout: section -->
# Part 3 - Cooperativity and the Hill function
- When binding sites influence one another

---

# Same chain, same ligand, different curve
- Haemoglobin: four chains, oxygen binding is sigmoidal
- Myoglobin: one chain of the same kind, hyperbolic
- So the S-shape cannot come from the site itself
- It comes from the chains influencing each other
<!-- notes: Jalankan ini sebagai penalaran, bukan fakta. Saat pertama diukur sekitar 1900, kurva sigmoid mengejutkan karena kebanyakan kurva pengikatan hiperbolik. Perbandingan terkontrol dengan mioglobin yang menjawabnya. -->

---

# Fractional saturation, one site
$$Y = \frac{[PX]}{[P] + [PX]} = \frac{[X]}{K + [X]}, \qquad K = \frac{k_{-1}}{k_1}$$
- Y: the fraction of sites holding a ligand
- The same shape as Michaelis-Menten
- A rate is proportional to fractional occupancy
<!-- notes: Turunkan dari kesetimbangan k1[P][X] = k-1[PX]. Tunjukkan bahwa ini bentuk Michaelis-Menten lagi, dan alasan Ingalls: laju enzim sebanding dengan keterisian fraksionalnya. -->

---

# The surprise: four sites are not enough
- Four identical, independent sites: still hyperbolic
- Different affinities, still independent: still hyperbolic
- Several sites do not make cooperativity
- The sites must affect one another
<!-- notes: Cold call sebelum membuka bullet: apakah protein dengan empat sisi otomatis sigmoid? Kebanyakan akan menjawab ya. Biarkan mereka terkejut. Setiap sisi independen terisi seolah sendirian. Soal 3.7.9 Ingalls membuktikan kasus afinitas berbeda. -->

---

# Interacting sites: the two-site Adair form
$$Y = \frac{[X]/K_1 + [X]^2/(K_1K_2)}{1 + 2[X]/K_1 + [X]^2/(K_1K_2)}$$
- Sigmoidal when later binding is much tighter: $K_2 \ll K_1$
- That is positive cooperativity
- The four-site form has the same structure; not derived here
<!-- notes: Ingalls Latihan 3.3.1. Tunjukkan saja, jangan turunkan versi empat sisi di papan. -->

---

# The Hill function in three lines
$$P + nX \rightleftharpoons PX_n \quad\Rightarrow\quad Y = \frac{[X]^n}{K^n + [X]^n}, \qquad K^n = \frac{k_{-1}}{k_1}$$
- Extreme cooperativity: $n$ ligands bind at once
- At equilibrium $[PX_n] = [P][X]^n/K^n$
- Divide, and the Hill function appears
<!-- notes: Latihan 3.3.3 Ingalls. Kerjakan di papan: Y = [PXn]/([P] + [PXn]), substitusikan, bagi dengan [P]. Tiga baris. A. V. Hill mengajukan bentuk ini pada 1910. -->

---

# Two parameters, two jobs
- $K$: where the switch sits; $Y = 1/2$ at $[X] = K$
- $n$: how sharply the curve turns
- $n = 1$ is the hyperbola again
- Larger $n$: flatter below $K$, steeper through it
- Enzyme form, two sites: $v = V_{max}s^2/(K_M + s^2)$
<!-- notes: Latihan 3.3.4 untuk bentuk enzimnya; perhatikan KM di sana bersatuan konsentrasi kuadrat. -->

---

# n is not the number of sites
- Haemoglobin has four sites
- Hill's own fits: $n$ from 1 to 3.2
- Non-integer values are routine; 2.7 sites is impossible
- Read $n$ as steepness, not as a count
<!-- notes: Bukti lebih kuat daripada peringatan. n = 4 muncul hanya di bawah asumsi ekstrem pengikatan serentak. Pertanyaan: protein Anda punya enam sisi dan datanya cocok dengan n = 2.1. Apa artinya? Ada kooperativitas nyata tetapi parsial - bukan bahwa proteinnya punya dua sisi. Hill sendiri memakai bentuk ini sebagai kurva pengepasan tanpa makna mekanistik. -->

---

<!-- layout: section -->
# Part 4 - Hill functions as regulation models
- Cooperative inhibitors, and a factor you can bolt onto any rate law

---

# A cooperative inhibitor
$$nI + E \rightleftharpoons EI_n \quad\Rightarrow\quad c_I = e\left(\frac{i}{K_i}\right)^n, \qquad K_i^n = \frac{k_{-3}}{k_3}$$
- $n$ inhibitor molecules bind together, as in the Hill derivation
- Everything else in Part 1 is unchanged
- So $i/K_i$ becomes $(i/K_i)^n$
<!-- notes: Tegaskan bahwa ini inferensi: Ingalls tidak mencetak kedua hukum laju berikut, tetapi keduanya tinggal menggabungkan skema 3.2 dengan Latihan 3.3.3. Soal 3.7.8(b) Ingalls melakukan hal yang sama untuk aktivator. -->

---

# Hill-type inhibition, both kinds
$$\text{competitive: } v = \frac{V_{max}\,s}{K_M\left(1 + (i/K_i)^n\right) + s}$$
$$\text{non-competitive: } v = \frac{V_{max}}{1 + (i/K_i)^n}\cdot\frac{s}{K_M + s}$$
- The non-competitive factor is a decreasing Hill function
- It equals 1/2 at $i = K_i$
- A module: multiply any rate law by it
<!-- notes: Tulis 1/(1 + (i/Ki)^n) = Ki^n/(Ki^n + i^n) supaya terlihat sebagai fungsi Hill menurun. Pemisahan menjadi pengali inilah yang membuat faktor Hill praktis sebagai balok penyusun model yang lebih besar. Ingalls memberi isyarat bahwa suku seperti ini muncul lagi di bab-bab berikutnya. -->

---

# Does substrate move the switch?
$$\left(\frac{i_{50}}{K_i}\right)^n = 1 + \frac{s}{K_M} \quad\Rightarrow\quad i_{50} = K_i\left(1 + \frac{s}{K_M}\right)^{1/n}$$
- Competitive: yes, but only by the $n$-th root
- Non-competitive: $i_{50} = K_i$ at every $s$
- Predict before the next slide: $n = 1$ against $n = 4$
<!-- notes: Turunkan di papan: v(i)/v(0) = (KM + s)/(KM(1 + (i/Ki)^n) + s) = 1/2, kalikan silang. Lalu mini-whiteboard: dengan KM = 0.5 mM dan Ki = 0.4 mM, berapa i50 pada s = 10 KM untuk n = 1 dan n = 4? Jawaban: 4.40 mM dan 0.73 mM. -->

---

<!-- layout: picture -->
# Cooperative inhibitors resist substrate
![Hill functions as regulation](../../build/l06-hill-regulation.png)
From $s = 0.1K_M$ to $10K_M$, $i_{50}$ shifts 10-fold at $n = 1$ but 1.8-fold at $n = 4$.
<!-- notes: Panel A: faktor regulasi untuk n = 1, 2, 4. Panel B: inhibitor kompetitif kooperatif, tiga tingkat substrat - sakelarnya bergeser sedikit. Panel C: non-kompetitif, tiga tingkat substrat menjadi satu kurva. -->

---

# An activator gives a rising Hill factor
$$v = \frac{V_{max}\,s}{K_1 + s}\cdot\frac{r^n}{r^n + K_2/(K_1 + s)}$$
- Ingalls Problem 3.7.8: activator $R$ must bind first
- A Michaelis-Menten part times a Hill factor in $r$
- Inhibitors: decreasing factors. Activators: increasing
<!-- notes: Bentuk asli di Ingalls: v = Vmax s r^n/(K1 r^n + K2 + r^n s). Bagi pembilang dan penyebut dengan (K1 + s). Cukup satu slide; ini bacaan, bukan penurunan wajib. -->

---

<!-- layout: section -->
# Part 5 - Sigmoidal kinetics as soft switches
- Steep, but graded, reversible and without memory

---

# How sensitive is a response?
$$\frac{x}{Y}\frac{dY}{dx} = n\,(1 - Y)$$
- Kinetic order: % change out per % change in
- Hyperbola: $K/(K + x)$, never above 1
- Hill: starts at $n$, equals $n/2$ at $K$
- Above 1 means small relative changes get amplified
<!-- notes: Dari bacaan lanjutan L05. Turunkan dengan aturan hasil bagi: dY/dx = n x^(n-1) K^n/(K^n + x^n)^2, kalikan dengan x/Y. Untuk n = 4: 4.0 pada x = 0.1K, 2.0 pada K, hampir 0 pada 10K. Inilah isi tepat dari "mirip sakelar". -->

---

# How far must the input move?
$$\frac{x_{90}}{x_{10}} = 9^{2/n}$$
- $n = 1$: 81-fold
- $n = 2$: 9-fold
- $n = 3$: 4.3-fold
- $n = 4$: 3-fold
- Slope at half-saturation: $n/(4K)$
<!-- notes: Turunkan: Y = 0.1 memberi (x/K)^n = 1/9, Y = 0.9 memberi 9, rasionya 81^(1/n). Latihan 3.3.2 untuk kemiringannya. -->

---

# Why haemoglobin needs the S-shape
- Myoglobin stores: it should stay loaded
- Haemoglobin shuttles: load in lungs, unload in muscle
- The oxygen difference is only about five-fold
- Hyperbolic carrier needs 81-fold; $n = 3$ needs 4.3-fold
<!-- notes: Tanya: mengapa mioglobin tidak perlu kooperatif? Karena menyimpan dan mengangkut adalah pekerjaan berbeda. Aritmetika satu baris ini menjelaskan sebuah sistem organ. -->

---

<!-- layout: picture -->
# Three readings of a sigmoid
![Three readings of a sigmoid](../../build/l06-cooperativity-switch.png)
In a five-fold window, $n = 1$ unloads 0.38 of its sites; $n = 3$ unloads 0.84.
<!-- notes: Panel A: jendela lima kali lipat diletakkan di sekitar K sebagai ilustrasi - Ingalls memberi lebarnya, bukan letaknya. Panel B: rentang 10-90%. Panel C: orde kinetik n(1 - Y); garis putus-putus adalah batas hiperbola. -->

---

# Why call it a soft switch?
- Graded: $n = 4$ gives 0.06, 0.50, 0.94 at inputs 0.5, 1, 2
- Reversible: lower the input, it retraces the curve
- Memoryless: output depends only on the present input
- A light switch jumps; a sigmoid only turns steeply
<!-- notes: "Sakelar lunak" adalah istilah ringkas mata kuliah ini; Ingalls menyebutnya "switch-like". Tiga sifat di slide ini yang membedakannya dari sakelar sungguhan. -->

---

# A test model from parts you know
$$\frac{dy}{dt} = \alpha\,\frac{x^n}{K^n + x^n} - \delta\,y$$
- Production set by a Hill function of the input
- First-order decay, as in L03
- Ramp $x$ slowly up to 3, then back down
<!-- notes: Satuan sembarang, alpha = delta = K = 1. Masukan naik selama 400 satuan waktu dan turun selama 400, jauh lebih lambat daripada waktu respons 1/delta = 1. Tanya dulu: apakah kurva turun akan sama dengan kurva naik? -->

---

<!-- layout: picture -->
# Same path both ways: no memory
![A soft switch has no memory](../../build/l06-soft-switch.png)
Rising and falling sweeps coincide to within 0.016. The small gap is lag, not memory.
<!-- notes: Cold call: kalau sigmoid adalah sakelar, apakah ia ingat ke arah mana ia dibalik? Tidak. Selisih kecil itu keterlambatan - kalau landaian dipercepat, selisihnya membesar sebanding kecepatannya (Soal 6). -->

---

# Memory needs feedback
- L01's toggle switch holds its state after the inducer leaves
- Its genes repress each other: a feedback loop
- The model needed nonlinear, cooperative binding to work
- Sigmoid supplies the steepness; feedback supplies the memory
- Even $n \to \infty$ gives a step, still memoryless
<!-- notes: Kembali ke studi kasus L01 (Gardner, Cantor, Collins 2000). Model generik mereka menunjukkan nonlinieritas pengikatan protein-DNA mengompensasi asimetri komponen. Ini jembatan ke bab-bab berikutnya. -->

---

<!-- layout: section -->
# Part 6 - One technique, five rate laws

---

# The same moves, five times
- Michaelis-Menten: the complex is fast
- Competitive: two fast complexes, $K_M$ moves
- Non-competitive: three fast complexes, $V_{max}$ moves
- Cooperative binding: simultaneous binding gives the Hill function
- Hill regulation: $i/K_i$ becomes $(i/K_i)^n$
<!-- notes: Setiap baris berasal dari langkah yang sama: aksi massa untuk reaksi elementer, konservasi, ganti persamaan spesies cepat dengan aljabar, substitusi kembali, baca konstantanya. Exit ticket: sebutkan satu hal yang bisa dilakukan sigmoid tetapi tidak bisa oleh hiperbola, dan satu hal yang tetap tidak bisa dilakukannya. -->

---

# Practical and problem set
- Notebook 05 (planned): inhibition fingerprints, Hill fits, the ramp
- 1: reproduce the competitive derivation
- 2: diagnose three drugs; 3: uncompetitive inhibition
- 4: minimum $n$; 5: cooperative $i_{50}$
- 6: lag or memory? Design the test
<!-- notes: Notebook 05 belum terbit di repositori praktikum. Soal 5 dan 6 bisa dikerjakan di notebook Colab mana pun. Jawaban ada di bagian terlipat di akhir catatan. Soal 3 menutup rangkaian berjenjang yang dimulai di L05. -->

---

# Three sentences to carry forward
- Competitive inhibitors move $K_M$; allosteric ones lower $V_{max}$
- A sigmoid needs interacting sites; $n$ measures steepness
- A Hill factor is a soft switch; memory needs feedback
<!-- notes: Kalau mereka bisa mengucapkan tiga kalimat ini, dua pertemuan kinetika enzim sudah tercapai. -->
