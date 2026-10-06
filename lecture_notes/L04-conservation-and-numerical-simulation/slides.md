---
title: Conservation and Numerical Simulation
subtitle: TKBM262615 - Lecture 4
author: Matin Nuhamunada
date: 2026-09-30
---

<!-- layout: quote -->
> Differential equation models of biochemical and genetic systems are invariably nonlinear,
> and nonlinear models do not typically admit explicit solutions.
> -- Brian Ingalls, Mathematical Modelling in Systems Biology
<!-- notes: Bacakan keras-keras. Kalimat ini adalah alasan seluruh kuliah hari ini ada. Kalau persamaan tidak bisa diselesaikan, hanya ada dua jalan: kecilkan sistemnya secara eksak (konservasi), atau selesaikan secara numerik (Euler, lalu solve_ivp). Hari ini keduanya. -->

---

# Retrieval - what L03 left you holding
- Why is the rate for A + B a product, not a sum?
- Five species, three reactions: how many equations?
- What are the units of $k$ in a second-order rate law?
<!-- notes: Tanpa catatan, dari ingatan. Sudah diposting setelah L03. Jawaban: (1) laju sebanding dengan peluang tumbukan, dan peluang dua kejadian independen adalah perkalian; (2) lima persamaan, satu per spesies; (3) konsentrasi^-1 waktu^-1. Kalau nomor 3 macet, tulis analisis dimensinya di papan - 90 detik. -->

---

# Count the molecules, not the concentrations
- $A \to B$: every B that appears cost exactly one A
- Nothing enters the beaker, nothing leaves it
- So the total cannot move
<!-- notes: Ini pembuka konkret. Pegang dua spidol: satu A, satu B. Ubah satu A jadi B di depan kelas. Tanya: berapa jumlah total sekarang? Sama. Itu saja isi konsep konservasi - sisanya notasi. -->

---

<!-- layout: section -->
# Part 1 - Conservation in a closed system

---

# What "closed" buys you
- No inflow, no outflow, no synthesis, no degradation
- Whatever is passed around is fixed in total
- Every closed network has at least one conservation
<!-- notes: Tekankan "at least one". Jaringan tertutup dengan lima spesies bisa punya dua atau tiga konservasi independen. Jaringan terbuka boleh punya, boleh tidak - jangan diasumsikan. -->

---

# Route 1 - read it off the arrows
- Look at what gets passed along unchanged
- $A \to B$: each event moves one molecule, A to B
- Works while you can still eyeball the diagram
<!-- notes: Cara ini cepat tapi tidak scalable. Sebutkan sekarang bahwa cara kedua yang akan bertahan, supaya mereka tidak merasa cara kedua itu ritual yang tidak perlu. -->

---

# Route 2 - add the differential equations
$$\frac{d[A]}{dt} = -k[A], \qquad \frac{d[B]}{dt} = +k[A]$$
- Add them and the terms cancel
- A derivative that is zero for all time means a constant
<!-- notes: Turunkan di papan, jangan hanya ditampilkan. Jumlahkan ruas kiri, jumlahkan ruas kanan, tunjukkan -ka + ka = 0. Momen penting: dua jalan berbeda, satu jawaban - itu yang membuat jalur aljabar bisa dipercaya saat kimianya sudah terlalu rumit untuk dilihat. -->

---

# The conservation, written down
$$a(t) + b(t) = T \quad \text{for all } t$$
$$T = A_0 + B_0$$
- $T$ is set by the initial conditions, once
- After that it is a number you already know
<!-- notes: Tanyakan ke kelas: dari mana T datang? Dari kondisi awal, bukan dari konstanta laju. Ini yang membuat T berguna: satu bilangan yang sudah diketahui sebelum simulasi dijalankan. -->

---

# Conserved concentration is not conserved mass
- The conserved thing is a count of molecules
- A and B need not have the same molecular mass
- Ingalls separates the two on purpose
<!-- notes: Miskonsepsi utama halaman ini. Tanya langsung: "A -> B mengonservasi a + b. Apakah massa terkonservasi?" Hanya jika massa molekul A dan B sama, dan itu tidak harus. Jangan lewati ini - istilah "konservasi massa" di judul silabus justru mengundang salah baca. -->

