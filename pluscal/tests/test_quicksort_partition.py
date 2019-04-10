from textwrap import dedent


ALGORITHM = dedent("""\
    --algorithm quicksort_pivot
    variable A, lo in 1..N, hi in lo..N
    begin
      with piv \\in lo..(hi −1),
           B \\in { C \\n Perms(A) :
                  ( \\A i \\in 1..(lo − 1) \\U (hi + 1)..N : C[i] = A[i])
                ∧ ( \\A i \\in lo..piv, j \\in (piv + 1)..hi : C[i] ≤ C[j] ) }
      do
        pivot := piv;
        A : = B
      end with
    end algorithm""")
