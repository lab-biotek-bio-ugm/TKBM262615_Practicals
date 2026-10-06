---
title: Enzyme Kinetics I - Mechanism and the Michaelis-Menten Equation
subtitle: TKBM262615 Komputasi Biologi - Lecture 5
author: Matin Nuhamunada
date: 2026-10-07
---

<!-- layout: quote -->
> Experimental observations of enzyme-catalysed reactions show that they do not obey
> mass-action rate laws.
> -- Brian Ingalls, Mathematical Modelling in Systems Biology
<!-- notes: Bacakan keras-keras. Satu kalimat ini adalah alasan seluruh Bab 3 ada. Hukum aksi massa yang mereka pelajari di L03 dan pakai di L04 ternyata tidak berlaku untuk reaksi yang paling penting dalam sel. Hari ini kita cari tahu kenapa, dan apa penggantinya. -->

---

# Retrieval - what L04 left you holding
- Why is a conservation exact, and a reduction using it free?
- What does Euler assume across one step?
- Halve the step size. What happens to the error?
<!-- notes: Tanpa catatan, dari ingatan. Sudah diposting setelah L04. Jawaban: (1) konservasi mengikuti struktur jaringan, bukan nilai konstanta, jadi tidak ada yang diaproksimasi; (2) laju tetap sepanjang langkah, padahal tidak; (3) galat ikut separuh - metode orde satu. Nomor 1 adalah yang paling dibutuhkan hari ini. -->

---

# A straight line that is not there
- Mass action predicts $v = k[S]$: a line through the origin
- What is measured bends over and flattens
- The rate stops caring about substrate
<!-- notes: Gambar dua kurva di papan: garis lurus dari titik asal, dan kurva yang membelok dan mendatar. Tanya kelas mana yang salah, hukumnya atau pengukurannya. Jawabannya: tidak keduanya. Hukum aksi massa sedang ditanyai pertanyaan yang bukan bidangnya - ia berlaku untuk reaksi elementer, dan S -> P berkatalis enzim bukan reaksi elementer. -->

---

<!-- layout: section -->
# Part 1 - What an enzyme actually does
- One arrow on paper is three elementary reactions

---

# Lowers the barrier, not the destination
- The active site is complementary in shape and chemistry
- Binding lowers the barrier to the transition state
- Both directions speed up by the same factor
<!-- notes: Ini biokimia yang sudah mereka tahu, tapi bingkainya baru: enzim mengubah laju, bukan tujuan. Tekankan "both directions" - itu yang membawa ke slide berikutnya. -->

---

# Equilibrium is untouched, and it has to be
- Suppose a catalyst did shift the equilibrium
- Add it, remove it, add another, cycle forever
- You would extract work from nothing
<!-- notes: Ini argumen perpetual motion, dan layak dikerjakan sebagai penalaran, bukan diberikan sebagai aturan. Kalau katalis bisa menggeser kesetimbangan, Anda bisa memutar dua katalis bergantian dan menarik kerja tanpa masukan energi. Karena itu mustahil, katalis tidak bisa menggeser kesetimbangan. Aturannya jadi teorema, bukan catatan kaki empiris. -->

---

# One arrow is three reactions
- "$S \to P$, catalysed by an enzyme" is not elementary
- It is binding, unbinding, and conversion
- Mass action applies to those three, not to the lump
<!-- notes: Inilah diagnosisnya, dan seluruh kuliah bergantung padanya. Hukum aksi massa tidak gagal - kita hanya menerapkannya pada level yang salah. Turun satu level ke reaksi elementer, terapkan aksi massa di situ, lalu naik lagi. -->

---

# The three reactions, drawn out
:::flow across
Free enzyme\nplus substrate
--> binding $k_1$\nunbinding $k_{-1}$
The complex\nE and S joined
--> catalysis $k_2$
Product released,\nenzyme free again
:::
Mass action applies to each of these three. It never applied to the lump.
<!-- notes: Tunjuk kotak ketiga dan kotak pertama: enzimnya sama. Itulah siklusnya - enzim kembali ke keadaan awal, siap mengikat lagi, dan tidak pernah terpakai habis. Dari gambar ini konservasi enzim di Bagian 2 nanti terasa wajar, bukan trik aljabar. Tanya juga: reaksi mana yang cepat? Dua yang pertama. -->