---

# Structural, not parametric
- Does the conservation depend on the value of $k$?
- No. It holds for every rate constant
- It is a property of which arrows exist
<!-- notes: Cold call. Ini benih dari seluruh analisis struktur jaringan metabolik di Bab 5. Kalau ada yang menjawab "tergantung k", kembali ke penjumlahan dua persamaan: k pernah muncul, lalu saling meniadakan. -->

---

# The biological name for it
- Moiety: a group of atoms passed between molecules
- Phosphate groups, adenine nucleotides
- ATP + ADP + AMP is a moiety conservation
<!-- notes: Beri contoh yang mereka sudah kenal dari biokimia: total nukleotida adenin dalam sel praktis tetap dalam skala waktu menit, yang berpindah hanya gugus fosfatnya. NAD+ / NADH juga. Ini menjadikan konservasi biologi, bukan sekadar aljabar. -->

---

# Not every conservation is a sum
- One reaction producing C and D together
- Then $c - d$ is constant, not $c + d$
- Look for combinations, not totals
<!-- notes: Ingalls Latihan 2.1.8. Layak diberikan sebagai tugas justru karena mematahkan pola yang akan mereka generalisasi sendiri. Kalau waktu mepet, cukup sebutkan dan tinggalkan sebagai soal. -->

---

<!-- layout: section -->
# Part 2 - Using conservation to shrink a model

---

# What a conservation buys you
:::flow
Two coupled differential equations
--> substitute $b = T - a$\nEXACT, nothing approximated
One differential equation\nplus one line of arithmetic
--> set the derivative to zero
The steady state, by algebra
:::
Every arrow here is a rewriting. Nothing on this slide is an approximation.
<!-- notes: Ini peta Bagian 2, tunjukkan sebelum aljabarnya. Dua panah, dua langkah, dan keduanya eksak. Simpan gambar ini di ingatan mereka - slide dengan bentuk yang sama muncul di L05, dan di sana satu panahnya putus-putus. Kontras visual itu yang akan mengingatkan mereka bahwa QSSA adalah taruhan. -->

---

# Two ODEs become one ODE plus one line
- Systems of ODEs are much harder than single ODEs
- Substitute $b = T - a$ and B's equation disappears
- Solve for $a(t)$, then read $b(t)$ off
<!-- notes: Ini keuntungan praktisnya dan harus dinyatakan sebagai keuntungan. Mereka baru saja belajar bahwa sistem ODE tidak punya solusi eksplisit; di sini satu persamaan hilang tanpa biaya apa pun. -->

---

# Worked example - the reversible pair
$$\frac{da}{dt} = k_-(T-a) - k_+a = k_-T - (k_++k_-)a$$
- Two coupled equations, now one unknown
- The shape is production and decay, from L03
<!-- notes: Kerjakan substitusinya langsung di papan, jangan tampilkan hasil jadi. Biarkan kelas melihat b menghilang. Lalu tunjuk bentuk akhirnya: ini persis Contoh II dari praktikum notebook 02, dengan k_-T sebagai produksi dan (k_+ + k_-) sebagai peluruhan. -->

---

# The steady state falls out
$$a^{ss} = \frac{k_-T}{k_++k_-}, \qquad b^{ss} = \frac{k_+T}{k_++k_-}$$
- Set the derivative to zero and solve. Algebra, not calculus
- Check: they add back to $T$
<!-- notes: Dua hal. Pertama, cek penjumlahan itu wajib diucapkan - a^ss + b^ss = T, harus, karena konservasi berlaku juga di keadaan tunak. Kedua, perhatikan bahwa hanya rasio k+/k- yang menentukan pembagiannya, sama seperti Contoh IV di notebook praktikum. -->

---

