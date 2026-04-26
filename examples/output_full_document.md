

\frontmatter
\title \mbox\chancery F A N C y \\[2mm]
\chancery\Large an online documentation project on \\[3mm]
\chancery \underlineFunctional \underlineAnalysis and \underlineNon-\underlineCommutative Geometr\underliney
\addcontentslinetocchapterPreliminaries
\addcontentslinetocsectionTitlepage
\authorFounded by \scshape Markus J.~Pflaum
\maketitle

\phantomsection
\labelsection-phantom


<!-- XXSEC_DEF_SPLITTERXX\chapter*XXSEC_DEF_SPLITTERXXAuthorsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapter*Authors -->
(section-authors_1)=
# Authors
\addcontentslinetocsectionAuthors

The following people have contributed to the \mbox\chancery F A N C yProject, in alphabetical order: \\[2mm]
\scshape Fr\'ed\'eric Pierre-Jean Latr\'emoli\`ere \Paul Mitchener\Markus J.~Pflaum\Daniel Spiegel 
<!-- XXSEC_PREFIX_ENDXX\chapter*Authors -->

<!-- XXSEC_DEF_SPLITTERXX\chapter*XXSEC_DEF_SPLITTERXXCopyrightXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapter*Copyright -->
(section-copyright_1)=
# Copyright
\addcontentslinetocsectionCopyright

\textcopyright 2016--2020 Markus J.~Pflaum. The copyright of each chapter or section lies with its author(s); see the \hyperref[section-authors]Authors
and \hyperref[section-attribution]Attribution pages for authorships.

Permission is granted to copy, distribute and/or modify all parts of this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.

A copy of the GNU Free Documentation License, Version 1.3 license is included in the section entitled ``GNU FDL v1.3''

\tableofcontents
\addcontentslinetocsectionContents
<!-- XXSEC_PREFIX_ENDXX\chapter*Copyright -->

<!-- XXSEC_DEF_SPLITTERXX\chapter*XXSEC_DEF_SPLITTERXXIntroductionXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapter*Introduction -->
(section-introduction_1)=
# Introduction
\addcontentslinetocsectionIntroduction

The \mbox\chancery F A N C yProject is an open source textbook on functional analysis, the mathematics of quantum mechanics, noncommutative geometry and related topics.
<!-- XXSEC_PREFIX_ENDXX\chapter*Introduction -->

<!-- XXSEC_DEF_SPLITTERXX\chapter*XXSEC_DEF_SPLITTERXXAttributionXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapter*Attribution -->
(section-attribution_1)=
# Attribution
\addcontentslinetocsectionAttribution
The main author of this work is \textscMarkus J. Pflaum.

Chapter {ref}`chpt:general-topology_1`, *General Topology*, is based on the script *Foundations of Point Set Topology*
by \textscFr\'ed\'eric Latr\'emoli\`ere submitted to \hrefhttp://www.librimath.org\textsfLibri Mathematicae under the GNU FDL v1.3. The chapter is also part of the
\hrefhttp://www.librimath.org/CRingProjectCRingProject.

Chapter {ref}`chpt:measure-integration-theory_1`,
*Measure and Integration theory*, is based on the notes *Measure Theory and Integration* by \textscPaul Mitchener
submitted to \hrefhttp://www.librimath.org\textsfLibri Mathematicae under the GNU FDL v1.3.

\textscM.J.~Pflaum is the author of Chapter {ref}`chpt:topological-vector-spaces_1`,
*Topological Vector Spaces*.

Chapter {ref}`chpt:hilbert-spaces_1` *Hilbert Spaces* and Chapter {ref}`chpt:c*-algebras_1`
**$^*$-Algebras have been written by \textscMarkus J. Pflaum and \textscDaniel Spiegel.

\mainmatter
<!-- XXSEC_PREFIX_ENDXX\chapter*Attribution -->

<!-- XXSEC_DEF_SPLITTERXX\partXXSEC_DEF_SPLITTERXXFundamentalsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\partFundamentals -->
# Fundamentals
<!-- XXSEC_DEF_SPLITTERXX\chapterXXSEC_DEF_SPLITTERXXTools from AnalysisXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapterTools from Analysis -->
(chpt:tools-analysis_1)=
# Tools from Analysis
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXSome useful inequalitiesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionSome useful inequalities -->
(sec:useful-inequalities_1)=
# Some useful inequalities
In this section we collect several inequalities from real analysis which will be of use later in this monograph.

:::{prf:theorem} Young's inequality
:label: thm:Youngs-inequality_1
Let $a,b \geq 0$, and assume that $p,q > 1$ satisfy the relation $\frac 1p + \frac 1q =1$. Then

:::{math}
ab \leq \frac 1p a^p + \frac 1q b^q \: .
:::

Equality holds if and only if $a^p = b^q$.
:::


:::{prf:proof}

Since the second derivative $\exp''$ of the exponential function attains only positive values, the function $\exp$ is strictly convex that means satisfies

:::{math}
\exp \big( \lambda x + (1-\lambda) y \big) \leq
\lambda \exp ( x ) + (1-\lambda) \exp ( y )
:::

for all $x,y\in \mathbb{R}$ and $\lambda \in [0,1]$ with equality holding true if and only if $x = y$ or $\lambda \in \{ 1,0 \}$. Putting $x = p \ln a$, $y = q \ln b$, and $\lambda = \frac 1p$ one obtains

:::{math}
ab = \exp\big( \lambda x + (1-\lambda) y \big) \leq
\lambda \exp ( x ) + (1-\lambda) \exp ( y ) = \frac 1p a^p + \frac 1q b^q \: .
:::

Equality holds if and only if $x = y$ which is equivalent to $a^p = b^q$.
:::


:::{prf:theorem} Cauchy--Schwarz inequality for sums
:label: thm:Cauchy-Schwartz-inequality-for-sums_1
Let $v,w \in \C^n$. Then

:::{math}
\Big| \sum_{i=1}^n v_i \overline{w_i} \: \Big|^2 \leq \Big( \sum_{i1}^n |v_i|^2 \Big) \Big( \sum_{i=1}^n |w_i|^2 \Big).
:::

Equality holds true if and only if $v$ and $w$ are linearly dependant.
:::


:::{prf:proof}

Let us use the *inner product* notation

:::{math}
\langle v,w\rangle := \sum_{i=1}^n v_i \overline{w_i} \quad \text{for } v,w\in \C^n.
:::

Then the $\ell^2$-*norm*

:::{math}
\| v \| := \left( \sum_{i=1}^n |v_i|^2\right)^{1/2} = \langle v , v \rangle^{1/2}
:::

is well-defined and non-negative for any $v\in \C^n$. If $\|v \| =0$ or $\| w \|= 0$, then $v=0$ or $w=0$, and the claim is trivial. So we assume $\|v \|, \| w \| > 0$ and compute

:::{math}
:label: eq:inequality-chain_1
\begin{split}
0 \leq \, & \big\langle \|w\| v - \|v\| w , \|w\| v - \|v\| w \big\rangle =
\sum_{i=1}^n \big( \|w\| v_i - \|v\| w_i \big)\big( \|w\| \overline{v_i} - \|v\| \overline{w_i} \big) = \\ = \, & \sum_{i=1}^n \|w\|^2 v_i\overline{v_i} - \|w\| \|v\| v_i \overline{w_i} - \|w\| \|v\| w_i \overline{v_i}
+ \|v\|^2 w_i\overline{w_i} = \\ = \, & 2 \|v\|\|w\| \Big( \|v\|\|w\| - \Re \langle v,w \rangle \Big) .
\end{split}
:::

Now choose $c \in \C$ with $|c|=1$ such that $ c \langle v,w \rangle = |\langle v,w \rangle|$. Replacing $v$ by $cv$ in inequality {eq}`eq:inequality-chain_1` and observing that $\|cv \|$ and $ \| w \| $ are positive then entails

:::{math}
0 \leq \|c v\|\|w\| - \Re \langle c v,w \rangle = \|v\|\|w\| - \Re (c \langle v,w \rangle) =
\|v\|\|w\| - |\langle v,w \rangle|,
:::

which is the claimed Cauchy--Schwartz inequality for sums in abbreviated form.

Equality holds true if and only if $\|w\| c v - \|v\| w =0$. So if $\|v\|\|w\| = |\langle v,w \rangle| $, then $v$ and $w$ are linearly dependant. To show the converse, assume that $av =bw$ for some $a,b\in \C$ with $(a,b) \neq (0,0)$. Because we consider the nontrivial case where both $v$ and $w$ are nonzero, we can assume without loss of generality that $b=1$. But then

:::{math}
|\langle v,w \rangle |= |\langle v, av \rangle | = |a| \|v\|^2 = \|v\| \, \|w\| \ ,
:::

hence equality holds in this case. The proof is finished.
:::


\para Besides the $\ell^2$-norm on $\C^n$ one has the so-called $\ell^p$-norms $\| \cdot \| : \C^n \to \mathbb{R}_{\geq 0}$ for $p \geq 1$. They are defined by

:::{math}
\| v \|_p = \left( \sum_{k=1}^n |v_k|^p \right)^{1/p} \quad \text{for } v \in \C^n \ .
:::

The *maximum norm* or $\ell^\infty$-norm $\| \cdot \|_\infty$ is given by

:::{math}
\| v \|_\infty = \sup \big\{ |v_k| \bigm\vert k = 1,\ldots , n \big\} \ .
:::

The $\ell^p$-norms are all norms indeed as we will later see.

:::{prf:theorem} H\"older's inequality for sums
Let $p,q \in [1, \infty )$ such that $\frac 1p + \frac 1q =1$. Then

:::{math}
\sum_{k=1}^n | v_k w_k | \leq \| v \|_p \cdot \| w\|_q \quad \text{for all } v,w\in \C^n \ .
:::
:::


:::{prf:proof}

If $p=1$ or $q=1$ the claim is immediate, because then $q=\infty$ or $p=\infty$, respectively, and the two estimates

:::{math}
\sum_{k=1}^n | v_k w_k | \leq \left( \sum_{k=1}^n | v_k | \right) \cdot
\sup\big\{ |w_k| \bigm\vert k = 1,\ldots , n \big\}
:::

and

:::{math}
\sum_{k=1}^n | v_k w_k | \leq \left( \sum_{k=1}^n | w_k | \right) \cdot
\sup \big\{ |v_k| \bigm\vert k = 1,\ldots , n \big\}
:::

obviously hold. So we can assume $1 < p,q < \infty$. Moreover we can assume that both $v$ and $w$ are nonzero because otherwise the claim is trivial. Now observe that by Young's inequality

:::{math}
\frac{|v_k|}{\| v \|_p} \cdot \frac{|w_k|}{\| w \|_q} =
\left(\frac{|v_k|^p}{\| v \|_p^p} \right)^{1/p} \cdot \left(\frac{|w_k|^q}{\| w \|_q^q} \right)^{1/q}
\leq \frac 1p \frac{|v_k|^p}{\| v \|_p^p} + \frac 1q \frac{|w_k|^q}{\| w \|_q^q} \quad
\text{for } k=1,\ldots , n\ .
:::

Summing over all $k$ gives

:::{math}
\sum_{k=1}^n \frac{|v_k|}{\| v \|_p} \cdot \frac{|w_k|}{\| w \|_q} \leq
\frac 1p \frac{\|v\|_p^p}{\| v \|_p^p} + \frac 1q \frac{\|w\|_q^q}{\| w \|_q^q} =
\frac 1p + \frac 1q = 1 \ .
:::

Multiplication of both sides by $ \| v \|_p \cdot \| w\|_q$ entails H\"older's inequality.
:::



:::{prf:theorem} Minkowski's inequality for sums
Let $p \in [1, \infty )$. Then

:::{math}
\| v + w \|_p \leq \| v\|_q + \| w \|_p \quad \text{for all } v,w\in \C^n \ .
:::
:::



:::{prf:proof}

For $p=1$ the claim is trivial, likewise for $p=\infty$. So assume $1 < p < \infty$ and put $q := \frac{p}{p-1}$. Then $\frac 1p + \frac 1q =1$, and we can apply H\"older's inequality to compute

:::{math}
\begin{split}
\| v + w \|_p^p\, & = \sum_{k=1}^n | v_k + w_k|^p \leq
\sum_{k=1}^n |v_k| \, | v_k + w_k|^{p-1} + |v_k| \, | v_k + w_k|^{p-1}
\leq \\ &\leq \| v \|_p \cdot \left( | v_k + w_k|^{(p-1)q} \right)^{1/q} +
\| w \|_p \cdot \left( | v_k + w_k|^{(p-1)q} \right)^{1/q} = \\ & = \left( \| v \|_p + \| w \|_p \right) \, \| v + w \|_p^{p/q} \ .
\end{split}
:::

Minkowski's inequality follows.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionSome useful inequalities -->

<!-- XXSEC_PREFIX_ENDXX\chapterTools from Analysis -->

<!-- XXSEC_DEF_SPLITTERXX\chapterXXSEC_DEF_SPLITTERXXGeneral TopologyXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapterGeneral Topology -->
(chpt:general-topology_1)=
# General Topology
\IfFileExists../CRingProject/sections/category-topological-spaces 
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe category of topological spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe category of topological spaces -->
(sec:category-topological-spaces_1)=
# The category of topological spaces
<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXTopologies and continuous mapsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Topologies and continuous maps -->
## Topologies and continuous maps
:::{prf:definition} 
Let $X$ be a set. By a topology on $X$ on understands a set $\mathscr{T}$ of subsets of $X$ such that:

\setcounterenumi-1
(axiom:openness-full-empty-set-open_1)=
(Top1)
: The sets $X$ and $\emptyset$ are both elements of $\mathscr{T}$.

(axiom:openness-union-open-sets_1)=
(Top2)
: The union of any collection of elements of $\mathscr{T}$ is again in $\mathscr{T}$ that means if $(U_i)_{i\in I}$ is a family of elements $U_i\in \mathscr{T}$, then $\bigcup_{i\in I} U_i \in \mathscr{T}$.

(axiom:openness-finite-intersection-open-sets_1)=
(Top3)
: The intersection of finitely many elements of $\mathscr{T}$ is again in $\mathscr{T}$ that means for every natural $n$ and $U_1, \ldots , U_n \in \mathscr{T}$ one has $ \bigcap_{i = 1}^n U_i \in \mathscr{T}$.


A pair $(X,\mathscr{T})$ is a called a *topological space* when $X$ is a set and $\mathscr{T}$ a topology on $X$. Moreover, a subset $U$ of $X$ is called *open* if $U\in \mathscr{T}$ and *closed* if $\complement_X U \in \mathscr{T}$.
:::



:::{prf:remark} 


\itemindent
: Strictly speaking, Axiom {ref}`axiom:openness-full-empty-set-open_1` can be derived from Axioms {ref}`axiom:openness-union-open-sets_1` and {ref}`axiom:openness-finite-intersection-open-sets_1`, since the union of an empty family of subsets of $X$ coincides with $\emptyset$, and the intersection of an empty family of subsets of $X$ coincides with $X$. Nevertheless, it is useful to require it, since in proofs one often shows Axiom {ref}`axiom:openness-union-open-sets_1`
   only for non-empty families of open sets, and Axiom {ref}`axiom:openness-finite-intersection-open-sets_1` only for the case of the intersection of two open subsets. Then it is necessary to verify Axiom {ref}`axiom:openness-full-empty-set-open_1`, too, when one wants to prove that a given set of subsets of $X$ is a topology.

\itemindent
: When using the notation $\mathscr{T}_X$ for a topology we always mean that $\mathscr{T}_X$ is a topology on the space $X$.
:::



:::{prf:example} 
:label: ex:examples-topological-spaces_1


\itemindent
: For every set $X$ the power set $\mathscr{P}(X)$ is a topology on $X$. It is called the *discrete* or *strongest* topology on $X$.

\itemindent
: The set $\big\{ \emptyset , X \big\}$ is another topology on a set $X$ called the *indiscrete* or *trivial* or
   *weakest* topology on $X$. Unless $X$ is empty or has only one element, the discrete and indiscrete topologies differ.

\itemindent
: Let $S$ be a set $\{ 0, 1\}$. Then the set $\big\{ \emptyset , \{ 1 \}, \{ 0, 1 \} \big\} $ is a topology on $S$ which does neither coincide with the discrete nor the indiscrete topology. The set $S$ with this topology is called
   *Sierpi\'nski space*. The closed sets of the Sierpi\'nski space are $\emptyset$, $\{ 0 \}$ and $S$.

(ex:standard-topology-reals_1)=
\itemindent
: The *standard topology* on the set of real numbers $\mathbb{R}$ consists of all subsets $U\subset \mathbb{R}$ such that for each $x\in U$ there are real numbers $a,b$ satisfying $a < x < b$ and $  {\ltsbrak a,b \rtsbrak}  \subset U$. The standard topology on $\mathbb{R}$ will be denoted by $\mathscr{T}_{\mathbb{R}}$.
   
   Let us show that $\mathscr{T}_{\mathbb{R}}$ is a topology on $\mathbb{R}$ indeed. Obviously $\emptyset$ and $\mathbb{R}$ are elements of $\mathscr{T}_{\mathbb{R}}$. Let $U,V \in \mathscr{T}_{\mathbb{R}}$ and $x \in U\cap V$. Then there are $a,b,c,d \in \mathbb{R}$ such that $x \in  {\ltsbrak a,b \rtsbrak}  \subset U$ and $ x\in  {\ltsbrak c,d \rtsbrak}  \subset V$. Put $e := \max \{ a,c\}$ and $f := \min \{ b,d\}$. Then $x \in  {\ltsbrak e,f \rtsbrak}  \subset U \cap V$, which proves $U \cap V \in \mathscr{T}_{\mathbb{R}}$. If $(U_i)_{i\in I}$ is a family of elements $U_i \in \mathscr{T}_{\mathbb{R}}$ and $x \in \bigcup_{i\in I} U_i$, then there exists an $j \in I$ with $x \in U_j$. Choose $a,b \in \mathbb{R}$ such that $x \in  {\ltsbrak a,b \rtsbrak}  \subset U_j$. Then $x \in  {\ltsbrak a,b \rtsbrak}  \subset \bigcup_{i\in I} U_i$, which proves $\bigcup_{i\in I} U_i \in \mathscr{T}_{\mathbb{R}}$. If not mentioned differently, we always assume the set of real numbers to be equipped with the standard topology. The standard topology coincides with the metric topology induced by the euclidean metric on $\mathbb{R}$, see ERROR_UNDEFINED_LABEL__-1. One therefore often calls $\mathscr{T}_{\mathbb{R}}$ the *euclidean topology*
   on $\mathbb{R}$. We will use these terms interchangeably.

\itemindent
: The *standard topology* $\mathscr{T}_{\mathbb{Q}}$ on the set of rational numbers $\mathbb{Q}$ is defined analogously. It consists of all subset $U\subset \mathbb{Q}$ such that for each $x\in U$ there exist rational numbers $a,b$ with $a < x < b$ and $  {\ltsbrak a,b \rtsbrak}  \subset U$. Like for the reals one proves that $\mathscr{T}_{\mathbb{Q}}$ is a topology on $\mathbb{Q}$. Unless mentioned differently it is always assumed that $\mathbb{Q}$ comes equipped with the standard topology. Like for $\mathbb{R}$, the standard topology on $\mathbb{Q}$ coincides with the *euclidean topology* on $\mathbb{Q}$ which is the one induced by the euclidean metric.

\itemindent
: Let $X$ be a set, and let $\mathscr{T}_{cof}$ denote the set of all subset of $X$ which are either empty or have finite complement in $X$. Then $\mathscr{T}_{cof}$ is a topology on $X$ called the
   *cofinite topology*.

\itemindent
: Let $X$ be a set, and let $\mathscr{T}_{coc}$ denote the set of all subset of $X$ which are either empty or have countable complement in $X$. Then $\mathscr{T}_{coc}$ is a topology on $X$ called the
   *cocountable topology*.

\itemindent
: Let $X$ be a (nonempty) set, $(Y,\mathscr{T})$ be a topological space, and $f:X\rightarrow Y$ a function. Define
   
   :::{math}
   f^* \mathscr{T} := f^{-1} \mathscr{T} := \{ f^{-1}(U) \in \mathscr{P}(X) \mid U \in \mathscr{T} \} \ .
   :::
   
   Then $(X,f^*\mathscr{T})$ is a topological space. One calls $f^*\mathscr{T}$ the
   *initial topology on*$X$ with respect to $f$ or the *topology on*$X$ induced by $f$.
   
   Let us verify that $f^*\mathscr{T}$ is a topology on $X$ indeed. By $f^{-1}(Y)=X$ and $f^{-1}(\emptyset)=\emptyset$ the sets $X$ and $\emptyset$ are in $f^*\mathscr{T}$. Now let $(V_i)_{i\in I}$ be a family of elements of $f^*\mathscr{T}$. In other words we have, for each $i\in I$, $V_i = f^{-1} (U_i)$ for some $U_i\in \mathscr{T}$. Then $U := \bigcup_{i\in I} U_i \in \mathscr{T}$ and
   
   :::{math}
   \bigcup_{i\in I}V_i =\bigcup_{i\in I}f^{-1} (U_i) = f^{-1} \Big( \bigcup_{i\in I} U_i \Big) = f^{-1} (U) \in f^*\mathscr{T} \ .
   :::
   
   Finally, let $V_1,\ldots,V_n \in f^{-1}\mathscr{T}$. Then, by definition, there exist $U_1, \ldots , U_n \in\mathscr{T}$ such that $V_i=f^{-1}(U_i)$ for $i=1,\ldots , n$. Thus $U :=\bigcap_{i=1}^n U_i \in \mathscr{T}$ and
   
   :::{math}
   \bigcap_{i=1}^n V_i = \bigcap_{i=1}^n f^{-1}(U_i) = f^{-1} \Big( \bigcap_{i=1}^n U_i \Big) = f^{-1} (U) \in f^*\mathscr{T} \ .
   :::

\itemindent
: Let $(X,\mathscr{T})$ be a topological space, $Y$ a (nonempty) set, and $g:X\rightarrow Y$ a function. Define $g_* \mathscr{T} \subset \mathscr{P}(Y)$ as the set of all $U \subset Y$ such that $g^{-1} (U)\in \mathscr{T}$. Then $g_* \mathscr{T}$ is a topology on $Y$. It is called the *final topology on*$Y$ with respect to $g$ or the *topology on*$Y$ induced by $g$. If $g :X \to Y$ is a *quotient map*
   that means that $g$ is surjective, then the final topology on $Y$ induced by $g$ is also called the *quotient topology on*$X$ induced by $g$.
   
   Let us show why $g_* \mathscr{T}$ is a topology on $Y$. Obviously, $Y,\emptyset \in g_* \mathscr{T}$. Let $(U_i)_{i\in I}$ be a family of elements of $g_* \mathscr{T}$. Then $g^{-1} (U_i) \in \mathscr{T}$ for all $i\in I$ which entails
   
   :::{math}
   g^{-1} \Big( \bigcup\limits_{i\in I} U_i \Big) = \bigcup\limits_{i\in I} g^{-1} (U_i) \in \mathscr{T} ,
   :::
   
   hence $\bigcup\limits_{i\in I} U_i \in g_* \mathscr{T}$. If $U_1, \ldots U_k \in g_* \mathscr{T}$, then
   
   :::{math}
   g^{-1} (U_1\cap \ldots \cap U_k) = \bigcap_{i=1}^k g^{-1} (U_i) \in \mathscr{T} .
   :::
   
   So $U_1\cap \ldots \cap U_k \in g_* \mathscr{T}$ and the claim is proved.
:::


\para
\Crefsec:fundamental-examples-topologies on fundamental examples collects several more examples of topologies. For now, we will work out a few basic properties of topologies and their structure preserving morphisms, the continuous maps defined below.


:::{prf:definition} 
Let $(X,\mathscr{T}_X)$ and $(Y,\mathscr{T}_Y)$ be two topological spaces and assume that $f:X\rightarrow Y$ is a function. One says that $f$ is
*continuous* if for all $U \in \mathscr{T}_Y$ the preimage $f^{-1}(U)$ is open in $X$. The map $f$ is called *open* if $f(V)$ is open in $Y$ for all $V \in\mathscr{T}_X$.
:::



:::{prf:example} 
Any constant function $c : X \to Y$ between two topological spaces is continuous since the preimage of an open set in $Y$ is either the full set $X$ or empty depending on whether the image of $c$ is contained in the open set or not.
:::



:::{prf:theorem} 
:label: thm:category-topological-spaces_1


\itemindent
: The identity map $\mathrm{id}_X$ on a topological space $(X,\mathscr{T}_X)$ is continuous and open.

\itemindent
: Let $(X,\mathscr{T}_X)$, $(Y,\mathscr{T}_Y)$ and $(Z,\mathscr{T}_Z)$ be three topological spaces. Assume that $f:X\rightarrow Y$ and $g:Y\rightarrow Z$ are maps. If $f$ and $g$ are both continuous, so is $g\circ f$. If $f$ and $g$ are both open, then $g\circ f$ is open as well.

\itemindent
: Topological spaces as objects together with continuous maps as morphisms form a category. It is called the *category of topological spaces* and will be denoted by $\mathsf{Top}$.
:::



:::{prf:proof}

It is obvious by definition that the identity map $\mathrm{id}_X$ is continuous and open. Now assume that $f$ and $g$ are continuous and let $U\in\mathscr{T}_Z$. Then $g^{-1}(U)\in\mathscr{T}_Y$ by continuity of $g$. Hence $f^{-1}(g^{-1}(U))\in \mathscr{T}_X$ by continuity of $f$. So $g\circ f$ is continuous. If $f$ and $g$ are open maps, and $V\in\mathscr{T}_X$, then $f(V) \in \mathscr{T}_Y$ and $g\circ f (V) = g (f(V)) \in \mathscr{T}_Z$. Hence the composition of two open maps is open, too. The rest of the claim follows immediately.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Topologies and continuous maps -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXComparison of topologiesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Comparison of topologies -->
## Comparison of topologies
\para The initial topology $f^* \mathscr{T}_Y$ induced by a function $f:X\rightarrow Y$ between topological spaces is a subset of the topology on $X$ if and only if $f$ is continuous. This motivates the following definition.


:::{prf:definition} 
Let $X$ be a set. Let $\mathscr{T}_1$ and $\mathscr{T}_2$ be two topologies on $X$. One says that $\mathscr{T}_1$ is
*finer* or *stronger* than $\mathscr{T}_2$ and $\mathscr{T}_2$ is *coarser* or *weaker* than $\mathscr{T}_1$ when $\mathscr{T}_2\subset \mathscr{T}_1$.
:::


\para Of course, inclusion induces an order relation on topologies on a given set. A remarkable property is that any nonempty subset of the ordered set of topologies on a given set always admits a greatest lower bound.


:::{prf:theorem} 
:label: thm:topology-generated-set-topologies_1
Let $X$ be a set. Let $\mathfrak{S}$ be a nonempty set of topologies on $E$. Then the set

:::{math}
\mathscr{T}_\mathfrak{S} := \bigcap_{\mathscr{T} \in \mathfrak{S}} \mathscr{T} =
\big\{ U \in \mathscr{P}(X) \mid U \in \mathscr{T} \text{ for all }
\mathscr{T} \in \mathfrak{S} \big\}
:::

is a topology on $X$ and it is the greatest lower bound of $\mathfrak{S}$, where the order between topologies is given by inclusion. In other words, $\mathscr{T}_\mathfrak{S}$ is the finest topology contained in each topology from $\mathfrak{S}$.
:::



:::{prf:proof}

We first show that $\mathscr{T}_\mathfrak{S}$ is a topology. Since each $\mathscr{T} \in \mathfrak{S}$ is a topology on $X$, we have $\emptyset,X \in \mathscr{T}$ for all $\mathscr{T} \in \mathfrak{S}$. Hence $\emptyset,X \in \mathscr{T}_\mathfrak{S}$.

Let $(U_i)_{i\in I}$ be a nonempty family of elements $U_i \in \mathscr{T}_\mathfrak{S}$. Let $\mathscr{T} \in \mathfrak{S}$ be arbitrary. By definition of $\mathscr{T}_\mathfrak{S}$, we have $U_i \in \mathscr{T}$ for all $i\in I$. Since $\mathscr{T}$ is a topology, $\bigcup_{i \in I} U_i \in \mathscr{T}$. Hence, as $\mathscr{T}$ was arbitrary, $\bigcup_{i\in I} U_i \in \mathscr{T}_\mathfrak{S}$.

Now, let $U_1,\ldots , U_n \in \mathscr{T}_\mathfrak{S}$. Let $\mathscr{T} \in \mathfrak{S}$ be arbitrary. By definition of $\mathscr{T}_\mathfrak{S}$, we have $U_1, \ldots , U_n \in \mathscr{T}$. Therefore, $U_1 \cap \ldots \cap U_n \in \mathscr{T}$ since $\mathscr{T}$ is a topology. Since $\mathscr{T}$ was arbitrary in $\mathfrak{S}$, we conclude that $U_1 \cap \ldots \cap U_n \in \mathscr{T}_\mathfrak{S}$ by definition.

So $\mathscr{T}_\mathfrak{S}$ is a topology on $X$. By construction, $\mathscr{T}_\mathfrak{S} \subset \mathscr{T}$ for all $\mathscr{T} \in \mathfrak{S}$, so $\mathscr{T}_\mathfrak{S}$ is a lower bound for $\mathfrak{S}$. Assume given a new topology $\mathcal{Q}$ on $X$ such that $\mathcal{Q} \subset \mathscr{T}$ for all $\mathscr{T} \in\mathfrak{S}$. Let $U \in \mathcal{Q}$. Then we have $U \in \mathscr{T}$ for all $\mathscr{T} \in \mathfrak{S}$. Hence by definition $U\in \mathscr{T}_\mathfrak{S}$. So $\mathcal{Q} \subset \mathscr{T}_\mathfrak{S}$ and thus $\mathscr{T}_\mathfrak{S}$ is the greatest lower bound of $\mathfrak{S}$.
:::



:::{prf:corollary} 
Let $X$ be a set, $(Y,\mathscr{T})$ be a topological space, and $f:X\to Y$ a map. The coarsest topology on $X$ which makes $f$ continuous is the initial topology $f^*\mathscr{T}$.
:::



:::{prf:proof}

Let $\mathfrak{S}$ be the set of all topologies on $X$ such that $f$ is continuous. By definition, $f^*\mathscr{T}$ is a lower bound of $\mathfrak{S}$. Moreover, $f^* \mathscr{T} \in \mathfrak{S}$. Hence $f^*\mathscr{T}$ is the coarsest topology making the function $f:X\rightarrow Y$ continuous.
:::



:::{prf:proposition} 
Let $(X,\mathscr{T})$ be a topological space, $Y$ a set, and $g:X\to Y$ a map. The finest topology on $Y$ which makes $g$ continuous is the final topology $g_*\mathscr{T}$.
:::



:::{prf:proof}

Let $\mathscr{S}$ be a topology on $Y$ so that $g:(X,\mathscr{T})\to(Y,\mathscr{S})$ is continuous. Let $U\in \mathscr{S}$. Then $g^{-1} (U)\in \mathscr{T}$ by continuity of $g:(X,\mathscr{T})\to(Y,\mathscr{S})$. Hence $U\in g_*\mathscr{T}$ by definition, and $\mathscr{S} \subset \mathscr{T}$. Since $g:(X,\mathscr{T})\to (Y,g_*\mathscr{T})$ is continuous by definition, the claim follows.
:::

\para We can use \Crefthm:topology-generated-set-topologies to define other interesting topologies. Note that trivially $\mathscr{P}(X)$ is a topology on a given set $X$, so given any $\mathscr{S}\subset \mathscr{P}(X)$ there is at least one topology containing $\mathscr{S}$. From this:


:::{prf:theorem} 
Let $X$ be a set, and $\mathscr{S}$ a subset of $\mathscr{P}(X)$. The greatest lower bound of the set

:::{math}
\mathfrak{S} = \{ \mathscr{T} \in \mathscr{P}(\mathscr{P}(X))\mid \mathscr{T}
\textrm{ is a topology on } X \: \& \: \mathscr{S} \subset \mathscr{T} \}
:::

is the coarsest topology on $X$ containing $\mathscr{S}$. We call it the
*topology generated by*$\mathscr{S}$ on $X$ and denote it by $\mathscr{T}_\mathscr{S}$. The topology $\mathscr{T}_\mathscr{S}$ consists of unions of finite intersections of elements of $\mathscr{S}$ that means

:::{math}
\mathscr{T}_\mathscr{S} = \Big\{ U \in \mathscr{P}(X) \mid \exists J \, \forall j\in J \, \exists n_j\in \mathbb{N} \,
\exists U_{j,1},\ldots ,U_{j,n_j} \in \mathscr{S} : \: U = \bigcup_{j\in J} \bigcap_{k=1}^{n_j} U_{j,k} \Big\} \ .
:::
:::



:::{prf:proof}

By definition of $\mathfrak{S}$ and \Crefthm:topology-generated-set-topologies, $\mathscr{T}_\mathfrak{S} = \bigcap_{\mathscr{T} \in \mathfrak{S}} \mathscr{T} $ is a topology on $X$ which contains $\mathscr{S}$. Hence $\mathscr{T}_\mathfrak{S}$ is an element of $\mathfrak{S}$ and a subset of any element of $\mathfrak{S}$. The first claim follows. To verify the second, observe that it suffices to show that

:::{math}
\mathscr{R} := \Big\{ U \in \mathscr{P}(X) \mid \exists J \, \forall j\in J \, \exists n_j\in \mathbb{N} \,
\exists U_{j,1},\ldots ,U_{j,n_j} \in \mathscr{S} : \: U = \bigcup_{j\in J} \bigcap_{k=1}^{n_j} U_{j,k} \Big\}
:::

is a topology. The set $\mathscr{R}$ being a topology namely entails $ \mathscr{T}_\mathscr{S} \subset \mathscr{R} $ because $ \mathscr{S} \subset \mathscr{R}$. The inclusion $\mathscr{R} \subset \mathscr{T}_\mathscr{S}$ is clear by definition, since $\mathscr{T}_\mathscr{S}$ is a topology containing $\mathscr{S}$. So let us show that $\mathscr{R}$ is a topology. Obviously $\emptyset$ and $X$ are elements of $\mathscr{R}$ because $\bigcup_{i\in \emptyset} U_i = \emptyset$ and $\bigcap_{k=1}^0 U_k = X$. Now assume that $(U_i)_{i\in I}$ is a family of elements of $\mathscr{R}$. Then there exists for each $i\in I$ a set $J_i$ and for every $j\in J_i$ a natural number $n_{i,j}$ together with elements $U_{i,j,1}, \ldots , U_{i,j,n_{i,j}} \in \mathscr{S}$ such that

:::{math}
U_i = \bigcup_{j\in J_i} \bigcap_{k=1}^{n_{i,j}} U_{i,j,k} \ .
:::

Put $J := \bigcup_{i\in I} \{ i \} \times J_i$. Then

:::{math}
U := \bigcup_{i\in I} U_i = \bigcup_{i\in I} \bigcup_{j\in J_i} \bigcap_{k=1}^{n_{i,j}} U_{i,j,k}
= \bigcup_{(i,j) \in J} \bigcap_{k=1}^{n_{i,j}} U_{i,j,k} \in \mathscr{R} \ .
:::

Last assume $U_1, \ldots U_n \in \mathscr{T}$ where $n\in \mathbb{N}$. Then one can find for each $i \in \{ 1,\ldots, n \}$ a set $J_i$ and for every $j\in J_i$ a natural number $n_{i,j}$ together with elements $U_{i,j,1}, \ldots , U_{i,j,n_{i,j}} \in \mathscr{S}$ such that

:::{math}
U_i = \bigcup_{j\in J_i} \bigcap_{k=1}^{n_{i,j}} U_{i,j,k} \ .
:::

Put $J := J_1 \times \ldots \times J_n$. Then

:::{math}
U := \bigcap_{i=1}^n U_i = \bigcap_{i=1}^n \bigcup_{j\in J_i} \bigcap_{k=1}^{n_{i,j}} U_{i,j,k} =
\bigcup_{(j_1,\ldots ,j_n)\in J} \: \bigcap_{k_1=1}^{n_{1,j_1}} U_{1,j_1,k_1} \cap \ldots \cap \bigcap_{k_n=1}^{n_{n,j_n}} U_{n,j_n,k_n}
\in \mathscr{R} \ .
:::

Hence $\mathscr{R}$ is a topology, indeed, and the proposition is proved.
:::



:::{prf:definition} 
Let $X$ be a set, and $\mathscr{T}$ a topology on $X$. One calls a subset $\mathscr{S} \subset \mathscr{T}$ a *subbase* (or *subbasis*) of the topology if $\mathscr{T}$ coincides with $\mathscr{T}_\mathscr{S}$. If in addition $X = \bigcup_{S\in \mathscr{S}} S$, the subbase $\mathscr{S}$ is said to be *adequate*.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Comparison of topologies -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXBases of topologiesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Bases of topologies -->
## Bases of topologies
\para When inducing a topology from a family $\mathscr{B}$ of subsets of some set $X$, the fact that $\mathscr{B}$ enjoys the following property greatly simplifies the description of the topology $\mathscr{T}_\mathscr{B}$ generated by $\mathscr{B}$.


:::{prf:definition} 
Let $X$ be a set. A *base* (or *basis*) on $X$ is a subset $\mathscr{B}$ of the powerset $\mathscr{P}(X)$ such that


(Bas1)
: $X = \bigcup_{B \in \mathscr{B}}B $,

(Bas2)
: For all $B_1,B_2 \in \mathscr{B}$ and all $ x \in B_1 \cap B_2$ there exists a $B \in \mathscr{B}$ such that $x \in B$ and $B \subset B_1 \cap B_2$.
:::


The main purpose for this definition stems from the following theorem:


:::{prf:theorem} 
Let $X$ be some set. Let $\mathscr{B}$ be a base on $X$. Then the topology generated by $\mathscr{B}$ coincides with the set of unions of elements of $\mathscr{B}$ that means

:::{math}
\mathscr{T}_\mathscr{B} = \left\{ \bigcup_{B \in \mathscr{U}} B \in \mathscr{P}(\mathscr{P}(X)) \Bigm\vert \mathscr{U} \subset \mathscr{B} \right\} \ .
:::
:::



:::{prf:proof}

Denote, for this proof, the set $\big\{ \bigcup_{B \in \mathscr{U}} B \bigm\vert \mathscr{U} \subset \mathscr{B} \big\}$ by $\mathscr{S}$ and let us abbreviate $\mathscr{T}_\mathscr{B}$ by $\mathscr{T}$. We wish to prove that $\mathscr{T} = \mathscr{S}$. First, note that $\mathscr{B}\subset \mathscr{S}$ by construction. By definition, $\mathscr{B} \subset \mathscr{T}$. Since $\mathscr{T}$ is a topology, it is closed under arbitrary unions. Hence $\mathscr{S} \subset \mathscr{T}$. To prove the converse, it is sufficient to show that $\mathscr{S}$ is a topology. As it contains $\mathscr{B}$, and $\mathscr{T}$ is the smallest such topology, this will provide us with the inverse inclusion. By definition, $\bigcup_{B\in \emptyset}B = \emptyset$ and thus $\emptyset \in \mathscr{S}$. By assumption, since $\mathcal{B}$ is a base, $X = \bigcup_{B\in \mathscr{B}}B$ so $X\in \mathscr{S}$. As the union of unions of elements in $\mathscr{B}$ is a union of elements in $\mathscr{B}$, $\mathscr{S}$ is closed under abritrary unions. Now, let $B_1,B_2$ be elements of $\mathscr{B}$. If $B_1\cap B_2= \emptyset$ then $B_1\cap B_2 \in \mathscr{S}$. Assume that $B_1$ and $B_2$ are not disjoints. Then by definition of a base, for all $x\in B_1\cap B_2$ there exists $B_x \in \mathscr{B}$ such that $x\in B_x$ and $B_x \subset B_1\cap B_2$. So

:::{math}
B_1\cap B_2 = \bigcup_{x\in B_1\cap B_2} B_x \ ,
:::

and therefore, by definition, $B_1\cap B_2 \in \mathscr{S}$. We conclude that the intersection of two arbitary elements in $\mathscr{S}$ is again in $\mathscr{S}$ by using the distributivity of the union with respect to the intersection.
:::



:::{prf:definition} 
We shall say that a base $\mathscr{B}$ on a set $X$ is a *base for a topology*$\mathscr{T}$ on $X$ when the smallest topology containing $\mathscr{B}$ coincides with $\mathscr{T}$, in other words when $\mathscr{T} = \mathscr{T}_\mathscr{B}$.
:::


The typical usage of the preceding theorem comes from the following result.


:::{prf:corollary} 
Let $\mathscr{B}$ be a base for a topology $\mathscr{T}$ on $X$. A subset $U$ of $X$ is in $\mathscr{T}$ if and only if for evry $x \in U$ there exists $B \in \mathscr{B}$ such that $x\in B$ and $B \subset U$.
:::



:::{prf:proof}

We showed that any open set for the topology $\mathscr{T}$ is a union of elements in $\mathcal{B}$. Hence if $x \in U$ for $U \in \mathscr{T}$ then there exists $B\in\mathcal{B}$ such that $x\in B$ and $B \subset U$. Conversely, if $U$ is some subset of $X$ such that for all $x \in U$ there exists $B_x\in\mathscr{B}$ such that $x\in B_x$ and $B_x \subset U$, then $U = \bigcup_{x \in U} B_x$ and thus $U\in \mathscr{T}$.
:::


The last result in this section is a useful tool for showing continuity of a map.


:::{prf:proposition} 
Let $(X,\mathscr{T}_X)$ and $(Y,\mathscr{T}_Y)$ be two topological spaces, $\mathscr{A}$ a base for the topology $\mathscr{T}_X$ and $\mathscr{B}$ a base for the topology $\mathscr{T}_Y$. Assume further that $f:X\to Y$ is a map. Then the following are equivalent:



(ite:continuity-function_1)=
(i)
: The map $f$ is continuous.

(ite:preimages-open-sets-exhausted-base-elements_1)=
(ii)
: For every open $V \subset Y$ and all $x\in f^{-1}(V)$ there exists $A \in \mathscr{A}$ such that $x \in U$ and $f(A) \subset V$.

(ite:preimages-base-elements-open_1)=
(iii)
: For every $B\in \mathscr{B}$ the preimage $f^{-1} (B)$ is open in $X$.
:::



:::{prf:proof}

Obviously, {ref}`ite:continuity-function_1` implies {ref}`ite:preimages-base-elements-open_1`.

Assume that {ref}`ite:preimages-base-elements-open_1` holds and that $V \subset Y$ is open. Let $x\in f^{-1}(V)$ and put $y=f(x)$. Then $y \in V$. Since $\mathscr{B}$ is a base for the topology $\mathscr{T}_Y$ there exists $B\in \mathscr{B}$ such that $x\in B \subset V$. By assumption $f^{-1}(B)$ is open in $X$ and $x \in f^{-1}(B)$. Since $\mathscr{A}$ is a base for the topology $\mathscr{T}_X$, there exists $A \in \mathscr{A}$ such that $x \in A \subset f^{-1}(B)$. Since $f^{-1}(B) \subset f^{-1}(V)$, {ref}`ite:preimages-open-sets-exhausted-base-elements_1`
follows.

Now assume that {ref}`ite:preimages-open-sets-exhausted-base-elements_1` holds true. Let $V \subset Y$ be open, and choose for every $x\in f^{-1}(V)$ a base element $A_x\in \mathscr{A}$ such that $x \in A_x \subset f^{-1}(V)$. Then $ f^{-1}(V) = \bigcup_{x\in f^{-1}(V)} A_x $ which is open in $X$. Hence $f$ is continuous.
:::



<!-- XXSEC_PREFIX_ENDXX\subsection*Bases of topologies -->

<!-- XXSEC_PREFIX_ENDXX\sectionThe category of topological spaces -->


\IfFileExists../CRingProject/sections/fundamental-examples-topologies \section[Examples and categorical constructions of topological spaces]Examples and categorical constructions of topological spaces
\labelsec:fundamental-examples-topologies

This section provides various examples and constructions of topological spaces which will be used all along in this monograph.


<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXThe order topologyXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*The order topology -->
## The order topology
:::{prf:proposition} 
Let $(X,\leq)$ be a totally ordered set, and assume that $\infty, -\infty$ are two symbols not in $X$. Define $ {[ -\infty, \infty ]} _X = X \cup \{-\infty,\infty \}$ and extend $\leq$ to $ {[ -\infty, \infty ]} _X$ by requiring $x \leq y$ for $x,y \in  {[ -\infty, \infty ]} _X$ to hold when $x,y \in X$ and $x \leq y$, when $x = -\infty$, or when $y = \infty$. Then $ {[ -\infty, \infty ]} _X$ together with the relation $\leq$ becomes a totally ordered set as well, and the embedding $X \hookrightarrow  {[ -\infty,\infty ]} _X$ is order-preserving.
:::


:::{prf:proof}

By definition, the relation $\leq$ on $ {[ -\infty,\infty ]} _X$ is reflexive, and any two elements of $ {[ -\infty,\infty ]} _X$ are comparable. Also by definition, $x\leq -\infty$ is equivalent to $x =-\infty $ and $\infty \leq y$ equivalent to $y =\infty$. Since the restriction of $\leq$ to $X$ is antisymmetric by assumption, $\leq $ therefore is an antisymmetric relation on $ {[ -\infty, \infty ]} _X$. Using the definition of $\leq$ again one finally observes that for $x,y,z \in  {[ -\infty, \infty ]} _X$ the following implications hold true.

:::{math}
\begin{split}
-\infty \leq y \: \& \: y \leq z & \implies -\infty \leq z \\ x \leq -\infty \: \& \: - \infty \leq z & \implies x = -\infty \leq z \\ x \leq y\: \& \: y \leq - \infty & \implies x = y = -\infty \\ x \leq y\: \& \: y \leq \infty & \implies x \leq \infty \\ x \leq \infty \: \& \: \infty \leq z & \implies x \leq \infty = z \\
\infty \leq y \: \& \: y \leq z & \implies \infty = y =z \ .
\end{split}
:::

Since its restriction to $X$ is already transitive, transitivity of $\leq$ now follows and the proposition is proved.
:::



:::{prf:remark} 
For the rest of this paragraph we always assume that an ordered set $(X,\leq)$ does not contain the symbols $\infty, -\infty$, and that $ {[ -\infty, \infty ]} _X$ and the extended order relation $\leq$ are defined as in the preceding proposition.
:::



:::{prf:definition} 
For a totally ordered set $(X,\leq)$, define *intervals* with boundaries $x,y \in  {[ -\infty, \infty ]} $ as follows:

:::{math}
\begin{split}
 {\ltsbrak x,y \rtsbrak}  :=  {\ltsbrak x,y \rtsbrak} _{\, X} := \big\{ z \in  {[ -\infty, \infty ]}  \mid x < z < y \big\} \ , \\
 {[ x,y \rtsbrak}  :=  {[ x,y \rtsbrak} _{\, X} := \big\{ z \in  {[ -\infty, \infty ]}  \mid x \leq z < y \big\} \ , \\
 {\ltsbrak x,y ]}  :=  {\ltsbrak x,y ]} _X := \big\{ z \in  {[ -\infty, \infty ]}  \mid x < z \leq y \big\} \ ,\\
 {[ x,y ]}  :=  {[ x,y ]} _X := \big\{ z \in  {[ -\infty, \infty ]}  \mid x \leq z \leq y \big\} \ . \\
\end{split}
:::

The intervals $ {\ltsbrak x,y \rtsbrak} _{\, X}$ are called *open intervals*, intervals of the form $ {[ x,y ]} _X $ are called
*closed intervals*, and intervals of the form $ {[ x,y \rtsbrak} _{\, X}$ or $ {\ltsbrak x,y ]} _X$ are the
*half-open intervals*.
:::



:::{prf:remark} 


\itemindent
: Note that in case $x=y$ only the closed interval $ {[ x,x ]} _X $ is non-empty. In case $y < x$ all the intervals $ {\ltsbrak x,y \rtsbrak} _{\, X}$, $ {[ x,y \rtsbrak} _{\, X}$, $ {\ltsbrak x,y ]} _X$, and $ {[ x,y ]} _X$ are empty.

\itemindent
: We mostly use the notation $ {\ltsbrak x,y \rtsbrak} $, $ {[ x,y ]} $, etc.~for intervals and denote the $X$ in intervals only when otherwise some ambiguity could appear.
:::



:::{prf:definition} 
Let $(X,\leq)$ be a totally ordered set. Then the topology generated by the set

:::{math}
\mathscr{I}_X = \big\{ \,  {\ltsbrak x,y \rtsbrak}  \in \mathscr{P}(X)\mid x,y \in  {[ -\infty , \infty ]} 
\: \& \: x \leq y \big\}
:::

is called the *order topology* on $X$. It is usually denoted $\mathscr{T}_{(X,\leq)}$.
:::



:::{prf:proposition} 
Let $(X,\leq)$ be a totally ordered set. Then the set $\mathscr{I}_X$ is a base for the order topology on $X$. A subbase of the order topology is given by the set $\mathscr{S}_X$ of *rays* $ {\ltsbrak x,\infty \rtsbrak} $ and $ {\ltsbrak -\infty,y \rtsbrak} $, where $x,y$ run through the elements of $X$.
:::



:::{prf:proof}

Since $X$ is totally ordered, so is $ {[ -\infty, \infty ]} $. It is immediate that $ {\ltsbrak x,y \rtsbrak}  \, \cap \,  {\ltsbrak x',y' \rtsbrak}  =  {\ltsbrak w,z \rtsbrak} $ if $w$ is the largest of $x$ and $x'$ and $z$ is the smallest of $y$ and $y'$. Hence $\mathscr{I}_X$ is a base of the order topology.

Since $  {\ltsbrak x,\infty \rtsbrak}  \cap  {\ltsbrak -\infty,y \rtsbrak}  =  {\ltsbrak x,y \rtsbrak} $ for $x \leq y$, the set $\mathscr{S}_X$ is a subbase of the order topology.
:::



:::{prf:example} 
The standard topology on $\mathbb{R}$ from Example {prf:ref}`ex:examples-topological-spaces_1`
{ref}`ex:standard-topology-reals_1` is the order topology. Likewise, the standard topology on $\mathbb{Q}$ coincides with the order topology.
:::



:::{prf:remark} 
If $X$ neither has a minimum nor a maximum, one usually denotes the space $ {[ -\infty, \infty ]} $ by $\overline{X}$. This notation fits with the understanding that $\widebar{\phantom{X}}$ denotes the closure operation, because the closure of $X$ in $ {[ -\infty, \infty ]} $ with respect to the order topology coincides with the full space $ {[ -\infty, \infty ]} $ under the assumptions made.

Extending the ordered set of real numbers $(\mathbb{R},\leq )$ in that way gives the so-called *extended real number system* $\widebar{\mathbb{R}}$.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*The order topology -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXThe subspace topologyXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*The subspace topology -->
## The subspace topology
:::{prf:theorem} 
Let $(X,\mathscr{T})$ be a topological space. Let $S\subset X$ and $\iota : S \hookrightarrow X$ the canonical embedding. Then initial topology $\iota^*\mathscr{T}$ coincides with

:::{math}
\mathscr{T}^X_S := \{ U\cap S \in \mathscr{P}(S) \mid U \in \mathscr{T} \} \ .
:::

One calls $\mathscr{T}^X_Y$ the *subspace* or *trace topology* on $S$. Sometimes one says that $\mathscr{T}^X_Y$ is the *topology induced by* $(X,\mathscr{T})$.
:::



:::{prf:proof}

The claim follows immediately from the definition of the initial topology $\iota^*\mathscr{T}$.
:::


Just as easy is the following observation:


:::{prf:proposition} 
Let $(X,\mathscr{T})$ be a topological space, and $S \subset X$ a subset. Let $\mathscr{B}$ be a basis for $\mathscr{T}$. Then the set

:::{math}
\mathscr{B}^X_S:= \{ B\cap S \in \mathscr{P}(S) \mid B \in \mathscr{B} \}
:::

is a basis for the subspace topology on $S$ induced by $(X,\mathscr{T})$.
:::



:::{prf:proof}

Trivial exercise.
:::



:::{prf:example} 
The default topologies on $\mathbb{N}$ and $Z$ are the subspace topologies induced by the standard topology on $\mathbb{R}$. Since $\{ n \} =  {\ltsbrak n-\frac{1}{2},n+\frac{1}{2} \rtsbrak}  \cap \mathbb{Z}$ for all $n \in \mathbb{Z}$, we see that the natural topologies on $\mathbb{N}$ and $\mathbb{Z}$ are in fact the discrete topologies. The topology on $\mathbb{Q}$ induced by the standard topology on $\mathbb{R}$ coincides with the default topology on $\mathbb{Q}$ (which is, as pointed out above, the same as the order topology).
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*The subspace topology -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXThe quotient topologyXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*The quotient topology -->
## The quotient topology

<!-- XXSEC_PREFIX_ENDXX\subsection*The quotient topology -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXThe product topologyXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*The product topology -->
## The product topology
:::{prf:definition} 
Let $I$ be some nonempty set. Let us assume given a family $(X_i,\mathscr{T}_i)_{i \in I}$ of topological spaces. Consider the cartesian product $X := \prod_{i\in I}X_i$ and denote for each $j\in I$ by $\pi_j : X \to X_j$, $(x_i)_{i\in I} \mapsto x_j$ the projection on the $i$-th coordinate. The initial topology on $X$ with respect to the

basic open set of the cartesian product $\prod_{i \in I} E_i$ is a set of the form $\prod_{i \in I} U_i$ where $\{i \in I : U_i \not= E_i\}$ is finite and for all $i \in I$, we have $U_i \in \mathscr{T}_i$.
:::



:::{prf:definition} 
Let $I$ be some nonempty set. Let us assume given a family $(E_i,\mathscr{T}_i)_{i \in I}$ of topological spaces. The product topology on $\prod_{i \in I} E_i$ is the smallest topology containing all the basic open sets.
:::



:::{prf:proposition} 
Let $I$ be some nonempty set. Let us assume given a family $(E_i,\mathscr{T}_i)_{i \in I}$ of topological spaces. The collection of all basic open sets is a basis on the set $\prod_{i\in I} E_i$.
:::



:::{prf:proof}

Trivial exercise.
:::



:::{prf:remark} 
The product topology is not just the basic open sets on the cartesian products: there are many more open sets!
:::



:::{prf:proposition} 
Let $I$ be some nonempty set. Let us assume given a family $(E_i,\mathscr{T}_i)_{i \in I}$ of topological spaces. The product topology on $\prod_{i\in I} E_i$ is the initial topology for the the set $\{p_i : i \in I\}$ where $p_i : \prod_{j\in I} E_j \rightarrow E_i$ is the canonical surjection for all $i\in I$.
:::



:::{prf:proof}

Fix $i\in I$. Let $V\in \mathscr{T}_{E_i}$. By definition, $p_i^{-1}(V)=\prod_{j\in I} U_j$ where $U_j=E_j$ for $j\in I\setminus \{i\}$, and $U_i=V$. Hence $p_i^{-1}(V)$ is open in the product topology. As $V$ was an arbitrary open subset of $E_i$, the map $p_i$ is continuous by definition. Hence, as $i$ was arbitrary in $I$, the initial topology for $\{p_i : i \in I\}$ is coarser than the product topology.

Conversely, note that the product topology is generated by $\{p_i^{-1}(V):i \in I, V\in \mathscr{T}_{E_i}\}$, so it is coarser than the initial topology for $\{p_i : i \in I\}$. This concludes this proof.
:::



:::{prf:corollary} 
Let $I$ be some nonempty set. Let us assume given a family $(E_i,\mathscr{T}_i)_{i \in I}$ of topological spaces. Let $\mathscr{T}$ be the product topology on $F = \prod_{i\in I} E_i$. Let $(D,\mathscr{T}_D)$ be a topological space. Then $f:D\rightarrow F$ is continuous if and only if $p_i\circ f$ is continuous from $(D,\mathscr{T}_D)$ to $(E_i,\mathscr{T}_{E_i})$ for all $i \in I$, where $p_i$ is the canonical surjection on $E_i$ for all $i \in I$.
:::



:::{prf:proof}

We simply applied the fundamental property of initial topologies.
:::



:::{prf:remark} 


\itemindent
: The *box topology* on the cartesian product $\prod_{i\in I}X_i$ is the smallest topology containing all possible cartesian products of open sets $U_i \subset X_i$, $i\in I$. The box topology is strictly finer than the product topology when the index set is infinite and infintely many of the $X_i$ carry a topology strictly finer than the indiscrete topology. Of course, the box and product topologies coincide otherwise, in particular when the product is finite.

\itemindent
: Since the product topology is the coarsest topology which makes the canonical projections continuous, it is the preferred and default one on cartesian products.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*The product topology -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXThe metric topologyXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*The metric topology -->
## The metric topology
:::{prf:definition} 
Let $X$ be a set. A function $d: X \times X \rightarrow \mathbb{R}_{\geq 0}$ is a
*distance* or *metric* on $X$ when:


(ite:metric-positive-definiteness_1)=
(M1)
: For all $x,y \in X$ the relation $d(x,y)=0$ holds true if and only if $x=y$.

(ite:metric-symmetry_1)=
(M2)
: The map $d$ is *symmetric* that is one has $d(x,y)=d(y,x)$ for all $x,y\in X$.

(ite:metric-triangle-inequality_1)=
(M3)
: For all $x,y,z \in X$ the *triangle inequality*
   $d(x,y)\leq d(x,z)+d(z,y)$ is satisfied.

If instead of {ref}`ite:metric-positive-definiteness_1` the axiom \hyperref[ite:metric-distance-self-zero] (M1)'
below is fulfilled while {ref}`ite:metric-symmetry_1` and {ref}`ite:metric-triangle-inequality_1` are still valid, then $d$ is called a *pseudometric* on $X$.


(ite:metric-distance-self-zero_1)=
(M1)'
: For all $x\in X$ the equality $d(x,x)=0$ holds true.


A pair $(X,d)$ is a *metric space* when $X$ is a set and $d$ a distance on $X$. If $d$ is only a pseudometric on $X$, one calls the pair $(X,d)$ a *pseudometric space*.
:::


The following is often useful.


:::{prf:lemma} 
Let $(X,d)$ be a pseudometric space. Let $x,y,z \in X$. Then

:::{math}
|d(x,y)-d(x,z)|\leq d(y,z) \ .
:::
:::



:::{prf:proof}

Since $d(x,y)\leq d(x,z)+d(z,y)$ we have $d(x,y)-d(x,z)\leq d(z,y)=d(y,z)$. Since $d(x,z)\leq d(x,y)+d(y,z)$ we have $d(x,z)-d(x,y) \leq d(y,z)$. Hence the claim holds.
:::



:::{prf:definition} 
Let $(X,d)$ be a pseudometric space. Let $x\in E$ and $r\in \mathbb{R}_{ > 0}$. The *open ball* with *center* $x$ and *radius* $r$ in $(X,d)$ is the set

:::{math}
\mathbb{B} (x,r) = \mathbb{B}_r (x) = \{ y \in X \mid d(x,y) < r \} \ .
:::

The *closed ball* with *center* $x$ and *radius* $r$ is defined by

:::{math}
\overline{\mathbb{B}} (x,r) = \overline{\mathbb{B}}_r (x) = \{ y \in X \mid d(x,y) \leq r \} \ .
:::
:::



:::{prf:definition} 
Let $(X,d)$ be a pseudometric space. The *metric topology* on $X$ induced by $d$ is the smallest topology containing all the open balls of $X$.
:::



:::{prf:theorem} 
Let $(X,d)$ be a pseudometric space. The set of all open balls on $X$ is a basis for the metric topology on $X$ induced by $d$.
:::



:::{prf:proof}

It is enough to show that the set of all open balls is a topological basis. By definition, $X = \bigcup_{x\in X} \mathbb{B} (x,1)$. Now, let us be given $\mathbb{B} (x,r_x)$ and $\mathbb{B} (y,r_y)$ for some $x,y\in X$ and $r_x, r_y > 0$. If the intersection of these two balls is empty, we are done; let us assume that there exists $z\in \mathbb{B} (x,r_x)\cap \mathbb{B} (y,r_y)$. Let $r$ be the smallest of $r_x-d(x,z)$ and $r_y-d(y,z)$. Let $w \in \mathbb{B} (z,r)$. Then

:::{math}
d(x,w)\leq d(x,z)+d(z,w) < d(x,z)+r_x - d(x,z) = r_x \ ,
:::

so $w \in \mathbb{B} (x,r_x)$. Similarly, $w \in \mathbb{B} (y,r_y)$. Hence, $\mathbb{B} (z,r)\subset \mathbb{B} (x,r_x)\cap \mathbb{B} (y,r_y)$ as desired.
:::


The following result shows that metric topologies are minimal in the sense of making the distance functions continuous.


:::{prf:proposition} 
Let $(X,d)$ be a pseudometric space. For all $x \in X$, the function

:::{math}
d_x : X \to \mathbb{R}_{\geq 0}, \quad y \mapsto d(x,y)
:::

is continuous on $X$ for the metric topology. Moreover, the metric topology is the smallest topology such that all the functions $d_x$, $x \in X$ are continuous.
:::



:::{prf:proof}

Fix $x \in X$. To verify continuity of the maps $d_x$ it is sufficient to show that the preimages of $ {[ 0,r \rtsbrak} $ and $ {\ltsbrak r,\infty \rtsbrak} $ by $d_x$ are open in the metric topology of $X$, where $r > 0$ is arbitrary. Indeed, these intervals form a subbasis for the topology of $ {[ 0,\infty \rtsbrak} $ which we assume to carry the subspace topology induced by the order topology on $\mathbb{R}$. Let $r > 0$ be given. Then $d_x^{-1}( {[ 0,r \rtsbrak} ) = \mathbb{B} (x,r)$ by definition, so it is open. Now, let $y \in X$ such that $d(x,y) > r$. Let $\varrho_y = d(x,y)-r > 0$. If $d(w,y) < \varrho_y$ for some $w\in X$, then $ d(x,y)-d(w,y)\leq d(x,w)$, so $d(x,w) > r$. Hence

:::{math}
\mathbb{B} (y,\rho_y)\subset d_x^{-1}(  {\ltsbrak r,\infty \rtsbrak}  ) \quad \text{for all } y\in d_x^{-1}( {\ltsbrak r,\infty \rtsbrak} ) \ .
:::

Therefore, $d_x^{-1}( {\ltsbrak r,\infty \rtsbrak} )$ is open.

Finally, since $d_x^{-1}( {[ 0,r \rtsbrak} ) = \mathbb{B} (x,r)$ for all $x\in X$ and $r > 0$ the minimal topology making all the maps $d_x$ continuous must indeed contain the metric topology as desired, and our proposition is proven.
:::



:::{prf:remark} 
The metric topology is the default topology on a pseudometric space.
:::


\para There are more examples of continuous functions between metric spaces. More precisely, a natural category for metric spaces consists of metric spaces and Lipschitz maps as arrows, defined as follows.


:::{prf:definition} 
Let $(X,d_X)$, $(Y,d_Y)$ be pseudometric spaces. A function $f:X\rightarrow Y$ for which there exists an $L > 0$ such that

:::{math}
d_Y (f(x),f(y))\leq L \, d_X (x,y)\quad \text{for all } x,y \in X
:::

is called *Lipschitz*.
:::



:::{prf:definition} 
Let $(X,d_X)$, $(Y,d_Y)$ be pseudometric spaces. Let $f: X\rightarrow Y$ be a Lipschitz function. Then the *Lipschitz constant* of $f$ is defined as

:::{math}
\operatorname{Lip}(f) =
\sup\left\{ \left. \frac{d_Y(f(x),f(y))}{d_X(x,y)} \, \right| \: x,y \in X, d(x,y)\neq 0 \right\} \ .
:::

A Lipschitz function with Lipschitz constant $L\leq 1$ is called a *metric map*. If its Lipschitz constant is $ < 1$, then the Lipschitz function is called a *contraction*.
:::



:::{prf:example} 


\itemindent
: A constant map $f :X\to Y$ between pseudometric spaces is Lipschitz with Lipschitz constant $0$. If both $X$ and $Y$ are metric spaces and $f:X\to Y$ is Lipschitz, then $\operatorname{Lip}(f)=0$ if and only if $f$ is constant.

\itemindent
: The identity map $\mathrm{id}_X : X \to X$ on a pseudometric space $(X,d)$ is Lipschitz. If $d$ is not the zero pseudometric on $X$, then $\operatorname{Lip}(id_X)=0$.
:::



:::{prf:proposition} 
Let $(X,d_X)$, $(Y,d_Y)$ be pseudometric spaces. If $f:X\rightarrow Y$ is a Lipschitz function, then it is continuous.
:::



:::{prf:proof}

Let $L$ be the Lipschitz constant for $f$. Let $y \in Y$ and $\varepsilon > 0$. Let $x\in f^{-1}(\mathbb{B}(y,\varepsilon))$. Put $\delta_x = \frac{\varepsilon-d(f(x),y)}{L+1}$ and observe that $\delta_x > 0$. Then, for $z \in \mathbb{B} (x,\delta_x)$,

:::{math}
\begin{split}
d_Y( f(z),y) &\leq d_Y(f(z),f(x)) + d_Y(f(x),y) \leq L d_X(z,x) + d_Y(f(x),y) < \\ & < \varepsilon - d_Y(f(x),y) + d_Y(f(x),y) = \varepsilon .
\end{split}
:::

Hence $f^{-1}(\mathbb{B}(y,\varepsilon))$ is open and $f$ is continuous.
:::



:::{prf:theorem} 
Pseudometric spaces as objects together with metric maps between them form a category $\mathsf{PMet}$ which is called the *category of pseudometric spaces*. Changing the morphism class to Lipschitz maps between pseudometric spaces gives another category which we denote $\mathsf{PMetLip}$ and call the *category of pseudometric spaces and Lipschitz functions*. Metric spaces together with metric or Lipschitz maps between them form full subcategories $\mathsf{Met}$ and $\mathsf{MetLip}$ of $\mathsf{PMet}$ and $\mathsf{PMetLip}$, respectively. They are called the *category of metric spaces* respectively the
*category of metric spaces and Lipschitz functions*.
:::



:::{prf:proof}

The claim immediately follows from the observation that the identity map on a pseudometric space is metric and that the composition of two metric respectively Lipschitz maps is again metric respectively Lipschitz.
:::



:::{prf:remark} 
Using metric or Lipschitz maps as morphisms for categories of metric or pseudometric spaces is natural. Other, more general type of morphisms, would be uniform continuous maps, which are discussed in later sections.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*The metric topology -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXCo-Finite TopologiesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Co-Finite Topologies -->
## Co-Finite Topologies
A potential source for counter-examples, the family of cofinite topologies is easily defined:


:::{prf:proposition} 
Let $E$ be a set. Let: 
:::{math}
\mathscr{T}_\mathrm{cof} (E) = \{\emptyset \} \cup \{ U \subset E : \complement_E U \textrm{ is finite } \} \textrm{.}
:::
 Then $\mathscr{T}_\mathrm{cof}(E)$ is a topology on $E$.
:::



:::{prf:proof}

By definition, $\emptyset \in \mathscr{T}_\mathrm{cof}(E)$. Moreover, $\complement_E E=\emptyset$ which is finite, so $E\in\mathscr{T}_\mathrm{cof}(E)$. Let $U,V \in \mathscr{T}_\mathrm{cof}(E)$. If $U$ or $V$ is empty then $U\cap V = \emptyset$ so $U \cap V \in \mathscr{T}_\mathrm{cof}(E)$. Otherwise, $\complement_E (U\cap V) = \complement_E U \cup \complement V$ which is finite, since by definition $\complement_E U$ and $\complement_E V$ are finite. Hence $U\cap V \in \mathscr{T}_\mathrm{cof}(E)$. Last, let $\mathcal{U}\subset \mathscr{T}_\mathrm{cof}(E)$. Again, if $\mathcal{U}=\{\emptyset\}$ then $\bigcup \mathcal{U} = \emptyset \in \mathscr{T}_\mathrm{cof}(E)$. Let us now assume that $\mathcal{U}$ contains at least one nonempty set $V$. Then: 
:::{math}
\complement_E \bigcup \mathcal{U} = \bigcap \{ \complement_E U : U \in \mathcal{U} \} \subset \complement_E V\textrm{.}
:::
 Since $\complement_E V$ is finite by definition, so is $\bigcup \mathcal{U}$, which is therefore in $\mathscr{T}_\mathrm{cof}(E)$. This completes our proof.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Co-Finite Topologies -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXThe one-point compactification of $\mathbb{N}$XXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*The one-point compactification of $\mathbb{N}$ -->
## The one-point compactification of $\mathbb{N}$
Limits of sequences is a central tool in topology and this section introduces the natural topology for this concept. The general notion of limit is the subject of the next chapter.


:::{prf:definition} 
Let $\infty$ be some symbol not found in $\mathbb{N}$. We define $\widebar{\mathbb{N}}$ to be $\mathbb{N}\cup \{\infty\}$.
:::



:::{prf:proposition} 
The set: 
:::{math}
\mathscr{T}_{\widebar{\mathbb{N}}} = \{ U \subset \widebar{\mathbb{N}} : ( U\subset \mathbb{N})\vee (\infty \in U \wedge \complement_{\mathbb{N}} U \textrm{ is finite} ) \}
:::
 is a topology on $\widebar{\mathbb{N}}$.
:::



:::{prf:proof}

By definition, $\emptyset \subset \mathbb{N}$ so $\emptyset\in\mathscr{T}_{\widebar{\mathbb{N}}}$. Moreover $\complement_{\widebar{\mathbb{N}}} \widebar{\mathbb{N}} = \emptyset$ which has cardinal $0$ so $\widebar{\mathbb{N}} \in \mathscr{T}_{\widebar{\mathbb{N}}}$. Let $U,V \in \mathscr{T}_{\widebar{\mathbb{N}}}$. If either $U$ or $V$ is a subset of $\mathbb{N}$ then $U\cap V$ is a subset of $\mathbb{N}$ so $U\cap V \in \mathscr{T}_{\widebar{\mathbb{N}}}$. Othwiwse, $\infty \in U \cap V$. Yet $\complement_{\widebar{\mathbb{N}}} (U\cap V) = \complement_{\widebar{\mathbb{N}}} U \cup \complement_{\widebar{\mathbb{N}}}V$ which is finite as a finite union of finite sets. Hence $U\cap V \in\mathscr{T}_{\widebar{\mathbb{N}}}$ again.

Last, assume that $\mathcal{U}\subset \mathscr{T}_{\widebar{\mathbb{N}}}$. Of course, $\infty \in \bigcup \mathcal{U}$ if and only if $\infty \in U$ for some $U \in \mathcal{U}$. So, if $\infty \not \in \bigcup \mathcal{U}$ then $\bigcup \mathcal{U} \in \mathscr{T}_{\widebar{\mathbb{N}}}$ by definition. If, on the other hand, $\infty \in \bigcup \mathcal{U}$, then there exists $U\in\mathcal{U}$ with $\complement_{\widebar{\mathbb{N}}} U$ finite. Now, $\complement_{\widebar{\mathbb{N}}} \bigcup \mathcal{U} = \bigcap \{ \complement_{\widebar{\mathbb{N}}} V : V \in \mathcal{U} \} \subset \complement_{\widebar{\mathbb{N}}} U$ so it is finite, and thus again $\bigcup\mathcal{U} \in \mathscr{T}_{\widebar{\mathbb{N}}}$.
:::



<!-- XXSEC_PREFIX_ENDXX\subsection*The one-point compactification of $\mathbb{N}$ -->


\IfFileExists../CRingProject/sections/separation-properties 
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXSeparation propertiesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionSeparation properties -->
# Separation properties
\para The general definition of a topology allows for examples where elements of a topological space, seen as a set, can not be distinguished from each other by open sets (for instance if the topology is indiscrete). When points can be topologically differentiated, a topology is in some sense separated. The standard separation axioms allow to subsume topological spaces with certain separability properties in particular classes. One then studies the properties of these clases, often with a view to particular applications, and attempts to create counter examples, meaning examples not satsifying the corresponding separation axioms. The most important separability property goes back to the founder of set-theoretic topology, Felix Hausdorff, who introduced it in 1914. The first full presentation of the separation axioms as we know them today appeared in the classic book *Topologie* by [@AleHopT]
under their German name *Trennungsaxiome*.

Let us note that the literature on separation axioms is not uniform when it comes to the axioms {ref}`axiom:t3_1` to {ref}`axiom:t6_1` below, so one needs to always check which convention an author follows. Here, we follow the convention by [@SteSeeCT, Part I, Chap.~2] which coincides with the one of
:::{prf:definition} The Separation Axioms
Recall that two subsets $A,B$ of a topological space $(X,\mathscr{T})$ are called *disjoint* if $A\cap B = \emptyset$. The two sets are called
*separated* if $ \widebar{A} \cap B = A \cap \widebar{B} = \emptyset$. The topological space $(X,\mathscr{T})$ now is said to be

\setcounterenumi-1
(axiom:t0_1)=
( T1)\hspace2.3mm
: or *Kolmogorov*
   if for each pair of distinct points $x,y \in X$ there is an open $U\subset X$ such that $x\in U$ and $y \notin U$ holds true, or $y\in U$ and $x \notin U$,

(axiom:t1_1)=
( T2)\hspace2.3mm
: or *Fr\'echet*
   if for each pair of distinct points $x,y \in X$ there is an open $U\subset X$ such that $x\in U$ and $y \notin U$,

(axiom:t2_1)=
( T3)\hspace2.3mm
: or *Hausdorff*
   if for each pair of distinct points $x,y \in X$ there exist disjoint open sets $U,V \subset X$ such that $x\in U$ and $y \in V$,

\rmfamily ( T2$_{\mathsf{\frac 12}}$\rmfamily )
: or *Uryson* or *completely Hausdorff*
   if for each pair of distinct points $x,y \in X$ there exist distinct closed neigborhoods $U$ of $x$ and $V$ of $y$,

(axiom:t3_1)=
( T4)\hspace2.3mm
: if for each point $x \in X$ and closed subset $A \subset X$ with $x \notin A$ there exist disjoint open sets $U,V \subset X$ such that $x\in U$ and $A \subset V$,

(axiom:t3a_1)=
\rmfamily ( T3$_{\mathsf{\frac 12}}$\rmfamily )
: if for each point $x \in X$ and closed subset $A \subset X$ with $x \notin A$ there exists a continuous function $f: X \to \mathbb{R}$ such that $f(x)=0$ and $f (A) = \{ 1 \}$,

(axiom:t4_1)=
( T5)\hspace2.3mm
: if for each pair of closed disjoint subsets $A,B \subset X$ there exist disjoint open sets $U,V \subset X$ such that $A \subset U$ and $B \subset V$,

(axiom:t5_1)=
( T6)\hspace2.3mm
: if for each pair of separated subsets $A,B \subset X$ there exist disjoint open sets $U,V \subset X$ such that $A \subset U$ and $B \subset V$,

(axiom:t6_1)=
( T7)\hspace2.3mm
: if for each pair of disjoint closed subsets $A,B \subset X$ there exists a continuous function $f: X \to \mathbb{R}$ such that $A = f^{-1} (0)$ and $B = f^{-1}(0)$.

A Hausdorff space will be called *regular*
if it fulfills {ref}`axiom:t3_1`, *completely regular*, if it satisfies \hyperref[axiom:t3a]\rmfamily ( T3$_{\mathsf{\frac 12}}$\rmfamily ), and *normal* if {ref}`axiom:t4_1` holds true. Finally we call a Hausdorff space *completely normal* if it is {ref}`axiom:t5_1`
and *perfectly normal* if it is {ref}`axiom:t6_1`.
:::


<!-- XXSEC_PREFIX_ENDXX\sectionSeparation properties -->


\IfFileExists../CRingProject/sections/filters-convergence 
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXFilters and convergenceXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionFilters and convergence -->
(sec:filters-convergence_1)=
# Filters and convergence
<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXFilters and ultrafiltersXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Filters and ultrafilters -->
## Filters and ultrafilters
:::{prf:definition} 
Let $X$ be a set. A subset $\mathscr{F}$ of the powerset $\mathscr{P}(X)$ is called a *filter* on $X$ if it satisfies the following axioms:


(Fil1)
: The empty set $\emptyset$ is not an element of $\mathscr{F}$.

(Fil2)
: The set $X$ is an element of $\mathscr{F}$.

(Fil3)
: If $A\in \mathscr{F}$ and if $B \in \mathscr{P}(X)$ satisfies $A \subset B$, then $B \in \mathscr{F}$.

(Fil4)
: If $A \in \mathscr{F}$ and $B \in \mathscr{F}$, then the intersection $A \cap B$ is an element of $\mathscr{F}$ as well.

If $\mathscr{F}_1$ and $\mathscr{F}_2$ are two filters on $X$ such that $\mathscr{F}_1 \subset \mathscr{F}_2$, then one calls $\mathscr{F}_1$ a *subfilter* of $\mathscr{F}_2$ or says that $\mathscr{F}_2$ is *finer* than $\mathscr{F}_1$. Sometimes one expresses this by saying that $\mathscr{F}_2$ *refines* $\mathscr{F}_1$. Filters maximal with respect to set inclusion are called *ultrafilters*. A filter $\mathscr{F}$ is called *free* if $\bigcap_{A\in \mathscr{F}} A = \emptyset$ otherwise it is called *fixed*.
:::



:::{prf:example} 


\itemindent
: For every set $X$, the set $\{ X\}$ is a filter. It is the smallest of all filters on $X$.

\itemindent
: Given an element $x \in X$ the set $\mathscr{F}_x := \{ A \in \mathscr{P}(X) \mid x \in A \}$ is an ultrafilter on $X$. More generally, if $Y\subset X$ is a non-empty subset, then $\mathscr{F}_Y := \{ A \in \mathscr{P}(X) \mid Y \subset A \}$ is a filter on $X$. It is an ultrafilter if and only if $Y$ has exactly one element.

\itemindent
: If $(X,\mathscr{T})$ is a topological space and $x\in X$ an element, then the *neigborhood filter*
   $\mathscr{U}_x := \{ V \in \mathscr{P}(X)\mid \exists U \in \mathscr{T} : \; x\in U \subset V \}$ is a filter contained in $\mathscr{F}_x$. The filters $\mathscr{U}_x$ and $\mathscr{F}_x$ coincide if and only if $x$ is an isolated point.

\itemindent
: Now consider the reals and let $\mathscr{F} = \{ A \in \mathscr{P}(\mathbb{R})\mid \exists \, \varepsilon > 0 : \:  {[ 0,\varepsilon \rtsbrak}  \subset A \}$. Then $\mathscr{F}$ is a filter on $\mathbb{R}$ which is properly contained in the ultrafilter $\mathscr{F}_0$ and which properly contains the neighborhood filter $\mathscr{U}_0$ (where $\mathbb{R}$ carries the standard topology).
:::



:::{prf:proposition} 
Let $\mathscr{A}\subset \mathscr{P}(X)$ be a non-empty set of subset of $X$ which has the
*finite intersection property*
that is that $A_1 \cap \ldots \cap A_n $ is non-empty for all $n\in \mathbb{N}^*$ and all $A_1 , \ldots , A_n\in \mathscr{A}$. Then there is an ultrafilter $\mathscr{F}$ containing $\mathscr{A}$.
:::


:::{prf:proof}

Let $P$ be the set of all $\mathscr{J}\subset \mathscr{P}(X)$ having the finite intersection property and containing $\mathscr{A}$. Then $P$ is non-empty, as it contains at least $\mathscr{A}$, and is ordered by set inclusion. If $C\subset P$ is a chain, then $\mathscr{M} := \bigcup_{\mathscr{J} \in C} \mathscr{J}$ contains $\mathscr{A}$ and fulfills the finite intersection property. To verify the latter let $Y_1,\ldots , Y_n \in \mathscr{M}$. Then there exist $\mathscr{J}_1,\ldots , \mathscr{J}_n \in C$ such that $Y_i \in \mathscr{J}_i$ for $i=1,\ldots ,n$. Hence all $Y_i$ lie in the maximum $\mathscr{J}_{m}$ of the sets $\mathscr{J}_1,\ldots , \mathscr{J}_n$. But $\mathscr{J}_{m}$ has the finite intersection property, hence $Y_1 \cap \ldots \cap Y_n \neq \emptyset$. So $\mathscr{M}$ is an upper bound of the chain $C$. By Zorn's Lemma, $P$ has a maximal element $\mathscr{F}$. It contains $\mathscr{A}$ and has the finite intersection property. Moreover, if $A\in \mathscr{F}$ and $B\in \mathscr{P}(X)$ contains $A$ as a subset, then $\mathscr{F} \cup \{ B \}$ also satisfies the finite intersection property, hence by maximality of $\mathscr{F}$ one concludes $B \in \mathscr{F}$. Again by maximality $\mathscr{F}$ has to be an ultrafilter.
:::



:::{prf:corollary} 
Every filter on $X$ is contained in an ultrafilter.
:::


:::{prf:proof}

This follows from the preceding proposition since a filter has the finite intersection property.
:::



:::{prf:theorem} 
Let $\mathscr{F}$ be a filter on a set $X$. Then the following are equivalent:



(i)
: $\mathscr{F}$ is an ultrafilter.

(ii)
: If $A$ is a subset of $X$ and $A$ has non-empty intersection with every element of $\mathscr{F}$, then $A \in \mathscr{F}$.

(iii)
: For all $A \subset X$ either $A \in \mathscr{F}$ or $X\setminus A \in \mathscr{F}$.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Filters and ultrafilters -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXConvergence of filtersXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Convergence of filters -->
## Convergence of filters

<!-- XXSEC_PREFIX_ENDXX\subsection*Convergence of filters -->

<!-- XXSEC_PREFIX_ENDXX\sectionFilters and convergence -->


\IfFileExists../CRingProject/sections/nets 
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXNetsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionNets -->
(sec:nets_1)=
# Nets
<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXDirected setsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Directed sets -->
## Directed sets
Let us first recall that by a *preordered set* one understands a set $P$ together with a binary relation $\leq$ which is reflexive and transitive, see \Crefdef:ordered-set.


:::{prf:definition} Directed sets
By a directed set one understands a preordered set $(P,\leq)$ such that the binary relation $\leq$ is *directed* which means that


(\textsfDir)
: for all $x,y\in D$ there exists an element $z\in D$ with $x \leq z$ and $y\leq z$.
:::



:::{prf:remark} 
The property that $(P,\leq)$ is directed is the same as saying that any two elements of the preordered set $P$ have an upper bound.
:::


<!-- XXSEC_PREFIX_ENDXX\subsection*Directed sets -->

<!-- XXSEC_PREFIX_ENDXX\sectionNets -->


\IfFileExists../CRingProject/sections/compactness 
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXCompactnessXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionCompactness -->
(sec:compactness_1)=
# Compactness
<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXQuasi-compact topological spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Quasi-compact topological spaces -->
## Quasi-compact topological spaces
\para Before we come to defining quasi-compactness let us recall some relevant notation. By a *cover* (or *covering*) of a set $X$ one understands a family $\mathcal{U} = ( U_i )_{i\in I}$ of subsets $U_i \subset X$ such that $ X \subset \bigcup_{i\in I} U_i$. This terminology also holds for a subset $Y \subset X$. That is a family $\mathcal{U} = ( U_i )_{i\in I}$ of subsets $U_i \subset X$ is called a *cover* of $Y$ if $ Y \subset \bigcup_{i\in I} U_i$. A *subcover* of a cover $\mathcal{U} = ( U_i )_{i\in I}$ of $Y$ or shortly a subcover of $\mathcal{U}$ then is a subfamily $( U_i )_{i\in J}$ which also covers $Y$ which means that $J\subset I$ and $Y \subset \bigcup_{i\in J} U_i$. If $J$ is finite, one calls the subcover $( U_i )_{i\in J}$ a *finite subcover*. If $(X,\mathscr{T})$ is a topological space and all elements $U_i$ of a cover $\mathcal{U} = ( U_i )_{i\in I}$ of some $Y \subset X$ are open sets, the cover is called an
*open cover* of $Y$.


:::{prf:proposition} 
Let be a topological spaces $(X,\mathscr{T})$. Then the following are equivalent:



(ite:subcover_1)=
(i)
: Every open cover of $X$ has a finite subcover.

(ite:empty-intersection-property_1)=
(ii)
: For every family $(A_i)_{i\in I}$ of closed subset $A_i\subset X$ such that $\bigcap_{i\in I} A_i = \emptyset$ there exist finitely many elements $A_{i_1}, \ldots , A_{i_n}$ such that $A_{i_1} \cap \ldots \cap A_{i_n} =\emptyset $.

(ite:filter-accummulation-point_1)=
(iii)
: Every filter on $X$ has an accummulation point.

(ite:ultrafilter-convergence_1)=
(iv)
: Every ultrafilter on $X$ converges.
:::



:::{prf:proof}

Assume that {ref}`ite:subcover_1` holds true and let $(A_i)_{i\in I}$ be a family of closed subset $A_i\subset X$ such that $\bigcap_{i\in I} A_i = \emptyset$. Put $U_i := X \setminus A_i$ for all $i\in I$. Then $(U_i)_{i\in I}$ is an open covering of $X$, hence by assumption there exist $i_1, \ldots , i_n \in I$ such that $X = U_{i_1} \cup \ldots \cup U_{i_n}$. By de Morgan's laws the relation $A_{i_1} \cap \ldots \cap A_{i_n} =\emptyset $ the follows, hence
{ref}`ite:empty-intersection-property_1` follows.

Next assume {ref}`ite:empty-intersection-property_1`, and let $\mathscr{F}$ be a filter on $X$. Then $\widebar{A_1} \cap \ldots \cap \widebar{A_n} \neq \emptyset $ for all $n\in \mathbb{N}^*$ and $A_1, \ldots , A_n\in \mathscr{F}$, since $\mathscr{F}$ is a filter. Hence $\bigcap_{A \in \mathscr{F}} \widebar{A} \neq \emptyset$ by {ref}`ite:empty-intersection-property_1`. Every element of $\bigcap_{A \in \mathscr{F}} \widebar{A}$ now is an accummulation point of $\mathscr{F}$, so {ref}`ite:filter-accummulation-point_1` follows.

By \Crefthm: , {ref}`ite:filter-accummulation-point_1` implies {ref}`ite:ultrafilter-convergence_1`.

Finally assume that every ultrafilter on $X$ converges, and let $\mathcal{U} = ( U_i )_{i\in I}$ be an open cover of $X$. Assume that $\mathcal{U}$ has no finite subcover. For each finite subset $J\subset I$ the set $B_J := X \setminus \bigcup_{i\in J} U_i$ then is non-empty, hence $\mathscr{B} := \{ B_J \in \mathscr{P}(X) \mid J \subset I \: \& \: \# J < \infty \}$ is a filter base. Let $\mathscr{F}$ be an ultrafilter containing $\mathscr{B}$. By assumption $\mathscr{F}$ converges to some $x\in X$. Since $\mathcal{U}$ is an open covering of $X$ there is some $U_i$ with $x \in U_i$, hence $U_i$ since $\mathscr{F}$ converges to $x$. On the other hand $X \setminus U_i \in \mathscr{B} \subset \mathscr{F}$ by construction. This is a contradiction, so $\mathcal{U}$ must have a finite subcover.
:::



:::{prf:definition} [@BouGTC1-4][I.\S9.1.]
A topological space $(X,\mathscr{T})$ is called *quasi-compact*, if every filter on $X$ has an accummulation point.
:::



:::{prf:theorem} Alexander Subbase Theorem
Let $(X,\mathscr{T})$ be a topological space, and $\mathscr{S}$ an *adequate* subbase of the topology that is a subbase of $\mathscr{T}$ such that $X = \bigcup_{S\in \mathscr{S}} S$. If every cover of $X$ by elements of $\mathscr{S}$ has a finite subcover, the topological space $(X,\mathscr{T})$ is quasi-compact.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Quasi-compact topological spaces -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXCompact topological spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Compact topological spaces -->
## Compact topological spaces

<!-- XXSEC_PREFIX_ENDXX\subsection*Compact topological spaces -->

<!-- XXSEC_PREFIX_ENDXX\sectionCompactness -->


\IfFileExists../CRingProject/sections/compact-open-topology-function-spaces 
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe compact-open topology on function spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe compact-open topology on function spaces -->
(sec:compact-open-topology-function-spaces_1)=
# The compact-open topology on function spaces
Let $X$ and $Y$ be topological spaces. We denote the set of all functions from $Y$ to $X$ by $X^Y$. This is the same thing as the direct product $\prod_Y X$ of $X$ over $Y$. The space of continuous functions $\mathscr{C}(Y,X)$ sits in $X^Y$ so we can give $\mathscr{C}(Y,X)$ the product topology induced by $X^Y$. This is the topology of
*pointwise convergence* and will not be useful for studying most function spaces. We will instead be interested in the *compact open topology* which is the topology of
*uniform convergence on compact sets*.


:::{prf:definition} 
Let $X$ and $Y$ be topological spaces. The *compact open topology* on $\mathscr{C}(Y,X)$ is the topology with subbasis given by the sets $\mathscr{V}(K,U)=\{f \in \mathscr{C} (Y,X)|f(K) \subset U\}$ for $K \subset Y$ compact and $U \subset X$ open.
:::



:::{prf:definition} 
A topology $\mathscr{T}$ on $\mathscr{C}(Y,X)$ is called *admissable* if the evaluation map $e:\mathscr{C}(Y,X) \times Y \rightarrow X$, $(f,y) \mapsto f(y)$ is continuous.
:::



:::{prf:proposition} 
The compact open topology is coarser than any admissable topology on $\mathscr{C}(Y,X)$.
:::


:::{prf:proof}

Let $\mathscr{T}$ be an admissable topology on $\mathscr{C}(Y,X)$ so that the evaluation map $e:\mathscr{C}(Y,X) \times Y \rightarrow X$ is continuous. Let $K\subset Y$ be compact, $U\subset X$ be open and $f\in T(K,U)$. We have to find $V\in O$ such that $f \in V \subset T(K,U)$. Let $k \in K$. Since $e$ is continuous and $U$ is an open neighborhood of $f(x)$, then there are open sets $W_k \subset Y$ and $V_k \subset C_O(Y,X)$ such that $k\in W_k$, $f(k)\in V_k$ amd $e(V_k \times W_k)\subset U$. Since $K$ is compact, there are $k_1,k_2,...,k_l \in K$ such that $K\subset \bigcup_{i=1}^l W_{k_i}$. Put $V:=\bigcap_{i=1}^l V_{k_i}$ so that $f \in V$ and $V$ is open in $O$. Now take $g \in V$ and let $k \in K$. Choose $i$ such that $k\in W_{k_i}$ and observe that $g\in W_{k_i}$ so that 
:::{math}
g(k)=e(g,k) \in e(V_{k_i} \times W_{k_i} \subset U
:::
 Hense $g \in T(K,U)$
:::



:::{prf:theorem} 
If $Y$ is locally compact, then the compact open topology on $\mathscr{C}(Y,X)$ is admissable, and it is the coarsets topology on $\mathscr{C}(Y,X)$ with that property.

:::{prf:proof}

We have to show that 
:::{math}
e:\mathscr{C}(Y,X) \times Y \rightarrow X \\ (f,y)\mapsto f(y)
:::
 is continuous. Since sets of the form $T(K,U)$ form a subbasis for the compact open topology, it suffices to show that for an open neighborhood $W \subset X$ of some $e(f,y)$, there is compact $K\subset Y$, open $U \subset X$ and open $V \subset Y$ such that $e(T(K,U) \times V) \subset W$ with $f \in T(K,U)$ and $y\in V$. By assumption, and since $f$ is continuous, there is an open neighborhood $\tilde{W}$ of $y$ such that $f(\tilde{W}) \subset W$. By local compactness, there is an open neighborhood $V\subset Y$ of $Y$ such that $y \in V \subset \bar{V} \subset \tilde{W}$ and $\bar{V}$ is compact. If we put $K:=\bar{V}$ and $U=W$, then $e(T(K,U) \times V) \subset W$ since for $f'\in T(K,U)$ and $y'\in V$, we have $e(f',y')=f'(y')\subset W$.
:::
:::


Let $X,Y,Z$ be topological spaces. As sets, it is always true that $Z^{X \times Y} \cong Z^{Y^X}$ via the maps 
:::{math}
\Phi:Z^{X \times Y} \rightarrow Z^{Y^X} \\ f \mapsto (x \mapsto (y \mapsto f(x,y)))
:::
 and 
:::{math}
\Psi:Z^{Y^X} \rightarrow Z^{X \times Y} \\ g \mapsto ((x,y) \mapsto g(x)(y))
:::



:::{prf:theorem} The exponential law
If $Y$ is locally compact, then 
:::{math}
\Phi(\mathscr{C}(X \times Y),Z) \subset \mathscr{C}(X,\mathscr{C}(Y,Z))
:::
 and 
:::{math}
\Psi(\mathscr{C}(X,\mathscr{C}(Y,Z))) \subset (\mathscr{C}(X \times Y),Z)
:::


:::{prf:proof}

For $f\in\mathscr{C}(X \times Y, Z)$ and $x\in X$, we have to show that $\Phi(f)(x)\in\mathscr{C}(Y,Z)$ and $\Phi(f)\in \mathscr{C}(X,\mathscr{C}(Y,Z))$. $\Phi(f)(x)(y)=f \circ i_x(y)=f(x,y)$. Consider $T(K,U)$ for $K\subset Y$ compact and $U \subset X$ open. We need ot prove that the preimage $\Phi(f)^{-1}(T(K,U))$ is open in X. Let $x \in \Phi(f)^{-1}(T(K,U))$ so that $f(x,_) \in T(K,U)$. Hence for all $y \in K$, we have $f(x,y)\in U$. By the continuity of $f$, there are open neighborhoods $W_y$ of $x$ and $V_y$ of $y$ such that $f(W_y \times V_y)\subset U$. Since $K$ us compact, there are open sets $y_1,y_2, \ldots y_k \subset Y$ such that $K\subset V_{y_1} \cup V_{y_2} \cup \ldots \cup V_{y_k}$. Put $W=W_{y_1} \cap W_{y_2} \cap \ldots \cap W_{y_k}$ so that $W$ is a neighborhood of $x$ and $\Phi(f)(W)\subset T(K,U)$.

Now we need to show for $g \in \mathscr{C}(X,\mathscr{C}(Y,Z))$ that $\Psi(g)\in \mathscr{C}(X \times Y,Z)$. Let $g:X \times \mathscr{C}(Y,Z)$ be continuous and assume that $U \subset Z$ be open. We have to show that $\Psi(g)^{-1}(U)$ is open. Take $(x,y)\in \Psi(g)^{-1}(U)$. Since $g$ is continuous, there is an open neighborhood $W$ of $y$ such that $g(x)(W) \subset U$. Since $Y$ is locally compact, there is an open $V \subset Y$ such that $y\in V \subset \bar{V} \subset W$ with $\bar{V}$ compact. Hence $g(x)(V)\subset g(x)(\bar{V})\subset U$. Thus $g(x)\in T(K,U)$ so there is an open neighborhood $O \subset X$ of $x$ such that $g(O) \subset T(\bar{V},U)$. Therefore 
:::{math}
\Psi(g)(O \times V) \subset g(O)(V) \subset g(O)(\bar{V}) \subset U
:::
:::
:::



:::{prf:lemma} 
:label: cosubbasis_1
The sets $(U^L)^K = T(K,T(L,U))$ with $K \subset X$ and $L \subset Y$ compact and $U \subset Z$ open form a subbasis for the compact open topology on $\mathscr{C}(X,\mathscr{C}(Y,Z))$.

:::{prf:proof}

Let $I$ be an index set $W_i \subset \mathscr{C}(Y,Z)$ be open and $K\subset X$ be compact. 
:::{math}
T\left(K,\bigcup_I W_i\right)=
\bigcup_{n \in \mathbb{N}^+}
\bigcup_{\substack{K_1 \times \ldots \times K_n \subset K^n \\ K_1\cup \ldots \cup K_n = K \\ K_i = \bar{K_i} \forall i }}
\bigcup_{(i_1,\ldots,i_n)\in I^n}
\bigcap_{l=1}^n T(K_{i_l},W_{i_l})
:::
 Suppose $J$ is a finite set. then $T\left(K,\bigcap_{j \in J}W_j\right)=\bigcap_{j \in J}T(K,W_j)$. Sets of the form $T(L,U)$ with $L \subset Y$ compact and $U \subset Z$ open form a subbasis of $\mathscr{C}(Y,Z)$, so if $W \subset \mathscr{C}(Y,Z)$ is open, we have $W=\bigcup_{i\in I}\bigcap_{j \in J_i} T(L_{i_j},U_{i_j})$ so that 
:::{math}
T(K,W)=
\bigcup_{n \in \mathbb{N}^+}
\bigcup_{\substack{K_1 \times \ldots \times K_n \subset K^n \\ K_1\cup \ldots \cup K_n = K \\ K_i = \bar{K_i} \forall i }}
\bigcup_{(i_1,\ldots,i_n)\in J^n}
\bigcap_{l=1}^n
\bigcap_{j \in J_{i_l}}
T(K_{i_l},T(L_{i_lj},U_{i_lj}))
:::
:::
:::



:::{prf:theorem} 
Let $X,Y,Z$ be topological spaces with $X$ and $Y$ Hausdorff and $Y$ locally compact. Then the natural isomorphism 
:::{math}
\bar{\Phi}:\mathscr{C}(X \times Y, Z) \rightarrow \mathscr{C}(X, \mathscr{C}(Y,Z))
:::
 is a homeomorphism.

:::{prf:proof}

Let $f\in \mathscr{C}(X \times Y, Z)$ and let $W\in \mathscr{C}(X,\mathscr{C}(Y,Z))$ be an open neighborhood of $\bar{\Phi}(f)$. By {prf:ref}`cosubbasis_1`, there is an open $U \subset Z$ and compact subsets $L \subset Y$ and $K \subset X$ such that $\bar{phi}(f)\in T(K,T(L,U)) \subset W$. $T(K \times L ,U)$ is open in $\mathscr{C}(X \times Y, Z)$ and note that $f\in T(K \times L ,U)$ since for $(x,y)\in K \times L$, $\bar{\Phi}(f)(x)\in T(L,U)$ and $f(x,y)=\bar{\Phi}(f)(x)(y)\in U$.

Assume that $g\in T(K \times L, U)$. The $\bar{\Phi}(g)(x)(y)=g(x,y)=\in U$ so $\bar{\Phi}(g)(x)\in T(L,U)$ so $\bar{\Phi}(g)\in T(K,T(L,U))$, hence $\bar{\Phi}$ is continuous.
\marginparRest of proof in email 9/27/10
:::
:::



<!-- XXSEC_PREFIX_ENDXX\sectionThe compact-open topology on function spaces -->


<!-- XXSEC_PREFIX_ENDXX\chapterGeneral Topology -->

<!-- XXSEC_DEF_SPLITTERXX\chapterXXSEC_DEF_SPLITTERXXMeasure and Integration theoryXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapterMeasure and Integration theory -->
(chpt:measure-integration-theory_1)=
# Measure and Integration theory
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe category of measurable spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe category of measurable spaces -->
(sec:category-measurable-spaces_1)=
# The category of measurable spaces
The natural domains of measures are the so-called $\sigma$-algebras. Similarly to a topology, a $\sigma$-algebra is a particular kind of set of subsets of some given ambient space $\Omega$. By definition, a $\sigma$-algebra contains the ambient space and is stable under taking complements and countable unions. To construct a measure one usually starts with defining it on a generating set of the $\sigma$-algebra which fulfills some weaker properties like for example is only a ring on $\Omega$. In this section we introduce algebras and $\sigma$-algebras on sets and the related concepts of rings on sets and Dynkin systems. Crucial is the observation that together with their structure preserving maps, the measurable funtions, sets endowed with $\sigma$-algebras form a category, the category of measurable spaces.


<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXX$\sigma$-AlgebrasXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*$\sigma$-Algebras -->
## $\sigma$-Algebras
:::{prf:definition} 
Let $\Omega$ be a set. A *ring on* $\Omega$ is a set $\mathscr{R}$ of subset of $\Omega$ or in other words an element $\mathscr{R}\in \mathscr{P}(\mathscr{P}(\Omega))$ which satisfies the following axioms:


(ite:ring-set-containing-empty-set_1)=
(Rng1)
: $\emptyset \in \mathscr{R}$.

(ite:ring-set-stability-relative-complements_1)=
(Rng2)
: For all $A, B\in \mathscr{R}$ the complement $A \setminus B $ belongs to $\mathscr{R}$.

(ite:ring-set-stability-binary-unions_1)=
(Rng3)
: For all $A, B\in \mathscr{R}$ the union $A \cup B $ lies $\mathscr{R}$.

If in addition

\setcounterenumi3
(ite:ring-set-containing-full-set_1)=
(Rng1)
: $\Omega \in \mathscr{A}$,

then one calls $\mathscr{R}$ an *algebra on* $\Omega$.
:::



:::{prf:proposition} 
:label: thm:equivalent-characerization-set-algebras_1
Let $\Omega$ be a set and $\mathscr{A}$ a set of subsets of $\Omega$. Then $\mathscr{A}$ is an algebra on $\Omega$ if and only if $\mathscr{A}$ has following properties:


(ite:algebra-set-containing-full-set_1)=
(Alg1)
: $\Omega \in \mathscr{A}$.

(ite:algebra-set-stability-complements_1)=
(Alg2)
: For all $A\in \mathscr{A}$ the complement $\complement A = \Omega \setminus A $ belongs to $\mathscr{A}$.

(ite:algebra-set-stability-finite-unions_1)=
(Alg3)
: For each finite sequence $(A_k)_{k=1}^n$ of elements of $\mathscr{A}$ the union $A= \bigcup\limits_{k=1}^n A_k$ belongs to $\mathscr{A}$.
:::



:::{prf:proof}

Assume that $\mathscr{A}$ is an algebra on $\Omega$. Then {ref}`ite:algebra-set-containing-full-set_1` holds true by definition, and {ref}`ite:algebra-set-stability-complements_1` by {ref}`ite:ring-set-stability-relative-complements_1`
and {ref}`ite:algebra-set-containing-full-set_1`. Property {ref}`ite:algebra-set-stability-finite-unions_1`
follows from {ref}`ite:ring-set-stability-binary-unions_1` by induction.

Conversely, assume now that $\mathscr{A}$ satisfies {ref}`ite:algebra-set-containing-full-set_1` to
{ref}`ite:algebra-set-stability-finite-unions_1`. Properties {ref}`ite:ring-set-stability-binary-unions_1`
and {ref}`ite:ring-set-containing-full-set_1` are immediate. Axiom {ref}`ite:ring-set-containing-empty-set_1`
follows by {ref}`ite:algebra-set-stability-complements_1` since $\emptyset = \complement \Omega$. Finally, {ref}`ite:ring-set-stability-relative-complements_1` is true since $A\setminus B$ can be written as $A \cap \complement B$ and since $\mathscr{A}$ is stable under finite intersections by de Morgan's laws.
:::



:::{prf:remark} 
Obviously, the set of rings on a set $\Omega$, the set of algebras on $\Omega$ and the later defined set of $\sigma$-algebras on $\Omega$ are all ordered by set-theoretic inclusion. Therefore, when talking about a ``smaller`` ring or a ``largest'' $\sigma$-algebra we always implicitely mean in regard to set-theoretic inclusion as underlying order relation.
:::



:::{prf:example} 
:label: ex:rings-algebras-sets_1


\itemindent
: Trivial examples of rings and algebras on a set $\Omega$ are the power set $\mathscr{P}(\Omega)$ and the set $\{\emptyset,\Omega\}$. These are the largest and the smallest ring on $\Omega$, respectively.

(ite:ring-generated-half-right-open-intervals_1)=
\itemindent
: Of fundamental importance for Lebesgue integration theory is the ring on euclidean space $\mathbb{R}^n$ generated by the $n$-dimensional right half-open intervals. Let us explain the construction of that ring in some detail. To be precise we mention that the dimension $n$ is assumed to be positive. Now define for any pair of elements $a=(a_1,\ldots,a_n) \in \mathbb{R}^n$ and $b=(b_1,\ldots,b_n) \in \mathbb{R}^n$ the right half-open interval $ {[ a,b \rtsbrak} $ by
   
   :::{math}
   {[ a,b \rtsbrak}  := \big\{ x=(x_1,\ldots , x_n)\in \mathbb{R}^n \bigm\vert \forall i \in \{ 1,\ldots , n\} : a_i \leq x_i < b_i \big\} \ .
   :::
   
   Denote by $\mathscr{I}^n$ the set of right half-open intervals in $\mathbb{R}^n$. Since for $a,b,c,d \in \mathbb{R}^n$ the intersection $ {[ a,b \rtsbrak} \cap  {[ c,d \rtsbrak}  $ coincides with
   
   :::{math}
   \big\{ x\in \mathbb{R}^n \bigm\vert \forall i \in \{ 1,\ldots , n\} : \max \{ a_i ,b_i\} \leq x_i < \min \{ b_i ,d_i\} \big\} \ ,
   :::
   
   the set $\mathscr{I}^n$ ist stable under finite intersections. The empty set is an element of $\mathscr{I}^n$ since for example for $a \in \mathbb{R}^n$ and $b = a$ the relation $ {[ a,a \rtsbrak}  =\emptyset$ holds true. But $\mathscr{I}^n$ is not a ring since the union of finitely many right half-open intervals is in general not a right half-open interval. But one can minimally enlarge $\mathscr{I}^n$ to obtain a ring. Define $\mathscr{R}^n$ as the space of all subsets of $\mathbb{R}^n$ which can be written as the finite union of elements of $\mathscr{I}^n$. Obviously, $\mathscr{I}^n \subset \mathscr{R}^n$ which entails that $\emptyset \in \mathscr{R}^n$. Hence {ref}`ite:ring-set-containing-empty-set_1` holds for $\mathscr{R}^n$. By definition, the union $A\cup B$ of two elements $A,B \in \mathscr{R}^n$ lies in $\mathscr{R}^n$ which means that {ref}`ite:ring-set-stability-binary-unions_1` is fulfilled. It remains to show
   {ref}`ite:ring-set-stability-relative-complements_1`. To this end we proceed in steps and first prove that for elements $A,B \in \mathscr{R}^n$ the intersection $A\cap B$ is also an element of $\mathscr{R}^n$. By assumption, one can represent the two sets in the form $A= \bigcup_{i=1}^k I_i$ and $B= \bigcup_{j=1}^l J_j$ where $k,l\in \mathbb{N}^+$ and $I_1,\ldots , I_k, J_1,\ldots , J_l \in \mathscr{I}^n$. The distributivity law for sets now entails
   
   :::{math}
   A \cap B = \bigcup_{i=1}^k I_i \: \cap \: \bigcup_{j=1}^l J_j =
   \bigcup_{i=1}^k \bigcup_{j=1}^l I_i \cap J_j \ .
   :::
   
   Since $I_i \cap J_j \in \mathscr{I}^n$, the intersection $A\cap B$ therefore lies in $\mathscr{R}^n$. By induction one concludes that $\mathscr{R}^n$ is stable under finite intersections. In the next step we show that $I \setminus J \in \mathscr{R}^n$ for all right half-open intervals $I = {[ a,b \rtsbrak} $ and $J= {[ c,d \rtsbrak} $. To avoid trivial cases we assume $a\leq b$ and $c\leq d$ that is $a_i\leq b_i$ and $c_i\leq d_i$ for all $i \in \{1,\ldots,n\}$. Note that then
   
   :::{math}
   {[ a_i,b_i \rtsbrak} \:\setminus\:  {[ c_i,d_i \rtsbrak} =
   \begin{cases}
   {[ a_i,b_i \rtsbrak}  & \text{if } b_i\leq c_i \text{ or } d_i\leq a_i \ , \\
   {[ a_i,c_i \rtsbrak} \cup  {[ d_i,b_i \rtsbrak}  & \text{if } c_i < b_i \text{ and } a_i < d_i \ .
   \end{cases}
   :::
   
   Hence $  {[ a_i,b_i \rtsbrak} \:\setminus\:  {[ c_i,d_i \rtsbrak}  \in \mathscr{R}^1$. By the formula
   
   :::{math}
   {[ a,b \rtsbrak} \:\setminus \:  {[ c,d \rtsbrak}  =
   \prod_{i=1}^n  {[ a_i,b_i \rtsbrak} \:\setminus\:  {[ c_i,d_i \rtsbrak}
   :::
   
   and since the cartesian product distributes over union, the complement $ {[ a,b \rtsbrak} \:\setminus \:  {[ c,d \rtsbrak} $ coincides with the union of finitely many right half-open intervals, hence is in $\mathscr{R}^n$. In the final step we consider the complement $A \setminus B$ for $A,B \in \mathscr{R}^n$. Representing $A,B$ as before one obtains by de Morgan's laws
   
   :::{math}
   A \:\setminus\: B = \bigcup_{i=1}^k I_i \: \setminus \: \bigcup_{j=1}^l J_j =
   \bigcap_{j=1}^l \Big( \bigcup_{i=1}^k I_i \Big) \: \setminus \: J_j =
   \bigcap_{j=1}^l \bigcup_{i=1}^k \left( I_i\: \setminus \: J_j \right) \ .
   :::
   
   Since $\mathscr{R}^n$ is stable under finite unions and finite intersections the complement $A \setminus B$ must be in $\mathscr{R}^n$ again. This proves that $\mathscr{R}^n$ is a ring on $\mathbb{R}^n$ as claimed. By construction, $\mathscr{R}^n$ is the smallest ring on $\mathbb{R}^n$ containing the set $\mathscr{I}^n$ of right half-open intervals.
:::



:::{prf:definition} 
A ring $\mathscr{R}$ on a set $\Omega$ is called a **$\sigma$-ring on $\Omega$ if it satisfies the following condition:

\setcounterenumi2
($\sigma$Rng1)
: For each sequence $(A_k)_{k\in \mathbb{N}}$ of elements of $\mathscr{R}$ the union $A= \bigcup\limits_{k\in\mathbb{N}} A_k$ belongs to $\mathscr{R}$.

In case a set $\mathscr{A}$ of subsets of $\Omega$ is both a $\sigma$-ring and an algebra on $\Omega$, then one calls $\mathscr{A}$ a **$\sigma$-algebra (*on* $\Omega$). A set $\Omega$ endowed with a $\sigma$-algebra $\mathscr{A}$ on it is referred to as a
*measurable space*. The elements of the $\sigma$-algebra $\mathscr A$ are termed the *measurable subsets* of $\Omega$. We will often denote measurable spaces as pairs $(\Omega,\mathscr{A})$ or $(E,\mathfrak{M})$, where the first component always denotes the underlying set and the second component the $\sigma$-algebra on it.
:::



:::{prf:remark} 
It is immediate by \Crefthm:equivalent-characerization-set-algebras that a set $\mathscr{A}$ of subsets of some $\Omega$ is a $\sigma$-algebra on $\Omega$ if and only if $\mathscr{A}$ satisfies the following conditions:


(ite:sigma-algebra-set-containing-full-set_1)=
($\sigma$Alg1)
: $\Omega \in \mathscr{A}$.

(ite:sigma-algebra-set-stability-complements_1)=
($\sigma$Alg2)
: For all $A\in \mathscr{A}$ the complement $\complement A = \Omega \setminus A $ belongs to $\mathscr{A}$.

(ite:sigma-algebra-set-stability-countable-unions_1)=
($\sigma$Alg3)
: For each sequence $(A_k)_{k\in \mathbb{N}}$ of elements of $\mathscr{A}$ the union $A= \bigcup\limits_{k\in\mathbb{N}} A_k$ belongs to $\mathscr{A}$.

This is the standard list of axioms defining a $\sigma$-algebra and we will use it from now on.
:::



:::{prf:proposition} 
If $\mathscr{A}$ is a $\sigma$-algebra on $\Omega$, then the intersection of countably many measurable sets is also measurable.
:::


:::{prf:proof}

This follows immediately from the axioms and the set-theoretic de Morgan's laws.
:::



:::{prf:example} 


\itemindent
: Let $\Omega$ be any set. Then the power set of $\Omega$ is a $\sigma$-algebra. The set $\{ \emptyset , \Omega \}$ is also a $\sigma$-algebra. These are the largest and smallest $\sigma$-algebra on $\Omega$, respectively.

\itemindent
: Let $\Omega$ be any set. Let $\mathscr A$ be the set of all sets $A\subset \Omega$ such that $A$ or $\Omega \backslash A$ is a countable set. Then $\mathscr A$ is a $\sigma$-algebra.

\itemindent
: Let $E$ be a set, $(\Omega,\mathscr{A})$ a measurable space, and $f:E \to \Omega $ a map. Then the set
   
   :::{math}
   f^{-1} (\mathscr{A}) := \{ M \in \mathscr{P}(E)\mid \exists A \in \mathscr{A} : \: M =f^{-1} (A) \}
   :::
   
   is a $\sigma$-algebra on $E$ called the *preimage* of $\mathscr{A}$ under $f$.
:::


The following two results are extremely useful when constructing examples.


:::{prf:proposition} 
:label: thm:intersection-collectionsigma-algebras_1
Let $\mathfrak{S}$ be a non-empty set of algebras on a set $\Omega$. Then the intersection

:::{math}
\mathscr{A}_\mathfrak{S} = \bigcap\limits_{\mathscr{A} \in \mathfrak{S}} \mathscr{A} =
\big\{ A \in \mathscr{P}(\Omega) \mid A \in \mathscr{A} \text{ for all }
\mathscr{A} \in \mathfrak{S} \big\}
:::

is an algebra on $\Omega$. If each of the elements $\mathscr{A} \in \mathfrak{S}$ is a $\sigma$-algebra, then $\mathscr{A}_\mathfrak{S}$ is so, too.
:::


:::{prf:proof}

Assume first that each $\mathscr{A} \in \mathfrak{S}$ is an algebra on $\Omega$. Obviously, $\Omega \in \mathscr{A}_\mathfrak{S}$ because $\Omega \in \mathscr{A}$ for all $\mathscr{A} \in \mathfrak{S}$. Similarly, if $A \in \mathscr{A}_\mathfrak{S}$, then $A \in \mathscr{A}$, hence $\complement A \in \mathscr{A}$ for all $\mathscr{A} \in \mathfrak{S}$. Therefore, $\complement A $ lies in the intersection $\mathscr{A}_\mathfrak{S} = \bigcap\limits_{\mathscr{A} \in \mathfrak{S}} \mathscr{A} $. Now assume that $(A_k)_{k=1}^n$ is a finite sequence of sets belonging to $\mathscr{A}_\mathfrak{S}$, hence to all $\mathscr{A} \in \mathfrak{S}$. Then the union $\bigcup\limits_{k=1}^n A_k$ is in each of the $\mathscr{A}\in \mathfrak{S}$, hence in $\mathscr{A}_\mathfrak{S}$. The latter argument also works under the condition that every $\mathscr{A} \in \mathfrak{S} $ is a $\sigma$-algebra to verify that for a sequence $(A_k)_{k\in\mathbb{N}}$ in $\mathscr{A} (\mathfrak{S})$ the union $\bigcup\limits_{k\in\mathbb{N}} A_k$ lies in $\mathscr{A}_\mathfrak{S}$. So the proposition is proved.
:::



:::{prf:corollary} 
:label: thm:sigma-algebra-generated-collection-subsets_1
Let $\mathscr{E}$ be a collection of subsets of a set $\Omega$. Then there exists a smallest $\sigma$-algebra on $\Omega$ containing $\mathscr{E}$. It is called the **$\sigma$-algebra generated by $\mathscr{E}$ and will be denoted by $\mathscr{A} (\mathscr{E})$.
:::



:::{prf:proof}

Let $\mathfrak{S}$ be the set of all $\sigma$-algebras on $\Omega$ which contain $\mathscr{E}$. The set of all subsets of $\Omega$ is certainly a $\sigma$-algebra, so $\mathfrak{S} \neq \emptyset$. Let $\mathscr{A} (\mathscr{E})$ be the intersection of all $\sigma$-algebras in the set $\mathfrak{S}$. By the preceding proposition $\mathscr{A} (\mathscr{E})$ is a $\sigma$-algebra. Since every element of $\mathfrak{S}$ contains $\mathscr{E}$, the intersection $\mathscr{A} (\mathscr{E}) = \bigcap\limits_{\mathscr{A} \in \mathfrak{S}} \mathscr{A} $ contains $\mathscr{E}$ as well. By construction, $\mathscr{A} (\mathscr{E})$ is the smallest $\sigma$-algebra with that propery.
:::



:::{prf:remark} 
Obviously, given a collection $\mathscr{E}$ of subsets of $\Omega$ there also exist a smallest ring and a smallest algebra containing $\mathscr{E}$. They are constructed analogously to the $\sigma$-algebra case and are called the
*ring generated by* $\mathscr{E}$ and *algebra generated by* $\mathscr{E}$, respectively. Note that the ring $\mathscr{R}^n$ constructed in
\Crefex:rings-algebras-sets {ref}`ite:ring-generated-half-right-open-intervals_1` is generated in exactly that sense by the set $\mathscr{I}^n$ of right half-open ideals in $\mathbb{R}^n$.
:::



:::{prf:example} 
Let $X$ be a topological space. The $\sigma$-algebra generated by the topology on $X$ is called the \em Borel $\sigma$-algebra on $X$. Its elements are the \em Borel measurable sets or simply the \em Borel sets of $X$. Obviously, all open and all closed sets of $X$ are Borel measurable, as are all countable unions of closed sets and countable intersections of open sets. We will denote the Borel $\sigma$-algebra on $X$ by $\mathscr{A}_{Borel} (X)$ or shortly by $\mathscr{A}_{Borel}$.
:::



:::{prf:example} 


\itemindent
: All intervals including the half-open intervals $ {[ a,b \rtsbrak} $ and $ {\ltsbrak a,b ]} $ with $a < b$ are Borel subsets of $\mathbb{R}$.

\itemindent
: The elements of the ring $\mathscr{R}^n$ constrcuted in
   \Crefex:rings-algebras-sets {ref}`ite:ring-generated-half-right-open-intervals_1`
   are Borel measurable subsets of the euclidean space $\mathbb{R}^n$.

\itemindent
: If $X$ is a topological space with the discrete topology, then every subset of $X$ is Borel measurable.

\itemindent
: If $X$ is a topological space carrying the indiscrete topology $\{ X ,\emptyset \}$, then the $\sigma$-algebra of Borel sets coincides with the topology $\{ X , \emptyset \}$.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*$\sigma$-Algebras -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXDynkin systemsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Dynkin systems -->
## Dynkin systems
In measure theory, one often faces the problem to check whether a system of subsets of some given set is a $\sigma$-algebra. To address that problem the following concept going back to \textscEugene Dynkin is often useful.


:::{prf:definition} 
A system $\mathscr{D}$ of subset of a set $\Omega$ is called a *Dynkin system* (*in* $\Omega$)
if it has the following properties:


(ite:dynkin-axiom-full-set_1)=
(Dyn1)
: $\Omega \in \mathscr{D}$,

(ite:dynkin-axiom-complement_1)=
(Dyn2)
: for all $D\in \mathscr{D}$ the complement $\complement D = \Omega \setminus D $ belongs to $\mathscr{D}$,

(ite:dynkin-axiom-countable-union-pairwise-disjoint-elements_1)=
(Dyn3)
: for each sequence $(D_k)_{k\in \mathbb{N}}$ of pairwise disjoint elements of $\mathscr{D}$ the union $D= \bigcup\limits_{k\in\mathbb{N}} D_k$ belongs to $\mathscr{D}$.
:::



:::{prf:remark} 
By {ref}`ite:dynkin-axiom-full-set_1` and $\ref{ite:dynkin-axiom-complement}$, the empty set is contained in every Dynkin system $\mathscr{D}$. Moreover,
{ref}`ite:dynkin-axiom-countable-union-pairwise-disjoint-elements_1` then entails that every Dynkin system is stable under finite unions of pairwise disjoints elements.
:::


\para Dynkin systems on a set $\Omega$ are ordered by set-theoretic inclusion. Analogously to the case of $\sigma$-algebras one can use this observation to construct the Dynkin system generated by a collection of subsets of $\Omega$.


:::{prf:proposition} 
Let $\mathfrak{S}$ be a non-empty set of Dynkin systems on a set $\Omega$. Then the intersection

:::{math}
\mathscr{D}_\mathfrak{S} = \bigcap\limits_{\mathscr{D} \in \mathfrak{S}} \mathscr{D} =
\big\{ D \in \mathscr{P}(\Omega) \mid D \in \mathscr{D} \text{ for all }
\mathscr{D} \in \mathfrak{S} \big\}
:::

is a Dynkin system on $\Omega$.
:::


:::{prf:proof}

The claim follows immediately from the proof of \Crefthm:intersection-collectionsigma-algebras.
:::



:::{prf:corollary} 
:label: thm:dynkin-system-generated-collection-subsets_1
Let $\mathscr{E}$ be a collection of subsets of a set $\Omega$. Then there exists a smallest Dynkin system on $\Omega$ containing $\mathscr{E}$. It is called the *Dynkin system generated by* $\mathscr{E}$ and will be denoted by $\mathscr{D} (\mathscr{E})$.
:::



:::{prf:proof}

Analogously as in the proof of \Crefthm:sigma-algebra-generated-collection-subsets the claim can be derived from the preceding proposition.
:::



:::{prf:lemma} 
:label: thm:dynkin-system-stability-complements-subsets_1
Let $\mathscr{D}$ be a Dynkin system on a set $\Omega$. Then $\mathscr{D}$ is stable with respect to complements of subsets that means

:::{math}
A \setminus B \in \mathscr{D} \quad \text{for all } A,B \in \mathscr{D} \text{ with } B \subset A \ .
:::
:::



:::{prf:proof}

By assumption, $\complement A$ and $B$ are disjoint and elements of the Dynkin system, hence there union is also in $\mathscr{D}$. Therefore, by de Morgan's laws

:::{math}
A \setminus B = A \cap \complement B = \complement ( \complement A \cup B ) \in \mathscr{D} \ .
:::
:::


The next two results are central for the application of Dynkin system in measure theory.


:::{prf:theorem} 
:label: thm:dynkin-system-stable-finite-intersections-sigma-algebra_1
A Dynkin system $\mathscr{D}$ on a set $\Omega$ is a $\sigma$-algebra if and only if it is stable under binary intersections which in other words means if and only if for two elements $D_1,D_2 \in \mathscr{D}$ the intersection $D_1 \cap D_2 $ belongs to $\mathscr{D}$.
:::



:::{prf:proof}

If the Dynkin system $\mathscr{D}$ is a $\sigma$-algebra, then it is obviously stable under finite intersections. So let us prove the converse and assume that $\mathscr{D}$ contains with two elements also their intersection. Axioms {ref}`ite:sigma-algebra-set-containing-full-set_1` and {ref}`ite:sigma-algebra-set-stability-complements_1`
hold trivially by definition of a Dynkin system. So it remains to show
{ref}`ite:sigma-algebra-set-stability-countable-unions_1`. By assumption on $\mathscr{D}$ and
\Crefthm:dynkin-system-stability-complements-subsets, the complement $A\setminus B = A \setminus (A \cap B)$ lies again in $\mathscr{D}$ whenever $A,B \in \mathscr{D}$. Moreover, since $A\cup B$ can be written as the disjoint union $(A \setminus B ) \cup B$, the Dynkin system $\mathscr{D}$ therefore is stable under finite unions. Now let $(A_k)_{k\in \mathbb{N}}$ be a sequence of elements of $\mathscr{D}$. Define a new sequence $(A_k^\prime)_{k\in \mathbb{N}}$ of elements of $\mathscr{D}$ by

:::{math}
A_0^\prime := A_0, \quad A_{k+1}^\prime = A_{k+1} \setminus \bigcup_{l=0}^k A_l \ .
:::

Note that by our previous observations the sets $A_k^\prime$ are all elements of $\mathscr{D}$, indeed. By induction one checks that

:::{math}
:label: eq:finite-unions-elements-derived-sequence-dynkin-system-stable-finite-intersections_1
\bigcup_{l=0}^k A_l^\prime = \bigcup_{l=0}^k A_l \quad \text{for all } k\in \mathbb{N} .
:::

The elements of the sequence $(A_k^\prime)_{k\in \mathbb{N}}$ are pairwise disjoint by construction, hence the union $\bigcup_{k\in \mathbb{N}} A_k^\prime$ is an element of $\mathscr{D}$. Since by
{eq}`eq:finite-unions-elements-derived-sequence-dynkin-system-stable-finite-intersections_1`
the set $\bigcup_{k\in \mathbb{N}} A_k$ coincides with $\bigcup_{k\in \mathbb{N}} A_k^\prime$, the union of the family $(A_k)_{k\in \mathbb{N}}$ lies again in $\mathscr{D}$. This proves {ref}`ite:sigma-algebra-set-stability-countable-unions_1`, and $\mathscr{D}$ is a $\sigma$-algebra.
:::



:::{prf:theorem} 
:label: thm:dynkin-system-generated-system-stable-finite-intersections-equals-generated-sigma-algebra_1
Assume that $\mathscr{E}$ is a set of subsets of $\Omega$ which contains with each pair of elements also their intersection. Then the Dynkin system and the $\sigma$-algebra generated by $\mathscr{E}$ coincide that is

:::{math}
\mathscr{D} (\mathscr{E}) = \mathscr{A} (\mathscr{E}) \ .
:::
:::



:::{prf:proof}

Since every $\sigma$-algebra is a Dynkin system and since $\mathscr{A} (\mathscr{E})$ contains $\mathscr{E}$, the inclusion $\mathscr{D} (\mathscr{E}) \subset \mathscr{A} (\mathscr{E})$ is clear by the minimality assumption of $\mathscr{D} (\mathscr{E})$. So it remains to show that $\mathscr{A} (\mathscr{E}) \subset \mathscr{D} (\mathscr{E})$. This relation follows if we can verify that $\mathscr{D} (\mathscr{E})$ is a $\sigma$-algebra. Hence by \Crefthm:dynkin-system-stable-finite-intersections-sigma-algebra it suffices to show that $\mathscr{D} (\mathscr{E})$ contains with any two elements also their intersection. To this end put for $D\in \mathscr{D} (\mathscr{E})$

:::{math}
\mathscr{D}_D := \{ A \in \mathscr{P}(\Omega) \mid A \cap D \in \mathscr{D} (\mathscr{E} \} \ .
:::

Let us show that $\mathscr{D}_D$ is a Dynkin system. Obviously, $\Omega \in \mathscr{D}_D$. If $A\in \mathscr{D}_D$, then $\complement A \cap D = D \setminus A = D \setminus (A \cap D) \in \mathscr{D} (\mathscr{E})$ by \Crefthm:dynkin-system-stability-complements-subsets. Hence $\complement A \in \mathscr{D}_D$. If $(A_k)_{k\in \mathbb{N}}$ is a family of pairwise disjoint elements of $\mathscr{D}_D$, then $\bigcup_{k\in \mathbb{N}} A_k\in\mathscr{D}_D$ since $A_k\cap D\in \mathscr{D} (\mathscr{E})$ for all $k\in \mathbb{N}$ and therefore

:::{math}
\Big(\bigcup_{k\in \mathbb{N}} A_k\Big) \cap D = \bigcup_{k\in \mathbb{N}} ( A_k \cap D ) \in \mathscr{D} (\mathscr{E}) \ .
:::

By assumption on $\mathscr{E}$ and because $\mathscr{E} \subset \mathscr{D} (\mathscr{E})$ the relation $\mathscr{E} \subset \mathscr{D}_E$ holds true for all $E\in\mathscr{E}$. Since $\mathscr{D}_E$ is a Dynkin system, this entails $\mathscr{D} (\mathscr{E}) \subset \mathscr{D}_E$ for all $E\in\mathscr{E}$. Given $D\in \mathscr{D} (\mathscr{E})$ one concludes that $E\cap D \in \mathscr{D} (\mathscr{E})$ for all $E\in\mathscr{E}$, hence $\mathscr{E}\subset \mathscr{D}_D$ and $ \mathscr{D} (\mathscr{E})\subset \mathscr{D}_D$. But that means that $ \mathscr{D} (\mathscr{E})$ is stable under binary intersections and the claim is proved.
:::


Application of this results leads to an important observation about the $\sigma$-algebra generated by the right half-open intervals in euclidean space.


:::{prf:proposition} 
The Dynkin system generated by the set $\mathscr{I}^n$ of right half-open intervals in $\mathbb{R}^n$ is a $\sigma$-algebra and coincides with the Borel $\sigma$-algebra $\mathscr{A}_{Borel} (\mathbb{R}^n)$. More precisely,

:::{math}
\mathscr{I}^n \subset \mathscr{R}^n \subset \mathscr{D} (\mathscr{I}^n) = \mathscr{A} (\mathscr{I}^n) =
\mathscr{A}_{Borel} (\mathbb{R}^n) \ ,
:::

where $ \mathscr{R}^n$ denotes the ring on $\mathbb{R}^n$ generated by $\mathscr{I}^n$.
:::



:::{prf:proof}

Obviously $\mathscr{I}^n \subset \mathscr{A}_{Borel} (\mathbb{R}^n)$. Moreover, $\mathscr{I}^n $ is stable under finite intersections as shown in \Crefex:rings-algebras-sets {ref}`ite:ring-generated-half-right-open-intervals_1`. By \Crefthm:dynkin-system-generated-system-stable-finite-intersections-equals-generated-sigma-algebra, the claim now is proved when we can show that the Borel $\sigma$-algebra on $\mathbb{R}^n$ is generated by $\mathscr{I}^n$. But that is clear since for all $a,b \in \mathbb{R}^n$ the open interval

:::{math}
{\ltsbrak a,b \rtsbrak}  := \big\{ x\in \mathbb{R}^n \bigm\vert \forall i\in \{1,\ldots,n\} \colon a_i < x_i < b_i \big\}
:::

can be written as the union of the countable family $\big( {[ a-\frac 1k,b \rtsbrak} \big)_{k\in \mathbb{N}^+}$ of elements of $\mathscr{I}^n $, and since the set of all open intervals $ {\ltsbrak a,b \rtsbrak}  \subset \mathbb{R}^n$ with $a,b \in \mathbb{Q}^n$ is a countable basis of the topology of $\mathbb{R}^n$.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Dynkin systems -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXMeasurable functionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Measurable functions -->
## Measurable functions
:::{prf:definition} 
Let $(\Omega,\mathscr{A})$ and $(E,\mathfrak{M})$ be two measurable spaces. A map $f\colon \Omega \rightarrow E$ is termed \em measurable if the set $f^{-1}(M)$ is measurable for every measurable set $M\subset E$ that is if $f^{-1}(M) \in \mathscr{A}$ for all $M\in \mathfrak{M}$.
:::



:::{prf:remark} 
Let $(\Omega,\mathscr{A})$ be a measurable space. A real or complex valued function $f:\Omega \to \mathbb{K}$ with $K=\mathbb{R}$ or $=\C$ is understood to be measurable if it is measurable when $\mathbb{K}$ is equipped with the Borel $\sigma$-algebra $\mathscr{A}_{Borel} (\mathbb{K})$.
:::



:::{prf:example} 
:label: ex:characteristic-function_1
Let $(\Omega,\mathscr{A})$ be a measurable space, and let $A\subset \Omega$ be a measurable set. Then the function $\chi_A \colon \Omega\rightarrow \mathbb{R}$ given by the formula

:::{math}
\chi_A (x) = \begin{cases} 1 & \text{for } x\in A, \\ 0 & \text{for } x\not\in A,
\end{cases}
:::

is measurable since for each Borel set $B \subset \mathbb{R}$ the preimage $\chi_A^{-1} (B)$ is either $\emptyset$, $A$, $\complement A$ or $\mathbb{R}$, depending on whether $0,1\notin B$, $1 \in B$ but $0\notin B$, $0 \in B$ but $1\notin B$ or $0,1\in B$, respectively. The function $\chi_A$ is called the \em characteristic function of $A$.
:::



:::{prf:theorem} 
:label: thm:category-measurable-spaces_1


\itemindent
: The identity map $\mathrm{id}_\Omega$ on a measurable space $(\Omega,\mathscr{A})$ is measurable.

\itemindent
: Let $(\Omega_1,\mathscr{A}_1)$, $(\Omega_2,\mathscr{A}_2)$ and $(\Omega_3,\mathscr{A}_3)$ be measurable spaces. Assume that $f:\Omega_1\rightarrow \Omega_2$ and $g:\Omega_2\rightarrow \Omega_3$ are maps. If $f$ and $g$ are both measurable, so is $g\circ f :\Omega_1\to \Omega_3$.

\itemindent
: Measurable spaces as objects together with measurable maps as morphisms form a category. It is called the *category of measurable spaces* and will be denoted by $\mathsf{Measble}$.
:::



:::{prf:proof}

By definition the identity map $\mathrm{id}_\Omega$ is measurable. Under the assumption that $f$ and $g$ are measurable let $A\in\mathscr{A}_3$. Then $g^{-1}(A)\in\mathscr{A}_2$ since $g$ is measurable. Hence $f^{-1}(g^{-1}(A))\in \mathscr{A}_1$ since $f$ is measurable. Therefore, the composition $g\circ f$ is measurable. The claim follows.
:::



:::{prf:proposition} 
:label: thm:measurability-terms-generating-set_1
Let $(\Omega_i,\mathscr{A}_i)$ for $i=1,2$ be measurable spaces and assume that the $\sigma$-algebra $\mathscr{A}_2$ is generated by the set $\mathscr{E}\subset \mathscr{A}_2$. Then a map $f:\Omega_1 \to \Omega_2$ is measurable if and only for all $E\in \mathscr{E}$ the preimage $f^{-1} (E)$ is measurable.
:::



:::{prf:proof}

If $f$ is measurable, then $f^{-1} (E)\in \mathscr{A}_1$ for all $E\in \mathscr{E}$ by definition of measurability. It remains to prove the converse. So assume that $f^{-1} (E)\in \mathscr{A}_1$ for all $E\in \mathscr{E}$. Then the set

:::{math}
\mathfrak{M}= \big\{ A \in \mathscr{P}(\Omega_2) \mid f^{-1} (A) \in \mathscr{A}_1 \big\}
:::

is a $\sigma$-algebra since it contains $\Omega_2$ and is stable under complements and countable unions. Moreover, $\mathscr{E} \subset \mathfrak{M}$ by assumption. Since $\mathscr{A}_2$ is generated by $\mathscr{E}$, the relation $\mathscr{A}_2 \subset \mathfrak{M}$ follows and the claim is proved.
:::



:::{prf:corollary} 
Let $(\Omega,\mathscr{A})$ be a measurable space and $f:X \to \mathbb{R}$ a function. Then the following are equivalent:



(ite:measurability-real-valued-function_1)=
(i)
: $f$ is measurable with respect to the Borel $\sigma$-algebra on $\mathbb{R}$.

(ite:preimage-open-sets-measurable_1)=
(ii)
: The preimage $f^{-1} (O)$ of any open subset $O\subset \mathbb{R}$ is measurable.

(ite:preimage-closed-sets-measurable_1)=
(iii)
: The preimage $f^{-1} (A)$ of any closed subset $A\subset \mathbb{R}$ is measurable.

(iv)
: The preimage $f^{-1} ( {\ltsbrak a,b \rtsbrak}  )$ of any open interval $ {\ltsbrak a,b \rtsbrak}  \subset \mathbb{R}$ with $a,b\in \mathbb{R}$ is measurable.

(v)
: The preimage $f^{-1} ( {[ a,b ]} )$ of any closed interval $ {[ a,b ]} \subset \mathbb{R}$ with $a,b\in \mathbb{R}$ is measurable.

(vi)
: The preimage $f^{-1} ( {[ a,b \rtsbrak} )$ of any right half-open interval $ {[ a,b \rtsbrak} \subset \mathbb{R}$ with $a,b\in \mathbb{R}$ is measurable.

(vii)
: The preimage $f^{-1} ( {\ltsbrak a,b ]} )$ of any left half-open interval $ {\ltsbrak a,b ]} \subset \mathbb{R}$ with $a,b\in \mathbb{R}$ is measurable.
:::



:::{prf:proof}

The equivalence of {ref}`ite:measurability-real-valued-function_1` and {ref}`ite:preimage-open-sets-measurable_1`
follows from the preceding proposition since the open sets generate the Borel $\sigma$-algebra on $\mathbb{R}$. Likewise {ref}`ite:measurability-real-valued-function_1` and {ref}`ite:preimage-closed-sets-measurable_1`
are equivalent because the closed subsets of $\mathbb{R}$ also generate the Borel $\sigma$-algebra. For the other equivalences it suffices to show that the sets of open intervals, of closed intervals and of right respectively of left half-open intervals each generate the Borel $\sigma$-algebra on $\mathbb{R}$. Since every open set in $\mathbb{R}$ is the countable union of open intervals, this is clear for the set of open intervals. An open interval of the form $ {\ltsbrak a,b \rtsbrak} $ can be written as the countable union $\bigcup_{n=1}^\infty  {[ a+\frac 1n ,b -\frac 1n ]} $, which implies that the closed bounded intervals generate the Borel $\sigma$-algebra. Similarly, $ {\ltsbrak a,b \rtsbrak}  = \bigcup_{n=1}^\infty  {[ a+\frac 1n ,b \rtsbrak} =\bigcup_{n=1}^\infty  {\ltsbrak a,b -\frac 1n ]} $, which entails that the set of right half-open intervals and the set of left half-open intervals each generate the Borel $\sigma$-algebra.
:::



:::{prf:definition} 
Let $f\colon X\rightarrow Y$ be a mapping between topological spaces. If $f$ is measurable with respect to the Borel $\sigma$-algebras on $X$ and $Y$, respectively, then one calls $f$ *Borel measurable* or a
*Borel function*.
:::



:::{prf:example} 
By \Crefthm:measurability-terms-generating-set, a continuous function $f:X\to Y$ between topological spaces is Borel measurable.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Measurable functions -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXCategorical constructionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Categorical constructions -->
## Categorical constructions
:::{prf:theorem} 
Let $(\Omega_i,\mathscr{A}_i)$, $i\in I := \{ 1,2 \}$ be two measurable spaces. Denote by $\Omega_1\sqcup\Omega_2 = \bigcup_{i\in I} \{ (p,i) \in (\Omega_1\cup\Omega_2) \times I \mid p \in \Omega_i \}$ their disjoint union and by $\Omega_1 \times \Omega_2$ their cartesian product. Let $\mathscr{A}_1 \coprod \mathscr{A}_2$ be the $\sigma$-algebra generated by the collection of disjoint unions $A_1 \sqcup A_2 \subset \Omega_1\sqcup\Omega_2$ and $\mathscr{A}_1 \prod \mathscr{A}_2$ the $\sigma$-algebra generated by the set of cartesian products $A_1 \times A_2 \subset \Omega_1\times\Omega_2$, where in both cases $A_i$ runs through the elements of $\mathscr{A}_i$ for both $i\in I$. Then the pairs $(\Omega_1,\mathscr{A}_1)\coprod (\Omega_2,\mathscr{A}_2) := \big( \Omega_1\sqcup\Omega_2 , \mathscr{A}_1\coprod\mathscr{A}_2 \big)$ and $(\Omega_1,\mathscr{A}_1)\prod (\Omega_2,\mathscr{A}_2) := \big( \Omega_1\times\Omega_2 , \mathscr{A}_1 \prod \mathscr{A}_2 \big)$ form the categorical coproduct and product, respectively, of $(\Omega_1,\mathscr{A}_1)$ and $(\Omega_2,\mathscr{A}_2)$ within the category of measurable spaces.
:::



:::{prf:proof}

By construction, $(\Omega_1,\mathscr{A}_1)\coprod (\Omega_2,\mathscr{A}_2)$ and $(\Omega_1,\mathscr{A}_1)\prod (\Omega_2,\mathscr{A}_2)$ are measurable spaces, so it remains to show that they fulfill the universal properties of the coproduct and product, respectively. To this end observe first that for $i\in I$ we have natural maps

:::{math}
\iota_{\Omega_i} = \iota_i
\colon: \: \Omega_i \hookrightarrow \Omega_1 \sqcup \Omega_2, \quad p \mapsto (p,i)
:::

and

:::{math}
\pi_{\Omega_i} = \pi_i
\colon \: \Omega_1 \times \Omega_2 \to \Omega_i, \quad (p_1,p_2) \mapsto p_i \ .
:::

The injections $\iota_1$ and $\iota_2$ are measurable by \Crefthm:measurability-terms-generating-set
and the construction of $\mathscr{A}_1\coprod\mathscr{A}_2$. The projections $\pi_1$ and $\pi_2$ are measurable by definition of $\mathscr{A}_1\times\mathscr{A}_2$.

Now assume that $(E,\mathfrak{M})$ is a measurable space and that there are measurable maps $g_i: \Omega_i \to E$. Define $g : \Omega_1\sqcup \Omega_2 \to E$ by $(p,i) \mapsto g (p,i) = g_i (p)$. Then $g$ is measurable by \Crefthm:measurability-terms-generating-set since for $A_i\in \mathscr{A}_i$ the preimage $g^{-1} (A_i\times \{ i\}) = g_i^{-1} (A_i)$ is measurable. Moreover, $g\circ \iota_i= g_i$ for $i\in I$, and $g$ is the only map with that property. Hence, $(\Omega_1,\mathscr{A}_1)\coprod (\Omega_2,\mathscr{A}_2)$ together with the maps $\iota_i$, $i\in I$ is the categorical coproduct in the category $\mathsf{Measbl}$.

Finally assume that we are given measurable maps $f_i: E \to \Omega_i$. Define $f : E \to \Omega_1\times \Omega_2$ by $e \mapsto (f_1(e),f_2(e))$. Since for all $A_1\in \mathscr{A}$ and $A_2\in\mathscr{A}_2$ the preimage $f^{-1} (A_1 \times A_2)$ coincides with the intersection $f_1^{-1} (A_1) \cap f_2^{-1} (A_2)$, the map $f$ is measurable by measurability of the $f_i$ and by \Crefthm:measurability-terms-generating-set. Clearly, $\pi_i \circ f= f_i$ for $i\in I$, and $f$ is the only map having that property. Altogethr this proves that $(\Omega_1,\mathscr{A}_1)\prod (\Omega_2,\mathscr{A}_2)$ together with the maps $\pi_i$, $i\in I$ is the categorical product in the category $\mathsf{Measbl}$.
:::



:::{prf:remark} 


\itemindent
: The unique map $g$ associated to the measurable maps $g_i:\Omega_i\to E$, $i=1,2$ in the universal property of the coproduct will sometimes be denoted by $[g_1,g_2] : \Omega_1\sqcup \Omega_2 \to E$. The unique map $f$ associated to the measurable maps $f_i :E\to \Omega_i$, $i=1,2$ in the universal property of the product will often be written as a pair $(f_1,f_2)$ or sometimes as $\langle f_1,f_2\rangle$.

\itemindent
: Assume to be given two measurable functions $f_i : (\Omega_i,\mathscr{A}_i)\to (E_i,\mathfrak{M}_i)$ with $i=1,2$. By the universal properties of the product and coproduct there exist uniquely determined measurable functions $f_1 \sqcup f_2 : \Omega_1\sqcup \Omega_2 \to E_1\sqcup E_2$ and $f_1 \times f_2 : \Omega_1\times \Omega_2 \to E_1\times E_2$ making the following diagrams for $i =1,2$ commute:
   
   :::{math}
   \begin{tikzcd}
   \Omega_i \arrow{r}{\iota_{\Omega_i}} \arrow[swap]{d}{f_i} & \Omega_1\sqcup \Omega_2 \arrow{d}{f_1\sqcup f_2} \\ E_i \arrow[swap]{r}{\iota_{E_i}} & E_1\sqcup E_2
   \end{tikzcd}
   \qquad
   \begin{tikzcd}
   \Omega_1\times \Omega_2 \arrow[swap]{d}{f_1\times f_2} \arrow{r}{\pi_{\Omega_i}} & \Omega_i \arrow{d}{f_i} \\ E_1 \times E_2 \arrow[swap]{r}{\pi_{E_i}} & E_i
   \end{tikzcd}
   :::
   
   These diagrams can be understood as functoriality relations for the coproduct and product in $\mathsf{Measbl}$, respectively.

\itemindent
: If $X$ and $Y$ are topological spaces, the product $\sigma$-algebra $\mathscr{A}_{Borel} (X\times Y)$ of the product topological space $X\times Y$ coincides with the product $\sigma$-algebra of the Borel $\sigma$-algebras $\mathscr{A}_{Borel} (X)$ and $\mathscr{A}_{Borel} (Y)$ since the product sets $ U\times V$ form a basis of the topology on $X\times Y$ and a generating system of the product $\sigma$-algebra $\mathscr{A}_{Borel} (X) \prod \mathscr{A}_{Borel} (Y)$ when $U$ and $V$ run through the open sets of $X$ and $Y$, respectively.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Categorical constructions -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXAlgebras of real and complex valued measurable functionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Algebras of real and complex valued measurable functions -->
## Algebras of real and complex valued measurable functions
:::{prf:proposition} 
:label: thm:algebra-measurable-real-complex-valued-functions_1
Let $\mathbb{K}$ be the field of real or complex numbers and $(\Omega,\mathscr{A})$ a measurable space. Endow $\mathbb{K}$ with the Borel $\sigma$-algebra. Then the set $\mathscr{M} (\Omega,\mathbb{K})$ of measurable $\mathbb{K}$-valued functions becomes an algebra over $\mathbb{K}$ with pointwise addition, poitwise scalar multiplication and pointwise multiplication of functions as structure operations.
:::



:::{prf:proof}

It suffices to show that $\mathscr{M} (\Omega,\mathbb{K})$ is a subalgebra of the algebra $\mathscr{F} (\Omega,\mathbb{K})$ of $\mathbb{K}$-valued functions on $\Omega$. More precisely, we therefore only need to show that for $f,f_1,f_2 \in \mathscr{M} (\Omega,\mathbb{K})$ and $\lambda\in \mathbb{K}$ the functions $f_1 + f_2$, $\lambda f$ and $f_1 \cdot f_2$ are measurable again. To this end recall that the functions

:::{math}
\begin{split}
\alpha\colon & \: \mathbb{K} \times \mathbb{K} \to \mathbb{K}, \quad (x,y) \mapsto x+y \ , \\
\mu \colon & \: \mathbb{K} \times \mathbb{K} \to \mathbb{K}, \quad (x,y) \mapsto x\cdot y \ , \text{ and}\\
\mu_\lambda \colon & \: \mathbb{K} \to \mathbb{K}, \quad x \mapsto \lambda\cdot y
\end{split}
:::

are continuous, hence Borel measurable. Since the map $f$ is measurable by assumption and $(f_1,f_2) : \Omega \to \mathbb{K} \times \mathbb{K}$, $p\mapsto (f_1(p),f_2(p))$ by the universal property of the product in $\mathsf{Measbl}$, the compositions $\lambda f = \mu_\lambda \circ f$, $f_1 + f_2 = \alpha \circ (f_1,f_2)$ and $f_1\cdot f_2 = \mu \circ (f_1,f_2)$ are all measurable.
:::



:::{prf:proposition} 
Let $f\colon \Omega\rightarrow \C$ be a function on a measurable space $(\Omega,\mathscr{A})$. Then the function $f$ is measurable if and only if the functions $\Re (f)$ and $\Im (f)$ are measurable.
:::



:::{prf:proof}

Since the maps $\Re :\C \cong \mathbb{R}^2\to \mathbb{R}$ and $\Im :\C \cong \mathbb{R}^2 \to \mathbb{R}$ are the projections onto the first and second coordinate, respectively, and since $f$ can be identified with the pair $(\Re (f) , \Im (f))$, the claim is essentially a consequence of the universal property of the product in the category $\mathsf{Measbl}$.
:::



:::{prf:proposition} 
Let $f\colon \Omega\rightarrow \C$ be a measurable function on the measurable space $(\Omega,\mathscr{A})$. Then the function $|f|$ is measurable, and there is a measurable function $\alpha \colon \Omega\rightarrow \C$ having image in $\mathbb{S}^1$ such that $f= \alpha |f|$.
:::



:::{prf:proof}

Since the absolut value $|\cdot|\colon \C \to \mathbb{R}_{\geq 0}$ is continuous, hence Borel measurable, the composition $|f|$ is measurable by assumption on $f$. Let $E = \{ p\in \Omega \mid f(p)=0 \}$. Then the set $E$ is the inverse image of a closed subset, and so measurable. We can define a continuous function $\varphi \colon \C\setminus \{ 0\} \rightarrow \C$ by the formula $\varphi (z) = z/|z|$. By measurability of $\varphi$ it follows from
\Crefthm:algebra-measurable-real-complex-valued-functions
that the function $\alpha \colon \Omega \rightarrow \C$ defined by the formula $\alpha = \varphi \circ (f + \chi_E )$ is measurable. The formulae $|\alpha (p)| =1$ for all $p\in \Omega$ and $f=\alpha |f|$ are immediate by construction.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Algebras of real and complex valued measurable functions -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXMeasurable numerical functionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Measurable numerical functions -->
## Measurable numerical functions
:::{prf:definition} 
Let $(a_n)$ be a sequence of real numbers. Then we define 
:::{math}
{\lim \sup}_{n\rightarrow \infty} a_n = {\lim \sup}_{n\rightarrow \infty} \{ a_n , a_{n+1} , a_{n+2} , \ldots \}
:::
 and 
:::{math}
{\lim \inf}_{n\rightarrow \infty} a_n = {\lim \inf}_{n\rightarrow \infty} \{ a_n , a_{n+1} , a_{n+2} , \ldots \}
:::
:::


We can pass from results about $\lim \sup$ to results about $\lim \inf$, or conversely, by the observation 
:::{math}
{\lim \sup}_{n\rightarrow \infty} a_n = - {\lim \inf}_{n\rightarrow \infty} (-a_n)
:::


It will occasionally be convenient to us to allow $\infty$ and $-\infty$ as values of limits and functions. This is a safe enough option provided we do not attempt to do arithmetic with these symbols; for example, expressions such as `$\infty - \infty$' are completely meaningless.

However, we can form `intervals' 
:::{math}
[a,\infty ] = [a ,\infty )\cup \{ \infty \} \qquad [\infty ,b] = (\infty ,b]\cup \{ \infty \}
:::
 and so on. These intervals are topological spaces. We can also allow ourselves the inequality 
:::{math}
-\infty < a < \infty
:::
 for all $a\in {\mathbb R}$. The standard result about $\lim \sup$ and $\lim \inf$ can now be expressed quite simply; although a number of special cases need to be examined in the proof.


:::{prf:theorem} 
Let $(a_n)$ be a real-valued sequence. Then the limits 
:::{math}
{\lim \inf}_{n\rightarrow \infty} a_n \in [-\infty , \infty ) \qquad {\lim \sup}_{n\rightarrow \infty} a_n \in (-\infty , \infty ]
:::
 exist and satisfy the inequality 
:::{math}
{\lim \inf}_{n\rightarrow \infty} a_n \leq {\lim \sup}_{n\rightarrow \infty} a_n
:::


Further, the equality 
:::{math}
{\lim \inf}_{n\rightarrow \infty} a_n = a = {\lim \sup}_{n\rightarrow \infty} a_n
:::
 holds precisely when the sequence $(a_n)$ converges to the real number $a$.
**proof to be filled in!**
:::


Note that the number $a$ in the above result must be finite.


:::{prf:proposition} 
Let $\Omega$ be a measurable space, and let $f\colon \Omega \rightarrow [\infty , \infty]$ be any map. Suppose that the inverse image $f^{-1}((\alpha , \infty ])$ is measurable for every point $\alpha \in {\mathbb R}$. Then the function $f$ is measurable.
:::



:::{prf:proof}

Let 
:::{math}
{\mathscr M} = \{ E\subseteq [-\infty ,\infty]\ |\ f^{-1}[E] \textrm{ is measurable } \}
:::


By proposition ERROR_UNDEFINED_LABEL_ime_-1 the set $\mathscr M$ is a $\sigma$-algebra. Choose points $\alpha \in {\mathbb R}$ and $\alpha_n < \alpha$ such that $\lim_{n\rightarrow \infty} \alpha_n = \alpha$. Since the set $(\alpha_n , \infty ]$ is measurable by hypothesis, and 
:::{math}
[-\infty , \alpha ) = \bigcup_{n=1}^\infty [-\infty , \alpha_n ] = \bigcup_{n=1}^\infty [-\infty , \infty ]\backslash (\alpha_n , \infty]
:::
 it follows that $[-\infty , \alpha )\in \Omega$. Hence 
:::{math}
(\alpha , \beta ) = [-\infty , \beta ) \cap (\alpha , \infty ] \in \Omega
:::
 for every point $\alpha , \beta \in {\mathbb R}$. Since every open set in $[-\infty , \infty ]$ is a countable union of such open intervals, the collection $\mathscr M$ contains every open set. Thus the map $f$ is measurable.
:::



:::{prf:corollary} 
Let $f_n\colon X\rightarrow [-\infty , \infty]$ be measurable functions for $n\in {\mathbb N}$. Then the functions 
:::{math}
\sup \{ f_n \} \quad {\lim \sup}_{n\rightarrow \infty} f_n \quad \inf \{ f_n \} \quad {\lim \inf}_{n\rightarrow \infty} f_n
:::
 are measurable.
:::



:::{prf:proof}

Let $a\in {\mathbb R}$. Observe that the set 
:::{math}
(\sup \{ f_n \})^{-1} (a,\infty ] = \bigcup_{n=1}^\infty f_n^{-1}(a,\infty ]
:::
 is measurable. Hence by the above proposition, the function $\sup \{ f_n \}$ is measurable. The formula $\inf \{ f_n \} = - \sup \{ -f_n \}$ tells us that the function $\inf \{ f_n \}$ is also measurable.

Now, for each point $x\in \Omega$, the sequence of numbers 
:::{math}
g_n (x) = \sup \{ f_n (x) , f_{n+1} (x) , f_{n+2}(x) , \ldots \}
:::
 is monotonic increasing. It follows that 
:::{math}
{\lim \sup }_{n\rightarrow \infty} f_n (x) = \inf \{ g_n (x) \}
:::


We know that each function $f_n$ is measurable. The above argument tells us that each function $g_n$ is measurable, and that the function ${\lim \sup}_{n\rightarrow \infty}f_n$ is measurable. A similar argument tells us that the function ${\lim \inf}_{n\rightarrow \infty}g_n$ is measurable.
:::



:::{prf:corollary} 
If $f,g\colon X\rightarrow [-\infty, \infty ]$ are measurable functions, then so are the functions $\max \{ f,g \}$ and $\min \{ f,g \}$.
**proof to be filled in!**
:::



:::{prf:corollary} 
The limit of a pointwise-convergent sequence of meaurable functions is measurable.
**proof to be filled in!**
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Measurable numerical functions -->

<!-- XXSEC_PREFIX_ENDXX\sectionThe category of measurable spaces -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXMeasure SpacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionMeasure Spaces -->
(sec:measure-spaces_1)=
# Measure Spaces
:::{prf:definition} 
Let $\Omega$ be a measurable space, equipped with a $\sigma$-algebra $\mathscr A$. A *measure* on $\Omega$ is a function $\mu \colon {\mathscr A}\rightarrow [0,\infty ]$ such that:


(M1)
: The function $\mu$ is **$\sigma$-additive, i.e.
   
   :::{math}
   \mu \left( \bigcup_{n=1}^\infty A_n \right) = \sum_{n=1}^\infty \mu (A_n ) \ ,
   :::
   
   whenever $(A_n)_{n\in \mathbb{N}}$ is a sequence of disjoint mesaurable sets.

(M2)
: There is a measurable set $A$ such that $\mu (A) < \infty$.

The number $\mu (A)$ is called the *measure* of a set $A$. A measurable space equipped with some measure is called a
*measure space*.
:::


For the above definition to make sense, we need to make a convention concerning our `number' $\infty$, namely that $a + \infty = \infty$ whenever $a\in [0,\infty ]$.


:::{prf:example} 
Let $\Omega$ be a measurable space. For any measurable set $E\subseteq \Omega$, let us define $\mu (E) = |E|$, where $|E|$ denotes the number of elements of $E$. Then $\mu$ is a measure on $\Omega$, called the \em counting measure.
:::



:::{prf:example} 
Let $\Omega$ be a measurable space, and let $x_0 \in \Omega$. For any measurable set $E\subseteq \Omega$, let us define 
:::{math}
\mu (E) = \left\{ \begin{array}{ll}
1 & x_0 \in E \\ 0 & x_0 \not\in E \\
\end{array} \right.
:::


Then $\mu$ is a measure on $\Omega$, called the \em Dirac measure.
:::



:::{prf:proposition} 
Let $\Omega$ be a measure space, with measure $\mu$. Then $\mu (\emptyset ) =0$.
:::



:::{prf:proof}

Choose a measurable set $A$ such that $\mu (A) < \infty$. Then 
:::{math}
\mu (A) = \mu (A) + \mu (\emptyset ) + \mu (\emptyset ) +\cdots
:::
 Hence $\mu (\emptyset ) =0$.
:::



:::{prf:corollary} 
Let $A_1 , \ldots , A_n$ be disjoint measurable sets. Then 
:::{math}
\mu (A_1 \cup \cdots \cup A_n ) = \mu (A_1 ) + \cdots + \mu (A_n)
:::

**proof to be filled in!**
:::



:::{prf:corollary} 
Let $A$ and $B$ be measurable set where $A\subseteq B$. Then $\mu (A) \leq \mu (B)$.
:::



:::{prf:proof}

The set $B\backslash A = B\cap (\Omega \backslash A )$ is measurable, the sets $A$ and $B\backslash A$ are disjoint, and $B = A\cup B\backslash A$. By the above corollary 
:::{math}
\mu (B) = \mu (A) + \mu (B\backslash A)
:::


The inequality $\mu (A)\leq \mu (B)$ follows since $\mu (B\backslash A)\geq 0$.
:::



:::{prf:proposition} 
:label: limsub_1
Let $(A_n )$ be a sequence of measurable sets such that $A_n \subseteq A_{n+1}$ for all $n$. Let $A = \bigcup_{n=1}^\infty A_n$. Then $\lim_{n\rightarrow \infty} \mu (A_n ) = \mu (A)$.
:::



:::{prf:proof}

Let $B_1 =A_1$, and $B_n = A_n \backslash A_{n-1}$ when $n\geq 2$. Then the sets $B_n$ are measurable and disjoint. Further 
:::{math}
A_n = B_1 \cup \cdots \cup A_n \qquad A= \bigcup_{n=1}^\infty B_n
:::


Hence 
:::{math}
\mu (A) = \sum_{n=1}^\infty \mu (B_n) = \lim_{N\rightarrow} \sum_{n=1}^N \mu (B_n) = \lim_{N\rightarrow \infty}\mu (A_N)
:::
:::



:::{prf:corollary} 
Let $(A_n)$ be a sequence of measurable sets such that $\mu (A_1) < \infty$ and $A_{n+1}\subseteq A_n$ for all $n$. Let $A = \bigcap_{n=1}^\infty A_n$. Then $\lim_{n\rightarrow \infty} \mu (A_n ) = \mu (A)$.
:::



:::{prf:proof}

Let $C_n =A_1\backslash A_n$. Then the set $C_n$ is measurable, $C_n\subseteq C_{n+1}$ for all $n$, and $\bigcup_{n=1}^\infty C_n = A_1 \backslash A$. Hence, by the above proposition 
:::{math}
\lim_{n\rightarrow \infty}\mu (C_n) = \mu (A_1 \backslash A)
:::


We know that the measure $\mu (A_1)$ is finite, and that we have disjoint unions
:::{math}
A_1 = A_n \cup C_n \qquad A_1 = A_1\backslash A \cup A
:::
 Hence 
:::{math}
\mu (A_1 )- \lim_{n\rightarrow \infty} \mu (A_n) = \mu (A_1 ) - \mu (A)
:::
 and 
:::{math}
\lim_{n\rightarrow \infty} \mu (A_n ) = \mu (A)
:::
:::


The above corollary is false if we omit the assumption that $\mu (A_1) < \infty$.
<!-- XXSEC_PREFIX_ENDXX\sectionMeasure Spaces -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXLebesgue integrationXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionLebesgue integration -->
(sec:lebesgue-integration_1)=
# Lebesgue integration
<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXSimple FunctionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Simple Functions -->
## Simple Functions
:::{prf:definition} 
A function $s\colon \Omega \rightarrow {\mathbb C}$ on a measurable space $\Omega$ is called \em simple if the range of $s$ is a finite set of points.
:::


Let $s\colon \Omega \rightarrow {\mathbb C}$ be a simple function, with image $s[X] = \{ 0 \} \cup \{ \alpha_1 , \ldots , \alpha_n \}$. Write $A_i = s^{-1}(\alpha_i )$. Then clearly 
:::{math}
s = \sum_{i=1}^n \alpha_i \chi_{A_i}
:::
 and the function $s$ is measurable if and only if each set $A_i$ is measurable.


:::{prf:proposition} 
:label: simpapp_1
Let $f\colon \Omega \rightarrow [0,\infty ]$ be a measurable function. Then there are simple measurable functions $s_n \colon X\rightarrow [0,\infty )$ such that the sequence $(s_n (x))$ is monotonically increasing, with limit $f(x)$ for each point $x\in X$.
:::



:::{prf:proof}

Let $n\in {\mathbb N}$, and $t\in [0,\infty ]$. Then there is a unique integer $k_n (t)$ such that 
:::{math}
k_n (T) 2^{-n} \leq t \leq (k_n (t) +1)2^{-n}
:::


Define 
:::{math}
\varphi_n (t) = \left\{ \begin{array}{ll}
k_n (t)2^{-n} & 0\leq t < n \\ n & n\leq t\leq \infty \\
\end{array} \right.
:::


The function $\varphi_n \colon [0,\infty ]\rightarrow [0,\infty ]$ is a Borel function, and 
:::{math}
t-2^{-n} \leq \varphi_n (t) \leq t
:::
 if $0\leq t\leq n$. Thus we have a monotonically increasing sequence $(\varphi_n (t))$ with limit $t$. If we write $s_n = \varphi_n \circ f$, then $(s_n)$ is a monotonically increasing sequence of simple measurable functions, with pointwise limit $f$ as required.
:::


We now come to the first of our definitions of the integral.


:::{prf:definition} 
Let $\Omega$ be a measure space, with measure $\mu$. Let $s\colon \Omega \rightarrow {\mathbb C}$ be a measurable simple function, with set of non-zero values $\{ \alpha_1 ,\ldots , \alpha_n \}$. Write 
:::{math}
s = \sum_{k=1}^n \alpha_k \chi_{A_k}
:::


Let $E\subseteq \Omega$ be a measurable subset of $\Omega$. Then we define the \em integral of $s$ over $E$ to be the complex number 
:::{math}
\int_E s\ d\mu = \sum_{k=1}^n \alpha_k \mu (A_k \cap E )
:::
:::


There are several simple computations we can do immediately with integrals. For example, with $s$ as above: 
:::{math}
\int_\Omega s\chi_E \ d\mu = \sum_{k=1}^\infty \alpha_k \mu (A_k \cap E) = \int_E s\ d\mu
:::



:::{prf:lemma} 
:label: stepmeasure_1
Let $\Omega$ be a measure space, with measure $\mu$. Let $s\colon \Omega \rightarrow [0,\infty )$ be a measurable simple function. Then we can define a new measure $\varphi$ on $\Omega$ by the formula 
:::{math}
\varphi (E) = \int_E s\ d\mu
:::
:::



:::{prf:proof}

To begin with, observe that $\varphi (E)\geq 0$ for every measurable set $E$, and that if $\mu (E) < \infty$, then $\varphi (E) < \infty$, so there is at least one measurable set with finite measure. We need to test $\sigma$-additivity.

Let $(E_n)$ be a sequence of disjoint measurable sets. We know that 
:::{math}
\mu (\bigcup_{i=1}^\infty E_i ) = \sum_{i=1}^\infty \mu (E_i)
:::


Let $\{ \alpha_1 , \ldots , \alpha_k \}$ be the set of non-zero values of the simple function $s$. Then 
:::{math}
\varphi (\bigcup_{i=1}^\infty E_i ) = \sum_{k=1}^n \sum_{i=1}^\infty \alpha_k \mu (A_k \cap E_i )
:::


Exchanging the summation signs is possible since all of the numbers involved in the above equation are positive. Therefore 
:::{math}
\varphi (\bigcup_{i=1}^\infty E_i ) = \sum_{i=1}^\infty \sum_{k=1}^n \alpha_k \mu (A_k \cap E_i ) = \sum_{i=1}^\infty \varphi (E_i)
:::
 and we are done.
:::



:::{prf:proposition} 
:label: simpsum_1
Let $s,t\colon \Omega \rightarrow [0,\infty ]$ be simple functions. Then 
:::{math}
\int_\Omega s+t\ d\mu = \int_\Omega s\ d\mu + \int_\Omega t\ d\mu
:::
:::



:::{prf:proof}

Write as usual 
:::{math}
s = \sum_{i=1}^m \alpha_k \chi_{A_i} \qquad t = \sum_{j=1}^n \beta_j \chi_{B_j}
:::


Let $E_{ij} = A_i \cap B_j$. Then certainly 
:::{math}
int_{E_{ij}} (s+t)\ d\mu = (\alpha_i +\beta_j)\mu (E_{ij}) = \int_{E_{ij}}s\ d\mu + \int_{E_{ij}}t\ d\mu
:::


Now the sets $\{ 0, \alpha_1 , \ldots , \alpha_m \}$ and $\{ 0, \beta_1 , \ldots ,\beta_n \}$ are the ranges of the functions $s$ and $t$ respectively. Let $A_0 = s^{-1}[0]$ and $B_0 = t^{-1}[0]$. Then 
:::{math}
\Omega = \bigcup_{i=0}^m A_i = \bigcup_{j=0}^n B_j
:::


Hence 
:::{math}
\Omega = \bigcup_{i,j=0}^{m,n}E_{ij}
:::


The sets $E_{ij}$ are certainly disjoint. Hence by the above lemma, we know that 
:::{math}
\int_\Omega s+t \ d\mu = int_\Omega s\ d\mu + \int_\Omega t\ d\mu
:::
 and we are done.
:::


If $s$ is a step function, and $\alpha \in {\mathbb C}$, then clearly 
:::{math}
\int_\Omega \alpha s\ d\mu = \alpha \int_\Omega s\ d\mu
:::


Hence we have proven linearity for integrals of positive-valued step functions.
<!-- XXSEC_PREFIX_ENDXX\subsection*Simple Functions -->

<!-- XXSEC_PREFIX_ENDXX\sectionLebesgue integration -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXIntegration of Positive-Valued FunctionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionIntegration of Positive-Valued Functions -->
# Integration of Positive-Valued Functions
:::{prf:definition} 
Let $\Omega$ be a measure space, with measure $\mu$. Let $f\colon \Omega \rightarrow [0,\infty ]$ be a measurable function, and let $E\subseteq \Omega$ be a measurable set. Let $S$ be the set of simple functions, $s\colon \Omega \rightarrow [0,\infty )$, such that $s(x) \leq f(x)$ for all $x\in \Omega$. Then we define the \em integral of $f$ over $E$: 
:::{math}
\int_E f\ d\mu = \sup \{ \int_E s\ d\mu \ |\ s\in S \}
:::
:::


A few properties of the integral are easy to prove. For example:



Let $f\colon \Omega \rightarrow [0,\infty ]$ and $E\subseteq \Omega$ be measurable. Then
   :::{math}
   \int_\Omega f\ d\mu = \int_\Omega f\chi_E\ d\mu
   :::

Let $f,g\colon \Omega \rightarrow [0,\infty ]$ be measurable functions such that $f\leq g$, that is to say $f(x)\leq g(x)$ for all $x\in \Omega$. Then
   :::{math}
   \int_E f \leq \int_E g
   :::
   whenever $E\subseteq \Omega$ is a measurable subset.



:::{prf:theorem} The Monotone Convergence Theorem
Let $f_n\colon \Omega \rightarrow [0,\infty ]$ be a sequence of measurable functions, such that for each point $x\in \Omega$ the sequence $(f_n (x))$ is monotonically increasing, with limit $f(x)$. Then the function $f\colon \Omega \rightarrow [0,\infty ]$ is measurable, and 
:::{math}
\int_\Omega f\ d\mu = \lim_{n\rightarrow \infty} \int_\Omega f_n \ d\mu
:::
:::



:::{prf:proof}

As the limit of a sequence of measurable functions, the function $f$ is measurable. Since the seqyebce $(f_n (x))$ is monotonic increasing, with limit $f(x)$, we know that $F_n \leq f_{n+1} \leq f$ for all $n$. Therefore the sequence of integrals $\left( \int_\Omega f_n \right)$ is monotonic increasing, and 
:::{math}
\int_\Omega f_n \ d\mu \leq \int_\Omega f \ d\mu
:::
 for all $n$.

Choose a simple function $s$ such that $0\leq s\leq f$. Let $0 < \alpha < 1$, and write 
:::{math}
E_n = \{ x\in \Omega \ |\ f_n (x) \geq \alpha s(x) \}
:::


Each set $E_n$ is measurable, and $E_n \subseteq E_{n+1}$ for all $n$ since the sequence $(f_n)$ is monotonic increasing. Since the sequence $(f_n)$ has pointwise limit $f$, we see that 
:::{math}
\Omega = \bigcup_{n=1}^\infty E_n
:::


Further 
:::{math}
\int_\Omega f_n\ d\mu \geq \int_{E_n} f_n \ d\mu \geq \alpha \int_{E_n}s\ d\mu \qquad (\ast )
:::


By lemma {prf:ref}`stepmeasure_1` we can define a measure on the set $\Omega$ by the formula 
:::{math}
\varphi (E) = \int_E s\ d\mu
:::
 Hence 
:::{math}
\int_\Omega s\ d\mu = \varphi (\Omega ) = \lim_{n\rightarrow \infty} \varphi (E_n ) = \lim_{n\rightarrow \infty} \int_{E_n}s\ d\mu
:::
 by proposition {prf:ref}`limsub_1`.

Taking limits in inequality $(\ast )$, we see that 
:::{math}
\lim_{n\rightarrow \infty } \int_\Omega f_n \ d\mu \geq \alpha \int_\Omega s\ d\mu
:::


In particular, this inequality holds whenever $0 < \alpha < 1$ and $s\leq f$. By the definition of the integral, it follows that 
:::{math}
\lim_{n\rightarrow \infty}\int_\Omega f_n \ d\mu \geq \int_\Omega f \ d\mu
:::
 and we are done.
:::


Let $f\colon \Omega \rightarrow [0,\infty ]$ be a measurable function. By proposition {prf:ref}`simpapp_1`, there is a monotonically increasing sequence of simple functions $s\colon \Omega \rightarrow [0,\infty )$ with pointwise limit $f$.

The monotone convergence theorem tells us that 
:::{math}
\int_\Omega f = \lim_{n\rightarrow \infty} \int_\Omega s_n
:::
 and so gives us a new way of viewing the definition of the integral. Using this viewpoint, the following result follows immediately from proposition {prf:ref}`simpsum_1`


:::{prf:corollary} 
Let $f,g\colon \Omega \rightarrow [0,\infty ]$ be measurable functions, and let $\alpha, \beta \in [0, \infty )$. Then 
:::{math}
\int_\Omega (\alpha f+ \beta g)\ d\mu = \alpha \int_\Omega f\ d\mu + \beta \int_\Omega g\ d\mu
:::

**proof to be filled in!**
:::


We can also immediately deduce the following result from the monotone convergence theorem.


:::{prf:corollary} 
Consider a sequence of measurable functions $f_n \colon \Omega \rightarrow [0,\infty ]$. Then for any measurable subset $E\subseteq \Omega$ we have the formula
:::{math}
\sum_{n=1}^\infty \int_E f_n\ d\mu = \int_E \left( \sum_{n=1}^\infty f_n \right) \ d\mu
:::

**proof to be filled in!**
:::



:::{prf:theorem} Fatou's lemma
Let $f_n \colon \Omega \rightarrow [0,\infty ]$ be a sequence of measurable functions. Then 
:::{math}
\int_\Omega {\lim \inf}_{n\rightarrow \infty} f_n \leq {\lim \inf}_{n\rightarrow \infty} \int_\Omega f_n
:::
:::



:::{prf:proof}

Let 
:::{math}
g_n (x) = \inf \{ f_n (x) , f_{n+1} (x) , f_{n+2} (x) , \ldots \}
:::


Then the function $g_n$ is measurable, the sequence $(g_n)$ is monotonic increasing, and the inequality $g_n \leq f_n$ holds for all $n$.

We know that 
:::{math}
\lim_{n\rightarrow \infty} g_n (x) = {\lim \inf}_{n\rightarrow \infty} f_n (x)
:::


Hence, by the monotone convergence theorem 
:::{math}
\int_\Omega {\lim \inf}_{n\rightarrow \infty} f_n = \lim_{n\rightarrow \infty} \int_\Omega g_n \leq {\lim \inf}_{n\rightarrow \infty} \int_\Omega f_n
:::
 and we are done.
:::


The inequality 
:::{math}
\int_\Omega {\lim \sup}_{n\rightarrow \infty} f_n \geq {\lim \sup}_{n\rightarrow \infty} \int_\Omega f_n
:::
 is easily deduced from Fatou's lemma.
<!-- XXSEC_PREFIX_ENDXX\sectionIntegration of Positive-Valued Functions -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXIntegration of Complex-Valued FunctionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionIntegration of Complex-Valued Functions -->
# Integration of Complex-Valued Functions
:::{prf:definition} 
Let $\Omega$ be a measure space, with measure $\mu$. We call a measurable function $f\colon \Omega \rightarrow {\mathbb C}$ \em integrable if 
:::{math}
\int_\Omega |f|\ d\mu < \infty
:::


We write $L^1 (\Omega )$ to denote the set of all integrable functions.
:::


Suppose we have a measurable function $f$ and a positive-valued integrable function $g$ such that $|f|\leq g$. Then it follows by the above definition that the function $f$ is integrable. This integrability criterion is often used.


:::{prf:definition} 
Let $f\colon \Omega \rightarrow {\mathbb R}$ be any real-valued function. Then we define functions $f^+ , f^- \colon \Omega \rightarrow [0, \infty )$ by the formulae 
:::{math}
f^+ (x) = \max (f(x), 0)) \qquad f^- (x) = \max (-f(x) , 0)
:::
 respectively.
:::


Observe that $f = f^+ - f^-$. If the function $f$ is measurable, then so are the functions $f^+$ and $f^-$.


:::{prf:proposition} 
Let $f\colon \Omega \rightarrow {\mathbb R}$ be an integrable function. Then the functions $f^+$ and $f^-$ are also integrable.
:::



:::{prf:proof}

The functions $f^+$ and $|f|$ are positive-valued, and $f^+ \leq |f|$. We know that $\int_\Omega |f| < \infty$, so $\int_\Omega f^+ < \infty$.

The proof that the function $f^-$ is integrable is identical to the above.
:::



:::{prf:definition} 
Let $f\colon \Omega \rightarrow {\mathbb R}$ be an integrable function. Then we define we define the integral 
:::{math}
\int_\Omega f\ d\mu := \int_\Omega f^+\ d\mu - \int_\Omega f^-\ d\mu
:::
:::


It is easy to see that definition agrees with the previous definition when the function $f$ is positive-valued. Further, the equation 
:::{math}
\int_\Omega (\alpha f + \beta g)\ d\mu = \alpha \int_\Omega f \ d\mu + \beta \int_\Omega g\ d\mu
:::
 holds for all real numbers $\alpha , \beta \in {\mathbb R}$ and integrable functions $f,g\colon \Omega \rightarrow {\mathbb R}$.


:::{prf:definition} 
Let $f,g\colon \Omega \rightarrow {\mathbb C}$ be integrable functions. Then we define the integral 
:::{math}
\int_\Omega f\ d\mu := \int_\Omega \Re (f)\ d\mu +i \int_\Omega \Im (f)\ d\mu
:::
:::


An argument similar to that made above tells us that this integral is well-defined, agrees with the previous definition for real-valued functions, and is linear.


:::{prf:proposition} 
:label: posineq_1
Let $f\colon \Omega \rightarrow {\mathbb C}$ be an integrable function. Then 
:::{math}
\left| \inf_\Omega f\ d\mu \right| \leq \int_\Omega |f|\ d\mu
:::
:::



:::{prf:proof}

Choose $\alpha \in {\mathbb C}$ such that $|\alpha |=1$ and 
:::{math}
\left| \inf_\Omega f\ d\mu \right| = \alpha \int_\Omega f\ d\mu = \int_\Omega \alpha f\ d\mu
:::


Let $g = \Re (\alpha f )$ and $h= \Im (\alpha f)$. Then 
:::{math}
\left| \inf_\Omega f\ d\mu \right| = \int_\Omega g\ d\mu + i \int_\Omega h\ d\mu
:::


Certainly, $\left| \inf_\Omega f\ d\mu \right| \in {\mathbb R}$, so 
:::{math}
\int_\Omega h\ d\mu
:::
 and 
:::{math}
\left| \inf_\Omega f\ d\mu \right| = \int_\Omega g\ d\mu
:::


However 
:::{math}
g\leq |g| \leq |\alpha f| = |f|
:::
 It follows that 
:::{math}
\left| \inf_\Omega f\ d\mu \right| \leq \int_\Omega |f|\ d\mu
:::
 and we are done.
:::


Observe that the proof of the above result uses only positivity and linearity of the integral.


:::{prf:theorem} The Dominated Convergence Theorem
Let $(f_n)$ be a sequence of measurable functions $f_n \colon \Omega \rightarrow {\mathbb C}$ such that:



The limit
   :::{math}
   f(x) = \lim_{n\rightarrow \infty} f_n (x)
   :::
   exists for all $x\in \Omega$.

There is an integrable function $g\in L^1 (\Omega )$ such that $|f_n (x)|\leq g(x)$ for all $x\in \Omega$ and $n\in {\mathbb N}$.


Then $f\in L^1 (\Omega )$, and 
:::{math}
\lim_{n\rightarrow \infty} \int_\Omega |f_n - f|\ d\mu =0
:::
:::



:::{prf:proof}

Since each fucntion $f_n$ is measurable, the limit function $f$ is also measurable. We know that $|f_n|\leq g$ for all $n$. Therefore $|f|\leq g$. It follows that $f\in L^1 (\Omega )$.

Now, let 
:::{math}
h_n = 2g - |f_n -f |
:::


Observe that $h_n \geq 0$ for all $n$. Hence by Fatou's lemma 
:::{math}
\int_\Omega {\lim \inf}_{n\rightarrow \infty} h_n \leq {\lim \inf}_{n\rightarrow \infty} \int_\Omega h_n
:::
 that is 
:::{math}
\int_\Omega 2g\ d\mu \leq \int_\Omega 2g\ d\mu - {\lim \inf}_{n\rightarrow \infty} \int_\Omega |f_n -f| \ d\mu
:::
 and so 
:::{math}
{\lim \inf}_{n\rightarrow \infty} \int_\Omega |f_n -f| \ d\mu \leq 0
:::


Since $|f_n -f | \geq 0$ for all $n$, we deduce that 
:::{math}
\lim_{n\rightarrow \infty} \int_\Omega |f_n - f|\ d\mu =0
:::
 as required.
:::


Combining the dominated convergence theorem with proposition {prf:ref}`posineq_1` we obtain the following corollary, also referred to as the dominated convergence theorem.


:::{prf:corollary} The Dominated Convergence Theorem
Let $(f_n)$ be a sequence of measurable functions $f_n \colon \Omega \rightarrow {\mathbb C}$ such that:



The limit
   :::{math}
   f(x) = \lim_{n\rightarrow \infty} f_n (x)
   :::
   exists for all $x\in \Omega$.

There is an integrable function $g\in L^1 (\Omega )$ such that $|f_n (x)|\leq g(x)$ for all $x\in \Omega$ and $n\in {\mathbb N}$.


Then $f\in L^1 (\Omega )$, and 
:::{math}
\lim_{n\rightarrow \infty} \int_\Omega f_n \ d\mu = \int_\Omega f\ d\mu
:::

**proof to be filled in!**
:::

<!-- XXSEC_PREFIX_ENDXX\sectionIntegration of Complex-Valued Functions -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXNull SetsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionNull Sets -->
# Null Sets
:::{prf:definition} 
Let $\Omega$ be a measure space, with measure $\mu$. Then a set $E\subseteq \Omega$ is called a \em null set if $E$ is measurable, and $\mu (E) =0$.

The measure space $\Omega$ is called \em complete if every subspace of a null set is measurable.
:::


The usual manipulations of the axioms tell us that every measure space is contained in a unique smallest complete measure space. To be more precise, we have the following result.


:::{prf:proposition} 
Let $\Omega$ be a measure space, equipped with $\sigma$-algbebra $\mathcal M$, and measure $\mu$. Let us define 
:::{math}
{\mathcal M}^\star := \{ E\subseteq \Omega \ |\ A\subseteq E\subseteq B,\, A,B\in \Omega ,\, \mu (B\backslash A) = 0 \}
:::


Then the set ${\mathcal M}^\star$ is a $\sigma$-algebra. We can define a measure $\mu^\star$ on the set ${\mathcal M}^\star$ by writing 
:::{math}
\mu^\star (E) = \mu (A) \qquad A\subseteq E\subseteq B,\ A,B\in \Omega ,\ \mu (B\backslash A) =0
:::

**proof to be filled in!**
:::


As we might expect from the terminology, null sets are irrelevant from the point of view of integration theory.


:::{prf:theorem} 
Let $f\colon \Omega \rightarrow [0,\infty ]$ be a measurable function. Then the integral of $f$ is zero if and only if the function $f$ is equal to zero except on a null set.
:::



:::{prf:proof}

Suppose that the set 
:::{math}
N = \{ x\in \Omega \ |\ f(x)\neq 0 \}
:::
 is a null set. Let $s\colon \Omega \rightarrow [0,\infty ]$ be a simple function such that $s\leq f$. Then $s(x)=0$ when $x\not\in N$. The definition of the integral of a simple function tells us that 
:::{math}
\int_\Omega s \ d\mu =0
:::


The definition of the integral of a non-negative function now implies that 
:::{math}
\int_\Omega f\ d\mu =0
:::


Conversely, suppose that the integral of the function $f$ is zero. Let 
:::{math}
A_n = \{ x\in \Omega \ |\ f(x) > 1/n \}
:::


Then clearly 
:::{math}
\frac{1}{n} \mu (A_n ) \leq \int_{A_n} f\ d\mu \leq \int_\Omega f d\mu =0
:::
 so $\mu (A_n ) =0$. But 
:::{math}
\{ x\in \Omega \ |\ f(x) > 0 \} = \bigcup_{n=1}^\infty A_n
:::


Thus $\sigma$-additivity implies that the set of all points $x\in \Omega$ such that $f(x)\neq 0$ has measure zero.
:::


Given two functions $f,g\colon \Omega \rightarrow {\mathbb C}$, let us say that $f$ and $g$ are equal \em almost everywhere if they are equal outside of some set of measure zero.


:::{prf:corollary} 
Let $f,g\colon \Omega \rightarrow {\mathbb C}$ be integrable functions that are equal almost everywhere. Then 
:::{math}
\int_\Omega f = \int_\Omega g
:::

**proof to be filled in!**
:::



:::{prf:corollary} 
Let $f\colon \Omega \rightarrow {\mathbb C}$ be an integrable function. Suppose that 
:::{math}
\int_E f =0
:::
 whenever the subset $E\subseteq \Omega$ is measurable. Then the function $f$ is equal to zero almost everywhere.
:::



:::{prf:proof}

Let us write 
:::{math}
f(x) = u(x) + iv(x) = (u^+(x)- u^- (x)) + i(v^+(x) - v^-(x))
:::
 where the functions $u$ and $v$ are real and integrable, and the functions $u^\pm$ and $v^\pm$ are integrable and non-negative.

Let 
:::{math}
E = \{ x\in \Omega \ |\ u(x)\geq 0 \}
:::
 Then 
:::{math}
\Re \left( \int_E f \right) = \int_E u^+ =0
:::


By the above theorem, it follows that $u^+ =0$ except on a null set. Similarly, it follows that $u^- =0$ except on a null set. Since the union of two null sets is also a null set, we have shown that $u=0$ almost everywhere.

A similar argument tells us that $v=0$ almost everywhere. We conclude that $f=0$ almost everywhere.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionNull Sets -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe Riesz Representation TheoremXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe Riesz Representation Theorem -->
# The Riesz Representation Theorem
Before we are ready to state the Riesz representation theorem, we need some terminology from point-set topology.


:::{prf:definition} 
Let $X$ be a topological space. Then we define the \em support of a continuous function $f\colon X\rightarrow {\mathbb C}$ to be the closure 
:::{math}
\operatorname{supp} (f):= \overline{ \{ x\in X \ |\ f(x)\neq 0 \} }
:::
:::


We write $C_c (X)$ to denote the set of all continuous compactly supported functions $f\colon X\rightarrow {\mathbb C}$. The set $C_c (X)$ is a vector space under the operations of pointwise addition and scalar multiplication.


:::{prf:definition} 
A linear map $\Lambda \colon C_c (X) \rightarrow {\mathbb C}$ is said to be a \em positive functional if $\Lambda (f) \geq 0$ whenever $f\geq 0$.
:::


Let $X$ be a topological space equipped with a Borel measure $\mu$ such that $\mu (K) < \infty$ whenever $K\subseteq X$ is a compact subspace. Then the integration map 
:::{math}
f\mapsto \int_X f
:::
 defines a positive linear functional.

The Riesz representation theorem is essentially a converse of the above observation.


:::{prf:theorem} 
Let $X$ be a locally compact Hausdorff space, and let $\Lambda \colon C_c (X) \rightarrow {\mathbb C}$ be a positive linear functional.

Then the set $X$ has a $\sigma$-algebra $\Omega$ containing all Borel sets, and a unique measure $\mu$ on $\Omega$ such that 
:::{math}
\Lambda (f) = \int_X f\ d\mu
:::
 whenever $f\in C_c (X)$.
:::


The proof of this theorem is in a series of lemmas; the proof is quite long. Before we begin the proof, let us note a theorem from general topology which we shall need.


:::{prf:theorem} 
:label: partition_1
Let $X$ be a locally compact Hausdorff space, and let ${\mathcal U} = \{ U_\alpha \ |\ \alpha \in A \}$ be an open cover of the space $X$. Then there is a \em partition of unity subordinate to the cover $\mathcal U$, that is to say a set of continuous functions $u_\alpha \colon X\rightarrow [0,1]$ such that $\operatorname{supp} u_\alpha \subseteq U_\alpha$ and 
:::{math}
\sum_{\alpha \in A} u_\alpha (x) =1
:::
 whenever $x\in X$.
**proof to be filled in!**
:::


The following corollary is known as \em Urysohn's lemma.


:::{prf:corollary} 
Let $X$ be a locally compact Hausdorff space, and let $K\subseteq X$ be a compact set, and let $U$ be an open set containing $K$. Then there is a continuous function $f\colon X\rightarrow [0,1]$ such that 
:::{math}
\chi_K(x) \leq f(x) \leq \chi_U (x)
:::
:::



:::{prf:proof}

The collection $\{ U, X\backslash K \}$ is an open cover of the space $X$. There is therefore a partition of unity $\{ f,g\}$ subordinate to this open cover.

The definition of a partition of unity gives us the required inequality for the function $f$.
:::


We now begin our proof of the Riesz representation theorem with the definition of the measure we are looking for.


:::{prf:definition} 
Let $\Lambda \colon C_c (X) \rightarrow {\mathbb C}$ be a positive linear functional. Let $U\subseteq X$ be open. Then we define 
:::{math}
\mu (U):= \sup \{ \Lambda f \ |\ f\leq \chi_U \}
:::


In general, for a subset, $E\subset X$, we define 
:::{math}
\mu (E) = \inf \{ \{ \mu (U) \ |\ U \textrm{ open }, E\subseteq U \}
:::
:::



:::{prf:proposition} 
Let $f,g\in C_c (X)$, and let $f\leq g$. Then $\Lambda f \leq \Lambda g$.
:::



:::{prf:proof}

Observe $g-f \geq 0$. The result follows from positivity and linearity of the function $\Lambda$.
:::



:::{prf:corollary} 
Let $A$ and $B$ be subsets of the space $X$ where $A\subseteq B$. Then $\mu (A)\leq \mu (B)$.
**proof to be filled in!**
:::


Although we have defined a function $\mu$ for every subset of $E$, the definition is only sensible for a certain $\sigma$-algebra.


:::{prf:definition} 
We define $\Omega_F$ to be the sollection of all subsets $E\subseteq X$ such that $\mu (E) < \infty$ and 
:::{math}
\mu (E) = \sup \{ \mu (K) \ |\ K\subseteq E, K \textrm{ compact} \}
:::


We define $\Omega$ to be the collection of all subsets $E\subseteq X$ such that $E\cap K \in \Omega_F$ whenever $K$ is compact.
:::


We need to prove that the set $\Omega$ is a $\sigma$-algebra which contains all Borel sets; this statement is not obvious.


:::{prf:proposition} 
:label: lem3_1
Let $V\subseteq X$ be an open subset such that $\mu (V) < \infty$. Then $V\in \Omega_F$.
:::



:::{prf:proof}

Choose a number $a < \mu (V)$. By the definition of $\mu$, there is a function $f\in C_c (X)$ such that $f\leq \chi_V$ and $a < \Lambda f$. Write $K=\operatorname{supp} (f)$, and let $W$ be an open set that contains $K$. Then $\Lambda f \leq \mu (W)$, so $\Lambda f \leq \mu (K)$, using the above proposition and corollary, and the definition of the function $\mu$.

Thus $K\subseteq V$ and $\mu (K) > a$. It follows that 
:::{math}
\mu (V) = \sup \{ \mu (K) \ |\ K\subseteq E, K \textrm{ compact} \}
:::
 and we are done.
:::



:::{prf:proposition} 
Let $U_1 , \ldots , U_N\subseteq X$ be open sets. Then $\mu (U_1\cup \cdots \cup U_N) \leq \mu (U_1)+ \cdots +\mu (U_N)$.
:::



:::{prf:proof}

Let $N=2$. Choose a function $g\in C_c (X)$ such that $g\leq \chi_{U_1\cup U_2}$. By theorem {prf:ref}`partition_1` there are functions $u_1 , u_2\in C_c (X)$ such that $u_1\leq \chi_{U_1}$, $u_2\leq \chi_{u_2}$, and $u_1(x) + u_2 (x) =1$ whenever $x\in U_1\cup U_2$. It follows that 
:::{math}
u_1 g\leq \chi_{U_1},\ u_2g \leq \chi_{U_2} \qquad g=u_1 g + u_2 g
:::
 and therefore 
:::{math}
\Lambda g = \Lambda (u_1 g) +\Lambda (u_2 g) \leq \mu (U_1) + \mu (U_2)
:::


Since the above inequality holds for every function $g\in C_c (X)$ such that $g\leq \chi_{U_1\cup U_2}$, the result follows from the definition of $\mu$ when $N=2$. The general result follows by induction.
:::



:::{prf:lemma} 
:label: lem1_1
Let $E_1,E_2,E_3,\ldots$ be subsets of the space $X$. Write 
:::{math}
E = \bigcup_{n=1}^\infty E_n
:::


Then 
:::{math}
\mu (E) \leq \sum_{n=1}^\infty \mu (E_n)
:::
:::



:::{prf:proof}

If $\mu (E_n )=\infty$ for some $n$, then the result is obviously true. Thus, let us suppose that $\mu (E_n) < \infty$ for all $n$. Choose $\varepsilon > 0$. By definition of the function $\mu$, there are open sets $U_n \supseteq V_n$ such that 
:::{math}
\mu (V_n) < \mu (E_n) +2^{-n} \varepsilon
:::
 for all $n$.

Let $U = \bigcup_{n=1}^\infty U$, and choose $f\in C_c (X)$ such that $f\leq \chi_U$. The support of the function $f$ is covered by the collection of sets $\{ U_n \ |\ n=1,2,3,\ldots \}$. Since the function $f$ has compact support, it follows that it has a finite subcovering, and so 
:::{math}
f\leq \chi_{U_1 \cup \cdots \cup U_N }
:::
 for some $N$. By the above proposition, we see that 
:::{math}
\Lambda f \leq \mu (U_1 \cup \cdots \cup U_N) \leq \mu(V_1 ) + \cdots + \mu (V_N) \leq \sum_{n=1}^\infty \mu (E_n) + \varepsilon
:::


Since the above inueqality holds for every funtion $f\subseteq \chi_U$, and $E\subseteq U$, we see that 
:::{math}
\mu (E) \leq \sum_{n=1}^\infty \mu (E_n) +\varepsilon
:::


But this inequality holds whenever $\varepsilon > 0$, so the result follows.
:::



:::{prf:proposition} 
Let $K\subseteq X$ be compact. Then $\mu (K)\leq \Lambda f$ whenever $f\geq \chi_K$, and $K\in \Omega_F$.
:::



:::{prf:proof}

Let $0 < a < 1$, and choose $f\in C_c (X)$ such that $f\geq \chi_K$. Write 
:::{math}
V_a = \{ x\in X \ |\ f(x) > a \}
:::


Then $K\subseteq V_a$, and $ag\leq f$ whenever $f\leq \chi_{V_a}$. Therefore 
:::{math}
\mu (K) \leq \mu (V_a ) = \sup \{ \Lambda g \ |\ g\leq \chi_{V_a} \} \leq a^{-1}\Lambda f
:::


Since this inequaltity holds whenever $0 < a < 1$, it follows that $\mu (K)\leq \Lambda f$. It follows that $\mu (K) < \infty$, and so $K\in \Omega_F$.
:::



:::{prf:lemma} 
:label: lem2_1
Let $K\subseteq X$ be compact. Then 
:::{math}
\mu (K) =\inf \{ \Lambda f \ |\ \chi_K \leq f \}
:::
:::



:::{prf:proof}

Let $\varepsilon > 0$. Then there is an open set $U\supseteq K$ such that $\mu (U) < \mu (K) +\varepsilon$. By Urysohn's lemma there is a continuous function $f\colon [0,1]\rightarrow X$ such that $\chi_K \leq f \leq \chi_U$. It follows that 
:::{math}
\Lambda f\leq \mu(U) < \mu (K) +\varepsilon
:::


The result follows from the above inequality combined with the previous proposition.
:::



:::{prf:proposition} 
Let $K_1,\ldots K_N$ be disjoint compact sets. Then 
:::{math}
\mu (K_1 \cup \cdots \cup K_N) \leq \mu (K_1 ) + \cdots + \mu (K_N)
:::
:::



:::{prf:proof}

Let $N=2$. We can find an open set $U$ such that $U\supseteq K_1$ and $U\cap K_2 = \emptyset$. It follows by Urysohn's lemma that we can find a compactly supported function $u\colon X\rightarrow [0,1]$ such that $u(x)=1$ whenever $x\in K_1$, and $u(x) =0$ whenever $x\in K_2$.

Let $\varepsilon > 0$. By lemma {prf:ref}`lem2_1` there is a function $g\in C_c (X)$ such that 
:::{math}
\chi_{K_1 \cup K_2}\leq g \qquad \Lambda g \leq \mu (K_1 + K_2) +\varepsilon
:::


Observe that 
:::{math}
\chi_{K_1} \leq fg \qquad \chi_{K_2} \leq (1-f)g
:::


Hence 
:::{math}
\mu (K_1 ) + \mu (K_2) \leq \Lambda (fg) + \Lambda (g-fg) \leq \mu (K_1 \cup K_2 ) + \varepsilon
:::


Since the above inequality holds whenever $\varepsilon > 0$, the desired result follows when $N=2$. The general result follows by induction.
:::



:::{prf:lemma} 
:label: lem4_1
Let $E_1,E_2,E_3,\ldots$ be pairwise disjoint members of the collection $\Omega_F$. Write 
:::{math}
E = \bigcup_{n=1}^\infty E_n
:::


Then 
:::{math}
\mu (E) = \sum_{n=1}^\infty \mu (E_n)
:::


Further, if $\mu (E) < \infty$, then $E\in \Omega_F$.
:::



:::{prf:proof}

Observe that the result follows from lemma {prf:ref}`lem1_1` when $\mu (E)=\infty$. Let us therefore assume that $\mu (E) < \infty$. Choose $\varepsilon > 0$. Since $E_n\in \Omega_F$, we can find a compact set $K_n \subseteq E_n$ such that 
:::{math}
\mu (K_n ) > \mu (E_n ) - 2^{-n} \varepsilon
:::
 for each $n$. Let $H_N = K_1 \cup \cdots \cup K_N$. Then by the above propositiion: 
:::{math}
\mu E) \geq \mu (H_N) = \sum_{n=1}^N \mu (K_n) > \sum_{n=1}^N \mu (E_n) - \varepsilon
:::


Since the above inequality holds whenever $\varepsilon > 0$, combining it with the inequality in lemma {prf:ref}`lem1_1`, we see that 
:::{math}
\mu (E) = \sum_{n=1}^\infty \mu (E_n)
:::


Now, if $\mu (E) < \infty$, and $\varepsilon > 0$, then we can find $N$ such that 
:::{math}
\mu (E) \leq \sum_{n=1}^N \mu (E_n) + \varepsilon
:::


It follows that $\mu (E)\leq \mu (H_N) +2\varepsilon$, and so $E\in \Omega_F$.
:::



:::{prf:proposition} 
:label: lem5_1
Let $E\subseteq \Omega_F$, and let $\varepsilon > 0$. Then there is a compact set $K$ and an open set $V$ such that $K\subseteq E\subseteq V$, and $\mu (V\backslash K) < \varepsilon$.
:::



:::{prf:proof}

by definition of the collection $\Omega_F$, we can find a compact set $K\subseteq E$ and an open set $U\supseteq E$ such that 
:::{math}
\mu (V) - \frac{\varepsilon}{2} < \mu (E) < \mu(K) + \frac{\varepsilon}{2}
:::


By lemma {prf:ref}`lem3_1`, we see that $V\backslash K \in \Omega_F$. By lemma {prf:ref}`lem4_1`, we see 
:::{math}
\mu (K) + \mu (U\backslash K) = \mu (U) < \mu (K) +\varepsilon
:::
 and we are done.
:::



:::{prf:proposition} 
Let $A,B\in \Omega_F$. Then the sets $A\backslash B$, $A\cup B$, and $A\cap B$ belong to the collection $\Omega_F$.
:::



:::{prf:proof}

By the above proposition, there are compact sets $K$ and $K'$, and open sets $U$ and $U'$ such that 
:::{math}
K\subseteq A\subseteq U \qquad K'\subseteq B\subseteq U'
:::
 and 
:::{math}
\mu (U\backslash K) < \varepsilon \qquad \mu (U'\backslash K') < \varepsilon
:::


Observe 
:::{math}
A\backslash B \subseteq U\backslash K' \subseteq U\backslash K \cup K\backslash U'\cup U'\backslash K'
:::


Hence by lemme {prf:ref}`lem1_1`: 
:::{math}
\mu (A\backslash B) \subseteq \mu (K\backslash V') +2\varepsilon
:::


Further, the set $K\backslash V'$ is compact, so the above inequality tells us that $A\backslash B \in \Omega_F$.

But $A\cup B = (A\backslash B)\cup B$, so $A\cup B \in \Omega_F$ by lemma {prf:ref}`lem4_1`. Finally, $A\cap B = A\backslash (A\backslash B)$, so $A\cap B\in \Omega_F$ by the above calculation.
:::


We are now nearly done, and can prove a slightly less technical result.


:::{prf:theorem} 
The set $\Omega$ is a $\sigma$-algebra containing all Borel sets.
:::



:::{prf:proof}

Let $K\subseteq X$ be compact. If $A\in \Omega$, then $X\backslash A \cap K = K \backslash (A\cap K)$, so $X\backslash A \cap K\in \Omega_F$ by the above proposition, and $X\backslash A\in \Omega$.

Suppose that 
:::{math}
A = \bigcup_{n=1}^\infty A_n \qquad A_n \in \Omega
:::


Let $B_1 = A_1 \cap K$, and 
:::{math}
B_n = (A_n \cap K) \backslash (B_1 \cup \cdots \cup B_n) \qquad n\geq 2
:::


Then the collection $\{ B_n \ |\ n=1,2,\ldots \}$ is a pairwise disjoint, and $B_n \in \Omega_F$ for all $n$ by the above lemma. But $A\cap K =\bigcup_{n=1}^\infty B_n$, so $A\cap K \in \Omega_F$ by lemma {prf:ref}`lem4_1`. It follows that $A\in \Omega$.

We have proved that the collection $\Omega$ is a $\sigma$-algebra. If $C\subseteq X$ is a closed subset, then the intersection $K\cap C$ is compact. Thus $C\cap K \in \Omega_F$, and so $C\in \Omega$. Thus every closed set belongs to the collection $\Omega$. It follows that the $\sigma$-algebra $\Omega$ contains all Borel sets.
:::



:::{prf:lemma} 
:label: lem8_1

:::{math}
\Omega_F = \{ E\in \Omega \ |\ \mu (E) < \infty \}
:::
:::



:::{prf:proof}

Let $E\in \Omega_F$. Then by lemmas {prf:ref}`lem2_1` and {prf:ref}`lem4_1`, we see $E\cap K \in \Omega_F$ whenever $K\subseteq X$ is compact. Then $E\in \Omega$. By definition of the set $\Omega_F$, $\mu (E) < \infty$.

Conversely, suppose that $E\in \Omega$ and $\mu (E) < \infty$. Let $\varepsilon > 0$. We can certainly find an open set $U\supseteq E$ such that $\mu (E) < \infty$. By propositions {prf:ref}`lem3_1` and {prf:ref}`lem5_1`, there is a compact set $K\subseteq U$ such that $\mu (U\backslash K) < \varepsilon$.

We know that $E\cap K\in \Omega_F$. There is therefore a compact set $H\subseteq E\cap K$ such that 
:::{math}
\mu (E\cap K) < \mu (H) +\varepsilon
:::


But $E\subseteq (E\cap K) \cup (U\backslash K)$. Therefore 
:::{math}
\mu (E)\subseteq \mu (E\cap K) + \mu (V\backslash K) < \mu (H)+\varepsilon
:::
 and we see that $E\in \Omega_F$.
:::


We can now prove our main result.


:::{prf:theorem} 
The function $\mu$ is a measure on the $\sigma$-algebra $\Omega$. It is the unique measure with the property 
:::{math}
\Lambda f = \int_X f(x)\ d\mu (x)
:::
 for all $f\in C_c (X)$.
:::



:::{prf:proof}

It follows immediately that $\mu$ is a measure from lemmas {prf:ref}`lem4_1` and {prf:ref}`lem8_1`. Our next step is to prove the inequality 
:::{math}
\Lambda f \leq \int_X f(x)\ d\mu (x)
:::
 for every real-valued compactly supported function $f$. To do this, let $K = \operatorname{supp} (f)$, and choose $a,b\in {\mathbb R}$ such that $f[K]\subseteq [a,b]$. Let $\varepsilon > 0$, and choose $y_0 ,\ldots ,y_N$ such that 
:::{math}
a=y_0 < \cdots < y_N \qquad y_n - y_{n-1} < \varepsilon \textrm{ for all }n
:::


We can form Borel sets 
:::{math}
E_n := \{ x\in X \ | \ y_{n-1} < f(x) \leq y_n \}
:::


The sets $E_n$ are pairwise disjoint with union $K$. We can find open sets $U_n \supseteq E_n$ such that 
:::{math}
\mu (U_k ) < \mu (E_k ) + \frac{\varepsilon}{n} \qquad f(x) < y_n + \varepsilon
:::
 whenever $x\in U_n$.

By theorem {prf:ref}`partition_1`, we can choose a partition of unity $\{ u_1 , \ldots , u_N \}$ subordinate to the open cover $\{ U_1 ,\ldots , U_N \}$. It follows that 
:::{math}
f = \sum_{n=1}^N u_n f
:::
 and by lemma {prf:ref}`lem2_1`

:::{math}
\mu (K) \leq \Lambda \left( \sum_{n=1}^N u_n \right) = \sum_{n=1}^N \Lambda (u_n)
:::


But by construction $u_nf \leq (y+n + \varepsilon )u_n$, and $y_n - \varepsilon < f(x)$ for all $x\in E_n$, so 
:::{math}
\Lambda f \leq \sum_{n=1}^N (y_k + \varepsilon) \Lambda (u_n) = \sum_{n=1}^N (|a|+ y_k + \varepsilon) \Lambda (u_n) - |a| \sum_{n=1}^N \Lambda (u_n)
:::
 and 
:::{math}
\Lambda f \leq \sum_{n=1}^N (|a|+ y_k + \varepsilon) (\mu (E_n) + \varepsilon /n ) - |a| \mu (K)
:::


Multiplying out, we see that 
:::{math}
\Lambda f \leq \sum_{n=1}^N (y_n - \varepsilon )\mu (E_n) + 2\varepsilon \mu (K) \frac{\varepsilon}{n} \sum_{n=1}^N (|a| + y_n + \varepsilon )
:::
 so by construction of the integral 
:::{math}
\Lambda f \leq \int_X f\ d\mu + \varepsilon (2\mu (K) + |a| +b +\varepsilon )
:::


Since the above inequality must hold for every choice of $\varepsilon > 0$, we see that 
:::{math}
\Lambda f \leq \int_X f(x)\ d\mu (x)
:::
 as required.

Now, if we replace the function $f$ by the function $-f$, we see that 
:::{math}
-\Lambda f \leq -\int_X f(x)\ d\mu (x)
:::


Combining the above two inequalities, we have the equation 
:::{math}
\Lambda f = \int_X f(x)\ d\mu (x)
:::
 for every real-valued compactly supported function $f$. The proof of the above equation for complex-valued functions follows by splitting such a function into real and imaginary parts, and using linearity.

All that remains is to show uniqueness. Let $\mu'$ be a measure such that the eqation 
:::{math}
\Lambda f = \int_X f(x)\ d\mu' (x)
:::
 holds for every compactly supported function $f$. Let $K$ be a compact set. By theorem {prf:ref}`partition_1`, given an open set $U\supseteq K$, there is a compactly supported function $g$ such that $\chi_K \leq g\leq \chi_U$. Hence 
:::{math}
\mu' (K) \leq \int_X f d\mu' \leq \mu' (U)
:::
 and 
:::{math}
\mu'(U) = \sup \{ \Lambda f \ |\ f\leq \chi_U \} = \mu (U)
:::


It follows that $\mu (B)= \mu' (B)$ whenever $B$ is a Borel set, and we are done.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionThe Riesz Representation Theorem -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXIntegration of Continuous FunctionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionIntegration of Continuous Functions -->
# Integration of Continuous Functions
We would like to use the Riesz representation theorem to define a measure on the real line $\mathbb R$ that gives the usual integral expected from elementary calculus. To apply the Reisz representation theorem, we need a sensible definition of the integral of a continuous compactly supported function.

Let us consider a continuous function $f\colon [a,b]\rightarrow {\mathbb R}$. Let $n$ be a positive integer. Then the interval $[a,b]$ can be divided into $S^n$ equal-sized pieces: 
:::{math}
a < a+ 2^{-n}(b-a) < a+ 2(2^{-n})(b-a) < \cdots < a+ (2^n -1)(2^{-n})(b-a) < b
:::


Let us define 
:::{math}
\mu_{n,r} = \inf \{ f(x) \ |\ a+r2^{-n}(b-a) \leq f(x) < a+ (r+1)2^{-n}(b-a)
:::
 and 
:::{math}
I_n (f) = \sum_{r=0}^{2^n -1} 2^{-n}(b-a) \mu_{n,r}
:::


The following observations are clear.



The sequence $(I_n (f))$ is monotonically increasing

Since the interval $[a,b]$ is compact, and the function $f$ is continuous, there is a constant $C$ such that $f(x)\leq C$ for all $x\in [a,b]$. Hence $I_n (f) \leq C(b-a)$ for all $n$.


It follows that we have a well-defined limit 
:::{math}
\Lambda (f) := \lim_{n\rightarrow \infty} I_n (f)
:::


We would like to extend the definition of the function $\Lambda$. There are two stages to this extension.



Let $f\colon [a,b]\rightarrow {\mathbb C}$ be a continuous function. Write $f(x) = u(x) + iv(x)$, where $u,v\colon [a,b]\rightarrow {\mathbb R}$, and define
   :::{math}
   \Lambda (f) = \Lambda (u) + i \Lambda (v)
   :::

Let $f\in C_c ({\mathbb R})$. Let $[a,b]\supseteq \operatorname{supp} (f)$. Then we define
   :::{math}
   \Lambda (f) = \Lambda (f|_{[a,b]})
   :::


The following result is straightforward to check.


:::{prf:proposition} 
The map $\Lambda$ is a positive linear functional on the space $C_c ({\mathbb R})$.
**proof to be filled in!**
:::



:::{prf:definition} 
Let $f\in C_c ({\mathbb R})$. Then the number $\Lambda (f)$ is called the \em Riemann integral of $f$.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionIntegration of Continuous Functions -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe Lebesgue Measure on $\mathbb R$XXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe Lebesgue Measure on $\mathbb R$ -->
# The Lebesgue Measure on $\mathbb R$
:::{prf:definition} 
Let $\Lambda \colon C_c ({\mathbb R})\rightarrow {\mathbb C}$ be the Riemann integral. Then the \em Lebesgue measure on $\mathbb R$ is the unique measure such that 
:::{math}
\int_{\mathbb R} f\ d\mu = \Lambda (f)
:::
 whenever $f\in C_c ({\mathbb R})$.
:::


By the Riesz representation, the Lebesgue measure exists and is unique on the collection of all Borel sets. The integral of a Borel measurable function with respect to the Lebesgue measure is termed the \em Lebesgue integral. We will normally write 
:::{math}
\int_a^b f\ d\mu := \int_{\mathbb R} f\chi_{(a,b)}\ d\mu
:::



:::{prf:proposition} 
Let $a < b$ be real numbers. Then $\mu (a,b) = b-a$.
:::



:::{prf:proof}

Let $[c,d]\subseteq (a,b)$ be a compact interval. By Urysohn's lemma, there is a function $f\in C_c ({\mathbb R})$ such that $\chi_{[c,d]} \leq f \leq \chi_{(a,b)}$.

By definition of the Riemann integral: 
:::{math}
d-c \leq \int_{\mathbb R} f \leq b-a
:::


Let $c\rightarrow a$ and $d\rightarrow b$. Then $f\rightarrow \chi_{(a,b)}$ and by the dominated convergence theroem, 
:::{math}
\int_{\mathbb R} f \rightarrow \mu (a,b)
:::


It follows that $\mu (a,b) = b-a$, and we are done.
:::


A similar computation tells us that 
:::{math}
\mu [a,b] = \mu [a,b) = \mu (a,b] = b-a
:::
 whenever $a < b$.

The next fundamental property of the Lebesgue measure follows from a topological property of the real line, which we will state without proof.


:::{prf:proposition} 
Every open subset of the real line $\mathbb R$ is a countable disjoint union of open intervals.
**proof to be filled in!**
:::



:::{prf:corollary} 
:label: translation_1
Let $E\subseteq {\mathbb R}$ be a Borel set. Then $\mu (X+E) = \mu (E)$ whenever $x\in {\mathbb R}$.
**proof to be filled in!**
:::


We conclude with a general characterisation of sets of measure zero, or \em null sets.


:::{prf:theorem} 
Let $E\subseteq {\mathbb R}$ be a set such that every subset of $A$ is measurable. Then $\mu (A) =0$.
:::



:::{prf:proof}

The set $\mathbb R$ is an Abelian group under the operation of addition, and the set $\mathbb Q$ is a subgroup. Let $E$ be a set of real numbers containing precisely one element of each coset $x+ {\mathbb Q} \in {\mathbb R}/{\mathbb Q}$.

We claim:



$(r+E)\cap (s+E) = \emptyset$ whenever $r,s\in {\mathbb Q}$, $r\neq s$.

Let $x\in {\mathbb R}$. Then we can find an element $r\in {\mathbb Q}$ such that $x\in r+E$.


To see the first claim, suppose that $x\in (r+E)\cap (s+E)$, where $r,s\in {\mathbb Q}$. Then there are elements $y,z\in E$ such that $r+y = s+z$, and so $y-z\in {\mathbb Q}$. But the definition of the set $E$ means that $r=s$.

As for the second claim, let $x\in {\mathbb R}$. Construction of the set $E$ means that we can find a point $y\in E$ such that $x-y \in {\mathbb Q}$. But $x = y + (x-y)$ so the claim is established.

We now use the above to claims to prove the theorem. Let $t\in {\mathbb Q}$, and define $A_t := A\cap (t+E)$. The set $A_t$ is measurable since it is a subset of the set $A$. Consider a compact subset $K\subseteq A_t$, and let 
:::{math}
H = \bigcup_{r\in {\mathbb Q}\cap [0,1]} (r+K)
:::


Then the set $H$ is bounded and measurable, so $\mu (H) < \infty$. The first of the above claims tells us that the sets $r+K$ are pair-wise disjoint, so 
:::{math}
\mu (H) = \sum_{r\in {\mathbb Q}\cap [0,1]} \mu (r+K) = \sum_{r\in {\mathbb Q}\cap [0,1]} \mu (K)
:::
 by corollary {prf:ref}`translation_1`. It follows that $\mu (K)=0$ whenever $K\subseteq A_t$ is compact.

So $\mu (A_t) =0$. But 
:::{math}
A = \bigcup_{t\in {\mathbb Q}} A_t
:::
 and it follows that $\mu (A)=0$.
:::



:::{prf:corollary} 
Any countable subset of the space ${\mathbb R}$ has measure zero.
**proof to be filled in!**
:::



:::{prf:corollary} 
There are non-measurable subsets of the space $\mathbb R$.
**proof to be filled in!**
:::

<!-- XXSEC_PREFIX_ENDXX\sectionThe Lebesgue Measure on $\mathbb R$ -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe Fundamental Theorem of CalculusXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe Fundamental Theorem of Calculus -->
# The Fundamental Theorem of Calculus
By convention, when $a < b$ are real numbers, and $\mu$ is the Lebesgue measure on the space $\mathbb R$, we simplfy our notation slightly and write just 
:::{math}
\int_a^b f(x)\ dx := \int_a^b f\ d\mu
:::


If $b < a$, we write 
:::{math}
\int_a^b f(x)\ dx := - \int_b^a f(x)\ dx
:::


Linearity of the integral gives us the equation 
:::{math}
\int_a^b f(x)\ dx = \int_a^c f(x)\ dx + \int_c^b f(x)\ dx
:::
 whenever $a,b,c\in {\mathbb R}$.

This new notation is convenient when integating a concrete function given by some definite formula.

In this section we will focus on one major result, which is of absolutely vital importance when trying to calculate integrals. This result is termed the em fundamental theorem of calculus.


:::{prf:theorem} 
Let $f\colon [a,b] \rightarrow {\mathbb C}$ be a continuous function. Define a function $F\colon [a,b]\rightarrow {\mathbb C}$ by the formula 
:::{math}
F(x) = \int_a^x f(y)\ dy
:::


Then the function $F$ is differentiable on the open interval $(a,b)$, and has a one-sided derivative at the end-points $a$ and $b$. In all cases, the derivative is given by the formula 
:::{math}
F'(x) = f(x)
:::
:::



:::{prf:proof}

Let $\varepsilon > 0$, and let $x\in [a,b]$. Since the function $f$ is continuous, we can choose $\delta > 0$ such that $|f(x+h) -f(x)| < \varepsilon$ whenever $|h| < \delta$ and $x+h\in [a,b]$.

Let $x\in [a,b]$, and $x+h\in [a,b]$. Observe: 
:::{math}
F(x+h)- F(x)= \int_x^{h+h} f(y)\ dy
:::
 and 
:::{math}
hf(x) = f(x)\mu (x,x+h) = \int_x^{x+h} f(x)\ dy
:::


Suppose that $|h| < \delta$. Then $|f(y)-f(x)| < \varepsilon$ whenever $y\in [x,x+h]$, and so: 
:::{math}
\left| \int_x^{x+h} f(y)-f(x)\ dy \right| \leq \int_x^{x+h} |f(y) -f(x)|\ dy \leq \varepsilon |h|
:::


Thus: 
:::{math}
|F(x+h) -F(x) - hf(x)| \leq \varepsilon |h|
:::
 whenver $|h| < \delta$. It follows that the function $F$ is differentiable, and $F'(x) =f(x)$ as claimed.
:::


In actual fact, the more useful form of the fundmantal theorem of calculus is a variation of the above formula.


:::{prf:corollary} 
Let $F\colon [a,b]\rightarrow {\mathbb C}$ be a function with a continuous derivative $f$. Then 
:::{math}
\int_a^b f(x)\ dx = F(b)-F(a)
:::
:::



:::{prf:proof}

Define 
:::{math}
F_0 (x) = \int_a^x f(y)\ dy
:::


Then by the above version of the fundamental theorem of calculus, $F_0'(x) = f(x)$ whenever $x\in [a,b]$. Hence $F_0'(x) = F'(x)$ whenever $x\in [a,b]$, so there is a constant $C$ such that $F_0(x) = F(x) +C$ for all $x\in [a,b]$.

We know that $F_0 (a)=0$. Therefore $C=-F(a)$. We see that 
:::{math}
int_a^b f(x)\ dx = F_0 (b) = F(b) - F(a)
:::
 as claimed.
:::


The various integration formulae, such as integration by parts and the change of variable formula, come from the fundamental theorem of calculus along with the corresponding formulae for differentives, such as the derivative of a product and the derivative of a composition.
<!-- XXSEC_PREFIX_ENDXX\sectionThe Fundamental Theorem of Calculus -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXProduct MeasuresXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionProduct Measures -->
# Product Measures
Let $\Omega_1$ and $\Omega_2$ be measure spaces, with measures $\mu_1$ and $\mu_2$ on $\sigma$-algebras ${\mathcal M}_1$ and ${\mathcal M}_2$ respectively.


:::{prf:definition} 
We call a subset of the form $A\times B\subseteq X\times Y$, where $A\in {\mathcal M}_1$ and $B\in {\mathcal M}_2$ a \em measurable rectangle. A finite union of measurable rectangles is called an \em elementary set.

We write ${\mathcal M}_{12}$ to denote the smallest $\sigma$-algebra in the set $\Omega_1\times \Omega_2$ that contains every measurable rectangle.
:::


We want to define a measure on the $\sigma$-algebra ${\mathcal M}_{12}$. Before we can do this, we need some technical constructions.


:::{prf:definition} 
Let $\mathcal C$ be a collection of subsets of some set. Suppose that the following two conditions hold:



Let $(A_n)$ be a sequence of sets in the collection $\mathcal C$ such that $A_n\subseteq A_{n+1}$ for all $n$. Then $\bigcup_{n=1}^\infty A_n \in {\mathcal C}$.

Let $(B_n)$ be a sequence of sets in the collection $\mathcal C$ such that $B_n\supseteq B_{n+1}$ for all $n$. Then $\bigcup_{n=1}^\infty B_n \in {\mathcal C}$.


Then we call the collection $\mathcal C$ a \em monotone class.
:::


The proof of the following lemma is elementary, but rather abstract. We omit it.


:::{prf:lemma} 
:label: tech-product_1
The $\sigma$-algebra ${\mathcal M}_{12}$ is the smallest monotone class in the product $\Omega_1 \times \Omega_2$ which contains all elementary sets.
**proof to be filled in!**
:::


Given a subset $E\subseteq \Omega_1 \times \Omega_2$, and points $x\in Omega_1$ and $y\in \Omega_2$, let us write 
:::{math}
E_x = \{ y\in \Omega_2 \ |\ (x,y)\in E \} \qquad E^y = \{ x\in \Omega_1 \ |\ (x,y)\in E \}
:::



:::{prf:proposition} 
Let $E\in {\mathcal M}_{12}$. Then $E_x\ in {\mathcal M}_1$ and $E^y\in {\mathcal M}_2$ whenever $x\in \Omega_1$ and $y\in \Omega_2$.
:::



:::{prf:proof}

Let $x\in \Omega_1$. Let $\mathcal M$ be the collection of all elements $E\in \Omega_1 \times \Omega_2$ such that $E_x\in \Omega_2$. It is straightforward to check that $\mathcal M$ is a $\sigma$-algebra that contains every measurable rectangle. Therefore ${\mathcal M}_{12}\subseteq {\mathcal M}$, and we see that $E_x\in {\mathcal M}_2$ for every measurable set $E\subseteq \Omega_1\times \Omega_2$ and point $x\in \Omega_2$.

The corresponding statement concerning sets of the form $E^y$ is proved in the same way.
:::



:::{prf:corollary} 
:label: mpf_1
Let $X$ be a topological space, and let $f\colon \Omega_1 \times \Omega_2 \rightarrow X$ be a measurable function. Choose points $x\in \Omega_1$ and $y\in \Omega_2$. Then the functions 
:::{math}
f(x,-) \colon \Omega_2 \rightarrow X \qquad f(-,y) \colon \Omega_1 \rightarrow X
:::
 are measurable.
**proof to be filled in!**
:::



:::{prf:definition} 
A measure space $\Omega$ is called \em $\sigma$-finite if it is a countable union of spaces of finite measure.
:::



:::{prf:example} 
The space $\mathbb R$, equipped with the standard Lebesgue measure, is $\sigma$-finite.
:::


The following result lets us define measures on products of $\sigma$-finite measure spaces.


:::{prf:theorem} 
:label: pre-fub_1
Let $\Omega_1$ and $\Omega_2$ be $\sigma$-finite measure spaces. Let $E\subseteq \Omega_1\times \Omega_2$ be a measurable subset. Then we can define measurable functions $f\colon \Omega_1\rightarrow [0,\infty]$ and $g\colon \Omega_1\rightarrow [0,\infty]$ by the formulae 
:::{math}
f_E(x) = \mu_2 (E_x) \qquad g_E(y) = \mu_1 (E^y)
:::
 respectively. Further, 
:::{math}
\int_{\Omega_1} f_E = \int_{\Omega_2} g_E
:::
:::



:::{prf:proof}

Measurability of the functions $f_E$ and $g_E$ associated as above to a measurable set $E\subseteq X\times Y$ follows from the above proposition and corollary; all that remains it to prove the main equation.

Let ${\mathcal M}$ be the set of all measurable subsets $E\subseteq \Omega_1 \times \Omega_2$ such that the equation 
:::{math}
\int_{\Omega_1} f_E = \int_{\Omega_2} g_E
:::
 holds.

Let $E=A\times B$ be a measurable rectangle. Then $f_E = \mu_2 (B)\chi_A$ and $g_E = \mu_1 (A)\chi_B$. It follows that 
:::{math}
\int_{\Omega_1} f_E = \int_A \mu_2 (B) = \mu_1 (A) \mu_2 (B) \qquad \int_{\Omega_1} g_E = \int_B \mu_1 (A) = \mu_1 (A) \mu_2 (B)
:::
 so $E\in {\mathcal M}$.

Let $(E_n)$ be a sequence of sets in the collection $\mathcal M$ such that $E_n\subseteq E_{n+1}$ for all $n$. Write 
:::{math}
E= \bigcup_{n=1}^\infty E_n
:::


Then the sequences of functions $(f_{E_n})$ and $(g_{E_n})$ are monotonic increasing, with limits $f_E$ and $g_E$ respectively. We know that $E_n \in {\mathcal M}$ for all $n$, so that the equation 
:::{math}
\int_{\Omega_1} f_{E_n} = \int_{\Omega_2} g_{E_n}
:::
 holds for all $n$. The monotone convergence theorem gives us the equation 
:::{math}
\int_{\Omega_1} f_E = \int_{\Omega_2} g_E
:::
 and so tells us that $E\in {\mathcal M}$.

As a consequence of the above calculation, we can easily show that the union of a discrete sequence of measurable sets in the set $\mathcal M$ also belongs to the set $\mathcal M$. Let $(E_n)$ be a sequence of sets in the collection $\mathcal M$ such that $E_1\subseteq A\times B$, where $\mu_1 (A) < \infty$, $\mu_2 (B) < \infty$, and $E_n\supseteq E_{n+1}$ for all $n$. Write 
:::{math}
E= \bigcup_{n=1}^\infty E_n
:::


Then an argument similar to the above one, only using the dominated convergence theorem rather than the monotone convergence theorem, tells us that the set $E$ belongs to the collection $\mathcal M$.

Now, let $\Omega_1 = \cup_{n=1}^\infty \Omega_1^{(n)}$ and $\Omega_2 = \cup_{n=1}^\infty \Omega_2^{(n)}$, where $\mu_1 (\Omega_1^{(m)}) < \infty$ and $\mu_2 (\Omega_2^{(n)}) < \infty$ for all $m,n\in {\mathbb N}$. Given a set $E\subseteq \Omega_1\times \Omega_2$, let us write 
:::{math}
E_{mn} = E \cap (\Omega_1^{(m)} \times \Omega_2^{(n)}
:::


Let ${\mathcal C}$ be the collection of all measurable sets $E\subseteq \Omega_1 \times \Omega_2$ such that $E_{mn}\in {\mathcal M}$ for all natural numbers $m$ and $n$. Then the above calculations tell us that the collection $\mathcal C$ is a monotone class that contains every elementary rectangle. It follows from lemma {prf:ref}`tech-product_1` ${\mathcal M}_{12}\subseteq {\mathcal C}$, and we are done.
:::


To paraphrase the above theorem, the equation 
:::{math}
\int_{\Omega_1} \left( \int_{\Omega_2} \chi_E (x,y) \ d\mu_2 (y) \right) \ d\mu_1 (x)= \int_{\Omega_2} \left( \int_{\Omega_1} \chi_E (x,y) \ d\mu_1 (x) \right) \ d\mu_2 (y)
:::
 holds for every measurable set $E\subseteq \Omega_1 \times \Omega_2$.


:::{prf:definition} 
Let $\Omega_1$ and $\Omega_2$ be $\sigma$-finite measure sets. Then we define a measure $\mu$ on the product $\Omega_1 \times \Omega_2$ by writing 
:::{math}
\mu (E) := \int_{\Omega_1} \left( \int_{\Omega_2} \chi_E (x,y) \ d\mu_2 (y) \right) \ d\mu_1 (x)= \int_{\Omega_2} \left( \int_{\Omega_1} \chi_E (x,y) \ d\mu_1 (x) \right) \ d\mu_2 (y)
:::
 whenever the set $E\subseteq \Omega_1 \times \Omega_2$ is measurable.
:::


It is easy to check that the above definition satisfies the axioms required of a measure. As a special case of the above definition, we can now define a Lebesgue measure on the space ${\mathbb R}^n$ by viewing it as a product of copies of the space $\mathbb R$. This measure is defined on every Borel set, and the measure of the $n$-dimensional cuboid 
:::{math}
[a_1 , b_1] \times \cdots \times [a_n , b_n]
:::
 is the product 
:::{math}
(b_1 - a_1)(b_2-a_2) \cdots (b_n-a_n)
:::

<!-- XXSEC_PREFIX_ENDXX\sectionProduct Measures -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXFubini's TheoremXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionFubini's Theorem -->
# Fubini's Theorem
In the previous section, we saw how to define measures on products of $\sigma$-finite measure spaces. We can therefore integrate on such spaces. The purpose of this section is two state two results on the integrability of such functions, and how they are integrated. These results are usually put together, and referred to in one piece as \em Fubini's theorem.


:::{prf:theorem} 
Let $\Omega_1$ and $\Omega_2$ be $\sigma$-finite measure spaces, and let $f\colon \Omega_1 \times \Omega_2 \rightarrow {\mathbb C}$ be an integrable function. Then the functions $f(x,-)$ and $f(-,y)$ are integrable almost everywhere, and the functions 
:::{math}
x\mapsto \int_{\Omega_2} f(x,y) d\mu_2 (y) \qquad y\mapsto \int_{\Omega_2} f(x,y) d\mu_2 (y)
:::
 are integrable. Moreover, 
:::{math}
\int_{\Omega_1 \times \Omega_2} f(x,y) d\mu (x,y)
=\int_{\Omega_1} \left( \int_{\Omega_2} f (x,y) \ d\mu_2 (y) \right) \ d\mu_1 (x)= \int_{\Omega_2} \left( \int_{\Omega_1} f (x,y) \ d\mu_1 (x) \right) \ d\mu_2 (y)
:::
:::



:::{prf:proof}

Let $s\colon \Omega_1 \times \Omega_2 \rightarrow {\mathbb C}$ be a simple function. Then the functions $s(x,-)$ and $s(-,y)$ are integrable almost everywhere, the functions 
:::{math}
x\mapsto \int_{\Omega_2} s(x,y) d\mu_2 (y) \qquad y\mapsto \int_{\Omega_2} s(x,y) d\mu_2 (y)
:::
 are integrable, and the equation 
:::{math}
\int_{\Omega_1 \times \Omega_2} s(x,y) d\mu (x,y)
=\int_{\Omega_1} \left( \int_{\Omega_2} s (x,y) \ d\mu_2 (y) \right) \ d\mu_1 (x)= \int_{\Omega_2} \left( \int_{\Omega_1} s (x,y) \ d\mu_1 (x) \right) \ d\mu_2 (y)
:::
 holds by theorem {prf:ref}`pre-fub_1` and the definition of the product measure.

Now, suppose that $f(x,y)\geq 0$ for all points $(x,y)\in \Omega_1 \times \Omega_2$. Since the function $f$ is measurable, by proposition {prf:ref}`simpapp_1` there is a monotonically increasing sequence, $(s_n)$, of simple functions, with point-wise limit $f$. The result therefore follows in this case by the monotone convergence theorem.

By splitting a real-valued function into positive and negative parts, we see that the result holds for all real-valued functions. We can deduce the result for complex-valued functions by splitting such a function into real and imaginary parts.
:::


For the above theorem to be useful, we would like a criterion for a function $f\colon \Omega_1 \times \Omega_2 \rightarrow {\mathbb C}$ to be integrable. Fortunately, such a condition forms the second half of Fubini's theorem, which is also sometimes referred to as Tonelli's theorem.


:::{prf:theorem} 
Let $\Omega_1$ and $\Omega_2$ be $\sigma$-finite measure spaces, and let $f\colon \Omega_1 \times \Omega_2 \rightarrow {\mathbb C}$ be an integrable function. Suppose that 
:::{math}
\int_{\Omega_1} \left( \int_{\Omega_2} |f (x,y)| \ d\mu_2 (y) \right) \ d\mu_1 (x) < \infty
:::
 or 
:::{math}
\int_{\Omega_2} \left( \int_{\Omega_1} |f (x,y)| \ d\mu_1 (x) \right) \ d\mu_2 (y) < \infty
:::
 Then the function $f\colon \Omega_1\times \Omega_2 \rightarrow {\mathbb C}$ is integrable.
:::



:::{prf:proof}

The result is obvious if the function $f$ is simple. A similar argument to the proof of Fubini's theorem gives us the result in general.
:::


Combining the two theorems in this section (ie: the two halves of Fubini's theorem), we have the following handy result on swapping the order of integration.


:::{prf:corollary} 
Let $\Omega_1$ and $\Omega_2$ be $\sigma$-finite measure spaces, and let $f\colon \Omega_1 \times \Omega_2 \rightarrow {\mathbb C}$ be an integrable function. Suppose that 
:::{math}
\int_{\Omega_1} \left( \int_{\Omega_2} |f (x,y)| \ d\mu_2 (y) \right) \ d\mu_1 (x) < \infty
:::


Then 
:::{math}
\int_{\Omega_2} \left( \int_{\Omega_1} f (x,y) \ d\mu_1 (x) \right) \ d\mu_2 (y) < \infty = \int_{\Omega_1} \left( \int_{\Omega_2} f (x,y) \ d\mu_2 (y) \right) \ d\mu_1 (x) < \infty
:::

**proof to be filled in!**
:::

<!-- XXSEC_PREFIX_ENDXX\sectionFubini's Theorem -->

<!-- XXSEC_PREFIX_ENDXX\chapterMeasure and Integration theory -->

<!-- XXSEC_PREFIX_ENDXX\partFundamentals -->

<!-- XXSEC_DEF_SPLITTERXX\partXXSEC_DEF_SPLITTERXXFunctional AnalysisXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\partFunctional Analysis -->
# Functional Analysis
<!-- XXSEC_DEF_SPLITTERXX\chapterXXSEC_DEF_SPLITTERXXTopological Vector SpacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapterTopological Vector Spaces -->
(chpt:topological-vector-spaces_1)=
# Topological Vector Spaces
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXTopological division rings and fieldsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionTopological division rings and fields -->
(sec:topological-division-rings-fields_1)=
# Topological division rings and fields
\para Vector spaces with a compatible topology can not only defined for vector spaces over the ground fields $\mathbb{R}$ and $\C$ but also over fields $\mathbb{K}$ carrying an absolute value $|\cdot | : \mathbb{K} \to \mathbb{R}_{\geq 0}$. This endows the ground field with a topology which will be needed in the definition of a topological vector space. We therefore give here a brief introduction to topological division rings and fields first.


:::{prf:definition} 
Let $R$ be a division ring. By an *absolute value* on $R$ one understands a map $ |\cdot | : R \to \mathbb{R}_{\geq 0}$ such that the following axioms hold true.


(axiom:field-absolute-value-multiplicativity_1)=
(VDR1)
: The function $| \cdot |$ is multiplicative that is
   
   :::{math}
   |xy| = |x| \, | y| \quad \text{for all } x,y \in R \ .
   :::

(axiom:field-absolute-value-subadditivity_1)=
(VDR2)
: The triangle inequality is satisfied which means that
   
   :::{math}
   |x + y| \leq |x| + | y| \quad \text{for all } x,y \in R \ .
   :::

(axiom:field-absolute-value-nondegeneracy_1)=
(VDR3)
: For all $x \in R$ the relation $|x|=0$ holds true if and only if $x=0$.

A division ring or field endowed with an absolute value is called a *valued division ring*
respectively a *valued field*. An absolute value $|\cdot|$ on a division ring $R$ and the corresponding valued division ring $(R,|\cdot|)$ are called *non-archimedean* if the *strong triangle inequality* is satisfied that is if

\setcounterenumi3
(axiom:field-absolute-value-non-archimedean_1)=
(VDR1)
: $ |x + y| \leq \max \{ |x| , | y| \} $ for all $x,y \in R$.

Otherwise $|\cdot|$ and $(R,|\cdot|)$ are called *archimedean*.
:::



:::{prf:lemma} 
Let $(R,|\cdot|)$ be a valued division ring. Then



(ite:absolute-value-one_1)=
(i)
: $|1|=1$,

(ite:absolute-value-negative_1)=
(ii)
: $|-x| =|x|$ for all $x\in R$, and

(ite:absolute-value-difference_1)=
(iii)
: $\big| |x| - |y| \big| \leq |x - y| \leq |x| + |y|$ for all $x,y\in R$.
:::



:::{prf:proof}

{ref}`ite:absolute-value-one_1` holds true since $|1| = |1^2| = |1|^2$ and $|1| \neq 0$ by $1 \neq 0$. To verify {ref}`ite:absolute-value-negative_1` it suffices to show that $|-1| =1$. But that holds true since $|-1|^2 = | (-1)^2| = 1$ and $|-1| \geq 0$. The last claim follows by

:::{math}
- |x-y| = |x| - (|y-x| +|x|) \leq |x| - |y| \leq |x-y| + |y | - |y| = |x-y|
:::

and

:::{math}
|x - y| = | x + (-y)| \leq |x| + |-y| = |x| + |y| \ .
:::
:::



:::{prf:example} 


\itemindent
: Obviously, the *standard absolute values*
   
   :::{math}
   |\cdot |_\infty : \mathbb{Q}, \mathbb{R}\to \mathbb{R}_{\geq 0}, \: x \mapsto
   \begin{cases}
   x & \text{if } x\geq 0\\ -x & \text{if } x < 0
   \end{cases}
   \quad\text{and}\quad |\cdot |_\infty : \C\to \mathbb{R}_{\geq 0}, \: z \mapsto \sqrt{z \overline{z}}
   :::
   
   are absolute values on the fields $\mathbb{Q}$, $\mathbb{R}$ and $\C$, respectively. These absolute values are all archimedean since $|1+ 1|_\infty = 2 > 1$. Unless mentioned differently, we always assume $\mathbb{Q}$, $\mathbb{R}$ and $\C$ to be equipped with the standard absolute values. If no confusion can arise we usually write $|\cdot|$ instead of $|\cdot |_\infty$.

\itemindent
: The *standard absolute value* on the quaternions
   
   :::{math}
   |\cdot |_\infty : \H \to \mathbb{R}_{\geq 0} , \: q = a + b \,\mathsf{i} + c\,\mathsf{j} + d \,\mathsf{k} \mapsto \sqrt{\overline{q}q} = \sqrt{a^2 +b^2+ c^2 + d^2} \ ,
   :::
   
   where $a,b,c,d$ are real, is an archimedean absolute value. Usually it is briefly denoted $|\cdot|$.

\itemindent
: For every division ring $R$ the map
   
   :::{math}
   |\cdot| :R \to \mathbb{R}, \: x \mapsto
   \begin{cases}
   0 & \text{if } x=0 ,\\ 1 & \text{else}
   \end{cases}
   :::
   
   is a non-archimedean absolute value. It is called the *trivial absolute value* on $R$.

\itemindent
: An absolute value $|\cdot|:\mathbb{F} \to\mathbb{R}_{\geq 0}$ defined on a finite field $\mathbb{F}$ has to be trivial. To see this observe that for each $x\in \mathbb{K}^\times$ there exists an $n\in \mathbb{N}$ such that $x^n =1$. This entails $|x|^n=1$, hence $|x|=1$ for all $x\in \mathbb{K}^\times$. So $|\cdot|$ is trivial.

\itemindent
: The field of formal Laurent power series $\mathbb{K} ((X))$ over a field $\mathbb{K}$ can be equipped with an absolute value as follows. Choose $0 < \varepsilon < 1$ and define the absolute value $\left| \sum_{k\in \mathbb{Z}} a_k X^k\right| $ of an element $\sum_{n\in \mathbb{Z}} a_n X^n\in \mathbb{K} ((X)) $ as $\varepsilon^n$, where $n$ is the minimal integer such that $a_n\neq 0$.

\itemindent
: Let $p$ be prime number. For every integer $m\neq 0$ let $\nu_p(m)$ be the exponent of $p$ in the prime factor decomposition of $m$ that is $m = p^{\nu_p(n)}n$ where $n$ is relatively prime to $p$. For $m \in \mathbb{Z}$ and $n\in \mathbb{N}_{ > 0}$ one defines the **$p$-adic absolute value of the rational number $x = \frac mn$ by
   
   :::{math}
   \left| x \right|_p =
   \begin{cases}
   0 & \text{if } m=0 \ ,\\ p^{-\nu_p(m) +\nu_p(n)} & \text{else}\ .
   \end{cases}
   :::
   
   Note that $ \left| x \right|_p$ does not depend on the particular representation of $x$ as the quotient of integers $m$ and $n$. By definition it is immediately clear that the $p$-adic absolute value is an absolute value on $\mathbb{Q}$ indeed. It is non-archimedean.
:::



:::{prf:proposition} 
A valued division ring $(R,|\cdot|)$ is non-archimedean if and only if the image of $\mathbb{Z}$ under the canonical map $\mathbb{Z}\to R$ is bounded.
:::



:::{prf:proof}

Assume that $(R,|\cdot|)$ is a non-archimedean valued division ring. Then, $|0 \cdot 1| = |0|= 0 $ and, under the assumption that $|(n-1)\cdot 1|\leq 1$ for some $n\in \mathbb{N}_{ > 0}$, $|n\cdot 1| = | (n-1)\cdot 1 + 1 | = \max \{ |(n-1)\cdot 1| , 1 \} = 1$. Hence by induction and since $|-1| =1$ one obtains that $|n\cdot 1|\leq 1$ for all $n\in \mathbb{Z}$, and the image of $\mathbb{Z}$ in $R$ is bounded.

To show the converse assume that the image of $\mathbb{Z}$ in $R$ is bounded by some constant $C > 0$. Then, for all $x,y\in R$ and $n\in \mathbb{N}_{ > 0}$ by the binomial formula and the triangle inequality

:::{math}
|x+y|^n =\left|\sum_{k=0}^n {n \choose k} x^k y^{n-k} \right|
\leq (n+1) \,C \max \{|x|,|y|\}^n \ .
:::

Taking the $n$-th root gives $|x+y|\leq \big( (n+1)C\big)^{1/n} \max \{|x|,|y|\}$ which after passing to the limit $n\to\infty$ entails $|x+y| \leq \max \{|x|,|y|\}$ since $\lim\limits_{n\to\infty} \big( (n+1)C\big)^{1/n} = 1$. Hence $(R,|\cdot|)$ is non-archimedean.
:::



:::{prf:proposition} 
Let $|\cdot|$ be an absolute value on the division ring $R$. Then for every $\tau > 0$ with $\tau\leq 1$ the map $|\cdot|^\tau: R\to\mathbb{R}_{\geq 0}$ is an absolute value on $R$ as well. It is archimedean if and only if $|\cdot|$ is archimedean.
:::



:::{prf:proof}

To prove that $|\cdot|^\tau$ is an absolute value it suffices to show that $(a+b)^\tau \leq a^\tau + b^\tau$ for all $a,b\geq 0$. Without loss of generality we may assume $a \geq b > 0$. By dividing through $b^\tau$ one sees that the claim is equivalent to $(t +1 )^\tau \leq t^\tau + 1$ for all $t\geq 1$. For $t=1$ this is certainly true. The derivative of the function $h : {[ 1,\infty \rtsbrak}  \to\mathbb{R}$, $t\mapsto (t +1 )^\tau - t^\tau$ now is given by $h'(t) = \tau \big( (t +1 )^{\tau-1} - t^{\tau-1} \big)$ which is negative since $\tau-1\leq 0$ and $1+ t > t\geq 1$. Hence $h$ is monotone decreasing and $(t +1 )^\tau - t^\tau \leq 1$ for all $t\geq 1$.

Since $ {\ltsbrak 0,\infty \rtsbrak}  \to \mathbb{R}$, $t\mapsto t^\tau$ is strictly increasing and unbounded, the image of $\mathbb{Z}$ in $R$ is unbounded with respect to $|\cdot|$ if and only if it is with respect to $|\cdot|^\tau$.
:::


\para An absolute value $ |\cdot | : R \to \mathbb{R}_{\geq 0}$ on a division ring $R$ induces the metric $d : R \times R \to \mathbb{R}_{\geq 0}$, $(x,y) \mapsto |x-y|$ which then gives rise to a topology on $R$. This topology has the following properties:


(axiom:topological-division-ring-continuity-addition_1)=
(TDR1)
: Addition $+ : R \times R \to R$ is continuous.

(axiom:topological-division-ring-continuity-multiplication_1)=
(TDR2)
: Multiplication $\cdot : R \times R \to R$ is continuous.

(axiom:topological-division-ring-continuity-inversion_1)=
(TDR3)
: Inversion $(\:\cdot\:)^{-1}:R^\times \to R^\times $ is continuous, where $R^\times$ denotes the set of units in $R$ i.e.~$R^\times = R \setminus \{ 0\}$.



:::{prf:proof}

Addition is continuous since for all $a,b,x,y \in R$ by the triangle inequality

:::{math}
d ( x + y , a+ b ) = | x + y -( a+ b)| \leq | x-a| + | y-b| = d(x,a) + d(y,b)\ .
:::

Actually, this even shows that addition is Lipschitz continuous. Now fix $a,b \in R$ and let $C = \max \{ |a|,|b| \} + 1$. Then for all $x,y \in R$ with $d(y,b) < 1$

:::{math}
d ( x \cdot y , a \cdot b ) = | (x \cdot y - a \cdot y) + (a \cdot y - a \cdot b)|
\leq | x-a| \, |y| + |a| \, | y-b| \leq C \big( d(x,a) + d(y,b) \big) \ .
:::

Hence multiplication is continuous. Finally, fix $a \in R^\times$ and let $x \in R^\times $ with $d(x,a) < \frac{|a|}{2}$. Then $|x| \geq |a| - d(x,a) > \frac{|a|}{2} > 0$ and

:::{math}
d \left( x^{-1} , a^{-1} \right) = \left| x^{-1} - a^{-1} \right| = \left| x^{-1} \cdot a^{-1} \right|
\, | x-a | = \frac{1}{|x| \, |a|} d( x,a ) < \frac{2}{|a|^2} d( x,a ) \ .
:::

So inversion is also continuous.
:::



:::{prf:definition} 
A division ring or field $R$ which is equipped with a topology so that
{ref}`axiom:topological-division-ring-continuity-addition_1`,
{ref}`axiom:topological-division-ring-continuity-multiplication_1` and
{ref}`axiom:topological-division-ring-continuity-inversion_1` are satisfied is called a
*topological division ring* or a *topological field*, respectively.
:::



:::{prf:lemma} 
:label: thm:zero-neighborhood-topological-division-ring-infinite_1
If $|\cdot|$ is a non-trivial absolute value on the division ring $R$, then there exists an element $t\in R^\times$ such that the sequence $(t^n)_{n\in\mathbb{N}}$ converges to $0$. Furthermore in this case every $0$-neighborhood in $R$ contains infinitely many elements.
:::


:::{prf:proof}

By non-triviality of $|\cdot|$ there exists $t\in R^\times$ such that $|t|\neq 1$. By possibly passing to $t^{-1}$ we can assume $|t| < 1$. Since then $\lim\limits_{n\to\infty} |t|^n =0$, the sequence $(t^n)_{n\in\mathbb{N}}$ converges to $0$. This implies in particular that for every $\varepsilon > 0$ the open ball $\mathbb{B} (0,\varepsilon) =\{t \in R \mid |t| < \varepsilon \}$ contains infinitely many elements. So the lemma is proved.
:::



:::{prf:definition} 
Two absolute values $|\cdot|$ and $|\cdot|^\prime$ on a division ring $R$ are called *equivalent*
if they induce the same topology on $R$.
:::



:::{prf:theorem} 
Let $|\cdot|$ and $|\cdot|^\prime$ be two absolute values on the division ring $R$. Then they are equivalent if and only if there exists $e > 0$ such that $|\cdot|^\prime =|\cdot|^\tau$. In particular the trivial absolute value is the only one inducing the discrete topology on $R$.
:::



:::{prf:proof}

Let us first show the following proposition.


(ite:absolute-values-preserving-unit-balls_1)=
( A)
: If $|\cdot|$ and $|\cdot|^\prime$ are equivalent, then the relation $|x| < 1$ holds true for $x \in R^\times$ if and only if $|x|^\prime < 1$.

Since $\left| x^{-1}\right| =\frac{1}{|x|}$ and $\left| x^{-1}\right|^\prime =\frac{1}{|x|^\prime}$ for all $x \in R^\times$, {ref}`ite:absolute-values-preserving-unit-balls_1`
implies that $|x| > 1$ if and only if $|x|^\prime > 1$ and that $|x|= 1$ if and only if $|x|^\prime = 1$. To verify claim {ref}`ite:absolute-values-preserving-unit-balls_1` assume now that $0 < |x| < 1$. Then $\lim\limits_{n\to\infty}|x^n|=0$, hence $(x^n)_{n\in\mathbb{N}}$ converges to $0$. By assumption, $\lim\limits_{n\to\infty}|x^n|^\prime=0$ then holds as well which implies that $|x|^\prime < 1$. By switching $|\cdot|$ and $|\cdot|^\prime$ the converse holds true, so
{ref}`ite:absolute-values-preserving-unit-balls_1` is proved.

Next we show that $|\cdot|$ is trivial if and only if the induced topology on $R$ is discrete. Namely, if $|\cdot|$ is non-trivial, then there exists $x\in R^\times$ such that $|x| \neq 1$. After possibly passing to $\frac 1x$ we can achieve that $|x| < 1$. So $\lim\limits_{n\to\infty}|x^n|=0$, which means that $(x^n)_{n\in\mathbb{N}}$ is a sequence of non-zero elements of $R$ converging to $0$. But this implies that the singleton $\{ 0\}$ is not open in the topology induced by $|\cdot|$, hence this topology is non-discrete. Since obviously the trivial absolute value induces the discrete topology on $R$ the second claim of the theorem is proved.

Now assume that $|\cdot|^\prime =|\cdot|^\tau$ for some $\tau > 0$. Then a subset $B \subset R$ is a metric open ball with respect to $|\cdot|$ if and only if it is one with respect to $|\cdot|^\prime$ since for $x \in R$ and $\varepsilon > 0$

:::{math}
\begin{split}
&\big\{ y \in R \bigm\vert |y -x| < \varepsilon \big\} = \big\{ y \in R \bigm\vert |y-x|^\prime < \varepsilon^\tau \big\}
\text{ and } \\ &\big\{ y \in R \bigm\vert |y- x|^\prime < \varepsilon \big\} = \big\{ y \in R \bigm\vert |y-x| < \varepsilon^{1/\tau} \big\} \ .
\end{split}
:::

Hence the open sets with respect to the metric defined by $|\cdot|$ coincide with those defined by $|\cdot|^\prime$ and the two absolute values are equivalent.

Let us finally show the other direction and assume that $|\cdot|$ and $|\cdot|^\prime$ are equivalent. By the already proven second claim of the theorem we can restrict to the case where the induced topology is non-discrete which means to the case where both $|\cdot|$ and $|\cdot|^\prime$ are non-trivial. We show that there exists $\tau > 0$ such that $|x|^\prime = |x|^\tau $ for all $x\in R^\times$ with $ |x| > 1$. This is sufficient, since if $ |x|= 1$, then $|x|^\prime = 1 = |x|^\sigma $ for any $\sigma > 0$ by {ref}`ite:absolute-values-preserving-unit-balls_1`, and since if $x\in R^\times$ with $ |x| < 1$ then $ |x^{-1}| > 1$ and

:::{math}
|x|^\prime = \frac{1}{\left|x^{-1}\right|^\prime} = \frac{1}{\left|x^{-1}\right|^\tau} = |x|^\tau \ .
:::

The existence of a $\tau > 0$ with the claimed property is equivalent to the function

:::{math}
R^\times \to \mathbb{R},\: x \mapsto \frac{\ln |x|^\prime}{\ln |x|}
:::

being constant. Assume that that is not the case. Then there exist $x,y \in R^\times$ with $|x|,|y| > 1$ such that $\frac{\ln |x|^\prime}{\ln |x|} \neq \frac{\ln |y|^\prime}{\ln |y|}$. By possibly switching $x$ and $y$ we can assume $\frac{\ln |x|^\prime}{\ln |x|} < \frac{\ln |y|^\prime}{\ln |y|}$. But that implies $\frac{\ln |x|^\prime}{\ln |y|^\prime} < \frac{\ln |x|}{\ln |y|}$ since the logarithms are positive by assumptions on $x$ and $y$ and {ref}`ite:absolute-values-preserving-unit-balls_1`. Hence there exists a rational number $\frac pq$ with $p,q \in \mathbb{N}_{ > 0}$ such that

:::{math}
\frac{\ln |x|^\prime}{\ln |y|^\prime} < \frac pq < \frac{\ln |x|}{\ln |y|} \ .
:::

Then $|x^q|^\prime < |y^p|^\prime$ and $|y^p| < |x^q|$ which entails

:::{math}
\left| \frac{x^q}{y^p} \right|^\prime < 1 \text{ and }
\left| \frac{x^q}{y^p} \right| > 1 \ .
:::

This contradicts {ref}`ite:absolute-values-preserving-unit-balls_1` and the theorem is proved.
:::



:::{prf:remark} 


\itemindent
: By Ostrowski's theorem [@OstLF, p.~276], see also [@GouAN, Thm.~3.1.3], every non-trivial absolute value on the field$\mathbb{Q}$ of rational numbers is either equivalent to the standard absolute value $|\cdot|_\infty$ or to a $p$-adic absolute value $|\cdot|_p$ for some prime number $p$. Observe that for different primes $p$ and $q$ the absolute values $|\cdot|_p$ and $|\cdot|_q$ are not equivalent.

\itemindent
: Another theorem of Ostrowski [@OstLF, p.~284], sometimes called big Ostrowski's theorem, tells that for every archimedean valued field$(\mathbb{K},|\cdot|)$ there exists an embedding $\iota :\mathbb{K} \hookrightarrow \C$ into the field of complex numbers with its standard absolute value and a positive real number $\tau\leq 1$ such that
   
   :::{math}
   |x| =|\iota(x) |_\infty^\tau \quad \text{for all } x \in \mathbb{K} \ .
   :::
   
   In particular this means that every complete archimedean valued field is isomorphic to either $(\mathbb{R},|\cdot|_\infty^\tau)$ or $(\C,|\cdot|_\infty^\tau)$ for some positive $\tau\leq 1$.

\itemindent
: The $p$-adic absolute values on $\mathbb{Q}$ have extensions to $\mathbb{R}$ by [@LanA3rd, XII, \S4, Thm.~4.1]. This is a highly non-obvious result. To prove it one has to check first that$|\cdot|_p$ can be extended to an absolute value $|\cdot|$ on the field $\Bbbk$ of real numbers algebraic over $\mathbb{Q}$. This extended absolute value is, and that turns out to be crucial, again non-archimedean. Now one observes that $|\cdot|$ can be extended to the polynomial ring $\Bbbk [X]$ by the *Gau\ss norm*
   $|p(X)| = \max_{0\leq i \leq n} \{a_i\}$ where $p(X)= a_n X^n + \ldots + a_1 X + a_0 \in\Bbbk [X]$. The Gau\ss norm obviously extends to an absolute value on the fraction field $\Bbbk(X)$. Again, this extension is non-archimedean. Now one recalls that $\mathbb{R}$ is a purely transcendental field extension of $\Bbbk$ and uses a transfinite induction type argument involving the just constructed Gau\ss norm to extend $|\cdot|$ from $\mathbb{K}$ to $\mathbb{R}$. The thus obtained extension of the $p$-adic absolute value to $\mathbb{R}$ is not unique. In its construction, the axiom of choice is used, so one can not even give an explicit formula for such an extension.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionTopological division rings and fields -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe category of topological vector spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe category of topological vector spaces -->
(sec:vector-space-topologies-local-convexity_1)=
# The category of topological vector spaces
<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXVector space topologiesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Vector space topologies -->
## Vector space topologies
:::{prf:definition} 
:label: def:topological-vector-space_1
Let $R$ be a topological division ring. A topology $\mathscr{T}$ on a vector space $\mathrm{E}$ over $R$ is called a *vector space topology* if the following axioms hold true:


(axiom:tvs-continuity-addition_1)=
(TVS1)
: Addition $+ : \mathrm{E} \times \mathrm{E} \to \mathrm{E}$ is continuous.

(axiom:tvs-continuity-multiplication-scalars_1)=
(TVS2)
: Multiplication by scalars $\cdot : R \times \mathrm{E} \to \mathrm{E}$ is continuous.

The topology $\mathscr{T}$ on $\mathrm{E}$ is called *translation invariant*
if for every $w\in \mathrm{E}$ the linear map $\ell_{w} : \mathrm{E} \to \mathrm{E}$, $v\mapsto v +w$ is a homeomorphism.

A vector space $\mathrm{E}$ endowed with a vector space topology on it is called a *topological vector space* (*over* $R$), for short a \texttvs
:::



:::{prf:remark} 
Let us recall at this point some notation from linear algebra. Assume that $\mathrm{V}$ is a left vector space over the divison ring $R$. If $A,B\subset \mathrm{V}$ are two non-empty subsets, then $A+B$ is the set of all $v\in \mathrm{V}$ for which there exist $x\in A$ and $y\in B$ such that $v = x+y$. If $A$ or $B$ is empty, then $A+B$ is defined as the empty set. In case $A$ is a singleton that is if $A =\{x\}$, then we often write $x + B$ instead of $\{x\} +B$. If $\mathscr{B} \subset \mathscr{P}(\mathrm{V})$ is a non-empty set of subsets of $\mathrm{V}$, then we denote by $A + \mathscr{B}$ and $x + \mathscr{B}$ the sets $\{ A + B \in \mathscr{P}(\mathrm{V}) \mid B \in \mathscr{B}\} $ and $\{ x + B \in \mathscr{P}(\mathrm{V}) \mid B \in \mathscr{B}\} $, respectively. If $\mathscr{A} \subset \mathscr{P}(\mathrm{V})$ is a second non-empty set of subsets of $\mathrm{V}$, then $\mathscr{A} + \mathscr{B}$ stands for the set of all sets of the form $A+B$, where $A\in \mathscr{A}$ and $B\in \mathscr{B}$.

In case $C$ is a subset of the ground ring $R$, then $C \cdot A$ is defined as the set of all $v\in \mathrm{V}$ for which there exist $r\in C$ and $x\in A$ such that $v =r \cdot x$. If $r\in R$ we write $r\cdot A$ for $\{r\} \cdot A$. Likewise, if $x \in \mathrm{V}$, $C\cdot x$ stands for $C\cdot\{x\}$. Analogously as for addition the sets $\mathscr{C}\cdot A$, $C\cdot \mathscr{A}$ and $\mathscr{C}\cdot \mathscr{A}$ are defined when $\mathscr{C} \subset \mathscr{P}(R)$ and $\mathscr{A} \subset \mathscr{P}(\mathrm{V})$ are non-empty.
:::



:::{prf:proposition} 
:label: thm:basic-properties-sets-maps-topological-vector-spaces_1
Let $\mathrm{E}$ be a \texttvs~over a topological division ring $R$. Then the following holds true:



(ite:translated-homotheties-homeomorphisms_1)=
(i)
: For every $r\in R^\times$ and $w\in \mathrm{E}$ the homothety $\ell_{r,w} : \mathrm{E} \to \mathrm{E}$, $v\mapsto rv +w$ is a homeomorphism with inverse $\ell_{r^{-1},-r^{-1}w}$.

(ite:translated-base_1)=
(ii)
: Let $w$ be an element of $\mathrm{E}$ and $r\in R^\times$. A filter base $\mathscr{B}$ on $\mathrm{E}$ then is a filter base for the zero neighborhoods if and only if $w + r \mathscr{B}$ is a filter base for the neighborhoods of $w$.

(ite:closure-terms-base_1)=
(iii)
: If $\mathscr{B}$ is a filter base of the filter of zero neighborhoods, then the closure of any non-empty $A\subset \mathrm{E}$ is given by
   
   :::{math}
   \widebar{A} =\bigcap\limits_{U \in \mathscr{B}} A + U \ .
   :::

(ite:sum-open_1)=
(iv)
: Let $A\subset \mathrm{E}$ be open and $B\subset \mathrm{E}$. Then the set $A+B$ is open.

(ite:sum-closed_1)=
(v)
: Let $A, B \subset \mathrm{E}$ be closed and assume that $A$ is quasi-compact that is that any filter on $A$ has a cluster point. Then the set $A+B$ is closed.

(vi)
: The space $\mathrm{E}$ is {ref}`axiom:t3_1` or, equivalently, each point of $\mathrm{E}$ possesses a neighborhood base consisting of closed subsets.
:::



:::{prf:proof}



\itemindent
: The homothety $\ell_{r,w}$ is continuous since addition and multiplication by a scalar are continuous maps on a \texttvsSince for all $v\in V$
   
   :::{math}
   \nonumber & \ell_{r^{-1},-r^{-1}w}\circ \ell_{r,w} (v) = r^{-1} (rv +w) - r^{-1}w = v, \text{ and}\\
   \nonumber & \ell_{r,w} \circ \ell_{r^{-1},-r^{-1}w} (v) = r (r^{-1}v - r^{-1}w) + w = v
   :::
   
   the homothety $\ell_{r,w}$ is invertible, and its inverse is $\ell_{r^{-1},-r^{-1}w}$.

\itemindent
: This follows since $\ell_{r,w}$ is a homeomorphism.

\itemindent
: Let $B = \bigcap\limits_{U \in \mathscr{B}} A + U$. Let $v$ be an element of the closure of $A$. Then, for $U \in \mathscr{B}$, there exists an element $a \in A \cap v - U$ by {ref}`ite:translated-base_1`
   and since $-U$ is a zero neighborhood. Hence $v \in a + U$, and $\widebar{A} \subset B$ follows. Now let $v \in B$ and $V$ be a neighborhood of $v$. Then there exists $U\in \mathscr{B}$ such that $v -U \subset V$. By definition of $B$ there exists an element $a\in A$ such that $v \in a + U$. Hence $a \in v - U \subset V$ which implies that $v \in \widebar{A}$. So $B \subset \widebar{A}$.

\itemindent
: The set $A+B$ is either empty or coincides with the union $\bigcup_{v\in B} v + A$. In the latter case, each of the sets $v+ A$ is non-empty and open by continuity of addition. So $A+B$ is open under the assumptions made.

\itemindent
: We can assume that $A$ and $B$ are non-empty because the claim is trivial otherwise. Assume that $A+B$ is not closed. Then there exists an element $v \in \mathrm{E} \setminus (A+B) $ such that each neighborhood of $v$ meets $A+B$. This means in particular that the restriction of the neighborhood filter $\mathscr{U}$ of $v$ to $A+B$ is a filter base. Consequently, $(- B + \mathscr{U})\cap A$ is a filter base on $A$, hence possesses an accummulation point $x \in A$. For each neighborhood $V \in \mathscr{U}$ the point $x$ is then contained in the closure of $-B +V$. Hence, by {ref}`ite:closure-terms-base_1`, $x$ is contained in $v -B + U + U$ for every zero neighborhood $U$. Since by continuity of addition $U + U$ runs through a base of zero neighborhoods when $U$ runs through the zero neighborhoods, $x \in v - \widebar{B} = v -B$ follows. Since $x \in A$ this contradicts the assumption $v \in A+B$ and $A+B$ has to be closed.

\itemindent
: Let $v \in \mathrm{E}$, $A\subset \mathrm{E}$ closed, and assume $v \notin A$. Choose an open neighborhood $V$ of $v$ such that $V \cap A = \emptyset$. Then there exists an open zero neighborhood $U$ such that $v + U + U \subset V$. By possibly passing to $U \cap (-U)$ we can assume that $U = -U$. Now $v+U$ is an open neighborhood of $v$ and $A+U$ one of $A$. These neighborhoods are disjoint because if the intersection $v+U \cap A+U$ is non-empty, then there exists an element $w \in v+U + U\cap A$ since $-U =U$. This contradicts $V \cap A = \emptyset$, so $v+U$ and $A+U$ are disjoint neighborhoods of $v$ and $A$, respectively. Hence $\mathrm{E}$ satisfies {ref}`axiom:t3_1`.
:::



:::{prf:corollary} 
Every vector space topology on a vector space over a topological division ring is translation invariant.
:::



:::{prf:proof}

This follows immediately by
\Crefthm:basic-properties-sets-maps-topological-vector-spaces
{ref}`ite:translated-homotheties-homeomorphisms_1`.
:::



:::{prf:definition} 
A subset $C$ of a vector space $\mathrm{E}$ over a valued division ring $(R,|\cdot|)$ is called



(i)
: *symmetric* if $-v \in C$ for all $v\in C$,

(ii)
: *circled* or *balanced* if $rv \in C$ for all $v\in C$ and $r\in R$ with $|r| \leq 1$.
:::



:::{prf:remark} 
Symmetry of a subset of a vector space of a division ring is even defined when the underlying division ring does not carry an absolute value.
:::



:::{prf:lemma} 
:label: thm:closure-interior-circled-set-circled_1
Let $C$ be a subset of a topological vector space $\mathrm{E}$ over a valued division ring $(R,|\cdot|)$ and $r\in R$.



(ite:interior-closure-symmetric-sets-symmetric_1)=
(i)
: If $C$ is symmetric, then the closure $\widebar{C}$ and the interior $\mathring{C}$ are symmetric.

(ite:interior-closure-circled-sets-circled_1)=
(ii)
: If $C$ is circled, then the closure $\widebar{C}$ and the union $\mathring{C} \cup\{0\}$ are circled.

(ite:stretching-preserving-symmetric-circled-sets_1)=
(iii)
: The set $rC$ is symmetric (respectively circled) if $C$ has that property.
:::



:::{prf:proof}

Without loss of generality we can assume $C \neq \emptyset$. Claim {ref}`ite:interior-closure-symmetric-sets-symmetric_1` then follows immediately since multiplication by $-1$ is a homeomorphism. To prove claim {ref}`ite:interior-closure-circled-sets-circled_1` assume that $C$ is circled. Let $s\in R$ with $|s|\leq 1$. Assume $v \in \widebar{C}$ and consider $sv$. We have to show that $sv \in \widebar{C}$. If $s=0$ then $sv =0\in C \subset \widebar{C}$ since $C$ is circled. So we can assume $s\neq 0$ and need to show that for every neighborhood $V$ of $sv$ the intersection $C\cap V$ is non-empty. Since $|s| > 0$, the homothety $\ell_s:\mathrm{E}\to \mathrm{E}$, $w\mapsto sw$ is a homeomorphism with inverse $\ell_{s^{-1}}$. Hence $s^{-1}V$ is a neighborhood of $v$. Since $v$ lies in the closure of $C$ there exists an element $w\in C\cap s^{-1}V$. Hence $sw \in C \cap V$ by assumption on $C$ and $\widebar{C}$ is circled.

If $v \in \mathring{C}\cup\{0\}$ then $0 = 0 \cdot v \in \mathring{C}\cup\{0\}$. It remains to show that $sv \in \mathring{C}\cup\{0\}$ for $s\in R$ with $0 < |s|\leq 1$ and $v \in \mathring{C} \setminus \{ 0\}$. Under this assumption the homothety $\ell_s$ is a homeomorphism, so $s \mathring{C}$ is an open subset of $C$ since $C$ is circled. Hence $s v \in s \mathring{C} \subset \mathring{C}$, and $\mathring{C}\cup\{0\}$ is circled as well.

Claim {ref}`ite:stretching-preserving-symmetric-circled-sets_1` follows immediately from the observation that for $v\in C$ and $s\in R$ the relation $srv \in rC$ holds true if $sv \in C$.
:::



:::{prf:theorem} 
:label: thm:symmetric-circled-hulls_1
The intersection of a non-empty family $(C_i)_{i\in I}$ of symmetric (respectively circled) subsets $C_i \subset \mathrm{E}$, $i\in I$ of a topological vector space $\mathrm{E}$ over a valued division ring $(R,|\cdot|)$ is symmetric (respectively circled). In particular, if $A \subset \mathrm{E}$ is a subset, then the sets

:::{math}
\operatorname{Sym} A = \bigcap\limits_{A \subset B \subset \mathrm{E} \atop {B \text{ is symmetric}} } B \quad \text{and} \quad
\operatorname{Circ} A = \bigcap\limits_{A \subset B \subset \mathrm{E} \atop {B \text{ is circled}} } B
:::

are symmetric and circled, respectively. They have the property that $\operatorname{Sym} A$ is the smallest symmetric and $\operatorname{Circ} A$ the smallest circled subsets of $\mathrm{E}$ containing $A$. They are called the *symmetric* and the *circled hull* of $A$, respectively. Analogously,

:::{math}
\widebar{\operatorname{Sym}}\, A = \bigcap\limits_{A \subset B =\widebar{B} \subset \mathrm{E} \atop {B \text{ is symmetric}} } B \quad \text{and} \quad
\overline{\operatorname{Circ}}\, A = \bigcap\limits_{A \subset B =\widebar{B} \subset \mathrm{E} \atop {B \text{ is circled}} } B
:::

are called the *closed symmetric* and the *closed circled hull* of $A$, respectively. They have the property that $\widebar{\operatorname{Sym}}\, A$ is the smallest closed symmetric and $\overline{\operatorname{Circ}}\, A$ the smallest closed circled subset of $\mathrm{E}$ containing $A$.
:::


:::{prf:proof}

Note first that all the hulls in the proposition are well-defined since $\mathrm{E}$ is closed and circled. Let $C$ denote the intersection of the family $(C_i)_{i\in I}$. Assume that for some $r\in R$ with $|r|\leq 1$ the inclusion $rC_i \subset C$ holds true for all $i\in I$. Then $rC \subset C$, hence if all $C_i$ are symmetric (respectively circled), so is $C$. This observation now entails that $\operatorname{Sym} A$ is symmetric, $\operatorname{Circ}$ is circled, $\widebar{\operatorname{Sym}}\, A$ is closed and symmetric, and finally that $\overline{\operatorname{Circ}}\, A$ is closed and circled. Moreover, all those sets contain $A$. The minimality properties of these sets are clear by construction.
:::



:::{prf:remark} 
Observe that by the proposition $A$ is symmetric if and only if $\operatorname{Sym} A = A$ and circled if and only if $\operatorname{Circ} A = A$. Analogously, $\widebar{\operatorname{Sym}}\, A = A$ if and only if $A$ is closed symmetric and $\overline{\operatorname{Circ}}\, A = A$ if and only if $A$ is closed and circled.
:::



:::{prf:lemma} 
Let $\mathrm{E}$ be a topological vector space over the valued division ring $(R,|\cdot|)$ and $A \subset \mathrm{E}$ non-empty. Then

:::{math}
\operatorname{Sym} A = A \cup -A \quad \text{and} \quad \operatorname{Circ} A = \bigcup_{r\in R, \: |r|\leq 1} r A \ .
:::

For the closed hulls one has

:::{math}
\widebar{\operatorname{Sym}}\, A = \overline{\operatorname{Sym} A} \quad \text{and} \quad \overline{\operatorname{Circ}}\, A = \overline{\operatorname{Circ} A} \ .
:::
:::



:::{prf:proof}

Since $A \cup -A$ is symmetric by definition, contains $A$, and is contained in $\operatorname{Sym} A$, the equality $\operatorname{Sym} A = A \cup -A$ holds true. Similarly, $\bigcup_{r\in R, \: |r|\leq 1} r A$ is circled by definition, contains $A$, and is contained in $\operatorname{Circ} A$ by definition of the circled hull. Hence $ \operatorname{Circ} A = \bigcup_{r\in R, \: |r|\leq 1} r A $. The remainder of the claim follows from \Crefthm:closure-interior-circled-set-circled.
:::



:::{prf:definition} 
Assume that $B,C$ are subsets of a vector space $\mathrm{E}$ over the valued division ring $(R,|\cdot|)$. Then one says that



(i)
: $C$ *absorbes* $B$ if there exists a real number $t \in \mathbb{R}_{\geq 0}$ such that $B \subset rC$ for all $r\in R$ with $|r| \geq t$,

(ii)
: $C$ is *absorbing* or *absorbent*
   if $C$ absorbes every one-point set of $\mathrm{E}$ that is if for every $v\in \mathrm{E}$ there exists $t \in \mathbb{R}_{\geq 0}$ such that $v \in rC$ for all $r\in R$ with $|r| \geq t$.



If the vector space $\mathrm{E}$ carries in addition a vector space topology, then one says that


\setcounterenumi2
(i)
: the subset $B \subset \mathrm{E}$ is *bounded* if it is absorbed by every zero neighborhood.
:::



:::{prf:lemma} 
:label: thm:intersection-scalar-multiples-absorbing-sets-absorbing_1
Let $\mathrm{E}$ be a vector space over the valued division ring $(R,|\cdot|)$. Then the following holds true.



(ite:intersection-absorbing-sets-absorbing_1)=
(i)
: If $C_1,\ldots,C_n$ are absorbing subset of $\mathrm{E}$, then the intersection $C_1\cap\ldots \cap C_n$ is absorbing.

(ite:scalar-multiple-absorbing-set-absorbing_1)=
(ii)
: If $C$ is an absorbing subset of $\mathrm{E}$, then $rC$ is absorbing for every $r\in R^\times$.
:::



:::{prf:proof}



\itemindent
: Let $v\in\mathrm{E}$ and choose $t_1,\ldots,t_n\in \mathbb{R}_{\geq 0}$ such that $v \in rC_i$ for $|r|\geq t_i$. Put $t = \max \{ t_1,\ldots , t_n\}$. Then $v \in r (C_1\cap\ldots \cap C_n)$ for $|r|\geq t$, hence $C_1\cap\ldots \cap C_n$ is absorbing.

\itemindent
: Choose $t\in \mathbb{R}_{\geq 0}$ such that $v \in sC$ for all $s\in R$ with $|s|\geq t$. Then one has $|sr| \geq t$ for all $s\in R$ with $|s|\geq \frac{t}{|r|}$, hence $v \in s (rC)$ for all such $s$. Therefore $rC$ is absorbing.
:::



:::{prf:proposition} 
:label: thm:topological-vector-space-zero-neighborhood-filter-base-circled-absorbing_1
The filter of zero neighborhoods of a topological vector space $\mathrm{E}$ over $(R,|\cdot|)$ has a filter base $\mathscr{B}$ with the following properties:



(ite:tvs-base-element-containing-sum-base-elements_1)=
(i)
: For each $V \in \mathscr{B}$ there exists $U\in\mathscr{B}$ such that $U+U \subset V$.

(ite:tvs-base-elements-circled-balanced_1)=
(ii)
: Every element $V\in \mathscr{B}$ is circled and absorbing.

(ite:tvs-base-element-containing-shrunk-base-element_1)=
(iii)
: There exists an element $r\in R^\times$ with $0 < |r| < 1$ such that $V\in \mathscr{B}$ implies $rV \in \mathscr{B}$.


Conversely, if $\mathscr{B}$ is a filter base on an $R$-vector space $\mathrm{E}$ such that
{ref}`ite:tvs-base-element-containing-sum-base-elements_1` to {ref}`ite:tvs-base-element-containing-shrunk-base-element_1`
hold true, then there exists a unique vector space topology on $\mathrm{E}$ such that $\mathscr{B}$ is a neighborhood base at the origin. In case the ground ring $R$ is archimedean, a filter base on $\mathrm{E}$ which satisfies
{ref}`ite:tvs-base-element-containing-sum-base-elements_1` and {ref}`ite:tvs-base-elements-circled-balanced_1`
already induces a unique vector space topology having $\mathscr{B}$ as a neighborhood base at $0$. In either of these two cases, the thus constructed topology coincides with the coarsest translation invariant topology for which $\mathscr{B}$ is a set of zero neighborhoods.
:::



:::{prf:proof}

Assume that $\mathrm{E}$ is a \texttvsLet $\mathscr{B}$ be the set of circled neighborhoods of $0$. We show first that $\mathscr{B}$ is a base of the filter $\mathscr{U}_0$ of zero neighborhoods. Let $W \in \mathscr{U}_0$. By Axiom {ref}`axiom:tvs-continuity-multiplication-scalars_1` there exists an $\varepsilon > 0$ and an open zero neighborhood $U$ such that $sU \subset W$ for all $s\in R$ with $|s| < \varepsilon$. Then $V = \bigcup\limits_{s\in R^\times \:\&\: |s| < \varepsilon} sU $ is a zero neighborhood since by \Crefthm:zero-neighborhood-topological-division-ring-infinite the set of $s\in R^\times$ with $|s| < \varepsilon$ is non-empty. By construction $V$ is contained in $W$ and circled, so $V \in \mathscr{B}$. Hence $\mathscr{B}$ is a filter base of $\mathscr{U}_0$.

Next recall that there exists $r\in R^\times$ with $0 < |r| < 1$ since the absolute value $|\cdot|$ is non-trivial. Let $V\in \mathscr{B}$. Then $sV\subset V$ for all $s\in R$ with $|s|\leq 1$ which entails $srV \subset rV$ for all such $s$. Hence $rV$ is circled and an element of $\mathscr{B}$ as well. This proves
{ref}`ite:tvs-base-element-containing-shrunk-base-element_1`. Since addition on $\mathrm{E}$ is continuous, there exist for given $V\in \mathscr{B}$ open neighborhoods $U_1,U_2$ of the origin such that $U_1+U_2\subset V$. Choose $U\in \mathscr{B}$ such that $U \subset U_1 \cap U_2$. Then $U + U \subset V$ and {ref}`ite:tvs-base-element-containing-sum-base-elements_1` is proved. To show that any $V\in\mathscr{B}$ is absorbing let $v\in \mathrm{E}$. By continuity of scalar multiplication there exists $\varepsilon > 0$ such that $sv \in V $ for all $s\in R$ with $|s| < \varepsilon$. By \Crefthm:basic-properties-sets-maps-topological-vector-spaces {ref}`ite:translated-homotheties-homeomorphisms_1`
this entails $v \in sV $ for all $s\in R$ with $|s| > \varepsilon$ and $V$ is absorbing.

Now assume that $\mathrm{E}$ is an $R$-vector space and that $\mathscr{B}$ is a filter base that satisfies
{ref}`ite:tvs-base-element-containing-sum-base-elements_1`, {ref}`ite:tvs-base-elements-circled-balanced_1` and, if $|\cdot|$ is non-archimedean, {ref}`ite:tvs-base-element-containing-shrunk-base-element_1`. Since $\mathscr{B}$ consists of non-empty circled sets, $0\in V$ for all $V\in\mathscr{B}$. Let $\mathscr{T} \subset \mathscr{P}(\mathrm{E})$ be the set of all $U\subset \mathrm{E}$ such that for each $v\in U$ there exists $V\in \mathscr{B}$ with $v+V \subset U$. By definition and since $\mathscr{B}$ is a filter base, $\mathscr{T}$ is a topology on $\mathrm{E}$. By construction, $\mathscr{T}$ is also the coarsest translation invariant topology for which $\mathscr{B}$ is a set of zero neighborhoods. We show that $\mathscr{B}$ is a base of the filter $\mathscr{U}_0$ of zero neighborhoods. By definition of $\mathscr{T}$ there exists for each $U \in \mathscr{U}_0$ a $V\in \mathscr{B}$ such that $V\subset U$. So it remains to show that each $V\in \mathscr{B}$ is a zero neighborhood. To this end let $U$ be the set of all $v\in V$ for which there exists a $W\in \mathscr{B}$ with $v + W \subset V$. Since $0 +V \subset V$ one has $0\in U$. The relation $U \subset V$ holds because $0\in W$ for all $W\in \mathscr{B}$. Now let $v \in U$. By {ref}`ite:tvs-base-element-containing-sum-base-elements_1` there exists $W^\prime$ such that $v + W^\prime + W^\prime \subset V$ which entails $v + W^\prime \subset U$. Hence $U\in\mathscr{T}$ and $V$ is a zero neighborhood. Next we verify that $\mathscr{T}$ is a vector space topology. We start with continuity of addition. Let $W$ be an open neighborhood of $v+w$, where $v,w\in \mathrm{E}$. Then there exists $V\in \mathscr{B}$ such that $v+w + V \subset W$. Choose $U\in \mathscr{B} $ such that $U+U \subset V$. Then $v+U$ and $w +U$ are neighborhoods of $v$ and $w$, respectively, and $(v+U) + (w +U) \subset v+w +V\subset W$. So addition is continuous. We continue with scalar multiplication. Let $W$ be an open neighborhood of $rv$, where $r\in R$ and $v\in \mathrm{E}$. Then there exists $V \in \mathscr{B} $ such that $rv + V + V \subset W$. Since $V$ is absorbing by {ref}`ite:tvs-base-elements-circled-balanced_1` there exists $\varepsilon > 0$ such that $ (s-r)v \in V$ for all $s\in R$ with $|s-r| < \varepsilon$. Now if $|\cdot|$ is non-archimedean choose $t\in R^\times$ according to {ref}`ite:tvs-base-element-containing-shrunk-base-element_1`, and put $V_n = t^n V$ for all $n\in\mathbb{N}$. In the archimedean case let $t = \frac 12$ and use {ref}`ite:tvs-base-element-containing-sum-base-elements_1` to construct recursively a sequence $(V_n)_{n\in \mathbb{N} }$ of elements of $\mathscr{B}$ such that $2^nV_n = V_n + \ldots + V_n \subset V$, where the sum has $2^n$ summands. In either of these cases, choose $N\in \mathbb{N}$ large enough so that $|t|^N < \frac{1}{|r| + \varepsilon}$. Then $V_N \in \mathscr{B}$ and $v + V_N$ is a neighborhood of $v$. Moreover, for $w \in v + V_N$ there exists an element $x\in V$ such that $w-v = t^N x$. Then the relation $s (w-v) = s t^N x \in V $ holds whenever $|s-r| < \varepsilon$ since $V_N$ is circled. Hence for such $w$ and $s$

:::{math}
sw = rv + s (w-v) + (s-r)v \in rv + V + V \subset W \ .
:::

This means that scalar multiplication is continuous, and the proof is finished.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Vector space topologies -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXMorphisms of topological vector spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Morphisms of topological vector spaces -->
## Morphisms of topological vector spaces
:::{prf:definition} 
By a *morphism* of topological vector spaces over the topological division ring $R$ one understands a continuous $R$-linear map $f:\mathrm{E} \to\mathrm{F}$ between two topological vector spaces $\mathrm{E}$ and $\mathrm{F}$ over $R$. The space of morphisms between $\mathrm{E}$ and $\mathrm{F}$ will be denoted $\operatorname{Hom}\nolimits_{R\text{-}\mathsf{TVS}} (\mathrm{E},\mathrm{F})$ or just $\operatorname{Hom}\nolimits_R (\mathrm{E},\mathrm{F})$ or $\operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F})$ if now confusion can arrise.
:::



:::{prf:theorem} 
The topological vector spaces over a topological division ring $R$ as objects together with their morphisms form an additive category which we denote by $R\text{-}\mathsf{TVS}$. More precisely, $R\text{-}\mathsf{TVS}$ is a category enriched over the category of $R$-vector spaces where addition and scalar multiplication on the hom-spaces $\operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F})$ are given by

:::{math}
\nonumber +:&\:\operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F}) \times \operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F}) \to \operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F}),\: (f,g) \mapsto f+g = \left(\mathrm{E} \ni v \mapsto f(v)+g(v)\in \mathrm{F}\right)\ , \\ \nonumber
\cdot:&\:R \times \operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F}) \to \operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F}),\: (r,f) \mapsto r \cdot f = \left(\mathrm{E} \ni v \mapsto r \cdot f(v) \in \mathrm{F}\right) \ .
:::
:::



:::{prf:proof}

Observe first that the identity map $\mathrm{id}_\mathrm{E}$ on a topological vector space $\mathrm{E}$ is linear and continuous and so is the composition $g\circ f$ of two morphisms of topological vector spaces $f:\mathrm{E} \to\mathrm{F}$ and $g:\mathrm{F} \to\mathrm{G}$. Hence topological vector spaces over $R$ together with linear and continuous maps between them form a category.

Next check that the hom-space $\operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F})$ is an abelian group. Associativity and commutativity of addition follow from the respective properties on $\mathrm{F}$. The zero element is the constant map $\mathrm{E} \to\mathrm{F}$, $v \mapsto 0$ and the inverse of a morphism $f:\mathrm{E} \to\mathrm{F}$ is given by $-f:\mathrm{E} \to\mathrm{F}$, $v \mapsto -f(v)$. Similarly one checks that multiplication by scalars on $\operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F})$ is associative and distributes from the left and from the right over addition since scalar multiplication on $\mathrm{F}$ has these properties. Finally, the unit of $R$ acts as identity on $\operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F})$ since it does so on $\mathrm{F}$. Hence $\operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F})$ carries the structure of an $R$ left vector space.

Composition of morphisms $\operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F}) \times \operatorname{Hom}\nolimits (\mathrm{F},\mathrm{G}) \to \operatorname{Hom}\nolimits (\mathrm{E},\mathrm{G})$, $(f,g)\to g \circ f $ is an $R$-bilinear map as the following equalities for $f,f_1,f_2\in \operatorname{Hom}\nolimits (\mathrm{E},\mathrm{F})$, $g,g_1,g_2 \in \operatorname{Hom}\nolimits (\mathrm{F},\mathrm{G})$, $r\in R$, and $v\in \mathrm{E}$ show:

:::{math}
\nonumber &(f \circ (g_1+g_2)) (v) = f( (g_1+g_2) (v) ) = f( g_1(v) +g_2(v) ) = \\ \nonumber & \quad = f\circ g_1(v) + f\circ g_2(v) = (f\circ g_1+ f\circ g_2) (v)\ , \\ \nonumber &(f \circ (r g)) (v) = f( (rg) (v) ) = f(r g(v)) = r f( g(v)) = (r(f\circ g)) (v)\ , \\ \nonumber &((f_1+f_2) \circ g) (v) = (f_1+f_2) ( g (v)) = f_1(g(v)) + f_2 (g(v)) = \\ \nonumber & \quad = f_1\circ g(v) + f_2\circ g(v) = (f_1\circ g+ f_2\circ g) (v)\ , \\ \nonumber &((rf) \circ g) (v) = (rf)( g (v)) = r (f(g(v))) = r (f \circ g (v)) = (r(f\circ g)) (v) \ .
:::

Hence $R\text{-}\mathsf{TVS}$ is a category enriched over the category of $R$-vector spaces. In particular, $R\text{-}\mathsf{TVS}$ then is an additive category.
:::



:::{prf:example} 
For every \texttvs~$\mathrm{E}$ and non-zero element $t$ of the ground ring $R$ the map $\ell_t :\mathrm{E} \to \mathrm{E}$, $v \mapsto tv$ is an isomorphism of topological vector spaces by \Crefthm:basic-properties-sets-maps-topological-vector-spaces {ref}`ite:translated-homotheties-homeomorphisms_1`.
:::



:::{prf:theorem} 
A linear map $f: \mathrm{E} \to \mathrm{F}$ between topological vector spaces over a valued division ring $(R,|\cdot|)$ maps symmetric sets to symmetric sets and circled sets to circled sets. If in addition $f$ is continuous, then $f$ is *bounded* that means it maps bounded subsets of $\mathrm{E}$ to bounded subsets of $\mathrm{F}$.
:::



:::{prf:proof}

Since by linearity $f(tv) = t f(v)$ for all $v\in \mathrm{E}$ and $t\in R$, $f (C)$ is symmetric (respectively circled) if the subset $C\subset \mathrm{E}$ is.

To verify the second claim let $B\subset \mathrm{E}$ be bounded and $V\subset \mathrm{F}$ a zero neighborhood. Then $f^{-1} (V)$ is a zero neighborhood in $\mathrm{E}$ by continuity of $f$. Hence there exists an $r\in \mathbb{R}_{\geq 0}$ such that $B \subset tf^{-1} (V) $ for all $t\in R$ with $|t|\geq r$. By linearity of $f$ one obtains $f(B) \subset tV$ for all such $t$, so $f$ is bounded.
:::



:::{prf:remark} 
By the proposition continuity of a linear map between topological vector spaces implies the map to be bounded. As we will see later in this monograph, the converse does in general not hold true unless the underlying topological vector spaces are for example normable.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Morphisms of topological vector spaces -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXNormed real division algebras and local convexityXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Normed real division algebras and local convexity -->
## Normed real division algebras and local convexity
\para The major class of topological divison rings over which topological vector spaces are defined is formed by valued division rings $(R,|\cdot|)$ which carry the structure of an $\mathbb{R}$-algebra such that for all $r\in \mathbb{R}$ and $x\in R$ the equality

:::{math}
| rx | = |r|_\infty\cdot |x|
:::

holds true. We will therefore given them a particular name and call them
*normed real division algebras*. Note that the field of real numbers can be embedded into a normed real division algebra $R$ by the natural map $ \mathbb{R} \mapsto R$, $r \mapsto r\cdot 1$. Since $\mathbb{R}$ with its standard absolute value is archimedean, so is every normed real division algebra. By the Frobenius theorem, [@FroLSBF], there exist only three finite dimensional real division algebras, namely the field of real numbers$\mathbb{R}$, the field of complex numbers $\C$, and the quaternions $\H$.


:::{prf:definition} 
Under the assumption that $R$ is a normed real division algebra one calls a subset $C\subset \mathrm{E}$ of an $R$-vector space



(i)
: *convex* if $tv + (1-t)w \in C$ for all $v,w \in C$ and $t \in \mathbb{R}$ with $0\leq t \leq 1$,

(ii)
: *absolutely convex* if $rv + sw \in C$ for all $v,w \in C$ and $r,s \in R$ such that $|r|+|s|\leq 1$,

(iii)
: a *cone* if $tv \in C$ for all $v\in C$ and $t \in \mathbb{R}$ with $0\leq t \leq 1$.
:::



:::{prf:lemma} 
Let $R$ be a normed real division algebra. A subset $C$ of an $R$-vector space $\mathrm{E}$ then is absolutely convex if and only if it is circled and convex.
:::



:::{prf:proof}

The claim is trivial when $C=\emptyset$, so we assume that $C$ is nonempty.

Let $C$ be absolutely convex. Since $C$ contains at least one element $v$ one has $0 = 0 \cdot v + 0 \cdot v \in C$. Hence $ rv = (1-|r|) \cdot 0 + r v \in C$ for all $v\in C$ and $r\in R$ with $|r|\leq 1$. So $C$ is circled. By definition of absolute convexity $C$ is convex.

If $C$ is circled and convex, then it contains with elements $v,w$ also $r v + s w$ if $|r| + |s|\leq 1$. To see this observe first that $\varrho v \in C$ and $\sigma w \in C$ where the elements $\varrho,\sigma \in R $ have been chosen so that $|\varrho|=|\sigma|=1$, $r = |r| \cdot\varrho$ and $s = |s| \cdot\sigma$. Now if $|r| + |s| =0$, then $r v + s w = 0 \in C$ since $C$ is circled. If $|r| + |s| > 0$, then

:::{math}
r v + s w = (|r| + |s|) \left( \frac{|r|}{|r|+|s|} \varrho v + \frac{|s|}{|r|+|s|} \sigma w\right) \in C
:::

since $C$ is convex and circled. Hence $C$ is absolutely convex.
:::



:::{prf:lemma} 
A linear map $f:\mathrm{E} \to \mathrm{F}$ between vector spaces over a normed real divison algebra $R$ maps convex sets to convex sets, absolutely convex sets to absolutely convex sets, and cones to cones.
:::



:::{prf:proof}

This an immediate consequence of the linearity of $f$.
:::



:::{prf:lemma} 
:label: thm:closure-interior-convex-set-convex_1
Let $\mathrm{E}$ be a \texttvs~over a normed real division algebra $R$, let $C,D \subset \mathrm{E}$ be convex and $r \in R$. Then the following holds true.



(ite:closure-interior-convex-set-convex_1)=
(i)
: The closure $\widebar{C}$ and the interior $\mathring{C}$ are convex.

(ite:sum-multiple-convex-set-convex_1)=
(ii)
: The sets $C + D$ and $rC$ are convex.

(iii)
: If $C$ is absolutely convex, then so are $\widebar{C}$ and $\mathring{C}$.

(iv)
: If $C$ is absolutely convex, then so is $rC$ for each $r \in R^\times$.
:::



:::{prf:proof}

We consider only the cases $C,D\neq \emptyset$ because otherwise the claim is trivial.



\itemindent
: Let $t\in  {\ltsbrak 0,1 \rtsbrak} $. Then $t \widebar{C} + (1-t)\widebar{C} \subset \widebar{C} $ by continuity of the map $\mathrm{E} \times \mathrm{E} \to \mathrm{E}$, $(v,w) \mapsto tv +(1-t)w$. Hence $\widebar{C}$ is convex. Now let $v,w$ be points of the interior of $C$ and $ z =tv + (1-t)w$. Then $z\in C$, and there exists a zero neighborhood $U$ such that $v+U \subset C$ and $w+U\subset C$. Let $u\in U$ and compute
   
   :::{math}
   z + u = tv + (1-t)w + tu + (1-t)u = t(v+u) + (1-t)(w+u) \ .
   :::
   
   Since both $v+u$ and $w+u$ are elements of $C$ so is $z+u$ by convexity of $C$. Hence $z +U \subset C$ and $z$ lies in the interior of $C$.

\itemindent
: If $v,w \in C$, $x,y\in D$ and $t\in  {\ltsbrak 0,1 \rtsbrak} $, then by convexity of $C$ and $D$
   
   :::{math}
   t(v+x) + (1-t) (w+y) = \big( tv +(1-t) w \big) + \big( tx +(1-t) y \big) \in C + D \ .
   :::
   
   Hence $C+D$ is convex. Similarly,
   
   :::{math}
   t (rv) + (1-t) (rw) = r \big( t v + (1-t) w \big) \in r C \ ,
   :::
   
   so $rC$ is convex as well.

\itemindent
: Let $C$ be absolutely convex. If $\mathring{C}\neq \emptyset$, then $0\in \frac 12 \mathring{C} - \frac 12 \mathring{C} \subset C$, hence $0 \in \mathring{C}$. By \Crefthm:closure-interior-circled-set-circled and
   {ref}`ite:closure-interior-convex-set-convex_1`
   the claim now follows.

\itemindent
: By {ref}`ite:sum-multiple-convex-set-convex_1`, $rC$ is convex, so it remains to show that $rC$ is circled. Assume that $v\in rC$. Then $v = rw$ for a unique $w\in C$. Since $C$ is circled, $tw\in C$ for every $t\in R$ with $|t|\leq 1$. Hence $tv = r (tw) \in rC$ for such $t$ and $rC$ is circled.
:::



:::{prf:theorem} 
:label: thm:absolutely-convex-hulls_1
The intersection of a non-empty family $(C_i)_{i\in I}$ of convex (respectively absolutely convex) subsets $C_i \subset \mathrm{E}$, $i\in I$ of a topological vector space $\mathrm{E}$ over a normed real division algebra $R$ is convex (respectively absolutely convex). In particular, if $A \subset \mathrm{E}$ is a subset, then the sets

:::{math}
\operatorname{Conv} A = \bigcap\limits_{A \subset B \subset \mathrm{E} \atop {B \text{ is convex}} } B \quad \text{and} \quad
\operatorname{AConv} A = \bigcap\limits_{A \subset B \subset \mathrm{E} \atop {B \text{ is absolutely convex}} } B
:::

are convex and absolutely convex, respectively. The set $\operatorname{Conv} A$ is called the *convex hull* of $A$ and is the smallest convex set containing $A$. Similarly, $\operatorname{AConv} A$ is the smallest absolutely convex set containing $A$. It is called the *absolutely convex hull* of $A$. The *closed convex hull* $\overline{\operatorname{Conv}}\, A$ and the *closed absolutely convex hull* $\overline{\operatorname{AConv}}\, A$ of $A$ are defined by

:::{math}
\overline{\operatorname{Conv}}\, A = \bigcap\limits_{A \subset B = \widebar{B} \subset \mathrm{E} \atop {B \text{ is convex}} } B
\quad \text{and} \quad
\overline{\operatorname{AConv}}\, A = \bigcap\limits_{A \subset B = \widebar{B} \subset \mathrm{E} \atop {B \text{ is absolutely convex}} } B \ .
:::

These sets have the property that $\overline{\operatorname{Conv}}\, A$ is the smallest closed convex subset and $\overline{\operatorname{AConv}}\, A$ the smallest closed absolutely convex subset of $\mathrm{E}$ containing $A$.
:::



:::{prf:proof}

Let $C$ be the intersection $\bigcap\limits_{i\in I} C_i$ and assume that each $C_i$ is absolutely convex. Let $v,w\in C$ and $r,s \in R$ with $|r|+|s|\leq 1$. Then $v,w\in C_i$, hence $rv + sw \in C_i$ for all $i\in I$. Therefore $rv +sw \in C$ and $C$ is absolutely convex. This argument also shows that $C$ is convex if all $C_i$ are convex. The rest of the claim follows as in the proof of \Crefthm:symmetric-circled-hulls.
:::



:::{prf:remark} 
The proposition in particular entails that $A$ is convex if and only if $\operatorname{Conv} A = A$ and absolutely convex if and only if $\operatorname{AConv} A = A$. Analogously, $\overline{\operatorname{Conv}}\, A = A$ if and only if $A$ is closed and convex, and $\overline{\operatorname{AConv}}\, A = A$ if and only if $A$ is closed and absolutely convex.
:::



:::{prf:lemma} 
:label: thm:representation-convex-absolutely-convex-hulls-closures_1
Let $A \subset \mathrm{E}$ be a non-empty subset of a \texttvs~$\mathrm{E}$ over a normed real division algebra $R$. Then

:::{math}
:label: eq:absolutely-convex-hull-expression_1
& \operatorname{Conv} A = \left\{ \sum_{i=1}^k t_i v_i\in
\mathrm{E} \bigm\vert k \in \mathbb{N}_{ > 0},\: v_1,\ldots v_k\in A,\: t_1\ldots ,t_k \in \mathbb{R}_{\geq 0}, \: \sum_{i=1}^k t_i = 1 \right\}
\ , \\

& \operatorname{AConv} A = \left\{ \sum_{i=1}^k r_i v_i\in
\mathrm{E} \bigm\vert k \in \mathbb{N}_{ > 0},\: v_1,\ldots v_k\in A,\: r_1\ldots ,r_k \in R, \: \sum_{i=1}^k |r_i| \leq 1 \right\}
\ .
:::

For the closed hulls one has

:::{math}
\overline{\operatorname{Conv}}\, A = \overline{\operatorname{Conv} A} \quad \text{and} \quad \overline{\operatorname{AConv}}\, A = \overline{\operatorname{AConv} A} \ .
:::

Finally, if $A$ is circled, then

:::{math}
\operatorname{AConv} A = \operatorname{Conv} A \ .
:::
:::



:::{prf:proof}

By definition, the right hand side of Eq.~{eq}`eq:convex-hull-expression_1` is convex and contains $A$, hence it contains $\operatorname{Conv} A$. Conversely, one shows by induction on $k\in \mathbb{N}_{ > 0}$ and convexity of $\operatorname{Conv} A$ that each element of the form $\sum_{i=1}^k t_i v_i$ with $v_1,\ldots , v_k\in A$ and $t_1,\ldots ,t_k \in \mathbb{R}_{\geq 0}$ such that $\sum_{i=1}^k t_i = 1$ is in $\operatorname{Conv} A$. This proves Eq.~{eq}`eq:convex-hull-expression_1`. The proof of Eq.~{eq}`eq:absolutely-convex-hull-expression_1` is similar. Observe that the right hand side of Eq.~{eq}`eq:absolutely-convex-hull-expression_1` is absolutely convex and contains $A$. Hence it contains $\operatorname{AConv} A$. An argument using induction on $k\in \mathbb{N}_{ > 0}$ and absolute convexity of $\operatorname{AConv} A$ shows that each element of the form $\sum_{i=1}^k r_i v_i$ with $v_1,\ldots v_k\in A$ and $r_1\ldots ,r_k \in R$ such that $\sum_{i=1}^k |r_i| \leq 1$ is in $\operatorname{Conv} A$. So Eq.~{eq}`eq:absolutely-convex-hull-expression_1` holds true as well. The claim about the closed hulls is a consequence of \Crefthm:closure-interior-convex-set-convex. For the proof of the last claim it suffices to show that $\operatorname{Conv} A$ is circled if $A$ is. To this end let $v \in \operatorname{Conv} A$ and $r\in R$ with $|r|\leq 1$. Then one can write $v$ in the form $v = \sum_{i=1}^k t_i v_i$ with $v_1,\ldots, v_k\in A$ and $t_1, \ldots ,t_k \in \mathbb{R}_{\geq 0}$, where $\sum_{i=1}^k t_i = 1$. Hence $rv = \sum_{i=1}^k t_i (rv_i)$, which is in $\operatorname{Conv} A$, since $rv_i\in A$ for all $i$ because $A$ is circled.
:::



:::{prf:lemma} 
:label: thm:weighted-sum-convex-absolutely-convex-sets_1
Let $A \subset \mathrm{E}$ be a non-empty subset of a \texttvs~$\mathrm{E}$ over a normed real division algebra $R$.



(ite:weighted-sum-convex-sets_1)=
(i)
: If $A$ is convex and $t_1,\ldots, t_k\in \mathbb{R}_{\geq 0}$ with $k\in \mathbb{N}_{ > 0}$, then
   
   :::{math}
   \sum_{i=1}^k t_iA = \left( \sum_{i=1}^k t_i \right) A \ .
   :::

(ii)
: If $A$ is absolutely convex and $r_1,\ldots, r_k\in R$ with $k\in \mathbb{N}_{ > 0}$, then
   
   :::{math}
   \sum_{i=1}^k r_iA = \left( \sum_{i=1}^k |r_i| \right) A \ .
   :::
:::



:::{prf:proof}



\itemindent
: Obviously $\sum_{i=1}^k t_iA \supset \left( \sum_{i=1}^k t_i \right) A$. Let us show the converse inclusion. Without loss of generality we can assume that $t_i > 0$ for all $i$. Then $t = \sum_{i=1}^k t_i > 0$, so, after division by $t$, we can reduce the claim to showing that $\sum_{i=1}^k t_iA \subset A$ for $t_1,\ldots , t_k\in \mathbb{R}_{ > 0}$ such that $\sum_{i=1}^k t_i =1$. But $\sum_{i=1}^k t_iA \subset \operatorname{Conv} A = A$ by
   \Crefthm:representation-convex-absolutely-convex-hulls-closures and convexity of $A$.

\itemindent
: Since by absolute convexity $r_i A = |r_i|A$ for $i=1,\ldots,k$, the claim follows from {ref}`ite:weighted-sum-convex-sets_1`.
:::



:::{prf:lemma} 
:label: thm:real-absorbance-implies-arbsorbance-finite-dimensional-divison-algebra_1
Let $\mathbb{K}$ be one of the division rings $\C$ or $\H$ with their standard absolute values and let $\mathrm{E}$ be a vector space over $\mathbb{K}$. Then a convex subset $C\subset \mathrm{E}$ is absorbent in $\mathrm{E}$ if and only if it is absorbent in the realification $\mathrm{E}^\mathbb{R}$.
:::



:::{prf:proof}

It suffices to show the non-trivial direction. So assume that $C$ is convex and absorbent in the realification $\mathrm{E}^\mathbb{R}$. Denote by $u_1,\ldots , u_n$ the standard basis of $\mathbb{K}$ over $\mathbb{R}$ with $n=2$ or $n=4$ depending on $\mathbb{K}$. In particular this means $u_1 =1$. For given $v\in\mathrm{E}$ there now exists $t\in\mathbb{R}_{\geq 0}$ such that

:::{math}
\pm \frac{1}{u_1} v , \ldots , \pm \frac{1}{u_n} v \in rC \quad \text{for all } r\geq t \ .
:::

Without loss of generality we can assume $t\geq 1$. Let $z\in \mathbb{K}$ with $|z| \geq n t$. Then the vectors $c_1 = \operatorname{sgn} z_1\frac{n}{|z| \, u_1} v, \ldots , c_n = \operatorname{sgn} z_n\frac{n}{|z| \, u_n} v$ are elements of $C$. By convexity of $C$ and since $0\in C$ one has $ \frac{|z_1|}{|z|} c_1 , \ldots , \frac{|z_n|}{|z|} c_n \in C$. Again by convexity one concludes

:::{math}
\frac{1}{z} v = \sum_{i=1}^n \frac{z_i}{|z|^2 \, u_i} v =
\sum_{i=1}^n \frac{|z_i|}{n |z|} c_i \in C \ .
:::

Hence $C$ is absorbing and the claim is proved.
:::



:::{prf:definition} 
A topological vector space $\mathrm{E}$ over a normed real division algebra $R$ for which Axiom \hyperref[axiom:tvs-local-convexity]LCVS below holds true is called a
*locally convex topological vector space*, a *locally convex vector space* or shortly a
*locally convex \texttvs*.


(axiom:tvs-local-convexity_1)=
( LCVS)\!
: The vector space topology on $\mathrm{E}$ has a base consisting of convex sets.
:::



:::{prf:remark} 
For better readability, we often say *locally convex topology* instead of *locally convex vector space topology*.
:::



:::{prf:proposition} 
The locally convex topological vector spaces over a normed real division algebra $R$ together with the continuous linear maps between them form a full subcategory of the category $R\text{-}\mathsf{TVS}$ of topological $R$-vector spaces. It is denoted $R\text{-}\mathsf{LCVS}$.
:::


:::{prf:proof}

This is clear by definition.
:::



:::{prf:theorem} 
:label: thm:filter-base-absorbing-absolutely-convex-sets-generating-locally-convex-topology_1
The filter of zero neighborhoods of a locally convex topological vector space $\mathrm{E}$ over a normed real divison algebra $R$ has a filter base $\mathscr{B}$ with the following properties:



(ite:lctvs-base-element-containing-sum-base-elements_1)=
(i)
: For each $V \in \mathscr{B}$ there exists $U\in\mathscr{B}$ such that $U+U \subset V$.

(ite:lctvs-base-elements-circled-balanced_1)=
(ii)
: Every element of $\mathscr{B}$ is a *barrel* that means is absolutely convex, closed and absorbing.

(ite:lctvs-base-element-containing-shrunk-stretched-base-element_1)=
(iii)
: Let $r\in R^\times$. Then $V\in \mathscr{B}$ if and only if $rV \in \mathscr{B}$.


Conversely, if $\mathscr{B}$ is a filter base on an $R$-vector space $\mathrm{E}$ such that
{ref}`ite:lctvs-base-element-containing-sum-base-elements_1` holds true and such that each element of $\mathscr{B}$ is absolutely convex and absorbing, then there exists a unique locally convex topology on $\mathrm{E}$ such that $\mathscr{B}$ is a neighborhood base of the origin. It is the coarsest among all translation invariant topologies for which $\mathscr{B}$ is a set of zero neighborhoods and is called the *locally convex topology generated* or
*induced by* $\mathscr{B}$.
:::



:::{prf:proof}

Let $\mathrm{E}$ be a locally convex \texttvs. Let $\mathscr{B}$ be the collection of all barrels which are at the same time zero neighborhoods. Let $V$ be an element of $\mathscr{U}_0$, the filter of zero neighborhoods. Since $\mathrm{E}$ is \textsf(T3) by
\Crefthm:basic-properties-sets-maps-topological-vector-spaces, there exists a closed zero neighborhood $V_a$ such that $V_a \subset V $. By local convexity of $\mathrm{E}$ there exists a convex zero neighborhood $V_b$ with $V_b\subset V_a$. By
\Crefthm:topological-vector-space-zero-neighborhood-filter-base-circled-absorbing there exists a circled zero neighborhood $V_c$ with $V_c\subset V_b$. The closed convex hull $U = \overline{\operatorname{Conv}}\, V_c$ then is a barrel contained in $V$. Since it is a zero neighborhood it is an element of $\mathscr{B}$, and $\mathscr{B}$ is a filter base of $\mathscr{U}_0$. This proves {ref}`ite:lctvs-base-elements-circled-balanced_1`.

To verify {ref}`ite:lctvs-base-element-containing-sum-base-elements_1`, let $V \in \mathscr{B}$ and observe that by continuity of addition there exist zero neighborhoods $U_1$ and $U_2$ such that $U_1 + U_2 \subset V$. Choose $U\in \mathscr{B} $ such that $U \subset U_1\cap U_2$. Then $U + U \subset V$.

Claim {ref}`ite:lctvs-base-element-containing-shrunk-stretched-base-element_1` holds true since multiplication by an element $r\in R^\times$ is a homeomorphism which preserves circled and convex sets.

The remaining claim follows immediately from
\Crefthm:topological-vector-space-zero-neighborhood-filter-base-circled-absorbing
and the observation that a real division algebra is archimedean.
:::



:::{prf:corollary} 
Let $\mathscr{S}$ be a non-empty set of absolutely convex and absorbent subsets of a vector space $\mathrm{E}$ over a normed real divison algebra $R$. Then the set

:::{math}
\mathscr{B} = \Big\{ r\, \bigcap\limits_{B\in\mathscr{F}} B \in\mathscr{P}(\mathrm{E}) \bigm\vert
\mathscr{F}\in \mathscr{P}_{fin}(\mathscr{S}),\: \mathscr{F} \neq \emptyset \:\: \& \:\: r\in R^\times
\Big\}
:::

consists of absolutely convex and absorbent subsets of $\mathrm{V}$ and is a base of the filter of zero neighborhoods of a locally convex topology $\mathscr{T}$ on $\mathrm{E}$ uniquely determined by that property. This topology is the coarsest among all vector space topologies for which $\mathscr{S}$ is a set of zero neighborhoods. The topology $\mathscr{T}$ is called the
*locally convex topology generated* or *induced* by $\mathscr{S}$.
:::



:::{prf:proof}

The intersection of finitely many absolutely convex and absorbing sets is non-empty and again absolutely convex and absorbing by
\Crefthm:intersection-scalar-multiples-absorbing-sets-absorbing {ref}`ite:intersection-absorbing-sets-absorbing_1`
and \Crefthm:absolutely-convex-hulls. By \Crefthm:intersection-scalar-multiples-absorbing-sets-absorbing
{ref}`ite:scalar-multiple-absorbing-set-absorbing_1` and
\Crefthm:closure-interior-convex-set-convex, the scalar multiple of an absolutely convex and absorbing set again has these properties whenever the scalar is invertible. Hence each element of $\mathscr{B}$ is absolutely convex and absorbing. Given two elements $C,D\in \mathscr{B}$ there exist non-empty $\mathscr{F},\mathscr{G}\in \mathscr{P}_{fin}(\mathscr{S})$ and $r,s\in R^\times$ such that $ C = r \bigcap\limits_{B \in \mathscr{F}} B $ and $D = s \bigcap\limits_{B \in \mathscr{G}} B$. Without loss of generality one can assume that $|r|\leq |s|$. Then $A= r \bigcap\limits_{B \in \mathscr{F}\cup \mathscr{G}} B \in \mathscr{B}$ and $A = C \cap rs^ {-1}D \subset C \cap D$ since $D$ is balanced and $|rs^{-1}| \leq 1$. Hence $\mathscr{B}$ is a filter base consisting of absolutely convex and absorbent sets. Moreover, $\frac 12 C + \frac 12 C\subset C $ for every $C \in \mathscr{B}$ by absolut convexity. By Proposition {prf:ref}`thm:filter-base-absorbing-absolutely-convex-sets-generating-locally-convex-topology_1`
the filter base $\mathscr{B}$ therefore generates a unique locally convex topology $\mathscr{T}$ for which $\mathscr{B}$ is a base of the filter of zero neighborhoods. Moreover, $\mathscr{T}$ is the coarsest translation invariant topology so that $\mathscr{B}$ is a set of zero neighborhoods. This implies in particular that $\mathscr{S}$ is a set of zero neighborhoods for $\mathscr{T}$. Now let $\mathscr{T}'$ be a vector topology such that each element of $\mathscr{S}$ is a zero neighborhood. Then finite intersections of elements of $\mathscr{S}$ are zero neighborhoods with respect to $\mathscr{T}'$ and therefore also all elements of $\mathscr{B}$. Since $\mathscr{T}'$ is translation invariant one concludes that $\mathscr{T}$ is coarser than $\mathscr{T}'$ and the claim is proved.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Normed real division algebras and local convexity -->

<!-- XXSEC_PREFIX_ENDXX\sectionThe category of topological vector spaces -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXSeminorms and gauge functionalsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionSeminorms and gauge functionals -->
(sec:seminorms-gauge-functionals_1)=
# Seminorms and gauge functionals
\para Throughout the rest of this chapter the symbol $\mathbb{K}$ will always stand for the field of real numbers $\mathbb{R}$, the field of complex numbers $\C$ or the division algebra of quaternions $\H$. We assume these division algebras to be equipped with their standard absolute values $|\cdot |$. Moreover, vector spaces are assumed to be defined over the ground field $\mathbb{K}$ unless mentioned differently and are always assumed to be left vector spaces.


<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXSeminorms and induced vector space topologiesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Seminorms and induced vector space topologies -->
## Seminorms and induced vector space topologies
:::{prf:definition} 
By a *seminorm* on a vector space $\mathrm{E}$ one understands a map $p:\mathrm{E} \to \mathbb{R}$ with the following properties:

\setcounterenumi-1
(axiom:positive_1)=
(N1)
: The map $p$ is *positive* that is $p(v)\geq 0$ for all $v\in \mathrm{E}$.

(axiom:norm-absolute-homogeneity_1)=
(N2)
: The map $p$ is *absolutely homogeneous* that means
   
   :::{math}
   p(r v) = |r| \, p(v) \quad \text{for all $v \in \mathrm{E}$ and $r\in \mathbb{K}$}.
   :::

(axiom:norm-subadditivity_1)=
(N3)
: The map $p$ is *subadditive* or in other words satisfies the *triangle inequality*
   
   :::{math}
   p(v+w) \leq p(v) + p(w) \quad \text{for all $v,w \in \mathrm{E}$}.
   :::

A seminorm is called a *norm* if in addition the following axiom is satisfied:

\setcounterenumi2
(axiom:norm-nondegeneracy_1)=
(N1)
: For all $v\in \mathrm{E}$ the relation $p(v) = 0$ holds true if and only if $v = 0$.

A vector space $\mathrm{E}$ equipped with a norm $\| \cdot \| : \mathrm{E} \to \mathbb{R}_{\geq 0}$ is called a *normed vector space*.
:::


\para Let us introduce some useful further properties a map $p:\mathrm{E} \to \mathbb{R}$ can have. One calls such a map $p$


(ite:definition-positive-homogeneity_1)=
(1)
: *positively homogeneous* if $p (tv) = t\, p(v)$ for all $t\in \mathbb{R}_{ > 0}$ and all $v\in \mathrm{E}$,

(ite:definition-sublinearity_1)=
(2)
: *sublinear* if $p (tv + sw) \leq t\, p(v) + s\, p(w)$ for all $t,s\in \mathbb{R}_{\geq 0}$ and all $v,w\in \mathrm{E}$, and

(ite:definition-convexity_1)=
(3)
: *convex* if $p (tv + sw) \leq t\, p(v) + s\, p(w)$ for all $t,s\in \mathbb{R}_{\geq 0}$ with $t+s=1$ and all $v,w\in \mathrm{E}$.



:::{prf:lemma} 
:label: thm:equivalent-characterizations-sublinearity_1
For a real-valued map $p:\mathrm{E} \to \mathbb{R}$ on a vector space $\mathrm{E}$ the following are equivalent:



(ite:sublinearity_1)=
(i)
: $p$ is sublinear.

(ite:positive-homogeneity-convexity_1)=
(ii)
: $p$ is positively homogeneous and convex.

(ite:positive-homogeneity-subadditivity_1)=
(iii)
: $p$ is positively homogeneous and subadditive.
:::


:::{prf:proof}

Let $p$ be sublinear. Then $p$ is subadditive by definition. Subadditivity implies $p(0) \leq p(0) + p(0)$, hence $p(0)\geq 0$. By sublinearity

:::{math}
p(0) = p(0\cdot 0 + 0\cdot 0) \leq 0 \cdot p(0) + 0\cdot p(0) = 0 \ ,
:::

so $p(0)=0$. We show that $p$ is positively homogeneous. Applying sublinearity again one checks for $v\in \mathrm{E}$ and $t\geq 0$ that

:::{math}
p(tv)=p(tv+ 0\cdot 0) \leq t p(v) + 0 \cdot p(0)= tp(v) \ ,
:::

so $p$ is positively homogeneous and the implication
{ref}`ite:sublinearity_1` $\implies$ {ref}`ite:positive-homogeneity-subadditivity_1` follows. If $p$ is positively homogeneous and subadditive, then for $v,w \in \mathrm{E}$ and $t,s > 0$ with $t +s =1$

:::{math}
p(tv +sw) \leq p(tv) + p(sw) \leq t p(v) + s p(w),
:::

so $p$ is convex. This gives the implication
{ref}`ite:positive-homogeneity-subadditivity_1` $\implies$ {ref}`ite:positive-homogeneity-convexity_1`. If $p$ is positively homogeneous and convex, then one computes for $v,w \in \mathrm{E}$ and $t,s\geq 0$ with $t+s > 0$

:::{math}
p( tv +sw ) = (t+s)\, p \left( \frac{t}{t+s} v+ \frac{s}{t+s} w \right) \leq (t+s) \left( \frac{t}{t+s} p(v) + \frac{s}{t+s} p(w) \right) = t p(v)+ sp(w) \ .
:::

Since $p(0)=\lim\limits_{t\searrow 0} p(t0) = \lim\limits_{t\searrow 0} t\, p(0) = 0$ by positive homogeneity, $p$ then has to be sublinear and one obtains the implication
{ref}`ite:positive-homogeneity-convexity_1` $\implies$ {ref}`ite:sublinearity_1`.
:::



:::{prf:lemma} 
:label: thm:properties-subadditive-convex-real-valued-maps-vector-space_1
Let $p:\mathrm{E} \to \mathbb{R}$ be a real-valued map defined on a vector space $\mathrm{E}$ over $\mathbb{K}$.



(ite:implications-positive-homogeneity_1)=
(i)
: If $p:\mathrm{E} \to \mathbb{R}$ is positively homogeneous, then $p(0)=0$.

(ite:implications-subadditivity_1)=
(ii)
: If $p:\mathrm{E} \to \mathbb{R}$ is subadditive, then $p(0)\geq 0$ and for all $v,w\in \mathrm{E}$
   
   :::{math}
   |p(v)-p(w)| \leq \max \{ p(v-w),p(w-v) \} \ .
   :::

(ite:implications-convexity-real-valued-map_1)=
(iii)
: If $p:\mathrm{E} \to \mathbb{R}$ is convex, then the sets $\mathbb{B}_{p,\varepsilon} := \{v\in \mathrm{E}\mid p(v) < \varepsilon\} $ and $\overline{\mathbb{B}}_{p,\varepsilon} := \{v\in \mathrm{E}\mid p(v) \leq \varepsilon\}$ are convex for all $\varepsilon > 0$.

(ite:implications-sublinearity-real-valued-map_1)=
(iv)
: If $p$ is sublinear, then $\mathbb{B}_{p,\varepsilon}$ and $\overline{\mathbb{B}}_{p,\varepsilon}$ are convex and absorbent for all $\varepsilon > 0$.
:::


:::{prf:proof}



\itemindent
: As already observed, $p(0)=\lim\limits_{t\searrow 0} p(t0) = \lim\limits_{t\searrow 0} t\, p(0) = 0$.

\itemindent
: Note that by subadditivity
   
   :::{math}
   p(0)\leq p(0) + p(0), \quad p(v) -p(w) \leq p(v-w), \quad \text{and} \quad p(w) -p(v) \leq p(w-v) \ .
   :::
   
   This entails {ref}`ite:implications-subadditivity_1`.

\itemindent
: Let $v,w\in \{v\in \mathrm{E}\mid p(v) < \varepsilon\}$ and $0\leq t \leq 1$. Then, by convexity of $p$,
   
   :::{math}
   p\big(tv + (1-t)w\big) \leq t p(v) + (1-t) p(w) < t\varepsilon + (1-t) \varepsilon = \varepsilon \ .
   :::
   
   Hence $tv + (1-t)w\in \{v\in \mathrm{E}\mid p(v) < \varepsilon\} $. The proof for $\{v\in \mathrm{E}\mid p(v) \leq \varepsilon\}$ is analogous.

\itemindent
: Convexity of the sets $\mathbb{B}_{p,\varepsilon}$ and $\overline{\mathbb{B}}_{p,\varepsilon}$ holds by
   {ref}`ite:implications-convexity-real-valued-map_1`. Moreover, $\mathbb{B}_{p,\varepsilon} \subset \overline{\mathbb{B}}_{p,\varepsilon}$ by definition. Hence it suffices by \Crefthm:real-absorbance-implies-arbsorbance-finite-dimensional-divison-algebra
   to show that $\mathbb{B}_{p,\varepsilon} $ is absorbent in the realification $\mathrm{E}^\mathbb{R}$. Since $p$ is positively homogenous by \Crefthm:equivalent-characterizations-sublinearity and $0\leq p(v) + p(-v)$ for all $v\in \mathrm{E}$, one concludes that for all $t\in\mathbb{R}$ and $v\in \mathrm{E}$
   
   :::{math}
   |p(tv) | \leq |t|\max\{ p(v),p(-v) \} \ .
   :::
   
   Hence $tv\in \mathbb{B}_{p,\varepsilon}$ if $0 < t < \frac{\varepsilon}{\max\{ p(v),p(-v) \} +1}$, and $\mathbb{B}_{p,\varepsilon}$ is absorbent in $\mathrm{E}^\mathbb{R}$.
:::



:::{prf:definition} 
If $p :\mathrm{E} \to \mathbb{R}$ is a seminorm on a vector space $\mathrm{E}$, we denote for every $v \in \mathrm{E}$ and $\varepsilon > 0$ by $\mathbb{B}_{p,\varepsilon} (v)$ the (*open*) $\varepsilon$-*ball associated with* $p$ and
*with center* $v$ that is the set

:::{math}
\mathbb{B}_{p,\varepsilon} (v) = \big\{ w \in \mathrm{E} \bigm\vert p(w-v) < \varepsilon \big\} \ .
:::

The *closed* $\varepsilon$-*ball associated with* $p$ and *with center* $v$ is defined as

:::{math}
\overline{\mathbb{B}}_{p,\varepsilon} (v) = \big\{ w \in \mathrm{E} \bigm\vert p(w-v) \leq \varepsilon \big\} \ .
:::

The positive number $\varepsilon$ is called the *radius* of the ball. In case the center of the ball is the origin, we often write $\mathbb{B}_{p,\varepsilon}$ and $\overline{\mathbb{B}}_{p,\varepsilon}$ for $\mathbb{B}_{p,\varepsilon} (0)$ and $\overline{\mathbb{B}}_{p,\varepsilon} (0)$, respectively. If in addition the radius equals $1$, then we usually write only $\mathbb{B}_{p}$ and $\overline{\mathbb{B}}_{p}$ and call these sets the *open* respectively the
*closed unit ball*. More generally, for the particular radius $1$ we denote the corresponding balls by $\mathbb{B}_p (v)$ and $\overline{\mathbb{B}}_p (v)$ and call them the *open* respectively
*closed* *unit balls with center* $v$. When by the context it is clear which seminorm $p$ a ball is associated with we often do not mention $p$ explicitely. This is in particular the case when the underlying vector space is a normed vector space.

If $P$ is a finite set or a finite family of seminorms on $\mathrm{E}$ we define the
*open* and *closed* $\varepsilon$-*multiballs with center* $v$ by

:::{math}
\mathbb{B}_{P,\varepsilon} (v) =
\big\{ w \in \mathrm{E}\bigm\vert p(w-v) < \varepsilon \text{ for all } p\in P\big\}
:::

and

:::{math}
\overline{\mathbb{B}}_{P,\varepsilon} (v) = \big\{ w \in \mathrm{E} \bigm\vert p(w-v) \leq \varepsilon
\text{ for all } p\in P \big\} \ ,
:::

respectively. As before, we abbreviate $\mathbb{B}_{P,\varepsilon} = \mathbb{B}_{P,\varepsilon} (0)$ and $\overline{\mathbb{B}}_{P,\varepsilon} = \overline{\mathbb{B}}_{P,\varepsilon} (0)$.
:::



:::{prf:remark} 
For convenience, we will also use the symbols $\mathbb{B}_{p,\varepsilon}$ and $\overline{\mathbb{B}}_{p,\varepsilon}$ to denote the sets $\big\{ v \in \mathrm{E} \bigm\vert p(v) < \varepsilon \big\}$ and $\big\{ v \in \mathrm{E} \bigm\vert p(v) \leq \varepsilon \big\}$, respectively, when $p:\mathrm{E} \to \mathbb{R}$ is just a real-valued convex map on the vector space $\mathrm{E}$. Note that for such a $p$ the set $\big\{ v \in \mathrm{E} \bigm\vert p(v) < 0 \big\}$ might be non-empty. But as we have shown in
\Crefthm:properties-subadditive-convex-real-valued-maps-vector-space
the sets $\mathbb{B}_{p,\varepsilon}$ and $\overline{\mathbb{B}}_{p,\varepsilon} $ associated to a convex $p$ share with the the balls associated to a seminorm several nice properties like convexity.
:::



:::{prf:proposition} 
:label: thm:convexity-balls-seminorms_1
Let $\mathrm{E}$ be a $\mathbb{K}$-vector space, and $P$ a finite set of seminorms on $\mathrm{E}$. Then, for every $\varepsilon > 0$ and $v\in \mathrm{E}$, the $\varepsilon$-multiballs $\mathbb{B}_{P,\varepsilon} (v)$ and $\overline{\mathbb{B}}_{P,\varepsilon} (v)$ are convex. The $\varepsilon$-multiballs $\mathbb{B}_{P,\varepsilon}$ and $\overline{\mathbb{B}}_{P,\varepsilon}$ centered at the origin are absolutely convex and absorbent.
:::


:::{prf:proof}

Axiom {ref}`axiom:norm-absolute-homogeneity_1` immediately entails that $\mathbb{B}_{P,\varepsilon}$ and $\overline{\mathbb{B}}_{P,\varepsilon}$ are circled. Axiom {ref}`axiom:norm-subadditivity_1`
together with {ref}`axiom:norm-absolute-homogeneity_1` entails that the sets $\mathbb{B}_{P,\varepsilon} (v)$ and $\overline{\mathbb{B}}_{P,\varepsilon} (v)$ are convex. Namely, if $w_1, w_2 \in \mathbb{B}_{P,\varepsilon} (v)$ and $t \in [0,1]$, then one has for all seminorms $p\in P$

:::{math}
p\left( tw_1 + (1-t) w_2 - v \right) \leq t \, p \left( w_1 - v \right) + (1-t) \, p \left( w_2 - v \right) < t \, \varepsilon + (1-t) \, \varepsilon = \varepsilon
:::

and likewise $p\left( tw_1 + (1-t) w_2 - v \right) \leq \varepsilon$ for all $w_1, w_2 \in \overline{\mathbb{B}}_{P,\varepsilon}(v)$ and $p\in P$.

Now let $v\in \mathrm{E}$ and $\varepsilon > 0$ be given. Put $t_p = \frac{p(v)+1}{\varepsilon}$ for every $p\in P$ and $t_0 = \max \{t_p\mid p\in P\}$. Then one has for all $t\in \mathbb{K}$ with $|t|\geq t_0$ and for all $p\in P$

:::{math}
p\left( \frac{1}{t} v \right) \leq \frac{\varepsilon}{p(v)+1} \, p(v) < \varepsilon \ ,
:::

hence $v \in t \, \mathbb{B}_{P,\varepsilon}$. So $\mathbb{B}_{P,\varepsilon}$ is absorbing. Since $\overline{\mathbb{B}}_{P,\varepsilon}$ contains the absorbing set $\mathbb{B}_{P,\varepsilon}$, it is absorbing as well.
:::



:::{prf:theorem} 
Assume to be given a set $Q$ of seminorms on a vector space $\mathrm{E}$. Let $\mathscr{P}_{fin}(Q)$ be the collection of all finite subsets of $Q$. A base of a topology on $\mathrm{E}$ then is given by

:::{math}
\mathscr{B} = \big\{ \mathbb{B}_{P,\varepsilon} (v) \bigm\vert P \in \mathscr{P}_{fin}(Q) , \: v \in \mathrm{E} , \: \varepsilon > 0 \big\} \ .
:::

The topology $\mathscr{T}$ generated by $\mathscr{B}$ is called the topology *generated*, *induced* or *defined* by $Q$. Moreover, $\mathscr{T}$ is a locally convex vector space topology on $\mathrm{E}$. It coincides with the coarsest translation invariant topology on $\mathrm{E}$ such that each seminorm in $Q$ is continuous.
:::



:::{prf:proof}

Consider the set $\mathscr{B}_0$ of all multiballs $\mathbb{B}_{P,\varepsilon}$ with $P \in \mathscr{P}_{fin}(Q)$ and $\varepsilon > 0 $ centered at the origin. Clearly, $\mathscr{B}_0$ is a filter base since for $P_1,P_2 \in \mathscr{P}_{fin}(Q)$ and $\varepsilon_1,\varepsilon_2 > 0 $ the multiball $\mathbb{B}_{P_1\cup P_2, \min\{ \varepsilon_1,\varepsilon_2\}}$ is contained in $\mathbb{B}_{P_1,\varepsilon_1}\cap \mathbb{B}_{P_2,\varepsilon_2}$. Moreover it consists of absolutely convex and absorbing sets by \Crefthm:convexity-balls-seminorms.

By a similar argument one shows that $\mathscr{B}$ is base of a topology. Let $\mathbb{B}_{P_1,\varepsilon_1} (v_1), \mathbb{B}_{P_2,\varepsilon_2} (v_2) \in \mathscr{B}$ and $v \in \mathbb{B}_{P_1,\varepsilon_1}(v_1)\cap \mathbb{B}_{P_2,\varepsilon_2}(v_2)$. Let $\varepsilon$ be the minium of the numbers $\varepsilon_1 - p_1 (v-v_1)$ and $\varepsilon_2 - p_2 (v-v_2)$, where $p_1$ runs through the elements of $P_1$ and $p_2$ through the ones of $P_2$. Then $\varepsilon > 0$ and $\mathbb{B}_{P_1\cup P_2, \varepsilon}(v)
\subset\mathbb{B}_{P_1,\varepsilon_1}(v_1)\cap\mathbb{B}_{P_2,\varepsilon_2}(v_2)$, and $\mathscr{B}$ is a base for a topology $\mathscr{T}$ indeed. By construction, $\mathscr{B}_0$ then is a base for the filter of zero neighborhoods and each element of $\mathscr{B}_0$ is open in $\mathscr{T}$. Moreover, each closed multiball $\overline{\mathbb{B}}_{P,\varepsilon} (v)$ is closed in $\mathscr{T}$ since the complement $\mathrm{E}\setminus \overline{\mathbb{B}}_{P,\varepsilon} (v)$ contains with $w$ also the open multiball $\mathbb{B}_{P,\delta} (w)$, where $\delta = \min \{ p(v-w) - \varepsilon| p\in P\}$.

We now prove continuity of addition with respect to $\mathscr{T}$. Let $v_1,v_2\in \mathrm{E}$, $P \in \mathscr{P}_{fin}(Q)$, and $\varepsilon > 0$. Since the triangle inequality holds for every seminorm in $F$, one has

:::{math}
\mathbb{B}_{P,\frac\varepsilon 2} (v_1) + \mathbb{B}_{P,\frac\varepsilon 2} (v_2)
\subset \mathbb{B}_{P,\varepsilon}(v_1+v_2) \ ,
:::

which entails continuity of addition at each $(v_1,v_2) \in \mathrm{E} \times \mathrm{E}$. Next consider multiplication by scalars and let $\lambda \in \mathbb{K}$ and $v\in \mathrm{E}$. Again let $P= \{ p_1,\ldots, p_n\} \in \mathscr{P}_{fin}(Q)$ and $\varepsilon > 0$. Let $C_1 = \sup \{ p_j (v) \mid 1\leq j \leq n\} + 1$, $C_2 = |\lambda| + 1$ and put $\delta_1 = \min \{1,\frac{\varepsilon}{2 \, C_1} \}$ and $\delta_2 = \frac{\varepsilon}{2 \, C_2}$. Then one obtains by absolute homogeneity and subadditivity of each seminorm

:::{math}
p_j ( \mu w -\lambda v) \leq | \mu | \, p_j( w-v) + | \mu -\lambda| \, p_j(v) \quad \text{for all }
\mu \in \mathbb{K} \text{ and } w \in \mathrm{E},
:::

hence

:::{math}
\mathbb{B}_{\delta_1} (\lambda ) \cdot \mathbb{B}_{P,\delta_2} (v) \subset
\mathbb{B}_{P,\varepsilon} (\lambda \cdot v ) \ ,
:::

where $\mathbb{B}_{\delta_1} (\lambda) = \{ \mu \in \mathbb{K} \mid |\mu -\lambda| < \delta_1\} $. This shows continuity of scalar multiplication at each $(\lambda,v) \in \mathbb{K} \times \mathrm{E}$, and $\mathscr{T}$ is a vector space topology.

Since each of the base elements $\mathbb{B}_{P,\varepsilon}\in \mathscr{B}_0$ is convex, Axiom \hyperref[axiom:tvs-local-convexity]LCVS holds true as well and the topology $\mathscr{T}$ is locally convex.

Every seminorm $p\in Q$ is continuous with respect to the topology $\mathscr{T}$ since for all $a < b$ the preimage $p^{-1} ( {\ltsbrak a,b \rtsbrak} ) = \mathbb{B}_{p,b} \setminus \overline{\mathbb{B}}_{p,a}$ is open in $\mathscr{T}$. Now let $\mathscr{T}'$ be a translation invariant topology on $\mathrm{E}$ for which every seminorm $p\in Q$ is continuous. In that topology $\mathscr{B}_0$ is a set of zero neighborhoods. As shown before, every element $B\in \mathscr{B}_0$ is absolutely convex, absorbing and satisfies $\frac 12 B + \frac 12 B \subset B$. Hence by \Crefthm:filter-base-absorbing-absolutely-convex-sets-generating-locally-convex-topology
the topology $\mathscr{T}'$ is finer than the locally convex topology generated by $\mathscr{B}_0$. But the latter topology coincides with $\mathscr{T}$ by construction. This shows the last part of the claim and the proof is finished.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Seminorms and induced vector space topologies -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXGauge functionals and induced seminormsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Gauge functionals and induced seminorms -->
## Gauge functionals and induced seminorms
\para As we have seen, any vector space with a topology defined by a family of seminorms on it is a locally convex topological vector space. The converse also holds true. The fundamental notion needed for the proof of this is the following.


:::{prf:definition} 
Let $\mathrm{E}$ be a vector space and $A \subset \mathrm{E}$ absorbent. Then the map

:::{math}
p_A : \mathrm{E} \to \mathbb{R}_{\geq 0} , \: v \mapsto p_A (v)= \inf \big\{ t \in \mathbb{R}_{ > 0} \bigm\vert v \in t A \big\}
:::

is called the *gauge functional*, the *Minkowski functional* or the *Minkowski gauge*
of $A$.
:::



:::{prf:remark} 
By definition of an absorbent set, $\big\{ t \in \mathbb{R}_{ > 0} \bigm\vert v \in t A \big\}$ is non-empty whenever $A\subset \mathrm{E}$ is absorbent. Hence $p_A$ is well-defined for such $A$.
:::



:::{prf:proposition} 
:label: thm:properties-gauge-functional-absorbent-set_1
The Minkowski gauge $p_A :\mathrm{E} \to \mathbb{R}_{\geq 0}$ of an absorbent subset $A$ of a vector space $\mathrm{E}$ has the following properties.



(ite:gauge-functional-positively-homogenous_1)=
(i)
: The gauge functional is positively homogeneous that is $p_A (t v) = t\, p_A(v)$ for all $t\in \mathbb{R}_{ > 0}$ and all $v\in \mathrm{E}$.

(ite:gauge-functional-subadditivity_1)=
(ii)
: If $A$ is convex, then $p_A$ is subadditive and
   
   :::{math}
   \mathbb{B}_p (v)= \bigcup_{0 < t < 1} tA \subset A \subset
   \bigcap_{1 < t} tA = \overline{\mathbb{B}}_p (v) \ .
   :::

(ite:gauge-functional-seminorm_1)=
(iii)
: If $A$ is absolutely convex, then $p_A$ is a seminorm on $\mathrm{E}$.
:::



:::{prf:proof}

If $t > 0$, then $tv \in sA$ for some $s > 0$ if and only if $v \in \frac st A$. Hence $\big\{ s \in \mathbb{R}_{ > 0} \bigm\vert t v \in s A \big\}$ and $t \big\{ s \in \mathbb{R}_{ > 0} \bigm\vert v \in s A \big\}$ coincide for all $t > 0$, so {ref}`ite:gauge-functional-positively-homogenous_1` follows.

Assume that $A$ is convex. Let $v,w\in \mathrm{E}$ and $\varepsilon > 0$. Then there exist $t > p_A(v)$ and $s > p_A(w)$ such that $v \in tA$, $w\in sA$, $t < p_A(v) +\frac \varepsilon 2$ and $s < p_A(w) +\frac \varepsilon 2$. By convexity of $A$ and
\Crefthm:weighted-sum-convex-absolutely-convex-sets, $v+w \in tA+ sA = (t+s)A$. Hence $p_A(v+w) \leq (t+s) < p_A(v) + p_A (w) + \varepsilon$. Since $\varepsilon > 0$ was arbitrary, $p_A(v+w) \leq p_A(v) + p_A (w)$ and $p_A$ is subadditive. If $v \in tA$ for some $t$ with $0 < t < 1$, then $p_A(v) \leq t < 1$ by definition. Conversely, if $p_A(v) < 1$, then there exists a $t > 0$ such that $t < 1$ and $v \in tA$. Hence the equality $\mathbb{B}_p (v) = \bigcup_{0 < t < 1} tA$ follows. Since $A$ is absorbing, $0$ is an element of $A$. By convexity of $A$ one therefore concludes $tA = (1-t) \{ 0 \} + tA \subset A$ whenever $0 < t < 1$. For $t > 1$ this shows $\frac 1t A \subset A$, hence $A \subset tA$. So the relation $\bigcup_{0 < t < 1} tA \subset A \subset \bigcap_{1 < t} tA$ is proved. Now assume that $v \in tA$ for all $t > 1$. Then $p_A(v)\leq 1$ by definition. If conversely $p_A(v)\leq 1$, then there exists for each $\varepsilon > 0$ an $s\geq 0$ such that $p_A(v) \leq s$, $v \in sA$ and $s < 1 +\varepsilon$. Hence, for $t\geq 1 +\varepsilon$ by \Crefthm:weighted-sum-convex-absolutely-convex-sets
and $0\in A$,

:::{math}
v \in sA = s A + (t-s) \{0\} \subset s A + (t-s) A = tA \ .
:::

Since $\varepsilon > 0$ was arbitrary, $v \in tA$ for all $t > 1$ follows. So one obtains the equality $\bigcap_{1 < t} tA = \overline{\mathbb{B}}_p (v)$, and {ref}`ite:gauge-functional-subadditivity_1` is proved.

To verify {ref}`ite:gauge-functional-seminorm_1` recall that $A$ is circled whenever $A$ is absolutely convex. This entails for $r\in \mathbb{K}$, $v\in \mathrm{E}$ and absolutely convex $A$

:::{math}
p_A (rv)= \inf \big\{ t \in \mathbb{R}_{ > 0} \bigm\vert r v \in tA \big\} =
\inf \big\{ t \in \mathbb{R}_{ > 0} \bigm\vert |r|v \in t A \big\} = p_A (|r|v) = |r| p_A(v) \ ,
:::

where for the last equality we have used {ref}`ite:gauge-functional-positively-homogenous_1`.
:::



:::{prf:lemma} 
Let $A$ and $B$ be absorbent subsets of a vector space $\mathrm{E}$. Then the following holds true.



(i)
: $p_{tA}(v) = p_A(t^{-1} v)$ for all $t\in \mathbb{K}^\times$ and $v\in \mathrm{E}$.

(ite:comparison-gauge-functionals-subsets_1)=
(ii)
: If $B\subset A$, then $p_A \leq p_B$.

(iii)
: If $A$ is convex, then $v \in tA$ for all $v\in \mathrm{E}$ and $t > p_A(v)$.

(iv)
: If $A$ and $B$ are convex, then the intersection $A\cap B$ is absorbent and convex and $p_{A\cap B} = \sup \{ p_A,p_B\}$, where $\sup \{ p_A,p_B\} (v) = \sup \{ p_A (v) ,p_B (v) \}$ for all $v\in \mathrm{E}$.
:::



:::{prf:proof}



\itemindent
: If $t\in \mathbb{K}$ is invertible, then $v \in tA$ if and only if $t^{-1}v \in A$.

\itemindent
: Let $v\in \mathrm{E}$ and $\varepsilon > 0$. Then there exists $t$ with $p_B(v) \leq t < p_B(v) + \varepsilon$ such that $v \in tB$. By $B\subset A$ this implies $v \in tA$, hence $p_A(v) \leq t < p_B(v) + \varepsilon$. Since $\varepsilon > 0$ was arbitrary, the estimate $p_A \leq p_B$ follows.

\itemindent
: By definition of the Minkowski gauge there exists $s \in \mathbb{R}$ such that $p_A(v) < s < t$ and $v \in sA$. By convexity of $A$ one concludes $\frac st v = \frac st v + \left( 1 - \frac st \right) \cdot 0 \in sA$, hence $v \in tA$.

\itemindent
: The intersection of convex sets is convex, so $A\cap B$ is convex. Let $v\in \mathrm{E}$ and choose $r_A\geq 0$ and $r_B\geq 0$ such that $v \in tA$ for all $t\geq r_A$ and $v \in sB $ for all $s\geq r_B$. Then $v \in (tA)\cap (tB) = t(A\cap B) $ for all $t\geq \max\{r_A,r_B\}$, so $A\cap B$ is absorbent. One has $p_{A\cap B} \geq \sup \{ p_A,p_B\}$ by {ref}`ite:comparison-gauge-functionals-subsets_1`. To show the converse inequality assume that $v \in \mathrm{E}$ and $t > \sup \{ p_A (v) ,p_B (v)\}$. Then $v \in tA \cap tB = t(A\cap B)$, which implies $p_{A\cap B} (v)\leq t$. Hence $p_{A\cap B} (v) \leq \sup \{ p_A (v) ,p_B (v)\}$ since $t > \sup \{ p_A (v) ,p_B (v)\}$ was arbitrary.
:::



:::{prf:lemma} 
Let $p:\mathrm{E} \to\mathbb{R}$ be a sublinear map on a vector space $\mathrm{E}$ and $A\subset \mathrm{E}$ convex. If

:::{math}
\mathbb{B}_p \subset A \subset \overline{\mathbb{B}}_p \ ,
:::

then the gauge functional $p_A$ coincides with $\sup \{p,0\} $. If $p$ is even a seminorm, then $p=p_A$.
:::



:::{prf:proof}

Let $p:\mathrm{E}\to\mathbb{R}$ be sublinear. Observe that then $\mathbb{B}_p$ is absorbent by
\Crefthm:properties-subadditive-convex-real-valued-maps-vector-space
{ref}`ite:implications-sublinearity-real-valued-map_1`. Hence $A$ must also be absorbent by assumption, so the associated Minkowski gauge $p_A$ is positively homogeneous by
\Crefthm:properties-gauge-functional-absorbent-set
{ref}`ite:gauge-functional-positively-homogenous_1`.

Assume now that there exists $v\in\mathrm{E}$ such that $\max\{p(v),0 \} < p_A(v)$. By positive homogeneity of $p$ and $p_A$ one can achive by possibly multiplying $v$ by a positive real number that $\max\{p(v),0 \} < 1 < p_A(x)$. The first inequality entails $v \in \mathbb{B}_p$, the second $v\notin \overline{\mathbb{B}}_p $ which is a contradiction. Next assume that there exists $v\in\mathrm{E}$ with $p_A(v) < \max\{p(v),0 \}$. As before one can then achieve that $ p_A(v) < 1 < \max\{p(v),0 \}$ for some $v\in\mathrm{E}$. By the first inequality one concludes $v \in A$, by the second $v \notin A$. This is a contradiction. So the equality $\max\{p(v),0 \} = p_A(v)$ holds for all $v\in \mathrm{E}$.

In case $p$ is a seminorm, then $p(v) \geq 0$ for all $v\in \mathrm{E}$ and the second claim follows by the first.
:::



:::{prf:proposition} 
Let $\mathrm{E}$ be a topological vector space, and $p:\mathrm{E} \to \mathbb{R}$ be sublinear. Then the following are equivalent.



(ite:continuity-sublinear-map-origin_1)=
(i)
: The map $p$ is continuous in the origin.

(ite:uniform-continuity-sublinear-map_1)=
(ii)
: The map $p$ is uniformly continuous.

(ite:continuity-sublinear-map_1)=
(iii)
: The map $p$ is continuous.

(ite:unit-ball-sublinear-map-zero-neighborhood_1)=
(iv)
: The unit ball $\mathbb{B}_p $ is a zero neighborhood.
:::



:::{prf:proof}

Let us first show {ref}`ite:continuity-sublinear-map-origin_1` $\implies$ {ref}`ite:uniform-continuity-sublinear-map_1`. To this end fix $\varepsilon > 0$. By assumption there exists a zero neighborhood $V\subset \mathrm{E}$ such that $|p(v)| < \varepsilon$ for all $v\in V$. By possibly passing to $V \cap (-V)$ one can assume that $V$ is symmetric.
\Crefthm:properties-subadditive-convex-real-valued-maps-vector-space {ref}`ite:implications-subadditivity_1`
now implies

:::{math}
| p(v) - p(w)| < \varepsilon \quad \text{for all } v,w \in V \ .
:::

Hence $p$ is uniformly continuous. The implications {ref}`ite:uniform-continuity-sublinear-map_1` $\implies$ {ref}`ite:continuity-sublinear-map_1`
and {ref}`ite:continuity-sublinear-map_1` $\implies$ {ref}`ite:unit-ball-sublinear-map-zero-neighborhood_1` are trivial. It remains to prove
{ref}`ite:unit-ball-sublinear-map-zero-neighborhood_1` $\implies$ {ref}`ite:continuity-sublinear-map-origin_1`. Assume that $\mathbb{B}_p (0,1)$ is a zero neighborhood. Then there exists a symmetric zero neighborhood $V$ contained in $\mathbb{B}_p (0,1)$. Since $p(0)=0$ one concludes by
\Crefthm:properties-subadditive-convex-real-valued-maps-vector-space {ref}`ite:implications-subadditivity_1`

:::{math}
| p(v) | < \max \{ p(v), p(-v )\} < 1 \quad \text{for all } v \in V \ .
:::

But this implies $|p(v)| < \varepsilon $ for all $v \in \varepsilon V$ and $\varepsilon > 0$, so $p$ is continuous at the origin.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Gauge functionals and induced seminorms -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXNormabilityXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Normability -->
## Normability
:::{prf:definition} 
A topological vector space $\mathrm{E}$ is called *seminormable* if its topology is generated by a single seminorm $p:\mathrm{E}\to \mathbb{R}_{\geq 0}$. If the topology on $\mathrm{E}$ coincides with the vector space topology generated by a norm $\|\cdot\|$, then one calls $\mathrm{E}$ *normable*.
:::



:::{prf:theorem} Kolmogorov's normability criterion
A topological vector space $\mathrm{E}$ is normable if and only if it is a {ref}`axiom:t1_1` space and possesses a bounded convex neighborhood of the origin.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Normability -->

<!-- XXSEC_PREFIX_ENDXX\sectionSeminorms and gauge functionals -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXCauchy filters and completenessXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionCauchy filters and completeness -->
(sec:cauchy-filters-completeness_1)=
# Cauchy filters and completeness

<!-- XXSEC_PREFIX_ENDXX\sectionCauchy filters and completeness -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXFunction spaces and their topologiesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionFunction spaces and their topologies -->
(sec:function-spaces-topologies_1)=
# Function spaces and their topologies
:::{prf:proposition} 
:label: thm:metric-structure-space-bounded-maps_1
Let $X$ be a topological space and $(Y,d)$ a metric space. Then the following holds true.



(ite:metric-space-bounded-maps_1)=
(i)
: The space
   
   :::{math}
   \mathscr{B} (X,Y) = \big\{ f : X \to Y \bigm\vert
   \exists y_0\in Y \, \exists C > 0 \, \forall x\in X : \: d\big(f(x),y_0\big) \leq C\big\}
   :::
   
   of bounded functions from $X$ to $Y$ is a metric space with metric
   
   :::{math}
   \varrho : \mathscr{B} (X,Y) \times \mathscr{B} (X,Y) \to \mathbb{R}_{\geq 0} , \: (f,g) \mapsto
   \sup_{x\in X} d\big( f(x),g(x)\big) \ .
   :::

(ite:completeness-space-bounded-maps-range-complete-metric-space_1)=
(ii)
: If $(Y,d)$ is complete, then $(\mathscr{B} (X,Y),\varrho)$ is so, too.

(ite:closedness-bounded-continuous-functions-space-bounded-functions_1)=
(iii)
: The space
   
   :::{math}
   \mathscr{C}_{b} (X,Y) = \mathscr{C} (X,Y) \cap \mathscr{B} (X,Y)
   :::
   
   of continuous bounded functions from $X$ to $Y$ is a closed subspace of $\mathscr{B} (X,Y)$.
:::


:::{prf:proof}

Note first that by the triangle inequality there exists for every $f\in \mathscr{B} (X,Y)$ and $y\in Y$ a real number $C_{f,y} > 0$ such that

:::{math}
d\big(f(x),y\big) \leq C_{f,x} \quad \text{for all } x\in X \ .
:::




\itemindent
: Before verifying the axioms of a metric for $\varrho$ we need to show that $\varrho$ is well-defined meaning that $\sup_{x\in X} d\big( f(x),g(x)\big) < \infty$ for all $f,g \in \mathscr{B} (X,Y)$. To this end fix some $y\in Y$ and observe using the triangle inequality that
   
   :::{math}
   d\big( f(x),g(x)\big) \leq d\big( f(x), y\big) + d\big( y, g(x)\big)
   \leq C_{f,y} + C_{g,y} \quad \text{for all } x \in X \ .
   :::
   
   Since furthermore $d\big( f(x),g(x)\big) \geq 0$ for all $x\in X$, the map $\varrho$ is well-defined indeed with image in $\mathbb{R}_{\geq 0}$. If $\varrho (f,g) = 0$, then $d \big( f(x),g(x) \big)=0$ for all $x\in X$, hence $f=g$. Obviously, $\varrho$ is symmetric since $d$ is symmetric. Finally, let $f,g,h\in \mathscr{B} (X,Y)$ and check using the triangle inequality for $d$:
   
   :::{math}
   \begin{split}
   \varrho (f,g) & = \sup_{x\in X} d\big( f(x),g(x)\big) \leq
   \sup_{x\in X} \left( d\big( f(x),h (x)\big) + d\big( h(x),g(x)\big)\right) \leq \\ & \leq \sup_{x\in X} d\big( f(x),h (x)\big) + \sup_{x\in X} d\big( h(x),g(x)\big) = d(f,h) + d(h,g) \ .
   \end{split}
   :::
   
   Hence $\varrho$ is a metric.

\itemindent
: Assume $(Y,d)$ to be complete and let $(f_n)_{n\in\mathbb{N}}$ be a Cauchy sequence in $\mathscr{B} (X,Y)$. Let $\varepsilon > 0$ and choose $N_\varepsilon \in \mathbb{N}$ so that
   
   :::{math}
   \varrho (f_n,f_m) < \varepsilon \quad \text{for all } n,m\geq N \ .
   :::
   
   Then for every $x\in X$ the relation
   
   :::{math}
   :label: eq:cauchy-sequence-relation-values_1
   d\big(f_n(x),f_m(x)\big) < \varepsilon \quad \text{for all } n,m\geq N_\varepsilon
   :::
   
   holds true, so $(f_n(x))_{n\in \mathbb{N}}$ is a Cauchy sequence in $Y$. By completeness of $(Y,d)$ it has a limit which we denote by $f(x)$. By passing to the limit $m\to \infty$ in {eq}`eq:cauchy-sequence-relation-values_1`
   one obtains that
   
   :::{math}
   :label: eq:limit-relation-values_1
   d\big(f(x),f_n(x)\big) \leq \varepsilon \quad \text{for all } x \in X \text{ and } n \geq N_\varepsilon \ .
   :::
   
   Using the triangle inequality one infers from this for an element $y\in Y$ which we now fix that
   
   :::{math}
   d\big(f(x),y )\big) \leq d\big(f(x),f_{N_1}(x))\big) + d\big(f_{N_1}(x),y \big) \leq 1 + C_{f_{N_1},y} \ .
   :::
   
   Hence $f$ is a bounded function. Moreover, {eq}`eq:limit-relation-values_1` entails that
   
   :::{math}
   \varrho (f,f_n) = \sup_{x\in X} d\big(f(x),f_n(x)\big) \leq \varepsilon
   \quad \text{for all } n \geq N_\varepsilon \ ,
   :::
   
   so $(f_n)_{n\in \mathbb{N}}$ converges to $f$.

\itemindent
: We have to show that the limit $f$ of a sequence $(f_n)_{n\in}$ of functions $f_n \in \mathscr{C}_{b} (X,Y)$ which converges in $(\mathscr{B} (X,Y),\varrho)$ has to be continuous. To this end let $\varepsilon > 0$ and choose $N_\varepsilon \in \mathbb{N}$ so that
   
   :::{math}
   \varrho (f_n,f) < \frac{\varepsilon}{3} \quad \text{for all } n \geq N_\varepsilon \ .
   :::
   
   Let $x_0\in X$. By continuity of $f_{N_\varepsilon}$ there exists a neighborhood $U\subset X$ of $x$ so that
   
   :::{math}
   d\big(f_{N_\varepsilon} (x),f_{N_\varepsilon}(x_0)\big) < \frac{\varepsilon}{3} \quad \text{for all } x\in U \ .
   :::
   
   By the triangle inequality one concludes that
   
   :::{math}
   d\big(f (x),f(x_0)\big) \leq d\big(f(x),f_{N_\varepsilon}(x)\big) + d\big(f_{N_\varepsilon} (x),f_{N_\varepsilon}(x_0)\big) + d\big(f_{N_\varepsilon} (x_0),f(x_0)\big) < \varepsilon
   :::
   
   for all $x\in U$. Hence $f$ is continuous at $x_0$. Since $x_0\in X$ was arbitrary $f$, is a continuous map, hence an elemnt of $\mathscr{C}_{b} (X,Y)$.

\mbox
:::



:::{prf:proposition} 
Let $X$ be a topological space and $\mathbb{K}$ the division algebra of real or complex numbers or of quaternions. Then the following holds true.



(i)
: The space $\mathscr{B} (X,\mathbb{K})$ of bounded $\mathbb{K}$-valued functions on $X$ can be expressed as
   
   :::{math}
   :label: eq:algebra-bounded-functions-values-real-complex-numbers-quaternions_1
   \mathscr{B} (X,\mathbb{K}) =
   \big\{ f : X \to \mathbb{K} \bigm\vert
   \exists C > 0 \, \forall x\in X :\: |f(x)| \leq C \big\} \ .
   :::
   
   It carries the structure of a $\mathbb{K}$-algebra by pointwise addition and multiplication of functions and becomes a Banach algebra when equipped with the *supremums-norm*
   
   :::{math}
   \| \cdot \|_\infty : \: \mathscr{B} (X,\mathbb{K}) \to \mathbb{K},\quad f \mapsto \sup_{x\in X} |f(x)| \ .
   :::

(ii)
: The subspace $\mathscr{C}_{b} (X,\mathbb{K}) \subset \mathscr{B} (X,\mathbb{K})$ of bounded continuous $\mathbb{K}$-valued functions on $X$ is a closed subalgebra of $\big( \mathscr{B} (X,\mathbb{K}) , \| \cdot \|_\infty\big)$, so a Banach algebra as well when endowed with the supremums-norm. For $X$ compact this means in particular that the algebra $\big( \mathscr{C} (X,\mathbb{K}), \| \cdot \|_\infty\big)$ is a Banach algebra.
:::



:::{prf:proof}

Eq.~{eq}`eq:algebra-bounded-functions-values-real-complex-numbers-quaternions_1` is obvious since the distance of two elements $a,b\in \mathbb{K}$ is given by $d(a,b) = |a-b|$, so in particular $d(a,0) = |a|$. Let $f,g \in \mathscr{B} (X,\mathbb{K})$ and choose $C_f,C_g \geq 0$ so that $ |f(x)| \leq C_f $ and $ |g(x)| \leq C_g $ for all $x \in X$. Then, by the triangle inequality and absolute homogeneity of the absolute value,

:::{math}
| f(x) + g (x)| \leq C_f + C_g , \quad | a\, f(x) | \leq |a| \, C_f , \quad \text{and} \quad | f(x) \cdot g (x)| \leq C_f \cdot C_g \ .
:::

Hence the sum and the product of two bounded functions are bounded and so is any scalar multiple of a bounded function. Therefore, $\mathscr{B} (X,\mathbb{K})$ is an algebra over $\mathbb{K}$. Using the triangle inequality and absolute homogeneity of the absolute value again one verifies that $ \|f \|_\infty$ is a norm on $\mathscr{B} (X,\mathbb{K})$ indeed and that it fulfills $\|fg \|_\infty\leq \|f \|_\infty \cdot \|g \|_\infty$ for all $f,g \in \mathscr{B} (X,\mathbb{K})$. Furthermore, by definition, $ \|f \|_\infty = \varrho (f,0)$ for all $f \in \mathscr{B} (X,\mathbb{K})$, where $\varrho$ is defined as in \Crefthm:metric-structure-space-bounded-maps. Since $(\mathscr{B} (X,\mathbb{K}),\varrho) $ is a complete metric space, $(\mathscr{B} (X,\mathbb{K}),\|\cdot \|_\infty)$ therefore is a Banach algebra. This proves the first claim.

For the second observe that for $f, g \in \mathscr{C}_{b} (X,\mathbb{K})$ and $a\in \mathbb{K}$ the sum $f+g$, the scalar multiple $af$, and the product $f\cdot g$ are elements of $\mathscr{C}_{b} (X,\mathbb{K})$ again. To verify this let $x\in X$ and $\varepsilon > 0$. Choose neighborhoods $U_1$ and $U_2$ of $x$ so that

:::{math}
| f (y) - f(x) | < \min \left\{\frac{\varepsilon}{2}, \frac{\varepsilon}{|a|+1}, \frac{\varepsilon}{2(|g(x)|+1)} \right\}
\quad \text{for } y\in U_1
:::

and

:::{math}
| g(y) - g(x) | < \left\{1,\frac{\varepsilon}{2},\frac{\varepsilon}{2(|f(x)|+1)} \right\} \quad\text{for } y\in U_2 \ .
:::

Then for all $y\in U_1\cap U_2$

:::{math}
\begin{split}
| (f+g) (y) - (f+g) (x) | & \leq | f (y) - f(x) | + | g (y) - g (x) | < \varepsilon \ , \\ | (af) (y) - (af) (x) | & \leq |a| \cdot | f (y) - f(x) | < \varepsilon \ , \\ | (f\cdot g) (y) - (f\cdot g) (x) | & \leq |g(y)| \cdot | f (y) - f(x) | + |f(x) | \cdot | (g (y) - g (x) | < \varepsilon \ .
\end{split}
:::

This means that $f+g$, $af$ and $fg$ are continuous in $x$, hence elements of $\mathscr{C}_{b} (X,\mathbb{K})$ since $x \in X$ was arbitrary. So $\mathscr{C}_{b} (X,\mathbb{K})$ is a subalgebra of $\mathscr{B} (X,\mathbb{K})$. By \Crefthm:metric-structure-space-bounded-maps one knows that $\mathscr{C}_{b} (X,\mathbb{K})$ is a closed subspace of $\mathscr{B} (X,\mathbb{K})$. The rest of the claim is obvious.
:::


\para As the next step, we introduce seminorms and their topologies on spaces of differentiable functions defined over an open set $\Omega\subset\mathbb{R}^n$. We agree that from now on $\Omega$ will always denote in this section an open subset of $\mathbb{R}^n$. For any differentiability order $m\in \mathbb{N} \cup \{ \infty\}$ the symbol $\mathscr{C}^m (\Omega)$ stands for the space of $m$-times continuously differentiable complex valued functions on $\Omega$. For $i=1,\ldots,n$ we denote by $x^i : \mathbb{R}^n \to \mathbb{R}$ the $i$-th coordinate function and, if $m\geq 1$, by $\partial_i : \mathscr{C}^{m} (\Omega) \to \mathscr{C}^{m-1} (\Omega)$ the operator which maps $f \in \mathscr{C}^m (\Omega)$ to the partial derivative $\frac{\partial f}{\partial x^i}$. More generally, if $\alpha \in \mathbb{N}^n$ is a multiindex satisfying $|\alpha| = \alpha_1+\ldots \alpha_n \leq m$, then we write $\partial^\alpha : \mathscr{C}^{m} (\Omega) \to \mathscr{C}^{m-|\alpha|} (\Omega)$ for the higher order partial derivative which maps $f \in \mathscr{C}^{m} (\Omega)$ to $\frac{\partial^{|\alpha|} f}{\partial x_1^{\alpha_1} \cdot \ldots \cdot \partial x_n^{\alpha_n}}$. Recall that the sum and the product of two $m$-times differentiable functions and scalar multiples of $m$-times differentiable functions are again $m$-times differentiable, hence $\mathscr{C}^{m} (\Omega)$ forms a $\C$-algebra. Now we define $\widebar{\mathscr{C}}^{m} (\Omega)$ to be the space of continuous functions on the closure $\widebar{\Omega}$ which are $m$-times continuosly differentiable on $\Omega$ so that each of its partial derivatives of order $\leq m$ has a continuos extension to $\widebar{\Omega}$. Since the operators $\partial_i$ are linear and also derivations by the Leibniz rule, $\widebar{\mathscr{C}}^{m} (\Omega)$ is a subalgebra of $\mathscr{C}^{m} (\Omega)$. In general, these algebras do not coincide as for example the function $\frac 1x$ on $\mathbb{R}_{ > 0}$ shows. It is an element of $\mathscr{C}^{\infty} (\mathbb{R}_{ > 0})$ but can not be extended to a continuous function on $\mathbb{R}_{\geq 0}$, so is not an element of $\widebar{\mathscr{C}}^{\infty} (\mathbb{R}_{ > 0})$.

If $X \subset \mathbb{R}^n$ is locally closed which means that $X$ is the intersection of an open and a closed susbet of $\mathbb{R}^n$, then define $\mathscr{C}^{m} (X)$ as the quotient space $\mathscr{C}^{m} (\Omega) / \mathscr{J}_{X} (\Omega)$, where $\Omega \subset \mathbb{R}^n$ open is chosen so that $X = \widebar{X} \cap \Omega$ and where $\mathscr{J}_{X}$ denotes the ideal sheaf of all $m$-times continuously differentiable functions vanishing on $X$ that is

:::{math}
\mathscr{J}_{X} (\Omega) = \big\{ f \in \mathscr{C}^{m} (\Omega) \bigm\vert f|_X = 0 \big\} \ .
:::

Using a smooth partition of unity type of argument one shows that $\mathscr{C}^{m} (X)$ does not depend on the particular choice of the neighborhood $\Omega$ in which $X$ is relatively closed and that $\mathscr{C}^{m} (X)$ can be naturally identified with the space of continuous functions on $X$ which have an extension to an element of $\mathscr{C}^{m} (\Omega)$.


:::{prf:proposition} 
Let $\Omega \subset \mathbb{R}^n$ be open and bounded and $m\in \mathbb{N}_{ > 0}$. Then $\widebar{\mathscr{C}}^{m} (\Omega)$ equipped with the norm

:::{math}
\| \cdot \|_{\Omega,m} : \widebar{\mathscr{C}}^{m} (\Omega) \to \mathbb{R}_{\geq 0}, \quad f \mapsto
:::
:::

<!-- XXSEC_PREFIX_ENDXX\sectionFunction spaces and their topologies -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXSummabilityXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionSummability -->
(sec:summability_1)=
# Summability
:::{prf:definition} 
Assume to be given a locally convex topological vector space $\mathrm{V}$ over the field $\mathbb{K}$ of real or complex numbers. Let $(v_i)_{i \in I}$ be a family of elements of $\mathrm{V}$. Let $\mathscr{F} (I)$ be the set of finite subsets of $I$ and note that it is filtered by set-theoretic inclusion. The family $(v_i)_{i \in I}$ then gives rise to the net $\Big( \sum_{i \in J} v_i \Big)_{J \in \mathscr{F}(I)}$. One calls the family $(v_i)_{i \in I}$
*summable* to an element $v \in \mathrm{V}$ if the net $\Big( \sum_{i \in J} v_i \Big)_{J \in \mathscr{F}(I)}$ converges to $v$. In other words this means that for every convex zero neighborhood $U \subset \mathrm{V}$ and $\varepsilon > 0$ there exists an element $J_{U,\varepsilon} \in \mathscr{F} (I)$ such that for all finite sets $J$ with $ J_{U,\varepsilon} \subset J \subset I$

:::{math}
p_U \left( v - \sum_{i \in J} v_i \right) < \varepsilon \ .
:::

As before, $p_U$ denotes here the gauge of $U$. If $\mathrm{V}$ is Hausdorff, the limit $v$ of a summable family $(v_i)_{i \in I}$ is uniquely determined, and one writes in this situation

:::{math}
v = \sum_{i \in I} v_i \ .
:::

We denote the space of summable families in $\mathrm{V}$ over the given index set $I$ by $\ell^1 (I ,\mathrm{V})$. For $E=\C$ we just write $\ell^1 (I )$ instead of $\ell^1 (I ,\C)$. If in addition the index set coincides with $\mathbb{N}$, we briefly denote $\ell^1 (\mathbb{N} )$ by $\ell^1$.
:::



:::{prf:proposition} Cauchy criterion for summability
Let $\mathrm{V}$ be a complete locally convex topological vector space. A family $(v_i)_{i \in I}$ of elements of $\mathrm{V}$ then is summable to some $v\in \mathrm{V}$ if and only if it satisfies the following Cauchy condition:


(C)
: For every convex zero neighborhood $U \subset \mathrm{V}$ and $\varepsilon > 0$ there exists an element $J_{U,\varepsilon} \in \mathscr{F} (I)$ such that for all $K \in \mathscr{F} (I)$ with $ K \cap J_{U,\varepsilon} = \emptyset$ the relation
   
   :::{math}
   p_U \left( \sum_{i \in K} v_i \right) < \varepsilon
   :::
   
   holds true.
:::


:::{prf:proof}

By completeness of $\mathrm{V}$ it suffices to verify that the net $\Big( \sum_{i \in J} v_i \Big)_{J \in \mathscr{F}(I)}$ is a Cauchy net if and only if condition  (C) is satisfied. Recall that one calls $\Big( \sum_{i \in J} v_i \Big)_{J \in \mathscr{F}(I)}$ a Cauchy net if for every convex zero neighborhood $U \subset \mathrm{V}$ all $\varepsilon > 0$ there exists an element $J_{U,\varepsilon} \in \mathscr{F} (I)$ such that for all $J,J' \in \mathscr{F} (I)$ containing $ J_{U,\varepsilon}$ as a subset the relation

:::{math}
p_U \left( \sum_{i \in J} v_i - \sum_{i\in J'} v_i \right) < \varepsilon
:::

holds true. But that is clearly equivalent to condition  (C).
:::


\para Several other notions of summability have been introduced in the analysis and functional analysis literature. These are mainly either used to establish summability criteria or are used in the study of topological tensor products and nuclearity of locally convex topological vector spaces, see [@GroPTTEN; @PieNLCS]. In the following we define these further notions of summability and study their properties. The symbol$\mathrm{V}$ hereby always stands for a locally convex \texttvs, $I$ always denotes a nonempty index set, and $\mathscr{F} (I)$ the set of its finite subsets.


:::{prf:definition} 
A family $(v_i)_{i \in I}$ in $\mathrm{V}$ is called *weakly summable* to $v \in \mathrm{V}$ if for every continuous linear form $\alpha : \mathrm{V} \to \mathbb{K}$ the net $\Big( \sum_{i \in J} \alpha( v_i ) \Big)_{J \in \mathscr{F}(I)}$ converges in $\mathbb{K}$ to $\alpha ( v )$. In other words this means that for every $\alpha \in \mathrm{V}'$ and $\varepsilon > 0$ there exists a finite set $J_{\alpha,\varepsilon} \subset I$ such that for all finite sets $J$ with $J_{\alpha,\varepsilon} \subset J \subset I $

:::{math}
\left| \alpha (v) - \sum_{j\in J} \alpha( v_i ) \right| < \varepsilon \ .
:::

The set of all weakly summable families in $\mathrm{V}$ with index set $I$ is denoted $\ell^1 [I, \mathrm{V}]$.
:::



:::{prf:definition} 
A family $(v_i)_{i \in I}$ in $\mathrm{V}$ is called *absolutely summable* if for every circled convex zero neighborhood $U \subset \mathrm{V}$ there exists some $C\geq 0$ such that

:::{math}
\sum_{i \in J} p_U \left( v_i\right) \leq C \quad \text{for all } J \in \mathscr{F} (I) \ .
:::

We denote the set of all absolutely summable families in $\mathrm{V}$ by $\ell^1 \{ I, \mathrm{V} \}$.
:::



:::{prf:proposition} 
A family $(v_i)_{i \in I} \subset \mathrm{V}$ is absolutely summable if and only if for every element $U$ of a basis of circled convex zero neighborhoods there exists a $C\geq 0$ such that

:::{math}
\sum_{i \in J} p_U \left( v_i\right) \leq C \quad \text{for all } J \in \mathscr{F} (I) \ .
:::
:::





:::{prf:definition} 
A family $(v_i)_{i \in I}$ in $\mathrm{V}$ is called *totally summable* if there exists a bounded absolutely convex subset $B\subset \mathrm{V}$ and a $C\geq 0$ such that

:::{math}
\sum_{i \in J} p_B \left( v_i\right) \leq C \quad \text{for all } J \in \mathscr{F} (I) \ .
:::

We write $\ell^1 \langle I, \mathrm{V} \rangle$ for the set of all totally summable families in $\mathrm{V}$.
:::



<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXSummable families of complex numbersXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Summable families of complex numbers -->
## Summable families of complex numbers
:::{prf:lemma} cf.~[@PieNLCS, Lem.~1.1.2]
Let $(z_i)_{i\in I}$ be a family of complex numbers for which there exists a positive real number $C > 0$ such that

:::{math}
\left|\sum_{i\in J} z_i \right| \leq C \quad \text{for all } J \in \mathscr{F} (I) \ .
:::

Then one has the estimate

:::{math}
\sum_{i\in J}\left| z_i \right| \leq 4 C \quad \text{for all } J \in \mathscr{F} (I) \ .
:::
:::



:::{prf:proof}

We assume first that all $z_i$ are real. Then let $I^+$ the set of all indices $i\in I$ such that $z_i \geq 0$, and $I^-$ the set of all $i\in I$ such that $z_i < 0$. Then, for all finite $J\subset I$

:::{math}
\sum_{i\in J} \left| z_i \right| = \sum_{i\in J\cap I^+} \left| z_i \right| + \sum_{i\in J\cap I^-} \left| z_i \right| = \left| \sum_{i\in J\cap I^+} z_i \right| + \left| \sum_{i\in J\cap I^-} z_i \right| \leq 2 C \ .
:::

In the general case decompose $z_i$ into real and imaginary parts $x_i = \Re z_i$ and $y_i = \Im z_i$. By the triangle inequality one obtains for all finite $J\subset I$

:::{math}
\sum_{i\in J} \left| z_i \right| \leq \sum_{i\in J} \left| x_i \right| + \sum_{i\in J} \left| y_i \right| \leq 4 C \ .
:::
:::



:::{prf:proposition} 
:label: thm:summability-criteria-family-complex-numbers_1
For a family $(z_i)_{i\in I}$ of complex numbers the following are equivalent.



(i)
: The family $(z_i)_{i\in I}$ is summable.

(ii)
: The family $(\left| z_i \right| )_{i\in I}$ is summable.

(iii)
: The family $(z_i)_{i\in I}$ is absolutely summable.

(iv)
: There exists some $C > 0$ such that $\sum_{i\in J}\left| z_i \right| \leq C$ for all $J\in \mathscr{F} (I)$.


In case that one hence all of the conditions are fulfilled, the estimate

:::{math}
\left| \sum_{i\in I} z_i \right| \leq \sum_{i\in I}\left| z_i \right|
:::

holds true.
:::



:::{prf:proof}

Assume that $(z_i)_{i\in I}$ is absolutely summable. Since $\C$ is normed with norm given by the absolut value this just means that there exists some $C > 0$ such that $\sum_{i\in J}\left| z_i \right| \leq C$ for all $J\in \mathscr{F} (I)$. Hence the supremum $c = \sup \left\{ \sum_{i\in J}\left| z_i \right| \mid J \in \mathscr{F} (I)\right\}$ exists and is $\leq C$. For given $\varepsilon > 0$ choose $J_\varepsilon \in \mathscr{F} (I)$ such that

:::{math}
c- \varepsilon \leq \sum_{i\in J_\varepsilon}\left| z_i \right| \leq c \ .
:::

Then one has for all $K\in \mathscr{F} (I)$ with $K\cap J_\varepsilon = \emptyset$

:::{math}
\left| \sum_{i\in K} z_i \right| \leq \sum_{i\in K} \left| z_i \right| \leq \varepsilon \ .
:::

Hence $\left( \sum_{i\in J} z_i \right)_{J \in \mathscr{F} (I)}$ is a Cauchy net, so has to converges by completeness of $\C$. This proves summability of $(z_i)_{i\in I}$.

Vice versa, assume now that $(z_i)_{i\in I}$ is summable. Then $\left( \sum_{i\in J} z_i \right)_{J \in \mathscr{F} (I)}$ is a Cauchy net. Hence there exists an element $J_1 \in \mathscr{F} (I)$ such that for all $K\in \mathscr{F} (I)$ with $K \cap J_1 = \emptyset$ the inequality

:::{math}
\left| \sum_{i\in K} z_i \right| < 1
:::

holds true. Let $C = \sum_{i\in J_1} \left| z_i\right|$. Then one has for all $J\in \mathscr{F} (I)$

:::{math}
\left| \sum_{i\in J} z_i \right| \leq \left| \sum_{i\in J\setminus J_1} z_i \right| +
\left| \sum_{i\in J\cap J_1} z_i \right| \leq 1 + C \ .
:::

By the preceding lemma the set of partial sums $ \sum_{i\in J} \left| z_i \right|$, where $J$ runs through the finite subsets of $I$, is then bounded by $4 + 4C$, hence $(z_i)_{i\in I}$ is absolutely summable.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Summable families of complex numbers -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXSummability in Banach spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Summability in Banach spaces -->
## Summability in Banach spaces
:::{prf:proposition} 
:label: thm:summability-criteria-family--normed-vector-space_1
Let $\mathrm{V}$ be a normed vector space. For a family $(v_i)_{i\in I}$ of elements in $\mathrm{V}$ the following are equivalent:



(ite:absolute-summable-family-normed-vector-space_1)=
(i)
: The family $(v_i)_{i\in I}$ is absolutely summable.

(ite:norm-summable-family-normed-vector-space_1)=
(ii)
: The family $(\left\| v_i \right\| )_{i\in I}$ is summable.

(ite:cauchy-summable-family-normed-vector-space_1)=
(iii)
: There exists some $C > 0$ such that $\sum_{i\in J}\left\| v_i \right\| \leq C$ for all $J\in \mathscr{F} (I)$.


If $\mathrm{V}$ is even a Banach space, these conditions are all equivalent to


\setcounterenumi3
(i)
: The family $(v_i)_{i\in I}$ is summable.
:::


:::{prf:proof}

{ref}`ite:norm-summable-family-normed-vector-space_1` and {ref}`ite:cauchy-summable-family-normed-vector-space_1`
are equivalent by \Crefthm:summability-criteria-family-complex-numbers
Assume now that {ref}`ite:absolute-summable-family-normed-vector-space_1` holds true.
:::


**to do:** Carl Neumann series
<!-- XXSEC_PREFIX_ENDXX\subsection*Summability in Banach spaces -->

<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXProperties of and relations between the various summability typesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Properties of and relations between the various summability types -->
## Properties of and relations between the various summability types
:::{prf:theorem} 
Let $I$ be a non-empty index set. Then the spaces $\ell^1 (I, \mathrm{V} )$ of summable families, $\ell^1 [I, \mathrm{V} ]$ of weakly summable families, $\ell^1 \{I, \mathrm{V} \}$ of absolutely summable families and $\ell^1 \langle I, \mathrm{V} \rangle$ of totally summable families in $E$ are all subvector spaces of the product vector space $E^I = \Pi_{i\in I} E$. Furthermore one has the following chain of inclusions:

:::{math}
\ell^1 \langle I, \mathrm{V} \rangle\subset\ell^1 \{I, \mathrm{V} \} \quad\text{and} \quad \ell^1 (I, \mathrm{V}) \subset \ell^1 [I, \mathrm{V} ] \ .
:::

If $E$ is complete, then one even has

:::{math}
\ell^1 \{I, \mathrm{V} \} \subset \ell^1 (I, \mathrm{V})
:::
:::



:::{prf:proof}

Now let $(v_i)$ be a summable family and $\alpha : \mathrm{V} \to \mathbb{K}$ a continuous linear form.

Let $U$ be an absolutely convex zero neighborhood. Then $U$ absorbes $B$, so there exists $r > 0$ such that $B \subset rU$. Hence
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Properties of and relations between the various summability types -->

<!-- XXSEC_PREFIX_ENDXX\sectionSummability -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXTopological tensor productsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionTopological tensor products -->
(sec:topological-tensor-products_1)=
# Topological tensor products
:::{prf:definition} cf.~[@brace_error, Chap.~I, \S\,3,]$^\text{o}$\,3]GroPTTEN
Let $\mathrm{V}$ and $\mathrm{W}$ be two locally convex topological vector spaces over the ground field $\mathbb{K}$. A locally convex vector topology $\tau$ on the (algebraic) tensor product $\mathrm{V} \otimes \mathrm{W}$ is called *compatible with the tensor product structure*, an *admissible tensor product topology*
or just *admissible* if the following conditions hold true:


(ATPT1)
: The canonical map $\mathrm{V} \times \mathrm{W} \to \mathrm{V} \otimes_\tau \mathrm{W}$ is seperately continuous that is for each $v \in \mathrm{V}$ and each $w\in\mathrm{W}$ the linear maps
   
   :::{math}
   \mathrm{W} \to \mathrm{V} \otimes_\tau \mathrm{W}, y \mapsto v \otimes y \quad\text{and} \quad
   \mathrm{V} \to \mathrm{V} \otimes_\tau \mathrm{W}, x \mapsto x \otimes w
   :::
   
   are continuous where $\mathrm{V} \otimes_\tau \mathrm{W} $ denotes the vector space $\mathrm{V} \otimes \mathrm{W}$ equipped with $\tau$.

(ATPT2)
: For all linear maps $\alpha \in \mathrm{V}'$ and $\beta \in \mathrm{W}'$ the canonical linear map map $\alpha \otimes \beta : \mathrm{V} \otimes_\tau \mathrm{W} \to \mathbb{K}$ is continuous.

(ATPT3)
: For every equicontinuous subset $A \subset \mathrm{V}'$ and equicontinuous subset $B\subset \mathrm{W}'$ the set $\left\{ \alpha \otimes \beta \mid \alpha \in A \:\&\: \beta \in B \right\}$ is an equicontinuous subset of the topological dual of $\mathrm{V} \otimes_\tau \mathrm{W}$.

The locally convex vector topology $\tau$ is called *strongly compatible with the tensor product structure*, a *strongly admissible tensor product topology* or briefly *strongly admissible*
if it satisfies:


(sATPT)
: The canonical map $\mathrm{V} \times \mathrm{W} \to \mathrm{V} \otimes_\tau \mathrm{W}$ is continuous where $\mathrm{V} \times \mathrm{W}$ carries the product topology.
:::


\para The admissible respectively strongly admissible vector topologies on $ \mathrm{V} \otimes \mathrm{W}$ are obviously partially ordered by set-theoretic inclusion. Therefore, the following definition makes sense.


<!-- XXSEC_PREFIX_ENDXX\sectionTopological tensor products -->

<!-- XXSEC_PREFIX_ENDXX\chapterTopological Vector Spaces -->

<!-- XXSEC_DEF_SPLITTERXX\chapterXXSEC_DEF_SPLITTERXXBanach Spaces and AlgebrasXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapterBanach Spaces and Algebras -->
# Banach Spaces and Algebras
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXFunctional calculusXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionFunctional calculus -->
(sec:functional-calculus_1)=
# Functional calculus

<!-- XXSEC_PREFIX_ENDXX\sectionFunctional calculus -->

<!-- XXSEC_PREFIX_ENDXX\chapterBanach Spaces and Algebras -->

<!-- XXSEC_DEF_SPLITTERXX\chapterXXSEC_DEF_SPLITTERXXHilbert SpacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapterHilbert Spaces -->
(chpt:hilbert-spaces_1)=
# Hilbert Spaces
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXInner product spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionInner product spaces -->
(sec:inner-product-spaces_1)=
# Inner product spaces
\para Let us first remind the reader that as before $\mathbb{K}$ stands for the field of real or of complex numbers. We will keep this notational agreement throughout the whole chapter.

:::{prf:definition} 
By a *sesquilinear form* on a $\mathbb{K}$-vector space $\mathrm{V}$ one understands a map $\langle \cdot , \cdot \rangle : \mathrm{V} \times \mathrm{V} \to \mathbb{K}$ with the following two properties:


(axiom:form-conjugate-linearity-in-first-coordinate_1)=
( SF1)
: The map $\langle \cdot , \cdot \rangle$ is *conjugate-linear* in its first coordinate which means that
   
   :::{math}
   \langle v_1 + v_2, w \rangle = \langle v_1, w \rangle + \langle v_2, w \rangle
   \quad \text{and} \quad \langle r v, w \rangle = \overline{r} \langle v, w \rangle
   :::
   
   for all $v, v_1,v_2, w \in \mathrm{V}$ and $r\in \mathbb{K}$.

(axiom:form-linearity-in-second-coordinate_1)=
( SF2)
: The map $\langle \cdot , \cdot \rangle$ is *linear* in its second coordinate which means that
   
   :::{math}
   \langle v,w_1 + w_2 \rangle = \langle v, w_1 \rangle + \langle v, w_2 \rangle
   \quad \text{and} \quad \langle v, r w \rangle = r \langle v, w \rangle
   :::
   
   for all $v, w , w_1,w_2 \in \mathrm{V}$ and $r\in \mathbb{K}$.

A *hermitian form* is a sesquilinear form $\langle \cdot , \cdot \rangle$ on $\mathrm{V}$ with the following additional property:


(axiom:form-conjugate-symmetry_1)=
( SF1)
: The map $\langle \cdot , \cdot \rangle$ is *conjugate-symmetric* which means that
   
   :::{math}
   \langle v, w \rangle = \overline{\langle w, v \rangle} \quad \text{for all } v, w \in \mathrm{V} \ .
   :::

A sesquilinear form $\langle \cdot , \cdot \rangle$ is called
*weakly-nondegenerate* if it satisfies axiom


(axiom:form-weakly-nondegenerate_1)=
( SF1w)
: For every $v\in \mathrm{V}$, the map $\mathrm{V} \to \mathbb{K}$, $w \to \langle w,v \rangle$ is the zero map if and only if $v=0$.

Finally, one calls a hermitian form $\langle \cdot , \cdot \rangle$ on $\mathrm{V}$
*positive semidefinite* if


(axiom:form-positive-semidefinite_1)=
( SF1s)
: $\langle v,v \rangle \geq 0$ for all $v\in \mathrm{V}$.
:::



:::{prf:remark} 
Recall that a map $\langle \cdot , \cdot \rangle : \mathrm{V} \times \mathrm{V} \to \mathbb{K}$ is called *bilinear*
if it satisfies {ref}`axiom:form-linearity-in-second-coordinate_1` and the following condition:


(axiom:form-linearity-in-first-coordinate_1)=
(BF1)
: The map $\langle \cdot , \cdot \rangle$ is *linear* in its first coordinate which means that
   
   :::{math}
   \langle v_1 + v_2, w \rangle = \langle v_1, w \rangle + \langle v_2, w \rangle
   \quad \text{and} \quad \langle rv, w \rangle = r \langle v, w \rangle
   :::
   
   for all $v, v_1,v_2, w \in \mathrm{V}$ and $r\in \mathbb{K}$.

In case the underlying ground field $\mathbb{K}$ coincides with the field of real numbers, a sesquilinear form is by definition the same as a bilinear form, and a hermitian form the same as a symmetric bilinear form.
:::


\para \labelpara:properties-seminorm-associated-positive-semidefinite-hermitian-form
Given a positive semidefinite hermitian form $\langle \cdot , \cdot \rangle$ on a $\mathbb{K}$-vector space $\mathrm{V}$, one calls two vectors $v,w \in \mathrm{V}$ *orthogonal*
if $\langle v , w \rangle = 0$. Since the hermitian form $\langle \cdot , \cdot \rangle$ is assumed to be positive semidefinite, the map

:::{math}
\| \cdot \| : \mathrm{V} \to \mathbb{R}_{\geq 0} , \: v \mapsto \|v \| = \sqrt{\langle v , v \rangle}
:::

is well-defined. We will later see that $\| \cdot \|$ is a seminorm on $\mathrm{V}$ and therefore call the map $\| \cdot \|$ the *seminorm associated to*
$\langle \cdot , \cdot \rangle$. The following formulas are immediate consequences of the properties defining a positive semidefinite hermitian form and the definition of the associated seminorm:

:::{math}
:label: eq:absolute-homogeneity_1
& \| v+w \|^2 = \| v\|^2 + 2\, \Re \, \langle v , w \rangle + \| w\|^2 \quad \text{for all }
v,w \in \mathrm{V} \ , \\

& \| v+w \|^2 = \| v\|^2 + \| w\|^2 \quad \text{for all orthogonal } v,w \in \mathrm{V} \ , \\

& \| v+w \|^2 + \|v-w\|^2 = 2 \big( \| v\|^2 + \| w\|^2 \big) \quad \text{for all } v,w \in \mathrm{V}\ ,\\

& \| rv \| = \sqrt{ |r|^2 \langle v , v \rangle } = |r| \| v \|
\quad \text{for all } v,w \in \mathrm{V} \text{ and } r\in \mathbb{K} \ .
:::

Formula {eq}`eq:pythagorean-theorem_1` is an abstract version of the *pythagorean theorem*,
\Crefeq:parallelogram-identity is called the *parallelogram identity*. The triangle inequality for the map $\| \cdot \|$ will turn out to be a consequence of the next result.


:::{prf:proposition} Cauchy--Schwarz inequality
:label: thm:cauchy-schwartz-inequality-inner-product-spaces_1
Given a positive semidefinite hermitian form $\langle \cdot , \cdot \rangle$ on a $\mathbb{K}$-vector space $\mathrm{V}$ the following inequality holds true:

:::{math}
:label: eq:cauchy-schwarz-inequality_1
|\langle v, w \rangle| \leq \|v\|\|w\| \quad \text{for all $v,w \in \mathrm{V}$}.
:::

Equality holds if $v$ and $w$ are linearly dependant. In case $\langle \cdot , \cdot \rangle$ is positive definite, the converse holds true as well.
:::


:::{prf:proof}

First consider the case where $\| v\| =\|w\| =0$. Note that this does not imply that $v=0$ (or $w=0$)
unless the hermitian form $\langle \cdot , \cdot \rangle$ is positive definite. Now put $c = - \langle v, w \rangle$ and compute

:::{math}
:label: eq:expanding-seminorm-of-sum-terms-sesquilinear-form_1
\begin{split}
0 & \leq \|c v + w\|^2 = 2 \, \Re \big( \overline{c} \, \langle v, w \rangle \big) = - 2 |\langle v, w \rangle|^2 \ .
\end{split}
:::

This entails $\langle v, w \rangle =0$ and the Cauchy--Schwarz inequality is proved for $\| v\| =\|w\| =0$.

If $\|v\| \neq 0 $ or $\| w \| \neq 0$, we can assume without loss of generality that $\|v\| \neq 0$. Under this assumption put

:::{math}
c = - \frac{\langle v, w \rangle}{\|v\|^2}
:::

and compute

:::{math}
:label: eq:expanding-norm-of-sum-in-inner-product-space_1
\begin{split}
0 & \leq \|c v + w\|^2 = |c|^2\|v\|^2 + 2 \, \Re \big( \overline{c} \, \langle v, w \rangle \big) + \|w\|^2 = \\ & = \frac{|\langle v, w \rangle|^2}{\|v\|^2} - 2\frac{|\langle v, w \rangle|^2}{\|v\|^2} + \|w\|^2 = \|w\|^2 - \frac{|\langle v, w \rangle|^2}{\|v\|^2} \ .
\end{split}
:::

Hence the estimate

:::{math}
|\langle v, w \rangle|^2 \leq \|v\|^2\|w\|^2
:::

holds which entails the Cauchy--Schwarz inequality.

In the case where $v,w$ are linearly dependant nonzero elements of $\mathrm{V}$ there exists a nonzero scalar $a\in \mathbb{K}$ such that $v = a w$. Therefore

:::{math}
|\langle v , w \rangle| = |a| \, \| w \|^2 = \| v \| \| w \| \, .
:::

If one of $v$ or $w$ is $0$, then both sides of the Cauchy--Schwarz inequality are $0$.

In the positive definite case, equality in {eq}`eq:cauchy-schwarz-inequality_1`
entails by \Crefeq:expanding-norm-of-sum-in-inner-product-space
that $c v +w = 0$ whenever $v \neq 0$. If $v=0$, then $v =0 \cdot w$. In either case this means that $v$ and $w$ are linearly dependant.
:::



:::{prf:lemma} 
:label: thm:positive-definitess-equivalent-nondegeneracy_1
A positive semidefinite hermitian form $\langle \cdot , \cdot \rangle$ on a $\mathbb{K}$-vector space $\mathrm{V}$ is weakly-nondegenerate if and only if it is *positive definite* that is if and only if

\setcounterenumi4
(axiom:form-positive-definite_1)=
( SF1p)
: $\langle v,v \rangle > 0$ for all $v\in \mathrm{V} \setminus \{ 0 \}$.
:::



:::{prf:proof}

A positive definite real bilinear or complex hermitian form $\langle \cdot , \cdot \rangle$ is weakly-nondegenerate since for every $v \in \mathrm{V} \setminus \{ 0 \}$ the linear form $\langle v,-\rangle : \mathrm{V} \to \mathbb{K}$ is nonzero by $\langle v,v \rangle > 0$.

Conversely, if $\langle v,- \rangle : \mathrm{V} \to \mathbb{K}$ is nonzero for all $v \in \mathrm{V} \setminus \{ 0 \}$, then there exists an element $w \in \mathrm{V}$ such that $\langle w,v \rangle \neq 0$. The Cauchy--Schwarz inequality entails

:::{math}
0 < |\langle w,v \rangle |^2 \leq \langle w,w \rangle \, \langle v,v \rangle \ ,
:::

which implies $\langle v,v \rangle > 0$. Hence $\langle \cdot , \cdot \rangle$ is positive definite.
:::



:::{prf:proposition} 
The map

:::{math}
\| \cdot \| :V \to \mathbb{R}_{\geq 0} , \: v \mapsto \|v \| = \sqrt{\langle v , v \rangle}
:::

associated to a positive semidefinite hermitian form $\langle \cdot , \cdot \rangle$ on a $\mathbb{K}$-vector space $\mathrm{V}$ is a seminorm. If the hermitian form is positive definite, then $\| \cdot \|$ is even a norm.
:::


:::{prf:proof}

Absolute homogeneity {ref}`axiom:norm-absolute-homogeneity_1` is given by Eq.~{eq}`eq:absolute-homogeneity_1`. The triangle inequality is a consequence of the Cauchy--Schwarz inequality:

:::{math}
\| v + w \|^2 = \| v\|^2 + 2 \, \Re \, \langle v , w \rangle + \| w\|^2 \leq
\| v\|^2 + 2 \, \| v \| \, \| w \| + \| w\|^2 = \big(\| v\|+\| w\| \big)^2 \ .
:::

Finally, if $\langle \cdot , \cdot \rangle$ is positive definite, then $\| v \| = \sqrt{\langle v , v \rangle} > 0 $ for all $v \in \mathrm{V} \setminus \{ 0 \}$, so $\| \cdot \|$ is a norm.
:::


Hilbert space definition

:::{prf:definition} 
:label: def:hilbert-space_1
By an *inner product* or a *scalar product* on a $\mathbb{K}$-vector space $\mathscr{H}$ one understands a positive definite hermitian form on $\mathscr{H}$. A $\mathbb{K}$-vector space $\mathscr{H}$ endowed with an inner product $\langle \cdot , \cdot \rangle : \mathscr{H} \times \mathscr{H} \to \mathbb{K}$ is called an *inner product space* or a *pre-Hilbert space*.

A hermitian form on a $\mathbb{K}$-vector space $\mathscr{H}$ which is only positive semidefinite is called a *semi-inner product* or a *semi-scalar product*.

A *Hilbert space* is an inner product space $(\mathscr{H} , \langle \cdot , \cdot \rangle)$ which is complete as a normed vector space. In other words, a Hilbert space is Banach space where the norm on the space is induced by an inner product.
:::



:::{prf:example} 
:label: ex:inner-product-spaces_1


\itemindent
: The vector space $\mathbb{R}^n$ with the *euclidean inner product*
   
   :::{math}
   \langle \cdot , \cdot \rangle : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}, \:
   \big( (v_1,\ldots , v_n),(w_1,\ldots , w_n) \big) \mapsto
   \sum_{i=1}^n v_i w_i
   :::
   
   is a real Hilbert space. Obviously, $\langle \cdot , \cdot \rangle$ is linear in the first argument, symmetric, and positive definite, hence a real inner product. The associated norm is the *euclidean norm*. We have seen before that $\mathbb{R}^n$ with the euclidean norm is complete.

\itemindent
: The vector space $\C^n$ together with the hermitian form
   
   :::{math}
   \langle \cdot , \cdot \rangle : \C^n \times \C^n \to \C, \:
   \big( (v_1,\ldots , v_n),(w_1,\ldots , w_n) \big) \mapsto
   \sum_{i=1}^n \overline{v}_iw_i
   :::
   
   is a complex Hilbert space. One immediately verifies that $\langle \cdot , \cdot \rangle$ is linear in the second argument, conjugate-symmetric, and positive definite. Hence $\langle \cdot , \cdot \rangle$ is a complex inner product which we sometimes call the *standard hermitian inner product* on $\C^n$. Its associated norm is again the euclidean norm, so by completeness of $\C^n\cong \mathbb{R}^{2n}$ with respect to the euclidean norm one obtains the claim.

\itemindent
: The set
   
   :::{math}
   \ell^2 =
   \left\{(z_k)_{k\in \mathbb{N}} \in \C^\mathbb{N} \;\ifnum\currentgrouptype=16 \middle\fi|\; \sum_{k=0}^\infty |z_k|^2 < \infty \right\}
   :::
   
   of square summable sequences of complex numbers is a complex Hilbert space with inner product
   
   :::{math}
   \langle \cdot , \cdot \rangle :
   \ell^2 \times \ell^2 \to \C, \: \big((z_k)_{k\in \mathbb{N}},(w_k)_{k\in \mathbb{N}} \big)
   \mapsto \sum_{k=0}^\infty \overline{z}_k w_k \ .
   :::
   
   To prove this one needs to first verify that $\ell^2$ is a subvector space of $\C^\mathbb{N}$. For $z = (z_k)_{k\in \mathbb{N}} \in \C^\mathbb{N}$ denote by $\| z\|$ the *extended norm*
   $\sqrt{\sum_{k=0}^\infty |z_k|^2} = \sup\limits_{K\in \mathbb{N}} \sqrt{\sum_{k=0}^K |z_k|^2} \in  {[ 0,\infty ]} $. Then $z\in \ell^2$ if and only if $\|z\| < \infty$. Now let $a \in \C$ and $z\in \ell^2$ and compute
   
   :::{math}
   \| a z \| = \sqrt{\sum_{k=0}^\infty |a z_k|^2} = |a| \, \sqrt{\sum_{k=0}^\infty |z_k|^2} = |a| \cdot \| z \| < \infty \ .
   :::
   
   Hence $az \in \ell^2$. If $z,w \in \ell^2$, denote for each $K\in \mathbb{N}$ by $z_{(K)}$ and $w_{(K)}$ the ``cut-off'' vectors $(z_0, \ldots , z_K) \in \C^{K+1}$ and $(w_0, \ldots , w_K) \in \C^{K+1}$, respectively. By the triangle inequality for the norm on the Hilbert space $\C^{K+1}$ one concludes
   
   :::{math}
   \sqrt{\sum_{k=0}^K | z_k + w_k |^2} = \| z_{(K)} + w_{(K)} \| \leq
   \| z_{(K)} \| + \| w_{(K)} \| \leq \| z \| + \| w \| < \infty \ .
   :::
   
   Therefore, the sequence of partial sums $\sum_{k=0}^K | z_k + w_k |^2$, $K\in \mathbb{N}$, is bounded, so convergent by the the monotone convergence theorem. One obtains
   
   :::{math}
   \| z + w \| = \lim_{K\to\infty} \sqrt{ \sum_{k=0}^K | z_k + w_k |^2} \leq \| z \| + \| w \| < \infty \ .
   :::
   
   Hence $z + w$ is square summable and $\ell^2$ a vector subspace of $\C^\mathbb{N}$ indeed. Note that our argument also shows that the restriction of the extended norm to $\ell^2$ is a norm.
   
   We need to show that $\langle \cdot , \cdot \rangle$ is well-defined. To this end it suffices to prove that for all $z,w \in\ell^2$ the family $\left( z_k \overline{w}_k\right)_{k\in \mathbb{N}}$ is absolutely summable or in other words that $\sum_{k=0}^\infty \left| z_k \overline{w}_k \right| < \infty$. One concludes by the H\"older inequality for sums
   
   :::{math}
   \sum_{k=0}^K \left| \overline{z}_k w_k \right| = \sum_{k=0}^K \left| z_k w_k \right|
   \leq \| z_{(K)} \| \, \| w_{(K)} \| \leq \| z \| \, \| w \| \ .
   :::
   
   So the left hand side has an upper bound uniform in $K$ which by the monotone convergence theorem entails convergence of the partial sums and the estimate
   
   :::{math}
   \sum_{k=0}^\infty \left| \overline{z}_k w_k \right| \leq \| z \| \, \| w \| < \infty \ .
   :::
   
   By definition it is clear that $ \langle \cdot , \cdot \rangle $ is linear in the second argument, conjugate-symmetric and positive definite, hence a complex inner product. Note that the norm associated to $ \langle \cdot , \cdot \rangle $ coincides with the above defined map $\| \cdot \|$.
   
   It remains to be shown that $\ell^2$ is complete. Let $(z^n)_{n\in \mathbb{N}}$ with $z^n = {(z^n_k)}_{k\in \mathbb{N}}\in \ell^2$ for all $n\in \mathbb{N}$ be a Cauchy sequence in $\ell^2$. For $\varepsilon > 0$ choose $N_\varepsilon \in \mathbb{N}$ so that
   
   :::{math}
   \| z^n - z^m \| < \varepsilon \quad \text{for all } n,m \geq N_\varepsilon \ .
   :::
   
   For each fixed $k\in \mathbb{N}$ one therefore has
   
   :::{math}
   :label: eq:estimate-component-sequence-Cauchy-sequence-square-summable-sequences_1
   | z^n_k - z^m_k | \leq \| z^n - z^m \| < \varepsilon \quad \text{for all } n,m \geq N_\varepsilon \ .
   :::
   
   By completeness of $\C$ there exist $z_k \in \C$ such that $\lim_{n\to\infty} z^n_k = z_k$ for all $k\in \mathbb{N}$. We claim that $z = (z_k)_{k\in \mathbb{N}}$ is an element of $\ell^2$ and that $(z^n)_{n\in \mathbb{N}}$ converges to $z$. To verify this observe that for all $\varepsilon > 0$, $K\in \mathbb{N}$ and $n\geq N_\varepsilon$
   
   :::{math}
   \sum_{k=0}^K | z_k - z^n_k |^2 = \lim_{m\to\infty} \sum_{k=0}^K | z^m_k - z^n_k |^2
   \leq \sup_{m \geq N_\varepsilon} \sum_{k=0}^K | z^m_k - z^n_k |^2
   \leq \sup_{m \geq N_\varepsilon} \| z^m - z^n \|^2 \leq \varepsilon^2 \ .
   :::
   
   This implies by the triangle inequality and the fact that the Cauchy sequence $(z^n)_{n\in \mathbb{N}}$ is bounded in norm by some $C > 0$ that for all $K\in \mathbb{N}$ and $N = N_1$
   
   :::{math}
   \sqrt{\sum_{k=0}^K | z_k|^2 } = \| z_{(K)} \| \leq \| z_{(K)} - z^N_{(K)} \| + \| z^N_{(K)} \|
   \leq \| z_{(K)} - z^N_{(K)} \| + \| z^N \|
   \leq 1 + C \ .
   :::
   
   Hence $ \| z \|= \sqrt{\sum_{k=0}^\infty | z_k|^2 } \leq 1 + C $ and $z \in \ell^2$. In addition one obtains
   
   :::{math}
   \| z - z^n \| = \lim_{K\to\infty} \sqrt{\sum_{k=0}^K | z_k - z^n_k |^2} \leq \varepsilon \quad \text{for all } n \geq N_\varepsilon \ .
   :::
   
   This means that $z$ is the limit of the sequence $(z^n)_{n\in \mathbb{N}}$ and $\ell^2$ is complete.

\itemindent
: Denote by $\lambda$ the Lebesgue measure and let
   
   :::{math}
   \mathscr{L}^2(\mathbb{R}^d) = \left\{ f : \mathbb{R}^d \to \C \;\ifnum\currentgrouptype=16 \middle\fi|\; f
   \text{ is Lebesgue measurable and }
   \| f \|_2 := \sqrt{\int_{\mathbb{R}^d}|f|^2 d\lambda} < \infty \right\}
   :::
   
   be the space of Lebesgue square integrable functions on $\mathbb{R}^d$. Then $\mathscr{L}^2(\mathbb{R}^d)$ is a linear subspace of the space of all measurable functions by Minkowski's inequality which reads
   
   :::{math}
   \| f + g \|_p \leq \| f \|_p + \| g \|_p \quad
   \text{for all measurable } f,g : \mathbb{R}^d \to \C \ .
   :::
   
   Hereby, $\| f \|_p$ denotes for $p\in  {[ 1,\infty \rtsbrak} $ the $\mathscr{L}^p$-seminorm $\left( \int_{\mathbb{R}^d}|f|^p d\lambda\right)^{1/p} $ of a measurable function $f:\mathbb{R}^d\to \C$. Note that $\| f \|_p $ can attain the value $\infty$, namely when $f$ is not in the space $\mathscr{L}^p(\mathbb{R}^d)$. By H\"older's inequality, the product $fg$ is Lebesgue integrable for $f,g \in \mathscr{L}^2(\mathbb{R}^d)$ and one has the estimate
   
   :::{math}
   \int_{\mathbb{R}^d}| f g | d\lambda = \| fg\|_1 \leq \|f\|_2\,\| g\|_2 \ .
   :::
   
   Hence the map
   
   :::{math}
   \langle \cdot , \cdot \rangle : \mathscr{L}^2(\mathbb{R}^d) \times \mathscr{L}^2(\mathbb{R}^d) \to \C, \: (f,g) \mapsto \int_{\mathbb{R}^d}\overline{f}g\, d\lambda
   :::
   
   is well-defined and a positive semidefinite hermitian form on $\mathscr{L}^2(\mathbb{R}^d)$. By construction, the associated seminorm is the $\mathscr{L}^2$-seminorm $\|\cdot\|_2$. Modding out $\mathscr{L}^2(\mathbb{R}^d)$ by the kernel
   
   :::{math}
   \mathscr{N} := \operatorname{Ker} (\| \cdot \|_2) =
   \left\{ f \in \mathscr{L}^2(\mathbb{R}^d) \;\ifnum\currentgrouptype=16 \middle\fi|\; \int_{\mathbb{R}^d}|f|^2 d\lambda = 0 \right\}
   :::
   
   gives the Lebesgue space
   
   :::{math}
   L^2 (\mathbb{R}^d) := \mathscr{L}^2(\mathbb{R}^d) / \mathscr{N} \ .
   :::
   
   
   The hermitian form $\langle \cdot , \cdot \rangle $ vanishes on $\mathscr{N} \times \mathscr{L}^2(\mathbb{R}^d)$ and $\mathscr{L}^2(\mathbb{R}^d) \times \mathscr{N}$ by the Cauchy--Schwarz inequality, hence descends to a hermitian form
   
   :::{math}
   \langle \cdot , \cdot \rangle : L^2(\mathbb{R}^d) \times L^2(\mathbb{R}^d) \to \C, \: (f + \mathscr{N} ,g+ \mathscr{N}) \mapsto \int_{\mathbb{R}^d}\overline{f}g\, d\lambda \ .
   :::
   
   That hermitian form is positive definite, since $\langle f + \mathscr{N}, f + \mathscr{N} \rangle = 0$ means $ \int_{\mathbb{R}^d}|f|^2 d\lambda =0$, hence $f\in \mathscr{N}$. Let us show that $L^2(\mathbb{R}^d)$ is complete with respect to the $L^2$-norm $\|\cdot\|_2$ induced by the inner product. Note that on the quotient space $\|\cdot\|_2$ is a norm indeed by construction. So let $(f_n+ \mathscr{N})_{n\in\mathbb{N}}$ be a Cauchy sequence in $L^2(\mathbb{R}^d)$. Choose a subsequence $(f_{n_k})_{k\in \mathbb{N}}$ such that
   
   :::{math}
   \| f_{n_k} - f_{n_{k-1}}\|_2 < \frac{1}{2^k} \quad \text{for all } k \in \mathbb{N}_{ > 0}
   :::
   
   and put
   
   :::{math}
   g_n(x) = \sum\limits_{k=1}^n | f_{n_k} (x)- f_{n_{k-1}}(x)| \quad
   \text{for } x\in \mathbb{R}^d \text{ and } n \in \mathbb{N} \ .
   :::
   
   The limit function
   
   :::{math}
   g:\mathbb{R}^d \to  {[ 0,\infty ]} , \: x \mapsto \lim_{n\to\infty} g_n(x) = \liminf_{n\to\infty} g_n(x)
   :::
   
   then exists even though it might not be finite everyhwere. Minkowski's inequality for the $\mathscr{L}^2$-norm entails that $\| g_n\|_2 \leq 1$ for all $n\in \mathbb{N}$, hence $g$ is measurable and $\|g\|_2 \leq \liminf_{n\to\infty} \|g_n\|_2 \leq 1$ by Fatou's lemma. Therefore, $g(x)$ is finite for all $x$ up to a set $Z\subset \mathbb{R}^d$ of measure $0$, and for those $x$ the series with partial sums $g_n(x)$ converges absolutely. For all $x \in \mathbb{R}^d\setminus Z$ the limit
   
   :::{math}
   f(x) = \lim_{k\to\infty} f_{n_k} (x) = f_{n_0} + \lim_{k\to\infty} \sum_{j=1}^{k} (f_{n_j} (x) - f_{n_{j-1}} (x))
   :::
   
   therefore exists in $\C$. Put $f(x)=0$ for all $x\in Z$, and let $\chi_Z:\mathbb{R}^d\to \mathbb{R}$ be the characteristic function of $Z$. Then the sequence of functions $(\chi_Zf_{n_k})_{k \in\mathbb{N}}$ converges pointwise to $f$, and each of the functions $\chi_Zf_n$ is measurable, actually even square integrable. Since
   
   :::{math}
   |\chi_Z f_{n_k}|\leq |\chi_Zf_{n_0}| + g_k\leq |\chi_Zf_{n_0}| + g \quad
   \text{for all } k\in \mathbb{N}
   :::
   
   and since $|\chi_Zf_{n_0}| + g$ is square integrable by Minkowski's inequality, the pointwise limit $f$ is square integrable by Lebesgue's dominated convergence theorem, and $f +\mathscr{N}$ is in $L^2(\mathbb{R}^d)$. It remains to show that $(f_{n}+\mathscr{N})_{n\in \mathbb{N}}$ converges to $f+\mathscr{N}$ in the norm $\|\cdot\|_2$. To this end let $\varepsilon > 0$ and choose $N\in \mathbb{N}$ such that $\| f_n - f_m\|_2 < \varepsilon$ for $n,m\geq N$. By Fatou's lemma one obtains
   
   :::{math}
   \int_{\mathbb{R}^d} | f_n -f|^2 d\lambda \leq \liminf_{m\to \infty}
   \int_{\mathbb{R}^d} | f_n -f_m|^2 d\lambda \leq \varepsilon^2 \quad\text{for all } n \geq N \ .
   :::
   
   Hence $\lim_{n\to\infty} \|f_n -f\|_2 =0$, and $L^2(\mathbb{R}^d)$ endowed with the inner product $\langle \cdot , \cdot \rangle $ is a Hilbert space. It is called the
   *Hilbert space of square-integrable functions* on $\mathbb{R}^d$. Note that for every complete measure space $(\Omega,\mu)$ one obtains in the same way the Hilbert space $L^2(\Omega,\mu)$ of square-integrable functions on $(\Omega,\mu)$.
:::


Theorem giving condition to relate inner product with norm


:::{prf:theorem} 
:label: thm:parallegram-identity-guarantees-that-norm-comes-from-some-inner-product_1
Let $\mathrm{V}$ be a normed $\mathbb{K}$-vector space. Then the norm $\|\cdot\| : \mathrm{V} \to \mathbb{R}_{\geq 0}$ is associated to an inner product $\langle \cdot , \cdot \rangle : \mathrm{V} \times \mathrm{V} \to \mathbb{K}$ if and only if the *parallelogram identity*

:::{math}
\| v + w \|^2 + \| v - w\|^2 = 2\|v\|^2 + 2\|w\|^2
:::

holds true for all $v,w \in \mathrm{V}$. In this case, the inner product of two elements $v,w\in \mathrm{V}$ can be expressed by the *polarization identity for* $\mathbb{K} = \mathbb{R}$

:::{math}
:label: eq:real-polarization-identity_1
\langle v , w \rangle = \frac 14 \left( \| v + w \|^2 - \| v - w \|^2 \right)
= \frac 12 \left( \| v + w \|^2 - \| v \|^2 - \| w \|^2 \right)
:::

respectively by the *polarization identity for* $\mathbb{K} = \C$

:::{math}
:label: eq:complex-polarization-identity_1
\langle v , w \rangle = \frac 14 \sum_{k=1}^4 \hspace{0.1em}\mathsf{i}\hspace{0.1em}^k \, \| w + \hspace{0.1em}\mathsf{i}\hspace{0.1em}^k \, v \|^2 \ .
:::
:::


:::{prf:proof}

The forward direction is a consequence of
ERROR_UNDEFINED_LABEL_para:properties-seminorm-associated-positive-semidefinite-hermitian-form_-1, Eq.~{eq}`eq:parallelogram-identity_1`. To show the backward direction we consider two cases $\mathbb{K} = \mathbb{R}$ and $\mathbb{K} = \C$ separately.

*1.~Case.* Given the norm $\|\cdot\|$ define $\langle \cdot , \cdot \rangle : \mathrm{V} \times \mathrm{V} \to \mathbb{R}$ by real polarization

:::{math}
\langle v , w \rangle = \frac 14 \left( \| v + w \|^2 - \| v - w \|^2 \right), \quad \text{where } v,w\in \mathrm{V} \ .
:::

Note that the parallelogram identity entails

:::{math}
\frac 14 \left( \| v + w \|^2 - \| v - w \|^2 \right) =
\frac 12 \left( \| v + w \|^2 - \| v \|^2 - \| w \|^2 \right) \ .
:::

Observe that by definition $\langle v , w \rangle = \langle w , v \rangle$ and $\| v \| = \sqrt{ \langle v , v \rangle}$. Let us show additivity in the first variable. Let $v_1,v_2,w \in \mathrm{V}$ and compute using the parallelogram identity

:::{math}
\begin{split}
\| v_1 + v_2 + w \|^2 & = 2 \| v_1 + w \|^2 + 2 \| v_2\|^2 - \| v_1 + w - v_2\|^2 \ , \\
\| v_1 + v_2 + w \|^2 & = 2 \| v_2 + w \|^2 + 2 \| v_1\|^2 - \| v_2 + w - v_1\|^2 \ .
\end{split}
:::

Hence

:::{math}
\begin{split}
\| v_1 + v_2 \pm w \|^2 & =
\| v_1 \pm w \|^2 + \| v_2 \pm w \|^2 + \| v_1\|^2 + \| v_2\|^2 - \| v_1 \pm w - v_2\|^2 - \| v_2 \pm w - v_1\|^2 \ .
\end{split}
:::

Subtracting the $-$ version from the $+$ version of this equation entails

:::{math}
\begin{split}
\langle v_1 + v_2 , w \rangle \, & = \frac 14 \left( \| v_1 + v_2 + w \|^2 - \| v_1 + v_2 - w \|^2 \right)= \\ & = \frac 14 \left( \| v_1 + w \|^2 + \| v_2 + w \|^2 - \| v_1 - w \|^2 - \| v_2 - w \|^2 \right) =
\langle v_1 , w \rangle + \langle v_2 , w \rangle \ ,
\end{split}
:::

so additivity in the first variable is proved. By induction one derives from this that for all natural $n$

:::{math}
:label: eq:natural-number-homogeneity_1
\langle nv , w \rangle = n \langle v , w \rangle \quad \text{for all } v,w \in \mathrm{V} \ .
:::

Since then $\langle - nv , w \rangle - n \langle v , w \rangle = \langle -nv + nv , w \rangle = 0$ for all $n\in \mathbb{N}$, Eq.~{eq}`eq:natural-number-homogeneity_1` also holds for $n\in \mathbb{Z}$. Now let $p\in \mathbb{Z}$ and $q \in \mathbb{N}_{ > 0}$. Then $ q\, \langle \frac pq v , w \rangle = \langle p v , w \rangle = p \, \langle v , w \rangle$, hence one has for rational $r$

:::{math}
:label: eq:rational-number-homogeneity_1
\langle rv , w \rangle = r \langle v , w \rangle \quad \text{for all } v,w \in \mathrm{V} \ .
:::

Since addition, multiplication by scalars and the norm are continuous, the function

:::{math}
\mathbb{R} \to \mathbb{R}, \:r \mapsto \langle rv , w \rangle - r \langle v , w \rangle = \frac 14 \left( \| r v + w \|^2 + r \| v - w \|^2 - \| rv - w \|^2 - r \| v + w \|^2 \right)
:::

is continuous. Since it vanishes over $\mathbb{Q}$, it has to coincide with the zero map. Therefore, Eq.~{eq}`eq:rational-number-homogeneity_1` holds for all $r\in \mathbb{R}$. So $\langle \cdot , \cdot \rangle$ is linear in the first coordinate. By symmetry, it is so too in the second coordinate. Hence $\langle \cdot , \cdot \rangle$ is a symmetric bilinear form inducing $\| \cdot \|$.

*2.~Case.* In the case $\mathbb{K} = \C$ use complex polarization and put

:::{math}
\langle v , w \rangle = \frac 14 \sum_{k=1}^4 \hspace{0.1em}\mathsf{i}\hspace{0.1em}^k \, \| w + \hspace{0.1em}\mathsf{i}\hspace{0.1em}^k \, v \|^2
\quad \text{for all } v,w\in \mathrm{V} \ .
:::

Then $\langle \cdot , \cdot \rangle$ is conjugate-symmetric, since

:::{math}
\overline{\langle v , w \rangle} = \frac 14 \sum_{k=1}^4 (- \hspace{0.1em}\mathsf{i}\hspace{0.1em})^k \, \| w + \hspace{0.1em}\mathsf{i}\hspace{0.1em}^k \, v \|^2 = \frac 14 \sum_{k=1}^4 (-\hspace{0.1em}\mathsf{i}\hspace{0.1em})^k \, \| (-\hspace{0.1em}\mathsf{i}\hspace{0.1em})^k \, w + v \|^2 =
\langle w , v \rangle \ .
:::

Next compute

:::{math}
\Re \, \langle v , w \rangle = \frac 14 \left( \| w + v \|^2 - \| w - v \|^2 \right)
:::

and

:::{math}
\Im \, \langle v , w \rangle = \frac 14 \left( \| w + \hspace{0.1em}\mathsf{i}\hspace{0.1em} v \|^2 - \| w - \hspace{0.1em}\mathsf{i}\hspace{0.1em} v \|^2 \right) \ .
:::

By the first case one concludes that $\Re \langle \cdot , \cdot \rangle$ and $\Im \langle \cdot , \cdot \rangle$ are both $\mathbb{R}$-linear in the first and the second coordinate. Moreover,

:::{math}
\Re \, \langle v , \hspace{0.1em}\mathsf{i}\hspace{0.1em} w \rangle = \frac 14 \left( \| \hspace{0.1em}\mathsf{i}\hspace{0.1em} w + v \|^2 - \| \hspace{0.1em}\mathsf{i}\hspace{0.1em} w - v \|^2 \right)
= \frac 14 \left( \| w - \hspace{0.1em}\mathsf{i}\hspace{0.1em} v \|^2 - \| w + \hspace{0.1em}\mathsf{i}\hspace{0.1em} v \|^2 \right) = - \Im \, \langle v , w \rangle = \Re \, \hspace{0.1em}\mathsf{i}\hspace{0.1em} \langle v , w \rangle
:::

and

:::{math}
\Im \, \langle v , \hspace{0.1em}\mathsf{i}\hspace{0.1em} w \rangle =
\frac 14 \left( \| \hspace{0.1em}\mathsf{i}\hspace{0.1em} w + \hspace{0.1em}\mathsf{i}\hspace{0.1em} v \|^2 - \| \hspace{0.1em}\mathsf{i}\hspace{0.1em} w - \hspace{0.1em}\mathsf{i}\hspace{0.1em} v \|^2 \right) =
\Re \, \langle v , w \rangle = \Im \, \hspace{0.1em}\mathsf{i}\hspace{0.1em} \langle v , w \rangle \ ,
:::

hence $\langle \cdot , \cdot \rangle$ is complex linear in the second coordinate. Finally,

:::{math}
\Re \, \langle v , v \rangle = \| v \|^2 \quad \text{and} \quad
\Im \, \langle v , v \rangle = \frac 14 \left( \| v + \hspace{0.1em}\mathsf{i}\hspace{0.1em} v \|^2 - \| v - \hspace{0.1em}\mathsf{i}\hspace{0.1em} v \|^2 \right) = 0 \ .
:::

This finishes the proof that $ \langle \cdot , \cdot \rangle$ is a complex inner product inducing the norm $\| \cdot \|$.
:::


\para Next we will turn Hilbert spaces into a category. To this end one needs to know what morphisms in this category should be. There are two options each giving rise to a category of Hilbert spaces. These categories just differ by their morphism classes. The first one is to have as morphisms linear maps $A:\mathscr{H}_1\to\mathscr{H}_2$ preserving the inner products which means that they fulfill

:::{math}
\langle Av_1,Av_2 \rangle = \langle v_1,v_2 \rangle \quad \text{for all } v_1,v_2 \in \mathscr{H}_1 \ .
:::

By \Crefthm:parallegram-identity-guarantees-that-norm-comes-from-some-inner-product this property is equivalent to

:::{math}
\| Av \| = \| v \| \quad \text{for all } v \in \mathscr{H}_1 \ ,
:::

that is to $A$ being *norm preserving* or *isometric*. Obviously, the identity map on a Hilbert space is isometric and the composition of two composable isometric linear maps is again isometric and linear. Hence Hilbert spaces together with norm preserving linear maps between them form a category which we denote by $\mathsf{Hilb_{np}}$. The isomorphisms in this category are the surjective isometric linear maps between Hilbert spaces. Such maps are called *unitary*. The condition of a linear map being norm preserving is pretty restrictive, so the category $\mathsf{Hilb_{np}}$ contains only few morphisms. This can be cured by allowing all
*bounded* linear maps between Hilbert spaces to be morphisms that is of all linear $A:\mathscr{H}_1\to\mathscr{H}_2$ for which there exists a $C\geq 0$ such that

:::{math}
:label: eq:norm-bound-values-bounded-linear-operator_1
\| Av \| \leq C \| v \| \quad \text{for all } v \in \mathscr{H}_1 \ .
:::

The existence of a smallest such $C$ is guaranteed by the following. It is called the *operator norm* of $A$ and is denoted $\| A\|$.


:::{prf:lemma} 
:label: thm:equivalent-descriptions-operator-norm_1
The operator norm of a bounded linear operator $A:\mathscr{H}_1\to\mathscr{H}_2$ between Hilbert spaces $\mathscr{H}_1$ and $\mathscr{H}_2$ exists and is given by

:::{math}
\begin{split}
\| A\| \, & = \sup \big\{ \| Av \| \bigm\vert v\in \mathscr{H}_1, \, \| v \| = 1 \big\} \\ & = \sup \big\{ \| Av \| \bigm\vert v\in \mathscr{H}_1, \, \| v \| \leq 1 \big\} \\ & = \sup \big\{ |\langle w,Av  \rangle| \bigm\vert v\in \mathscr{H}_1, \, w\in \mathscr{H}_2, \, \| v \| =\|w\| = 1 \big\} \ .
\end{split}
:::
:::


:::{prf:proof}

If $A:\mathscr{H}_1\to\mathscr{H}_2$ is bounded, then the set $\big\{ \| Av \| \bigm\vert v\in \mathscr{H}_1, \, \| v \| = 1 \big\}$ is bounded, hence has a supremum $C_0$. This implies that for all non-zero $v \in \mathscr{H}_1$

:::{math}
\| Av \| = \|v\| \, \left\| A\left( \frac{v}{\| v\|} \right) \right\| \leq C_0 \| v\| \ .
:::

Hence the estimate {eq}`eq:norm-bound-values-bounded-linear-operator_1` holds true for $C=C_0$. Moreover, $C_0$ is the smallest such $C$ because if $0\leq C_1 < C_0$, then there exists $v \in \mathscr{H}_1$ with $\| v\| =1$ and $\| Av\| > C_1$. This proves that the operator norm of $A$ exists and that it fulfills $\| A \| = C_0$.

By definition of $C_0$, the estimate $\| A \| = C_0 \leq \sup \big\{ \| Av \| \bigm\vert v\in \mathscr{H}_1, \, \| v \| \leq 1 \big\}$ holds true. By definition of the operator norm, $\| Av \| \leq \| A \| $ for all $v\in \mathscr{H}_1$ with $ \| v \| \leq 1$. The two estimates together entail the equality $\| A \| = \sup \big\{ \| Av \| \bigm\vert v\in \mathscr{H}_1, \, \| v \| \leq 1 \big\}$.

The Cauchy--Schwarz inequality entails

:::{math}
\sup \big\{ |\langle w,Av  \rangle| \bigm\vert v\in \mathscr{H}_1, \, w\in \mathscr{H}_2, \, \| v \| =\|w\| = 1 \big\} \leq \| A \| \ .
:::

The converse estimate follows by the observation that

:::{math}
\sup \big\{ |\langle w,Av  \rangle| \bigm\vert w\in \mathscr{H}_2, \, \|w\| = 1 \big\} \geq
\Big|\Big\langle \frac{Av}{\| Av\|} ,Av \Big\rangle\Big| = \| Av \|
:::

whenever $Av \neq 0$. This proves the last claimed equality.
:::


Every norm preserving linear map is bounded with operator norm $1$. In particular, the identity map on a Hilbert space is bounded. Moreover, if $A: \mathscr{H}_1\to\mathscr{H}_2$ and $B: \mathscr{H}_2\to\mathscr{H}_3$ are bounded linear operators between Hilbert spaces, then the composition $BA : \mathscr{H}_1\to\mathscr{H}_3$ is bounded with operator norm $\leq \| B\|\, \| A\|$ since for all $v \in \mathscr{H}_1 $ with $\| v\|\leq 1$

:::{math}
\| BAv \| \leq \| B \| \, \|Av\| \leq \| B\|\, \| A\| \ .
:::

Hence Hilbert spaces as objects together with bounded linear maps as morphisms form a category which we denote by $\mathsf{Hilb}$ and call the *category of Hilbert spaces*. Note that the morphisms in this category appear to ``forget'' the inner product and just preserve the linear and the topological structure. John Baez [@BaeHDAII2HS, p.~133] has explained how to heal this apparent defect by showing that$\mathsf{Hilb}$ carries a so-called $*$-structure given by the adjoint map on bounded linear operators. We will come back to this point later when we introduce adjoint operators.

As proved already for Banach spaces, a linear map between Hilbert spaces is bounded if and only if it is continuous. For reasons of completeness and convenience we state here the result for inner product spaces.


:::{prf:proposition} 
Let $A: \mathscr{H}_1 \to \mathscr{H}_2$ be a linear map between two inner product spaces. Then the following are equivalent.



(ite:boundedness-linear-map_1)=
(i)
: $A$ is bounded.

(ite:continuity-linear-map_1)=
(ii)
: $A$ is continuous.

(ite:continuity-linear-map-at-zero_1)=
(iii)
: $A$ is continuous at $0$.
:::


:::{prf:proof}

{ref}`ite:boundedness-linear-map_1` $\implies$ {ref}`ite:continuity-linear-map_1`. Assume that $A$ is bounded. Let $\| A\| :=\sup_{v\in \mathscr{H}_1} \| Av \| $ be its norm. Then, for all $v,w \in \mathscr{H}_1$

:::{math}
\| Av - Aw\| \leq \| A\| \cdot \| v -w\| \ .
:::

Hence $A$ is Lipschitz continuous, so in particular continuous. \\
{ref}`ite:continuity-linear-map_1` $\implies$ {ref}`ite:continuity-linear-map-at-zero_1`. If the map $A$ is continuous, it is in particular continuous at the origin. \\
{ref}`ite:continuity-linear-map-at-zero_1` $\implies$ {ref}`ite:boundedness-linear-map_1`. If $A$ is continuous at the origin, there exists $\delta > 0$ such that for all $v \in \mathscr{H}_1$ the estimate $\| A v\| < 1$ holds whenever $\| v \| < \delta$. This implies that for $v$ with $\| v \| \leq 1 $

:::{math}
\| A v\| = 2 \delta \left\| A\left( \frac{1}{2\delta}v \right) \right\| < 2 \delta \ .
:::

This means that $A$ is bounded.
:::


\para Last in this section we will introduce bounded bilinear and sesquilinear maps. We define them for normed vector spaces. Their main application lies in the operator theory on Hilbert spaces, so we introduce them here.


:::{prf:definition} 
Let $\mathrm{V}_1$ and $\mathrm{V}_2$ be two normed vector spaces over $\mathbb{K}$ and denote the norms on $\mathrm{V}_1$ and $\mathrm{V}_2$ by the same symbol $\| \cdot \|$. Assume that $b : \mathrm{V}_1 \times \mathrm{V}_2 \to \mathbb{K}$ is a *bilinear* or
*sesquilinear form* that is $b$ is linear in each argument respectively $b$ is conjugate linear in the first and linear in the second argument. The form $b : \mathrm{V}_1 \times \mathrm{V}_2 \to \mathbb{K}$ then is called *bounded* if there exists a $C > 0$ such that

:::{math}
| b(v,w)| \leq C \, \| v\| \, \| w \| \quad \text{for all } v \in \mathrm{V}_1, \: w \in \mathrm{V}_2 \ .
:::

In this case,

:::{math}
\| b \| := \sup \big\{ | b(v,w) | \bigm\vert v \in \mathrm{V}_1 , \: w \in \mathrm{V}_2, \: \| v\| = \| w \| = 1 \big\}
:::

exists and is called the *norm* of the form $b$.
:::


:::{prf:example} 
The inner product on a (pre-) Hilbert space is bounded by the Cauchy--Schwarz inequality and has norm $1$.
:::



:::{prf:proposition} 
A bilinear or sesquilinear form $b : \mathrm{V}_1 \times \mathrm{V}_2 \to \mathbb{K}$ defined on the cartesian product of two normed vector space $\mathrm{V}_1$ and $\mathrm{V}_2$ over $\mathbb{K}$ is bounded if and only if it is continuous.
:::


:::{prf:proof}

If $b$ is bounded, then

:::{math}
\begin{split}
\big\vert b(v,w) - b(v',w') \big\vert \, &
\leq \big\vert b(v,w) - b(v',w) \big\vert + \big\vert b(v',w) - b(v',w') \big\vert \leq \\ & \leq \| b \| \, \left( \| w \| \, \| v-v'\| + \| v' \| \, \| w-w'\| \right)
\end{split}
:::

for all $v,v'\in \mathrm{V}_1$ and $w,w' \in \mathrm{V}_2$. Hence $b$ is locally Lipschitz continuous, so in particular continuous.

Conversely, assume now that $b$ is continuous. Then one can find $\delta > 0$ such that for all $v\in \mathrm{V}_1$ and $w\in \mathrm{V}_2$ of norm less than $\delta$ the relation $|b(v,w)| < 1$ holds true. But that entails for all non-zero $v,w$

:::{math}
|b(v,w)| = \frac{4 \, \|v\| \, \|w\| }{\delta^2} \cdot b\left( \delta \frac{v}{2 \|v\| }, \delta \frac{w}{2 \|w\| }\right)
\leq \frac{4}{ \delta^2} \|v\| \, \|w\| \ .
:::

Hence $b$ is bounded.
:::



:::{prf:remark} 
Given two normed vector spaces or more generally two topological vector spaces $\mathrm{V}_1$ and $\mathrm{V}_2$ one can consider bilinear or sesquilinear forms $b:\mathrm{V}_1 \times \mathrm{V}_2 \to \mathbb{K}$ which are only
*separately-continuous*. That means that for all $v\in \mathrm{V}_1$ the map $b_v = b(v,-) :\mathrm{V}_2 \to \mathbb{K}$ and for all $w \in \mathrm{V}_2$ the map $\overline{b}_w = b(-,w): \mathrm{V}_1 \to \mathbb{K}$ is continuous. In general, separate-continuity is strictly weaker than continuity unless the underlying vector spaces are Banach spaces where the two notions coincide as a consequence of the Banach--Steinhaus theorem. Let us prove this. By continuity of $b_v$ there exist $C_v \geq 0$ such that $| b_v (w)| \leq C_v \, \| w \| $ for all $w \in \mathrm{V}_2$ and $\overline{C}_w \geq 0$ such that $| \overline{b}_w (v)| \leq \overline{C}_w \, \| v \| $ for all $v \in \mathrm{V}_1$. Hence, for all $w\in \mathrm{V}_2$

:::{math}
\sup_{v\in \mathrm{V} , \: \|v\| \leq 1} | b_v (w)| =
\sup_{v\in \mathrm{V} , \: \|v\| \leq 1} | \overline{b}_w (v)| \leq \overline{C}_w < \infty \ .
:::

The Banach--Steinhaus theorem now entails

:::{math}
\sup_{v, w\in \mathrm{V} , \: \|v\| , \, \|w\| \leq 1} |b(v,w)| = \sup_{v\in \mathrm{V} , \: \|v\| \leq 1} \| b_v\| < \infty \ .
:::

Therefore, $b$ is bounded, so continuous by the preceding proposition.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionInner product spaces -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXOrthogonal decomposition and the Riesz representation theoremXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionOrthogonal decomposition and the Riesz representation theorem -->
# Orthogonal decomposition and the Riesz representation theorem
\para One of the issues with infinite-dimensional analysis is that a closed subspace of an infinite dimensional Banach space might not have a closed complement. Fortunately, the situation in Hilbert space theory is not so grim because every closed subspace of a Hilbert space admits an orthogonal complement. This is one of the four crucial properties which distinguish Hilbert spaces from Banach spaces and which are stated in the following.

In this section $\mathscr{H}$ will always denote a Hilbert space over the field $\mathbb{K}=\mathbb{R}$ or $\mathbb{K}=\C$. The symbol $\langle \cdot , \cdot\rangle$ will stand for the inner product of $\mathscr{H}$.


:::{prf:theorem} Best approximation theorem
Every closed convex nonempty subset $C$ of a Hilbert space $\mathscr{H}$ has a unique element of minimal norm.
:::


:::{prf:proof}

Let $d = \inf\{ \|v\| \mid v \in C \}$ which is a non-negative real number. We claim there exists a unique $v_0 \in C$ with $\|v_0\| =d$. For uniqueness, consider two vectors $v_0, v_1$ satisfying the desired property, and let $v = \frac{1}{2}(v_0 + v_1)$ be their midpoint. Then

:::{math}
\|v\| = \frac{1}{2}\|v_0 + v_1\| \leq \frac{1}{2}(\|v_0\| + \|v_1\|) = d
:::

By minimality of $d$ this entails $\|v\| =d$. By the parallelogram identity

:::{math}
\left\|\frac{1}{2} (v_0 + v_1)\right\|^2 + \left\|\frac{1}{2}(v_0 - v_1) \right\|^2 = 2\left\|\frac{v_0}{2}\right\|^2 + 2\left\|\frac{v_1}{2}\right\|^2 = d^2 \ ,
:::

hence

:::{math}
\left\| \frac{1}{2} (v_0 - v_1) \right\|^2 \leq d^2 - \|v\|^2 = 0 \ ,
:::

proving $v_0 = v_1$.

For the proof of existence observe that by definition of $d$ there exists a sequence $(v_n)_{n \in \mathbb{N}} \subset C$ such that $\lim_{n \to \infty}\|v_n \| = d$. By convexity

:::{math}
\frac{1}{2}(v_n + v_m) \in C
:::

for all $n,m \in \mathbb{N}$, hence $\frac{1}{4}\|v_n + v_m \|^2 \geq d^2$. The parallelogram equality entails

:::{math}
0 \leq \| v_n - v_m \|^2 = 2\|v_n \|^2 + 2\|v_m \|^2 - \| v_n + v_m \|^2 \leq 2\|v_n \|^2 + 2\|v_m \|^2 - 4d^2 \ .
:::

Since $\lim_{n \to \infty}\|v_n \| = d$ there exists for given $\varepsilon > 0$ an $N\in \mathbb{N}$ such that $ \|v_n \|^2 -d^2 \leq \frac 14 \varepsilon^2 $ for all $n \geq N$. Hence, for $n,m \geq N$

:::{math}
0 \leq \| v_n - v_m \| \leq \varepsilon \ ,
:::

and $(v_n)_{n \in \mathbb{N}}$ is a Cauchy-sequence, so convergent by completeness of $\mathscr{H}$. Put $v_0:= \lim_{n \to \infty}v_n$. Then $v_0 \in C$ since $C$ is closed and $\|v_0 \|=\lim_{n \to \infty}\|v_n \| = d$. The existence claim follows and the proof is finished.
:::



:::{prf:theorem} Orthogonal decomposition theorem
:label: thm:orthogonal-decomposition-theorem_1
Let $\mathrm{V} \subset \mathscr{H}$ be a closed subspace of the Hilbert space $\mathscr{H}$. Then the
*orthogonal complement*

:::{math}
\mathrm{V}^\bot = \big\{ w \in \mathscr{H} \bigm\vert \langle v,w \rangle = 0 \text{ for each } v \in \mathrm{V} \big\}
:::

is a closed subspace of $\mathscr{H}$ and $\mathscr{H} = \mathrm{V} \oplus \mathrm{V}^\bot$. The map $\operatorname{pr}_\mathrm{V} : \mathscr{H} \to \mathrm{V}$ which maps $w \in \mathscr{H}$ to the unique $w_1\in \mathrm{V}$ such that $w - w_1 \in \mathrm{V}^\bot$ is called the *orthogonal projection* onto $\mathrm{V}$. It satisfies $\left\| w- \operatorname{pr}_\mathrm{V} (w)\right\| = d(w,\mathrm{V}) := \inf \big\{ \| v-w \| \bigm\vert v\in \mathrm{V} \big\}$ that is $\operatorname{pr}_\mathrm{V} (w)$ is the unique element of $\mathrm{V}$ having shortest distance from $w$.
:::


:::{prf:proof}

For $v \in \mathscr{H}$ define $v^\flat :\mathscr{H} \to \mathbb{R}$ by $v^\flat (w) = \langle w,v \rangle$. Recall that this map is continuous and linear. Hence the kernel $(v^\flat)^{-1}(0)$ is a closed linear subspace of $\mathscr{H}$ and

:::{math}
:label: eq:expression-orthogonal-complement-intersection-kernels-linear-functionals_1
\mathrm{V}^{\bot} = \bigcap_{v \in \mathrm{V}} (v^\flat)^{-1}(0)
:::

is a closed linear subspace. To show $\mathrm{V} \cap \mathrm{V}^\bot = \{0\}$, consider $v \in \mathrm{V} \cap \mathrm{V}^\bot$. Then $\|v \|^2 = \langle v,v \rangle = 0$. Next we want to show that every $w \in \mathscr{H}$ can be written in the form $w = w_1 + w_2$ with $w_1 \in \mathrm{V}$ and $w_2 \in \mathrm{V}^\bot$. To see this put $C = w - \mathrm{V}$. Then $C$ is closed and convex. By the best approximation theorem there exists a unique element $w_2 \in C$ of minimal norm. Let $w_1$ be the unique element of $\mathrm{V}$ such that $w_2 = w -w_1$. It remains to show $w_2 \in \mathrm{V}^\bot$. Since $w_2$ has minimal norm among the elements of $w-\mathrm{V}$, the following inequality holds for all vectors $v \in \mathrm{V}$:

:::{math}
\|w_2 \|^2 \leq \| w_2 + v \|^2 = \|w_2 \|^2 + 2\, \Re\langle w_2,v\rangle + \| v \|^2 \ .
:::

Hence

:::{math}
0 \leq 2\, \Re\langle w_2,v\rangle + \| v \|^2 \quad \text{for all } v \in \mathrm{V} \ .
:::

Now assume that $\|v\|=1$ and choose $\varphi \in \mathbb{R}$ such that $e^{i\varphi}\langle w_2, v \rangle \in \mathbb{R}$. Setting $v' = e^{i\varphi}v$, one obtains for all $\lambda \in \mathbb{R}$ by the last inequality

:::{math}
0 \leq 2 \langle w_2,\lambda v'\rangle + \| \lambda v' \|^2 = 2\lambda\langle w_2, v'\rangle + \lambda^2\ .
:::

For $\lambda = -\langle w_2, v' \rangle$ this entails the estimate

:::{math}
| \langle w_2, v' \rangle |^2 = - \left( - 2 |\langle w_2,v' \rangle |^2 + | \langle w_2, v' \rangle |^2 \right) = - \left( 2\lambda\langle w_2, v'\rangle + \lambda^2 \right) \leq 0 \ .
:::

Hence $\langle w_2, v \rangle = 0$ for all unit vectors $v \in \mathrm{V}$, therefore $w_2 \in \mathrm{V}^\bot$.

The remainder of the claim is now an immediate consequence of the construction of $w_1$ from the given $w$ and the observation that $\operatorname{pr}_\mathrm{V} (w) = w_1$.
:::



:::{prf:corollary} 
For every subspace $\mathrm{V} \subset \mathscr{H}$ of a Hilbert space $\mathscr{H}$ the orthogonal complement $V^\perp$ is closed, and the relation

:::{math}
V^\perp = \overline{V}^\perp
:::

holds true. Moreover,

:::{math}
\overline{V} = (V^\perp)^\perp \ .
:::
:::



:::{prf:proof}

By \Crefeq:expression-orthogonal-complement-intersection-kernels-linear-functionals, the orthogonal complement $V^\perp$ is closed. Since $V \subset \overline{V}$ the inclusion $\overline{V}^\perp \subset V^\perp$ holds true. The converse inclusion $V^\perp \subset \overline{V}^\perp $ follows from the observation that if $w \in V^\perp$ and $(v_n)_{n\in \mathbb{N}}$ is a sequence in $V$ converging to some $v \in \overline{V}$, then

:::{math}
\langle w , v \rangle = \lim_{n\to\infty} \langle w, v_n \rangle = 0 \ .
:::

This proves the equality $V^\perp = \overline{V}^\perp$. The inclusion $ \overline{V} \subset (\overline{V}^\perp)^\perp = (V^\perp)^\perp $ is immediate by definition of the orthogonal complement. Since 
:::{math}
\mathscr{H} = \overline{V} \oplus V^\perp = (V^\perp)^\perp \oplus V^\perp
:::

by the preceding theorem, the equality $\overline{V} = (V^\perp)^\perp$ follows.
:::



:::{prf:theorem} Riesz representation theorem for Hilbert spaces
Let $\mathscr{H}$ be a Hilbert space and $\mathscr{H}'$ its topological dual. Then the *musical map*

:::{math}
{}^\flat: \mathscr{H} \to \mathscr{H}',\quad v \mapsto v^\flat = \left( \mathscr{H} \ni w \mapsto \langle v, w \rangle \in \mathbb{K}\right)
:::

is an isometric isomorphism which is linear in the real case and conjugate-linear in the complex case.
:::



:::{prf:proof}

Obviously, ${}^\flat$ is linear if the ground field $\mathbb{K}$ equals $\mathbb{R}$ and conjugate-linear if $\mathbb{K}=\C$. Now observe that for all $v \in \mathscr{H}$ by the Cauchy--Schwarz inequality

:::{math}
\| v^\flat \| = \sup\big\{ |\langle v, w \rangle | \bigm\vert w \in \mathscr{H} \: \& \: \|w\| =1 \big\} =
\| v \| \ ,
:::

hence ${}^\flat$ is an isometry, so in particular injective. It remains to show surjectivity. So assume that $\alpha : \mathscr{H} \to \mathbb{K}$ is a nontrivial continuous linear form. Let $\mathrm{V}$ be its kernel. Then $\mathrm{V}$ is a closed linear subspace of $\mathscr{H}$. Since $\alpha$ is nontrivial, the orthogonal complement $\mathrm{V}^\bot$ is nontrivial, too. Hence $\mathrm{V}^\bot \cong \mathscr{H}/\mathrm{V}$ is isomorphic to $\operatorname{im} \alpha = \mathbb{K}$ and there exists a vector $v \in \mathrm{V}^\bot \setminus \{ 0 \} $ such that $\alpha (v) = 1$. Since $v$ spans $ \mathrm{V}^\bot$ there exists for every $w\in \mathscr{H}$ a unique $\lambda_w \in \mathbb{K}$ such that $w = \operatorname{pr}_V (w) + \lambda_w v$. Then compute

:::{math}
\alpha (w) = \alpha (\lambda_w v ) = \lambda_w \quad \text{and} \quad
\left( \frac{v}{\|v\|^2}\right)^\flat (w) =
\frac{1}{\|v\|^2} \langle v, w \rangle = \frac{ \lambda_w}{\|v\|^2} \langle v , v \rangle = \lambda_w \ .
:::

This entails $\alpha = \left( \frac{v}{\|v\|^2}\right)^\flat$, and ${}^\flat$ is surjective.
:::



:::{prf:remark} 
Sometimes in the Hilbert space literature the inverse of the musical isomorphism ${}^\flat: \mathscr{H} \to \mathscr{H}'$ is denoted ${}^\sharp: \mathscr{H}' \to \mathscr{H}$. We will follow that convention.
:::



:::{prf:corollary} 
Every Hilbert space $\mathscr{H}$ is *reflexive* that is the canonical map

:::{math}
H \to H'' , \: v \mapsto \left( H' \ni \lambda \mapsto \lambda(v) \in \mathbb{K} \right)
:::

is an isometric isomorphism.
:::



:::{prf:proof}

By the Riesz Representation Theorem, the dual $\mathscr{H}'$ is a Hilbert space with inner product

:::{math}
\langle\!\langle \cdot, \cdot \rangle\!\rangle : \mathscr{H}' \times \mathscr{H}' \to \mathbb{K}, \: (\lambda,\mu) \mapsto \langle\!\langle \lambda, \mu \rangle\!\rangle = \langle \mu^\sharp,\lambda^\sharp \rangle \ .
:::

Hence, by applying the Riesz Representation Theorem twice, the map ${}^\flat \circ {}^\flat : \mathscr{H} \to \mathscr{H}''$ is an isometric linear isomorphism. Now compute for $v\in \mathscr{H}$ and $\lambda \in \mathscr{H}'$

:::{math}
(v^\flat)^\flat (\lambda) = \langle\!\langle v^\flat,\lambda \rangle\!\rangle =
\langle  \lambda^\sharp, v \rangle = \lambda (v) \ .
:::

Hence ${}^\flat \circ {}^\flat$ coincides with the canonical map above and the claim follows.
:::



:::{prf:corollary} 
:label: thm:correspondence-bounded-sesquilinear-forms-bounded-operators_1
Let $\mathscr{H}_1$ and $\mathscr{H}_2$ be two Hilbert spaces and $b:\mathscr{H}_1 \times \mathscr{H}_2 \to \mathbb{K}$ a bounded sesquilinear form. Then there exists unique bounded linear map $A : \mathscr{H}_2 \to \mathscr{H}_1$ such that

:::{math}
:label: eq:sesquilinear-form-expressed-inner-product-bounded-operator_1
b(v,w) = \langle v,Aw \rangle \quad \text{for all } v \in \mathscr{H}_1 ,\: w\in \mathscr{H}_2 \ .
:::

Moreover, the operator norm $\| A \|$ coincides with $\| b\|$.
:::


:::{prf:proof}

First let us show uniqueness. So let $A,B : \mathscr{H}_2 \to \mathscr{H}_1$ be bounded and linear so that

:::{math}
b(v,w) = \langle v,Aw \rangle = \langle v,Bw \rangle \quad \text{for all } v\in \mathscr{H}_1 , \: w\in \mathscr{H}_2 \ .
:::

Then $ \|(A-B)w \|^2 = \langle (A-B)w,Aw-Bw \rangle = b((A-B)w,w) - b((A-B)w,w)= 0$ for all $w\in \mathscr{H}_2$ which entails equality of $A$ and $B$.

To prove existence observe that for every $w\in \mathscr{H}_2$ the map

:::{math}
\overline{b}_w : \mathscr{H}_1 \to \mathbb{K}, \: v \mapsto \overline{b} (w,v) :=
\overline{b(v,w)}
:::

is bounded and linear, so by the Riesz representation theorem there exists for every $w$ a unique element $Aw \in \mathscr{H}_1$ such that $\langle Aw,v \rangle = \overline{b}(w,v)$ for all $v\in \mathscr{H}_1$. By construction, $Aw = (\overline{b}_w)^\sharp$. Since the maps $\mathscr{H}_2 \to \mathscr{H}_1^\prime$, $ w \mapsto \overline{b}_w$ and ${}^\sharp: \mathscr{H}_1^\prime \to \mathscr{H}_1$ are both conjugate-linear, $A$ is linear. Hence $A$ is the desired linear operator fulfilling
\Crefeq:sesquilinear-form-expressed-inner-product-bounded-operator.

For the operator norm compute

:::{math}
\begin{split}
\| A \| & = \sup \big\{ \left|\langle v,Aw \rangle \right| \bigm\vert v\in \mathscr{H}_1,\: w\in \mathscr{H}_2, \: \|v\| = \|w\| =1 \big\} = \\ & = \sup \big\{ \left| b(v,w) \right| \bigm\vert v\in \mathscr{H}_1,\: w\in \mathscr{H}_2, \: \|v\| = \|w\| =1 \big\} = \| b\| \ .
\end{split}
:::

Hence $A$ is bounded with operator norm equal to $\| b\|$ and the claim is proved.
:::


\para Last in this section we will examine the *Hilbert direct sum* or just *Hilbert sum* of a family $(\mathscr{H}_i)_{i\in I}$ of Hilbert spaces. It is defined by

:::{math}
\begin{split}
\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i & = \left\{ (v_i)_{i\in I} \in \prod_{i\in I}\mathscr{H}_i
\Bigm\vert \left( \|v_i\|^2 \right)_{i\in I} \text{ is summable} \right\} = \\ & = \left\{ (v_i)_{i\in I} \in \prod_{i\in I}\mathscr{H}_i
\Bigm\vert \exists C \geq 0 \, \forall J \in \mathscr{P}_{fin}(I) : \: \sum_{i\in J} \|v_i\|^2 \leq C \right\} \ ,
\end{split}
:::

where, as usual, $\mathscr{P}_{fin}(I)$ denotes the set of all finite subsets of $I$.


:::{prf:proposition} 
Let $(\mathscr{H}_i)_{i\in I}$ be a family of Hilbert spaces. Then the Hilbert direct sum $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$ is a Hilbert space with inner product given by

:::{math}
\langle -,- \rangle : \widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i \times
\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i \to \mathbb{K}, \quad
\left( (v_i)_{i\in I} , (w_i)_{i\in I} \right) \mapsto \sum_{i\in I} \langle v_i,w_i \rangle \ .
:::
:::



:::{prf:proof}

We show first that $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$ is a subvector space of the direct product $\prod_{i\in I} \mathscr{H}_i$. Let $z\in \mathbb{K}$ and $(v_i)_{i\in I}, (w_i)_{i\in I}\in \widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$. Choose $C,D \geq 0$ such that

:::{math}
\sum_{i\in J} \|v_i\|^2 \leq C \quad\text{and}\quad
\sum_{i\in J} \|w_i\|^2 \leq D \quad\text{for all } J \in \mathscr{P}_{fin}(I) \ .
:::

Then

:::{math}
:label: eq:estimate-finite-sum-square-norms-multiple_1
\sum_{i\in J} \|z v_i\|^2 = |z| \, \sum_{i\in J} \| v_i\|^2\leq |z| \, C \quad
\text{for all } J\in \mathscr{P}_{fin}(I) \ ,
:::

so $(zv_i)_{i\in I} \in \widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$. Moreover, by Minkowski's inequality for finite sums,

:::{math}
:label: eq:estimate-finite-sum-square-norms-sum_1
\sum_{i\in J} \|v_i + w_i\|^2 \leq
\left( \sqrt{\sum_{i\in J} \|v_i\|^2} + \sqrt{\sum_{i\in J} \| w_i\|^2} \right)^2
\leq \left( \sqrt{C} + \sqrt{D} \right)^2 \quad\text{for all } J\in \mathscr{P}_{fin}(I) \ .
:::

Hence the family $\left( \| v_i + w_i\|^2 \right)_{i\in I}$ is summable and $\left( v_i + w_i \right)_{i\in I} \in \widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$.

Next observe that the map

:::{math}
\big\| - \big\| : \widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i \to \mathbb{K},
\: (v_i)_{i\in I} \mapsto \big\| (v_i)_{i\in I} \big\| = \sqrt{\sum_{i\in I} \| v_i\|^2}
:::

is well-defined by definition of the Hilbert direct sum. It is even a norm by {eq}`eq:estimate-finite-sum-square-norms-multiple_1` and
{eq}`eq:estimate-finite-sum-square-norms-sum_1`.

Now we need to show that the inner product on $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$ is well-defined which means that the family $\left( \langle v_i,w_i \rangle \right)_{i\in I}$ is summable for all $(v_i)_{i\in I} , (w_i)_{i\in I} \in \widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$. To this end let $J\subset I$ be a finite subset. Then, by the triangle inequality, the Cauchy--Schwarz inequality on the Hilbert spaces $\mathscr{H}_i$ and the Cauchy--Schwarz inequality for finite sums,

:::{math}
\left| \sum_{i\in J} \langle v_i,w_i \rangle \right| \leq
\sum_{i\in J} \left| \langle v_i,w_i \rangle \right| \leq
\sum_{i\in J} \| v_i\| \, \| w_i\| \leq
\sqrt{\sum_{i\in J} \| v_i\|^2} \cdot \sqrt{\sum_{i\in J} \| w_i\|^2}
\leq \big\| (v_i)_{i\in I} \big\| \, \big\| (w_i)_{i\in I} \big\| \ .
:::

Hence the family $\left( \langle v_i,w_i \rangle \right)_{i\in I}$ is absolutely summable, so in particular summable, and the inner product is well-defined.

By definition and since all the inner products on the Hilbert spaces $\mathscr{H}_i$ are conjugate symmetric and positive definite, the map $\langle -,- \rangle $ on $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$ has to be conjugate symmetric and positive definite as well. It remains to show linearity in the second argument. Denote for $(v_i)_{i\in I}, (w_i)_{i\in I} \in \prod_{i\in I} \mathscr{H}_i$ and $J\in \mathscr{P}_{fin}(I)$ by $\langle (v_i)_{i\in I} ,(w_i)_{i\in I} \rangle_J$ the finite sum $\sum_{i\in J} \langle v_i,w_i \rangle$. Observe that the net $\big( \langle (v_i)_{i\in I} ,(w_i)_{i\in I} \rangle_J \big)_{J\in \mathscr{P}_{fin}(I)}$ converges to $\langle (v_i)_{i\in I} ,(w_i)_{i\in I} \rangle$ in case both $(v_i)_{i\in I}$ and $(w_i)_{i\in I}$ are in $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$. Now let $z\in \mathbb{K}$ and $(v_i)_{i\in I}, (w_i)_{i\in I}, (w^\prime_i)_{i\in I} \in \widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$. Then

:::{math}
\begin{split}
\langle (v_i)_{i\in I}, (w_i)_{i\in I} + (w^\prime_i)_{i\in I} \rangle_J & =
\langle (v_i)_{i\in I} ,(w_i)_{i\in I} \rangle_J + \langle (v_i)_{i\in I},(w^\prime_i)_{i\in I} \rangle_J
\quad\text{and}\\
\langle  (v_i)_{i\in I},z(w_i)_{i\in I} \rangle_J & = z \langle (v_i)_{i\in I} ,(w_i)_{i\in I} \rangle_J \ .
\end{split}
:::

By convergence of all the nets $\big( \langle (v_i)_{i\in I} ,(w_i)_{i\in I} \rangle_J \big)_{J\in \mathscr{P}_{fin}(I)}$, linearity in the second argument follows.

By construction, the norm associated to the inner product $\langle -,- \rangle $ on $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$ coincides with the above defined norm $\big\|-\big\|$. It remains to show that $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$ equipped with the norm $\big\|-\big\|$ is complete. To this end observe that for every finite $J\subset I$ the map

:::{math}
\big\| - \big\|_J : \prod_{i\in I} \mathscr{H}_i \to \mathbb{R}_{\geq 0}, \: (v_i)_{i\in I} \mapsto \sqrt{\langle (v_i)_{i\in I},(v_i)_{i\in I} \rangle_J}
= \sqrt{\sum_{i\in J} \| v_i \|^2}
:::

is a seminorm and that $(v_i)_{i\in I} \in \prod_{i\in I} \mathscr{H}_i$ lies in the Hilbert direct sum $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$ if and only if the family $\left(\big\| (v_i)_{i\in I} \big\|_J\right)_{J\in \mathscr{P}_{fin}(I)}$ is bounded. Now let $\left((v_i^n)_{i\in I} \right)_{n\in \mathbb{N}}$ be a Cauchy sequence. Let $\varepsilon > 0$ and choose $N_\varepsilon \in \mathbb{N}$ such that

:::{math}
:label: eq:cauchy-criterion-sequence-hilbert-direct-sum_1
\big\| (v_i^m)_{i\in I} - (v_i^n)_{i\in I} \big\| < \varepsilon \quad
\text{for all } n,m\geq N_\varepsilon \ .
:::

Then

:::{math}
:label: eq:cauchy-criterion-sequence-finite-cutoff_1
\big\| (v_i^m)_{i\in I} - (v_i^n)_{i\in I} \big\|_J < \varepsilon \quad
\text{for all } J\in \mathscr{P}_{fin}(I) \text{ and } n,m\geq N_\varepsilon \ .
:::

Taking $J =\{ j\}$ for $j\in I$ this implies that the sequence $ (v_j^n)_{n\in \mathbb{N}}$ is a Cauchy sequence in the Hilbert space $\mathscr{H}_j$. Let $v_j \in \mathscr{H}_j$ be its limit. The family $(v_i)_{i\in I}$ then is an element of $\widehat{\bigoplus\limits_{i\in I}} \mathscr{H}_i$. To verify this put $N=N_1$ and observe that by {eq}`eq:cauchy-criterion-sequence-finite-cutoff_1`
for all finite $J\subset I$

:::{math}
\begin{split}
\big\| (v_i)_{i\in I} \big\|_J & \leq
\big\| (v_i^N)_{i\in I} \big\|_J + \big\| (v_i)_{i\in I} - (v_i^N)_{i\in I} \big\|_J = \\ & = \big\| (v_i^N)_{i\in I} \big\|_J + \lim_{m\to \infty} \big\| (v_i^m)_{i\in I} - (v_i^N)_{i\in I} \big\|_J
\leq \big\| (v_i^N)_{i\in I} \big\| + 1.
\end{split}
:::


Hence the family $\left(\big\| (v_i)_{i\in I} \big\|_J\right)_{J\in \mathscr{P}_{fin}(I)}$ is bounded and $(v_i)_{i\in I}$ lies in the Hilbert direct sum of the spaces $\mathscr{H}_i$, $i\in I$. Moreover, {eq}`eq:cauchy-criterion-sequence-finite-cutoff_1` entails that

:::{math}
\big\| (v_i)_{i\in I} - (v_i^n)_{i\in I} \big\|_J =
\lim_{m\to \infty} \big\| (v_i^m)_{i\in I} - (v_i^n)_{i\in I} \big\|_J \leq \varepsilon \quad
\text{for all } J\in \mathscr{P}_{fin}(I) \text{ and } n\geq N_\varepsilon \ .
:::

Since $\big\| (v_i)_{i\in I} - (v_i^n)_{i\in I} \big\|$ is the limit of the net $\left(\big\| (v_i)_{i\in I} - (v_i^n)_{i\in I} \big\|_J\right)_{J\in \mathscr{P}_{fin}(I)}$, the estimate

:::{math}
\big\| (v_i)_{i\in I} - (v_i^n)_{i\in I} \big\| \leq \varepsilon \quad
\text{for all } n\geq N_\varepsilon
:::

follows, and the sequence $\left((v_i^n)_{i\in I} \right)_{n\in \mathbb{N}}$ convergences to $(v_i)_{i\in I}$. This finishes the proof.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionOrthogonal decomposition and the Riesz representation theorem -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXOrthonormal bases in Hilbert spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionOrthonormal bases in Hilbert spaces -->
(sec:orthonormal-baes-hilbert-spaces_1)=
# Orthonormal bases in Hilbert spaces
:::{prf:definition} 
A (possibly empty) subset $S$ of a Hilbert space $\mathscr{H}$ is called an *orthogonal system* or just *orthogonal* if for any two different elements $v,w \in S$ the relation $\langle v,w \rangle = 0$ holds true. If in addition $\left\|v\right\|=1$ for all elements $v \in S$, then the set is called *orthonormal* or an *orthonormal system*. A family $(v_i)_{i\in I}$ of vectors in $\mathscr{H}$ is called *orthogonal* if $\langle v_i,v_j \rangle = 0$ for all $i,j\in I$ with $i\neq j$ and *orthonormal*
if in addition $\|v_i\| =1$ for all $i\in I$.
:::


\para Obviously, the set of orthonormal subsets of a Hilbert space is ordered by set-theoretic inclusion. Therefore, the following definition makes sense.


:::{prf:definition} 
A maximal orthonormal set in a Hilbert space $\mathscr{H}$ is called an *orthonormal basis*
or a *Hilbert basis* of $\mathscr{H}$.
:::



:::{prf:proposition} 
Every Hilbert space $\mathscr{H}$ has an orthonormal basis.
:::



:::{prf:proof}

Wothout loss of generality we can assume that $\mathscr{H} \neq \{ 0\}$, because $\emptyset$ is a Hilbert basis for $\{ 0 \}$. Let $\mathscr{O}$ denote the set of orthonormal subsets of $\mathscr{H}$. As mentioned before, $\mathscr{O}$ is ordered by set-theoretic inclusion. Let $\mathscr{C} \subset \mathscr{O}$ be a non-empty chain. Put $U = \bigcup_{S\in \mathscr{C}} S$. Then $U$ is an upper bound of $\mathscr{C}$. So by Zorn's lemma $\mathscr{O}$ has a maximal element.
:::



:::{prf:remark} 


\itemindent
: By slight abuse of language we sometimes call an orthonormal family $(b_i)_{i\in I}$ in a Hilbert space $\mathscr{H}$ an *orthonormal basis* or a *Hilbert basis* of $\mathscr{H}$ if the set $\{ b_i \mid i\in I \}$ is an orthornormal basis.

\itemindent
: If on an orthonormal basis $B \subset \mathscr{H}$ a total order relation is given, one calls $B$ an *ordered Hilbert basis* of $\mathscr{H}$. Likewise, an orthonormal basis of the form $(b_i)_{i\in I}$ is called *ordered* if the index set $I$ carries a total order.
:::



:::{prf:proposition} Pythagorean theorem for orthogonal families
:label: thm:pythagorean-theorem-infinite-families_1

An orthogonal family $(v_i)_{i\in I}$ in a Hilbert space $\mathscr{H}$ is summable if and only if the family of norms $\left(\|v_i\| \right)_{i\in I}$ is square summable. In this case one has

:::{math}
\Big\|\sum_{i\in I} v_i\Big\|^2 = \sum_{i\in I} \|v_i\|^2 \ .
:::
:::



:::{prf:proof}

Assume that $\left(\|v_i\| \right)_{i\in I}$ is square summable or in other words that the net of partial sums $\left( \sum_{i\in J} \|v_i\|^2 \right)_{J\in\mathscr{P}_{fin}(I)}$ converges to some $s \in \mathbb{R}$. For $\varepsilon > 0$ choose a finite $J_\varepsilon \subset I$ such that for all finite $J$ with $J_\varepsilon \subset J\subset I$ the relation

:::{math}
\Big| s - \sum_{i\in J} \|v_i\|^2 \Big| < \frac{\varepsilon^2}{2}
:::

holds true. For finite $K\subset I$ with $K\cap J_\varepsilon =\emptyset$ one then obtains by the pythagorean theorem for finite orthogonal families, Eq.~({eq}`eq:pythagorean-theorem_1`),

:::{math}
\Big\| \sum_{i\in K} v_i\Big\|^2 = \sum_{i\in K} \left\| v_i\right\|^2 \leq
\Big| s - \sum_{i\in K \cup J_\varepsilon} \|v_i\|^2 \Big| + \Big| s - \sum_{i\in J_\varepsilon} \|v_i\|^2 \Big| < \varepsilon^2 \ .
:::

Hence $\left( \sum_{i\in J} v_i \right)_{J\in\mathscr{P}_{fin}(I)}$ is a Cauchy net in $\mathscr{H}$, so convergent.

Now let $(v_i)_{i\in I}$ be summable to $v\in \mathscr{H}$. Then there exists a $J_1 \in \mathscr{P}_{fin}(I)$ such that for all finite $J \subset I$ containing $J_1$

:::{math}
\Big\| v - \sum_{i\in J} v_i \Big\| \leq 1 \ .
:::

This implies by the pythagorean theorem for finite orthogonal families

:::{math}
\sum_{i\in J} \left\| v_i \right\|^2 = \Big\| \sum_{i\in J} v_i \Big\|^2 \leq
\left( \Big\| v - \sum_{i\in J} v_i \Big\| + \left\| v \right\| \right)^2 \leq ( 1 + \| v\| )^2 \ .
:::

Therefore, the net of partial sums $\left( \sum_{i\in J} \|v_i\|^2 \right)_{J\in\mathscr{P}_{fin}(I)}$ is bounded, so convergent since each term $\|v_i\|^2$ is non-negative.

By continuity of the inner product and pairwise orthogonality of the $v_i$ one finally obtains in the convergent case

:::{math}
\Big\| \sum_{i\in I} v_i \Big\|^2 = \Big\langle \sum_{i\in I} v_i, \sum_{j\in I} v_j\Big\rangle =
\sum_{i\in I} \Big\langle v_i, \sum_{j\in I} v_j\Big\rangle =
\sum_{i\in I} \sum_{j\in I} \langle  v_i, v_j \rangle = \sum_{i\in I} \left\| v_i \right\|^2 \ .
:::
:::



:::{prf:proposition} 
Let $(v_i)_{i\in I}$ be an orthonormal family in a Hilbert space $\mathscr{H}$. Then for every $v \in \mathscr{H}$ the family $\left( \langle v_i,v \rangle \right)_{i\in I}$ is square summable and
*Bessel's inequality* holds true that is

:::{math}
\sum_{i\in I} \left| \langle v_i,v \rangle \right|^2 \leq \| v \|^2 \ .
:::
:::



:::{prf:proof}

Let $J \subset I$ be finite. Then, by the pythagorean theorem for finite orthogonal families

:::{math}
0 \leq \Big\| v - \sum_{i\in J} \langle v_i,v \rangle v_i \Big\|^2 =
\| v\|^2 - 2 \sum_{i\in J} | \langle v_i,v \rangle |^2 + \Big\| \sum_{i\in J} \langle v_i,v \rangle v_i \Big\|^2 = \| v\|^2 - \sum_{i\in J} | \langle v_i,v \rangle |^2 \ .
:::

Therefore, for all $J\in \mathscr{P}_{fin}(I) $

:::{math}
:label: eq:bessel-inequality-finite-orthogonal-families_1
\sum_{i\in J} \left| \langle v_i,v \rangle \right|^2 \leq \| v \|^2 \ .
:::

Hence, by \Crefthm:summability-criteria-family-complex-numbers, the family $(\left| \langle v_i,v \rangle \right|)_{i\in I}$ is square summable. Bessel's inequality now follows from the observation that in
\Crefeq:bessel-inequality-finite-orthogonal-families one can pass over to the limit of the net $\left( \sum_{i\in J} \left| \langle v_i,v \rangle \right|^2 \leq \| v \|^2\right)_{J\in \mathscr{P}_{fin}(I)}$.
:::



:::{prf:theorem} 
Let $B$ be an orthonormal system in a Hilbert space $\mathscr{H}$. Then the following are equivalent:



(ite:orthonormal-system-maximal_1)=
(1)
: The orthonormal system $B$ is maximal, i.e.a Hilbert basis.

(ite:orthonormal-system-total_1)=
(2)
: The orthonormal system $B$ is *total* that is for all $v \in H$ such that $\langle v, b \rangle = 0$ for all $b \in B$ the equality $v = 0$ holds true.

(ite:orthonormal-system-isomorphism_1)=
(3)
: For every $b\in B$ let $\mathscr{H}_b = \{ r b \in \mathscr{H} \mid r \in \mathbb{K}\}$. Then the canonical map
   
   :::{math}
   \iota: \widehat{\bigoplus_{b \in B}} \mathscr{H}_b \to \mathscr{H} , \: (v_b)_{b \in B} \mapsto \sum_{b \in B} v_b
   :::
   
   is an isometric isomorphism.

(ite:orthonormal-system-closed-span_1)=
(4)
: The closed linear span of $B$ coincides with $\mathscr{H}$.

(ite:orthonormal-system-fourier-expansion_1)=
(5)
: For all $v \in \mathscr{H}$, one has the
   *Fourier expansion*
   
   :::{math}
   v = \sum_{b \in B} \langle v, b \rangle b \ .
   :::

(ite:orthonormal-system-inner-product-expansion_1)=
(6)
: For all $v, w \in \mathscr{H}$, one has
   
   :::{math}
   \langle v, w \rangle = \sum_{b \in B}\langle v, b \rangle \langle b, w \rangle \ .
   :::

(ite:orthonormal-system-parsevals-identity_1)=
(7)
: For all $v \in \mathscr{H}$, *Parseval's identity* holds true that is
   
   :::{math}
   \left\|v\right\|^2 = \sum_{b \in B} {\left|\langle v, b \rangle\right|}^2 \ .
   :::
:::



:::{prf:proof}

{ref}`ite:orthonormal-system-maximal_1` $\Rightarrow$ {ref}`ite:orthonormal-system-total_1`: If $v \neq 0$, then $\frac{v}{\left\|v\right\|}$ is a unit vector orthogonal to each $v_i$. Hence $\{v\} \cup B$ is an orthonormal system which is strictly larger than $B$, contradicting {ref}`ite:orthonormal-system-maximal_1`.

{ref}`ite:orthonormal-system-total_1` $\Rightarrow$ {ref}`ite:orthonormal-system-isomorphism_1`. First note that by the pythagorean theorem for infinite families, \Crefthm:pythagorean-theorem-infinite-families, the canonical map $\iota: \widehat{\bigoplus}_{b \in B} H_b \rightarrow H$ is well-defined and an isometry. Hence $\iota$ is injective. It remains to show that $\iota$ is surjective. To this end observe that $\operatorname{im} \iota$ is closed in $\mathscr{H}$ since $\iota$ is an isometry (the image is complete). If $\iota$ is not surjective, then $\operatorname{im} \iota^\perp$ is not the zero vector space. Choose $v \in \operatorname{im} \iota^\perp \setminus \{ 0\}$. Then $v$ is orthogonal to each element of $B$, but $v \neq 0$. This contradicts
{ref}`ite:orthonormal-system-total_1`, so $\operatorname{im} \iota = \mathscr{H}$.

{ref}`ite:orthonormal-system-isomorphism_1` $\Rightarrow$ {ref}`ite:orthonormal-system-fourier-expansion_1`: We can represent any $v \in \mathscr{H}$ in the form $v = \iota \left( (v_b)_{b \in B} \right) =
\sum_{b\in B} v_b$ with $\left( v_b \right)_{b\in B} \in \widehat{\bigoplus}_{b \in B} H_b$. Write $v_b = r_b \, b$ for every $b\in B$, where $r_b \in \mathbb{K}$ is uniquely determined by $v_b$. Then compute using continuity of the inner product

:::{math}
\langle v, b \rangle = \langle \sum_{c \in B} v_c, b \rangle = \sum_{c \in B} r_c \langle c, b \rangle = r_b \ .
:::

Therefore,

:::{math}
v = \sum_{b \in B} r_b \, b = \sum_{b \in B} \langle v, b \rangle b \ .
:::


{ref}`ite:orthonormal-system-fourier-expansion_1` $\Rightarrow$ {ref}`ite:orthonormal-system-inner-product-expansion_1`: Fourier expansion of $v, w \in H$ gives $v = \sum\limits_{b \in B} \langle v, b \rangle b$ and $w = \sum\limits_{b \in B} \langle w, b \rangle b$. Then, by continuity of the inner product,

:::{math}
\langle v, w \rangle = \sum\limits_{b \in B} \langle v, b \rangle\langle b, w \rangle \ .
:::


{ref}`ite:orthonormal-system-fourier-expansion_1` $\Rightarrow$ {ref}`ite:orthonormal-system-closed-span_1`: Let $v\in \mathscr{H}$. Then $\sum\limits_{b\in J}\langle v, b \rangle b \in \operatorname{Span} (B)$ for all finite $J \subset B$. By Fourier expansion $v$ is the limit of the net $\left( \sum\limits_{b\in J}\langle v, b \rangle b \right)_{J\in \mathscr{P}_{fin}(B)} $, so $v$ lies in the closure $\widebar{\operatorname{Span}} (B)$.

{ref}`ite:orthonormal-system-closed-span_1` $\Rightarrow$ {ref}`ite:orthonormal-system-total_1`: Assume that $\langle v, b \rangle = 0$ for all $b \in B$. By {ref}`ite:orthonormal-system-closed-span_1`, $v$ can be written as a limit $v = \lim\limits_{n\to\infty} v_n$, where $v_n \in \operatorname{Span} (B)$ for all $n\in \mathbb{N}$. Then $\langle v, v_n \rangle = 0$ for all $n\in \mathbb{N}$ by assumption. By continuity of the inner product this implies

:::{math}
\left\|v\right\|^2 = \lim\limits_{n\to\infty} \langle v, v_n \rangle = 0 \ ,
:::

so $v=0$.

{ref}`ite:orthonormal-system-inner-product-expansion_1` $\Rightarrow$ {ref}`ite:orthonormal-system-parsevals-identity_1`: Put $v = w$. Then, by assumption,

:::{math}
\left\|v\right\|^2 = \langle v, v \rangle = \sum\limits_{b\in B} \langle v, b \rangle \langle b, v \rangle = \sum\limits_{b \in B} {\left|\langle v, b \rangle\right|}^2 \ .
:::


{ref}`ite:orthonormal-system-parsevals-identity_1` $\Rightarrow$ {ref}`ite:orthonormal-system-maximal_1`: Assume {ref}`ite:orthonormal-system-parsevals-identity_1` and that {ref}`ite:orthonormal-system-maximal_1` is not true. Then there exists $v \in H$ with $\left\|v\right\| = 1$ and $\langle v, b \rangle = 0$ for all $b \in B$. But then

:::{math}
\left\|v\right\|^2 = \sum_{b \in B} {\left|\langle v, b \rangle\right|}^2 = 0,
:::

which is a contradiction.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionOrthonormal bases in Hilbert spaces -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe monoidal structure of the category of Hilbert spacesXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe monoidal structure of the category of Hilbert spaces -->
(sec:monoidal-structure-category-hilbert-spaces_1)=
# The monoidal structure of the category of Hilbert spaces
\para Let $\mathbb{K}$ be the field of real or complex numbers. Hilbert spaces over $\mathbb{K}$ together with bounded $\mathbb{K}$-linear maps between them form a category denoted by $\mathbb{K}\text{-}\mathsf{Hilb}$ or just $\mathsf{Hilb}$ if no confusion can arise. This can be seen immediately by observing that the identity map $\mathbbm{1}_\mathscr{H}$ on a Hilbert space is a bounded linear operator and that the composition $B \circ A : \mathscr{H}_1 \to\mathscr{H}_3$ of two bounded linear operators between Hilbert spaces $A:\mathscr{H}_1 \to \mathscr{H}_2 $ and $B :\mathscr{H}_2 \to \mathscr{H}_3$ is again a bounded linear operator. We want to endow the category $\mathsf{Hilb}$ with a bifunctor $ {\,\widehat{\otimes}\,} : \mathsf{Hilb} \times \mathsf{Hilb} \to \mathsf{Hilb}$ so that it becomes a monoidal category. The (bi)functor ${\,\widehat{\otimes}\,}$ will be called the *Hilbert tensor product*.

Unless mentioned differently, Hilbert spaces, vector spaces and the algebraic tensor product $\otimes$ in this section are assumed to be taken over the ground field $\mathbb{K}$.


:::{prf:proposition} 
:label: thm:construction-tensor-inner-product_1
Let $\mathscr{H}_1$ and $\mathscr{H}_2$ be two Hilbert spaces. Then there exists a unique inner product $\langle \cdot,\cdot \rangle: (\mathscr{H}_1 \otimes \mathscr{H}_2) \times (\mathscr{H}_1 \otimes \mathscr{H}_2)
\to \mathbb{K} $ on the algebraic tensor product $\mathscr{H}_1\otimes \mathscr{H}_2$ such that

:::{math}
:label: eq:defining-relation-inner-product-tensor-product_1
\langle v_1 \otimes v_2 , w_1 \otimes w_2 \rangle = \langle v_1,w_1 \rangle \cdot \langle v_2,w_2 \rangle
\quad\text{for all } v_1,w_1 \in \mathscr{H}_1, \: v_2,w_2 \in \mathscr{H}_2 \ .
:::
:::



:::{prf:proof}

Let us first provide some preliminary constructions. Recall that for every pair of vector spaces $\mathrm{V}_1$ and $\mathrm{V}_2$ the bilinear map

:::{math}
\begin{split}
\tau: \operatorname{Hom}\nolimits (\mathrm{V}_1 ,\mathbb{K}) \times \operatorname{Hom}\nolimits (\mathrm{V}_2,\mathbb{K}) & \to
\operatorname{Hom}\nolimits (\mathrm{V}_1 \otimes \mathrm{V}_2,\mathbb{K}), \\ (\lambda_1,\lambda_2) & \mapsto \big( \mathrm{V}_1 \otimes \mathrm{V}_2 \to \mathbb{K}, \: v_1 \otimes v_2 \mapsto \lambda_1 (v_1) \cdot\lambda_2 (v_2) \big)
\end{split}
:::

induces a linear map

:::{math}
\widehat{\tau}: \operatorname{Hom}\nolimits (\mathrm{V}_1 ,\mathbb{K}) \otimes \operatorname{Hom}\nolimits (\mathrm{V}_2,\mathbb{K}) \to
\operatorname{Hom}\nolimits (\mathrm{V}_1 \otimes \mathrm{V}_2,\mathbb{K})
:::

by the universal property of the tensor product. This map is an isomorphism. To see this choose a basis $(v_{1i})_{i\in I} $ of $V_1$ and a basis $(v_{2j})_{j\in J} $ of $V_2$. Let $(v^\prime_{1i})_{i\in I} $ and $(v^\prime_{2j})_{j\in J} $ denote the respective dual bases of $V_1^\prime$ and $V_2^\prime$. Then $\left( v^\prime_{1i} \otimes v^\prime_{2j}\right)_{(i,j)\in I \times J}$ is a basis of $\operatorname{Hom}\nolimits (\mathrm{V}_1 ,\mathbb{K}) \otimes \operatorname{Hom}\nolimits (\mathrm{V}_2,\mathbb{K})$ which under $\widehat{\tau}$ is mapped bijectively to the basis $\left( (v_{1i} \otimes v_{2j})^\prime \right)_{(i,j)\in I \times J}$ of $\operatorname{Hom}\nolimits (\mathrm{V}_1 \otimes \mathrm{V}_2,\mathbb{K})$ dual to the basis $\left( v_{1i} \otimes v_{2j}\right)_{(i,j)\in I \times J}$ of $\mathrm{V}_1 \otimes \mathrm{V}_2$. Hence $\widehat{\tau}$ is a linear isomorphism as claimed, and we can identify the tensor product $\lambda_1\otimes \lambda_2$ of two linear functionals $\lambda_i: \mathrm{V}_i\to\mathbb{K}$, $i=1,2$ with its image in $\operatorname{Hom}\nolimits (\mathrm{V}_1 \otimes \mathrm{V}_2,\mathbb{K})$.

Now observe that for two conjugate-linear maps $\mu_1 :\mathrm{V}_1 \to \mathbb{K}$ and $\mu_2 :\mathrm{V}_2 \to \mathbb{K}$ the map $ \tau^* (\mu_1,\mu_2) = \overline{\overline{\mu_1}\otimes \overline{\mu_2}} :
\mathrm{V}_1 \otimes \mathrm{V}_2 \to \mathbb{K}$ is conjugate-linear and satisfies

:::{math}
:label: eq:defining-relation-tensor-product-conjugate-linear-maps_1
\tau^* (\mu_1,\mu_2) \, (v_1\otimes v_2) = \mu_1(v_1) \cdot \mu_2(v_2) \quad
\text{for all } v_1\in\mathrm{V}_1 ,\: v_2 \in\mathrm{V}_2 \ .
:::

One obtains a map

:::{math}
\tau^*: \operatorname{Hom}\nolimits^* (\mathrm{V}_1,\mathbb{K}) \times \operatorname{Hom}\nolimits^* (\mathrm{V}_2,\mathbb{K})
\to \operatorname{Hom}\nolimits^* (\mathrm{V}_1 \otimes \mathrm{V}_2 ,\mathbb{K}) \ ,
:::

where here the symbol $\operatorname{Hom}\nolimits^* (\mathrm{V},\mathbb{K})$ denotes the space of all conjugate linear functionals on a vector space $\mathrm{V}$. Since $\tau^*$ is biadditive and since $\tau^* (z\mu_1,\mu_2) = \tau^* (\mu_1,z\mu_2)$ for all $\mu_1\in \operatorname{Hom}\nolimits^*(\mathrm{V}_1 ,\mathbb{K})$, $\mu_2\in \operatorname{Hom}\nolimits^*(\mathrm{V}_2 ,\mathbb{K})$, and $z\in \mathbb{K}$, the map $\tau^*$ factors through a linear map

:::{math}
\widehat{\tau^*} :\operatorname{Hom}\nolimits^* (\mathrm{V}_1 ,\mathbb{K}) \otimes \operatorname{Hom}\nolimits^* (\mathrm{V}_2,\mathbb{K}) \to
\operatorname{Hom}\nolimits^* (\mathrm{V}_1 \otimes \mathrm{V}_2,\mathbb{K}) \ .
:::

Using the above bases $(v_{1i})_{i\in I} $ and $(v_{2j})_{j\in J} $ of $V_1$ and $V_2$ respectively, one observes that $\widehat{\tau^*}$ is an isomorphism since it maps the basis $\left( \overline{v^\prime_{1i}} \otimes \overline{v^\prime_{2j}}\right)_{(i,j)\in I \times J}$ of $\operatorname{Hom}\nolimits^* (\mathrm{V}_1 ,\mathbb{K}) \otimes \operatorname{Hom}\nolimits^* (\mathrm{V}_2,\mathbb{K})$ bijectively to the basis $\left( \overline{(v_{1i} \otimes v_{2j})^\prime} \right)_{(i,j)\in I \times J}$ of the space $\operatorname{Hom}\nolimits^* (\mathrm{V}_1 \otimes \mathrm{V}_2,\mathbb{K})$. So $\widehat{\tau^*}$ is also a linear isomorphism, which allows us to identify the tensor product $\mu_1 \otimes \mu_2$ of two conjugate linear functionals $\mu_i: \mathrm{V}_i\to\mathbb{K}$, $i=1,2$ with its image in $\operatorname{Hom}\nolimits^* (\mathrm{V}_1 \otimes \mathrm{V}_2,\mathbb{K})$.

After these preliminary considerations we consider the map

:::{math}
\mathscr{H}_1\times \mathscr{H}_2 \to \operatorname{Hom}\nolimits^* (\mathscr{H}_1\otimes \mathscr{H}_2,\mathbb{K}) ,
\: (w_1,w_2) \mapsto \overline{w_1^\flat} \otimes \overline{w_2^\flat} =
\tau^* \left( \overline{w_1^\flat} , \overline{w_2^\flat} \right)=
\widehat{\tau^*} \left( \overline{w_1^\flat} \otimes \overline{w_2^\flat} \right)\ ,
:::

which is well-defined and bilinear since the musical isomorphisms ${}^\flat: \mathscr{H}_l \to \mathscr{H}_l'$, $w \mapsto \langle w,- \rangle $, $l=1,2$, are conjugate-linear and since $\tau^*$ is bilinear. Hence it factors through a linear map

:::{math}
\beta: \mathscr{H}_1\otimes \mathscr{H}_2 \to \operatorname{Hom}\nolimits^* (\mathscr{H}_1\otimes \mathscr{H}_2,\mathbb{K})
:::

such that

:::{math}
:label: eq:defining-relation-map-beta_1
\beta (w_1\otimes w_2) (v_1\otimes v_2) = \langle v_1,w_1 \rangle \cdot \langle v_2,w_2 \rangle
\quad \text{for all } v_1,w_1\in \mathscr{H}_1 , \: v_2,w_2\in \mathscr{H}_2 \ .
:::

Now put

:::{math}
\langle \cdot,\cdot \rangle : (\mathscr{H}_1 \otimes \mathscr{H}_2) \times (\mathscr{H}_1 \otimes \mathscr{H}_2)
\to \mathbb{K}, \: (v,w) \mapsto \langle v,w \rangle := \beta (w) (v) \ .
:::

Then $\langle \cdot,\cdot \rangle$ is sesquilinear by construction, and
{eq}`eq:defining-relation-inner-product-tensor-product_1` holds true by
{eq}`eq:defining-relation-map-beta_1`.

Let us show that $\langle \cdot,\cdot \rangle$ is positive definite. Let $v = \sum_{k=1}^n v_{1k} \otimes v_{2k} \in \mathscr{H}_1 \otimes \mathscr{H}_2$. Choose an orthonormal basis $e_1, \ldots , e_m$ of the linear subspace spanned by $v_{21}, \ldots , v_{2n}$. Expand $ v_{2k} = \sum_{i=1}^m c_{ki} e_i$ with $c_{k1}, \ldots , c_{km} \in \mathbb{K}$. Then

:::{math}
:label: eq:expansion-tensor-product-vector-orthonormal-basis-second-component_1
v = \sum_{k=1}^n v_{1k} \otimes v_{2k} = \sum_{k=1}^n \sum_{i=1}^m v_{1k} \otimes (c_{ki} e_i) =
\sum_{i=1}^m \left( \sum_{k=1}^n c_{ki} v_{1k} \right) \otimes e_i =
\sum_{i=1}^m w_{1i} \otimes e_i \ ,
:::

where $ w_{1i} = \sum_{k=1}^n c_{ki} v_{1k} $. Hence

:::{math}
:label: eq:positivity-tensor-inner-product_1
\langle v,v \rangle = \langle \sum_{i=1}^m w_{1i} \otimes e_i,\sum_{j=1}^m w_{1j} \otimes e_j  \rangle
= \sum_{i=1}^m \sum_{j=1}^m \langle w_{1i}, w_{1j} \rangle \, \langle  e_i,e_j  \rangle =
\sum_{i=1}^m \| w_{1i} \|^2 \geq 0 \ .
:::

Moreover, if $\langle v,v \rangle = 0$, then $w_{1i}=0$ for $i=1,\ldots , m$, which implies $v= \sum_{i=1}^m w_{1i} \otimes e_i =0$. So $ \langle \cdot,\cdot \rangle$ is an inner product on $\mathscr{H}_1\otimes \mathscr{H}_2$ satisfying
{eq}`eq:defining-relation-inner-product-tensor-product_1`. It is uniquely determined by this condition since the vectors $v_1\otimes v_2$ with $v_1\in \mathscr{H}_1$ and $v_2\in \mathscr{H}_2$ span $\mathscr{H}_1\otimes \mathscr{H}_2$.
:::



:::{prf:definition} 
Let $\mathscr{H}_1$ and $\mathscr{H}_2$ be Hilbert spaces. The Hilbert completion of the algebraic tensor product $\mathscr{H}_1 \otimes \mathscr{H}_2$ equipped with the unique inner product $\langle \cdot,\cdot \rangle$ fulfilling
{eq}`eq:defining-relation-inner-product-tensor-product_1`
will be denoted $\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2$, its inner product again by $\langle \cdot,\cdot \rangle$. One calls the Hilbert space $\big(\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2 ,\langle \cdot,\cdot \rangle\big)$ the *Hilbert tensor product* of $\mathscr{H}_1$ and $\mathscr{H}_2$ or just the
*tensor product* of $\mathscr{H}_1$ and $\mathscr{H}_2$ if no confusion can arise.
:::



:::{prf:proposition} 
:label: thm:totality-tensor-product-total-sets_1
Let $\mathscr{H}_1$ and $\mathscr{H}_2$ be Hilbert spaces.



(ite:totality-simple-tensor-products-total-sets_1)=
(i)
: Let $A_1 \subset \mathscr{H}_1$ and $A_2 \subset \mathscr{H}_2$ be subsets which are total $\mathscr{H}_1$ and $\mathscr{H}_2$, respectively. Then the set of simple vectors $a_1\otimes a_2$ with $a_1 \in A_1$ and $a_2 \in A_2$ is total in the Hilbert tensor product $\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2$.

(ii)
: If $(e_i)_{i\in I}$ and $(f_j)_{j\in J}$ are orthonormal bases of $\mathscr{H}_1$ and $\mathscr{H}_2$, respectively, then $(e_i\otimes f_j)_{(i,j)\in I \times J}$ is an orthonormal basis of the Hilbert tensor product $\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2$.
:::



:::{prf:proof}



\itemindent
: Recall that a subset $A \subset \mathscr{H}$ or a family $A = (a_j)_{j\in J}$ of elements of a Hilbert space $\mathscr{H}$ is called *total* in $\mathscr{H}$ if the linear span of $A$ is dense in $\mathscr{H}$. By density of the algebraic tensor product $\mathscr{H}_1\otimes \mathscr{H}_2$ in the Hilbert tensor product $\mathscr{H}_1{\,\widehat{\otimes}\,} \mathscr{H}_2$, the set of simple tensors $v_1\otimes v_2$ with $(v_1,v_2) \in \mathscr{H}_1 \times \mathscr{H}_2$ is total in $\mathscr{H}_1{\,\widehat{\otimes}\,} \mathscr{H}_2$. Hence it suffices to find for each such pair $(v_1,v_2)$ and all $\varepsilon > 0$ vectors $w_1 \in \operatorname{Span} A_1$ and $w_2 \in \operatorname{Span} A_2$ such that
   
   :::{math}
   \| v_1\otimes v_2 - w_1\otimes w_2 \| < \frac{\varepsilon}{2} \ .
   :::
   
   By totality of $A_i$ in $\mathscr{H}_i$ there exist $w_i \in \operatorname{Span} A_i$ for $i=1,2$ such that
   
   :::{math}
   \| v_1 - w_1 \| < \min \left\{ 1, \frac{\varepsilon}{2(\| v_2 \| +1 ) } \right\}
   \quad \text{and}\quad
   \| v_2 - w_2 \| < \frac{\varepsilon}{2(\| v_1 \| +1 ) } \ .
   :::
   
   Then
   
   :::{math}
   \| v_1\otimes v_2 - w_1\otimes w_2 \| \leq
   \| v_1 - w_1 \| \, \| v_2 \| + \| v_2 - w_2 \| \| w_1 \| < \varepsilon \ .
   :::

\itemindent
: The family $(e_i\otimes f_j)_{(i,j)\in I \times J}$ is orthonormal by definition of the inner product on $\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2$. It is total by
   {ref}`ite:totality-simple-tensor-products-total-sets_1` and therefore a Hilbert basis.
:::



:::{prf:proposition} 
:label: thm:tensor-product-functor-category-hilbert-spaces-bounded-linear-operators_1
Assigning to each pair of Hilbert spaces $\mathscr{H}_1$ and $\mathscr{H}_2$ the Hilbert tensor product $\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2$ and to each pair of bounded linear operators $A_1:\mathscr{H}_1 \to \mathscr{H}_3$ and $A_2:\mathscr{H}_2 \to \mathscr{H}_4$ between Hilbert spaces the unique bounded extension $A_1 {\,\widehat{\otimes}\,} A_2 : \mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2 \to \mathscr{H}_3 {\,\widehat{\otimes}\,} \mathscr{H}_4$ of the operator $A_1 \otimes A_2 : \mathscr{H}_1 \otimes \mathscr{H}_2 \to \mathscr{H}_3 {\,\widehat{\otimes}\,} \mathscr{H}_4$, $v_1 \otimes v_2 \mapsto A_1(v_1) \otimes A_2(v_2)$ comprises a (covariant) bifunctor

:::{math}
{\,\widehat{\otimes}\,} : \mathsf{Hilb} \times \mathsf{Hilb} \to \mathsf{Hilb} \ .
:::

Moreover, ${\,\widehat{\otimes}\,}$ is isometric in the sense that

:::{math}
:label: eq:completed-tensor-product-isometry-equation-bounded-linear-maps_1
\| v_1 \otimes v_2\| & = \|v_1\| \, \|v_2\| \quad \text{for all } v_1\in \mathscr{H}_1, \: v_2 \in \mathscr{H}_1 \text{ and }\\

\| A_1 {\,\widehat{\otimes}\,} A_2\| & = \| A_1\| \, \|A_2\| \quad \text{for all }
A_1\in \mathfrak{B} ( \mathscr{H}_1, \mathscr{H}_3 ), \: A_2\in \mathfrak{B} ( \mathscr{H}_2, \mathscr{H}_4 ) \ .
:::
:::



:::{prf:proof}

We first show that $A_1 \otimes A_2 $ is a bounded operator. To this end observe that $A_1 \otimes A_2 $ can be written as the composition of the two operators $A_1\otimes \mathbbm{1}_{\mathscr{H}_2}$ and $ \mathbbm{1}_{\mathscr{H}_3} \otimes A_2$. Hence it suffices to show that each of these linear maps is bounded. Let $v = \sum_{k=1}^n v_{1k} \otimes v_{2k} \in \mathscr{H}_1 \otimes \mathscr{H}_2$ be of norm $1$. As in the proof of \Crefthm:construction-tensor-inner-product expand $ v_{2k} = \sum_{i=1}^m c_{ki} e_i$, $k=1,\ldots ,n$, where $e_1, \ldots , e_m$ is an orthonormal basis of $\operatorname{Span} \{ v_{21}, \ldots , v_{2n}\}$ and $c_{k1}, \ldots , c_{km} \in \mathbb{K}$. Equations {eq}`eq:expansion-tensor-product-vector-orthonormal-basis-second-component_1`
and {eq}`eq:positivity-tensor-inner-product_1` then entail that

:::{math}
v = \sum_{i=1}^m w_{1i} \otimes e_i \quad\text{and}\quad 1 = \langle v,v \rangle = \sum_{i=1}^m \| w_{1i} \|^2
:::

where $ w_{1i} = \sum_{k=1}^n c_{ki} v_{1k} $ for $i=1,\ldots , m$. Hence

:::{math}
\|( A_1 \otimes \mathbbm{1}_{\mathscr{H}_2})v \|^2 = \left\| \sum_{i=1}^m A_1 (w_{1i}) \otimes e_i\right\|^2 = \sum_{i=1}^m \| A_1 (w_{1i}) \|^2 \leq \|A_1\|^2 \sum_{i=1}^m \| w_{1i} \|^2 = \|A_1\|^2 \ ,
:::

so $A_1\otimes \mathbbm{1}_{\mathscr{H}_2}$ is bounded with norm $\leq \|A_1\|$. By symmetry, $ \mathbbm{1}_{\mathscr{H}_3} \otimes A_2$ is bounded with norm $\leq \|A_2\|$. Hence $A_1 \otimes A_2 = (\mathbbm{1}_{\mathscr{H}_3} \otimes A_2 )\circ (A_1\otimes \mathbbm{1}_{\mathscr{H}_2}) $ is bounded and

:::{math}
\| A_1 \otimes A_2 \| \leq \|A_1\| \, \|A_2\| \ .
:::

Therefore, $A_1 \otimes A_2$ has a unique bounded extension $A_1 {\,\widehat{\otimes}\,} A_2$ of norm

:::{math}
\| A_1 {\,\widehat{\otimes}\,} A_2 \| = \| A_1 \otimes A_2 \| \leq \|A_1\| \, \|A_2\| \ .
:::

Let us show that the converse inequality holds as well. For given $\varepsilon > 0$ there exist unit vectors $v_i \in \mathscr{H}_i$, $i=1,2$ such that $\|A_iv_i \|\geq \| A_i \| - \frac{\varepsilon}{2(\| A_1\| +\|A_2\| +1)}$. Then

:::{math}
\| (A_1 \otimes A_2) (v_1\otimes v_2) \| = \| A_1v_1\| \, \| A_2v_2\|
\geq \| A_1 \| \, \| A_2\| - \varepsilon \ .
:::

This implies

:::{math}
\| A_1 {\,\widehat{\otimes}\,} A_2 \| = \| A_1 \otimes A_2 \| \geq \|A_1\| \, \|A_2\|
:::

and {eq}`eq:completed-tensor-product-isometry-equation-bounded-linear-maps_1` follows. Equality {eq}`eq:completed-tensor-product-isometry-equation-vectors_1` is clear by construction of the Hilbert tensor product.

Next observe that $\mathbbm{1}_{ \mathscr{H}_1} {\,\widehat{\otimes}\,} \mathbbm{1}_{\mathscr{H}_2} = \mathbbm{1}_{\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2}$ by definition. Given Hilbert spaces $\mathscr{H}_1,\ldots,\mathscr{H}_6$ and bounded linear operators $A_i: \mathscr{H}_{i}\to \mathscr{H}_{i+2}$ and $B_i : \mathscr{H}_{i+2}\to \mathscr{H}_{i+4}$ for $i=1,2$, the composition $(B_1 \otimes B_2 ) \circ (A_1 \otimes A_2)$ coincides with $ (B_1\circ A_1) \otimes (B_2\circ A_2) $ by functoriality of the algebraic tensor product. By continuity of the operators $A_1 {\,\widehat{\otimes}\,} A_2$ and $B_1 {\,\widehat{\otimes}\,} B_2$ and by density of $\mathscr{H}_1\otimes \mathscr{H}_2$ in $\mathscr{H}_1{\,\widehat{\otimes}\,} \mathscr{H}_2$ the equality

:::{math}
(B_1 {\,\widehat{\otimes}\,} B_2 ) \circ (A_1 {\,\widehat{\otimes}\,} A_2) = (B_1\circ A_1) {\,\widehat{\otimes}\,} (B_2\circ A_2)
:::

follows. Hence ${\,\widehat{\otimes}\,}$ is a bifunctor as claimed.
:::



:::{prf:proposition} 
For every Hilbert space $\mathscr{H}$ one has two natural isomorphisms

:::{math}
\widehat{u}_\mathscr{H} : \mathbb{K} {\,\widehat{\otimes}\,} \mathscr{H} \to \mathscr{H} ,\: z\otimes v \to z v \quad \text{and} \quad {}_\mathscr{H} \widehat{u} : \mathscr{H} {\,\widehat{\otimes}\,} \mathbb{K} \to \mathscr{H} ,\: v \otimes z \to z v
:::

called the *left* and the *right unit*, respectively. Furthermore, for every triple of Hilbert spaces $\mathscr{H}_1,\mathscr{H}_2,\mathscr{H}_3$ there is a natural isomorphism, called *associator*

:::{math}
\widehat{a}_{\mathscr{H}_1,\mathscr{H}_2,\mathscr{H}_3} : (\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2) {\,\widehat{\otimes}\,} \mathscr{H}_3 \to
\mathscr{H}_1 {\,\widehat{\otimes}\,} ( \mathscr{H}_2 {\,\widehat{\otimes}\,} \mathscr{H}_3 ),\: (v_1\otimes v_2)\otimes v_3 \mapsto v_1\otimes (v_2 \otimes v_3 )\ .
:::

These data fulfill the so-called *coherence conditions* that is the *pentagon diagram*

:::{math}
\begin{tikzpicture}
\node (P0) at (90:2.8cm) {$((\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2) {\,\widehat{\otimes}\,} \mathscr{H}_3) {\,\widehat{\otimes}\,} \mathscr{H}_4$};
\node (P1) at (90+72:2.5cm) {$(\mathscr{H}_1{\,\widehat{\otimes}\,} (\mathscr{H}_2{\,\widehat{\otimes}\,} \mathscr{H}_3)){\,\widehat{\otimes}\,} \mathscr{H}_4$} ;
\node (P2) at (90+2*72:2.5cm) {$\mathllap{\mathscr{H}_1{\,\widehat{\otimes}\,} ((\mathscr{H}_2{\,\widehat{\otimes}\,} \mathscr{H}_3)}{\,\widehat{\otimes}\,} \mathscr{H}_4)$};
\node (P3) at (90+3*72:2.5cm) {$\mathscr{H}_1{\,\widehat{\otimes}\,} (\mathscr{H}_2\mathrlap{{\,\widehat{\otimes}\,} (\mathscr{H}_3{\,\widehat{\otimes}\,} \mathscr{H}_4))}$};
\node (P4) at (90+4*72:2.5cm) {$(\mathscr{H}_1{\,\widehat{\otimes}\,} \mathscr{H}_2){\,\widehat{\otimes}\,} (\mathscr{H}_3{\,\widehat{\otimes}\,} \mathscr{H}_4)$};
\draw (P0) edge[- > , > =angle 90] node[left] {$\widehat{a}_{\mathscr{H}_1,\mathscr{H}_2,\mathscr{H}_3} {\,\widehat{\otimes}\,} \, \mathbbm{1}_{\mathscr{H}_4}\hspace{2mm}$} (P1)
(P1) edge[- > , > =angle 90] node[left] {$\widehat{a}_{\mathscr{H}_1,\mathscr{H}_2{\,\widehat{\otimes}\,} \mathscr{H}_3 , \mathscr{H}_4}$} (P2)
(P2) edge[- > , > =angle 90] node[below] {$\hspace{5mm}\mathbbm{1}_{\mathscr{H}_1}{\,\widehat{\otimes}\,} \, \widehat{a}_{\mathscr{H}_2,\mathscr{H}_3,\mathscr{H}_4}$} (P3)
(P4) edge[- > , > =angle 90] node[right] {$ \widehat{a}_{\mathscr{H}_1 , \mathscr{H}_2,\mathscr{H}_3 {\,\widehat{\otimes}\,} \mathscr{H}_4}$} (P3)
(P0) edge[- > , > =angle 90] node[right] {$ \widehat{a}_{\mathscr{H}_1{\,\widehat{\otimes}\,} \mathscr{H}_2, \mathscr{H}_3 , \mathscr{H}_4}$} (P4);
\end{tikzpicture}
:::

and the *triangle diagram*

:::{math}
\begin{tikzcd}
( \mathscr{H}_1 {\,\widehat{\otimes}\,} \mathbb{K}) {\,\widehat{\otimes}\,} \mathscr{H}_2
\ar[rrrr,"\widehat{a}_{\mathscr{H}_1,\mathbb{K},\mathscr{H}_3}"]
\ar[drr,"{}_{\mathscr{H}_1}\!\widehat{u} \, {\,\widehat{\otimes}\,} \,\mathbbm{1}_{\mathscr{H}_2}",swap]& & &&
\mathscr{H}_1 {\,\widehat{\otimes}\,} (\mathbb{K} {\,\widehat{\otimes}\,} \mathscr{H}_2 )
\ar[dll,"\mathbbm{1}_{\mathscr{H}_1} {\,\widehat{\otimes}\,} \, \widehat{u}_{\mathscr{H}_2}"] \\ & & \mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2 & &
\end{tikzcd}
:::

commute for all Hilbert spaces $\mathscr{H}_1,\mathscr{H}_2,\mathscr{H}_3,\mathscr{H}_4$. In other words, the category $\mathsf{Hilb}$ endowed with the Hilbert tensor product ${\,\widehat{\otimes}\,}$ is a monoidal category.
:::



:::{prf:proof}

The category of $\mathbb{K}$-vector spaces with the usual tensor product as tensor functor is monoidal. Denote the corresponding unit isomorphisms and associator by $_{-}u$, $u_{-}$, and $a_{-,-,-}$, respectively. Then observe that by construction $\mathbb{K} {\,\widehat{\otimes}\,} \mathscr{H} = \mathbb{K} \otimes \mathscr{H}$ and $\mathscr{H} {\,\widehat{\otimes}\,} \mathbb{K} = \mathscr{H} \otimes \mathbb{K}$ for every Hilbert space $\mathscr{H}$. In particular this means that $\widehat{u}_\mathscr{H} $ coincides with the unit $u_\mathscr{H}$ and ${}_{\mathscr{H}}\widehat{u}$ with the unit ${}_{\mathscr{H}}u$. Moreover, both units $\widehat{u}_\mathscr{H} $ and ${}_{\mathscr{H}}\widehat{u}$ are bounded. Next recall that $\mathscr{H}_1 \otimes \mathscr{H}_2$ is dense in $\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2$ which by \Crefthm:totality-tensor-product-total-sets implies density of $(\mathscr{H}_1 \otimes \mathscr{H}_2) \otimes \mathscr{H}_3$ and $\mathscr{H}_1 \otimes (\mathscr{H}_2 \otimes \mathscr{H}_3)$ in $(\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2) {\,\widehat{\otimes}\,} \mathscr{H}_3$ and $\mathscr{H}_1 {\,\widehat{\otimes}\,} (\mathscr{H}_2 {\,\widehat{\otimes}\,} \mathscr{H}_3)$, respectively. Similarly one argues that $\mathscr{H}_1 \otimes (\mathscr{H}_2 \otimes (\mathscr{H}_3\otimes \mathscr{H}_4))$ is dense in $\mathscr{H}_1 {\,\widehat{\otimes}\,} (\mathscr{H}_2 {\,\widehat{\otimes}\,} (\mathscr{H}_3{\,\widehat{\otimes}\,} \mathscr{H}_4))$, and so on. Since the associator map $a_{\mathscr{H}_1,\mathscr{H}_2,\mathscr{H}_3} : (\mathscr{H}_1 \otimes \mathscr{H}_2) \otimes \mathscr{H}_3 \to
\mathscr{H}_1 \otimes ( \mathscr{H}_2 \otimes \mathscr{H}_3 )$ is bounded, it extends in a unique way to a linear bounded map $\widehat{a}_{\mathscr{H}_1,\mathscr{H}_2,\mathscr{H}_3} : (\mathscr{H}_1 {\,\widehat{\otimes}\,} \mathscr{H}_2) {\,\widehat{\otimes}\,} \mathscr{H}_3 \to
\mathscr{H}_1 {\,\widehat{\otimes}\,} ( \mathscr{H}_2 {\,\widehat{\otimes}\,} \mathscr{H}_3 )$. Using density, continuity, and commutativity of the pentagon and triangle diagrams for the tensor product functor one concludes that the coherence conditions for ${\,\widehat{\otimes}\,}$ with the unit and associator maps $_{-}\widehat{u}$, $\widehat{u}_{-}$, and $\widehat{a}_{-,-,-}$ are satisfied.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionThe monoidal structure of the category of Hilbert spaces -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXAdjoints of bounded operatorsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionAdjoints of bounded operators -->
(sec:adjoints-bounded-operators_1)=
# Adjoints of bounded operators
\para As before, the symbols $\mathscr{H}$ and $\mathscr{H}_k$ with $k=1,2$ always stand for Hilbert spaces over the field $\mathbb{K}$ of real or complex numbers. Several results of this section hold only in the complex case, thouhgh. Therefore we will be quite precise in stating all necessary assumptions, in particular about the ground field.

Let $A \in \mathfrak{B} (\mathscr{H}_1,\mathscr{H}_2)$ that is let $A:\mathscr{H}_1 \rightarrow \mathscr{H}_2$ be linear and bounded. Then the map

:::{math}
b_A : \mathscr{H}_1 \times \mathscr{H}_2 \to \mathbb{K}, \: (v,w) \mapsto \langle Av, w \rangle
:::

is sesquilinear and bounded with norm

:::{math}
\left\|b_A\right\| = \sup \big\{ \left| b_A(v,w)\right| \bigm\vert v \in \mathscr{H}_1, \: w \in \mathscr{H}_2, \: \left\|w\right\|=\left\|v\right\|=1 \big\} =
\left\|A\right\| \ .
:::

By \Crefthm:correspondence-bounded-sesquilinear-forms-bounded-operators
to the Riesz representation theorem there exists a unique bounded linear operator $A^* : \mathscr{H}_2 \to \mathscr{H}_1$ such that

:::{math}
b_A (v,w) = \langle  v, A^* w \rangle \quad
\text{for all } v \in \mathscr{H}_1, \: w\in \mathscr{H}_2 \ .
:::

This operator satisfies

:::{math}
:label: eq:equality-norm-operator-adjoint_1
\left\|A^*\right\|= \left\|b_A\right\| = \left\|A\right\|\ .
:::



:::{prf:definition} 
The unique operator $A^*\in \mathfrak{B} (\mathscr{H}_2,\mathscr{H}_1)$ associated to an operator $A\in \mathfrak{B}(\mathscr{H}_1,\mathscr{H}_2)$ such that

:::{math}
\langle Av,w \rangle = \langle  v, A^*w \rangle \quad
\text{for all } v \in \mathscr{H}_1, \: w\in \mathscr{H}_2
:::

is called the *adjoint* of $A$.
:::


The fundamental property of the adjoint operation is given by the following result.


:::{prf:proposition} 
:label: thm:adjoint-operation-conjugate-linear-map-square-identity_1
The adjoint map ${}^*: \mathfrak{B}(\mathscr{H}_1,\mathscr{H}_2) \to\mathfrak{B}(\mathscr{H}_2,\mathscr{H}_1)$ is a conjugate linear isometry whose square coincides with the identity operation that is $A^{**} = A$ for all $A \in \mathfrak{B}(\mathscr{H}_1,\mathscr{H}_2)$.
:::



:::{prf:proof}

By the proof of \Crefthm:correspondence-bounded-sesquilinear-forms-bounded-operators, $A^* w = \langle w, A( - )\rangle^\sharp$ for all $w\in \mathscr{H}_2$. Since the inner product is linear in the second argument and the operator ${}^\sharp$ conjugate linear, the map $A \mapsto A^*$ is conjugate linear in $A$. By Equation {eq}`eq:equality-norm-operator-adjoint_1`, the adjoint map is an isometry. The relation $A^{**}=A$ follows by uniqueness of the adjoint and since

:::{math}
\langle A^*w, v \rangle = \langle  w, Av \rangle \quad
\text{for all } v \in \mathscr{H}_1, \: w\in \mathscr{H}_2 \ .
:::
:::



:::{prf:definition} 
An operator $A \in \mathfrak{B} (\mathscr{H})$ is called *self-adjoint* if $A = A^*$,
*unitary* if $A^* = A^{-1}$, and *normal* if $[A, A^*] := AA^* - A^*A = 0$.
:::


We note that self-adjoint and unitary operators are always normal, but normal operators do not have to be self-adjoint or unitary. In the remainder of this section, we gather several results on self-adjoint and normal operators.


:::{prf:proposition} 
:label: thm:selfadjointness-criterion-operator-complex-hilbert-space_1
Assume that the ground field $\mathbb{K}$ of the Hilbert space $\mathscr{H}$ is the field of complex numbers. An operator $A \in \mathfrak{B} (\mathscr{H})$ then is self-adjoint if and only if $\langle Av, v \rangle \in \mathbb{R}$ for all $v \in \mathscr{H}$.
:::



:::{prf:proof}

($\Rightarrow$) If $A$ is self-adjoint, then

:::{math}
\langle Av, v \rangle = \langle v, A^*v \rangle = \langle v, Av \rangle = \overline{\langle Av,v \rangle}\ ,
:::

which implies that $\langle Av,v \rangle \in \mathbb{R}$.

($\Leftarrow$) Suppose that $\langle Av, v \rangle \in \mathbb{R}$ for all $v \in \mathscr{H}$. We know

:::{math}
:label: eq:expansion-inner-product-operator-action-argument_1
\langle A(v+w), v+w \rangle = \langle Av, v \rangle + \langle Av, w \rangle + \langle Aw, v \rangle + \langle Aw, w \rangle \ .
:::

By assumption, $\langle A(v+w), v+w \rangle$, $\langle Av, v \rangle$, and $\langle Aw, w \rangle$ are all real. This implies that the sum $\langle Av, w \rangle + \langle Aw, v \rangle$ is real as well, so

:::{math}
\Im \, \langle Av, w \rangle = -\Im \, \langle Aw, v \rangle= \Im \, \langle v, Aw \rangle \ .
:::

Since this holds for all $w \in \mathscr{H}$, it holds for $\hspace{0.1em}\mathsf{i}\hspace{0.1em} w$, too. Thus,

:::{math}
\Re \, \langle Av, w \rangle = \Im \, \hspace{0.1em}\mathsf{i}\hspace{0.1em} \langle Av, w \rangle = \Im \, \langle Av, \hspace{0.1em}\mathsf{i}\hspace{0.1em} w \rangle = \Im \, \langle v, A( \hspace{0.1em}\mathsf{i}\hspace{0.1em} w) \rangle =
\Im \, \hspace{0.1em}\mathsf{i}\hspace{0.1em} \langle v, Aw \rangle = \Re \,\langle v, Aw \rangle \ .
:::

Combining the above two lines yields $\langle Av, w \rangle = \langle v, Aw \rangle$ for all $v, w \in \mathscr{H}$. By uniqueness of the adjoint this implies that $A = A^*$.
:::



:::{prf:proposition} 
Assume that the ground field $\mathbb{K}$ of the Hilbert space $\mathscr{H}$ is the field of complex numbers and let $A \in \mathfrak{B} (\mathscr{H})$. If $\langle Av, v \rangle = 0$ holds for all $v \in \mathscr{H}$, then $A = 0$.
:::



:::{prf:proof}

Since $\langle Av, v \rangle = 0$ for all $v \in H$, equation
{eq}`eq:expansion-inner-product-operator-action-argument_1` from the proof of
\Crefthm:selfadjointness-criterion-operator-complex-hilbert-space reduces to

:::{math}
\langle Av, w \rangle = -\langle Aw, v \rangle = -\langle w, Av \rangle = -\overline{\langle Av, w \rangle} \quad
\text{for all } v, w \in \mathscr{H} \ .
:::

That means that $\langle Av,w \rangle$ has no real part for all $v, w \in \mathscr{H}$. But then fixing $v$ and setting $w = Av$ implies $\| Av \|^2 = 0$ for all $v \in \mathscr{H}$, so $A = 0$.
:::



:::{prf:example} 
The preceding proposition does not hold in the real case. To see this take rotation by $\frac \pi 2$:

:::{math}
R =
\begin{pmatrix}
\cos \frac \pi2 & -\sin \frac \pi2 \\
\sin \frac \pi2 & \cos \frac \pi2
\end{pmatrix}
:::

Then $\langle Rv,v \rangle =0$ for all $v\in \mathbb{R}^2$, but $R$ is non-zero. Note that the example of the rotation operator $R$ also shows that the criterion for self-adjointness from \Crefthm:selfadjointness-criterion-operator-complex-hilbert-space can not be applied in the real case.
:::



:::{prf:lemma} cf.~[@HirScharEF, Lem.\ 22.4]
:label: thm:estimate-sum-inner-products-operator-action-vector_1
Assume that $A$ is a bounded linear operator on the real or complex Hilbert space $\mathscr{H}$ for which there exists a $C\geq 0$ such that

:::{math}
|\langle Av,v \rangle| \leq C \| v\|^2 \quad \text{for all } v \in \mathscr{H} \ .
:::

Then

:::{math}
:label: eq:estimate-sum-inner-products-operator-action-vector-real-case_1
|\langle  Av,w \rangle + \langle v,Aw \rangle | \leq 2 C \| v\| \| w\| \quad \text{for all } v,w \in \mathscr{H} \ .
:::

In case $\mathscr{H}$ is a complex Hilbert space one even has the sharper estimate

:::{math}
:label: eq:estimate-sum-inner-products-operator-action-vector-complex-case_1
|\langle  Av,w \rangle| + | \langle v,Aw \rangle | \leq 2 C \| v\| \| w\| \quad \text{for all } v,w \in \mathscr{H} \ .
:::
:::



:::{prf:proof}

We start with the equality

:::{math}
:label: eq:expansion-inner-product-operator-action-sum-difference-arguments_1
\langle A(v+w), v+w \rangle + \langle A(v-w), v-w \rangle= 2 (\langle Av, w \rangle + \langle Aw, v \rangle) \ .
:::

By assumption and the parallelogram identity {eq}`eq:parallelogram-identity_1` this entails

:::{math}
:label: eq:estimate-sum-inner-products-operator-action-vector_1
2 | \langle Av, w \rangle + \langle Aw, v \rangle| \leq C \left( \| v+w\|^2 + \| v-w\|^2 \right)
= 2 C \big( \| v\|^2 + \| w\|^2 \big) \ .
:::

The claim obviously holds for $v=0$ or $w=0$, so we assume from now on that both $v$ and $w$ are non-zero. Then put $a= \sqrt{\frac{\|v\|}{\|w\|}}$ and replace in
{eq}`eq:estimate-sum-inner-products-operator-action-vector_1` $v$ by $\frac{v}{a}$ and $w$ by $aw$. One obtains

:::{math}
| \langle Av, w \rangle + \langle Aw, v \rangle| \leq C \left( \Big\|\frac{v}{a} \Big\|^2 + \Big\| a w \Big\|^2 \right)
= 2 C \| v \| \| w \|
:::

which is the claim in the real case. If $\mathscr{H}$ is a complex Hilbert space, let $x,y$ be complex numbers of modulus $1$. In the just proven estimate multiply the left side with $|x|$ and replace $w$ with $yw$. This gives

:::{math}
:label: eq:estimate-sum-inner-products-operator-action-vector-added-factors_1
\big| xy \langle Av, w \rangle + x \overline{y} \langle Aw, v \rangle \big| = |x| \cdot | \langle Av, yw \rangle + \langle A(yw), v \rangle|
\leq 2 C \| v \| \| w \| \ .
:::

Now write $ \langle Av, w \rangle = r e^{\hspace{0.1em}\mathsf{i}\hspace{0.1em} \varphi}$ and $\langle Aw, v \rangle = s e^{\hspace{0.1em}\mathsf{i}\hspace{0.1em} \psi}$ with $r,s\geq 0$ and $\varphi,\psi \in \mathbb{R}$. Then put

:::{math}
x = e^{-\hspace{0.1em}\mathsf{i}\hspace{0.1em} \frac 12 (\varphi +\psi))} \quad \text{and} \quad y = e^{-\hspace{0.1em}\mathsf{i}\hspace{0.1em} \frac 12 (\varphi - \psi))} \ .
:::

With these values, {eq}`eq:estimate-sum-inner-products-operator-action-vector-added-factors_1` becomes

:::{math}
|\langle  Av,w \rangle| + | \langle v,Aw \rangle | \leq 2 C \| v\| \| w\|
:::

which was to be shown.
:::



:::{prf:proposition} 
If $\mathscr{H}$ is a Hilbert space over the field $\mathbb{K}$ of real or complex numbers and $A \in \mathfrak{B} (\mathscr{H})$ is self-adjoint, then

:::{math}
\left\|A\right\| = \sup_{\left\|v\right\| = 1} |\langle Av, v \rangle| \ .
:::
:::



:::{prf:proof}

We know

:::{math}
:label: eq:operator-norm-inner-product-representation_1
\left\|A\right\| = \sup_{\left\|v\right\| = \left\|w\right\| = 1} | \langle Av, w \rangle| \ ,
:::

so we clearly have

:::{math}
\sup_{\left\|v\right\| = 1} {\left|\langle Av, v \rangle\right|} \leq \left\|A\right\| \ .
:::

The other direction follows from Equation {eq}`eq:operator-norm-inner-product-representation_1`
and \Crefthm:estimate-sum-inner-products-operator-action-vector since $A$ is self-adjoint.
:::



:::{prf:proposition} 
If $\mathscr{H}$ is a real or complex Hilbert space and $A \in \mathfrak{B} (\mathscr{H})$, then $A^*A$ is self-adjoint and $\left\|A^*A\right\| = \left\|A\right\|^2$.
:::



:::{prf:proof}

For arbitrary $v,w \in \mathscr{H}$, we have

:::{math}
\langle A^*Av, w \rangle = \langle Av, Aw \rangle = \langle v, A^*Aw \rangle
:::

so $A^*A$ is self-adjoint. Then

:::{math}
\left\|A^*A\right\| = \sup_{\left\|v\right\| = \left\|w\right\| = 1} {\left|\langle A^*Av, w \rangle\right|} =
\sup_{\left\|v\right\| = \left\|w\right\| = 1} {\left|\langle Av, Aw \rangle\right|} = \left\|A\right\|^2 \ ,
:::

where the last equality is a consequence of the Cauchy--Schwarz inequality and the observation that for all $\varepsilon > 0$ there exists a unit vector $v$ such that $ \langle Av, Av \rangle \geq \left\|A\right\|^2 -\varepsilon$.
:::



:::{prf:proposition} 
Let $\mathscr{H}$ be a complex Hilbert space $\mathscr{H}$. If $A \in \mathfrak{B} (\mathscr{H})$, then there exist unique self-adjoint $B,C \in \mathfrak{B} (\mathscr{H})$ such that $A = B+\hspace{0.1em}\mathsf{i}\hspace{0.1em} C$. Furthermore, $A$ is normal if and only if $[B,C] = 0$.
:::



:::{prf:proof}

We define

:::{math}
B = \frac{1}{2}(A + A^*) \quad \text{ and } \quad C = \frac{\hspace{0.1em}\mathsf{i}\hspace{0.1em}}{2}(A^* - A).
:::

Clearly $A = B +\!\hspace{0.1em}\mathsf{i}\hspace{0.1em} C$. Note also that $A^* = B - \hspace{0.1em}\mathsf{i}\hspace{0.1em} C$. Furthermore, by \Crefthm:adjoint-operation-conjugate-linear-map-square-identity

:::{math}
B^* = \frac{1}{2}(A^* + A) = B
:::

and

:::{math}
C^* = - \frac{\hspace{0.1em}\mathsf{i}\hspace{0.1em}}{2}(A - A^* ) = C \ .
:::

Hence $B$ and $C$ are self-adjoint, so fulfill the claim. Let us show uniqueness. Assume that $B^\prime,C^\prime \in \mathfrak{B} (\mathscr{H})$ are selfadjoint and satisfy $A = {B^\prime} +\!\hspace{0.1em}\mathsf{i}\hspace{0.1em} {C^\prime}$. Then

:::{math}
B - {B^\prime} = B^* - {B^\prime}^* = \left( \hspace{0.1em}\mathsf{i}\hspace{0.1em} ({C^\prime} - C)\right)^* = - \hspace{0.1em}\mathsf{i}\hspace{0.1em} ({C^\prime} - C) = - ( B - {B^\prime}) \ .
:::

Hence $B = {B^\prime}$ and consequently $C = {C^\prime}$. Finally, we compute

:::{math}
[A, A^*] = [B +\!\hspace{0.1em}\mathsf{i}\hspace{0.1em} C, B - \hspace{0.1em}\mathsf{i}\hspace{0.1em} C] = -\hspace{0.1em}\mathsf{i}\hspace{0.1em} [B, C]+\!\hspace{0.1em}\mathsf{i}\hspace{0.1em} [C,B] = -2 \hspace{0.1em}\mathsf{i}\hspace{0.1em} [B,C] \ .
:::

This entails that $A$ is normal if and only if $[B,C] = 0$.
:::



:::{prf:proposition} 
If $A$ is a normal operator on a real or complex Hilbert space $\mathscr{H}$, then

:::{math}
\left\|Av\right\| = \left\|A^*v\right\| \quad\text{for all }v \in \mathscr{H} \ .
:::
:::



:::{prf:proof}

Using the fact that $A^*A = AA^*$, we compute

:::{math}
\left\|Av\right\|^2 = \langle Av, Av \rangle = \langle v, A^*Av \rangle = \langle v, AA^*v \rangle = \langle A^*v, A^*v \rangle = \left\|A^*v\right\|^2 \ .
:::

Taking the square root yields the desired result.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionAdjoints of bounded operators -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXThe lattice of orthogonal projectionsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionThe lattice of orthogonal projections -->
(sec:lattice-orthogonal-projections_1)=
# The lattice of orthogonal projections
\para In their celebrated article on quantum logic from 1936, \citeauthorBirVonNeuLQM showed that the set of closed linear subspaces of a Hilbert space carries the structure of a complete orthocomplemented lattice. In this section, we will describe the Birkhoff--von Neumann lattice structure. We start with the definition of orthogonal projections and the observation that the space of orthogonal projections on a Hilbert space $\mathscr{H}$ is in bijective correspondence with the closed linear subspaces of $\mathscr{H}$.


:::{prf:definition} 
:label: def:orthogonal-complement_1
By an *orthogonal projection* on a Hilbert space $\mathscr{H}$ one understands a bounded self-adjoint operator $P: \mathscr{H} \to \mathscr{H}$ which is an *idempotent* that is it fulfills the relation

:::{math}
:label: eq:projection-relation_1
P^2 = P \ .
:::
:::

<!-- XXSEC_PREFIX_ENDXX\sectionThe lattice of orthogonal projections -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXProjection-valued measures and spectral integralsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionProjection-valued measures and spectral integrals -->
# Projection-valued measures and spectral integrals
\para In this section $\mathscr{H}$ will always denote a fixed complex Hilbert space.

:::{prf:definition} 
By a *projection-valued measure* or a *spectral measure* on a measurable space $(\Omega,\mathscr{A})$ one understands a map $E: \mathscr{A} \to \mathfrak{B}(\mathscr{H})$ having the following properties:

\setcounterenumi-1
(SM1)
: For each $\Delta \in \mathscr{A}$ the operator $E(\Delta)$ is an orthogonal projection that is $E(\Delta)^2 = E(\Delta)$ and $E(\Delta)^* = E(\Delta)$.

(SM2)
: $E(\Omega) = \mathrm{id}_\mathscr{H}$.

(SM3)
: For every sequence $(\Delta_n)_{n\in \mathbb{N}}$ of pairwise disjoint elements of $\mathscr{A}$ one has
   
   :::{math}
   E\left(\bigcup_{n\in\mathbb{N}} \Delta_n \right) = {s\,-\!\!}\sum_{n=0}^\infty E(\Delta_n) \ ,
   :::
   
   where convergence is with respect to the strong operator toplogy.
:::



:::{prf:remark} 
Recall that *convergence* of a sequence of operators $(A_n)_{n\in \mathbb{N}} \subset \mathfrak{B}(\mathscr{H})$ in the *strong operator topology* to some $A $ means that for every $v\in \mathscr{H}$ the sequence $(A_nv)_{n\in\mathbb{N}}$ converges in $\mathscr{H}$ to $Av$. One denotes this by $A ={s\,-\!\!}\lim\limits_{n\to\infty} A_n$. Likewise, $B = {s\,-\!\!}\sum\limits_{n=0}^\infty A_n$ means that the sequence of partial sums $\left( \sum\limits_{k=0}^n A_n \right)_{n\in \mathbb{N}}$ converges in the strong operator topology to some $B \in \mathfrak{B} (\mathscr{H})$.
:::



:::{prf:proposition} 
A spectral measure $E : \mathscr{A} \to \mathfrak{B} (\mathscr{H})$ has the following properties in addition to the defining axioms:

\setcounterenumi1
(SM1')
: \refstepcounteritemno\labelite:spectral-measure-empty-set
   $E(\emptyset) = 0$.

(SM2')
: \refstepcounteritemno\labelite:spectral-measure-finite-additivity
   (Finite additivity) One has for all disjoint $\Delta_1,\Delta_2 \in \mathscr{A}$
   
   :::{math}
   E( \Delta_1 \cup \Delta_2) = E(\Delta_1) + E(\Delta_2) \ .
   :::
   
   \setcounterenumi2

(ite:spectral-measure-finite-multiplicativity_1)=
(SM1)
: One has for all $\Delta_1,\Delta_2 \in \mathscr{A}$
   
   :::{math}
   E( \Delta_1 \cap \Delta_2) = E(\Delta_1)\cdot E(\Delta_2) \ .
   :::
:::



:::{prf:proof}

 ad \hyperref[ite:spectral-measure-empty-set] (SM1').

 ad \hyperref[ite:spectral-measure-finite-additivity] (SM2').

 ad {ref}`ite:spectral-measure-finite-multiplicativity_1`.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionProjection-valued measures and spectral integrals -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXSpectral theory of bounded operatorsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionSpectral theory of bounded operators -->
# Spectral theory of bounded operators
\para We now apply the foundations of Hilbert space theory built in the previous sections to spectral theory. For the moment we will sacrifice generality and work only with bounded linear operators. The spectral theory of unbounded linear operators will be treated later.

Let us a recall that a linear map $A: \mathscr{H}_1 \rightarrow \mathscr{H}_2$ between Hilbert spaces is continuous if and only if it is bounded, i.e.has finite operator norm, and that $\mathfrak{B} (\mathscr{H}_1,\mathscr{H}_2)$ is a Banach space with the operator norm. For the rest of this section, $\mathscr{H}$, $\mathscr{H}_1$, $\mathscr{H}_2, \ldots$ will always denote complex Hilbert spaces and $A$, $B$ bounded linear operators. We will also now fix the base field to be complex, i.e.$\mathbb{K} = \C$. Last we agree on writing $I_\mathscr{H}$ or just $I$ for the identity operator on a Hilbert space $\mathscr{H}$.


<!-- XXSEC_DEF_SPLITTERXX\subsection*XXSEC_DEF_SPLITTERXXSpectrum and ResolventXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\subsection*Spectrum and Resolvent -->
## Spectrum and Resolvent
:::{prf:definition} 
Let $A:\mathscr{H} \to \mathscr{H}$ be a bounded linear operator. A complex number $\lambda$ is then called an *eigenvalue* of $A$ if there exists a nonzero $v \in H$ such that $Av = \lambda v$. For every $\lambda \in \C$ one defines the $\lambda$-*eigenspace* of $A$ as

:::{math}
\operatorname{Eig}_\lambda (A) = \big\{ v \in H \bigm\vert Av = \lambda v \big\} \subset \mathscr{H},
:::

which is clearly a linear subspace of $\mathscr{H}$.
:::


\para By definition it is immediately clear that

:::{math}
\operatorname{Eig}_\lambda (A) = \ker(A - \lambda),
:::

where the $\lambda$ on the right stands for the operator $\lambda I$. In other words this means that $\lambda\in \C$ is an eigenvalue of $A$ if and only if $A - \lambda$ is not injective.


:::{prf:definition} 
Let $A \in \mathfrak{B}(\mathscr{H})$. We make the following definitions.



(i)
: A *regular value* of $A$ is a complex number $\lambda$ such that $A-\lambda$ is invertible.

(ii)
: The set of all regular values is the *resolvent* of $A$, denoted $\varrho(A)$.

(iii)
: A *spectral value* of $A$ is a complex number $\lambda$ such that $A - \lambda$ is not invertible.

(iv)
: The set of all spectral values is the *spectrum* of $A$, denoted $\sigma(A)$.

(v)
: The *point* or *eigenspectrum* of $A$ is the set
   
   :::{math}
   \sigma_{p}(A) = \big\{\lambda \in \C \bigm\vert \ker(A - \lambda) \neq \{0 \} \big\}.
   :::

(vi)
: An *approximate eigenvalue* of $A$ is a complex number $\lambda$ for which there exists a sequence of unit vectors $(v_n)_{n\in \mathbb{N}}\subset \mathscr{H}$ such that
   
   :::{math}
   \lim_{n \rightarrow \infty} (A - \lambda)v_n = 0.
   :::
   
   The set $\sigma_{ap}(A)$ is the set of all approximate eigenvalues.


\para Evidently, $\sigma(A) = \C \setminus \varrho(A)$ and $\sigma_{p}(A) \subset \sigma_{ap}(A) \subset \sigma(A)$, and these may all be strict inclusions. Note that $A - \lambda$ is bounded for any $\lambda \in \C$, so the open mapping theorem ERROR_UNDEFINED_LABEL__-1 implies that $(A - \lambda)^{-1} \in \mathfrak{B}(\mathscr{H})$ when $\lambda \in \varrho(A)$. We call the map

:::{math}
R_\bullet (A ):\varrho(A) \rightarrow \mathfrak{B}(\mathscr{H}), \quad R_\lambda (A) = (A-\lambda)^{-1}
:::

the *resolvent* of $A$, not to be confused with the resolvent set $\varrho(A)$. To keep the notation clean, we often briefly write $R_\lambda$ for $R_\lambda(A)$ and leave implicit that $R_\lambda$ depends on $A$.
:::

First, we prove some topological properties of the spectrum and resolvent. Recall the following lemma, which generalizes the geometric series.


:::{prf:lemma} Carl Neumann
:label: thm:neumann-series_1
Let $A \in \mathfrak{B}(\mathscr{H})$. If $\left\|A\right\| < 1$, then $I - A$ is invertible,

:::{math}
(I - A)^{-1} = \sum_{n=0}^\infty A^n,
:::

and

:::{math}
\left\|(I-A)^{-1}\right\| \leq \frac{1}{1 - \left\|A\right\|}.
:::
:::



:::{prf:proof}

Since $\left\|A\right\| < 1$ and $\left\|A^n\right\| \leq \left\|A\right\|^n$ by submultiplicativity of the operator norm, we know $\sum_{n=0}^\infty \left\|A^n\right\| < \infty$. This implies that the family $(A^n)_{n\in\mathbb{N}}$ is absolutely summable, so $\sum_{n=0}^\infty A^n$ exists. Furthermore, for every $N \in \mathbb{N}$ we have

:::{math}
(I-A)\sum_{n=0}^N A^n = \left(\sum_{n=0}^N A^n \right)(I-A)= \sum_{n=0}^N A^n - \sum_{n=1}^{N+1}A^n = I - A^{N+1},
:::

which implies that

:::{math}
\lim_{N \rightarrow \infty}(I-A)\sum_{n=0}^N A^n = \lim_{N \rightarrow \infty} \left(\sum_{n=0}^N A^n\right) (I-A) = I.
:::

By continuity of multiplication in $\mathfrak{B}(\mathscr{H})$ one gets

:::{math}
(I-A) \sum_{n=0}^\infty A^n = \left(\sum_{n=0}^\infty A^n\right) (I-A) = I,
:::

which proves that $I-A$ is invertible and $(I-A)^{-1} = \sum_{n=0}^\infty A^n$.

Finally, one concludes by the triangle inequality and submultiplicativity of the operator norm

:::{math}
\left\|(I - A)^{-1}\right\| \leq \sum_{n=0}^\infty \left\|A^n\right\| \leq \sum_{n=0}^\infty \left\|A\right\|^n = \frac{1}{1 - \left\|A\right\|}.
:::
:::



:::{prf:proposition} 
:label: thm:resolvent-topological-properties_1
Let $A \in \mathfrak{B}(\mathscr{H})$.



(i)
: For any $\lambda \in \varrho(A)$, one has
   
   :::{math}
   B_{\left\|R_{\lambda}\right\|^{-1}}(\lambda) \subset \varrho(A) \ .
   :::
   
   Hence, $\varrho(A) \subset \C$ is open.

(ii)
: The spectrum $\sigma(A)$ is compact and
   
   :::{math}
   \sigma(A) \subset \widebar{B}_{\left\|A\right\|}(0) \ .
   :::

(ite:resolvent-expansion-large-argument_1)=
(iii)
: If the complex number $\lambda$ satisfies ${\left|\lambda\right|} > \left\|A\right\|$, then $\lambda \in \varrho(A)$ and
   
   :::{math}
   R_\lambda = - \frac{1}{\lambda} - \sum_{n=1}^\infty \lambda^{-n-1}A^n \ ,
   :::
   
   where convergence is with respect to the operator norm.
:::



:::{prf:proof}



\itemindent
: Fix $\lambda \in \varrho(A)$ and set $r = \left\|R_{\lambda}\right\|^{-1}$. Let $\mu \in B_r(\lambda)$. Then
   
   :::{math}
   \left\|(\mu - \lambda)R_{\lambda}\right\| = {\left|\mu - \lambda\right|} \left\|R_{\lambda}\right\| < 1.
   :::
   
   Thus, by Lemma {prf:ref}`thm:neumann-series_1`, one knows that $I - (\mu - \lambda)R_{\lambda}$ is invertible. Since $A - \lambda$ is invertible, the composition
   
   :::{math}
   (A - \lambda) \, \big( I - (\mu - \lambda)R_{\lambda} \big) = A - \mu
   :::
   
   is invertible, which proves that $\mu \in \varrho(A)$. Hence $\varrho(A)$ is open.

\itemindent
: Since $\varrho(A)$ is open, the complement $\sigma(A) = \C \setminus \varrho(A)$ is closed. Furthermore, if ${\left|\lambda\right|} > \left\|A\right\|$, then $\left\|\lambda^{-1}A\right\| < 1$, so $I - \lambda^{-1}A$ and hence $A - \lambda$ are invertible by Lemma {prf:ref}`thm:neumann-series_1`. This implies that $\lambda \in \varrho(A)$, so $\sigma(A) \subset \widebar{B}_{\left\|A\right\|}(0)$. Since $\sigma(A)$ is closed and bounded, it is compact.

\itemindent
: If ${\left|\lambda\right|} > \left\|A\right\|$, then $I - \lambda^{-1}A$ is invertible by Lemma {prf:ref}`thm:neumann-series_1` and
   
   :::{math}
   (I - \lambda^{-1}A)^{-1} = \sum_{n=0}^\infty \lambda^{-n}A^n.
   :::
   
   Since $-\lambda(A - \lambda)^{-1} = (I - \lambda^{-1}A)^{-1}$, one obtains
   
   :::{math}
   R_\lambda = -\frac{1}{\lambda}\sum_{n=0}^\infty \lambda^{-n}A^n = -\frac{1}{\lambda} - \sum_{n=1}^\infty \lambda^{-n-1}A^n,
   :::
   
   as desired.
:::


Next, we prove some algebraic properties of the resolvent. Hereby, $[A,B] = AB - BA$ denotes the commutator of two operators, as usual.


:::{prf:proposition} 
:label: thm:resolvent-algebraic-properties_1
Let $A,B \in \mathfrak{B}(\mathscr{H})$. Then the following holds true.



(ite:commutativity-resolvent-operator_1)=
(i)
: The resolvent commutes with the operator which means that
   
   :::{math}
   [A, R_\lambda(A) ] = 0 \quad\text{for all } \lambda \in \varrho(A) \ .
   :::

(ite:commutativity-resolvent-itself_1)=
(ii)
: The values of the resolvent commute with each other that is
   
   :::{math}
   [R_\lambda (A), R_\mu (A)] = 0 \quad\text{for all } \lambda,\mu \in \varrho(A) \ .
   :::

(ite:first-resolvent-identity_1)=
(iii)
: ( First resolvent identity) For all $\lambda, \mu \in \varrho(A)$
   
   :::{math}
   R_\lambda(A) - R_\mu (A)= (\lambda - \mu)R_\lambda(A) R_\mu(A) \ .
   :::

(iv)
: ( Second resolvent identity) For all $\lambda \in \varrho(A)\cap \varrho(B)$
   
   :::{math}
   R_\lambda (A)- R_\lambda (B) = R_\lambda(A)\, (B-A) \, R_\lambda (B) \ .
   :::
:::



:::{prf:proof}



\itemindent
: Obviously $[A, A - \lambda] = 0$, so
   
   :::{math}
   0 = R_\lambda [A, A - \lambda]R_\lambda = R_\lambda A - AR_\lambda,
   :::
   
   as desired.
   \setcounterenumi2

\itemindent
: We compute
   
   :::{math}
   (R_\lambda - R_\mu)(A - \mu)(A - \lambda) &= (R_\lambda A - \mu R_\lambda)(A - \lambda) - (A - \lambda)\\ &= (A - \mu)R_\lambda (A - \lambda) - (A - \lambda)\\ &= \lambda - \mu ,
   :::
   
   where we used part {ref}`ite:commutativity-resolvent-operator_1` to commute $R_\lambda$ past $A$ in the second step. Now multiplying both sides with $R_\lambda R_\mu $ from the right yields the desired equality.
   \setcounterenumi1

\itemindent
: For $\lambda = \mu$, one obviously has $[A_\lambda, A_\mu] = 0$. For $\lambda \neq \mu$, one concludes from
   {ref}`ite:commutativity-resolvent-itself_1`
   
   :::{math}
   R_\mu R_\lambda = \frac{R_\mu - R_\lambda}{\mu - \lambda} = \frac{R_\lambda - R_\mu}{\lambda - \mu} = R_\lambda R_\mu,
   :::
   
   so $[R_\lambda, R_\mu] = 0$ for $\lambda \neq \mu $ as well.
   \setcounterenumi3

\itemindent
: The last equality follows by
   
   :::{math}
   R_\lambda(A)\, (B-A) \, R_\lambda (B) = R_\lambda(A)\, \big((B-\lambda)-(A-\lambda) \big) \, R_\lambda (B) = R_\lambda(A) - R_\lambda (B) \ .
   :::
:::


The resolvent $R_\bullet (A)$ also has some nice analytic properties which we are going to prove next.

:::{prf:proposition} 
:label: thm:resolvent-analytic-properties_1
The resolvent $R_\bullet (A) :\varrho(A) \rightarrow \mathfrak{B}(\mathscr{H})$, $\lambda \mapsto R_\lambda$ is continuous and complex differentiable with derivative given by

:::{math}
R_\bullet(A)' :\: \varrho(A) \rightarrow \mathfrak{B}(\mathscr{H}), \: \lambda \mapsto \lim_{\mu \rightarrow \lambda} \frac{R_\mu - R_\lambda}{\mu - \lambda} = R_\lambda^2
:::
:::



:::{prf:proof}

Fix $\lambda \in \varrho(A)$ and $\varepsilon > 0$. Let $0 < {\left|\mu - \lambda\right|} < \delta$, where

:::{math}
\delta = \min\left( \frac{\varepsilon}{2\left\|R_\lambda\right\|^2},\, \frac{1}{2\left\|R_\lambda\right\|} \right) \ .
:::

Note that $\mu \in \varrho(A)$ by Proposition {prf:ref}`thm:resolvent-topological-properties_1`. Moreover, $\left\|(\mu - \lambda)R_\lambda\right\| < 1$, so $I - (\mu - \lambda)R_\lambda$ is invertible with norm less than $(1 - \left\|(\mu - \lambda) R_\lambda\right\|)^{-1}$ by Lemma {prf:ref}`thm:neumann-series_1`. Now observe that the first resolvent identity can be rearranged to

:::{math}
R_\mu = R_\lambda[I - (\mu - \lambda)R_\lambda]^{-1} \ .
:::

Hence

:::{math}
\left\|R_\mu - R_\lambda\right\| &\leq {\left|\mu - \lambda\right|}\left\|R_\mu\right\|\left\|R_\lambda\right\| \\ &\leq {\left|\mu - \lambda\right|} \left\|R_\lambda\right\|^2 \left\|(I - (\mu - \lambda)R_\lambda)^{-1}\right\|\\ &\leq \frac{{\left|\mu - \lambda\right|} \left\|R_\lambda\right\|^2}{1 - \left\|(\mu - \lambda)R_\lambda\right\|}\\ & < \frac{\varepsilon/2}{1-1/2} = \varepsilon \ .
:::

This proves that $\lambda \mapsto R_\lambda$ is continuous.

As for complex differentiability, we simply use the first resolvent identity and continuity to conclude

:::{math}
\lim_{\mu \rightarrow \lambda} \frac{R_\mu - R_\lambda}{\mu - \lambda} = \lim_{\mu \rightarrow \lambda} R_\mu R_\lambda = R_\lambda^2.
:::
:::



:::{prf:proposition} 
:label: thm:resolvent-limes-infinity_1
Let $A \in \mathfrak{B}(\mathscr{H})$. Then $\lambda R_\lambda \rightarrow -I$ as ${\left|\lambda\right|} \rightarrow \infty$. In particular, $R_\lambda \rightarrow 0$ as ${\left|\lambda\right|} \rightarrow \infty$.
:::



:::{prf:proof}

Fix $\varepsilon > 0$. For ${\left|\lambda\right|} > \left\|A\right\|$, we have by \Crefthm:resolvent-topological-properties {ref}`ite:resolvent-expansion-large-argument_1`

:::{math}
\lambda R_\lambda = -I - \sum_{n=1}^\infty \lambda^{-n}A^n.
:::

Since

:::{math}
\left\|\sum_{n=1}^\infty \lambda^{-n}A^n\right\| \leq \frac{\left\|A\right\|}{{\left|\lambda\right|}-\left\|A\right\|},
:::

one sees that $\lambda R_\lambda \rightarrow - I$ as ${\left|\lambda\right|} \rightarrow \infty$. Similarly, for ${\left|\lambda\right|} > \left\|A\right\|$ one has

:::{math}
\left\|R_\lambda\right\| \leq \frac{1}{{\left|\lambda\right|}} + \frac{1}{{\left|\lambda\right|}}\sum_{n=1}^\infty \left\|\lambda^{-n}A^n\right\| \leq \frac{1}{{\left|\lambda\right|}} + \frac{1}{{\left|\lambda\right|}} \frac{\left\|A\right\|}{{\left|\lambda\right|} - \left\|A\right\|},
:::

which shows that $R_\lambda \rightarrow 0$ as ${\left|\lambda\right|} \rightarrow \infty$.
:::



:::{prf:proposition} 
For all $v, w \in \mathscr{H}$, the map

:::{math}
\langle  R_\bullet (A) v, w \rangle : \: \varrho(A) \rightarrow \C , \: \lambda \mapsto \langle  R_\lambda v, w \rangle
:::

is holomorphic with derivative

:::{math}
\langle  R_\bullet (A) v, w \rangle' : \: \varrho(A) \rightarrow \C , \: \lambda \mapsto \langle R_\lambda^2 v, w \rangle.
:::
:::



:::{prf:proof}

Given $\lambda \in \varrho(A)$, we compute

:::{math}
\lim_{\mu \rightarrow \lambda} \frac{\langle R_\mu v, w \rangle - \langle R_\lambda v, w \rangle}{\mu - \lambda} =
\lim_{\mu \rightarrow \lambda} \frac{\langle (\mu - \lambda)R_\mu R_\lambda v, w \rangle}{\mu - \lambda} =
\lim_{\mu \rightarrow \lambda} \langle  R_\mu R_\lambda v, w \rangle = \langle R_\lambda^2v , w \rangle,
:::

where we have used the first resolvent identity in the first step and continuity of the inner product in the last.
:::



:::{prf:proposition} 
The spectrum of an operator $A \in \mathfrak{B}(\mathscr{H})$ is nonempty.
:::



:::{prf:proof}

Suppose $\sigma(A) = \emptyset$, hence $\varrho(A) = \C$. The map

:::{math}
\C \to \C , \: \lambda \mapsto \langle R_\lambda v, w \rangle
:::

then is entire for every $v, w \in \mathscr{H}$. Furthermore, one has for $\left\|v\right\|, \left\|w\right\| \leq 1$

:::{math}
{\left|\langle R_\lambda v, w \rangle\right|} \leq \left\|R_\lambda\right\| \left\|v\right\| \left\|w\right\| \leq \left\|R_\lambda\right\| \ .
:::

Since $\lambda \mapsto \left\|R_\lambda\right\|$ is continuous and $\left\|R_\lambda\right\| \rightarrow 0$ as ${\left|\lambda\right|} \rightarrow \infty$, one sees that $\left\|R_\lambda\right\|$ is bounded. Hence $\langle R_\bullet v, w \rangle$ is a bounded entire function, which by Liouville's theorem implies that it is zero for every pair $v, w \in \mathscr{H}$ with $\left\|v\right\| = \left\|w\right\| = 1$. This entails that $R_\lambda = 0$ for every $\lambda \in \C$, which is a contradiction to $R_\lambda$ being invertible. Hence $\sigma(A) \neq \emptyset$.
:::

<!-- XXSEC_PREFIX_ENDXX\subsection*Spectrum and Resolvent -->

<!-- XXSEC_PREFIX_ENDXX\sectionSpectral theory of bounded operators -->

<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXUnbounded linear operatorsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionUnbounded linear operators -->
(sec:unbounded-linear-operators_1)=
# Unbounded linear operators
\para In this section let $\mathrm{V},\mathrm{W}$ always denote Banach spaces over the field $\mathbb{K} =\mathbb{R}$ or $\mathbb{K}=\C$. The symbols $\mathscr{H}$, $\mathscr{H}_1$, ... will always stand for Hilbert spaces over $\mathbb{K}$.


:::{prf:definition} 
By an *unbounded*$\mathbb{K}$-linear operator or shortly by an
*unbounded operator* from $\mathrm{V}$ to $\mathrm{W}$ we understand a linear map $A: \operatorname{Dom} (A) \to \mathrm{W}$ defined on a $\mathbb{K}$-linear subspace $\operatorname{Dom} (A)\subset \mathrm{V}$. As usual, $\operatorname{Dom} (A)$ is called the *domain* of the operator $A$. The space of unbounded $\mathbb{K}$-linear operators from $V$ to $W$ will be denoted $\mathfrak{L}_\mathbb{K} (V,W)$ or just $\mathfrak{L} (V,W)$.
:::



:::{prf:remark} 
In this work, the term ``unbounded'' is meant in the sense of ``not necessarily bounded''. Sometimes we just say
*linear operator* or even only *operator* instead of ``unbounded linear operator''.
:::


\para Observe that besides the domain $\operatorname{Dom} (A)$ of an unbounded operator $A \in \mathfrak{L} (\mathrm{V},\mathrm{W})$ the
*kernel*

:::{math}
\operatorname{Ker}(A)=\big\{ v \in \mathrm{V} \bigm\vert Av = 0 \big\}\subset\mathrm{V} \ ,
:::

the *image*

:::{math}
\operatorname{Im}(A)=\big\{ w \in \mathrm{W} \bigm\vert \exists v\in \operatorname{Dom} (A): w = Av \big\}
\subset \mathrm{W} \ ,
:::

and the *graph*

:::{math}
\operatorname{Gr}(A)=\big\{ (v,w) \in \operatorname{Dom} (A) \times \mathrm{W} \bigm\vert w = Av \big\} \subset \mathrm{V} \times \mathrm{W}
:::

of $A$ are all linear subspaces. We will frequently make use of this.


:::{prf:definition} 
An unbounded operator $A\in \mathfrak{L} (\mathrm{V},\mathrm{W})$ is called
*densely defined* if $\operatorname{Dom} (A)$ is dense in $\mathrm{V}$, and *closed* if the graph $\operatorname{Gr} (A)$ is closed in $\mathrm{V} \times \mathrm{W}$. The operator $A \in \mathfrak{L} (V,W)$ is called *closable* if the closure $\widebar{\operatorname{Gr}(A)}$ is the graph of an unbounded operator from $\mathrm{V}$ to $\mathrm{W}$.

An operator $A \in \mathfrak{L} (V,W)$ is called an *extension* of $B \in \mathfrak{L} (V,W)$ if $\operatorname{Gr} (B) \subset \operatorname{Gr} (A)$. One writes in this situation $B \subset A$.
:::

<!-- XXSEC_PREFIX_ENDXX\sectionUnbounded linear operators -->

<!-- XXSEC_PREFIX_ENDXX\chapterHilbert Spaces -->

<!-- XXSEC_DEF_SPLITTERXX\chapterXXSEC_DEF_SPLITTERXXC$^*$-AlgebrasXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapterC$^*$-Algebras -->
(chpt:c*-algebras_1)=
# C$^*$-Algebras
<!-- XXSEC_DEF_SPLITTERXX\sectionXXSEC_DEF_SPLITTERXXInfinite tensor productsXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\sectionInfinite tensor products -->
(sec:infinite-tensor-products_1)=
# Infinite tensor products
\para Infinite tensor products of Hilbert spaces were introduced by [@vNeuIDP]. They were motivated by mathematical physics where one needs to describe quantum systems with infinitely many degrees of freedom, see e.g.~[@EmcAMSMQFT; @BraRobOAQSM2]. The original construction of infinite tensor products was generalized to von Neumann and$C^*$-algebras by [@GuiPTIRRA], [@BlaITPC*A], and others. Meanwhile, the topic has been studied in quite some detail in the operator algebra literature, see e.g.~[@NakITPvNAI; @NakITPvNAII; @StoITPvNA]. A purely algebraic or better categorical approach allowing the construction of infinite tensor products of modules over a given commutative ring has been given in [@CheFCA, Sec.~III.10]. The work [@NgGIATP] is also in that spirit. We will essentially follow [@CheFCA] and construct the infinite tensor product as a module universal with respect to multilinear maps. First we present the main algebraic construction, then we explain some of the subtleties which distinguish infinite from finite tensor products, and finally we construct infinite Hilbert tensor products and infinite tensor products of$C^*$-algebras.

\para\labelpara:canonical-projections-embeddings-multilinear-maps
Let $R$ be a commutative ring and $(M_i)_{i\in I}$ a possibly infinite family of $R$-modules. Consider $\prod_{i\in I} M_i$, the product of the family $(M_i)_{i\in I}$ within the category of $R$-modules. For each $j\in I$ let $\pi_j : \prod_{i\in I} M_i \to M_j $ denote the natural projection onto the $j$-th factor and $\iota_j :M _j \hookrightarrow \prod_{i\in I}M_i$ the uniquely determined natural embedding such that

:::{math}
\pi_j\circ \iota_i =
\begin{cases}
\mathrm{id}_{M_i} & \text{for}\enspace i=j \enspace\text{and} \\ 0 & \text{else} .
\end{cases}
:::

Given an $R$-module $N$ one then understands by a *multilinear map* from $ \prod_{i\in I}M_i$ to $N$ a map $f: \prod_{i\in I}M_i \to N$ such that for each $j\in I$ and $x\in \prod_{i\in I} M_i$ with $\pi_j (x)=0$ the map $M_j\to N$, $m\mapsto f(\iota_j(m)+x)$ is linear. The set of multilinear maps from $\prod_{i\in I} M_i$ to $N$ will be denoted by $\mathfrak{Mlin} \big(\prod_{i\in I} M_i,N\big)$. It carries a natural structure of an $R$-module given by pointwise addition of multilinear maps and pointwise action of a scalar on a multilinear map that is by

:::{math}
f+ g = \left( \prod_{i\in I} M_i \ni x \mapsto f(x) + g(x) \in N \right) \quad\text{and}\quad r f = \left( \prod_{i\in I} M_i \ni x \mapsto rf(x)\in N \right)
:::

for all $f,g \in \mathfrak{Mlin} \big(\prod_{i\in I} M_i,N\big)$ and $r\in R$. Since for $j\in I$ and $x\in \prod_{i\in I} M_i$ with $\pi_j(x)= 0$ the maps $M_j\to N$, $m \mapsto (f+g) (\iota_j(m) + x) = f (\iota_j(m) + x) + g (\iota_j(m) + x)$ and $M_j\to N$, $m \mapsto rf (\iota_j(m) + x) $ are linear by assumption on $f$ and $g$, the maps $f+g$ and $rf$ are multilinear again, so $ \mathfrak{Mlin}\big(\prod_{i\in I} M_i,N\big)$ is an $R$-module indeed with zero element the constant function mapping to $0\in N$.


:::{prf:remark} 
Before proceeding further let us make several explanations concerning the notation used.



\itemindent
: The space of multilinear maps $ \mathfrak{Mlin} \big(\prod_{i\in I} M_i,N\big)$ actually depends on the family $(M_i)_{i\in I}$ and the $R$-module $N$, so in principle one should write $ \mathfrak{Mlin} \big((M_i)_{i\in I},N\big)$ instead of $ \mathfrak{Mlin} \big(\prod_{i\in I} M_i,N\big)$. Nevertheless we stick to the latter notation since it is closer to standard notation for linear maps and since it will not lead to any confusion.

\itemindent
: In case the index set $I$ has just two elements $i_1,i_2$, one calls a multilinear map $\prod_{i\in I}M_i = M_{i_1}\times M_{i_2} \to N$ a *bilinear map*. If the cardinality of $I$ is $3$, one sometimes calls a multilinear map $\prod_{i\in I}M_i \to N$ a
   *trilinear map*.

\itemindent
: In the following, when saying that $(I_a)_{a\in A}$ is a partition of the set $I$ we mean that each $I_a$ is a non-empty subset of $I$, that $I_a \cap I_b =\emptyset $ for $a \neq b$ and that $\bigcup_{a \in A} I_a = I$. The empty family is regarded as a partition of the empty set.

\itemindent
: We will frequently use in this section the same symbol for maps with the same ``universal'' properties despite those maps might be strictly speaking different. For example, $\pi_k$ will stand for the canonical projections $\prod_{i\in I} M_i \to M_k$ and $\prod_{j\in J} M_j \to M_k$ whenever $k\in J \subset I$. Likewise we use the same notation for the two canonical embeddings $M_k \hookrightarrow \prod_{i\in I} M_i $ and $M_k \hookrightarrow \prod_{j\in J} M_j $ defined in ERROR_UNDEFINED_LABEL_para:canonical-projections-embeddings-multilinear-maps_-1 and denote them both by $\iota_k$.
:::



:::{prf:lemma} cf.~[@CheFCA, Sec.~III.10, Lemma 1 \& 2]
:label: thm:construction-multilinear-maps-composition_1
Assume that $(M_i)_{i\in I}$ is a family of $R$-modules, $N$ an $R$-module, and $f : \prod_{i\in I}M_i \to N$ a mutilinear map.



(i)
: If $g :N \to N^\prime$ is an $R$-module map, then $g\circ f : \prod_{i\in I}M_i \to N^\prime$ is multilinear.

(ii)
: Let $J\subset I$ be non-empty, $y= (y_i)_{i\in I\setminus J}$ an element of the product $\prod_{i\in I\setminus J} M_i$, and $ \iota_{J,y} : \prod_{j\in J} M_j \to \prod_{i\in I} M_i$ the unique map such that for all $x = (x_j)_{j\in J} \in (M_j)_{j\in J}$ and $k\in I$
   
   :::{math}
   \pi_k \circ \iota_{J,y}\, (x) =
   \begin{cases}
   x_k & \text{for } k\in J , \\ y_k & \text{for } k \in I\setminus J .
   \end{cases}
   :::
   
   Then the composition $f\circ \iota_{J,x} : \prod_{j\in J} M_j \to N$ is multilinear.

(ite:multilinearity-composition-multilinear-map-product-multilinear-map_1)=
(iii)
: Let $(I_a)_{a \in A}$ be a partition of the index set $I$ which is assumed to be non-empty. Let $(N_a)_{a \in A}$ be a family of $R$-modules, $(g_a)_{a \in A}$ a family of multilinear maps $g_a : \prod_{i \in I_a} M_i \to N_a$, and $h : \prod_{a \in A}N_a \to N$ multilinear. Define $g: \prod_{i\in I} M_i \to \prod_{a \in A} N_a $ as the unique map such that
   
   :::{math}
   \pi_b \circ g = g_b \circ \pi_{I_b} \quad
   \text{for } b \in A ,
   :::
   
   where $\pi_J$ for $J\subset I$ as on the right side stands for the projection $\pi_J : \prod_{i\in I} M_i \to \prod_{j \in J} M_j$ uniquely determined by $\pi_j \circ \pi_J =\pi_j$ for all $j\in J$. Then the composition $h \circ g : \prod_{i\in I} M_i \to N$ is multilinear.
:::



:::{prf:proof}



\itemindent
: Let $j\in I$ and $x\in \prod_{i\in I} M_i$ with $\pi_j (x)=0$. By multilinearity of $f$ and linearity of $g$, the map $M_j\to N^\prime$, $m\mapsto g f (\iota_j(m)+x)$ then has to be linear, hence $g\circ f$ is multilinear.

\itemindent
: Let $j \in J$ and $x\in \prod_{i\in J} M_i$ with $\pi_j (x)= 0$. Then $\pi_j(\iota_{J,y}(x))=0$ and $f \iota_{J,y} (\iota_j(m)+x) = f(\iota_j(m) + \iota_{J,y}(x)$ for all $m\in M_j$ by construction of $\iota_{J,y}$. Hence the map $M_j\to N$, $m\mapsto f \iota_{J,y} (\iota_j(m)+x)$ is linear by multilinearity of $f$. This proves that $f\circ \iota_{J,y}$ is multilinear.

\itemindent
: Given $j\in I$ let $b$ be the unique element of $A$ such that $j\in I_b$. Assume that $x\in \prod_{i\in I} M_i$ with $\pi_j (x)=0$. By construction one has $\pi_j(\pi_{I_b} (x))=0$. Now let $y \in \prod_{a \in A}N_a$ such that
   
   :::{math}
   \pi_a (y) =
   \begin{cases}
   0 & \text{for } a = b , \\ g_a \pi_{I_a} (x) & \text{for } a \neq b.
   \end{cases}
   :::
   
   One then obtains for $m\in M_j$
   
   :::{math}
   \pi_a g ( \iota_j(m) + x)=
   \begin{cases}
   g_b \pi_{I_b} (\iota_j(m)+x) = g_b (\iota_j (m) + \pi_{I_b} (x)) &\text{for }a = b, \\ g_a \pi_{I_a} (x) = \pi_a (y) & \text{for } a \neq b .
   \end{cases}
   :::
   
   Hence
   
   :::{math}
   h g (\iota_j(m)+ x) = h \big( \iota_b \big( g_b ( \iota_j(m) + \pi_{I_b} (x) \big) + y \big) \ ,
   :::
   
   and the map $M_j\to N$, $m\mapsto h g (\iota_j(m)+ x)$ is linear as the composition of two linear maps.
:::



:::{prf:lemma} 
:label: thm:associator-cartesian-product_1
Assume to be given a non-empty family of $R$-modules $(M_i)_{i\in I}$ and a partition $(I_a)_{a \in A}$ of the index set $I$. Then there exists a natural ismorphism

:::{math}
\kappa_{I,A}: \prod_{i \in I} M_i \to \prod_{a \in A} \prod_{i \in I_a} M_i
:::

uniquely determined by the condition that $\pi_a \circ \kappa_{I,A} = \pi_{I_a}$ for all $a\in A$.
:::


:::{prf:proof}

By the universal property of the product the $R$-module map $ \kappa = \kappa_{I,A}: \prod_{i \in I} M_i \to \prod_{a \in A} \prod_{i \in I_a} M_i$ exists and is uniquely determined by the requirement that $\pi_a \circ \kappa_{I,A} = \pi_{I_a}$ for all $a\in A$. Naturality also follows from the universal property of the product. It remains to show that $\kappa$ is an isomorphism. By construction, $\pi_i(x) = \pi_i \pi_a \kappa (x) =0$ for all $i\in I$ and $a(i)\in A$ such that $i\in I_{a(i)}$, hence $x=0$. So $\kappa$ is injective. It is also surjective. To see this pick $x_a \in \prod_{i \in I_a} M_i$ for each $a\in A$. With $a(i)$ for $i\in I$ defined as before put $x = \big( \pi_i (x_{a(i)} )\big)_{i\in I}$. Then, by construction, $\pi_i \pi_{a} \kappa (x) = \pi_i \pi_{a} (x) = \pi_i (x) = \pi_i (x_{a})$ for all $a\in A$ and $i\in I_a$, hence $\big(\pi_a \kappa (x) \big)_{a \in A} = (x_a)_{a \in A}$ and $\kappa$ is surjective.
:::



:::{prf:proposition} Exponential law for multilinear maps
:label: thm:exponential-law-multilinear-maps_1
Let $(M_i)_{i\in I}$ be a family of $R$-modules over a commutative ring $R$, $N$ an $R$-module, and assume that $J \subset I$ is a non-empty subset such that the complement $K = I\setminus J$ is also non-empty. Then the map

:::{math}
\begin{split}
\eta_{I,J}: \:&
\mathfrak{Mlin} \left( \prod_{j\in J} M_j , \mathfrak{Mlin} \left(\prod_{k\in K} M_k ,N \right)\right)
\rightarrow \mathfrak{Mlin} \left( \prod_{i\in I} M_i, N \right), \\ & \hspace{1em} f \mapsto \left( \prod_{i\in I} M_i\ni (x_i)_{i\in I} \mapsto f\big( (x_j)_{j\in J} \big)\left( (x_k)_{k\in K} \right) \in N \right)
\end{split}
:::

is an isomorphism which is natural in $(M_i)_{i\in I}$ and $N$.
:::



:::{prf:proof}

We first show that $\eta= \eta_{I,J} $ is linear. To this end let\$f,g \in \mathfrak{Mlin} \left( \prod_{j\in J} M_j , \mathfrak{Mlin} \left(\prod_{k\in K} M_k ,N \right)\right)$ and $r\in R$. Then, for all $x = (x_i)_{i\in I} \in \prod_{i\in I} M_i$,

:::{math}
\begin{split}
\big( \eta (f & +g)\big) (x) = \big(f+g\big) \big( (x_j)_{j\in J} \big)\left( (x_k)_{k\in K} \right)
= \big( f((x_j)_{j\in J}) + g ((x_j)_{j\in J})\big) \left( (x_k)_{k\in K} \right) = \\ & = f((x_j)_{j\in J}) \left( (x_k)_{k\in K} \right) + g ((x_j)_{j\in J}) \left( (x_k)_{k\in K} \right) =
\big( \eta f \big) (x) + \big( \eta g \big) (x) = \big( \eta f + \eta g \big) (x)
\end{split}
:::

and

:::{math}
\begin{split}
\big( \eta (rf)\big) (x) & = (rf) ((x_j)_{j\in J}) \left( (x_k)_{k\in K} \right) =
\big( r f((x_j)_{j\in J})\big) \left( (x_k)_{k\in K} \right) = r \big( f((x_j)_{j\in J})\left( (x_k)_{k\in K} \right)\big) = \\ & = r \big( \eta f (x)\big) = \big( r (\eta f ) \big) (x) \ .
\end{split}
:::

Hence $\eta$ is an $R$-module map.

Next we show that $\eta$ is an isomorphism by constructing an inverse. Given $f \in \mathfrak{Mlin} \big( \prod_{i\in I} M_i, N \big)$ we define $f^\sharp : \mathfrak{Mlin} \big( \prod_{j\in J} M_j \big) \to \mathfrak{Mlin} \big(\prod_{k\in K} M_k ,N \big)$ by the requirement that

:::{math}
f^\sharp (y) (z) = f (x_{y,z}) \quad \text{for all}\enspace y = (y_j)_{j\in J}\enspace \text{and} \enspace z = (z_k)_{k \in K} \ ,
:::

where $x_{y,z}$ is the element of $\prod_{i\in I}M_i$ uniquely determined by

:::{math}
\pi_i (x_{y,z}) =
\begin{cases}
y_i & \text{for}\enspace i \in J , \\ z_i & \text{for}\enspace i \in K .
\end{cases}
:::

One thus obtains an $R$-module map

:::{math}
(-)^\sharp_{I,J} :
\mathfrak{Mlin} \left( \prod_{i\in I} M_i, N \right) \to
\mathfrak{Mlin} \left( \prod_{j\in J} M_j , \mathfrak{Mlin} \left(\prod_{k\in K} M_k ,N \right)\right),\quad f \mapsto f^\sharp
:::

which by construction is inverse to $\eta_{I,J}$.

Naturality of $\eta_{I,J}$ in $(M_j)_{j\in J}$ and $N$ is clear by definition.
:::



:::{prf:definition} 
Let $(M_i)_{i\in I}$ be a family of $R$-modules over a commutative ring $R$. By a
*tensor product* of $(M_i)_{i\in I}$ one understands an $R$-module $\bigotimes_{i\in I}M_i$ together with a multilinear map $\tau : \prod_{i\in I}M_i \to \bigotimes_{i\in I}M_i$ such that the following universal property is fulfilled:


(axiom:hilbert-tensor-product_1)=
(ITensor)
: For every $R$-module $N$ and every multilinear map $f : \prod_{i\in I}M_i \to N$ there exists a unique $R$-module map $\overline{f}: \bigotimes_{i\in I}M_i \to N$ such that the diagram
   
   :::{math}
   \begin{tikzcd}
   \prod\limits_{i\in I}M_i \ar[d,"\tau",swap] \ar[r,"f"] & N \\
   \bigotimes\limits_{i\in I}M_i \ar[ru,"\overline{f}",swap]
   \end{tikzcd}
   :::
   
   commutes.


The linear map $\overline{f}$ making the diagram comute will sometimes be called the *linearization*
of the multilinear map $f$.

Given a tensor product $\big( \bigotimes_{i\in I}M_i,\tau\big)$, we will usually denote the image of an element $(x_i)_{i\in I} \in \prod_{i\in I}M_i$ under the map $\tau$ by $\otimes_{i\in I} x_i$.
:::



:::{prf:remark} 


\itemindent
: Strictly speaking, a tensor product of a family $(M_i)_{i\in I}$ of $R$-modules is a pair $\big( \bigotimes_{i\in I}M_i,\tau\big)$ having the above properties. By slight abuse of language, one usually denotes a tensor product just by its first component, the $R$-module $\bigotimes_{i\in I}M_i$. When helpful for clarity, the associated map $\tau: \prod_{i\in I}M_i \to \bigotimes_{i\in I}M_i$ will be denoted by $\tau_{(M_i)_{i\in I}}$ or by $\tau_I$.

\itemindent
: In the case where the index set $I$ of the family $(M_i)_{i\in I}$ is infinite, one sometimes calls $\bigotimes_{i\in I}M_i$ an *infinite tensor product*.
:::



:::{prf:theorem} 
:label: thm:construction-fundamental-properties-infinite-tensor-product_1
Let $(M_i)_{i\in I}$ be a family of $R$-modules over a commutative ring $R$. Then the following holds true.



(i)
: A tensor product $\bigotimes_{i\in I}M_i$ of the family $(M_i)_{i\in I}$ exists and is unique up to isomorphism. If $I$ is the empty set, then $\bigotimes_{i\in I}M_i = R$, if $I$ contains a single element $i_\circ$, then $\bigotimes_{i\in I}M_i =M_{i_\circ}$.

(ii)
: If $(N_i)_{i\in I}$ is a second family of $R$-modules and $(f_i)_{i\in I}$ a family $R$-module maps $f_i :M_i \to N_i$, then there exists a unique linear map $\bigotimes_{i\in I}f_i: \bigotimes_{i\in I}M_i \to \bigotimes_{i\in I}N_i$ making the diagram
   
   :::{math}
   \begin{tikzcd}
   \prod\limits_{i\in I}M_i \ar[d,"\tau",swap] \ar[r,"f"] & \bigotimes\limits_{i\in I}N_i \\
   \bigotimes\limits_{i\in I}M_i \ar[ru,"\bigotimes\limits_{i\in I}f_i",swap]
   \end{tikzcd}
   :::
   
   commute, where $f:\prod_{i\in I}M_i\to \bigotimes_{i\in I}N_i$ is the multilinear map $(x_i)_{i\in I}\mapsto \otimes_{i\in I} f_i(x_i)$.

(iii)
: Let $J\subset I$ be a finite non-empty subset set such that $M_j$ is isomorphic to $R$ for all $j\in J$. Denote for each $j\in J$ by $1_j$ the image of the unit $1\in R$ under the isomorphism $R\cong M_j$ and by $1_J$ the family $(1_j)_{j\in J}$. Moreover, for every family $y =(y_j)_{j\in J}$ let $\iota_{J,y} : \prod_{i\in I\setminus J} M_i \to \prod_{i\in I}M_i$ be the map which associates to $x\in\prod_{i\in I\setminus J} M_i$ the family $ (x_i)_{i\in I}$ such that $x_i =\pi_i (x)$ for $i \in I\setminus J$ and $x_i = y_i$ for $i \in J$. Then the linearization $\overline{\iota}_{J,1_J}: \bigotimes_{i\in I\setminus J}M_i \to \bigotimes_{i\in I}M_i $ of the multilinear map $\tau_I \circ \iota_{J,1_J}: \prod_{i\in I\setminus J}M_i \to \bigotimes_{i\in I}M_i$ is an isomorphism.
:::



:::{prf:proof}



\itemindent
: By its universal property, the tensor product of the family $(M_i)_{i\in I}$ is uniquely determined up to isomorphism. Hence it remains to show the existence of the tensor product. To this end consider the free $R$-module over the set $\prod_{i\in I}M_i$ and denote it by $F$. Let $\delta: \prod_{i\in I}M_i \hookrightarrow F$ be the canonical injection and $U$ be the submodule of $F$ spanned by the elements
   
   :::{math}
   \delta \big( \iota_j (r y_j + z_j) + (x_i)_{i\in I} \big) - r \delta \big( \iota_j (y_j) + (x_i)_{i\in I}\big)
   - \delta \big( \iota_j (z_j) + (x_i)_{i\in I}\big) \ ,
   :::
   
   where $j\in I$, $y_j , z_j \in M_j$, $r \in R$, and $(x_i)_{i\in I} \in \pi_j^{-1} (0)$. Then put $\bigotimes_{i\in I}M_i = F/U$ and define $\tau$ as the composition of the canonical projection $\pi : F \to \bigotimes_{i\in I}M_i$ with $\delta : \prod_{i\in I}M_i \to F$. By construction, $\tau$ is multilinear. Assume that $N$ is an $R$-module and $f : \prod_{i\in I}M_i \to N$ is a multilinear map. By the universal property of free $R$-modules, $f$ lifts to a unique $R$-linear map $f^\prime : F \to N$ such that $f = f^\prime \circ \delta$. By multilinearity of $f$, the map $f^\prime$ vanishes on the submodule $U$, hence descends to an $R$-linear $\overline{f}: \bigotimes_{i\in I}M_i \to N$ such that $f^\prime = \overline{f} \circ \pi$. Hence $f = f^\prime \circ \delta = \overline{f} \circ \pi \circ \delta = \overline{f} \circ \tau$. By surjectivity of $\delta$ and uniqueness of $f^\prime$, $\overline{f}$ is the unique $R$-linear map satisfying $f = \overline{f} \circ \tau$. Hence $\big( \bigotimes_{i\in I}M_i,\tau\big)$ is a tensor product of the family $(M_i)_{i\in I}$.
   
   In case $I=\emptyset$, the cartesian product $\prod_{i\in I}M_i$ is final in the category of sets, hence consists of only one element $\star$ only. This means in particular that for an $R$-module $N$ any map $f: \prod_{i\in I}M_i = \{ \star\} \to N$ is multilinear. Put $\bigotimes_{i\in I}M_i = R$ and let $\tau : \{ \star\} \to R$ be the map $\star \mapsto 1$. Now let $\overline{f}: R \to N$ be the unique linear map such that $\overline{f}(1)= f(\star)$. Then $f = \overline{f}\circ \tau$ and the pair $(R,\tau)$ fulfills the universal property of the tensor product.
   
   If $I$ is a singleton with unique element $i_0$, then $\prod_{i\in I} M_i = M_{i_0}$ and a map $f: \prod_{i\in I} M_i \to N$ is multilinear if and only if $f$ as a map from $M_{i_\circ}$ to $N$ is linear. This implies that the pair $(M_{i_0},\mathrm{id}_{M_{i_\circ}})$ then is a tensor product for the family $(M_i)_{i\in I}$.

\itemindent
: This is an immediate consequence of the universal property of the tensor product.

\itemindent
: We construct an inverse to $\overline{\iota}_{J,1_J}: \bigotimes_{i\in I\setminus J}M_i \to \bigotimes_{i\in I}M_i $. Let $x = (x_i)_{i\in I}$ be an element of $\prod_{i\in I}M_i$ and put
   
   :::{math}
   \lambda (x) = \left( \prod_{j\in J} x_j \right)\cdot \otimes_{i\in I\setminus J} x_i
   \left( \prod_{j\in J} x_j \right) \cdot \tau_{I\setminus J} ((x_i)_{i\in I\setminus J}) \ .
   :::
   
   Then $\lambda : \prod_{i\in I}M_i \to \bigotimes_{i\in \setminus J} M_i$ is multilinear by construction, hence factors through a linear map $\overline{\lambda} : \bigotimes_{i\in I}M_i \to \bigotimes_{i\in I \setminus J} M_i$. By definition, $\overline{\lambda}$ is a left inverse of $\overline{\iota}_{J,1_J}$. It is also a right inverse since for all $(x_i)_{i\in I} \in \prod_{i\in I}M_i$ by multilinearity of $\tau_I$
   
   :::{math}
   \begin{split}
   \overline{\iota}_{J,1_J} \circ \overline{\lambda}\circ \tau_I \left( (x_i)_{i\in I} \right) & =
   \overline{\iota}_{J,1_J}
   \left( \left( \prod_{j\in J} x_j \right) \cdot \otimes_{i\in I\setminus J} x_i \right)
   =\left( \prod_{j\in J} x_j\right)\cdot\left( \overline{\iota}_{J,1_J} \circ \tau_{I\setminus J}
   \left((x_i)_{i\in I\setminus J}\right)\right) = \\ & \hspace{-5em}
   =\left( \prod_{j\in J} x_j\right)\cdot\left( \tau_I \circ
   \iota_{J,1_J}\left( (x_i)_{i\in I\setminus J}\right)\right) =
   \tau_I \circ \iota_{J,(x_j)_{j\in J}}\left( (x_i)_{i\in I\setminus J}\right) =
   \tau_I \left( (x_i)_{i\in I}\right) \end{split}
   :::
   
   and since by construction of the tensor product the image of $\tau_I$ is a generating system for the $R$-module $\bigotimes_{i\in I}M_i$.
:::



:::{prf:lemma} 
:label: thm:image-generating-system-canoncial-map-finite-tensor-product-generating-system_1
Assume that $(M_i)_{i\in I}$ is a finite family of $R$-modules such that for every $i\in I$ a generating set $S_i$ of the $R$-module $M_i$ has been given. Then the set $S = \tau \left( \prod_{i\in I}S_i \right)$ is a generating set of the tensor product $\bigotimes_{i\in I} M_i$.
:::



:::{prf:proof}

By construction of the tensor product in the proof of
\Crefthm:construction-fundamental-properties-infinite-tensor-product it is clear that a generating set of $\bigotimes_{i\in I} M_i$ is given by the set of elements of the form $\otimes_{i\in I}x_i$ where $(x_i)_{i\in I}\in \prod_{i\in I}M_i$. Each of the $x_i$ can now be represented in the form

:::{math}
x_i = \sum_{k=1}^{n_i} r_{i,k} s_{i,k} \quad\text{with}\enspace r_{i,1},\ldots ,r_{i,n_i}\in R,\enspace s_{i,1},\ldots ,s_{i,n_i}\in S_i \ .
:::

Hence, by multilinearity of $\tau$ and with $I=\{ i_1,\ldots ,i_d\}$,

:::{math}
\otimes_{i\in I}x_i = \tau \left( (x_i)_{i\in I} \right) =
\sum_{k_{i_1} =1}^{n_{i_1}}\cdots \sum_{k_{i_d} =1}^{n_{i_d}} r_{i_1,k_{i_1}} \cdot \ldots \cdot r_{i_d,k_{i_d}}
\cdot \tau \left( (s_{i,k_i})_{i\in I} \right) \ ,
:::

so $\otimes_{i\in I}x_i$ is a linear combination of elements of $S$ and the claim is proved.
:::



:::{prf:lemma} 
:label: thm:componentwise-multilinear-maps-factorization_1
Let $(M_i)_{i\in I}$ be a family of $R$-modules, $(I_a)_{a\in A}$ a finite partition of the index set $I$, and $N$ an $R$-module. For $a\in A$ put $N_a = \bigotimes_{i\in I_a} M_i$ and let $\tau_a: \prod_{i\in I_a} M_i \to N_a$ denote the canonical map. Assume that $f : \prod_{a\in A}\prod_{i\in I_a} M_i \to N$ is a map which is
*componentwise multilinear* in the following sense.


$(\mathsf{ CM})$ Let $b\in A$ and $y=(y_a)_{a\in A} \in \prod_{a\in A}\prod_{i\in I_a} M_i $ a family with $y_b =0$. If for all $j\in I_b$ and families $x=(x_i)_{i\in I_b}\in \prod_{i\in I_b} M_i$ with $x_j =0$ the map
   
   :::{math}
   M_j \to N , \enspace m \mapsto f( \iota_b (\iota_j (m) + x) + y)
   :::
   
   is linear, then $f$ factors through $(\tau_a)_{a\in A}: \prod_{a\in A}\prod_{i\in I_a} M_i \to
   \prod_{a\in A}N_a $. More precisely, there exists a unique multilinear map $\overline{f} : \prod_{a\in A}N_a \to N$ such that
   
   :::{math}
   f = \overline{f} \circ (\tau_a)_{a\in A} \ .
   :::
:::



:::{prf:proof}

We prove the claim by induction on the cardinality of $A$. If $A$ is a singleton, then $\prod_{a \in A} \prod_{i\in I_a} M_i$ canonically coincides with $\prod_{i\in I} M_i$ and $f: \prod_{i\in I_a} M_i \to N$ is multilinear, hence by the universal property of the tensor product there exists a unique linear map $\overline{f}: N_a \to N$ such that $f = \overline{f} \circ \tau_a$.

Now assume that the claim holds whenever the cardinality of the index set $A$ is $\leq n$ for some $n \in \mathbb{N}^*$. Assume to be given initial data $(M_i)_{i\in I}$ and $§N$, a partition $(I_a)_{a\in A}$ of $A$ with $|A| = n+1$ and componentwise multilinear map $f: \prod_{a\in A}\prod_{i\in I_a} M_i \to N$. Fix $a \in A$ and put $B =A \setminus \{ a\}$. Let $x = (x_i)_{i\in I_a} \in \prod_{i\in I_a}M_i$ and $\widetilde{x}$ be the element of $ \prod_{d\in A}\prod_{i\in I_d} M_i $ such that

:::{math}
\pi_d (\widetilde{x}) =
\begin{cases}
x &\text{for} \enspace d = a \ , \\ 0 &\text{else} \ .
\end{cases}
:::

The map

:::{math}
f_x: \prod_{b\in B}\prod_{i\in I_b} M_i \to N , \enspace y \mapsto f (\iota_B (y) + \widetilde{x})
:::

then is componentwise multilinear. Hence by inductive assumption there exists a unique multilinear map $\overline{f_x} : \prod_{b\in B}N_b \to N$ such that $f_x = \overline{f_x}\circ (\tau_b)_{b\in B}$. By assumption on $f$ the map $\prod_{i\in I_a} M_i \to \mathfrak{Map} \left( \prod_{b\in B} \prod_{i\in I_b} M_i,N\right) $, $x \mapsto f_x$ is multilinear which implies multilinearity of

:::{math}
\overline{f_\bullet} :
\prod_{i\in I_a} M_i \to \mathfrak{Mlin} \left( \prod_{b\in B} N_b ,N \right),
\enspace x \mapsto \overline{f_x} \ .
:::

Let $F: N_a \to \mathfrak{Mlin} \left( \prod_{b\in B} N_b,N \right)$ be its linearization. Application of the exponential law for multilinear maps,
\Crefthm:exponential-law-multilinear-maps, now gives a multilinear map $\eta (F) : \prod_{d \in A} N_d \to N$ which we denote by $\overline{f}$. Given a family $(x_d)_{d\in A}$ of families $x_d =(x_i)_{i\in I_d}$ one checks

:::{math}
\overline{f} \left( \big(\tau_d (x_d)\big)_{d\in A} \right)
= F \big( \tau_a(x_a) \big) \left( \big(\tau_b (x_b)\big)_{b\in B} \right)
= \overline{f}_{x_a} \left( \big(\tau_b (x_b)\big)_{b\in B} \right)
= f_{x_a} \left( (x_b)_{b\in B} \right) = f \left( (x_d)_{d\in A} \right) \ .
:::

Hence $\overline{f} \circ (\tau_d)_{d\in A} =f$. To finish the induction step it remains to prove uniqueness. So let $\overline{g} : \prod_{d \in A} N_d \to N$ be another multilinear map such that $\overline{g} \circ (\tau_d)_{d\in A} =f$ and consider the induced linear map $\overline{g}^\sharp =\eta^{-1} (\overline{g}) : N_a \mapsto \mathfrak{Mlin} (\prod_{b\in B}N_b, N)$. Then for every $x\in \prod_{i\in I_a}M_i$ the relation

:::{math}
\overline{g}^\sharp (\tau_a(x)) \circ (\tau_b)_{b\in B} = f_x =
\overline{f}_x \circ (\tau_b)_{b\in B}
:::

is satisfied. Hence $\overline{g}^\sharp (\tau(x)) = \overline{f}_x$ for all $x\in \prod_{i\in I_a}M_i$ which entails that $\overline{g}^\sharp$ coincides with $F$. By
\Crefthm:exponential-law-multilinear-maps one obtains $\overline{g} = \overline{f}$. This finishes the induction step and the lemma is proved.
:::



:::{prf:proposition} 
Let $(M_i)_{i\in I}$ be a family of $R$-modules and $(I_a)_{a\in A}$ a finite partition of the index set $I$. Then there exists a natural isomorphism

:::{math}
\alpha_{I,A}: \bigotimes_{i \in I} M_i \to \bigotimes_{a \in A} \bigotimes_{i \in I_a} M_i .
:::
:::



:::{prf:proof}

Put $N_a = \bigotimes_{i \in I_a} M_i$ for $a \in A$ and let $\tau_a : \prod_{i \in I_a} M_i \to N_a$ be the canonical map to the tensor product. Let $\tau_A :\prod_{a \in A}N_a \to \bigotimes_{a \in A} N_a$ be the canonical map to the tensor product of the modules $N_a$. Define $\tau_{I,A}: \prod_{i \in I} M_i\to \prod_{a \in A} N_a$ as the unique map so that $\pi_a \circ \tau_{I,A} = \tau_a \circ \pi_{I_a}$ for all $a\in A$. By construction $\tau_{I,A} = (\tau_a)_{a\in A} \circ \kappa_{I,A}$, where $\kappa_{I,A} : \prod_{i\in I} M_i \to \prod_{a \in A} \prod_{i \in I_a} M_i$ is the natural isomorphism from
\Crefthm:associator-cartesian-product. The composition $\tau_A \circ \tau_{I,A}$ then is multilinear by \Crefthm:construction-multilinear-maps-composition
{ref}`ite:multilinearity-composition-multilinear-map-product-multilinear-map_1`, hence factors through a linear map $\alpha_{I,A} : \bigotimes_{i\in I} M_i \to \bigotimes_{a \in A} N_a$ that is

:::{math}
:label: eq:defining-equation-associator-map-tensor-product_1
\tau_A \circ (\tau_a)_{a\in A} \circ \kappa_{I,A} =
\alpha_{I,A} \circ \tau_I \ .
:::


Naturality of $\alpha_{I,A}$ in $(M_i)_{i\in I}$ is clear by definition so it remains to construct an inverse to $\alpha_{I,A}$. Consider the composition $\tau_I \circ \kappa^{-1}: \prod_{a \in A} \prod_{i \in I_a} M_i
\to \bigotimes_{i\in I} M_i$. Assume that $a \in A$ and $(y_b)_{b\in A\setminus\{a\}} \in \prod_{b \in A\setminus\{a\}} \prod_{i \in I_b} M_i$ have been chosen. Let $y_a\in \prod_{i \in I_a} M_i$ be $0$, put $\widetilde{y} =(y_d)_{d\in A} \in \prod_{d \in A} \prod_{i \in I_d} M_i$, and let $y\in \prod_{i \in I} M_i$ be the family such that $\pi_i(y) = \pi_i (y_{a(i)})$ for all $i\in I$, where $a(i)$ denotes the unique element of $A$ such that $i\in I_{a(i)}$. In other words let $y =\kappa^{-1} (\widetilde{y})$. For every $j\in I_a$ and $x= (x_i)_{i\in I_a}\in \prod_{i\in I_a}M_i$ with $\pi_j (x)=0$ the map

:::{math}
M_j \to \bigotimes_{i\in I} M_i,\enspace m \mapsto \tau_I \circ \kappa^{-1} \left( \iota_a (\iota_j(m)+x)+\widetilde{y}\right)
= \tau_I \left( \iota_j (m) + \iota_{I_a}(x) + y \right)
:::

then is multilinear since $\tau_I$ is multilinear and $\pi_j(\iota_{I_a}(x) + y)=\pi_j(x) +\pi_j(y_a) = 0$. Hence $\tau_I \circ \kappa^{-1}$ is componentwise multilinear and therefore, by \Crefthm:componentwise-multilinear-maps-factorization, factors through the map $(\tau_a)_{a\in A} : \prod_{a\in A} \prod_{i\in I_a} M_i\to \prod_{a\in A} N_a$ which means that

:::{math}
:label: eq:defining-equation-inverse-associator-map-tensor-product_1
\tau_I \circ \kappa^{-1} = \lambda_{I,A}\circ (\tau_a)_{a\in A}
:::

for some uniquely defined multilinear map $\lambda_{I,A} : \prod_{a\in A} N_a\to\bigotimes_{i\in I} M_i$. Let

:::{math}
\overline{\lambda}_{I,A} : \bigotimes_{a\in A} N_a\to\bigotimes_{i\in I} M_i
:::

be the linearization of $\lambda_{I,A}$. We claim that $\overline{\lambda_{I,A}}$ is inverse to $\alpha_{I,A}$. By definition of $\overline{\lambda_{I,A}}$ and Eqs.~{eq}`eq:defining-equation-associator-map-tensor-product_1` and
{eq}`eq:defining-equation-inverse-associator-map-tensor-product_1` one concludes

:::{math}
\overline{\lambda_{I,A}} \circ \alpha_{I,A} \circ \tau_I =
\overline{\lambda_{I,A}} \circ \tau_A \circ (\tau_a)_{a\in A} \circ \kappa_{I,A} =
\lambda_{I,A} \circ (\tau_a)_{a\in A} \circ \kappa_{I,A} = \tau_I \ .
:::

Since the image of $\tau_I$ generates $\bigotimes_{i\in I} M_i$ as an $R$-module, $\overline{\lambda_{I,A}}$ has to be left inverse to $\alpha_{I,A}$. Using Eqs.~{eq}`eq:defining-equation-associator-map-tensor-product_1` and
{eq}`eq:defining-equation-inverse-associator-map-tensor-product_1` again compute

:::{math}
\alpha_{I,A} \circ\overline{\lambda_{I,A}} \circ \tau_A \circ (\tau_a)_{a\in A} =
\alpha_{I,A} \circ \lambda_{I,A} \circ (\tau_a)_{a\in A} = \alpha_{I,A}\circ\tau_A\circ \kappa_{I,A}^{-1}
= \tau_A \circ (\tau_a)_{a\in A} \ .
:::

Since by \Crefthm:image-generating-system-canoncial-map-finite-tensor-product-generating-system
the image of $\tau_A \circ (\tau_a)_{a\in A}$ generates $\bigotimes_{a \in A} \bigotimes_{i \in I_a} M_i$, the equality

:::{math}
\alpha_{I,A} \circ\overline{\lambda_{I,A}}=\mathrm{id}_{\bigotimes_{a \in A} \bigotimes_{i \in I_a} M_i}
:::

follows and the proposition is proved.
:::



:::{prf:theorem} 
Let $(A_i)_{i\in I}$ be a family of $R$-algebras. Then the tensor product $A = \bigotimes_{i\in I} A_i$ carries in a natural way the structure of an $R$-algebra where the product map is defined by

:::{math}
\cdot : A \times A \to A , \enspace (\otimes_{i\in I} a_i , \otimes_{i\in I} b_i)\mapsto
\otimes_{i\in I} (a_i\cdot b_i) \ .
:::

In case each of the algebras $A_i$ is commutative, then $A$ is commutative as well. Likewise, if each $A_i$ is unital and $1_i$ denotes the unit element of $A_i$, then $A$ is unital with unit given by $1 = \otimes_{i\in I} 1_i$. One calls $A$ the *tensor product algebra* of the family of algebras $(A_i)_{i\in I}$.
:::



:::{prf:proof}

The map

:::{math}
\prod_{(i,k)\in I \times \{ 1,2\}} A_i \to A,\enspace (a_{i,k})_{(i,k) \in I\times \{1,2\}} \mapsto\otimes_{i\in I}(a_{i,1}\cdot a_{i,2})
:::

is multilinear by bilinearity of the product maps on the $A_i$ and multilinearity of $\tau_I$, so factors through a linear map $\mu: A \otimes A \cong \bigotimes_{(i,k)\in I\times \{1,2\}} A_i \to A$. Composition of $\mu$ with the canonical bilinear map $A \times A \to A\otimes A$ gives the product map $\cdot : A \times A\to A$ and shows that the product on $A$ is well-defined. By construction, the product map $\cdot$ is bilinear. Given $\otimes_{i\in I} a_i, \otimes_{i\in I} b_i, \otimes_{i\in I} c_i \in A$ one computes

:::{math}
\big( \otimes_{i\in I} a_i \cdot \otimes_{i\in I} b_i \big) \cdot \otimes_{i\in I} c_i = \otimes_{i\in I} ((a_i\cdot b_i)\cdot c_i) =
\otimes_{i\in I} (a_i\cdot( b_i\cdot c_i)) =
\otimes_{i\in I} a_i \cdot \big( \otimes_{i\in I} b_i \cdot \otimes_{i\in I} c_i\big) \ .
:::

This entails that the product on $A$ is associative. In the same way one shows that $A$ is commutive respectively unital if each of the $A_i$ is.
:::


\para As we have seen, the infinite tensor product construction works well for objects of algebraic categories like $R$-modules, vector spaces or $R$-algebras. As soon as a topologies compatible with the algebraic structure come in it becomes difficult and sometimes even impossible to construct or even define

\newpage
<!-- XXSEC_PREFIX_ENDXX\sectionInfinite tensor products -->

<!-- XXSEC_PREFIX_ENDXX\chapterC$^*$-Algebras -->

<!-- XXSEC_PREFIX_ENDXX\partFunctional Analysis -->

\bibliographylmlib
\bibliographystyleapalike \iheadBibliography
\ohead


<!-- XXSEC_DEF_SPLITTERXX\chapter*XXSEC_DEF_SPLITTERXXLicensingXXSEC_DEF_SPLITTERXX -->
<!-- XXSEC_PREFIX_BEGINXX\chapter*Licensing -->
(chapt:licenses_1)=
# Licensing
\addcontentslinetocpartLicensing\iheadLicensing
\oheadGNU FDL v1.3
\addcontentslinetocchapterGNU FDL v1.3
<!-- XXSEC_PREFIX_ENDXX\chapter*Licensing -->