---

# The mechanism, written down
$$S + E \;\underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}}\; C \;\overset{k_2}{\longrightarrow}\; P + E$$
- $C$ is the enzyme-substrate complex
- $k_2$ is the catalytic constant, often written $k_{cat}$
- Two simplifications got us here. Say them out loud
<!-- notes: Dua penyederhanaan yang Ingalls nyatakan terbuka, jadi kita juga: (1) dua kompleks (enzim-substrat dan enzim-produk) dilebur jadi satu, dengan asumsi interkonversinya cepat; (2) produk tidak pernah mengikat ulang enzim bebas, yang dibenarkan karena pengukuran laju di laboratorium biasanya dilakukan tanpa produk. Penyederhanaan kedua membuat hukum laju ini tidak dapat balik. -->

---

# Why saturation has to happen
- The enzyme pool is limited
- At high substrate, every active site is occupied
- Adding more S then barely moves the rate
<!-- notes: Tanya lebih dulu: apa yang harus benar supaya laju berhenti naik? Seseorang akan menjawab "enzimnya habis". Terima jawaban itu - itu jawaban yang benar, dan mereka baru saja menurunkan sendiri alasan fisis di balik bentuk kurva jenuh yang mereka lihat sejak L01. -->

---

<!-- layout: section -->
# Part 2 - Writing the equations down
- Mass action on each step, then one exact reduction

---

# Mass action, one arrow at a time
$$\frac{ds}{dt} = -k_1se + k_{-1}c \qquad \frac{dc}{dt} = k_1se - k_{-1}c - k_2c$$
- Four species, so four equations
- Every term is a rate law you already know
<!-- notes: Bangun keempatnya di papan, minta ruangan menyebutkan tiap suku. Jangan tampilkan jadi. Yang belum tampil di slide: de/dt = k_-1 c - k_1 s e + k_2 c, dan dp/dt = k_2 c. Ini latihan L03 murni, dan mereka harus merasakan bahwa ini mudah. -->

---

# A mirror symmetry, not a coincidence
$$\frac{de}{dt} = -\frac{dc}{dt}$$
- Every term in one appears negated in the other
- The enzyme is never consumed, only occupied
<!-- notes: Tunjuk suku demi suku di papan. Lalu tanya kelas: kalau dua turunan selalu berlawanan, apa yang bisa dikatakan tentang jumlahnya? Nol. Dan sesuatu yang turunannya nol adalah konstanta. Mereka menurunkan konservasinya sendiri, persis rute kedua dari L04. -->

---

# The enzyme conservation
$$e_T = e + c = \text{constant}$$
- Free enzyme plus bound enzyme, fixed for all time
- This is L04's move, exact and free
- Substitute $e = e_T - c$ and one equation disappears
<!-- notes: Namai secara eksplisit: enzim adalah moiety terkonservasi, contoh yang dijanjikan minggu lalu. Katakan juga bahwa reduksi ini eksak - tidak ada yang diaproksimasi. Itu penting karena reduksi berikutnya, lima slide dari sekarang, kelihatan persis sama di atas kertas dan sebenarnya sebuah taruhan. -->

---

# Three equations left
$$\frac{dc}{dt} = k_1s(e_T-c) - k_{-1}c - k_2c$$
- Plus $\frac{ds}{dt}$ and $\frac{dp}{dt}$
- Still nonlinear: the $sc$ product will not integrate by hand
<!-- notes: Titik jujur. Kita sudah pakai satu-satunya reduksi eksak yang tersedia dan tetap tidak bisa menyelesaikannya. Di sinilah pendekatan yang bersifat aproksimasi menjadi perlu, bukan sekadar nyaman. -->

---

<!-- layout: section -->
# Part 3 - The quasi-steady-state assumption
- The fast complex, replaced by algebra

---

