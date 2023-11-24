## CPU-Benchmark

`this is a cpu benchmark test program`

------

### Install

```bash
sudo apt install libgmp-dev libmpfr-dev libmpc-dev python3-pip gcc g++ gfortran mpich git
pip3 install gmpy2
git clone https://github.com/mapkkkk/benchmark.git
chmod -R 777 benchmark
cd benchmark
```

#### CPU single-core speed test

```bash
python3 cpu_single_core_speed_test.py
```

#### CPU multi-core speed test	(all threads)

```
gcc -Ofast -march=native -fopenmp -o cpu_muti_core_speed_test cpu_muti_core_speed_test.c
./cpu_muti_core_speed_test
```