# Steady state, in one slide
$$f(\mathbf{x}^{ss},\mathbf{p}) = 0$$
- Every concentration's rate of change is zero, at once
- Not "the reactions stopped": both still run, at equal rates
- You never touch the differential equation
<!-- notes: Ini jembatan, bukan bagian utama - keadaan tunak dikembangkan penuh di L05 dan Bab 4. Tapi katakan kalimat "steady, not static" hari ini, karena hinge question berikutnya bergantung padanya. -->

---

# Hinge question - what does doubling both do?
$$A \rightleftharpoons B \quad a(0)=3,\; b(0)=1 \text{ mM}$$
- You double both $k_+$ and $k_-$. Then:
- A: $T$ changes, $a^{ss}$ does not  B: neither changes
- C: $T$ holds, $a^{ss}$ changes  D: both change
<!-- notes: Mini-whiteboard, serentak. Jawaban B. A salah: T ditetapkan kondisi awal, konstanta laju tidak menyentuhnya. C salah: a^ss = k_-T/(k_+ + k_-), gandakan atas dan bawah, hasilnya sama - hanya rasio yang penting. D salah dua kali. Kalau lebih dari sepertiga memilih C, kerjakan aljabar penggandaannya di papan lalu tanya ulang. Jangan lanjut sebelum ini masuk. Istirahat setelah slide ini. -->

---

# Finding one in a network you cannot see
:::flow across
A list of\nreactions
--> rows are species,\ncolumns are reactions
The stoichiometry\nmatrix N
--> left nullspace
Every conserved\ncombination
:::
Three steps, and the middle one is bookkeeping rather than insight.
<!-- notes: Tunjukkan alurnya dulu, baru rumusnya di slide berikutnya. Poin yang perlu diucapkan: hanya kotak pertama yang butuh kimia. Dua kotak berikutnya mekanis - itulah sebabnya cara ini bertahan pada jaringan seukuran apa pun, sementara Jalur 1 berhenti bekerja di sekitar enam spesies. -->

---

# When you cannot eyeball it
$$\mathbf{w}^{T}\mathbf{N} = 0 \;\Longleftrightarrow\; \frac{d}{dt}(\mathbf{w}\cdot\mathbf{x}) = 0$$
- $\mathbf{N}$ is the stoichiometry matrix: species by reactions
- Conservations are the left nullspace of $\mathbf{N}$
<!-- notes: Di sinilah nullspace dari L02 akhirnya dipakai untuk sesuatu. Katakan itu terang-terangan. Baca persamaan ini sebagai kalimat: cari kombinasi bobot w yang membuat setiap reaksi tidak mengubah apa pun. -->

---

# Three lines of Python find them all
```
N = np.array([[-1.0], [1.0]])
null_space(N.T).ravel()  ->  [0.707, 0.707]
```
- Proportional to $[1, 1]$, which reads "$a + b$"
- Direction matters, scale does not
<!-- notes: Angka 0.707 selalu memancing pertanyaan. Jawab sebelum ditanya: hasilnya dinormalisasi, jadi yang bermakna arahnya. Kalikan 0.707 dengan akar 2 dan Anda dapat [1,1]. Jalankan sel ini live kalau ada waktu. -->

---

# Exact, and that word is doing work
- Nothing is approximated here
- The reduced model is the same model, written shorter
- Simulation preserves it to machine precision
<!-- notes: Simpan kalimat ini. L05 akan memakai reduksi yang kelihatan persis sama di atas kertas tapi merupakan taruhan, bukan penulisan ulang. Kontras itu adalah salah satu ide paling penting di seluruh mata kuliah, dan lebih mudah dilihat kalau versi eksaknya sudah dipasang lebih dulu. -->

---

<!-- layout: section -->
# Part 3 - Euler's method, and where the error comes from

---

# You have trusted a black box for three lectures
- L01, L02, L03: `solve_ivp`, handed to you
- Today it opens
<!-- notes: Ucapkan ini secara eksplisit. Kalimat ini yang membeli perhatian ruangan untuk lima menit turunan berikutnya. Jangan diperhalus. -->

---