# Two clocks in one mechanism
- Fast: S and E associate and dissociate
- Slow: S is converted through to P
- Reactions can differ in speed by orders of magnitude
<!-- notes: Ingalls Gambar 3.3A. Ide pemisahan skala waktu, diperkenalkan tepat saat dibutuhkan. Aturan praktis: faktor sepuluh sudah cukup untuk memperlakukan yang satu sebagai instan relatif terhadap yang lain. Ini bukan mesin baru, ini pengamatan tentang jam. -->


---

<!-- layout: picture -->
# One mechanism, two clocks
![The full mechanism on a logarithmic time axis](../../build/l05-mechanism-timecourse.png)
Complex half-formed at 0.004 s; half the substrate converted at 0.29 s.
<!-- notes: Keempat persamaan aksi massa, tanpa reduksi apa pun, sumbu waktu logaritmik. Tunjuk kurva kompleks (oranye): naik dan mendatar dalam beberapa milidetik. Lalu tunjuk substrat dan produk: perubahan besarnya baru terjadi di sekitar sepersepuluh detik. Rasio kedua jam kira-kira 66, jauh di atas aturan praktis faktor sepuluh. Tanya: selama kompleks mendatar, apakah kompleksnya konstan? Tidak persis - ia turun perlahan mengikuti s. Itu bibit slide "Solved, and it is not a constant". -->
---

# Two independent reasons C is fast
- Time constants: $\frac{1}{k_1+k_{-1}}$ against $\frac{1}{k_2}$
- Concentrations: in the cell $s \gg e_T$
- Either one is enough. Usually both hold
<!-- notes: Alasan kedua yang paling sering dilewatkan mahasiswa, dan justru sering yang dominan. Substrat sel biasanya jauh lebih banyak daripada enzimnya, jadi kolam enzim terisi dan kosong berkali-kali sementara konsentrasi substrat baru turun sedikit. Ingat angka ini - alasan kedua yang akan membatasi keberlakuan hasil kita di akhir kuliah. -->

---

# Freeze the fast, follow the slow
- A fast species reaches its steady state essentially instantly
- Then it keeps up with everything slower
- Replace its differential equation with an algebraic one
<!-- notes: Nyatakan prosedurnya sebagai prosedur umum lebih dulu, baru terapkan. Satuan aproksimasinya adalah spesies, bukan reaksi. Syaratnya: semua reaksi yang menyentuh spesies itu harus cepat. Untuk C: pengikatan, pelepasan, dan konversi - ketiganya menyentuh C, dan semuanya cepat dibanding perubahan s. -->

---

# The quasi-steady-state procedure
:::flow
Identify the fast species\nevery reaction touching it is fast
--> here that is C
Replace its differential equation\nwith an algebraic one
~~> THIS is the approximation
Solve that equation for the species
--> substitute into what remains
A smaller model, in the slow variables
:::
Four steps. Only the second one is a bet, and it is the only one that can be wrong.
<!-- notes: Nyatakan prosedurnya sebagai prosedur umum sebelum diterapkan, supaya mereka tahu ini teknik yang bisa dipakai ulang, bukan trik khusus enzim. Bandingkan bentuk gambar ini dengan diagram konservasi di L04: bentuknya sama, tapi di sana semua panah utuh. Satu panah putus-putus itulah seluruh perbedaan antara reduksi eksak dan aproksimasi. -->

---

# Set the complex's derivative to zero
$$0 = k_1s(e_T-c^{qss}) - k_{-1}c^{qss} - k_2c^{qss}$$
- Expand the first term
- Collect everything containing $c^{qss}$
<!-- notes: Langkah pengumpulan suku ini adalah tempat mahasiswa kehilangan benang merah, dan hanya butuh sembilan puluh detik kalau dikerjakan pelan. Kerjakan live: jabarkan k1*s*eT - k1*s*c, lalu kumpulkan c^qss(k_-1 + k2 + k1*s) = k1*s*eT. Jangan lompati satu baris pun. -->

---

