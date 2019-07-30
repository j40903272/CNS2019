1. 

2.
python3 2.py
require : requests

3.
python3 3.py

4.
clang -I ~/klee_src/include -emit-llvm -c -g 4.c
klee 4.bc
file = ${ls -l klee-last | tail -n2 | head -n1}
ktest-tool klee-last/$file