# Start from the definition of a derivative
$$\frac{d}{dt}a(t) \;\approx\; \frac{a(t+h)-a(t)}{h}$$
- True in the limit; approximately true for small $h$
- Substitute it into $\frac{da}{dt} = f(a)$
<!-- notes: Tiga baris di papan, jangan ditampilkan jadi. Baris pertama definisi turunan dari L02, baris kedua substitusi, baris ketiga penataan ulang. Sebutkan dengan suara keras saat tanda hampir-sama diganti tanda sama dengan - di situlah seluruh galat masuk. -->

---

# Treat the approximation as an equality
$$a(t+h) = a(t) + h\,f(a(t))$$
- New value equals old value plus step times rate
- The rate is assumed constant across the step
- It is not constant. That is the error
<!-- notes: Baca versi kalimatnya keras-keras, bukan versi simbolnya. Mahasiswa yang bisa mengucapkan "nilai baru sama dengan nilai lama ditambah langkah kali laju" sudah memahami metode Euler; sisanya tinggal aritmetika. -->

---

# One Euler step, in three moves
:::flow across
Value now,\n$a(t)$
--> read the rate there,\n$f(a(t))$
Assume that rate\nholds all step
~~> add $h$ times it
Value one step on,\n$a(t+h)$
:::
The dashed arrow is the only approximation in the whole method.
<!-- notes: Panah putus-putus dipilih dengan sengaja dan layak ditunjuk. Dua langkah pertama eksak: nilai sekarang diketahui, lajunya dihitung dari model. Yang menjadi taruhan hanya asumsi bahwa laju itu bertahan sepanjang langkah. Semua galat Euler ada di satu panah itu, dan memperkecil h berarti memperpendek panah itu. -->

---

# Three steps by hand
$$a(h) = a(0) + hf(a(0))$$
- Take $\frac{da}{dt} = -a$, $a(0) = 1$, $h = 2/3$
- Compute three steps on paper, then compare to $e^{-t}$
<!-- notes: Kerjakan bersama, benar-benar di papan, angka demi angka: 1, lalu 1/3, lalu 1/9, lalu 1/27 = 0.037. Nilai eksaknya e^-2 = 0.135. Melihat aproksimasi buruk buatan sendiri jauh lebih berharga daripada peringatan apa pun. Beri waktu dua menit; jangan buru-buru. -->

---