# Solved, and it is not a constant
$$c^{qss}(t) = \frac{k_1e_T\,s(t)}{k_{-1}+k_2+k_1s(t)}$$
- Is there a $t$ in this expression?
- Yes. It moves whenever $s$ moves
<!-- notes: Cold call, langsung ke miskonsepsinya. Singkatan "set the derivative to zero" membuat mahasiswa menulis c = konstanta. Tunjuk s(t) di ruas kanan. Kalimat Ingalls layak dikutip: kita mengganti deskripsi diferensial dengan deskripsi aljabar yang mengatakan C mencapai seketika keadaan tunak yang akan dicapainya seandainya variabel lain tetap. Frasa yang perlu dipegang: "dari sudut pandang C". C tidak dibekukan; C selalu sudah menyusul. -->

---

<!-- layout: picture -->
# The assumption, tested
![The Michaelis-Menten curve, the QSSA under it, and what it costs](../../build/l05-michaelis-menten.png)
Panel B: the algebraic formula tracks the real complex, and it moves.
<!-- notes: Tunjuk panel B lebih dulu, bukan panel A. Garis putus-putus adalah rumus aljabar tanpa turunan sama sekali; garis tebal adalah kompleks sungguhan dari mekanisme penuh. Setelah transien pendek keduanya berimpit sampai 2.3% dari kolam enzim. Dan keduanya bergerak sepanjang waktu - itulah bukti visual untuk slide sebelumnya. Panel A dan C kita pakai nanti. -->

---

# What if you assume equilibrium instead?
- Michaelis and Menten, 1913: binding sits at equilibrium
- Briggs and Haldane, 1925: apply the QSSA to the complex
- Same curve, different formula for $K_M$
<!-- notes: Ini konteks sejarah yang sekaligus mengajarkan sesuatu. Asumsi kesetimbangan cepat memberi KM = k_-1/k1, murni konstanta disosiasi. QSSA memberi KM = (k_-1 + k2)/k1. Keduanya cocok dengan data yang sama. Yang kita pakai hari ini yang kedua, dan slide berikutnya menunjukkan kenapa asumsi kesetimbangan lebih rapuh. -->

---

<!-- layout: picture -->
# Two reductions, two fates
![Rapid equilibrium's error persists; the QSSA's error closes](../../build/l05-reduction-comparison.png)
On a simpler network: the equilibrium assumption stays wrong at steady state.
<!-- notes: Jaringan sederhana, bukan enzim, supaya argumennya terlihat telanjang. Asumsi kesetimbangan memaksakan syarat yang tidak dipenuhi keadaan tunak sejati, karena di keadaan tunak ada fluks yang mengalir melalui reaksi itu - maju tidak sama dengan mundur. QSSA memaksakan da/dt = 0, yang justru persis syarat keadaan tunak sejati. Satu fakta struktural menjelaskan kedua nasib itu. -->

---

<!-- layout: section -->
# Part 4 - The Michaelis-Menten equation
- Substitute back, tidy, and name what appears

---

# The whole derivation, in four moves
:::flow
Four mass-action ODEs\nfor S, E, C and P
--> enzyme conservation\n$e_T = e + c$ ... EXACT
Three ODEs,\nstill nonlinear
~~> QSSA on the complex\nAN APPROXIMATION
*$c$ as algebra,\nnot a differential equation
--> substitute into $dp/dt$
The Michaelis-Menten rate law
:::
One exact move and one bet. Everything the rate law can get wrong enters on the dashed arrow.
<!-- notes: Ini peta seluruh kuliah dan layak ditinggalkan di layar cukup lama. Minta kelas menyebutkan setiap panah sebelum Anda membacanya. Kalau ada yang bisa menunjuk panah putus-putus dan mengatakan "di situ letak sekuestrasi dan galat transien", mereka sudah memahami Bab 3, bukan menghafalnya. Kembali ke slide ini di akhir kuliah saat membahas di mana reduksinya patah. -->

---

# Substitute back
$$\frac{dp}{dt} = k_2c^{qss} = \frac{k_2k_1e_T\,s}{k_{-1}+k_2+k_1s}$$
- The rate of product formation is $k_2c$, always was
- Now $c$ is a formula in $s$, so the rate is too
<!-- notes: Sampai di sini kita punya hukum laju: laju sebagai fungsi konsentrasi substrat saja, tanpa persamaan diferensial untuk kompleks. Itulah yang dicari. Biarkan bentuk berantakan ini terpampang beberapa detik sebelum dirapikan - mahasiswa perlu melihat kekacauannya lebih dulu. -->

