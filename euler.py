import os
import subprocess
import time
import glob

# --- SETTINGS ---

source_dirs = {
    "C": "c_sources",
    "C++": "cpp_sources",
    "Java": "java_sources"
}

compilers = {
    "C": lambda f: ["gcc", f, "-o", f.replace(".c", ".out")],
    "C++": lambda f: ["g++", f, "-o", f.replace(".cpp", ".out")],
    "Java": lambda f: ["javac", f]
}

executors = {
    "C": lambda f: [f.replace(".c", ".out")],
    "C++": lambda f: [f.replace(".cpp", ".out")],
    "Java": lambda f: ["java", f.replace(".java", "")]
}


def run_and_time(cmd):
    start = time.time()
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    end = time.time()
    return result.stdout.strip(), result.stderr.strip(), end - start


def handle_language(lang, ext, problem_filter=None):
    print(f"\n--- Running {lang} Programs ---")
    pattern = f"Problem{problem_filter}.{ext}" if problem_filter else f"*.{ext}"
    files = glob.glob(os.path.join(source_dirs[lang], pattern))

    if not files:
        print("⚠️ No matching files found.")
        return

    for file in files:
        print(f"\n→ Running {os.path.basename(file)}")
        compile_cmd = compilers[lang](file)
        _, compile_err, _ = run_and_time(compile_cmd)
        if compile_err:
            print(f"❌ Compilation error:\n{compile_err}")
            continue

        exec_cmd = executors[lang](file)
        output, runtime_err, elapsed = run_and_time(exec_cmd)
        if runtime_err:
            print(f"⚠️ Runtime error:\n{runtime_err}")
        else:
            print(f"✅ Output: {output}")
            print(f"⏱ Time taken: {elapsed:.6f} seconds")


def display_menu():
    print("\n====== Project Euler Runner ======")
    print("1. Run C programs")
    print("2. Run C++ programs")
    print("3. Run Java programs")
    print("4. Run All Languages")
    print("0. Exit")
    choice = input("Select Language Option (0–4): ").strip()
    return choice


def get_problem_number():
    print("\n🔢 Enter problem number (e.g., 1 for Problem1), or press Enter to run all:")
    problem_input = input("Problem number: ").strip()
    return problem_input if problem_input else None


def main():
    while True:
        choice = display_menu()
        if choice == "0":
            print("👋 Exiting. Goodbye!")
            break
        elif choice in ["1", "2", "3", "4"]:
            problem_filter = get_problem_number()
            if choice == "1":
                handle_language("C", "c", problem_filter)
            elif choice == "2":
                handle_language("C++", "cpp", problem_filter)
            elif choice == "3":
                handle_language("Java", "java", problem_filter)
            elif choice == "4":
                for lang, ext in [("C", "c"), ("C++", "cpp"), ("Java", "java")]:
                    handle_language(lang, ext, problem_filter)
        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