<!-- layout: picture -->
# Both halves of today, in one figure
![Conservation is exact; Euler's error is something you chose](../../build/l04-conservation-and-euler.png)
Left: the sum never moves. Middle: Euler freezes the rate. Right: the price list.
<!-- notes: Panel A: dua konsentrasi bergerak, jumlahnya garis lurus - konservasi terlihat, bukan diceritakan. Panel B: titik-titik adalah satu-satunya nilai yang benar-benar dihitung Euler; ruas lurus di antaranya adalah asumsi laju konstan yang dibuat kelihatan. Panel C: kemiringan 1 di sumbu log-log berarti separuh h, separuh galat. -->

---

# Halving h halves the error. A bad deal.
```
h = 0.667   error = 0.0983
h = 0.333   error = 0.0475
h = 0.033   error = 0.0046
solve_ivp   error = 5.8e-14
```
- Ten times the work buys ten times the accuracy
- `solve_ivp` is twelve orders of magnitude better
<!-- notes: Ini definisi "metode orde satu", dinyatakan sebagai harga, bukan sebagai istilah. Lalu tunjuk baris terakhir: itulah alasan Euler dipelajari untuk dipahami, bukan untuk dipakai. -->

---

# Euler can also go unstable
- Large $h$: the numerical answer oscillates or diverges
- The true solution is decaying the whole time
- A property of the method, not of the biology
<!-- notes: Demo cepat kalau ada waktu: da/dt = -a dengan h = 2.5 memberikan tanda berganti-ganti dan membesar. Inilah alasan solver sungguhan mengatur ukuran langkahnya sendiri. Satu menit, tidak lebih. -->

---

# A mesh bug worth seeing fail once
```
np.arange(0, t_end + h, h)   # can overshoot t_end
np.linspace(0, t_end, n + 1) # lands on it exactly
```
- Symptom: the error stops halving when $h$ halves
- The answer is plausible and reported at the wrong time
<!-- notes: Bug nyata yang akan mereka temui, bukan catatan kaki. Gejalanya halus: jawabannya masuk akal, dan galatnya berhenti mengecil - yang terlihat seperti sifat metode, bukan seperti bug. Aturan praktisnya satu kalimat: jangan pernah membangun mesh floating-point dengan arange. -->

---

<!-- layout: section -->
# Part 4 - Solving ODEs in Python

---

# The whole call, with nothing hidden
```
sol = solve_ivp(rhs, [t0, t1], y0,
                args=(k1, k2),
                dense_output=True,
                rtol=1e-8, atol=1e-10)
```
- Signature is `rhs(t, y, *args)`: time first, always
- Prefer `solve_ivp` over the older `odeint`
<!-- notes: Tulis rhs untuk A <-> B di papan bersama-sama, lalu tunjuk setiap argumen. Perhatikan args: parameter dikirim lewat argumen, bukan lewat variabel global. Model dengan parameter global tidak bisa dipakai ulang dan tidak bisa disapu parameternya. -->

---

# Four settings worth knowing
- `args`: parameters in, no globals
- `dense_output`: evaluate anywhere, not just at solver steps
- `rtol`, `atol`: the default 1e-3 is loose
- `method`: swap it when the solver crawls
<!-- notes: Soal toleransi punya konsekuensi yang akan mereka temui di praktikum: dua integrasi independen dari sistem yang sama bisa berbeda di desimal keempat pada rtol default. Itu bukan bug di salah satunya. Setel toleransi setiap kali Anda berniat membandingkan dua hasil. -->

---

# What a simulation will not give you
- One run is one initial condition
- A formula shows how the answer depends on parameters
- A simulation fixes them, so you must run it again
<!-- notes: Ingalls memberi ini satu paragraf penuh dan bobotnya di kelas harus sama. Mahasiswa yang baru bisa memanggil solver cenderung menyimpulkan bahwa simulasi menggantikan aljabar. Dari a^ss = k_0/k_1 Anda bisa langsung membaca bahwa menggandakan k_0 menggandakan keadaan tunak; dari simulasi, Anda harus menebaknya dari banyak jalannya. -->

---

# Stiffness - a symptom to recognise
- Very fast and very slow reactions in one model
- Symptom: the solver takes tiny steps and crawls
- Try `method="LSODA"` or `method="Radau"`
<!-- notes: Sebutkan sebagai nama untuk dikenali, bukan topik untuk dikembangkan - tidak dibahas di Bab 2. Tapi mereka akan menabraknya begitu satu reaksi jauh lebih cepat dari yang lain, dan itu terjadi minggu depan pada kompleks enzim-substrat. -->

---

# In the practical this week
- Colab notebook 03: conservation, Euler, `solve_ivp`
- You write the Euler loop yourself, then compare
- The check to print: does $a + b$ stay flat?
<!-- notes: Repo praktikum: lab-biotek-bio-ugm/TKBM262615_Practicals. Notebook 02 sudah memuat empat jaringan sederhana; notebook 03 minggu ini menambahkan loop Euler dan sapuan ukuran langkah. Biasakan pola yang sama: cetak satu pemeriksaan, baru gambar grafik. Grafik yang mulus bukan bukti grafik yang benar. -->

---

# What to carry into L05
- A conservation is exact, structural, and free
- Reducing with it is rewriting, not approximating
- A numerical answer's accuracy is something you chose
<!-- notes: Pratinjau: minggu depan hukum aksi massa berhenti menjadi hukum laju yang benar, dan yang menyelamatkannya adalah konservasi enzim ditambah satu reduksi yang, tidak seperti hari ini, benar-benar sebuah taruhan. Bagikan soal latihan berjenjang, tenggat sebelum L05. -->