---

# Tidy it, then name what appears
$$v = \frac{k_2e_T\,s}{\frac{k_{-1}+k_2}{k_1}+s}$$
- Divide numerator and denominator by $k_1$
- Two groupings appear. Neither was planned
<!-- notes: Jangan sajikan Vmax dan KM sebagai definisi. Turunkan dulu dengan k berserakan, lihat kekacauannya, baru namai kelompoknya. Mahasiswa yang melihat kedua konstanta itu datang sebagai hasil merapikan akan mengerti kenapa justru keduanya yang bisa diukur. -->

---

# The Michaelis-Menten rate law
$$V_{max}=k_2e_T \qquad K_M=\frac{k_{-1}+k_2}{k_1} \qquad v=\frac{V_{max}\,s}{K_M+s}$$
- Derived, not postulated
- Called hyperbolic: the curve is part of a hyperbola
<!-- notes: Berhenti di sini. Ini penurunan terpenting dalam mata kuliah dan pantas mendapat jeda. Tanya ruangan dari mana asal setiap simbol: Vmax dari k2 kali enzim total, KM dari tiga konstanta laju dibagi satu. Tidak ada yang jatuh dari langit. -->

---

# Hinge question - does KM measure binding?
$$K_M = \frac{k_{-1}+k_2}{k_1}$$
- A: always  B: only when $k_2 \gg k_{-1}$
- C: only when $k_2 \ll k_{-1}$, then $K_M = k_{-1}/k_1$
- D: never
<!-- notes: Mini-whiteboard, serentak. Jawaban C. Periksa kedua limitnya live: dengan k2 = 0 tidak ada katalisis, KM menjadi k_-1/k1 yaitu konstanta disosiasi murni - itu benar-benar afinitas. Dengan k2 sangat besar, KM ~ k2/k1 dan tidak memuat informasi pengikatan sama sekali. A adalah miskonsepsi yang dibawa dari biokimia. D terlalu jauh. Jangan lanjut sebelum ini masuk. Istirahat setelah slide ini. -->

---

<!-- layout: section -->
# Part 5 - Reading the two constants
- What Vmax and KM tell you, and what they do not

---

# Vmax scales with how much enzyme you have
- $V_{max} = k_2e_T$: catalytic constant times total enzyme
- Double the enzyme and $V_{max}$ doubles
- It is not a property of the enzyme alone
<!-- notes: Tanya langsung: saya menggandakan konsentrasi enzim. Apa yang terjadi pada Vmax? Pada KM? Vmax menggandakan, KM tidak berubah. Ini diagnostik yang memisahkan kedua konstanta, dan ini menyiapkan kuliah inhibisi minggu depan dengan sempurna. -->

---

# kcat is the property of the protein
$$k_{cat} = \frac{V_{max}}{e_T} = k_2$$
- Turnovers per enzyme molecule per second
- Quote this when you mean "how good is this enzyme"
- Units: time$^{-1}$
<!-- notes: Perbedaan praktis. Vmax adalah sifat sebuah tabung reaksi; kcat adalah sifat sebuah protein. Kalau dua laboratorium melaporkan Vmax berbeda untuk enzim yang sama, mereka mungkin sama-sama benar - konsentrasi enzimnya berbeda. -->

---

# KM is where the curve bends
$$v(K_M) = \frac{V_{max}K_M}{K_M+K_M} = \frac{V_{max}}{2}$$
- The half-saturating concentration, by construction
- Units: concentration
- It sets where on the substrate axis saturation begins
<!-- notes: Substitusikan s = KM di depan kelas dan biarkan penyebutnya jadi 2KM. Pemeriksaan satu baris, tapi mengubah KM dari rumus yang dihafal menjadi sesuatu yang bisa mereka tunjuk di grafik. Lalu kembali ke panel A dari gambar tadi. -->

