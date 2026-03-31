# Python Concurrency — Multithreading & Multiprocessing

A practical collection of Python scripts demonstrating **multithreading** and **multiprocessing** from the ground up — covering basic usage, thread/process pools, CPU-bound tasks, and a real-world web scraping use case.

---

## 📁 File Overview

| File | Technique | Type | Key Concept |
|---|---|---|---|
| `multithreading.py` | `threading.Thread` | I/O-bound | Basic thread creation & joining |
| `adv_multi_threading.py` | `ThreadPoolExecutor` | I/O-bound | Thread pool with `executor.map` |
| `usecase_webscraping_threading.py` | `threading.Thread` | Real-world I/O | Concurrent web scraping |
| `multiprocessing_CPU.py` | `multiprocessing.Process` | CPU-bound | Parallel processes, timing |
| `adv_multi_processing.py` | `ProcessPoolExecutor` | CPU-bound | Process pool with `executor.map` |
| `fact_multi_processing.py` | `multiprocessing.Pool` | CPU-bound | Heavy computation (factorials) |

---

## 📄 Script Breakdown

### `multithreading.py` — Basic Multithreading
The starting point. Creates two threads manually — one prints numbers, one prints letters — and runs them concurrently using `threading.Thread`.

- `t1.start()` / `t2.start()` to launch threads
- `t1.join()` / `t2.join()` to wait for completion
- Measures total wall-clock time to demonstrate concurrency benefit

---

### `adv_multi_threading.py` — Thread Pool Executor
Upgrades the basic approach using `concurrent.futures.ThreadPoolExecutor` — the modern, cleaner way to manage a pool of worker threads.

- Simulates I/O delay with `time.sleep(1)` per task
- `max_workers=3` limits concurrent threads
- `executor.map()` distributes work across the pool automatically
- Returns results in the same order as input

---

### `usecase_webscraping_threading.py` — Real-World: Concurrent Web Scraping
A practical use case showing why threads are ideal for network I/O. Fetches three LangChain documentation pages simultaneously instead of one at a time.

- Uses `requests` to fetch each URL
- Parses HTML with `BeautifulSoup`
- Each URL gets its own thread — all fire in parallel
- Reports character count per page on completion

> **Why threads here?** Network requests spend most of their time waiting for a server response — threads let Python do other work during that wait.

---

### `multiprocessing_CPU.py` — Basic Multiprocessing (CPU-Bound)
Mirrors `multithreading.py` but for CPU-bound tasks. Spawns two separate processes — one computes squares, one computes cubes — running truly in parallel across CPU cores.

- Uses `multiprocessing.Process` directly
- Demonstrates that processes bypass Python's GIL
- Measures total execution time

> **Why not threads for this?** Python's GIL prevents true parallel execution of CPU-heavy code on threads. Processes get their own memory space and GIL, so they run on separate cores.

---

### `adv_multi_processing.py` — Process Pool Executor
The multiprocessing equivalent of `adv_multi_threading.py`. Uses `ProcessPoolExecutor` to distribute a list of squaring tasks across 3 worker processes.

- `max_workers=3` spawns up to 3 processes
- `executor.map()` handles task distribution and result collection
- `if __name__ == "__main__"` guard is required for safe process spawning on Windows/macOS

---

### `fact_multi_processing.py` — Heavy Computation with Process Pool
The most demanding script. Computes factorials of large numbers (5000–8000) in parallel using `multiprocessing.Pool` — a task that would be slow done sequentially.

- `sys.set_int_max_str_digits(100000)` raises Python's default integer-to-string limit for huge results
- `pool.map()` distributes numbers across all available CPU cores
- Benchmarks total time taken for parallel factorial computation

---

## 🧠 Threading vs Multiprocessing — Quick Reference

| | Multithreading | Multiprocessing |
|---|---|---|
| **Best for** | I/O-bound tasks (network, file, DB) | CPU-bound tasks (math, image, ML) |
| **Parallelism** | Concurrent (GIL limits true parallel) | True parallel (separate GIL per process) |
| **Memory** | Shared memory space | Separate memory per process |
| **Overhead** | Low | Higher (process spawn cost) |
| **Python GIL** | Affected | Not affected |
| **Use when** | Waiting on external resources | Crunching numbers / heavy computation |

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `threading` | Basic thread creation and management |
| `multiprocessing` | Process creation, Pool |
| `concurrent.futures` | High-level `ThreadPoolExecutor` / `ProcessPoolExecutor` |
| `requests` | HTTP requests for web scraping |
| `beautifulsoup4` | HTML parsing |
| `math` | Factorial computation |

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/Praveen23-kk/Muti_threading.git
cd Muti_threading
```

**2. Install dependencies**
```bash
pip install requests beautifulsoup4
```
> All other libraries (`threading`, `multiprocessing`, `concurrent.futures`, `math`) are part of the Python standard library — no install needed.

**3. Run any script**
```bash
python multithreading.py
python adv_multi_threading.py
python usecase_webscraping_threading.py
python multiprocessing_CPU.py
python adv_multi_processing.py
python fact_multi_processing.py
```

> ⚠️ On Windows/macOS, scripts using `multiprocessing` must be run as a file (not interactively in a REPL) due to the `if __name__ == "__main__"` requirement.

---

## 📌 Suggested Learning Order

1. `multithreading.py` — understand thread basics
2. `adv_multi_threading.py` — upgrade to thread pools
3. `usecase_webscraping_threading.py` — apply to a real use case
4. `multiprocessing_CPU.py` — understand process basics
5. `adv_multi_processing.py` — upgrade to process pools
6. `fact_multi_processing.py` — tackle heavy CPU workloads

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
