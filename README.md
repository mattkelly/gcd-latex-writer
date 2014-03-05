gcd-latex-writer
================

Write the [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) step-by-step in matrix form in LaTeX.

Requires `\usepackage{amsmath}`.

## Example

Computing gcd(6424608522503111, 3242940221833111):

```
\begin{multline*}
    \begin{pmatrix}
    6424608522503111 & 1 & 0 \\
    3242940221833111 & 0 & 1
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
    3181668300670000 & 1 & -1 \\
    3242940221833111 & 0 & 1
    \end{pmatrix}\\
    \rightarrow
    \begin{pmatrix}
    3181668300670000 & 1 & -1 \\
    61271921163111 & -1 & 2
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
    56800321351339 & 52 & -103 \\
    61271921163111 & -1 & 2
    \end{pmatrix}\\
    \rightarrow
    \begin{pmatrix}
    56800321351339 & 52 & -103 \\
    4471599811772 & -53 & 105
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
    3141123610075 & 688 & -1363 \\
    4471599811772 & -53 & 105
    \end{pmatrix}\\
    \rightarrow
    \begin{pmatrix}
    3141123610075 & 688 & -1363 \\
    1330476201697 & -741 & 1468
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
    480171206681 & 2170 & -4299 \\
    1330476201697 & -741 & 1468
    \end{pmatrix}\\
    \rightarrow
    \begin{pmatrix}
    480171206681 & 2170 & -4299 \\
    370133788335 & -5081 & 10066
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
    110037418346 & 7251 & -14365 \\
    370133788335 & -5081 & 10066
    \end{pmatrix}\\
    \rightarrow
    \begin{pmatrix}
    110037418346 & 7251 & -14365 \\
    40021533297 & -26834 & 53161
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
    29994351752 & 60919 & -120687 \\
    40021533297 & -26834 & 53161
    \end{pmatrix}\\
    \rightarrow
    \begin{pmatrix}
    29994351752 & 60919 & -120687 \\
    10027181545 & -87753 & 173848
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
    9939988662 & 236425 & -468383 \\
    10027181545 & -87753 & 173848
    \end{pmatrix}\\
    \rightarrow
    \begin{pmatrix}
    9939988662 & 236425 & -468383 \\
    87192883 & -324178 & 642231
    \end{pmatrix}
\end{multline*}
```