---

# Two regimes, one curve
$$s \ll K_M:\; v \approx \frac{V_{max}}{K_M}s \qquad s \gg K_M:\; v \approx V_{max}$$
- Low substrate: first order, the rate reports supply
- High substrate: zero order, the enzyme is the bottleneck
<!-- notes: Dua limit ini adalah cara membaca kurva jenuh apa pun, bukan hanya kurva enzim. Di rezim rendah, penyebut kira-kira KM saja; di rezim tinggi, penyebut kira-kira s saja dan s-nya saling meniadakan. Kerjakan keduanya di papan, masing-masing satu baris. -->

---

# What a cell can and cannot control
- In the linear regime, the enzyme reports substrate supply
- In the saturated regime, only more enzyme helps
- Adding substrate to a saturated pathway does nothing
<!-- notes: Tanya kelas: jalur metabolik Anda lambat dan enzimnya jenuh. Bagaimana mempercepatnya? Bukan dengan menambah substrat. Naikkan ekspresi enzimnya, atau cari enzim dengan kcat lebih tinggi. Ini konsekuensi teknik dari sebuah bentuk kurva, dan menjadikan Bab 3 terasa berguna. -->

---

# Where the reduction breaks
- The transient is wrong, by construction
- Substrate hides inside C, so the reduced model overcounts free S
- The error scales with $e_T$, not with luck
<!-- notes: Panel C dari gambar. Dengan eT = 1 mM selisihnya 0.84 mM, sekitar 17% dari substrat awal - terlihat jelas. Dengan eT = 0.01 mM tinggal 0.009 mM dan tidak terlihat. Ingalls sengaja melebih-lebihkan galat di gambarnya supaya mekanismenya kelihatan. Di sel, rasio substrat terhadap enzim jauh lebih tinggi, jadi efek ini dapat diabaikan. Jalankan kedua nilai eT live kalau ada waktu. -->

---

# Further reading, not derived today
- Kinetic order: how sensitive the rate is to $s$ - opens L06
- Two-substrate reactions: hold one fixed, the same form returns
- Both are in the notes and the wiki, not assessed this week
<!-- notes: Dua topik ini dipindah dari kuliah hari ini supaya penurunan Michaelis-Menten tidak terburu-buru. Orde kinetik akan dibuka di awal L06 karena di sana ia menjadi ukuran seberapa tajam sebuah sakelar. -->

---

# In the practical this week
- Colab notebook 04: the full mechanism beside its reduction
- Fit $V_{max}$ and $K_M$ to initial-rate data with `curve_fit`
- Sweep $e_T$: where does the approximation start to fail?
<!-- notes: Repo praktikum: lab-biotek-bio-ugm/TKBM262615_Practicals. Notebook 04 sedang diperbarui; saat ini yang terbit baru notebook 02. Soal 3 dan 5 di catatan kuliah ditulis supaya bisa dikerjakan di notebook itu. -->

---

# Problem set, in five rungs
- 1: reproduce today's derivation, closed notes
- 2: compute $V_{max}$, $K_M$, $k_{cat}$ from rate constants
- 3: read and fit initial-rate data
- 4: the 1913 equilibrium derivation (Ingalls Ex. 3.1.1)
- 5: find the $e_T$ where the reduction fails by 1%
<!-- notes: Soal berjenjang, dari yang dicontohkan penuh sampai yang hanya berupa pertanyaan. Jawaban ada di bagian terlipat di akhir catatan kuliah. Tenggat sebelum L06. -->

---

# What to carry into L06
- Chapter 3 is Chapter 2's QSSA, applied once
- $V_{max}$ scales with enzyme; $K_M$ does not
- $K_M$ is a binding affinity only when $k_2 \ll k_{-1}$
<!-- notes: Pratinjau: minggu depan sel mengecilkan laju ini dengan sengaja lewat dua cara, dan masing-masing menggeser konstanta yang berbeda. Lalu bentuk kurvanya sendiri berubah dari hiperbola menjadi sakelar. Kalau mereka bisa mengucapkan tiga kalimat ini, mereka siap. -->
