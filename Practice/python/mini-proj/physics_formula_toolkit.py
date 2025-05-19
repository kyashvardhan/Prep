#!/usr/bin/env python3
"""
physics_formula_toolkit.py

- Motion equations
- Newton’s 2nd law (Force)
- Kinetic Energy
- Potential Energy
- Work Done
- Pressure
- Wave speed
"""

def motion_equation():
    print("\n🧮 Equation of Motion (v = u + at)")
    u = float(input("Enter initial velocity u (m/s): "))
    a = float(input("Enter acceleration a (m/s²): "))
    t = float(input("Enter time t (s): "))
    v = u + a * t
    print(f"Final velocity v = {v:.2f} m/s")

def newtons_second_law():
    print("\n🧲 Newton's 2nd Law (F = m * a)")
    m = float(input("Enter mass m (kg): "))
    a = float(input("Enter acceleration a (m/s²): "))
    F = m * a
    print(f"Force F = {F:.2f} N (Newtons)")

def kinetic_energy():
    print("\n⚡ Kinetic Energy (KE = 0.5 * m * v²)")
    m = float(input("Enter mass m (kg): "))
    v = float(input("Enter velocity v (m/s): "))
    KE = 0.5 * m * v ** 2
    print(f"Kinetic Energy = {KE:.2f} J (Joules)")

def potential_energy():
    print("\n🪜 Potential Energy (PE = m * g * h)")
    m = float(input("Enter mass m (kg): "))
    h = float(input("Enter height h (m): "))
    g = 9.81  # gravitational acceleration
    PE = m * g * h
    print(f"Potential Energy = {PE:.2f} J (Joules)")

def work_done():
    print("\n🔨 Work Done (W = F * d)")
    F = float(input("Enter Force F (N): "))
    d = float(input("Enter displacement d (m): "))
    W = F * d
    print(f"Work Done = {W:.2f} J (Joules)")

def pressure():
    print("\n💨 Pressure (P = F / A)")
    F = float(input("Enter Force F (N): "))
    A = float(input("Enter Area A (m²): "))
    if A == 0:
        print("❌ Area can't be zero.")
        return
    P = F / A
    print(f"Pressure = {P:.2f} Pa (Pascals)")

def wave_speed():
    print("\n🌊 Wave Speed (v = f * λ)")
    f = float(input("Enter frequency f (Hz): "))
    wavelength = float(input("Enter wavelength λ (m): "))
    v = f * wavelength
    print(f"Wave speed = {v:.2f} m/s")

def show_menu():
    print("\n📘 Physics Formula Toolkit")
    print("1. Equation of Motion (v = u + at)")
    print("2. Newton's 2nd Law (F = m * a)")
    print("3. Kinetic Energy")
    print("4. Potential Energy")
    print("5. Work Done")
    print("6. Pressure")
    print("7. Wave Speed")
    print("0. Exit")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("\nChoose a formula (0 to exit): "))
            if choice == 1:
                motion_equation()
            elif choice == 2:
                newtons_second_law()
            elif choice == 3:
                kinetic_energy()
            elif choice == 4:
                potential_energy()
            elif choice == 5:
                work_done()
            elif choice == 6:
                pressure()
            elif choice == 7:
                wave_speed()
            elif choice == 0:
                print("👋 Exiting Physics Toolkit. Stay curious!")
                break
            else:
                print("❌ Invalid choice. Try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
